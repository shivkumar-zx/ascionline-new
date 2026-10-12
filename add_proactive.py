import os
import re
import urllib.request
from bs4 import BeautifulSoup

md_file = r'C:\Users\Admin\.gemini\antigravity-ide\brain\0ffb258c-ee42-4c70-b626-f822361c6058\.system_generated\steps\143\content.md'
with open(md_file, 'r', encoding='utf-8') as f:
    text = f.read()

html_part = re.sub(r'^.*?---', '', text, flags=re.DOTALL)
soup = BeautifulSoup(html_part, 'html.parser')
content = soup.find(id='primary') or soup.find('main') or soup.find(id='content')

inner_banner = content.find('section', class_='inner-banner') if content else None
page_content = content.find('section', class_='page-content') if content else None

if not page_content:
    print('Could not find page-content')
    exit(1)

breadcrumbs = page_content.find('div', class_='breadcum-inner')
if breadcrumbs:
    breadcrumbs.decompose()

sidebar = page_content.find('div', class_='col-sm-4')
if sidebar:
    sidebar.decompose()

title_text = 'Our Proactive Monitoring'
if inner_banner:
    h1 = inner_banner.find('h1')
    if h1:
        title_text = h1.get_text(strip=True)

# Format page-content
col_8 = page_content.find('div', class_='col-sm-8')
if col_8:
    col_8['class'] = 'content-main'
    col_8['style'] = 'max-width: 1280px; padding: 20px 0;'

row = page_content.find('div', class_='row')
if row:
    row['style'] = 'display: flex; flex-direction: column; align-items: flex-start;'

lft_detail = page_content.find('div', class_='lft-detail-page')
if lft_detail:
    lft_detail['style'] = 'font-family: var(--font-sans);'

h2 = page_content.find('h2')
if h2:
    h2['style'] = 'font-family: var(--font-serif); font-size: 28px; color: var(--color-asci-green-dark); margin-bottom: 24px; font-weight: 700; line-height: 1.3;'

for p in page_content.find_all('p'):
    p['style'] = 'font-size: 16px; line-height: 1.7; color: var(--color-text-muted); margin-bottom: 16px;'

for a in page_content.find_all('a'):
    if not a.get('class'):
        a['style'] = 'color: var(--color-accent-blue); text-decoration: none; font-weight: 600;'

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

os.makedirs('assets/images', exist_ok=True)
for img in page_content.find_all('img'):
    img['style'] = 'max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-top: 20px;'
    src = img.get('src')
    if src and src.startswith('http'):
        filename = src.split('/')[-1]
        local_path = os.path.join('assets', 'images', filename)
        if not os.path.exists(local_path):
            print(f'Downloading {src}')
            try:
                urllib.request.urlretrieve(src, local_path)
            except Exception as e:
                print('Failed to download', src, e)
        img['src'] = f'assets/images/{filename}'

# Append to the-work-we-do.html
with open('the-work-we-do.html', 'r', encoding='utf-8') as f:
    template_soup = BeautifulSoup(f, 'html.parser')

tabs_container = template_soup.find('div', class_='tabs-container')
if tabs_container:
    # Create new button
    new_btn = template_soup.new_tag('button', **{
        'class': 'tab-btn',
        'onclick': "openTab(event, 'tab-proactive')",
        'style': 'background-color: transparent; color: #555b66; border-radius: 50px; padding: 14px 40px; font-weight: 600; font-size: 16px; border: none; cursor: pointer; transition: all 0.3s ease;'
    })
    new_btn.string = title_text
    tabs_container.append(new_btn)

tabs_section = template_soup.find('section', class_='tabs-section')
if tabs_section:
    # Create new tab content div
    new_tab = template_soup.new_tag('div', id='tab-proactive', **{
        'class': 'tab-content',
        'style': 'display: none; text-align: left;'
    })
    new_tab.append(page_content)
    tabs_section.append(new_tab)

with open('the-work-we-do.html', 'w', encoding='utf-8') as f:
    f.write(str(template_soup))

# Now create our-proactive-monitoring.html
# Reset active classes
for btn in template_soup.find_all('button', class_='tab-btn'):
    if 'tab-proactive' in btn.get('onclick', ''):
        btn['class'] = 'tab-btn active'
        btn['style'] = 'background-color: #0b1221; color: white; border-radius: 50px; padding: 14px 40px; font-weight: 600; font-size: 16px; border: none; cursor: pointer; transition: all 0.3s ease;'
    else:
        btn['class'] = 'tab-btn'
        btn['style'] = 'background-color: transparent; color: #555b66; border-radius: 50px; padding: 14px 40px; font-weight: 600; font-size: 16px; border: none; cursor: pointer; transition: all 0.3s ease;'

for content in template_soup.find_all('div', class_='tab-content'):
    if content.get('id') == 'tab-proactive':
        content['style'] = 'display: block; text-align: left;'
    else:
        content['style'] = 'display: none; text-align: left;'

if template_soup.title:
    template_soup.title.string = title_text + ' | ASCI'

with open('our-proactive-monitoring.html', 'w', encoding='utf-8') as f:
    f.write(str(template_soup))

# Fix paths for the nested one
for img in template_soup.find_all('img'):
    src = img.get('src')
    if src and src.startswith('assets/images/'):
        img['src'] = '../' + src
with open(os.path.join('the-work-we-do', 'our-proactive-monitoring.html'), 'w', encoding='utf-8') as f:
    f.write(str(template_soup))

print('Successfully processed Our Proactive Monitoring')
