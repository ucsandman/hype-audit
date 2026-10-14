#!/usr/bin/env python3
"""Push the hype-audit tree to ucsandman/hype-audit via the GitHub
git-database API, using the custom.github connector surrogate.

The connector credential never touches this script: authd swaps the surrogate
on egress. Publishes exactly what is committed at local HEAD, parented to the
remote main HEAD so clones fast-forward with a plain `git pull` (no force).
Re-fetches the remote HEAD at push time; never force-pushes.
"""
import base64
import json
import subprocess
import sys
import urllib.request
import urllib.error

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
import dynamic_credentials as dc  # noqa: E402

OWNER, REPO = "ucsandman", "hype-audit"
API = f"https://api.github.com/repos/{OWNER}/{REPO}"
REPO_DIR = "/home/hatch/workspace/hype-audit"
HEADERS = {
    "User-Agent": "hype-audit-publish",
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/json",
}


def api(method, url, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=HEADERS)
    dc.add_surrogate_to_request(req, "custom.github", allowed_hosts=["api.github.com"])
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        body = resp.read()
        return resp.status, (json.loads(body.decode()) if body else None)
    except urllib.error.HTTPError as e:
        detail = e.read(500).decode("utf-8", "replace")[:300]
        raise SystemExit(f"HTTP {e.code} on {method} {url}\n{detail}")


def git(*args):
    return subprocess.run(
        ["git", "-C", REPO_DIR, *args], capture_output=True, check=True
    ).stdout


def main():
    _, repo = api("GET", API)
    print("repo:", repo["full_name"])
    _, existing = api("GET", API + "/git/refs/heads/main")
    remote_head = existing["object"]["sha"]
    print("remote HEAD:", remote_head[:7])

    files = git("ls-files").decode().splitlines()
    assert files, "no files listed"
    print(f"publishing {len(files)} files")

    tree_entries = []
    for p in files:
        content = git("show", f"HEAD:{p}")
        _, blob = api(
            "POST",
            API + "/git/blobs",
            {"content": base64.b64encode(content).decode(), "encoding": "base64"},
        )
        tree_entries.append(
            {"path": p, "mode": "100644", "type": "blob", "sha": blob["sha"]}
        )
    print("blobs created")

    message = (
        sys.argv[1]
        if len(sys.argv) > 1
        else git("log", "-1", "--format=%B").decode().strip()
    )
    _, tree = api("POST", API + "/git/trees", {"tree": tree_entries})
    _, commit = api(
        "POST",
        API + "/git/commits",
        {
            "message": message,
            "tree": tree["sha"],
            "parents": [remote_head],
            "author": {
                "name": "wes",
                "email": "ucsandman@users.noreply.github.com",
            },
        },
    )
    print("commit:", commit["sha"][:7])

    _, ref = api(
        "PATCH", API + "/git/refs/heads/main", {"sha": commit["sha"], "force": False}
    )
    print("ref:", ref["ref"], "->", commit["sha"][:7])


if __name__ == "__main__":
    main()
