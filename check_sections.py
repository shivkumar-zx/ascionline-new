with open('about-us.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="annual-reports"')
print(text[idx:idx+1500])
