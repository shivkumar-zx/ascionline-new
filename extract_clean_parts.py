# Extract clean subpage template components from ASCI (3).html

with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

head_end = -1
body_start = -1
header_start = -1
header_end = -1
mobile_start = -1
mobile_end = -1
hero_start = -1
footer_start = -1

for i, l in enumerate(lines):
    if '</head>' in l and head_end == -1:
        head_end = i
    if '<body' in l and body_start == -1:
        body_start = i
    if '<header class="site-header">' in l and header_start == -1:
        header_start = i
    if '</header>' in l and header_end == -1:
        header_end = i
    if 'id="mobileNavOverlay"' in l and mobile_start == -1:
        mobile_start = i
    if '<!-- Hero Section -->' in l and hero_start == -1:
        hero_start = i
    if '<footer class="site-footer">' in l and footer_start == -1:
        footer_start = i

print(f"head_end: line {head_end+1}")
print(f"body_start: line {body_start+1}")
print(f"header_start: line {header_start+1}")
print(f"header_end: line {header_end+1}")
print(f"mobile_start: line {mobile_start+1}")
print(f"hero_start: line {hero_start+1}")
print(f"footer_start: line {footer_start+1}")

# mobile_end is right before hero_start
mobile_end = hero_start

# Head content (lines 0 to head_end)
head_lines = lines[:head_end+1]

# Header clean (from body_start up to hero_start)
header_clean_lines = lines[body_start:hero_start]

# Footer clean (from footer_start to end of file)
footer_clean_lines = lines[footer_start:]

with open('head_part.html', 'w', encoding='utf-8') as f:
    f.writelines(head_lines)

with open('top_header_clean.html', 'w', encoding='utf-8') as f:
    f.writelines(header_clean_lines)

with open('footer_clean.html', 'w', encoding='utf-8') as f:
    f.writelines(footer_clean_lines)

print("Saved head_part.html, top_header_clean.html, and footer_clean.html successfully!")
print("top_header_clean.html line count:", len(header_clean_lines))
print("Does top_header_clean.html have hero-section?", any('hero-section' in l for l in header_clean_lines))
