"""
update_profile.py
─────────────────
Weekly GitHub Action script that:
  1. Fetches all public repos (and recently pushed external/org repos)
  2. Gathers rich per-repo detail: description, topics, languages,
     full commit history summary (filtered by author), and README extract
  3. Sends everything to Gemini, which rewrites the ENTIRE README.
"""

import os
import json
import textwrap
import requests
import base64
from datetime import datetime, timezone

# ── Config ────────────────────────────────────────────────────────────────────
GITHUB_USER       = os.environ["GITHUB_USER"]
GITHUB_TOKEN      = os.environ["GITHUB_TOKEN"]
GEMINI_API_KEY    = os.environ["GEMINI_API_KEY"]

README_PATH = "README.md"

# Repos to show in "Selected projects" — always the N most recently pushed
TOP_N_SPOTLIGHT = 6

# Additional repos fed to Gemini as background context
MAX_CONTEXT     = 20

# How much of each repo's own README to extract (chars).
README_CHARS    = 1200

# How many recent commits to summarise per spotlight repo
COMMITS_LIMIT   = 10

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
    """Fetch all public repositories owned by the user."""
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

def fetch_external_contributions(existing_repo_names: set) -> list[dict]:
    """
    Look through the user's recent activity stream to find external 
    repositories (e.g., organizations) they have recently pushed to.
    """
    external_repos = []
    seen = set(existing_repo_names)
    page = 1

    # The Events API typically caps at 300 events (3 pages of 100)
    while page <= 3:
        try:
            events = gh_get(
                f"https://api.github.com/users/{GITHUB_USER}/events"
                f"?per_page=100&page={page}"
            )
            if not events:
                break
        except Exception:
            break

        for event in events:
            if event.get("type") == "PushEvent":
                repo_name = event.get("repo", {}).get("name")
                
                # If it's a new repo and NOT in the user's personal namespace
                if repo_name and repo_name not in seen:
                    if not repo_name.lower().startswith(f"{GITHUB_USER.lower()}/"):
                        seen.add(repo_name)
                        try:
                            print(f"  ↳ Discovered recent external contribution: {repo_name}")
                            repo_data = gh_get(f"https://api.github.com/repos/{repo_name}")
                            external_repos.append(repo_data)
                        except Exception:
                            pass # Might fail if it's a private org repo your token can't read
        page += 1

    return external_repos

def fetch_languages(full_name: str) -> dict[str, int]:
    """Return {language: bytes} dict, empty on failure."""
    try:
        return gh_get(f"https://api.github.com/repos/{full_name}/languages")
    except Exception:
        return {}

def fetch_readme_text(full_name: str) -> str:
    """Decode a repo's README and return a clean text extract."""
    try:
        data    = gh_get(f"https://api.github.com/repos/{full_name}/readme")
        content = base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
        lines   = [
            l.strip() for l in content.splitlines()
            if l.strip() and not l.startswith("#")
        ]
        return " ".join(lines)[:README_CHARS]
    except Exception:
        return ""

def fetch_recent_commits(full_name: str) -> list[str]:
    """Return the last N commit messages by THIS USER for the default branch."""
    try:
        # Added ?author={GITHUB_USER} to ensure we only summarize YOUR work
        commits = gh_get(
            f"https://api.github.com/repos/{full_name}/commits"
            f"?author={GITHUB_USER}&per_page={COMMITS_LIMIT}"
        )
        return [c["commit"]["message"].splitlines()[0] for c in commits]
    except Exception:
        return []

def build_spotlight_entry(repo: dict) -> dict:
    """Rich data dict for a featured project."""
    full_name = repo["full_name"]
    langs     = fetch_languages(full_name)
    top_langs = sorted(langs, key=langs.get, reverse=True)[:5]

    return {
        "name":           repo["name"],
        "url":            repo["html_url"],
        "description":    repo.get("description") or "",
        "topics":         repo.get("topics") or [],
        "stars":          repo.get("stargazers_count", 0),
        "forks":          repo.get("forks_count", 0),
        "primary_language": repo.get("language") or "",
        "all_languages":  top_langs,
        "pushed_at":      repo.get("pushed_at") or "",
        "created_at":     repo.get("created_at") or "",
        "readme_extract": fetch_readme_text(full_name),
        "recent_commits": fetch_recent_commits(full_name),
    }

def build_context_entry(repo: dict) -> dict:
    """Lightweight dict for background repos (no extra API calls)."""
    return {
        "name":        repo["name"],
        "description": repo.get("description") or "",
        "language":    repo.get("language") or "",
        "topics":      repo.get("topics") or [],
        "stars":       repo.get("stargazers_count", 0),
        "pushed_at":   repo.get("pushed_at") or "",
    }

# ── Collect and organise repo data ───────────────────────────────────────────
def collect_repo_data(repos: list[dict]) -> tuple[list[dict], list[dict]]:
    sorted_repos = sorted(
        repos,
        key=lambda r: r.get("pushed_at") or "",
        reverse=True,
    )

    print(f"  Fetching rich data for top {TOP_N_SPOTLIGHT} active repos …")
    spotlight = [build_spotlight_entry(r) for r in sorted_repos[:TOP_N_SPOTLIGHT]]

    print(f"  Collecting context for up to {MAX_CONTEXT} additional repos …")
    context = [
        build_context_entry(r)
        for r in sorted_repos[TOP_N_SPOTLIGHT : TOP_N_SPOTLIGHT + MAX_CONTEXT]
    ]

    return spotlight, context

# ── Read existing README ──────────────────────────────────────────────────────
def read_current_readme() -> str:
    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# ── Call Gemini API ───────────────────────────────────────────────────────────
def call_gemini(spotlight: list[dict], context: list[dict],
                total: int, current_readme: str) -> str:

    spotlight_text = json.dumps(spotlight, indent=2)
    context_text   = json.dumps(context,   indent=2)
    now            = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    prompt = textwrap.dedent(f"""
        You are rewriting a developer's GitHub profile README.
        Use the repository data below as the sole source of truth.
        The current README is a formatting/structure reference only.

        ── REWRITE RULES ────────────────────────────────────────────────────

        HEADER & TAGLINE
        • Keep the developer's name exactly.
        • Update the one-line tagline to match what the repos reveal.

        INTRO PARAGRAPH
        • First person, 3–4 sentences, specific to actual projects.
        • Name recent repos naturally — no filler like "passionate about".

        CORE FOCUS AREAS
        • Derive entirely from repos. Add/remove areas to match the evidence.
        • Each area gets 2–3 bullet points describing concrete work done.

        SELECTED PROJECTS  ← most important section
        • Include ALL {len(spotlight)} spotlight repos, even if unchanged since
          last week. This section must always reflect the {len(spotlight)} most
          recently pushed repos — it is NOT a "what changed this week" list.
        • Each project MUST have:
            - A bold project name linked to its URL
            - A description paragraph of AT LEAST 30 words that explains
              what the project does, why it exists, and what makes it
              technically interesting. Use the readme_extract and
              recent_commits fields to write this — do not just restate
              the one-line description.
            - A "Stack:" line listing languages and key technologies.
        • If a repo has an empty readme_extract, infer from its name,
          description, topics, and commit messages — still write 30+ words.

        TECHNICAL SKILLS
        • Infer from all_languages, topics, and readme_extracts.
        • Update every sub-list; remove anything with no repo evidence.

        CONTACT
        • Copy the Contact section from the current README character-for-
          character. Do not add, remove, or alter any line in it.

        TONE  professional but human; no buzzwords or vague superlatives.

        OUTPUT  Markdown only — no preamble, no code fences, nothing else.

        ── DATA ─────────────────────────────────────────────────────────────

        SPOTLIGHT REPOS — {len(spotlight)} most recently pushed (highest weight):
        {spotlight_text}

        BACKGROUND REPOS — older / supporting context:
        {context_text}

        Total repos analyzed: {total}
        Profile owner: {GITHUB_USER}
        Today's date: {now}

        CURRENT README (structure reference only):
        {current_readme}
    """).strip()

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "maxOutputTokens": 8192
        }
    }

    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=90,
    )
    response.raise_for_status()
    
    response_data = response.json()
    candidate = response_data.get("candidates", [{}])[0]
    
    finish_reason = candidate.get("finishReason", "UNKNOWN")
    if finish_reason != "STOP":
        print(f"⚠️ WARNING: Gemini stopped generating early. Reason: {finish_reason}")
    
    try:
        return candidate["content"]["parts"][0]["text"]
    except KeyError:
        print("❌ ERROR: Could not extract text from Gemini response.")
        print(f"Full response debug: {json.dumps(response_data, indent=2)}")
        return ""

# ── Write README ──────────────────────────────────────────────────────────────
def update_readme(content: str) -> None:
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("✅  README.md fully rewritten.")

# ── Entry point ───────────────────────────────────────────────────────────────
def main():
    print(f"📡  Fetching personal repos for: {GITHUB_USER}")
    personal_repos = fetch_all_repos()
    print(f"    Found {len(personal_repos)} personal public repositories.")

    personal_repo_names = {r.get("full_name") for r in personal_repos}
    
    print(f"📡  Checking recent events for external contributions...")
    external_repos = fetch_external_contributions(personal_repo_names)

    all_repos = personal_repos + external_repos

    spotlight, context = collect_repo_data(all_repos)

    current_readme = read_current_readme()
    print("🤖  Asking Gemini to rewrite the README …")
    new_readme = call_gemini(spotlight, context,
                             total=len(all_repos),
                             current_readme=current_readme)
    update_readme(new_readme)

if __name__ == "__main__":
    main()
