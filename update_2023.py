from bs4 import BeautifulSoup

# The new bullets for 2023, with line breaks replaced by spaces
new_bullets = [
    "ASCI and Futurebrands launch 'Wielding Influence, Nurturing Trust' study at its #GetltRight Brand Influencer Summit in February 2023",
    "ASCI releases its 'Influencer Trust Report' a consumer dipstick study that unveils reasons for consumer trust and distrust among influencer, February 2023",
    "ASCI releases 'EdNext' study that lays down progressive and responsible approach to advertising for the EdTech industry in January 2023",
    "ASCI publishes guidelines for advertisements for charitable causes",
    "ASCI and Khaitan & Co Release Whitepaper: Leveraging Generative Al: Opportunities, Risks and Best Practices",
    "ASCI unveils the ASCI Academy, a pioneering initiative poised to amplify the advertising industry's capacity to create more responsible and progressive advertising campaigns.",
    "ASCI and the Unstereotype Alliance Unveil Study on Diversity & Inclusion in Advertising, with research partner Kantar at the D&I Edge Summit"
]

chevron_svg = '''
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 5px; color: var(--accent);">
    <polyline points="9 18 15 12 9 6"></polyline>
</svg>
'''

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the 2023 entry (it has data-title="2023")
entry_2023 = soup.find('article', attrs={'data-title': '2023'})
if entry_2023:
    container = entry_2023.find('div', class_='milestones-clean-container')
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

print("Successfully updated the 2023 data.")
