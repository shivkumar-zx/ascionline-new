from bs4 import BeautifulSoup

# The new bullets for 1990 - 1994
new_bullets = [
    "The first full-time Secretary-General of the Council is appointed in December 1993 - Mr. Gualbert Pereira",
    "The International Chamber of Commerce found ASCI's approach to achieving self-regulation in advertising, a workable model for the European Community"
]

chevron_svg = '''
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 5px; color: var(--accent);">
    <polyline points="9 18 15 12 9 6"></polyline>
</svg>
'''

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the 1990 - 1994 entry
entry = soup.find('article', attrs={'data-title': '1990 - 1994'})
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
        print("Successfully updated the 1990 - 1994 data.")
else:
    print("Could not find the 1990 - 1994 entry!")

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
