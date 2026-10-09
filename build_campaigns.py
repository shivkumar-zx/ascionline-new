import json

def build():
    with open('history-key-milestones.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header_block = ''.join(lines[4448:5717])
    # Footer block from <section class="cta-callout-section"> up to </footer>
    footer_block = ''.join(lines[6823:7364])

    with open('campaigns_clean.json', 'r', encoding='utf-8') as f:
        campaigns_data = json.load(f)

    # Process items
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
            
            # Meaningful title/badge based on official context
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

    page_html = f'''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <meta content="width=device-width, initial-scale=1.0" name="viewport" />
  <title>Our Past Campaigns – The Advertising Standards Council of India (ASCI)</title>
  <meta
    content="Find out more about the ads that ASCI has made in the past to encourage consumers to be more vigilant. Explore video films and print campaigns from 2016 to 2025."
    name="description" />
  <link href="https://fonts.googleapis.com" rel="preconnect" />
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect" />
  <link
    href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,200..800&amp;family=Domine:wght@400..700&amp;display=swap"
    rel="stylesheet" />
  <style>
    @font-face {{
      font-family: 'Domine';
      src: url('./Domine/Domine-VariableFont_wght.ttf') format('truetype-variations');
      font-weight: 400 700;
      font-style: normal;
      font-display: swap;
    }}

    @font-face {{
      font-family: 'Bricolage Grotesque';
      src: url('./Bricolage_Grotesque/BricolageGrotesque-VariableFont_opsz,wdth,wght.ttf') format('truetype-variations');
      font-weight: 200 800;
      font-style: normal;
      font-display: swap;
    }}

    :root {{
      --font-serif: 'Domine', Georgia, serif;
      --font-sans: 'Bricolage Grotesque', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

      --color-bg: #FFFFFF;
      --color-text-main: #111827;
      --color-text-muted: #555B66;
      --color-text-light: #7A828F;

      --color-asci-green: #086b59;
      --color-asci-green-dark: #054c3f;
      --color-asci-teal: #008779;
      --color-asci-deep-green: #03362a;
      --color-dark-bg: #032b22;
      --color-dark-emerald: #053b2f;
      --color-accent-blue: #026095;
      --color-accent-orange: #e57200;
      --color-accent-yellow: #f5a623;

      --color-card-bg: #FFFFFF;
      --color-card-border: #E8ECEF;
      --color-card-hover-border: #cbd5e1;

      --container-max-w: 1280px;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-pill: 9999px;
      --transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    html {{
      scroll-behavior: smooth;
      font-size: 16px;
    }}

    body {{
      font-family: var(--font-sans);
      color: var(--color-text-main);
      background-color: #f8fafc;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}

    .container {{
      max-width: var(--container-max-w);
      margin: 0 auto;
      padding: 0 24px;
      width: 100%;
    }}

    a {{
      color: inherit;
      text-decoration: none;
    }}

    button {{
      font-family: inherit;
      cursor: pointer;
      border: none;
      background: none;
    }}

    /* Top Notice Bar */
    .top-notice-bar {{
      background: #02261f;
      color: #ffffff;
      font-size: 0.8125rem;
      padding: 10px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
      z-index: 101;
    }}

    .top-notice-flex {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .top-notice-links {{
      display: flex;
      align-items: center;
      gap: 20px;
    }}

    .top-notice-links a:hover {{
      color: #4ade80;
    }}

    /* Header & Navigation */
    .site-header {{
      background: #ffffff;
      position: sticky;
      top: 0;
      z-index: 100;
      border-bottom: 1px solid #f0f2f5;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.02);
    }}

    .header-top-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 0;
      gap: 24px;
    }}

    .mobile-burger-btn,
    .mobile-search-btn,
    .mobile-nav-overlay {{
      display: none;
    }}

    .header-logo-link {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      flex-shrink: 0;
    }}

    .site-logo-img {{
      height: 48px;
      width: auto;
      display: block;
    }}

    .header-search-bar {{
      flex: 1;
      max-width: 520px;
      margin: 0 20px;
      position: relative;
    }}

    .search-input-wrapper {{
      display: flex;
      align-items: center;
      background: #ffffff;
      border: 1.2px solid #d0d7de;
      border-radius: var(--radius-pill);
      padding: 8px 18px;
      transition: var(--transition);
    }}

    .search-input-wrapper:focus-within {{
      border-color: var(--color-asci-teal);
      box-shadow: 0 0 0 3px rgba(0, 135, 121, 0.12);
    }}

    .header-search-icon {{
      width: 17px;
      height: 17px;
      color: var(--color-text-muted);
      margin-right: 10px;
      flex-shrink: 0;
    }}

    .search-input {{
      border: none;
      outline: none;
      background: transparent;
      font-size: 0.9375rem;
      color: var(--color-text-main);
      width: 100%;
      font-family: inherit;
    }}

    .search-shortcut-badge {{
      font-size: 0.6875rem;
      background: #f1f5f9;
      color: var(--color-text-muted);
      padding: 2px 7px;
      border-radius: 4px;
      font-weight: 600;
      border: 1px solid #e2e8f0;
      white-space: nowrap;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }}

    .btn-ad-check {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #f8fafc;
      color: #1e293b;
      border: 1.2px solid #cbd5e1;
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      font-size: 0.875rem;
      font-weight: 600;
      transition: var(--transition);
    }}

    .btn-ad-check:hover {{
      background: #f1f5f9;
      border-color: #94a3b8;
    }}

    .btn-ad-check-icon {{
      color: var(--color-asci-teal);
      font-weight: 700;
    }}

    .btn-raise-complaint {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--color-asci-teal);
      color: #ffffff;
      padding: 9px 20px;
      border-radius: var(--radius-pill);
      font-size: 0.875rem;
      font-weight: 600;
      transition: var(--transition);
      box-shadow: 0 2px 6px rgba(0, 135, 121, 0.2);
    }}

    .btn-raise-complaint:hover {{
      background: #007367;
      transform: translateY(-1px);
    }}

    /* Navigation Bar */
    .header-nav-bar {{
      border-top: 1px solid #f0f2f5;
    }}

    .main-nav-list {{
      display: flex;
      align-items: center;
      gap: 32px;
      list-style: none;
      padding: 0;
      margin: 0;
    }}

    .nav-item {{
      position: relative;
    }}

    .nav-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.9375rem;
      font-weight: 500;
      color: #334155;
      padding: 14px 0;
      transition: var(--transition);
    }}

    .nav-link:hover,
    .nav-item.active .nav-link {{
      color: var(--color-asci-teal);
    }}

    .chevron-icon {{
      width: 14px;
      height: 14px;
      stroke: currentColor;
      transition: transform 0.2s ease;
    }}

    .nav-item.nav-item-dropdown.open .chevron-icon {{
      transform: rotate(180deg);
    }}

    /* Megamenu Styles */
    .megamenu-panel {{
      display: none;
      position: absolute;
      top: 100%;
      left: 0;
      width: 100%;
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
      padding: 40px 0 48px;
      z-index: 99;
    }}

    .megamenu-panel.active {{
      display: block;
      animation: megaFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    @keyframes megaFadeIn {{
      from {{ opacity: 0; transform: translateY(-6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .about-mega-grid-3col {{
      display: grid;
      grid-template-columns: 280px 1.4fr 1.6fr;
      gap: 40px;
    }}

    .megamenu-grid {{
      display: grid;
      grid-template-columns: 280px 1fr 1fr 1fr;
      gap: 36px;
    }}

    .megamenu-highlight-col {{
      background: #f8fafc;
      border-radius: var(--radius-md);
      padding: 28px 24px;
      border: 1px solid #edf2f7;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .megamenu-highlight-title {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      line-height: 1.35;
      color: var(--color-text-main);
      margin-bottom: 12px;
      font-weight: 700;
    }}

    .megamenu-highlight-desc {{
      font-size: 0.875rem;
      color: var(--color-text-muted);
      line-height: 1.5;
      margin-bottom: 24px;
    }}

    .btn-megamenu-explore {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.875rem;
      font-weight: 600;
      color: var(--color-asci-teal);
    }}

    .megamenu-col-title {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--color-text-light);
      margin-bottom: 18px;
      font-weight: 600;
    }}

    .megamenu-2col-list {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }}

    .megamenu-links-list {{
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .megamenu-link-item a {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      font-size: 0.925rem;
      color: var(--color-text-muted);
      transition: var(--transition);
      line-height: 1.4;
    }}

    .megamenu-link-item a:hover {{
      color: var(--color-asci-teal);
    }}

    .arrow-diag-icon {{
      width: 14px;
      height: 14px;
      stroke: currentColor;
      opacity: 0.4;
      transition: opacity 0.2s, transform 0.2s;
    }}

    .megamenu-link-item a:hover .arrow-diag-icon {{
      opacity: 1;
      transform: translate(2px, -2px);
    }}

    /* ================= CAMPAIGNS HERO (Matching people.html) ================= */
    .directory-hero {{
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 48px 0 44px;
    }}

    .breadcrumb-nav {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.875rem;
      color: #64748b;
      margin-bottom: 18px;
    }}

    .breadcrumb-nav a {{
      color: var(--color-asci-teal);
      text-decoration: none;
      font-weight: 500;
    }}

    .breadcrumb-nav a:hover {{
      text-decoration: underline;
    }}

    .directory-hero-content-wrapper {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 36px;
    }}

    .directory-hero-left {{
      flex: 1;
      max-width: 720px;
    }}

    .campaigns-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 135, 121, 0.08);
      border: 1px solid rgba(0, 135, 121, 0.2);
      color: var(--color-asci-teal);
      padding: 5px 14px;
      border-radius: var(--radius-pill);
      font-size: 0.8125rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin-bottom: 14px;
    }}

    .campaigns-badge-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10b981;
    }}

    .directory-page-title {{
      font-family: var(--font-serif);
      font-size: 2.35rem;
      color: #0f172a;
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 12px;
    }}

    .directory-page-desc {{
      font-size: 1.05rem;
      color: #475569;
      max-width: 680px;
      line-height: 1.6;
      margin-bottom: 0;
    }}

    .directory-hero-right {{
      flex-shrink: 0;
      width: 100%;
      max-width: 500px;
    }}

    .directory-stats-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      width: 100%;
      position: relative;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
      overflow: hidden;
    }}

    .directory-stats-grid::before {{
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 50%;
      width: 1px;
      background: linear-gradient(to bottom, transparent 0%, #e2e8f0 15%, #e2e8f0 85%, transparent 100%);
    }}

    .directory-stats-grid::after {{
      content: '';
      position: absolute;
      top: 50%;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(to right, transparent 0%, #e2e8f0 15%, #e2e8f0 85%, transparent 100%);
    }}

    .stat-cell {{
      padding: 24px 20px;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }}

    .stat-number {{
      font-family: var(--font-serif);
      font-size: 2.2rem;
      font-weight: 700;
      color: var(--color-asci-teal);
      line-height: 1.1;
      margin-bottom: 6px;
    }}

    .stat-label {{
      font-size: 0.8125rem;
      color: #64748b;
      font-weight: 500;
      line-height: 1.35;
    }}

    @media (max-width: 991px) {{
      .directory-hero-content-wrapper {{
        flex-direction: column;
        align-items: flex-start;
      }}
      .directory-hero-right {{
        max-width: 100%;
      }}
    }}

    /* ================= STICKY CONTROLS SECTION (Matching people.html) ================= */
    .campaigns-controls-wrapper {{
      position: sticky;
      top: 155px;
      z-index: 45;
      margin-top: -24px;
      margin-bottom: 36px;
      pointer-events: none;
    }}

    .campaigns-controls-card {{
      pointer-events: auto;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid #cbd5e1;
      border-radius: 16px;
      padding: 16px 24px;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      flex-wrap: wrap;
    }}

    @media (max-width: 991px) {{
      .campaigns-controls-wrapper {{
        top: 72px;
        margin-top: 16px;
      }}
      .campaigns-controls-card {{
        padding: 14px 16px;
      }}
    }}

    .filter-type-group {{
      display: flex;
      align-items: center;
      background: #f1f5f9;
      padding: 4px;
      border-radius: var(--radius-pill);
      gap: 2px;
    }}

    .filter-type-btn {{
      padding: 8px 18px;
      font-size: 0.875rem;
      font-weight: 600;
      color: #475569;
      border-radius: var(--radius-pill);
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .filter-type-btn:hover {{
      color: #0f172a;
    }}

    .filter-type-btn.active {{
      background: #ffffff;
      color: var(--color-asci-teal);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    }}

    .filter-type-count {{
      font-size: 0.75rem;
      background: rgba(0, 135, 121, 0.1);
      color: var(--color-asci-teal);
      padding: 2px 7px;
      border-radius: 10px;
      font-weight: 700;
    }}

    .filter-year-group {{
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      scrollbar-width: none;
      padding: 2px 0;
    }}

    .filter-year-group::-webkit-scrollbar {{
      display: none;
    }}

    .filter-year-btn {{
      padding: 7px 16px;
      font-size: 0.8125rem;
      font-weight: 600;
      color: #475569;
      border: 1px solid #cbd5e1;
      border-radius: var(--radius-pill);
      white-space: nowrap;
      transition: var(--transition);
      background: #ffffff;
    }}

    .filter-year-btn:hover {{
      border-color: var(--color-asci-teal);
      color: var(--color-asci-teal);
    }}

    .filter-year-btn.active {{
      background: var(--color-asci-teal);
      color: #ffffff;
      border-color: var(--color-asci-teal);
    }}

    .search-input-box {{
      flex: 1;
      min-width: 240px;
      display: flex;
      align-items: center;
      background: #f8fafc;
      border: 1.5px solid #cbd5e1;
      border-radius: var(--radius-pill);
      padding: 8px 16px;
      gap: 10px;
      transition: var(--transition);
    }}

    .search-input-box:focus-within {{
      border-color: var(--color-asci-teal);
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(0, 135, 121, 0.12);
    }}

    .search-input-box input {{
      border: none;
      background: transparent;
      outline: none;
      width: 100%;
      font-size: 0.875rem;
      font-family: inherit;
      color: #0f172a;
    }}

    /* ================= CAMPAIGNS GALLERY ================= */
    .campaigns-gallery-section {{
      padding: 10px 0 80px;
    }}

    .gallery-header-meta {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
    }}

    .gallery-count-badge {{
      font-size: 0.9375rem;
      color: var(--color-text-muted);
      font-weight: 500;
    }}

    .gallery-count-badge strong {{
      color: var(--color-text-main);
      font-weight: 700;
    }}

    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 28px;
    }}

    .gallery-card {{
      background: #ffffff;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--color-card-border);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
      transition: var(--transition);
      display: flex;
      flex-direction: column;
      cursor: pointer;
    }}

    .gallery-card:hover {{
      transform: translateY(-5px);
      border-color: var(--color-asci-teal);
      box-shadow: 0 16px 32px rgba(0, 135, 121, 0.12);
    }}

    .gallery-thumb-wrap {{
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      background: #0f172a;
      overflow: hidden;
    }}

    .gallery-thumb-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.35s ease;
      display: block;
    }}

    .gallery-card:hover .gallery-thumb-img {{
      transform: scale(1.05);
    }}

    .gallery-type-badge {{
      position: absolute;
      top: 12px;
      left: 12px;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      font-size: 0.6875rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      z-index: 2;
      backdrop-filter: blur(8px);
    }}

    .badge-video {{
      background: rgba(220, 38, 38, 0.9);
      color: #ffffff;
    }}

    .badge-image {{
      background: rgba(14, 116, 144, 0.9);
      color: #ffffff;
    }}

    .gallery-year-badge {{
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(15, 23, 42, 0.85);
      color: #ffffff;
      padding: 3px 9px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
      z-index: 2;
    }}

    .video-play-overlay {{
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(0, 0, 0, 0.25);
      transition: background 0.2s ease;
    }}

    .gallery-card:hover .video-play-overlay {{
      background: rgba(0, 0, 0, 0.45);
    }}

    .play-btn-circle {{
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: #ff0000;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .gallery-card:hover .play-btn-circle {{
      transform: scale(1.15);
    }}

    .play-icon-tri {{
      width: 0;
      height: 0;
      border-top: 9px solid transparent;
      border-bottom: 9px solid transparent;
      border-left: 15px solid #ffffff;
      margin-left: 3px;
    }}

    .gallery-card-body {{
      padding: 16px 18px 18px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }}

    .gallery-card-title {{
      font-size: 1rem;
      font-weight: 600;
      color: var(--color-text-main);
      line-height: 1.4;
      margin-bottom: 8px;
    }}

    .gallery-card-caption {{
      font-size: 0.8125rem;
      color: var(--color-text-muted);
      line-height: 1.5;
      margin-top: auto;
    }}

    .gallery-card-footer {{
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px solid #f1f5f9;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.8125rem;
      color: var(--color-asci-teal);
      font-weight: 600;
    }}

    /* Empty state */
    .gallery-empty-state {{
      text-align: center;
      padding: 80px 20px;
      grid-column: 1 / -1;
      display: none;
    }}

    .gallery-empty-icon {{
      width: 56px;
      height: 56px;
      stroke: #94a3b8;
      margin-bottom: 16px;
    }}

    .gallery-empty-title {{
      font-family: var(--font-serif);
      font-size: 1.5rem;
      color: #334155;
      margin-bottom: 8px;
    }}

    .gallery-empty-desc {{
      color: #64748b;
      font-size: 0.9375rem;
    }}

    /* Lightbox Modal */
    .media-modal-backdrop {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}

    .media-modal-backdrop.open {{
      display: flex;
      animation: modalFadeIn 0.2s ease;
    }}

    @keyframes modalFadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}

    .media-modal-container {{
      background: #0f172a;
      border-radius: var(--radius-lg);
      max-width: 900px;
      width: 100%;
      overflow: hidden;
      box-shadow: 0 24px 48px rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.1);
      position: relative;
    }}

    .media-modal-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 24px;
      background: rgba(255, 255, 255, 0.04);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      color: #ffffff;
    }}

    .media-modal-title {{
      font-size: 1.05rem;
      font-weight: 600;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      padding-right: 16px;
    }}

    .media-modal-close-btn {{
      color: #ffffff;
      font-size: 1.5rem;
      line-height: 1;
      opacity: 0.7;
      transition: opacity 0.2s;
    }}

    .media-modal-close-btn:hover {{
      opacity: 1;
    }}

    .media-modal-player-wrap {{
      width: 100%;
      background: #000000;
      aspect-ratio: 16 / 9;
      position: relative;
    }}

    .media-modal-iframe {{
      width: 100%;
      height: 100%;
      border: none;
    }}

    .media-modal-img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .media-modal-footer {{
      padding: 14px 24px;
      background: rgba(255, 255, 255, 0.03);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: #cbd5e1;
      font-size: 0.875rem;
    }}

    .btn-external-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #38bdf8;
      font-weight: 600;
    }}

    .btn-external-link:hover {{
      text-decoration: underline;
    }}

    /* ================= HERO CALLOUT BANNER: RESPONSIBLE ADVERTISING ================= */
    .cta-callout-section {{
      position: relative;
      background-color: #06392c;
      background-image: radial-gradient(circle at 14% 50%, rgba(16, 185, 129, 0.15) 0%, transparent 65%);
      color: #ffffff;
      padding: 110px 0;
      text-align: center;
      overflow: hidden;
      margin-top: 60px;
    }}

    .cta-ripple-canvas {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }}

    .cta-callout-container {{
      position: relative;
      z-index: 2;
    }}

    .cta-callout-title {{
      font-family: var(--font-serif);
      font-size: 2.85rem;
      line-height: 1.25;
      font-weight: 400;
      margin-bottom: 20px;
      letter-spacing: -0.01em;
      color: #ffffff;
    }}

    .cta-callout-desc {{
      font-size: 1.2rem;
      color: rgba(255, 255, 255, 0.88);
      max-width: 720px;
      margin: 0 auto 36px;
      line-height: 1.55;
      font-weight: 400;
    }}

    .btn-cta-membership {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: 1px solid rgba(255, 255, 255, 0.65);
      border-radius: var(--radius-pill);
      padding: 11px 26px;
      font-size: 0.92rem;
      font-weight: 500;
      color: #ffffff;
      background: rgba(255, 255, 255, 0.04);
      transition: all 0.25s ease;
      backdrop-filter: blur(4px);
      text-decoration: none;
    }}

    .btn-cta-membership:hover {{
      background: #ffffff;
      color: #06392c;
      border-color: #ffffff;
    }}

    /* ================= FOOTER STYLES ================= */
    .site-footer {{
      background: #ffffff;
      padding: 70px 0 0px;
      border-top: 1px solid #e2e8f0;
    }}

    .footer-top-grid {{
      display: grid;
      grid-template-columns: 1.4fr 1fr 1fr 1fr;
      gap: 36px;
      padding-bottom: 50px;
      border-bottom: 1px solid #f1f5f9;
    }}

    .footer-brand-col {{
      padding-right: 32px;
    }}

    .footer-logo-img {{
      height: 48px;
      width: auto;
      margin-bottom: 16px;
      display: block;
    }}

    .footer-mission {{
      font-size: 0.84rem;
      color: #64748b;
      line-height: 1.5;
      margin-bottom: 18px;
    }}

    .footer-email-link {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 1rem;
      font-weight: 500;
      color: #0f172a;
      margin-bottom: 24px;
      text-decoration: none;
    }}

    .footer-socials-label {{
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: #0f172a;
      margin-bottom: 10px;
    }}

    .footer-social-icons {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .social-icon-circle {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: transparent;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition);
    }}

    .social-icon-circle:hover {{
      transform: translateY(-3px);
      opacity: 0.85;
    }}

    .footer-col-title {{
      font-family: var(--font-sans);
      font-size: 1.0625rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 20px;
    }}

    .footer-links-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding: 0;
      margin: 0;
    }}

    .footer-links-list a {{
      font-size: 0.92rem;
      color: #4b5563;
      font-weight: 500;
      text-decoration: none;
    }}

    .footer-links-list a:hover {{
      color: var(--color-asci-teal);
    }}

    .footer-bottom-bar {{
      background: #000000;
      color: #94a3b8;
      font-size: 0.8125rem;
      padding: 14px 0;
    }}

    .footer-bottom-flex {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .footer-legal-links {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .footer-legal-links a {{
      color: inherit;
      text-decoration: none;
    }}

    .footer-legal-links a:hover {{
      color: #ffffff;
    }}

    @media (max-width: 991px) {{
      .footer-top-grid {{
        grid-template-columns: 1fr;
        gap: 32px;
      }}
      .footer-bottom-flex {{
        flex-direction: column;
        gap: 12px;
        text-align: center;
      }}
      .cta-callout-title {{
        font-size: 2.1rem;
      }}
      .gallery-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>

<body>
  {header_block}

  <!-- Directory Hero Section (Institutional Style Matching people.html) -->
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

      <div class="gallery-empty-state" id="galleryEmpty">
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

  {footer_block}

  <!-- Gallery, Lightbox & 3D Ripple Scripts -->
  <script>
    const campaignItems = {items_json};

    let currentTypeFilter = 'all';
    let currentYearFilter = 'all';
    let currentSearchQuery = '';

    function renderGallery() {{
      const grid = document.getElementById('campaignsGrid');
      const emptyState = document.getElementById('galleryEmpty');
      const countLabel = document.getElementById('visibleCount');

      const filtered = campaignItems.filter(item => {{
        // Type filter
        if (currentTypeFilter !== 'all' && item.type !== currentTypeFilter) return false;
        // Year filter
        if (currentYearFilter !== 'all' && item.year !== currentYearFilter) return false;
        // Search query
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
      yearEl.textContent = `Campaign Year: ${{item.year}}`;

      if (item.type === 'video') {{
        playerWrap.innerHTML = `
          <iframe class="media-modal-iframe" src="https://www.youtube.com/embed/${{item.yt_id}}?autoplay=1&rel=0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        `;
        extLink.href = item.video_url || `https://www.youtube.com/watch?v=${{item.yt_id}}`;
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
      modal.classList.remove('open');
      playerWrap.innerHTML = ''; // stops youtube playback immediately
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

    // ================= RESPONSIBLE ADVERTISING 3D RIPPLE ANIMATION =================
    function initRippleCanvas() {{
      const rippleCanvas = document.getElementById('ctaRippleCanvas');
      if (!rippleCanvas) return;
      const ctx = rippleCanvas.getContext('2d');
      let offset = 0;
      let time = 0;

      function resizeCanvas() {{
        const rect = rippleCanvas.parentElement.getBoundingClientRect();
        const dpr = window.devicePixelRatio || 1;
        rippleCanvas.width = rect.width * dpr;
        rippleCanvas.height = rect.height * dpr;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      }}

      window.addEventListener('resize', resizeCanvas);
      resizeCanvas();

      function drawRipples() {{
        const rect = rippleCanvas.parentElement.getBoundingClientRect();
        const width = rect.width;
        const height = rect.height;

        ctx.clearRect(0, 0, width, height);

        const cx = width * 0.14;
        const cy = height * 0.5;

        // Draw central dot
        const centerDotWave = (Math.sin(-time * 1.5) + 1) / 2;
        ctx.beginPath();
        ctx.arc(cx, cy, 3.5, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(255, 255, 255, " + (0.3 + centerDotWave * 0.2).toFixed(3) + ")";
        ctx.fill();

        const step = 15;
        const speed = 0.25;
        offset = (offset + speed) % step;
        time += 0.022;

        const maxRadius = Math.hypot(Math.max(cx, width - cx), Math.max(cy, height - cy)) + step;
        const totalRings = Math.ceil(maxRadius / step);

        for (let i = 0; i <= totalRings; i++) {{
          const r = i * step + offset;
          if (r <= 4) continue;

          let opacity = 0.08;
          const wave = Math.sin(r * 0.015 - time * 1.5);
          const waveNorm = (wave + 1) / 2;
          opacity += waveNorm * 0.20;

          if (r > maxRadius - 100) {{
            opacity *= Math.max(0, (maxRadius - r) / 100);
          }}

          ctx.beginPath();
          ctx.arc(cx, cy, r, 0, Math.PI * 2);
          ctx.strokeStyle = "rgba(255, 255, 255, " + opacity.toFixed(3) + ")";
          ctx.lineWidth = 1.2 + waveNorm * 0.6;
          ctx.stroke();
        }}

        requestAnimationFrame(drawRipples);
      }}

      requestAnimationFrame(drawRipples);
    }}

    // Initialize gallery and animations on load
    document.addEventListener('DOMContentLoaded', () => {{
      renderGallery();
      initRippleCanvas();
    }});
  </script>
</body>
</html>
'''

    with open('campaigns.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print("campaigns.html successfully generated! Total size:", len(page_html))

    with open('ad-campaigns.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print("ad-campaigns.html successfully generated! Total size:", len(page_html))

if __name__ == '__main__':
    build()
