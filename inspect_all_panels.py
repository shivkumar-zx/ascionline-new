import re

with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

panels = ['aboutMegaPanel', 'codesMegaPanel', 'academyMegaPanel', 'topicsMegaPanel', 'membershipMegaPanel', 'newMegaPanel']

for p in panels:
    idx = text.find(f'id="{p}"')
    if idx != -1:
        end_idx = text.find('</nav>', idx)
        snippet = text[idx:idx+800]
        print(f"=== {p} ===")
        # extract first 10 lines
        lines = snippet.split('\n')[:15]
        for l in lines:
            print(l)
