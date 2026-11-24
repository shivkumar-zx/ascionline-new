import re

with open("data/academy/reports.html", "r", encoding="utf-8") as f:
    html = f.read()

headings = re.findall(r'<(h[1-4])[^>]*>(.*?)</\1>', html, re.I | re.S)
print("=== Headings in reports.html ===")
for tag, txt in headings:
    c = re.sub(r'<[^>]+>', '', txt).strip()
    if c:
        print(f"[{tag}] {c}")

pdfs = re.findall(r'<a\s+[^>]*href=["\']([^"\']+\.pdf)["\'][^>]*>(.*?)</a>', html, re.I | re.S)
print("\n=== PDFs in reports.html ===")
for p, txt in pdfs:
    clean = re.sub(r'<[^>]+>', '', txt).strip()
    print(f"  {clean} -> {p}")
