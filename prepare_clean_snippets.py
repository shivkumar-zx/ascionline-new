# Clean extraction of header_part, footer_part, and footer_scripts

with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Header part: from <!-- Header --> to right before <!-- Hero Section -->
header_marker = '<!-- Header -->'
hero_marker = '<!-- Hero Section -->'
idx_header = text.find(header_marker)
idx_hero = text.find(hero_marker)

assert idx_header != -1 and idx_hero != -1, "Header or Hero marker not found!"
header_part = text[idx_header:idx_hero].strip()

# 2. Footer part: from <!-- Footer --> to right before <!-- Search Overlay Popup Modal -->
footer_marker = '<!-- Footer -->'
search_marker = '<!-- Search Overlay Popup Modal -->'
idx_footer = text.find(footer_marker)
idx_search = text.find(search_marker)

assert idx_footer != -1 and idx_search != -1, "Footer or Search marker not found!"
footer_part = text[idx_footer:idx_search].strip()

# 3. Footer scripts: from <!-- Search Overlay Popup Modal --> to </html>
idx_html_end = text.find('</html>') + len('</html>')
footer_scripts = text[idx_search:idx_html_end].strip()

# Save snippets
with open('header_part.html', 'w', encoding='utf-8') as f:
    f.write(header_part)

with open('footer_part.html', 'w', encoding='utf-8') as f:
    f.write(footer_part)

with open('footer_scripts.html', 'w', encoding='utf-8') as f:
    f.write(footer_scripts)

print(f"header_part length: {len(header_part)} chars")
print(f"footer_part length: {len(footer_part)} chars")
print(f"footer_scripts length: {len(footer_scripts)} chars")

print("Checking for hero in header_part:", 'hero-section' in header_part)
print("Checking for header in header_part:", '<header class="site-header">' in header_part)
print("Checking for mobileNavOverlay in header_part:", 'mobileNavOverlay' in header_part)
print("Checking for aboutMegaPanel in header_part:", 'id="aboutMegaPanel"' in header_part)
