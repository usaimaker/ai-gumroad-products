#!/usr/bin/env python3
"""Gumroad auto-publisher (stdlib only).

Reads product markdown files from products/, creates them on Gumroad via the
REST API using GUMROAD_TOKEN, and tracks published product ids in published.json
to avoid duplicates.

Product file format:
    # Title
    <markdown body>
Optionally a leading frontmatter block may set price (USD):
    ---
    price: 9
    ---
"""
import os
import sys
import json
import glob
import urllib.request
import urllib.error

API = "https://api.gumroad.com/v2/products"
TOKEN = os.environ.get("GUMROAD_TOKEN")
PUBLISHED = "published.json"
PRODUCTS_DIR = "products"


def log(*a):
    print(*a, flush=True)


def multipart(url, fields, files):
    boundary = "----gumroadboundary7Q2k9"
    body = b""
    for k, v in fields.items():
        body += f"--{boundary}\r\n".encode()
        body += f'Content-Disposition: form-data; name="{k}"\r\n\r\n'.encode()
        body += str(v).encode() + b"\r\n"
    for k, (fn, data, ctype) in files.items():
        body += f"--{boundary}\r\n".encode()
        body += f'Content-Disposition: form-data; name="{k}"; filename="{fn}"\r\n'.encode()
        body += f"Content-Type: {ctype}\r\n\r\n".encode()
        body += data + b"\r\n"
    body += f"--{boundary}--\r\n".encode()
    return url, body, {"Content-Type": f"multipart/form-data; boundary={boundary}"}


def load_published():
    if os.path.exists(PUBLISHED):
        try:
            return json.load(open(PUBLISHED, encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_published(d):
    with open(PUBLISHED, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2)


def parse_product(path):
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    price = 0
    if lines and lines[0].strip() == "---":
        end = None
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                end = j
                break
        if end:
            for fl in lines[1:end]:
                if fl.strip().lower().startswith("price:"):
                    try:
                        price = int(float(fl.split(":", 1)[1].strip()) * 100)
                    except Exception:
                        pass
            lines = lines[end + 1:]
    title = None
    body_start = 0
    for idx, ln in enumerate(lines):
        if ln.lstrip().startswith("# "):
            title = ln.lstrip()[2:].strip()
            body_start = idx + 1
            break
    if not title:
        title = lines[0].lstrip("# ").strip() if lines else os.path.basename(path)
    body = "\n".join(lines[body_start:]).strip()
    return title, body, price


def create_product(title, body, price, slug, filepath, with_file=True):
    fields = {
        "access_token": TOKEN,
        "name": title,
        "description": body,
        "price": price,
        "published": "true",
        "currency": "usd",
    }
    files = {}
    if with_file:
        files["file"] = (slug + ".md", open(filepath, "rb").read(), "text/markdown")
    url, data, headers = multipart(API, fields, files)
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"success": False, "message": f"HTTP {e.code}: {e.read().decode()[:300]}"}


def main():
    if not TOKEN:
        log("MISSING_TOKEN: set GUMROAD_TOKEN (GitHub Actions secret) to enable auto-publish")
        sys.exit(0)
    published = load_published()
    count = 0
    for f in sorted(glob.glob(os.path.join(PRODUCTS_DIR, "*.md"))):
        slug = os.path.splitext(os.path.basename(f))[0]
        if slug in published:
            log(f"skip {slug} (already published id={published[slug]})")
            continue
        title, body, price = parse_product(f)
        log(f"publishing {slug}: {title!r} price_cents={price}")
        res = create_product(title, body, price, slug, f, with_file=True)
        if not res.get("success"):
            msg = str(res.get("message", ""))
            # retry without the file attachment (some accounts/configs reject it)
            if "file" in msg.lower() or "422" in msg:
                log("  retry without file attachment...")
                res = create_product(title, body, price, slug, f, with_file=False)
        if res.get("success"):
            pid = res.get("product", {}).get("id")
            published[slug] = pid
            count += 1
            u = res.get("product", {}).get("url")
            log(f"  OK -> https://gumroad.com/l/{u} (id={pid})")
        else:
            log(f"  FAIL: {res.get('message')}")
    save_published(published)
    log(f"done. published {count} new product(s). total tracked={len(published)}")


if __name__ == "__main__":
    main()
