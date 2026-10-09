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

    # 3. Dedicated Campaigns & Player CSS
    campaigns_css = """
    /* ================= CAMPAIGNS HERO (Institutional Style Matching people.html) ================= */
    .directory-hero {
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 48px 0 44px;
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
      gap: 40px;
    }

    .directory-hero-left {
      flex: 1;
      max-width: 680px;
    }

    .campaigns-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(8, 107, 89, 0.08);
      color: #086b59;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 6px 14px;
      border-radius: 9999px;
      margin-bottom: 14px;
      border: 1px solid rgba(8, 107, 89, 0.18);
    }

    .campaigns-badge-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #086b59;
      box-shadow: 0 0 0 3px rgba(8, 107, 89, 0.2);
    }

    .directory-page-title {
      font-family: var(--font-serif);
      font-size: 2.75rem;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.15;
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }

    .directory-page-desc {
      font-size: 1.0625rem;
      color: #475569;
      line-height: 1.6;
      max-width: 620px;
    }

    .directory-hero-right {
      flex-shrink: 0;
      width: 100%;
      max-width: 480px;
    }

    .directory-stats-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
    }

    .stat-cell {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 18px 20px;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .stat-cell:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
      border-color: #cbd5e1;
    }

    .stat-number {
      font-family: var(--font-sans);
      font-size: 1.85rem;
      font-weight: 800;
      color: #086b59;
      line-height: 1.1;
      margin-bottom: 4px;
    }

    .stat-label {
      font-size: 0.8125rem;
      color: #64748b;
      font-weight: 500;
      line-height: 1.35;
    }

    /* ================= STICKY CONTROLS SECTION (Matching people.html) ================= */
    .campaigns-controls-wrapper {
      position: sticky;
      top: 0;
      z-index: 95;
      background: rgba(248, 250, 252, 0.92);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      padding: 16px 0;
      border-bottom: 1px solid #e2e8f0;
      transition: all 0.2s ease;
    }

    .campaigns-controls-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 12px 20px;
      box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.06), 0 8px 10px -6px rgba(15, 23, 42, 0.04);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
    }

    .filter-type-group {
      display: inline-flex;
      background: #f1f5f9;
      padding: 4px;
      border-radius: 12px;
      gap: 4px;
    }

    .filter-type-btn {
      padding: 7px 16px;
      border-radius: 9px;
      font-size: 0.84rem;
      font-weight: 600;
      color: #64748b;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.18s ease;
      background: transparent;
      border: none;
      cursor: pointer;
    }

    .filter-type-btn:hover {
      color: #0f172a;
    }

    .filter-type-btn.active {
      background: #ffffff;
      color: #086b59;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.08);
    }

    .filter-type-count {
      background: rgba(8, 107, 89, 0.12);
      color: #086b59;
      font-size: 0.72rem;
      padding: 1px 7px;
      border-radius: 9999px;
      font-weight: 700;
    }

    .filter-year-group {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }

    .filter-year-btn {
      padding: 6px 13px;
      border-radius: 9999px;
      font-size: 0.8125rem;
      font-weight: 600;
      color: #475569;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      cursor: pointer;
      transition: all 0.16s ease;
    }

    .filter-year-btn:hover {
      border-color: #cbd5e1;
      color: #0f172a;
      background: #ffffff;
    }

    .filter-year-btn.active {
      background: #086b59;
      color: #ffffff;
      border-color: #086b59;
      box-shadow: 0 2px 8px rgba(8, 107, 89, 0.25);
    }

    .search-input-box {
      display: flex;
      align-items: center;
      gap: 10px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 6px 14px;
      flex: 1;
      min-width: 240px;
      max-width: 320px;
      transition: all 0.2s ease;
    }

    .search-input-box:focus-within {
      background: #ffffff;
      border-color: #086b59;
      box-shadow: 0 0 0 3px rgba(8, 107, 89, 0.12);
    }

    .search-input-box input {
      border: none;
      background: transparent;
      outline: none;
      font-family: inherit;
      font-size: 0.84rem;
      color: #0f172a;
      width: 100%;
    }

    .search-input-box input::placeholder {
      color: #94a3b8;
    }

    /* ================= CAMPAIGNS GALLERY ================= */
    .campaigns-gallery-section {
      padding: 44px 0 80px;
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
      background: rgba(8, 107, 89, 0.9);
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(8, 107, 89, 0.35);
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
      margin-bottom: 6px;
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
      color: #086b59;
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

    /* Lightbox Modal */
    .media-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
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
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 20px;
      width: 100%;
      max-width: 920px;
      overflow: hidden;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .media-modal-header {
      padding: 16px 20px;
      background: rgba(255, 255, 255, 0.04);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .media-modal-title {
      font-size: 1rem;
      font-weight: 700;
      color: #f8fafc;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      padding-right: 16px;
    }

    .media-modal-close-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      border: none;
      font-size: 1rem;
      transition: background 0.15s ease;
      flex-shrink: 0;
    }

    .media-modal-close-btn:hover {
      background: rgba(255, 255, 255, 0.25);
    }

    .media-modal-player-wrap {
      width: 100%;
      max-height: 72vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #000000;
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

    .media-modal-footer {
      padding: 14px 20px;
      background: rgba(255, 255, 255, 0.04);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: #cbd5e1;
      font-size: 0.875rem;
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

    /* Responsive */
    @media (max-width: 900px) {
      .directory-hero-content-wrapper {
        flex-direction: column;
        align-items: flex-start;
      }
      .directory-hero-right {
        max-width: 100%;
      }
      .campaigns-controls-card {
        flex-direction: column;
        align-items: stretch;
      }
      .search-input-box {
        max-width: 100%;
      }
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
              <div class="stat-label">Major Campaign Years (2016 – 2025)</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Sticky Filter Controls Card (Matching people.html) -->
  <section class="campaigns-controls-wrapper">
    <div class="container">
      <div class="campaigns-controls-card">
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
            <span>Print &amp; Digital Ads ({total_images})</span>
          </button>
        </div>

        <!-- Year Selector Pills -->
        <div class="filter-year-group" id="yearPillGroup">
          <button class="filter-year-btn active" data-year="all" onclick="setYear('all', this)">All Years</button>
          <button class="filter-year-btn" data-year="2025" onclick="setYear('2025', this)">2025</button>
          <button class="filter-year-btn" data-year="2022" onclick="setYear('2022', this)">2022</button>
          <button class="filter-year-btn" data-year="2021" onclick="setYear('2021', this)">2021</button>
          <button class="filter-year-btn" data-year="2020" onclick="setYear('2020', this)">2020</button>
          <button class="filter-year-btn" data-year="2019" onclick="setYear('2019', this)">2019</button>
          <button class="filter-year-btn" data-year="2016" onclick="setYear('2016', this)">2016</button>
        </div>

        <!-- Live Instant Search -->
        <div class="search-input-box">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input type="text" id="campaignSearch" placeholder="Search campaigns by title, topic, year..." oninput="handleSearch(this.value)" />
        </div>
      </div>
    </div>
  </section>

  <!-- Campaigns Gallery Grid -->
  <section class="campaigns-gallery-section">
    <div class="container">
      <div class="gallery-header-meta">
        <div class="gallery-count-badge">
          Showing <strong id="visibleCount">{len(processed_items)}</strong> campaigns
        </div>
      </div>

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

  <!-- Media Player Lightbox Modal -->
  <div class="media-modal-backdrop" id="mediaModal" onclick="closeModalOnBackdrop(event)">
    <div class="media-modal-container">
      <div class="media-modal-header">
        <div class="media-modal-title" id="modalTitle">Campaign Media</div>
        <button class="media-modal-close-btn" onclick="closeMediaModal()" aria-label="Close modal">✕</button>
      </div>
      <div class="media-modal-player-wrap" id="modalPlayerContent">
        <!-- Injected dynamically -->
      </div>
      <div class="media-modal-footer">
        <span id="modalMetaYear">Year: 2025</span>
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

    # 6. JavaScript Logic
    campaigns_scripts = f'''
  <script>
    const campaignItems = {items_json};

    let currentTypeFilter = 'all';
    let currentYearFilter = 'all';
    let currentSearchQuery = '';

    function renderGallery() {{
      const grid = document.getElementById('campaignsGrid');
      const emptyState = document.getElementById('galleryEmpty');
      const countLabel = document.getElementById('visibleCount');
      if (!grid || !emptyState || !countLabel) return;

      const filtered = campaignItems.filter(item => {{
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

      countLabel.textContent = filtered.length;

      if (filtered.length === 0) {{
        grid.style.display = 'none';
        emptyState.style.display = 'block';
        return;
      }}

      grid.style.display = 'grid';
      emptyState.style.display = 'none';

      grid.innerHTML = filtered.map(item => {{
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
          <div class="gallery-card" onclick="openMediaModal('${{item.id}}')">
            <div class="gallery-thumb-wrap">
              ${{typeBadge}}
              <span class="gallery-year-badge">${{item.year}}</span>
              <img src="${{item.image_src}}" alt="${{item.title}}" class="gallery-thumb-img" loading="lazy" />
              ${{playOverlay}}
            </div>
            <div class="gallery-card-body">
              <h3 class="gallery-card-title">${{item.title}}</h3>
              ${{item.caption ? `<p class="gallery-card-caption">${{item.caption}}</p>` : ''}}
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

    function openMediaModal(itemId) {{
      const item = campaignItems.find(i => i.id === itemId);
      if (!item) return;

      const modal = document.getElementById('mediaModal');
      const playerWrap = document.getElementById('modalPlayerContent');
      const titleEl = document.getElementById('modalTitle');
      const yearEl = document.getElementById('modalMetaYear');
      const extLink = document.getElementById('modalExternalLink');

      titleEl.textContent = item.title;
      yearEl.textContent = 'Campaign Year: ' + item.year;

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
      if (e.key === 'Escape') {{
        closeMediaModal();
      }}
    }});

    // Immediate execution
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
