from bs4 import BeautifulSoup
import os

with open('the-work-we-do/how-we-handle-complaints.html', 'r', encoding='utf-8') as f:
    how_soup = BeautifulSoup(f, 'html.parser')

inner_banner = how_soup.find('section', class_='inner-banner')
page_content = how_soup.find('section', class_='page-content')

# Note: We replace the src of the images inside page_content to be correct relative to the-work-we-do.html
for img in (page_content.find_all('img') if page_content else []):
    src = img.get('src')
    if src and src.startswith('../assets/'):
        img['src'] = src.replace('../', '')

for img in (inner_banner.find_all('img') if inner_banner else []):
    src = img.get('src')
    if src and src.startswith('../assets/'):
        img['src'] = src.replace('../', '')

tab_html = f'''
<section class="tabs-section container" style="margin-top: 60px; margin-bottom: 60px; text-align: center;">
  <div class="tabs-container" style="background-color: #f3f6f8; border-radius: 50px; display: inline-flex; padding: 5px; margin-bottom: 40px;">
    <button class="tab-btn active" onclick="openTab(event, 'tab-how-we-handle')" style="background-color: #0b1221; color: white; border-radius: 50px; padding: 14px 40px; font-weight: 600; font-size: 16px; border: none; cursor: pointer; transition: all 0.3s ease;">How We Handle Complaints</button>
    <button class="tab-btn" onclick="openTab(event, 'tab-other')" style="background-color: transparent; color: #555b66; border-radius: 50px; padding: 14px 40px; font-weight: 600; font-size: 16px; border: none; cursor: pointer; transition: all 0.3s ease;">Other Section</button>
  </div>
  
  <div id="tab-how-we-handle" class="tab-content" style="display: block; text-align: left;">
     {str(inner_banner) if inner_banner else ''}
     {str(page_content) if page_content else ''}
  </div>
  <div id="tab-other" class="tab-content" style="display: none; text-align: left; padding: 40px; background: #fff; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
     <h2 style="font-size: 24px; margin-bottom: 15px;">More Content Coming Soon</h2>
     <p style="color: #555b66;">This tab will hold the additional content you create.</p>
  </div>
</section>
<script>
function openTab(evt, tabId) {{
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabcontent.length; i++) {{
    tabcontent[i].style.display = "none";
  }}
  tablinks = document.getElementsByClassName("tab-btn");
  for (i = 0; i < tablinks.length; i++) {{
    tablinks[i].className = tablinks[i].className.replace(" active", "");
    tablinks[i].style.backgroundColor = "transparent";
    tablinks[i].style.color = "#555b66";
  }}
  document.getElementById(tabId).style.display = "block";
  evt.currentTarget.className += " active";
  evt.currentTarget.style.backgroundColor = "#0b1221";
  evt.currentTarget.style.color = "white";
}}
</script>
'''

with open('the-work-we-do.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

hero = soup.find('section', class_='work-hero')
if hero:
    new_tag = BeautifulSoup(tab_html, 'html.parser')
    hero.insert_after(new_tag)
    with open('the-work-we-do.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print('Successfully added tabs section')
else:
    print('Could not find work-hero')
