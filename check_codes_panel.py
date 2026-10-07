import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if '<div class="megamenu-panel" >' in c:
        print(f"{f}: has '<div class=\"megamenu-panel\" >'")
