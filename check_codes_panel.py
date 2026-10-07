with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="codesMegaPanel"')
end = text.find('id="academyMegaPanel"')
print(text[start:start+2500])
