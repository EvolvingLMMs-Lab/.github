#!/usr/bin/env python3
import json
import os
import re
import urllib.request


README_PATH = "profile/README.md"
HEADING_PATTERN = re.compile(
    r"^(#{3,4} \[[^\]]+\]\(https://github\.com/([^/\s)]+)/([^/\s)]+)\) ⭐ )([0-9.]+k?)",
    re.MULTILINE,
)


def format_stars(count):
    if count >= 1000:
        value = count / 1000
        if value >= 10 or value.is_integer():
            return f"{value:.0f}k"
        return f"{value:.1f}k"
    return str(count)


def fetch_stars(owner, repo, token):
    request = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "readme-star-updater",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    return int(data["stargazers_count"])


def main():
    token = os.environ["GITHUB_TOKEN"]

    with open(README_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    cache = {}

    def replace(match):
        prefix, owner, repo, _old_value = match.groups()
        key = (owner, repo)
        if key not in cache:
            cache[key] = format_stars(fetch_stars(owner, repo, token))
        return f"{prefix}{cache[key]}"

    updated = HEADING_PATTERN.sub(replace, content)

    if updated != content:
        with open(README_PATH, "w", encoding="utf-8") as file:
            file.write(updated)


if __name__ == "__main__":
    main()
