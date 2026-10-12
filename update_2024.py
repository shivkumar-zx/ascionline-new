from bs4 import BeautifulSoup

# The new bullets for 2024, with line breaks replaced by spaces
new_bullets = [
    "ASCI and DoCA Host Consultation with Stakeholders on Surrogate Ads",
    "ASCI publishes Guidelines to Ensure Honest Environmental Claims in Advertisements",
    "ASCI signs MOU with Maha RERA to scan for misleading ads to enhance consumer protection in the real estate sector. February 2024",
    "ASCI and the Department of Consumer Affairs hosted consultation with industry stakeholders operating in categories whose advertising is restricted, discussing issues and possible routes of resolution on the topic of surrogate advertising. February 2024",
    'ASCI Academy launches its whitepaper, "Privacy and Progress Pillars of Digital Bharat" with Lexplosion. March 2024',
    'ASCI Academy released a report on "Conscious Patterns," a study of comprehensive deceptive patterns in top Indian apps and Parallel, along with Industry Partner Nasscom. August 2024',
    "ASCI joins the ICAS Global Think Tank to Advance Responsible Advertising - September, 2024",
    "ASCI to host Global Summit for Ad self-regulation in Mumbai in March 2025 - October, 2024",
    "ASCI Academy has launched Hindi versions of its two flagship e-learning courses: The ASCI Guide to Responsible Advertising and The Responsible Influencing Playbook. - December, 2024"
]

chevron_svg = '''
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 5px; color: var(--accent);">
    <polyline points="9 18 15 12 9 6"></polyline>
</svg>
'''

with open('c:/Users/Admin/Documents/asci-og/ascionline-new/history-key-milestones.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the 2024 entry (it has data-title="2024")
entry_2024 = soup.find('article', attrs={'data-title': '2024'})
if entry_2024:
    container = entry_2024.find('div', class_='milestones-clean-container')
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

print("Successfully updated the 2024 data.")
