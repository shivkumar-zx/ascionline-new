from bs4 import BeautifulSoup

with open('the-work-we-do.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

tab = soup.find(id='tab-how-we-handle')
if tab:
    # Remove the sidebar
    sidebar = tab.find('div', class_='col-sm-4')
    if sidebar:
        sidebar.decompose()

    # Find the main content column and update its classes/styles
    col_8 = tab.find('div', class_='col-sm-8')
    if col_8:
        col_8['class'] = 'content-main'
        col_8['style'] = 'max-width: 900px; margin: 0 auto; padding: 20px;'

    # Update row and container
    row = tab.find('div', class_='row')
    if row:
        row['style'] = 'display: flex; flex-direction: column; align-items: center;'
    
    # Style the text container
    lft_detail = tab.find('div', class_='lft-detail-page')
    if lft_detail:
        lft_detail['style'] = 'font-family: var(--font-sans);'

    # Style H2
    h2 = tab.find('h2')
    if h2:
        h2['style'] = 'font-family: var(--font-serif); font-size: 28px; color: var(--color-asci-green-dark); margin-bottom: 24px; font-weight: 700; line-height: 1.3;'

    # Style paragraphs
    for p in tab.find_all('p'):
        p['style'] = 'font-size: 16px; line-height: 1.7; color: var(--color-text-muted); margin-bottom: 16px;'

    # Style links
    for a in tab.find_all('a'):
        # don't style if it has other classes
        if not a.get('class'):
            a['style'] = 'color: var(--color-accent-blue); text-decoration: none; font-weight: 600;'

    # Fix images
    images_col = tab.find('div', class_='col-sm-12')
    if images_col:
        images_col['style'] = 'width: 100%; text-align: center; margin-top: 40px;'

    for img in tab.find_all('img'):
        img['style'] = 'max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);'

    # Inject style tag for mobile/desktop image hiding
    style_tag = soup.new_tag('style')
    style_tag.string = '''
        .hwhc-mobile { display: none; }
        @media (max-width: 768px) {
            .hwhc-desktop { display: none; }
            .hwhc-mobile { display: block; }
        }
    '''
    tab.insert(0, style_tag)

    with open('the-work-we-do.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print('Updated UI successfully')
else:
    print('Tab not found')
