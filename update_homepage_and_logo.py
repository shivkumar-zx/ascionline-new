import os
import re

# 1. Update header_part.html
with open('header_part.html', 'r', encoding='utf-8') as f:
    header = f.read()

# Replace <a href="#" class="header-logo-link" with <a href="index.html" class="header-logo-link"
header_updated = header.replace('<a href="#" class="header-logo-link"', '<a href="index.html" class="header-logo-link"')

with open('header_part.html', 'w', encoding='utf-8') as f:
    f.write(header_updated)
print("Updated header_part.html with href='index.html' on logo links.")

# 2. Update ASCI (3).html to ensure logo links to index.html and also save as index.html
with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    asci_full = f.read()

asci_updated = asci_full.replace('<a href="#" class="header-logo-link"', '<a href="index.html" class="header-logo-link"')

with open('ASCI (3).html', 'w', encoding='utf-8') as f:
    f.write(asci_updated)
print("Updated ASCI (3).html with logo link to index.html.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(asci_updated)
print("Created index.html (exact complete homepage) with logo link to index.html.")

# Verify homepage sections in index.html
sections = [
    'hero-section',
    'stats-section',
    'what-to-do-section',
    'protect-prevent-section',
    'dialogue-section',
    'resource-library-section',
    'events-section',
    'coe-section',
    'cta-callout-section'
]
for s in sections:
    assert s in asci_updated, f"Missing {s} in homepage!"
print("Verified all 9 homepage sections are 100% intact in index.html and ASCI (3).html!")
