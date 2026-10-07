with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('id="codesMegaPanel"')
idx2 = text.find('<div class="megamenu-panel"', idx1 + 10)
print(text[idx1:idx2])
