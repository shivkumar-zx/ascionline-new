import json
import re

def build():
    # 1. Load shared master layouts (identical to index, about-us, people)
    with open('head_part.html', 'r', encoding='utf-8') as f:
        head_raw = f.read()

    with open('header_part.html', 'r', encoding='utf-8') as f:
        header_clean = f.read()

    with open('footer_part.html', 'r', encoding='utf-8') as f:
        footer_part = f.read()

    with open('footer_scripts.html', 'r', encoding='utf-8') as f:
        footer_scripts = f.read()

    # 2. Load authentic campaign assets
    with open('campaigns_clean.json', 'r', encoding='utf-8') as f:
        campaigns_data = json.load(f)

    processed_items = []
    item_counter = 0
    for y in campaigns_data:
        year_str = str(y['year'])
        for it in y['items']:
            item_counter += 1
            item_type = it['type']
            yt_id = it.get('yt_id') or ''
            video_url = it.get('video_url') or ''
            img_src = it.get('image_src') or ''
            caption = it.get('caption') or ''
            
            if item_type == 'video':
                if 'Chup-Na-Baitho' in img_src or year_str == '2021':
                    display_title = "ASCI #ChupNaBaitho Awareness Film"
                    if 'Advertising-Advice' in img_src:
                        display_title = "Advertising Advice Launch Campaign"
                elif 'Endorser-Due-Diligence' in img_src or year_str == '2022':
                    display_title = "Endorser Due Diligence Campaign"
                elif year_str == '2025':
                    display_title = "ASCI Public Vigilance & Compliance PSA"
                else:
                    display_title = f"ASCI Awareness Video ({year_str})"
            else:
                if 'Influencers' in img_src or 'Influencers' in caption:
                    display_title = f"Influencer Guidelines Disclosure - {caption or 'Artboard'}"
                elif 'Godrej' in img_src or 'Godrej' in caption:
                    display_title = f"Compliance Case Study - {caption or 'Ad Carousel'}"
                elif 'VOLINI' in img_src or 'VOLINI' in caption:
                    display_title = f"Volini Substantiation Case Study - {caption or 'Slide'}"
                elif 'World-Consumer-Day' in img_src:
                    display_title = f"World Consumer Rights Day Poster ({year_str})"
                elif 'Consumer-Awareness' in img_src:
                    display_title = f"Consumer Awareness Print Ad ({year_str})"
                elif 'Membership' in img_src:
                    display_title = f"ASCI Membership Campaign ({year_str})"
                elif 'elearning' in img_src:
                    display_title = f"ASCI E-Learning Campaign ({year_str})"
                elif caption and caption not in ['1','2','3','4','5','6','7']:
                    display_title = caption
                else:
                    display_title = f"ASCI Campaign Artboard ({year_str})"

            processed_items.append({
                'id': f"camp_{item_counter}",
                'year': year_str,
                'type': item_type,
                'title': display_title,
                'caption': caption,
                'video_url': video_url,
                'yt_id': yt_id,
                'image_src': img_src
            })

    total_videos = sum(1 for x in processed_items if x['type'] == 'video')
    total_images = sum(1 for x in processed_items if x['type'] == 'image')
    items_json = json.dumps(processed_items, ensure_ascii=False)

    # 3. Dedicated Campaigns & Player CSS (Matching people.html pixel-for-pixel)
    campaigns_css = """
    /* ================= CAMPAIGNS HERO (Matching people.html) ================= */
    .directory-hero {
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 48px 0 40px;
    }

    .breadcrumb-nav {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.875rem;
      color: #64748b;
      margin-bottom: 18px;
    }

    .breadcrumb-nav a {
      color: #008779;
      text-decoration: none;
      font-weight: 500;
    }

    .breadcrumb-nav a:hover {
      text-decoration: underline;
    }

    .directory-hero-content-wrapper {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 32px;
    }

    .directory-hero-left {
      flex: 1;
      max-width: 760px;
    }

    .campaigns-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 135, 121, 0.08);
      color: #008779;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 6px 14px;
      border-radius: 9999px;
      margin-bottom: 14px;
      border: 1px solid rgba(0, 135, 121, 0.18);
    }

    .campaigns-badge-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #008779;
      box-shadow: 0 0 0 3px rgba(0, 135, 121, 0.2);
    }

    .directory-page-title {
      font-family: var(--font-serif);
      font-size: 2.25rem;
      color: #0f172a;
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 12px;
      letter-spacing: -0.01em;
    }

    .directory-page-desc {
      font-size: 1.05rem;
      color: #475569;
      max-width: 820px;
      line-height: 1.6;
      margin-bottom: 0px;
    }

    .directory-hero-right {
      flex-shrink: 0;
      width: 100%;
      max-width: 520px;
    }

    /* Crosshair Stats Grid with Gradient Dividers (Identical to people.html) */
    .directory-stats-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      width: 100%;
      position: relative;
    }

    .directory-stats-grid::before {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 50%;
      width: 1px;
      background: linear-gradient(to bottom, transparent 0%, #e2e8f0 15%, #e2e8f0 85%, transparent 100%);
    }

    .directory-stats-grid::after {
      content: '';
      position: absolute;
      top: 50%;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(to right, transparent 0%, #e2e8f0 15%, #e2e8f0 85%, transparent 100%);
    }

    .stat-cell {
      padding: 32px 24px;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

    .stat-number {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      font-weight: 700;
      color: #008779;
      line-height: 1.1;
      margin-bottom: 8px;
    }

    .stat-label {
      font-size: 0.875rem;
      color: #64748b;
      font-weight: 500;
    }

    @media (max-width: 991px) {
      .directory-hero-content-wrapper {
        flex-direction: column;
        align-items: flex-start;
      }

      .directory-hero-right {
        max-width: 100%;
      }

      .directory-stats-grid {
        grid-template-columns: 1fr;
      }

      .directory-stats-grid::before,
      .directory-stats-grid::after {
        display: none;
      }

      .stat-cell {
        border-bottom: 1px solid #e2e8f0;
        padding: 20px 16px;
      }

      .stat-cell:last-child {
        border-bottom: none;
      }
    }

    /* ================= FLOATING STICKY CONTROLS SECTION (Matching people.html) ================= */
    .directory-controls-card {
      position: sticky;
      top: 155px;
      z-index: 35;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid #cbd5e1;
      border-radius: 16px;
      padding: 20px 24px;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
      margin-top: 24px;
      margin-bottom: 32px;
      transition: all 0.2s ease;
    }

    @media (max-width: 991px) {
      .directory-controls-card {
        top: 72px;
        padding: 16px;
      }
    }

    .controls-single-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: nowrap;
    }

    .search-input-box {
      flex: 1;
      min-width: 220px;
      max-width: 280px;
      display: flex;
      align-items: center;
      background: #f8fafc;
      border: 1.5px solid #cbd5e1;
      border-radius: 9999px;
      padding: 9px 18px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .search-input-box:focus-within {
      border-color: #008779;
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(0, 135, 121, 0.12);
    }

    .search-input-box input {
      border: none;
      background: transparent;
      outline: none;
      font-size: 0.92rem;
      color: #0f172a;
      width: 100%;
      margin-left: 10px;
      font-family: inherit;
    }

    .search-input-box input::placeholder {
      color: #94a3b8;
    }

    .filter-type-group {
      display: inline-flex;
      background: #f1f5f9;
      padding: 3px;
      border-radius: 12px;
      gap: 3px;
      flex-shrink: 0;
    }

    .filter-type-btn {
      padding: 7px 14px;
      border-radius: 9px;
      font-size: 0.8125rem;
      font-weight: 600;
      color: #64748b;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.18s ease;
      background: transparent;
      border: none;
      cursor: pointer;
      white-space: nowrap;
    }

    .filter-type-btn:hover {
      color: #0f172a;
    }

    .filter-type-btn.active {
      background: #ffffff;
      color: #008779;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.08);
    }

    .filter-type-count {
      background: rgba(0, 135, 121, 0.12);
      color: #008779;
      font-size: 0.72rem;
      padding: 1px 7px;
      border-radius: 9999px;
      font-weight: 700;
    }

    .controls-divider {
      width: 1px;
      height: 26px;
      background: #e2e8f0;
      flex-shrink: 0;
    }

    .filter-year-group {
      display: flex;
      align-items: center;
      gap: 5px;
      flex-shrink: 0;
      flex-wrap: nowrap;
    }

    .filter-year-label {
      font-size: 0.8125rem;
      font-weight: 700;
      color: #64748b;
      margin-right: 4px;
      white-space: nowrap;
    }

    .filter-year-btn {
      padding: 5px 12px;
      border-radius: 9999px;
      font-size: 0.8125rem;
      font-weight: 600;
      color: #475569;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      cursor: pointer;
      transition: all 0.16s ease;
      white-space: nowrap;
    }

    .filter-year-btn:hover {
      border-color: #cbd5e1;
      color: #0f172a;
      background: #ffffff;
    }

    .filter-year-btn.active {
      background: #008779;
      color: #ffffff;
      border-color: #008779;
      box-shadow: 0 2px 8px rgba(0, 135, 121, 0.25);
    }

    @media (max-width: 1200px) {
      .controls-single-row {
        flex-wrap: wrap;
        gap: 12px;
      }
      .controls-divider {
        display: none;
      }
      .search-input-box {
        max-width: 100%;
        min-width: 100%;
      }
    }

    /* ================= CAMPAIGNS GALLERY ================= */
    .campaigns-main-section {
      padding: 0 0 80px;
      background-color: #f8fafc;
      min-height: 500px;
    }

    .gallery-header-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
    }

    .gallery-count-badge {
      font-size: 0.875rem;
      color: #64748b;
    }

    .gallery-count-badge strong {
      color: #0f172a;
    }

    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 24px;
    }

    .gallery-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.24s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      position: relative;
    }

    .gallery-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 16px 32px -8px rgba(15, 23, 42, 0.12);
      border-color: #cbd5e1;
    }

    .gallery-thumb-wrap {
      position: relative;
      width: 100%;
      aspect-ratio: 1 / 1;
      background: #0f172a;
      overflow: hidden;
    }

    .gallery-thumb-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .gallery-card:hover .gallery-thumb-img {
      transform: scale(1.04);
    }

    .gallery-type-badge {
      position: absolute;
      top: 12px;
      left: 12px;
      z-index: 2;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: 9999px;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }

    .badge-video {
      background: rgba(220, 38, 38, 0.9);
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(220, 38, 38, 0.35);
    }

    .badge-image {
      background: rgba(0, 135, 121, 0.9);
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(0, 135, 121, 0.35);
    }

    .gallery-year-badge {
      position: absolute;
      top: 12px;
      right: 12px;
      z-index: 2;
      background: rgba(15, 23, 42, 0.75);
      color: #ffffff;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 9999px;
      backdrop-filter: blur(8px);
    }

    .video-play-overlay {
      position: absolute;
      inset: 0;
      background: rgba(15, 23, 42, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s ease;
    }

    .gallery-card:hover .video-play-overlay {
      background: rgba(15, 23, 42, 0.15);
    }

    .play-btn-circle {
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
      transition: transform 0.2s ease;
    }

    .gallery-card:hover .play-btn-circle {
      transform: scale(1.12);
    }

    .play-icon-tri {
      width: 0;
      height: 0;
      border-style: solid;
      border-width: 8px 0 8px 14px;
      border-color: transparent transparent transparent #dc2626;
      margin-left: 3px;
    }

    .gallery-card-body {
      padding: 16px 18px 20px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .gallery-card-title {
      font-family: var(--font-sans);
      font-size: 0.96rem;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.35;
      margin-bottom: 12px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .gallery-card-caption {
      font-size: 0.8125rem;
      color: #64748b;
      margin-bottom: 14px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      line-height: 1.4;
    }

    .gallery-card-footer {
      margin-top: auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.8125rem;
      font-weight: 600;
      color: #008779;
      padding-top: 10px;
      border-top: 1px solid #f1f5f9;
    }

    /* Empty state */
    .gallery-empty-state {
      padding: 80px 24px;
      text-align: center;
      background: #ffffff;
      border-radius: 20px;
      border: 1px dashed #cbd5e1;
      max-width: 520px;
      margin: 40px auto;
    }

    .gallery-empty-icon {
      width: 52px;
      height: 52px;
      margin: 0 auto 16px;
      color: #94a3b8;
    }

    .gallery-empty-title {
      font-family: var(--font-serif);
      font-size: 1.35rem;
      color: #0f172a;
      margin-bottom: 6px;
    }

    .gallery-empty-desc {
      color: #64748b;
      font-size: 0.92rem;
    }

    /* ================= LIGHTBOX MODAL WITH LEFT & RIGHT NAVIGATION ================= */
    .media-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }

    .media-modal-backdrop.open {
      opacity: 1;
      pointer-events: auto;
    }

    .media-modal-container {
      background: #0f172a;
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 20px;
      width: 100%;
      max-width: 960px;
      overflow: hidden;
      box-shadow: 0 25px 60px -12px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .media-modal-header {
      padding: 16px 22px;
      background: rgba(255, 255, 255, 0.04);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .media-modal-header-left {
      display: flex;
      align-items: center;
      gap: 14px;
      overflow: hidden;
    }

    .media-modal-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: #f8fafc;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .media-modal-counter {
      background: rgba(255, 255, 255, 0.12);
      color: #cbd5e1;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 9999px;
      white-space: nowrap;
    }

    .media-modal-close-btn {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      border: none;
      font-size: 1.1rem;
      transition: background 0.15s ease;
      flex-shrink: 0;
    }

    .media-modal-close-btn:hover {
      background: rgba(255, 255, 255, 0.25);
    }

    .media-modal-player-wrap {
      width: 100%;
      min-height: 380px;
      max-height: 72vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #000000;
      position: relative;
    }

    .media-modal-iframe {
      width: 100%;
      aspect-ratio: 16 / 9;
      max-height: 70vh;
      border: none;
    }

    .media-modal-img {
      max-width: 100%;
      max-height: 70vh;
      object-fit: contain;
      display: block;
    }

    /* Modal Navigation Buttons (Left & Right) */
    .modal-nav-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 20;
      transition: all 0.2s ease;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }

    .modal-nav-btn:hover {
      background: rgba(0, 135, 121, 0.95);
      border-color: #008779;
      transform: translateY(-50%) scale(1.1);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }

    .modal-prev-btn {
      left: 16px;
    }

    .modal-next-btn {
      right: 16px;
    }

    @media (max-width: 768px) {
      .modal-nav-btn {
        width: 38px;
        height: 38px;
      }
      .modal-prev-btn { left: 8px; }
      .modal-next-btn { right: 8px; }
    }

    .media-modal-footer {
      padding: 14px 22px;
      background: rgba(255, 255, 255, 0.04);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: #cbd5e1;
      font-size: 0.875rem;
      gap: 16px;
      flex-wrap: wrap;
    }

    .media-modal-footer-nav-hint {
      font-size: 0.78rem;
      color: #64748b;
    }

    .btn-external-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #38bdf8;
      font-weight: 600;
      text-decoration: none;
    }

    .btn-external-link:hover {
      text-decoration: underline;
    }
    """

    # 4. Prepare Head
    title = "Our Past Campaigns – The Advertising Standards Council of India (ASCI)"
    desc = "Find out more about the ads that ASCI has made in the past to encourage consumers to be more vigilant. Explore official video films, PSAs, and print campaigns from 2016 to 2025."
    head_custom = head_raw
    head_custom = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head_custom)
    head_custom = re.sub(r'<meta\s+name="description"\s+content=".*?"', f'<meta name="description" content="{desc}"', head_custom, flags=re.DOTALL)
    head_custom = head_custom.replace('</head>', f'\n<style>\n{campaigns_css}\n</style>\n</head>')

    # 5. Body HTML
    body_html = f'''
  <!-- Directory Hero Section (Matching people.html) -->
  <section class="directory-hero">
    <div class="container">
      <div class="breadcrumb-nav">
        <a href="index.html">Home</a>
        <span>/</span>
        <a href="about-us.html">About Us</a>
        <span>/</span>
        <span>Our Past Campaigns</span>
      </div>

      <div class="directory-hero-content-wrapper">
        <div class="directory-hero-left">
          <div class="campaigns-badge">
            <span class="campaigns-badge-dot"></span>
            <span>Public Vigilance &amp; Consumer Voice</span>
          </div>
          <h1 class="directory-page-title">Our Past Campaigns</h1>
          <p class="directory-page-desc">
            Find out more about the ads that ASCI has made in the past to encourage consumers to be more vigilant. Explore official video films, PSAs, and print campaigns from 2016 to 2025.
          </p>
        </div>

        <div class="directory-hero-right">
          <!-- Crosshair Stats Grid matching people.html -->
          <div class="directory-stats-grid">
            <div class="stat-cell">
              <div class="stat-number">{len(processed_items)}</div>
              <div class="stat-label">Total Campaign Assets</div>
            </div>
            <div class="stat-cell">
              <div class="stat-number">{total_videos}</div>
              <div class="stat-label">Video Films &amp; PSAs</div>
            </div>
            <div class="stat-cell">
              <div class="stat-number">{total_images}</div>
              <div class="stat-label">Print &amp; Digital Artboards</div>
            </div>
            <div class="stat-cell">
              <div class="stat-number">6</div>
              <div class="stat-label">Major Campaign Years</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Section with Floating Controls Card (Matching people.html) -->
  <section class="campaigns-main-section" id="campaigns">
    <div class="container">
      <!-- Floating Sticky Controls Card (top: 155px matching people.html) -->
      <div class="directory-controls-card">
        <div class="controls-single-row">
          <!-- Live Instant Search with Pill styling -->
          <div class="search-input-box">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input type="text" id="campaignSearch" placeholder="Search campaigns..." oninput="handleSearch(this.value)" />
          </div>

          <!-- Media Type Selector -->
          <div class="filter-type-group" id="mediaTypeTabs">
            <button class="filter-type-btn active" data-type="all" onclick="setMediaType('all', this)">
              <span>All Media</span>
              <span class="filter-type-count">{len(processed_items)}</span>
            </button>
            <button class="filter-type-btn" data-type="video" onclick="setMediaType('video', this)">
              <span>Video Films ({total_videos})</span>
            </button>
            <button class="filter-type-btn" data-type="image" onclick="setMediaType('image', this)">
              <span>Print ({total_images})</span>
            </button>
          </div>

          <!-- Vertical Divider -->
          <div class="controls-divider"></div>

          <!-- Year Selector Row in Same Single Row -->
          <div class="filter-year-group" id="yearPillGroup">
            <span class="filter-year-label">Year:</span>
            <button class="filter-year-btn active" data-year="all" onclick="setYear('all', this)">All</button>
            <button class="filter-year-btn" data-year="2025" onclick="setYear('2025', this)">2025</button>
            <button class="filter-year-btn" data-year="2022" onclick="setYear('2022', this)">2022</button>
            <button class="filter-year-btn" data-year="2021" onclick="setYear('2021', this)">2021</button>
            <button class="filter-year-btn" data-year="2020" onclick="setYear('2020', this)">2020</button>
            <button class="filter-year-btn" data-year="2019" onclick="setYear('2019', this)">2019</button>
            <button class="filter-year-btn" data-year="2016" onclick="setYear('2016', this)">2016</button>
          </div>
        </div>
      </div>

      <!-- Gallery Meta -->
      <div class="gallery-header-meta">
        <div class="gallery-count-badge">
          Showing <strong id="visibleCount">{len(processed_items)}</strong> campaigns
        </div>
      </div>

      <!-- Campaigns Gallery Grid -->
      <div class="gallery-grid" id="campaignsGrid">
        <!-- Rendered via JavaScript -->
      </div>

      <div class="gallery-empty-state" id="galleryEmpty" style="display: none;">
        <svg class="gallery-empty-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="8" y1="12" x2="16" y2="12"></line>
        </svg>
        <h3 class="gallery-empty-title">No campaigns found</h3>
        <p class="gallery-empty-desc">Try selecting a different year or clear the search filters.</p>
      </div>
    </div>
  </section>

  <!-- Media Player Lightbox Modal with Left & Right Navigation Arrows -->
  <div class="media-modal-backdrop" id="mediaModal" onclick="closeModalOnBackdrop(event)">
    <div class="media-modal-container">
      <div class="media-modal-header">
        <div class="media-modal-header-left">
          <div class="media-modal-title" id="modalTitle">Campaign Media</div>
          <div class="media-modal-counter" id="modalCounter">1 of {len(processed_items)}</div>
        </div>
        <button class="media-modal-close-btn" onclick="closeMediaModal()" aria-label="Close modal">✕</button>
      </div>

      <div class="media-modal-player-wrap" id="modalPlayerContent">
        <!-- Injected dynamically -->
      </div>

      <!-- Previous & Next Navigation Arrows -->
      <button class="modal-nav-btn modal-prev-btn" onclick="navigateModal(-1)" aria-label="Previous item">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      <button class="modal-nav-btn modal-next-btn" onclick="navigateModal(1)" aria-label="Next item">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>

      <div class="media-modal-footer">
        <span id="modalMetaYear">Year: 2025</span>
        <div class="media-modal-footer-nav-hint">Tip: Use &larr; &rarr; arrow keys to browse</div>
        <a href="#" target="_blank" rel="noopener noreferrer" class="btn-external-link" id="modalExternalLink">
          <span>Open Full Quality Asset</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </a>
      </div>
    </div>
  </div>
'''

    # 6. JavaScript Logic with Carousel Left/Right Navigation
    campaigns_scripts = f'''
  <script>
    const campaignItems = {items_json};

    let currentTypeFilter = 'all';
    let currentYearFilter = 'all';
    let currentSearchQuery = '';
    let currentFilteredItems = [];
    let currentModalIndex = 0;

    function renderGallery() {{
      const grid = document.getElementById('campaignsGrid');
      const emptyState = document.getElementById('galleryEmpty');
      const countLabel = document.getElementById('visibleCount');
      if (!grid || !emptyState || !countLabel) return;

      currentFilteredItems = campaignItems.filter(item => {{
        if (currentTypeFilter !== 'all' && item.type !== currentTypeFilter) return false;
        if (currentYearFilter !== 'all' && item.year !== currentYearFilter) return false;
        if (currentSearchQuery.trim() !== '') {{
          const q = currentSearchQuery.toLowerCase();
          const matchTitle = item.title.toLowerCase().includes(q);
          const matchCap = item.caption.toLowerCase().includes(q);
          const matchYear = item.year.includes(q);
          if (!matchTitle && !matchCap && !matchYear) return false;
        }}
        return true;
      }});

      countLabel.textContent = currentFilteredItems.length;

      if (currentFilteredItems.length === 0) {{
        grid.style.display = 'none';
        emptyState.style.display = 'block';
        return;
      }}

      grid.style.display = 'grid';
      emptyState.style.display = 'none';

      grid.innerHTML = currentFilteredItems.map((item, idx) => {{
        const isVideo = item.type === 'video';
        const typeBadge = isVideo ? '<span class="gallery-type-badge badge-video">Video Film</span>' : '<span class="gallery-type-badge badge-image">Print / Artboard</span>';
        const playOverlay = isVideo ? `
          <div class="video-play-overlay">
            <div class="play-btn-circle">
              <div class="play-icon-tri"></div>
            </div>
          </div>
        ` : '';

        return `
          <div class="gallery-card" onclick="openMediaModalByIndex(${{idx}})">
            <div class="gallery-thumb-wrap">
              ${{typeBadge}}
              <span class="gallery-year-badge">${{item.year}}</span>
              <img src="${{item.image_src}}" alt="${{item.title}}" class="gallery-thumb-img" loading="lazy" />
              ${{playOverlay}}
            </div>
            <div class="gallery-card-body">
              <h3 class="gallery-card-title">${{item.title}}</h3>
              <div class="gallery-card-footer">
                <span>${{isVideo ? 'Watch Video Film' : 'View High-Res Poster'}}</span>
                <span>&rarr;</span>
              </div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function setMediaType(type, btn) {{
      currentTypeFilter = type;
      document.querySelectorAll('#mediaTypeTabs .filter-type-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderGallery();
    }}

    function setYear(year, btn) {{
      currentYearFilter = year;
      document.querySelectorAll('#yearPillGroup .filter-year-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderGallery();
    }}

    function handleSearch(val) {{
      currentSearchQuery = val;
      renderGallery();
    }}

    function openMediaModalByIndex(index) {{
      if (!currentFilteredItems || currentFilteredItems.length === 0) return;
      if (index < 0) index = currentFilteredItems.length - 1;
      if (index >= currentFilteredItems.length) index = 0;
      currentModalIndex = index;

      const item = currentFilteredItems[currentModalIndex];
      if (!item) return;

      const modal = document.getElementById('mediaModal');
      const playerWrap = document.getElementById('modalPlayerContent');
      const titleEl = document.getElementById('modalTitle');
      const counterEl = document.getElementById('modalCounter');
      const yearEl = document.getElementById('modalMetaYear');
      const extLink = document.getElementById('modalExternalLink');

      titleEl.textContent = item.title;
      counterEl.textContent = `${{currentModalIndex + 1}} of ${{currentFilteredItems.length}}`;
      yearEl.textContent = `Campaign Year: ${{item.year}}`;

      if (item.type === 'video') {{
        playerWrap.innerHTML = `
          <iframe class="media-modal-iframe" src="https://www.youtube.com/embed/${{item.yt_id}}?autoplay=1&rel=0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        `;
        extLink.href = item.video_url || ('https://www.youtube.com/watch?v=' + item.yt_id);
        extLink.querySelector('span').textContent = 'Watch on YouTube';
      }} else {{
        playerWrap.innerHTML = `
          <img src="${{item.image_src}}" alt="${{item.title}}" class="media-modal-img" />
        `;
        extLink.href = item.image_src;
        extLink.querySelector('span').textContent = 'Open High-Res Poster';
      }}

      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }}

    function navigateModal(direction) {{
      openMediaModalByIndex(currentModalIndex + direction);
    }}

    function closeMediaModal() {{
      const modal = document.getElementById('mediaModal');
      const playerWrap = document.getElementById('modalPlayerContent');
      if (modal) modal.classList.remove('open');
      if (playerWrap) playerWrap.innerHTML = '';
      document.body.style.overflow = '';
    }}

    function closeModalOnBackdrop(e) {{
      if (e.target.id === 'mediaModal') {{
        closeMediaModal();
      }}
    }}

    document.addEventListener('keydown', (e) => {{
      const modal = document.getElementById('mediaModal');
      if (!modal || !modal.classList.contains('open')) return;

      if (e.key === 'Escape') {{
        closeMediaModal();
      }} else if (e.key === 'ArrowLeft') {{
        navigateModal(-1);
      }} else if (e.key === 'ArrowRight') {{
        navigateModal(1);
      }}
    }});

    // Immediate gallery rendering on script evaluation
    renderGallery();
    document.addEventListener('DOMContentLoaded', renderGallery);
  </script>
'''

    full_page = f"{head_custom}\n{header_clean}\n{body_html}\n{campaigns_scripts}\n{footer_part}\n{footer_scripts}"

    with open('campaigns.html', 'w', encoding='utf-8') as f:
        f.write(full_page)
    print("campaigns.html successfully generated! Total size:", len(full_page))

    with open('ad-campaigns.html', 'w', encoding='utf-8') as f:
        f.write(full_page)
    print("ad-campaigns.html successfully generated! Total size:", len(full_page))

if __name__ == '__main__':
    build()
