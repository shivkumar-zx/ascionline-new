import re

with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all megamenu panels
panels = re.findall(r'<div class="megamenu-panel"[^>]*id="([^"]+)"', text)
print("Megamenu panels found:", panels)

for p_id in panels:
    start = text.find(f'id="{p_id}"')
    end = text.find('</div>\n        </div>', start)
    snippet = text[start:start+1500]
    print(f"\n--- Panel: {p_id} ---")
    print(snippet[:600])
