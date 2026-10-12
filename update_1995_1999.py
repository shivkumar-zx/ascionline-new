from bs4 import BeautifulSoup

# The new bullets for 1995 - 1999
new_bullets = [
    "New CCC Procedure for Processing Complaints is adopted on 1st December 2000",
    "The New Advertising Code is issued in April 1995",
    "The revised Code \"applies to advertisements read or viewed in India by a significant number even if carried by media that are published or originate abroad\"."
]

chevron_svg = '''
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 5px; color: var(--accent);">
    <polyline points="9 18 15 12 9 6"></polyline>
</svg>
'''

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the 1995 - 1999 entry
entry = soup.find('article', attrs={'data-title': '1995 - 1999'})
if entry:
    container = entry.find('div', class_='milestones-clean-container')
    if container:
        container.clear()
        for bullet in new_bullets:
            milestone = soup.new_tag('div', **{
                'class': 'box-free-milestone', 
                'style': 'display: flex; gap: 15px; align-items: flex-start; margin-bottom: 30px;'
            })
            milestone.append(BeautifulSoup(chevron_svg, 'html.parser'))
            p = soup.new_tag('p', **{
                'class': 'milestone-clean-desc', 
                'style': 'margin: 0; font-size: 18px; line-height: 1.6; color: var(--text); font-weight: 400;'
            })
            p.string = bullet
            milestone.append(p)
            container.append(milestone)
        print("Successfully updated the 1995 - 1999 data.")
else:
    print("Could not find the 1995 - 1999 entry!")

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
