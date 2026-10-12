from bs4 import BeautifulSoup
import re

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

entries = soup.find_all('article', class_='timeline-entry')

for entry in entries:
    # 1. Change data-index to the year
    time_tag = entry.find('time')
    if time_tag:
        year = time_tag.text.strip()
        entry['data-index'] = year
    
    # 2. Remove the overarching eyebrow and h2
    body = entry.find('div', class_='timeline-entry__body')
    if not body:
        continue
    
    eyebrow = body.find('span', class_='timeline-entry__eyebrow')
    if eyebrow:
        eyebrow.decompose()
        
    h2 = body.find('h2')
    if h2:
        h2.decompose()
        
    # 3. Process cards
    grid = body.find('div', class_='timeline-milestones-grid')
    if grid:
        clean_container = soup.new_tag('div', **{'class': 'milestones-clean-container'})
        
        cards = grid.find_all('div', class_='timeline-milestone-card')
        for card in cards:
            date_el = card.find('span', class_='timeline-card-date')
            tag_el = card.find('span', class_='timeline-card-tag')
            title_el = card.find(['h3', 'h4'], class_='timeline-card-title')
            desc_el = card.find('p', class_='timeline-card-desc')
            
            # Clean up date text (remove SVG)
            date_text = ""
            if date_el:
                svg = date_el.find('svg')
                if svg:
                    svg.decompose()
                date_text = date_el.text.strip()
                
            tag_text = tag_el.text.strip() if tag_el else ""
            title_text = title_el.text.strip() if title_el else ""
            
            # We preserve desc inner html in case there are links
            desc_html = ""
            if desc_el:
                desc_html = "".join(str(c) for c in desc_el.contents).strip()
            
            # Create new structure
            milestone_div = soup.new_tag('div', **{'class': 'box-free-milestone'})
            
            # Eyebrow (Date + Tag)
            new_eyebrow = soup.new_tag('span', **{'class': 'timeline-entry__eyebrow'})
            new_eyebrow.string = f"{date_text} — {tag_text}" if tag_text else date_text
            milestone_div.append(new_eyebrow)
            
            # Title
            new_title = soup.new_tag('h3', **{'class': 'milestone-clean-title'})
            # Mimic the codepen title span if needed, but simple is fine
            new_title.string = title_text
            milestone_div.append(new_title)
            
            # Desc
            new_desc = soup.new_tag('p', **{'class': 'milestone-clean-desc'})
            new_desc.append(BeautifulSoup(desc_html, 'html.parser'))
            milestone_div.append(new_desc)
            
            clean_container.append(milestone_div)
            
        grid.replace_with(clean_container)

# Add CSS for the new classes
css = """
.milestones-clean-container {
    display: flex;
    flex-direction: column;
    gap: 80px;
    max-width: 900px;
    margin-top: 20px;
}
.box-free-milestone {
    position: relative;
}
.box-free-milestone .timeline-entry__eyebrow {
    display: block;
    margin-bottom: 20px;
    font-family: monospace;
    font-size: 11px;
    letter-spacing: 0.12em;
    color: var(--accent);
    font-weight: 600;
    text-transform: uppercase;
}
.milestone-clean-title {
    margin: 0 0 24px 0;
    font-size: clamp(32px, 4vw, 56px);
    line-height: 1.1;
    font-weight: 600;
    color: var(--text);
    letter-spacing: -0.03em;
}
.milestone-clean-desc {
    max-width: 600px;
    font-size: clamp(17px, 1.4vw, 21px);
    line-height: 1.7;
    color: var(--muted);
}
"""
style_tag = soup.find('style')
if style_tag:
    style_tag.append(css)

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully converted to box-free UI.")
