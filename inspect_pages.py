import re

def check_body_content():
    pages = ['history-key-milestones.html', 'people.html', 'about-us.html', 'the-work-we-do.html']
    for p in pages:
        with open(p, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # content between </header> (or mobile drawer) and <footer
        footer_pos = text.find('<footer')
        header_pos = text.find('</header>')
        body_part = text[header_pos:footer_pos]
        
        # Find headings after header
        headings = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', body_part)
        print(f"=== {p} ===")
        print("Body content length:", len(body_part))
        print("Page Headings:", [h.strip() for h in headings[:10]])
        
        # Check timeline years
        if 'history' in p:
            years = re.findall(r'timeline-year-heading[^>]*>(.*?)</div>', body_part)
            print("Timeline years in history:", [y.strip() for y in years])

if __name__ == '__main__':
    check_body_content()
