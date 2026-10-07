import glob

files = [
    'index.html',
    'ASCI (3).html',
    'about-us.html',
    'people.html',
    'history-key-milestones.html',
    'the-work-we-do.html',
    'header_part.html',
    'top_header_clean.html'
]

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
        
        if '<div class="megamenu-panel" >' in c:
            c = c.replace('<div class="megamenu-panel" >', '<div class="megamenu-panel" id="codesMegaPanel">')
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(c)
            print(f"[{f}] Fixed: added id=\"codesMegaPanel\"")
        else:
            print(f"[{f}] No '<div class=\"megamenu-panel\" >' found (already fixed or not present)")
    except Exception as e:
        print(f"[{f}] Error: {e}")
