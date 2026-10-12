from bs4 import BeautifulSoup

# The new bullets for 2018, with line breaks replaced by spaces
new_bullets = [
    "Ministry of Information & Broadcasting issues advisory to all TV broadcasters to carry ASCI scroll encouraging viewers to raise complaint against objectionable ads"
]

chevron_svg = '''
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 5px; color: var(--accent);">
    <polyline points="9 18 15 12 9 6"></polyline>
</svg>
'''

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the 2018 entry (it has data-title="2018")
entry_2018 = soup.find('article', attrs={'data-title': '2018'})
if entry_2018:
    container = entry_2018.find('div', class_='milestones-clean-container')
    if container:
        # Clear existing bullets
        container.clear()
        
        # Add new bullets
        for bullet in new_bullets:
            milestone = soup.new_tag('div', **{
                'class': 'box-free-milestone', 
                'style': 'display: flex; gap: 15px; align-items: flex-start; margin-bottom: 30px;'
            })
            
            # Add chevron
            milestone.append(BeautifulSoup(chevron_svg, 'html.parser'))
            
            # Add text
            p = soup.new_tag('p', **{
                'class': 'milestone-clean-desc', 
                'style': 'margin: 0; font-size: 18px; line-height: 1.6; color: var(--text); font-weight: 400;'
            })
            p.string = bullet
            
            milestone.append(p)
            container.append(milestone)

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully updated the 2018 data.")
