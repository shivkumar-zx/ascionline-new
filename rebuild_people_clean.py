import re
import json

# Read members_data and scripts from existing build_people.py
with open(r"C:\Users\Admin'\.gemini\antigravity-ide\brain\84e98776-9c99-4ac7-8865-a18787071ca6\scratch\build_people.py", "r", encoding="utf-8") as f:
    orig_code = f.read()

# Extract members_data
start_members = orig_code.find("members_data = [")
end_members = orig_code.find("people_css = \"\"\"")
members_code = orig_code[start_members:end_members]
ldict = {}
exec(members_code, globals(), ldict)
members_data = ldict["members_data"]

# Extract people_css
start_css = orig_code.find("people_css = \"\"\"") + len("people_css = \"\"\"")
end_css = orig_code.find("\"\"\"\n\nhtml_template = f\"\"\"")
people_css = orig_code[start_css:end_css]

# Extract people_body from html_template
start_body = orig_code.find("<!-- Directory Hero Section -->")
end_body = orig_code.find("{footer_part}")
people_body = orig_code[start_body:end_body]

# Read shared building blocks
with open('head_part.html', 'r', encoding='utf-8') as f:
    head_raw = f.read()

with open('header_part.html', 'r', encoding='utf-8') as f:
    header_clean = f.read()

with open('footer_part.html', 'r', encoding='utf-8') as f:
    footer_part = f.read()

with open('footer_scripts.html', 'r', encoding='utf-8') as f:
    footer_scripts = f.read()

title = "People & Governance Directory – ASCI | The Advertising Standards Council of India"
desc = "Complete directory of the Board of Governors, Consumer Complaints Council (CCC), Leadership Team, and Technical Experts governing self-regulation in Indian advertising."

head_custom = head_raw
head_custom = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head_custom)
head_custom = re.sub(r'<meta\s+name="description"\s+content=".*?"', f'<meta name="description" content="{desc}"', head_custom, flags=re.DOTALL)

css_injection = f"\n<style>\n{people_css}\n</style>\n</head>"
head_custom = head_custom.replace('</head>', css_injection)

# Add people directory JavaScript right before </script> in footer_scripts or in custom script block
people_js = f"""
<script>
const MEMBERS_DATA = {ldict.get('members_data') if False else '[]'};
</script>
"""

# Let's see the people JS inside orig_code
start_js = orig_code.find("<script id=\"peopleDirScript\">")
end_js = orig_code.find("</script>\n\n</body>")
if start_js != -1 and end_js != -1:
    extracted_js = orig_code[start_js:end_js+len("</script>")]
else:
    # search for script block at end
    idx = orig_code.rfind("<script>")
    idx2 = orig_code.rfind("</script>")
    extracted_js = orig_code[idx:idx2+len("</script>")]

people_full_html = f"{head_custom}\n{header_clean}\n{people_body}\n{extracted_js}\n{footer_part}\n{footer_scripts}"

with open('people.html', 'w', encoding='utf-8') as f:
    f.write(people_full_html)

print("SUCCESS: people.html rebuilt cleanly!")
