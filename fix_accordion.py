from bs4 import BeautifulSoup

with open('the-work-we-do.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

tab = soup.find(id='tab-working')
if tab:
    accordions = tab.find_all('div', class_='accordion')
    for accordion in accordions:
        cards = accordion.find_all('div', class_='card')
        
        # Create a new container for our custom details accordion
        custom_accordion = soup.new_tag('div')
        custom_accordion['class'] = 'custom-faq-accordion'
        custom_accordion['style'] = 'margin-top: 30px; border-top: 1px solid var(--color-card-border);'

        for card in cards:
            header_link = card.find('a', class_='btn-header-link')
            if not header_link:
                continue
            
            header_text = header_link.get_text(strip=True)
            
            # Find body
            body_div = card.find('div', class_='collapse')
            if not body_div:
                body_div = card.find('div', class_='card-body') # sometimes it's directly card-body
                
            card_body = body_div.find('div', class_='card-body') if body_div else None
            if not card_body:
                card_body = body_div

            details = soup.new_tag('details')
            details['style'] = 'border-bottom: 1px solid var(--color-card-border); padding: 16px 0; transition: all 0.3s ease;'
            
            summary = soup.new_tag('summary')
            summary['style'] = 'font-family: var(--font-sans); font-size: 18px; font-weight: 600; color: var(--color-text-main); cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;'
            summary.string = header_text
            
            # Webkit hides the default marker with list-style: none, but we can also use ::marker { display: none; }
            # We will use CSS classes injected later.
            details.append(summary)
            
            content_div = soup.new_tag('div')
            content_div['style'] = 'padding-top: 16px; color: var(--color-text-muted); line-height: 1.7;'
            if card_body:
                # Move all children of card_body to content_div
                for child in list(card_body.children):
                    content_div.append(child)
            
            details.append(content_div)
            custom_accordion.append(details)
            
        accordion.replace_with(custom_accordion)

    # Inject custom styles for details/summary
    style = soup.new_tag('style')
    style.string = '''
        .custom-faq-accordion details summary::-webkit-details-marker { display: none; }
        .custom-faq-accordion details summary::after {
            content: "+";
            font-size: 24px;
            color: var(--color-accent-orange);
            font-weight: 400;
            transition: transform 0.3s ease;
        }
        .custom-faq-accordion details[open] summary::after {
            content: "-";
        }
        .custom-faq-accordion details[open] summary {
            color: var(--color-asci-green-dark);
        }
    '''
    tab.insert(0, style)

with open('the-work-we-do.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Successfully converted accordion")
