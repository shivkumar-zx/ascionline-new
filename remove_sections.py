from bs4 import BeautifulSoup
import os

with open('the-work-we-do.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

sections_to_remove = []
for child in soup.body.find_all(recursive=False):
    classes = child.get('class') or []
    if 'work-detail-section' in classes or 'cta-callout-section' in classes:
        sections_to_remove.append(child)

if sections_to_remove:
    for s in sections_to_remove:
        s.decompose()
    with open('the-work-we-do.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print('Successfully removed', len(sections_to_remove), 'sections.')
else:
    print('Could not find sections to remove.')
