from bs4 import BeautifulSoup

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

entries = soup.find_all('article', class_='timeline-entry')
for idx, entry in enumerate(entries):
    # Set data-index to 01, 02, etc. starting from 1
    idx_str = f"{(idx+1):02d}"
    entry['data-index'] = idx_str

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Changed the background watermark back to sequential numbers (01, 02, etc.).")
