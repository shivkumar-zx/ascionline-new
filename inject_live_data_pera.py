import re
from bs4 import BeautifulSoup

# 1. Read live content
with open(r'C:\Users\Admin\.gemini\antigravity-ide\brain\4f0494d6-9631-4411-a197-f02c4592c554\.system_generated\steps\101\content.md', 'r', encoding='utf-8') as f:
    live_content = f.read()

live_html = live_content.split('---', 1)[1] if '---' in live_content else live_content
live_soup = BeautifulSoup(live_html, 'html.parser')

eras_data = []
his_numbers = live_soup.find_all('div', class_='his-number')

for hn in his_numbers:
    year = hn.text.strip()
    if not year:
        continue
    parent = hn.parent
    his_content = parent.find_next_sibling('div') or parent.find('div', class_='his-content') or hn.find_next('ul')
    bullets = []
    if his_content:
        lis = his_content.find_all('li')
        if lis:
            for li in lis:
                text = li.text.strip()
                if text:
                    bullets.append(text)
        else:
            text = his_content.text.strip()
            if text:
                bullets.append(text)
    
    if bullets:
        if not any(e['year'] == year for e in eras_data):
            eras_data.append({'year': year, 'bullets': bullets})

# We want 2026 if it wasn't scraped properly (maybe it's in a different tab)
# But we will just use the scraped eras_data. Let's add 2026 manually based on their screenshot if it's missing,
# but the user said "take the tab data from this link", so I'll just use what I scraped. 
# Wait! Let me check if 2026 is in the HTML.
# The previous python script output said "Extracted 18 eras from live site." starting with 2025. 
# I will just use the 18 eras extracted.

# 2. Read current page
with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    page_html = f.read()

page_soup = BeautifulSoup(page_html, 'html.parser')

timeline_section = page_soup.find('section', class_='story-timeline')
if not timeline_section:
    print("Could not find story-timeline section in the page!")
    exit(1)

# 3. Rebuild Sidebar Nav
nav = timeline_section.find('nav', class_='story-timeline__nav')
nav.clear()

track = page_soup.new_tag('span', **{'class': 'story-timeline__track', 'aria-hidden': 'true'})
progress = page_soup.new_tag('span', **{'class': 'story-timeline__progress', 'data-timeline-progress': '', 'aria-hidden': 'true'})
nav.append(track)
nav.append(progress)

for idx, era in enumerate(eras_data):
    is_active = 'is-active' if idx == 0 else ''
    nav_item = f"""
    <button type="button" class="story-timeline__nav-item {is_active}" data-timeline-nav-item="{idx}">
        <span class="story-timeline__dot"></span>
        <span class="story-timeline__nav-copy">
            <strong>{era['year']}</strong>
        </span>
    </button>
    """
    nav.append(BeautifulSoup(nav_item, 'html.parser'))

# 4. Update the current title display in sidebar
current_title = timeline_section.find('span', attrs={'data-timeline-current-title': True})
if current_title and eras_data:
    current_title.string = eras_data[0]['year']

# 5. Rebuild Content Entries
content_div = timeline_section.find('div', class_='story-timeline__content')
content_div.clear()

# SVG for chevron
chevron_svg = '''
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 5px; color: var(--accent);">
    <polyline points="9 18 15 12 9 6"></polyline>
</svg>
'''

for idx, era in enumerate(eras_data):
    is_state = 'is-active' if idx == 0 else 'is-future'
    idx_str = f"{(idx+1):02d}"
    
    article = page_soup.new_tag('article', **{
        'class': f'timeline-entry {is_state}',
        'data-timeline-entry': '',
        'data-index': era['year'],
        'data-title': era['year']
    })
    
    meta = f"""
    <div class="timeline-entry__meta">
        <span>{idx_str}</span>
        <time>{era['year']}</time>
    </div>
    """
    article.append(BeautifulSoup(meta, 'html.parser'))
    
    body = page_soup.new_tag('div', **{'class': 'timeline-entry__body', 'style': 'width: 100%;'})
    h2 = page_soup.new_tag('h2')
    h2.string = era['year']
    body.append(h2)
    
    container = page_soup.new_tag('div', **{'class': 'milestones-clean-container'})
    
    for bullet in era['bullets']:
        milestone = page_soup.new_tag('div', **{
            'class': 'box-free-milestone', 
            'style': 'display: flex; gap: 15px; align-items: flex-start; margin-bottom: 30px;'
        })
        
        # Add chevron
        milestone.append(BeautifulSoup(chevron_svg, 'html.parser'))
        
        # Add text as a simple paragraph ("pera"), no headings
        p = page_soup.new_tag('p', **{
            'class': 'milestone-clean-desc', 
            'style': 'margin: 0; font-size: 18px; line-height: 1.6; color: var(--text); font-weight: 400;'
        })
        p.string = bullet
        
        milestone.append(p)
        container.append(milestone)
        
    body.append(container)
    article.append(body)
    content_div.append(article)

# 6. Update CSS to handle more items in sidebar
style_tags = page_soup.find_all('style')
for st in style_tags:
    if '.story-timeline__nav-item' in st.text:
        st.string = st.string.replace('min-height: 90px;', 'min-height: 50px;')
        if 'scrollbar-width: none;' not in st.string:
            st.string = st.string.replace(
                '.story-timeline__nav { --progress: 0; position: relative; display: grid; }',
                '.story-timeline__nav { --progress: 0; position: relative; display: grid; max-height: 70vh; overflow-y: auto; scrollbar-width: none; }\n.story-timeline__nav::-webkit-scrollbar { display: none; }'
            )

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(str(page_soup))

print("Successfully injected live data as simple paragraphs with chevrons.")
