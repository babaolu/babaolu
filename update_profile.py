"""
update_profile.py
─────────────────
Weekly GitHub Action script that:
  1. Fetches all public repos via GitHub API (with pagination)
  2. Gathers per-repo detail: description, topics, languages, README snippet
  3. Sends the data to Gemini to write a compelling developer profile
  4. Injects the result between markers in the profile README.md
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
START_MARKER  = ""
END_MARKER    = ""

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
def call_gemini(recent: list[dict], context: list[dict], total: int) -> str:
    recent_text  = json.dumps(recent,  indent=2)
    context_text = json.dumps(context, indent=2)

    prompt = textwrap.dedent(f"""
        You are writing the "About me" section for a GitHub profile README.
        The owner of this profile is a developer. Use the repository data below
        to infer who they are, what they build, and what they care about.

        Guidelines:
        - Write in first person, friendly and genuine — not a boring CV.
        - Highlight what the recent projects reveal about current focus/skills.
        - Mention specific project names as natural examples, not a dry list.
        - Identify patterns across all repos (themes, tech stacks, domains).
        - Keep it concise: roughly 120–180 words of prose.
        - After the prose, add a "🔧 Current tech focus" line with 4–6 emoji-tagged
          technologies or domains, derived from the data.
        - End with a short "📌 Recently shipped" section: a Markdown table
          (columns: Project | What it does | Stack) for the {len(recent)} most
          recent repos.
        - Do NOT add a title heading — the README already has one.
        - Output only the Markdown content, nothing else.

        === RECENT REPOS (most important — give these most weight) ===
        {recent_text}

        === OLDER REPOS (background context, {total - len(recent)} total public repos) ===
        {context_text}
    """).strip()

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "maxOutputTokens": 1024
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

# ── Inject into README ────────────────────────────────────────────────────────
def update_readme(new_block: str) -> None:
    if not os.path.exists(README_PATH):
        text = f"# {GITHUB_USER}\n\n{START_MARKER}\n{END_MARKER}\n"
    else:
        with open(README_PATH, "r", encoding="utf-8") as f:
            text = f.read()

    if START_MARKER not in text:
        text = text.rstrip("\n") + f"\n\n{START_MARKER}\n{END_MARKER}\n"

    start_idx = text.index(START_MARKER) + len(START_MARKER)
    end_idx   = text.index(END_MARKER)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    updated = (
        text[:start_idx]
        + f"\n\n\n"
        + new_block.strip()
        + "\n\n"
        + text[end_idx:]
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print("✅  README.md updated.")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print(f"📡  Fetching repos for: {GITHUB_USER}")
    repos = fetch_all_repos()
    print(f"    Found {len(repos)} public repositories.")

    recent, context = collect_repo_data(repos)

    print("🤖  Asking Gemini to write the profile …")
    profile_md = call_gemini(recent, context, total=len(repos))

    update_readme(profile_md)

if __name__ == "__main__":
    main()
