import re

files = [
    'about-us.html',
    'people.html',
    'history-key-milestones.html',
    'the-work-we-do.html'
]

print("=== VERIFYING INSIDE PAGES ===")
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        t = f.read()
    
    sections = re.findall(r'<section[^>]*>', t)
    has_home_hero = '<section class="hero-section"' in t or '<section class=\'hero-section\'' in t
    body_count = t.count('<body')
    header_count = t.count('<header')
    footer_count = t.count('<footer')
    has_about_panel = 'id="aboutMegaPanel"' in t
    has_arrow_diag = 'arrow-diag-icon' in t
    
    print(f"\n--- {fname} ---")
    print(f"File size: {len(t):,} bytes")
    print(f"Has homepage hero section? {has_home_hero}")
    print(f"Body count: {body_count}, Header count: {header_count}, Footer count: {footer_count}")
    print(f"Has aboutMegaPanel? {has_about_panel}, Has arrow-diag-icon? {has_arrow_diag}")
    print(f"Section tags found ({len(sections)}):")
    for s in sections:
        print(f"  {s}")

print("\n=== VERIFYING HOMEPAGE ASCI (3).html ===")
with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    h = f.read()
print(f"ASCI (3).html size: {len(h):,} bytes")
print("Has aboutMegaPanel?", 'id="aboutMegaPanel"' in h)
print("Has about-mega-grid-3col in CSS?", '.about-mega-grid-3col' in h)
print("Has Organisation column?", 'Organisation</h4>' in h or 'Organisation' in h)
print("Has People column?", 'People</h4>' in h or 'People' in h)
print("Has arrow-diag-icon in aboutMegaPanel?", 'arrow-diag-icon' in h)
