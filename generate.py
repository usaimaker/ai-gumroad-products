import os, glob, html

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