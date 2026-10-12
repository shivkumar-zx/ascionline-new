from bs4 import BeautifulSoup

# The new bullets for 2022, with line breaks replaced by spaces
new_bullets = [
    "ASCI releases - Complaints report on 'What India Takes Offence to' and 'Influencer Advertising' Reports in January 2022",
    "ASCI publishes guidelines for Advertising of Virtual Digital Assets (Cryptocurrency)",
    "ASCI Code updated for greater inclusivity",
    "ASCI publishes Guidelines for 'Harmful Gender Stereotypes in Advertising 'released by Hon'ble Cabinet Minister for Women and Child Development (WCD), Smt. Smriti Zubin Irani in June 2022"
]

chevron_svg = '''
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 5px; color: var(--accent);">
    <polyline points="9 18 15 12 9 6"></polyline>
</svg>
'''

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the 2022 entry (it has data-title="2022")
entry_2022 = soup.find('article', attrs={'data-title': '2022'})
if entry_2022:
    container = entry_2022.find('div', class_='milestones-clean-container')
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

print("Successfully updated the 2022 data.")
