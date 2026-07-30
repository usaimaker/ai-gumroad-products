#!/usr/bin/env python3
"""Store the Gumroad API token as a GitHub Actions secret for ai-gumroad-products.

Usage:
    GUMROAD_TOKEN=xxxx python set_gumroad_secret.py
  or
    python set_gumroad_secret.py xxxx

Encrypts with the repo's libsodium public key (SealedBox) and writes the
GUMROAD_TOKEN secret. Requires `pynacl` (pip install pynacl).
"""
import os
import sys
import json
import base64
import urllib.request

try:
    from nacl.public import PublicKey, SealedBox
except ImportError:
    sys.exit("NEED_PYNACL: pip install pynacl")

REPO = "usaimaker/ai-gumroad-products"
PAT = open(os.path.expanduser("~/.git-credentials")).read().strip().split(":")[2].split("@")[0]
TOKEN = os.environ.get("GUMROAD_TOKEN") or (sys.argv[1] if len(sys.argv) > 1 else None)
if not TOKEN:
    sys.exit("usage: GUMROAD_TOKEN=xxxx python set_gumroad_secret.py")


def api(method, path, data=None):
    url = "https://api.github.com" + path
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": "Bearer " + PAT,
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        },
        method=method,
    )
    if data is not None:
        req.data = json.dumps(data).encode()
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main():
    pk = api("GET", f"/repos/{REPO}/actions/secrets/public-key")
    raw_key = base64.b64decode(pk["key"])
    sealed = SealedBox(PublicKey(raw_key)).encrypt(TOKEN.encode())
    enc = base64.b64encode(sealed).decode()
    api(
        "PUT",
        f"/repos/{REPO}/actions/secrets/GUMROAD_TOKEN",
        {"encrypted_value": enc, "key_id": pk["key_id"]},
    )
    print("OK: GUMROAD_TOKEN secret stored for", REPO)


if __name__ == "__main__":
    main()
