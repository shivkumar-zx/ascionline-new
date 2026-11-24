import urllib.request
import re
from urllib.parse import urljoin, urlparse

start_url = 'https://www.ascionline.in/academy/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = urllib.request.Request(start_url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
except Exception as e:
    print('Error:', e)
    html = ''

# Find all hrefs
all_hrefs = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
academy_urls = set()
for h in all_hrefs:
    full = urljoin(start_url, h)
    # clean fragment and query
    full_clean = full.split('#')[0].split('?')[0].rstrip('/')
    if 'ascionline.in/academy' in full_clean:
        academy_urls.add(full_clean)

print("Academy pages found:")
for u in sorted(academy_urls):
    print(" -", u)

# Also check menu or navigation links
print("\nTotal Academy URLs found on landing page:", len(academy_urls))
