from bs4 import BeautifulSoup

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

entries = soup.find_all('article', class_='timeline-entry')
for entry in entries:
    body = entry.find('div', class_='timeline-entry__body')
    if body:
        # Re-add an empty meta div so the CSS grid works properly
        # (It expects the first child to take up the 75px column)
        meta = soup.new_tag('div', **{'class': 'timeline-entry__meta'})
        body.insert_before(meta)

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Fixed the grid layout issue by restoring empty meta containers.")
