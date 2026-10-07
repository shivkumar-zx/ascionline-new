with open('about-us.html', 'r', encoding='utf-8') as f:
    c = f.read()

anchors = ['purpose', 'work', 'people', 'milestones', 'awards', 'annual-reports', 'campaigns', 'careers', 'newsletter']
for a in anchors:
    print(f'id="{a}" present: {f"id=\"{a}\"" in c}')
