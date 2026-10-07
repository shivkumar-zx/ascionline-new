with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(5394, len(lines)):
    line = lines[i].strip()
    if line.startswith('</'):
        print(f"{i+1}: {line}")
    elif '<script' in line:
        print(f"{i+1}: SCRIPT TAG -> {line}")
