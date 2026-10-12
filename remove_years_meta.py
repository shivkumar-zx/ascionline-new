from bs4 import BeautifulSoup

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

metas = soup.find_all('div', class_='timeline-entry__meta')
for meta in metas:
    meta.decompose()

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Removed the timeline-entry__meta blocks completely.")
