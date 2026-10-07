with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.topics-resources-mega-grid[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)
