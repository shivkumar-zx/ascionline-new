from bs4 import BeautifulSoup

with open(r'C:\Users\Admin\.gemini\antigravity-ide\brain\4f0494d6-9631-4411-a197-f02c4592c554\.system_generated\steps\101\content.md', 'r', encoding='utf-8') as f:
    content = f.read()

html = content.split('---', 1)[1] if '---' in content else content
soup = BeautifulSoup(html, 'html.parser')

# Look for the container that holds his-number
his_numbers = soup.find_all('div', class_='his-number')
print(f"Found {len(his_numbers)} his-number divs.")

for hn in his_numbers:
    year = hn.text.strip()
    print(f"\nYear: {year}")
    
    # The actual content is usually in a sibling div or parent div.
    # Let's see the parent's parent structure
    parent = hn.parent
    print(f"Parent class: {parent.get('class')}")
    
    # Check for lists or paragraphs nearby
    his_content = parent.find_next_sibling('div') or parent.find('div', class_='his-content') or hn.find_next('ul')
    
    if his_content:
        # print the text of li elements if it's a ul, or just text
        lis = his_content.find_all('li')
        if lis:
            for li in lis:
                print(f" - {li.text.strip()}")
        else:
            print(f" Content: {his_content.text.strip()}")
