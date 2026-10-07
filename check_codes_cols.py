import re

with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="codesMegaPanel"')
end = text.find('id="academyMegaPanel"')
panel_html = text[start:end]
titles = re.findall(r'<h4 class="megamenu-col-title">([^<]+)</h4>', panel_html)
print('Codes panel column titles:', titles)

start_css = text.find('.megamenu-grid {')
end_css = text.find('}', start_css)
print('megamenu-grid CSS:', text[start_css:end_css+1])
