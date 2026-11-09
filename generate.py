import os, glob, html

QRIFY_BLOCK = '<!-- QRIFY_TRAFFIC_START -->\n<section class="qrify-tool" style="margin:32px 0;padding:18px 20px;border:1px solid #d8dee9;border-radius:12px;background:#f8fafc;color:#0f172a;font-family:system-ui,Arial,sans-serif;line-height:1.6">\n  <div style="font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:#64748b;margin-bottom:8px">Free tool for readers</div>\n  <p style="margin:0 0 10px"><strong>Make a QR code in seconds &mdash; no signup, no watermark.</strong> QRify is a free browser-based QR generator with custom colours, a logo overlay and SVG export. Everything runs locally in your browser, so your links and data never leave your device.</p>\n  <p style="margin:0;font-size:14px">\n    <a href="https://qrify.dynv6.net/" rel="noopener" style="color:#0369a1">Free QR code generator</a> &nbsp;&middot;&nbsp;\n    <a href="https://qrify.dynv6.net/wifi-qr-code" rel="noopener" style="color:#0369a1">WiFi QR code</a> &nbsp;&middot;&nbsp;\n    <a href="https://qrify.dynv6.net/vcard-qr-code" rel="noopener" style="color:#0369a1">vCard QR code</a> &nbsp;&middot;&nbsp;\n    <a href="https://qrify.dynv6.net/qr-code-with-logo" rel="noopener" style="color:#0369a1">QR code with logo</a> &nbsp;&middot;&nbsp;\n    <a href="https://qrify.dynv6.net/restaurant-menu-qr-code" rel="noopener" style="color:#0369a1">Restaurant menu QR</a> &nbsp;&middot;&nbsp;\n    <a href="https://usaimaker.github.io/free-qr-code-generator.html" rel="noopener" style="color:#0369a1">Full how-to guide</a>\n  </p>\n</section>\n<!-- QRIFY_TRAFFIC_END -->'

SRC = "products_src"
OUT = "products"

def build():
    os.makedirs(OUT, exist_ok=True)
    items = ""
    for f in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        slug = os.path.splitext(os.path.basename(f))[0]
        with open(f, encoding="utf-8") as fh:
            body = fh.read()
        title = body.splitlines()[0].lstrip("# ").strip() if body else slug
        with open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8") as pf:
            pf.write(body)
        items += f'<li><a href="products/{slug}.md">{html.escape(title)}</a></li>\n'
    index = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>AI Solopreneur Toolkit</title>
<meta name="description" content="Free done-for-you AI prompt packs and checklists for solo founders."></head>
<body style="font-family:system-ui,Arial;max-width:760px;margin:40px auto;padding:0 20px;line-height:1.7">
<h1>AI Solopreneur Toolkit</h1>
<p>Free, done-for-you AI prompt packs and checklists. <a href="https://gumroad.com">Get them on Gumroad</a>.</p>
<h2>Products</h2><ul>{items}</ul></body></html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index)
    print("built", len(glob.glob(os.path.join(SRC, "*.md"))), "products")

if __name__ == "__main__":
    build()

# QRIFY_TRAFFIC_INJECT_START (idempotent, survives the daily rebuild)
if __name__ == "__main__":
    try:
        with open("index.html", encoding="utf-8") as _qf:
            _qh = _qf.read()
        if "QRIFY_TRAFFIC_START" not in _qh:
            if "</body>" in _qh:
                _qh = _qh.replace("</body>", QRIFY_BLOCK + "\n</body>", 1)
            else:
                _qh = _qh + QRIFY_BLOCK
            with open("index.html", "w", encoding="utf-8") as _qf:
                _qf.write(_qh)
    except Exception as _qe:
        print("qrify inject skipped:", _qe)
# QRIFY_TRAFFIC_INJECT_END
