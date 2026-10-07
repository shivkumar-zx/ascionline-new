import os
import shutil

# First, overwrite header_part.html with top_header_clean.html
shutil.copy('top_header_clean.html', 'header_part.html')
print("Updated header_part.html to clean version!")

# Check top_header_clean.html size and verify no hero section
with open('top_header_clean.html', 'r', encoding='utf-8') as f:
    hdr = f.read()

assert 'hero-section' not in hdr, "Error: hero-section found in clean header!"
print(f"Verified clean header! Length: {len(hdr)} chars")
