with open('about-us.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.about-section')
print(text[idx:idx+1400])
