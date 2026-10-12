from bs4 import BeautifulSoup
import re

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

nav_sticky = soup.find('div', id='timelineStickyBar')
body_section = soup.find('section', class_='timeline-body-section')

if nav_sticky and body_section:
    eras = body_section.find_all('div', class_='timeline-era-section')
    print(f'Found {len(eras)} eras.')
    for era in eras:
        badge = era.find('div', class_='timeline-era-badge')
        title = era.find('span', class_='timeline-era-title')
        title_text = title.text.strip() if title else ''
        print(f'Era: {badge.text.strip()} - {title_text}')
        cards = era.find_all('div', class_='timeline-milestone-card')
        print(f'  Cards: {len(cards)}')
else:
    print('Could not find nav or body section.')
