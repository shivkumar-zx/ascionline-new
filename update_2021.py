from bs4 import BeautifulSoup

# The new bullets for 2021, with line breaks replaced by spaces
new_bullets = [
    "ASCI releases 'Gendernext' Report in collaboration with Futurebrand In October 2021",
    "ASCI unveils its new Brand identity in August 2021",
    "ASCI publishes Guidelines for Influencers Advertising in Digital Media and ASCI.Social website in May 2021",
    "ASCI wins 2 ICAS Awards for 'Best Awareness Raising Initiative' and 'Best Sectoral Initiative' categories. In the 'special category at ICAS'. ASCI received a special mention for its extensive digital suo-moto monitoring through the NAMS initiative in June 2021",
    "ASCI launched a consumer connect initiative through its #ChupNaBaitho digital campaign in January 2021"
]

chevron_svg = '''
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 5px; color: var(--accent);">
    <polyline points="9 18 15 12 9 6"></polyline>
</svg>
'''

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the 2021 entry (it has data-title="2021")
entry_2021 = soup.find('article', attrs={'data-title': '2021'})
if entry_2021:
    container = entry_2021.find('div', class_='milestones-clean-container')
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

print("Successfully updated the 2021 data.")
