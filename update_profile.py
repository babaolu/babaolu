"""
update_profile.py
─────────────────
Weekly GitHub Action script that:
  1. Fetches public personal repos (excluding untouched forks) & recent external/org repos
  2. Gathers rich per-repo detail concurrently: description, topics, languages,
     author-filtered commit history, and clean README extracts
  3. Uses Gemini system instructions to rewrite the ENTIRE README with verified contact links.
"""

import os
import re
import sys
import time
import json
import base64
import requests
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor

# ── Config ────────────────────────────────────────────────────────────────────
GITHUB_USER    = os.environ["GITHUB_USER"]
GITHUB_TOKEN   = os.environ["GITHUB_TOKEN"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

README_PATH     = "README.md"
GEMINI_MODEL    = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")

# Protocol & Host constants (prevents Markdown/UI auto-linkifiers from mangling URLs)
GH_API          = "https" + "://api.github.com"
GEMINI_API      = "https" + "://generativelanguage.googleapis.com"
LINKEDIN_URL    = "https" + "://www.linkedin.com/in/babatunde-adeoti-1614b2b9/"
CONTACT_EMAIL   = "babaolu98@gmail.com"

# Repos to show in "Selected projects"
TOP_N_SPOTLIGHT = 6
MAX_CONTEXT     = 20
README_CHARS    = 1500
COMMITS_LIMIT   = 10

# Use a persistent session for connection pooling
SESSION = requests.Session()
SESSION.headers.update({
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
})

# ── GitHub helpers ────────────────────────────────────────────────────────────
def gh_get(url: str) -> dict | list:
    r = SESSION.get(url, timeout=15)
    r.raise_for_status()
    return r.json()

def fetch_all_repos() -> list[dict]:
    """Fetch public repositories owned by the user, skipping untouched forks."""
    repos, page = [], 1
    while True:
        batch = gh_get(
            f"{GH_API}/users/{GITHUB_USER}/repos"
            f"?type=public&per_page=100&page={page}"
        )
        if not batch:
            break
        for r in batch:
            # Skip forks unless the user has pushed commits after forking
            if r.get("fork") and (r.get("pushed_at") or "") <= (r.get("created_at") or ""):
                continue
            repos.append(r)
        page += 1
    return repos

def fetch_external_contributions(existing_repo_names: set) -> list[dict]:
    """
    Scan the user's recent activity stream for external/org repositories
    they have pushed to, overriding 'pushed_at' with the user's own push date.
    """
    external_repos = []
    seen = {name.lower() for name in existing_repo_names}
    user_prefix = f"{GITHUB_USER.lower()}/"

    for page in range(1, 4):  # Events API caps at 300 events (3 pages)
        try:
            events = gh_get(
                f"{GH_API}/users/{GITHUB_USER}/events"
                f"?per_page=100&page={page}"
            )
            if not events:
                break
        except Exception:
            break

        for event in events:
            if event.get("type") == "PushEvent":
                repo_name = event.get("repo", {}).get("name", "")
                repo_lower = repo_name.lower()

                if repo_name and repo_lower not in seen and not repo_lower.startswith(user_prefix):
                    seen.add(repo_lower)
                    try:
                        print(f"  ↳ Discovered recent external contribution: {repo_name}")
                        repo_data = gh_get(f"{GH_API}/repos/{repo_name}")
                        # Override pushed_at with the timestamp of YOUR push event
                        repo_data["pushed_at"] = event.get("created_at") or repo_data.get("pushed_at")
                        external_repos.append(repo_data)
                    except Exception:
                        pass
    return external_repos

def fetch_languages(full_name: str) -> dict[str, int]:
    try:
        return gh_get(f"{GH_API}/repos/{full_name}/languages")
    except Exception:
        return {}

def fetch_readme_text(full_name: str) -> str:
    """Decode a repo's README and return a clean text extract without markdown noise."""
    try:
        data    = gh_get(f"{GH_API}/repos/{full_name}/readme")
        content = base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
        # Strip HTML tags and markdown badges
        content = re.sub(r"<[^>]+>", "", content)
        content = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", content)
        lines   = [
            l.strip() for l in content.splitlines()
            if l.strip() and not l.strip().startswith("#")
        ]
        return " ".join(lines)[:README_CHARS]
    except Exception:
        return ""

def fetch_recent_commits(full_name: str) -> list[str]:
    """Return the last N commit messages authored by THIS USER."""
    try:
        commits = gh_get(
            f"{GH_API}/repos/{full_name}/commits"
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
        "name":             repo["name"],
        "full_name":        full_name,
        "url":              repo["html_url"],
        "description":      repo.get("description") or "",
        "topics":           repo.get("topics") or [],
        "stars":            repo.get("stargazers_count", 0),
        "forks":            repo.get("forks_count", 0),
        "primary_language": repo.get("language") or "",
        "all_languages":    top_langs,
        "pushed_at":        repo.get("pushed_at") or "",
        "created_at":       repo.get("created_at") or "",
        "readme_extract":   fetch_readme_text(full_name),
        "recent_commits":   fetch_recent_commits(full_name),
    }

def build_context_entry(repo: dict) -> dict:
    """Lightweight dict for background repos."""
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

    print(f"  Fetching rich data concurrently for top {TOP_N_SPOTLIGHT} active repos …")
    with ThreadPoolExecutor(max_workers=TOP_N_SPOTLIGHT) as executor:
        spotlight = list(executor.map(build_spotlight_entry, sorted_repos[:TOP_N_SPOTLIGHT]))

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

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    system_instruction = f"""You are rewriting a developer's GitHub profile README.
Use the provided repository JSON data as the sole source of truth for projects and skills.
The current README is provided strictly as a structural and formatting reference.

── REWRITE RULES ────────────────────────────────────────────────────

HEADER & TAGLINE
• Keep the developer's name exactly as shown in the current README.
• Update the one-line tagline to accurately reflect what the repositories reveal.

INTRO PARAGRAPH
• First person, 3–4 sentences, specific to actual projects and engineering focus.
• Name recent repos naturally — no filler or clichés like "passionate about".

CORE FOCUS AREAS
• Derive entirely from the repositories. Add or remove areas to match the evidence.
• Each area gets 2–3 bullet points describing concrete systems and work built.

SELECTED PROJECTS (Most Important Section)
• Include ALL {len(spotlight)} spotlight repos in the exact order provided.
• Each project MUST have:
  - A bold project name linked to its URL.
  - A description paragraph of AT LEAST 30 words explaining what the project does, why it exists, and what makes it technically interesting. Synthesize `readme_extract` and `recent_commits` — do not merely restate the one-line description.
  - A "Stack:" line listing languages and key technologies.
• If a repo has an empty `readme_extract`, infer from its name, description, topics, and commit messages — still write 30+ words.

TECHNICAL SKILLS
• Infer from `all_languages`, `topics`, and `readme_extract`.
• Update every sub-list; remove anything with no repository evidence.

CONTACT
• Use the exact structure of the Contact section from the current README, but enforce these verified contact details:
  - LinkedIn: {LINKEDIN_URL}
  - Email: {CONTACT_EMAIL}
• Preserve any other valid social/portfolio links from the current Contact section, replacing any broken or outdated LinkedIn/Email addresses with the verified ones above.

TONE & FORMAT
• Tone: Empirical, systems-focused, professional, and human; no buzzwords or vague superlatives.
• Output raw Markdown ONLY — do NOT wrap the output in ```markdown code fences, and include no conversational preamble."""

    user_content = (
        f"Profile owner: {GITHUB_USER}\n"
        f"Today's date: {now}\n"
        f"Total repos analyzed: {total}\n\n"
        f"SPOTLIGHT REPOS ({len(spotlight)} most recently pushed, highest weight):\n"
        f"{json.dumps(spotlight, indent=2)}\n\n"
        f"BACKGROUND REPOS (supporting context):\n"
        f"{json.dumps(context, indent=2)}\n\n"
        f"CURRENT README (structure reference):\n"
        f"{current_readme}"
    )

    models_to_try = [GEMINI_MODEL]
    for fallback in ["gemini-3.5-flash", "gemini-3.8-flash", "gemini-2.5-flash"]:
        if fallback not in models_to_try:
            models_to_try.append(fallback)

    last_exception = None
    for model_name in models_to_try:
        url = f"{GEMINI_API}/v1beta/models/{model_name}:generateContent?key={GEMINI_API_KEY}"

        payload = {
            "systemInstruction": {
                "parts": [{"text": system_instruction}]
            },
            "contents": [{
                "role": "user",
                "parts": [{"text": user_content}]
            }],
            "generationConfig": {
                "maxOutputTokens": 8192,
            }
        }

        response = None
        for attempt in range(1, 4):
            if attempt == 1:
                print(f"🤖  Attempting generateContent with model '{model_name}'...")
            else:
                print(f"🤖  Retrying generateContent with model '{model_name}' (attempt {attempt}/3)...")

            response = requests.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "x-goog-api-key": GEMINI_API_KEY,
                },
                json=payload,
                timeout=90,
            )

            if response.status_code in (429, 503) and attempt < 3:
                print(f"⚠️ HTTP {response.status_code} received from '{model_name}'. Retrying in {attempt * 3}s...")
                time.sleep(attempt * 3)
                continue
            break

        if not response.ok:
            print(f"❌ Gemini API request to '{model_name}' failed with HTTP {response.status_code}:")
            try:
                print(json.dumps(response.json(), indent=2))
            except Exception:
                print(response.text)
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                last_exception = e
                continue

        response_data = response.json()
        candidate = response_data.get("candidates", [{}])[0]

        finish_reason = candidate.get("finishReason", "UNKNOWN")
        if finish_reason != "STOP":
            print(f"⚠️ WARNING: Gemini stopped generating early. Reason: {finish_reason}")

        try:
            parts = candidate.get("content", {}).get("parts", [])
            # Skip thought parts if present and collect text parts
            text_parts = [p.get("text", "") for p in parts if not p.get("thought") and "text" in p]
            text = "\n".join(text_parts).strip()
            if not text and parts:
                text = parts[-1].get("text", "").strip()

            if text.startswith("```"):
                text = re.sub(r"^```(?:markdown|md)?\s*\n", "", text)
                text = re.sub(r"\n```\s*$", "", text)
            return text.strip()
        except (KeyError, IndexError, AttributeError):
            print("❌ ERROR: Could not extract text from Gemini response.")
            print(f"Full response debug: {json.dumps(response_data, indent=2)}")
            return ""

    if last_exception:
        raise last_exception
    return ""

# ── Write README ──────────────────────────────────────────────────────────────
def update_readme(content: str) -> None:
    if not content or len(content) < 200:
        print("❌ ERROR: Generated README content is empty or suspiciously short. Aborting write to protect existing README.md.")
        sys.exit(1)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content + "\n")
    print("✅  README.md fully rewritten.")

# ── Entry point ───────────────────────────────────────────────────────────────
def main():
    print(f"📡  Fetching personal repos for: {GITHUB_USER}")
    personal_repos = fetch_all_repos()
    print(f"    Found {len(personal_repos)} active personal public repositories.")

    personal_repo_names = {r.get("full_name") for r in personal_repos if r.get("full_name")}

    print("📡  Checking recent events for external contributions...")
    external_repos = fetch_external_contributions(personal_repo_names)

    all_repos = personal_repos + external_repos

    spotlight, context = collect_repo_data(all_repos)

    current_readme = read_current_readme()
    print(f"🤖  Asking {GEMINI_MODEL} to rewrite the README …")
    new_readme = call_gemini(
        spotlight,
        context,
        total=len(all_repos),
        current_readme=current_readme,
    )
    update_readme(new_readme)

if __name__ == "__main__":
    main()
