from bs4 import BeautifulSoup

# The new bullets for 2019, with line breaks replaced by spaces
new_bullets = [
    "Delhi district court settled that ASCI has the power to regulate ads as per guidelines laid down. It re-affirmed the remit of ASCI over non-members",
    "Insurance Regulatory and Development Authority guidelines specify that ASCI code is the minimum standards to be adhered to in addition to IRDA's advertising guidelines",
    "Guidelines for Usage of Awards and Rankings in Advertisements are laid down"
]

chevron_svg = '''
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 5px; color: var(--accent);">
    <polyline points="9 18 15 12 9 6"></polyline>
</svg>
'''

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the 2019 entry (it has data-title="2019")
entry_2019 = soup.find('article', attrs={'data-title': '2019'})
if entry_2019:
    container = entry_2019.find('div', class_='milestones-clean-container')
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

print("Successfully updated the 2019 data.")
