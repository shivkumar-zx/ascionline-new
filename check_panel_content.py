with open('top_header_clean.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="aboutMegaPanel"')
print(text[idx+700:idx+2500])
