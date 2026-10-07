with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.about-mega-grid-3col')
while idx != -1:
    print("Found at:", idx)
    print(text[idx:idx+300])
    idx = text.find('.about-mega-grid-3col', idx + 1)
