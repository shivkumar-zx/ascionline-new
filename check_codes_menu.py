with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('<div class="megamenu-panel" >')
idx2 = text.find('<div class="megamenu-panel" id="academyMegaPanel">')
print("Content of codesMegaPanel:")
print(text[idx1:idx1+800])
