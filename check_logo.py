with open('header_part.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<a[^>]+href=["\'][^"\']*["\'][^>]*>', text)
for m in matches:
    if 'logo' in m.lower() or 'asci' in m.lower():
        print('Link:', m)

# Also check mobile drawer and header
for line in text.splitlines():
    if '<a' in line and ('asci' in line.lower() or 'logo' in line.lower() or 'brand' in line.lower()):
        print('Header/logo line:', line.strip()[:150])
