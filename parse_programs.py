import re

with open("data/academy/programs.html", "r", encoding="utf-8") as f:
    html = f.read()

headings = re.findall(r'<(h[1-4])[^>]*>(.*?)</\1>', html, re.I | re.S)
print("=== Headings in programs.html ===")
for tag, txt in headings:
    c = re.sub(r'<[^>]+>', '', txt).strip()
    if c:
        print(f"[{tag}] {c}")
