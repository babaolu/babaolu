"""
update_profile.py
─────────────────
Weekly GitHub Action script that:
  1. Fetches all public repos via GitHub API (with pagination)
  2. Gathers per-repo detail: description, topics, languages, README snippet
  3. Sends the data to Gemini, along with the current README for structure reference
  4. Gemini rewrites the ENTIRE README — every section updated from repo data
"""

import os
import json
import textwrap
import requests
from datetime import datetime, timezone

# ── Config ────────────────────────────────────────────────────────────────────
GITHUB_USER      = os.environ["GITHUB_USER"]
GITHUB_TOKEN     = os.environ["GITHUB_TOKEN"]
GEMINI_API_KEY   = os.environ["GEMINI_API_KEY"]

README_PATH   = "README.md"

# How many repos to spotlight (most recent first)
TOP_N_RECENT  = 6
# How many repos to analyse for background context
MAX_CONTEXT   = 20
# Max chars to pull from each repo's own README for context
README_CHARS  = 400

GH_HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

# ── GitHub helpers ────────────────────────────────────────────────────────────
def gh_get(url: str) -> dict | list:
    r = requests.get(url, headers=GH_HEADERS, timeout=15)
    r.raise_for_status()
    return r.json()

def fetch_all_repos() -> list[dict]:
    repos, page = [], 1
    while True:
        batch = gh_get(
            f"https://api.github.com/users/{GITHUB_USER}/repos"
            f"?type=public&per_page=100&page={page}"
        )
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos

def fetch_languages(full_name: str) -> list[str]:
    try:
        langs = gh_get(f"https://api.github.com/repos/{full_name}/languages")
        # Return top 3 languages by bytes
        return sorted(langs, key=langs.get, reverse=True)[:3]
    except Exception:
        return []

def fetch_repo_readme_snippet(full_name: str) -> str:
    """Try to grab the first few hundred chars of a repo's README."""
    try:
        import base64
        data = gh_get(f"https://api.github.com/repos/{full_name}/readme")
        content = base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
        # Strip markdown noise for the LLM
        lines = [l for l in content.splitlines() if l.strip() and not l.startswith("#")]
        return " ".join(lines)[:README_CHARS]
    except Exception:
        return ""

def build_repo_summary(repo: dict) -> dict:
    full_name = repo["full_name"]
    return {
        "name":        repo["name"],
        "url":         repo["html_url"],
        "description": repo.get("description") or "",
        "topics":      repo.get("topics") or [],
        "stars":       repo.get("stargazers_count", 0),
        "forks":       repo.get("forks_count", 0),
        "language":    repo.get("language") or "",
        "languages":   fetch_languages(full_name),
        "pushed_at":   repo.get("pushed_at") or "",
        "readme_hint": fetch_repo_readme_snippet(full_name),
    }

# ── Prepare data for Gemini ───────────────────────────────────────────────────
def collect_repo_data(repos: list[dict]) -> tuple[list[dict], list[dict]]:
    """Return (recent_repos, context_repos) as summarised dicts."""
    sorted_repos = sorted(
        repos,
        key=lambda r: r.get("pushed_at") or "",
        reverse=True,
    )

    print(f"  Building detail for top {TOP_N_RECENT} recent repos …")
    recent  = [build_repo_summary(r) for r in sorted_repos[:TOP_N_RECENT]]

    # Remaining repos for broader context (lightweight — no README fetch)
    context = []
    for r in sorted_repos[TOP_N_RECENT : MAX_CONTEXT]:
        context.append({
            "name":        r["name"],
            "description": r.get("description") or "",
            "language":    r.get("language") or "",
            "topics":      r.get("topics") or [],
            "stars":       r.get("stargazers_count", 0),
        })

    return recent, context

# ── Call Gemini API ───────────────────────────────────────────────────────────
def read_current_readme() -> str:
    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def call_gemini(recent: list[dict], context: list[dict], total: int, current_readme: str) -> str:
    recent_text  = json.dumps(recent,  indent=2)
    context_text = json.dumps(context, indent=2)

    prompt = textwrap.dedent(f"""
        You are maintaining a developer's GitHub profile README.
        Your job is to rewrite the ENTIRE README from scratch, using the
        repository data below as the source of truth for every section.

        Use the current README as a structural template only — mirror its
        sections and formatting style (headings, bullet lists, tables, etc.)
        but replace ALL content with what you discover from the repo data.
        Nothing in the current README should carry over unchanged unless the
        repo data confirms it still belongs there.

        Rewrite rules:
        - Header / tagline: keep the developer's name, update the tagline if
          the repos suggest a more accurate description.
        - Intro paragraph: written in first person, genuine and specific.
          Reflect what the recent repos reveal about current focus.
        - Core focus areas: derive these entirely from the repos.
          Remove any area that has no repo evidence; add any that do.
        - Selected projects: pull from the {len(recent)} most recent repos.
          Each entry should have a one-line description and a stack note.
          Do not mention repos that have no description and no README content.
        - Technical skills: infer from languages, topics, and README hints
          across all repos. Update every sub-list accordingly.
        - Contact: preserve all links and placeholders exactly as they appear
          in the current README — do not change or remove any of them.
        - Tone: professional but human. No filler phrases like "passionate about".
        - Output ONLY the final Markdown. No commentary, no code fences.

        === CURRENT README (structure/style reference only) ===
        {current_readme}

        === RECENT REPOS (highest weight — {len(recent)} most recently pushed) ===
        {recent_text}

        === OLDER REPOS (background context — {total - len(recent)} repos) ===
        {context_text}

        Last updated: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}
    """).strip()

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "maxOutputTokens": 2048
        }
    }

    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=60,
    )
    response.raise_for_status()
    
    # Parse the text from the Gemini response payload
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

# ── Write full README ─────────────────────────────────────────────────────────
def update_readme(new_content: str) -> None:
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content.strip() + "\n")
    print("✅  README.md fully rewritten.")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print(f"📡  Fetching repos for: {GITHUB_USER}")
    repos = fetch_all_repos()
    print(f"    Found {len(repos)} public repositories.")

    recent, context = collect_repo_data(repos)

    current_readme = read_current_readme()
    print("🤖  Asking Gemini to rewrite the full profile README …")
    new_readme = call_gemini(recent, context, total=len(repos), current_readme=current_readme)

    update_readme(new_readme)

if __name__ == "__main__":
    main()
