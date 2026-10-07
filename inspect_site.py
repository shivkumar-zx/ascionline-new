import re

with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

panels = re.findall(r'<div class="megamenu-panel" id="([^"]+)">', text)
print("Panels:", panels)

# Let's inspect membershipMegaPanel and newMegaPanel
for p in panels:
    idx = text.find(f'id="{p}"')
    if idx != -1:
        snippet = text[idx:idx+1200]
        # find the grid class
        m = re.search(r'class="([^"]*grid[^"]*)"', snippet)
        grid_class = m.group(1) if m else "unknown"
        print(f"Panel: {p}, Grid class: {grid_class}")
