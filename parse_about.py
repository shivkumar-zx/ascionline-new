import re

with open("data/academy/about.html", "r", encoding="utf-8") as f:
    html = f.read()

# find headings
headings = re.findall(r'<(h[1-4])[^>]*>(.*?)</\1>', html, re.I | re.S)
print("=== Headings in about.html ===")
for tag, txt in headings:
    c = re.sub(r'<[^>]+>', '', txt).strip()
    if c:
        print(f"[{tag}] {c}")
