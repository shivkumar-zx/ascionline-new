with open('top_header_clean.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("top_header_clean starts with:")
print(text[:200])

# Check if there is an unclosed tag or extra body tag
print("Has <body>?", '<body' in text)
print("Has </header>?", '</header>' in text)
print("Has mobileNavOverlay?", 'mobileNavOverlay' in text)
print("Has hero-section?", 'hero-section' in text)
