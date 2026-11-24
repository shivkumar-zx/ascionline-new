import glob
import re

with open("top_header_clean.html", "r", encoding="utf-8") as f:
    clean_hdr = f.read()

# Extract the academyMegaPanel block from clean_hdr
academy_panel_match = re.search(r'(<div class="megamenu-panel" id="academyMegaPanel">.*?</div>\s*</div>\s*</div>)', clean_hdr, re.DOTALL)
if not academy_panel_match:
    # try another closing pattern
    academy_panel_match = re.search(r'(<!-- 3\. MEGAMENU PANEL: ASCI Academy -->.*?<!-- 4\. MEGAMENU PANEL: Topics & Resources -->)', clean_hdr, re.DOTALL)

assert academy_panel_match, "Could not extract academyMegaPanel from top_header_clean.html!"
new_academy_panel = academy_panel_match.group(1).rstrip()
print(f"Extracted clean academyMegaPanel ({len(new_academy_panel)} chars)")

# Target pages to update
files = sorted(glob.glob("*.html"))
updated_count = 0

for fname in files:
    if fname in ["top_header_clean.html", "header_part.html", "academy.html", "academy-about.html", "academy-programs.html", "academy-courses.html", "academy-reports.html"]:
        continue
    
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "id=\"academyMegaPanel\"" not in content:
        continue
        
    old_panel_match = re.search(r'(<!-- 3\. MEGAMENU PANEL: ASCI Academy -->.*?<!-- 4\. MEGAMENU PANEL: Topics & Resources -->)', content, re.DOTALL)
    if old_panel_match:
        content = content.replace(old_panel_match.group(1), new_academy_panel + "\n\n    ")
    else:
        # Fallback regex for academyMegaPanel
        content = re.sub(
            r'<div class="megamenu-panel" id="academyMegaPanel">.*?<!-- 4\. MEGAMENU PANEL',
            new_academy_panel + "\n\n    <!-- 4. MEGAMENU PANEL",
            content,
            flags=re.DOTALL
        )
        
    # Also update the nav link href for ASCI Academy
    content = re.sub(
        r'(<li class="nav-item nav-item-dropdown" data-menu="academyMegaPanel">\s*<a href=")#(" class="nav-link">\s*ASCI Academy)',
        r'\g<1>academy.html\g<2>',
        content
    )
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    updated_count += 1
    print(f"Updated {fname}")

print(f"\nSuccessfully synced Academy Mega Menu to {updated_count} pages!")
