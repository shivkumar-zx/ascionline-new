with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Line 1 to 50:")
for i in range(25):
    print(f"{i+1}: {lines[i]}", end="")

print("\n--- Header section search ---")
for i, l in enumerate(lines):
    if '<header class="site-header">' in l:
        print(f"Header starts at line {i+1}")
    if '</header>' in l:
        print(f"Header ends at line {i+1}")
    if 'id="mobileNavOverlay"' in l:
        print(f"Mobile nav overlay starts at line {i+1}")
    if '<!-- Hero Section -->' in l:
        print(f"Hero section starts at line {i+1}")
    if '<footer class="site-footer">' in l:
        print(f"Footer starts at line {i+1}")
    if '</footer>' in l:
        print(f"Footer ends at line {i+1}")
