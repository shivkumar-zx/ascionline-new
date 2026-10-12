from bs4 import BeautifulSoup

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

metas = soup.find_all('div', class_='timeline-entry__meta')
for meta in metas:
    span = meta.find('span')
    if span:
        span.decompose()

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Removed the numbers (01, 02, etc.) from the timeline entries.")
