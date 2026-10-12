import os
import re
from bs4 import BeautifulSoup

with open('the-work-we-do.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update openTab function to include history.pushState
if 'history.pushState' not in text:
    new_js = '''
  document.getElementById(tabId).style.display = "block";
  evt.currentTarget.className += " active";
  evt.currentTarget.style.backgroundColor = "#0b1221";
  evt.currentTarget.style.color = "white";
  
  const tabUrls = {
    'tab-how-we-handle': 'how-we-handle-complaints.html',
    'tab-what-we-cover': 'what-we-cover.html',
    'tab-proactive': 'our-proactive-monitoring.html',
    'tab-working': 'working-with-others.html'
  };
  if (tabUrls[tabId]) {
      window.history.pushState({}, '', tabUrls[tabId]);
  }
'''
    text = text.replace('''
  document.getElementById(tabId).style.display = "block";
  evt.currentTarget.className += " active";
  evt.currentTarget.style.backgroundColor = "#0b1221";
  evt.currentTarget.style.color = "white";''', new_js)

with open('the-work-we-do.html', 'w', encoding='utf-8') as f:
    f.write(text)

soup = BeautifulSoup(text, 'html.parser')

pages = [
    ('how-we-handle-complaints.html', 'tab-how-we-handle', 'How We Handle Complaints'),
    ('what-we-cover.html', 'tab-what-we-cover', 'What We Cover'),
    ('our-proactive-monitoring.html', 'tab-proactive', 'Our Proactive Monitoring'),
    ('working-with-others.html', 'tab-working', 'Working with Others'),
]

for filename, active_tab_id, title in pages:
    page_soup = BeautifulSoup(text, 'html.parser')
    
    # Reset all buttons
    for btn in page_soup.find_all('button', class_=re.compile(r'tab-btn')):
        if active_tab_id in btn.get('onclick', ''):
            btn['class'] = 'tab-btn active'
            btn['style'] = 'background-color: #0b1221; color: white; border-radius: 50px; padding: 14px 40px; font-weight: 600; font-size: 16px; border: none; cursor: pointer; transition: all 0.3s ease;'
        else:
            btn['class'] = 'tab-btn'
            btn['style'] = 'background-color: transparent; color: #555b66; border-radius: 50px; padding: 14px 40px; font-weight: 600; font-size: 16px; border: none; cursor: pointer; transition: all 0.3s ease;'

    # Reset all content
    for content in page_soup.find_all('div', class_='tab-content'):
        if content.get('id') == active_tab_id:
            content['style'] = 'display: block; text-align: left;'
        else:
            content['style'] = 'display: none; text-align: left;'

    if page_soup.title:
        page_soup.title.string = title + ' | ASCI'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(page_soup))

    # Also save to the nested folder
    nested_path = os.path.join('the-work-we-do', filename)
    os.makedirs('the-work-we-do', exist_ok=True)
    
    nested_soup = BeautifulSoup(str(page_soup), 'html.parser')
    for img in nested_soup.find_all('img'):
        src = img.get('src')
        if src and src.startswith('assets/images/'):
            img['src'] = '../' + src
    with open(nested_path, 'w', encoding='utf-8') as f:
        f.write(str(nested_soup))

print('Successfully generated all standalone pages and updated navigation')
