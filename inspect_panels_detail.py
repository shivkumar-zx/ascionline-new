import re

with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

for p in ['membershipMegaPanel', 'newMegaPanel', 'codesMegaPanel']:
    idx = text.find(f'id="{p}"')
    if idx != -1:
        end_idx = text.find('</div>\n    </div>', idx)
        print(f"=== {p} ===")
        print(text[idx:idx+1500])

# Search CSS for these classes
css_matches = re.findall(r'(\.(?:membership|new|about|megamenu)-mega-grid[^{]*\{[^}]*\})', text)
for c in css_matches:
    print(c)
