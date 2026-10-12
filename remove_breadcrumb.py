from bs4 import BeautifulSoup

with open('the-work-we-do.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Remove breadcrumbs
breadcrumbs = soup.find('div', class_='breadcum-inner')
if breadcrumbs:
    breadcrumbs.decompose()
    print('Removed breadcrumbs')

# Remove the banner image (or the container for it)
banner = soup.find('section', class_='inner-banner')
if banner:
    # Just remove the whole banner? Or just the image? 
    # If I remove just the image, the blue banner stays. 
    # Let's just remove the inner-banner entirely because the tab already says "How We Handle Complaints"
    # Wait, the user specifically said "and image". Let's remove the whole section inner-banner to be safe, 
    # since it looks like a hero section inside a tab which is redundant.
    # Actually, to be safe, let's remove the whole `inner-banner` section. 
    banner.decompose()
    print('Removed inner-banner')

with open('the-work-we-do.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
