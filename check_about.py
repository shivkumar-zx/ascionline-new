with open('about-us.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*>', text)
print("about-us.html sections:")
for s in sections:
    print(" ", s)

print("\nHeadings in about-us.html:")
h_tags = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', text, re.DOTALL)
for h in h_tags:
    print(" ", re.sub(r'\s+', ' ', h).strip())
