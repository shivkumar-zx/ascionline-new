with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="aboutMegaPanel"')
end = text.find('id="codesMegaPanel"')
print(text[start:end])
