with open('people.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*>', text)
print("people.html sections:")
for s in sections:
    print(" ", s)

print("\nHeadings in people.html:")
h_tags = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', text, re.DOTALL)
for h in h_tags:
    print(" ", re.sub(r'\s+', ' ', h).strip())

print("\nDoes people.html have FSSAI-style directory table or search?")
print("  Has search input:", 'id="peopleSearch"' in text or 'id="directorySearch"' in text or 'search' in text.lower())
print("  Has table:", '<table' in text)
print("  Has modal:", 'modal' in text.lower())
