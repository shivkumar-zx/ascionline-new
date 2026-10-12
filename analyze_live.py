from bs4 import BeautifulSoup
import re

with open(r'C:\Users\Admin\.gemini\antigravity-ide\brain\4f0494d6-9631-4411-a197-f02c4592c554\.system_generated\steps\101\content.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the HTML part (after ---)
html = content.split('---', 1)[1] if '---' in content else content

soup = BeautifulSoup(html, 'html.parser')

# Find elements that might contain timeline data
# E.g. look for elements with 'timeline' or 'history' in their class
possible_elements = soup.find_all(class_=re.compile("timeline|history|milestone|year", re.I))

print(f"Found {len(possible_elements)} elements related to timeline.")

# Let's just print out text grouped by some structure or find the specific structure.
# Many sites use an unordered list, or specific divs. Let's look for years like 1985, 2000, 2020.
years = soup.find_all(text=re.compile(r'\b(1985|2000|2020|2021|2023)\b'))
for y in years[:5]:
    parent = y.parent
    print(f"Year found in tag <{parent.name}> with classes {parent.get('class')}")
    # print a bit of its parent's parent structure
    if parent.parent:
        print(f"  Parent tag <{parent.parent.name}> classes {parent.parent.get('class')}")

# Let's try to extract all h2 or h3 elements to get an idea of the page structure
headings = soup.find_all(['h2', 'h3'])
print("\nHeadings:")
for h in headings:
    print(f"{h.name} ({h.get('class')}): {h.text.strip()}")
