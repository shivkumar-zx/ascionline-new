import os
import re
import json
import urllib.request
from urllib.parse import urljoin, urlparse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

TARGET_PAGES = {
    "home": "https://www.ascionline.in/academy/",
    "about": "https://www.ascionline.in/academy/about-asci-academy/",
    "programs": "https://www.ascionline.in/academy/our-programs/",
    "courses": "https://www.ascionline.in/academy/courses-2/",
    "course_responsible_advertising": "https://www.ascionline.in/academy/product/the-ascis-guide-to-responsible-advertising/",
    "course_influencing_playbook": "https://www.ascionline.in/academy/course/the-responsible-influencing-playbook/",
    "course_ethical_ui_ux": "https://www.ascionline.in/academy/product/ethical-ui-ux-designs-building-consumer-trust/",
    "reports": "https://www.ascionline.in/academy/reports/",
    "events": "https://www.ascionline.in/academy/category/event/",
    "launch_event": "https://www.ascionline.in/academy/asci-academy-launch-event/"
}

ASSET_DIR = os.path.join("assets", "images", "academy")
os.makedirs(ASSET_DIR, exist_ok=True)
RAW_DATA_DIR = os.path.join("data", "academy")
os.makedirs(RAW_DATA_DIR, exist_ok=True)

def fetch_url(url):
    print(f"Fetching: {url}")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return ""

def download_image(img_url):
    if not img_url or img_url.startswith('data:') or not img_url.startswith('http'):
        return img_url
    
    parsed = urlparse(img_url)
    filename = os.path.basename(parsed.path)
    if not filename or '.' not in filename:
        return img_url
    
    # clean filename
    filename = re.sub(r'[^a-zA-Z0-9_\.-]', '_', filename)
    local_path = os.path.join(ASSET_DIR, filename)
    rel_path = f"assets/images/academy/{filename}"
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        return rel_path
        
    try:
        req = urllib.request.Request(img_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            with open(local_path, 'wb') as f:
                f.write(resp.read())
        print(f"  Saved image: {filename}")
        return rel_path
    except Exception as e:
        print(f"  Failed image {img_url}: {e}")
        return img_url

def extract_page_data(key, url, html):
    # Save raw html
    with open(os.path.join(RAW_DATA_DIR, f"{key}.html"), "w", encoding="utf-8") as f:
        f.write(html)
        
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
    title = title_match.group(1).strip() if title_match else ""
    
    # Find all images
    img_matches = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', html, re.I)
    downloaded_images = {}
    for img in set(img_matches):
        full_img_url = urljoin(url, img)
        if 'wp-content' in full_img_url or 'uploads' in full_img_url or 'assets' in full_img_url:
            local_rel = download_image(full_img_url)
            downloaded_images[img] = local_rel

    # Extract headings (h1, h2, h3)
    headings = []
    for h in re.finditer(r'<(h[1-4])[^>]*>(.*?)</\1>', html, re.I | re.S):
        tag, text = h.group(1), re.sub(r'<[^>]+>', '', h.group(2)).strip()
        if text:
            headings.append({"tag": tag, "text": text})

    # Extract paragraphs
    paragraphs = []
    for p in re.finditer(r'<p[^>]*>(.*?)</p>', html, re.I | re.S):
        text = re.sub(r'<[^>]+>', '', p.group(1)).strip()
        if len(text) > 20:
            paragraphs.append(text)

    # Extract PDF links
    pdf_links = []
    for a in re.finditer(r'<a\s+[^>]*href=["\']([^"\']+\.pdf)["\'][^>]*>(.*?)</a>', html, re.I | re.S):
        pdf_url = urljoin(url, a.group(1))
        link_text = re.sub(r'<[^>]+>', '', a.group(2)).strip()
        pdf_links.append({"url": pdf_url, "text": link_text})

    page_info = {
        "key": key,
        "url": url,
        "title": title,
        "headings": headings,
        "paragraphs": paragraphs[:30],
        "pdf_links": pdf_links,
        "images_count": len(downloaded_images)
    }
    
    with open(os.path.join(RAW_DATA_DIR, f"{key}_summary.json"), "w", encoding="utf-8") as f:
        json.dump(page_info, f, indent=2)
        
    return page_info

print("=== STARTING FULL ASCI ACADEMY SCRAPING ===")
results = {}
for k, u in TARGET_PAGES.items():
    html = fetch_url(u)
    if html:
        data = extract_page_data(k, u, html)
        results[k] = data
        print(f"-> Extracted {k}: {len(data['headings'])} headings, {len(data['paragraphs'])} paragraphs, {data['images_count']} images")

print("=== SCRAPING COMPLETE ===")
