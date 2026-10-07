with open('people.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const members = [')
print(text[idx:idx+1200])
