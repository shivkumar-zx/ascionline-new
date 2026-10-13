import json
import re

# 1. Video Data from ascionline.in/asci-explained/
videos_data = [
    {
        "id": "9ftdKChre9U",
        "title": "Self-Regulation & ASCI",
        "category": "mandate",
        "category_label": "Mandate & Framework",
        "topic": "Self-Regulation Foundations",
        "description": "Understanding the philosophy, structure, and foundation of self-regulation in Indian advertising and ASCI's role in protecting consumers.",
    },
    {
        "id": "EjMGv8mQOrU",
        "title": "Overview of The ASCI Code",
        "category": "code",
        "category_label": "The ASCI Code",
        "topic": "Code Architecture",
        "description": "An essential primer on the core principles and four fundamental chapters of the Advertising Standards Council of India Code.",
    },
    {
        "id": "CAetoWmQJ14",
        "title": "Chapter 1 of the ASCI Code - Misleading Ads",
        "category": "code",
        "category_label": "The ASCI Code",
        "topic": "Chapter 1: Honest Representations",
        "description": "Standards ensuring advertisements are truthful, honest, and do not mislead consumers through ambiguous claims, exaggerations, or omissions.",
    },
    {
        "id": "H3U29WLLY8U",
        "title": "Chapter 2 of the ASCI Code - Offensive or Indecent Ads",
        "category": "code",
        "category_label": "The ASCI Code",
        "topic": "Chapter 2: Public Decency",
        "description": "Guidelines safeguarding public decency and ensuring ads do not cause grave or widespread offense across communities.",
    },
    {
        "id": "bgARAle-I9M",
        "title": "Chapter 3 of the ASCI Code - Against Harmful Products or Situations",
        "category": "code",
        "category_label": "The ASCI Code",
        "topic": "Chapter 3: Safety & Harm",
        "description": "Rules prohibiting promotions that encourage hazardous practices, unsafe products, dangerous acts, or disregard for human safety.",
    },
    {
        "id": "ngZt9ywSkzo",
        "title": "Chapter 4 of the ASCI Code - Fairness in Competition",
        "category": "code",
        "category_label": "The ASCI Code",
        "topic": "Chapter 4: Fair Competition",
        "description": "Ensuring fair play among competitors, preventing unjustified disparagement, plagiarism, and misleading comparative advertising.",
    },
    {
        "id": "ywPKLN-xhhU",
        "title": "Sector or Issue Based Guidelines",
        "category": "code",
        "category_label": "The ASCI Code",
        "topic": "Special Sector Guidelines",
        "description": "Specialized guidelines covering high-impact sectors including food & beverage, online real-money gaming, education, healthcare, and influencer marketing.",
    },
    {
        "id": "AfB2z0Qg7w8",
        "title": "The ASCI Code - A Living Document",
        "category": "code",
        "category_label": "The ASCI Code",
        "topic": "Evolution & Modernization",
        "description": "How the ASCI Code dynamically evolves with emerging media technologies, generative AI, dark patterns, and evolving consumer habits.",
    },
    {
        "id": "Hy5ft7b3uDw",
        "title": "ASCI's Complaint Management Process",
        "category": "complaints",
        "category_label": "Complaints & Appeals",
        "topic": "Complaint Handling Workflow",
        "description": "A step-by-step walkthrough of how complaints from consumers, industry rivals, and suo-motu monitoring are received and processed.",
    },
    {
        "id": "nb7xI1MAA1E",
        "title": "ASCI's Complaint Management Appeals Process",
        "category": "complaints",
        "category_label": "Complaints & Appeals",
        "topic": "Independent Review Panel",
        "description": "How the Independent Review Panel (IRP) provides an impartial, judicial review mechanism for parties seeking appeal against recommendations.",
    },
    {
        "id": "L8eYPMu4_DA",
        "title": "Process in Case of Non-Compliance",
        "category": "governance",
        "category_label": "Governance & Enforcement",
        "topic": "Non-Compliance Escalation",
        "description": "Escalation procedures, statutory regulator referrals (CCPA, Ministry of I&B, FSSAI), and public disclosures when an advertiser fails to comply.",
    },
    {
        "id": "mUQfdYKByEY",
        "title": "Managing Conflict of Interest",
        "category": "governance",
        "category_label": "Governance & Enforcement",
        "topic": "Ethical Governance",
        "description": "Institutional safeguards ensuring CCC and Board members recuse themselves whenever any potential conflict of interest arises.",
    },
    {
        "id": "aTZehrTW0k8",
        "title": "ASCI Complaint Resolution Time-Frame",
        "category": "complaints",
        "category_label": "Complaints & Appeals",
        "topic": "Resolution Timelines",
        "description": "Predictable, transparent turnaround times for complaint handling, advertiser responses, technical consultations, and committee rulings.",
    },
    {
        "id": "5kf6bfwLZcI",
        "title": "ASCI's Mandate",
        "category": "mandate",
        "category_label": "Mandate & Framework",
        "topic": "Statutory Recognition",
        "description": "The official scope and statutory recognition of ASCI under the Cable Television Networks (Regulation) Act and Central Consumer Protection Authority.",
    },
    {
        "id": "OHNd9lPE4uI",
        "title": "ASCI's Own Surveillance Framework",
        "category": "governance",
        "category_label": "Governance & Enforcement",
        "topic": "Proactive Surveillance",
        "description": "Proactive, multi-media AI surveillance scanning thousands of print advertisements, television broadcasts, and digital campaigns daily across India.",
    },
    {
        "id": "Q_o36jBBX4E",
        "title": "Ensuring Fairness in Complaint Hearings and Process",
        "category": "complaints",
        "category_label": "Complaints & Appeals",
        "topic": "Principles of Natural Justice",
        "description": "Upholding principles of natural justice through informal hearings and providing full opportunities for advertisers to submit substantiation.",
    },
    {
        "id": "JXmuc--tkys",
        "title": "ASCI's Ability to Drive Compliance",
        "category": "governance",
        "category_label": "Governance & Enforcement",
        "topic": "High Voluntary Compliance",
        "description": "Achieving more than 95% voluntary compliance across India through industry cooperation, public trust, and strong regulatory partnerships.",
    },
    {
        "id": "OvdTNlRfINI",
        "title": "ASCI's Initiatives to Promote Responsible Advertising",
        "category": "initiatives",
        "category_label": "Initiatives & Academy",
        "topic": "Pre-Emptive Solutions",
        "description": "Proactive industry services like Advertising Advice, Endorser Due Diligence, and Ad Check that resolve issues before campaigns go live.",
    },
    {
        "id": "yRFQR4wCJPY",
        "title": "ASCI Academy Overview",
        "category": "initiatives",
        "category_label": "Initiatives & Academy",
        "topic": "Education & Capability Building",
        "description": "Empowering marketers, creative agencies, creators, and students to embed ethical, consumer-first standards into everyday advertising practices.",
    },
]

def build_asci_explained():
    with open('head_part.html', 'r', encoding='utf-8') as f:
        head_raw = f.read()

    with open('header_part.html', 'r', encoding='utf-8') as f:
        header_raw = f.read()

    with open('footer_part.html', 'r', encoding='utf-8') as f:
        footer_part = f.read()

    with open('footer_scripts.html', 'r', encoding='utf-8') as f:
        footer_scripts = f.read()

    menu_item_asci_explained = '''              <li class="megamenu-link-item">
                <a href="asci-explained.html">
                  <span>ASCI Explained</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
'''

    # Ensure ASCI Explained link is present before Subscribe to newsletter
    def inject_menu_item(html_str):
        if 'href="asci-explained.html"' in html_str:
            return html_str
        target = r'(<li class="megamenu-link-item">\s*<a href="about-us\.html#newsletter">\s*<span>Subscribe to newsletter</span>)'
        if re.search(target, html_str):
            return re.sub(target, menu_item_asci_explained + r'\1', html_str, count=1)
        return html_str

    header_clean = inject_menu_item(header_raw)

    # CSS for ASCI Explained page matching campaigns.html exactly
    explained_css = """
    /* ================= ASCI EXPLAINED HERO (Matching campaigns.html) ================= */
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
      max-width: 740px;
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
      font-size: 2.35rem;
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

    /* Crosshair Stats Grid with Gradient Dividers (Identical to campaigns.html & people.html) */
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
      padding: 30px 24px;
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
        margin-top: 16px;
      }
    }

    /* ================= MAIN SECTION & FLOATING STICKY CONTROLS CARD ================= */
    .explained-main-section {
      padding: 36px 0 80px;
      background-color: #f8fafc;
      min-height: 80vh;
    }

    .directory-controls-card {
      position: sticky;
      top: 105px;
      z-index: 40;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(226, 232, 240, 0.85);
      border-radius: var(--radius-md);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.03);
      padding: 14px 20px;
      margin-bottom: 28px;
    }

    .controls-single-row {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    .search-input-box {
      display: flex;
      align-items: center;
      gap: 10px;
      background: #f1f5f9;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-pill);
      padding: 8px 16px;
      flex: 1;
      min-width: 240px;
      transition: var(--transition);
    }

    .search-input-box:focus-within {
      background: #ffffff;
      border-color: #008779;
      box-shadow: 0 0 0 3px rgba(0, 135, 121, 0.12);
    }

    .search-input-box input {
      border: none;
      outline: none;
      background: transparent;
      width: 100%;
      font-size: 0.9rem;
      color: #0f172a;
      font-family: inherit;
    }

    .controls-divider {
      width: 1px;
      height: 28px;
      background: #e2e8f0;
      flex-shrink: 0;
    }

    .filter-topic-group {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }

    .filter-topic-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 14px;
      border-radius: var(--radius-pill);
      font-size: 0.82rem;
      font-weight: 600;
      color: #475569;
      background: transparent;
      border: 1px solid transparent;
      transition: all 0.15s ease;
      cursor: pointer;
    }

    .filter-topic-btn:hover {
      background: #f1f5f9;
      color: #0f172a;
    }

    .filter-topic-btn.active {
      background: #008779;
      color: #ffffff;
      border-color: #008779;
      box-shadow: 0 2px 8px rgba(0, 135, 121, 0.25);
    }

    .filter-topic-count {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
      background: rgba(0, 0, 0, 0.08);
      color: inherit;
      padding: 1px 7px;
      border-radius: 9999px;
      font-weight: 700;
    }

    .filter-topic-btn.active .filter-topic-count {
      background: rgba(255, 255, 255, 0.22);
      color: #ffffff;
    }

    /* Gallery Meta Header */
    .gallery-header-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
      padding: 0 4px;
    }

    .gallery-count-badge {
      font-size: 0.95rem;
      color: #64748b;
    }

    .gallery-count-badge strong {
      color: #0f172a;
      font-weight: 700;
    }

    /* ================= VIDEO CARDS GRID (Matching campaigns.html) ================= */
    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }

    @media (max-width: 1024px) {
      .gallery-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
      }
    }

    @media (max-width: 640px) {
      .gallery-grid {
        grid-template-columns: 1fr;
        gap: 20px;
      }
      .directory-controls-card {
        top: 75px;
      }
    }

    .gallery-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      position: relative;
    }

    .gallery-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 16px 32px -8px rgba(0, 0, 0, 0.1);
      border-color: #cbd5e1;
    }

    .gallery-thumb-wrap {
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      background: #0f172a;
      overflow: hidden;
    }

    .gallery-thumb-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.35s ease;
    }

    .gallery-card:hover .gallery-thumb-img {
      transform: scale(1.05);
    }

    .gallery-category-badge {
      position: absolute;
      top: 12px;
      left: 12px;
      z-index: 2;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 9999px;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      background: rgba(0, 135, 121, 0.92);
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(0, 135, 121, 0.35);
    }

    .gallery-format-badge {
      position: absolute;
      top: 12px;
      right: 12px;
      z-index: 2;
      background: rgba(15, 23, 42, 0.75);
      color: #ffffff;
      font-size: 0.72rem;
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
      background: rgba(15, 23, 42, 0.12);
    }

    .play-btn-circle {
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .gallery-card:hover .play-btn-circle {
      transform: scale(1.15);
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
      padding: 20px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .gallery-topic-sub {
      font-size: 0.78rem;
      font-weight: 700;
      color: #008779;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }

    .gallery-card-title {
      font-family: var(--font-serif);
      font-size: 1.15rem;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.35;
      margin-bottom: 8px;
    }

    .gallery-card-desc {
      font-size: 0.88rem;
      color: #64748b;
      line-height: 1.5;
      margin-bottom: 16px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .gallery-card-footer {
      margin-top: auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.84rem;
      font-weight: 600;
      color: #008779;
      padding-top: 12px;
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

    # Head preparation
    title = "ASCI Explained – The Advertising Standards Council of India (ASCI)"
    desc = "Learn about ASCI and self-regulation in advertising, covering the ASCI Code, complaint management, compliance, fairness, and initiatives for responsible ads."
    head_custom = head_raw
    head_custom = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head_custom)
    head_custom = re.sub(r'<meta\s+name="description"\s+content=".*?"', f'<meta name="description" content="{desc}"', head_custom, flags=re.DOTALL)
    head_custom = head_custom.replace('</head>', f'\n<style>\n{explained_css}\n</style>\n</head>')

    items_json = json.dumps(videos_data, ensure_ascii=False)

    # Body HTML
    body_html = f'''
  <!-- Directory Hero Section (Matching campaigns.html) -->
  <section class="directory-hero">
    <div class="container">
      <div class="breadcrumb-nav">
        <a href="index.html">Home</a>
        <span>/</span>
        <a href="about-us.html">About Us</a>
        <span>/</span>
        <span>ASCI Explained</span>
      </div>

      <div class="directory-hero-content-wrapper">
        <div class="directory-hero-left">
          <div class="campaigns-badge">
            <span class="campaigns-badge-dot"></span>
            <span>Self-Regulation &amp; Institutional Framework</span>
          </div>
          <h1 class="directory-page-title">ASCI Explained</h1>
          <p class="directory-page-desc">
            Learn about ASCI and self-regulation in advertising, covering the ASCI Code, complaint management, compliance, fairness, and initiatives for responsible ads. Watch official explainer video films across core governance topics.
          </p>
        </div>

        <div class="directory-hero-right">
          <!-- Crosshair Stats Grid matching campaigns.html & people.html -->
          <div class="directory-stats-grid">
            <div class="stat-cell">
              <div class="stat-number">19</div>
              <div class="stat-label">Video Explainers</div>
            </div>
            <div class="stat-cell">
              <div class="stat-number">4</div>
              <div class="stat-label">Core Code Chapters</div>
            </div>
            <div class="stat-cell">
              <div class="stat-number">6</div>
              <div class="stat-label">Knowledge Topics</div>
            </div>
            <div class="stat-cell">
              <div class="stat-number">95%+</div>
              <div class="stat-label">Voluntary Compliance</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Section with Floating Controls Card -->
  <section class="explained-main-section" id="explained">
    <div class="container">
      <!-- Floating Sticky Controls Card -->
      <div class="directory-controls-card">
        <div class="controls-single-row">
          <!-- Live Instant Search with Pill styling -->
          <div class="search-input-box">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input type="text" id="explainedSearch" placeholder="Search explainer videos..." oninput="handleSearch(this.value)" />
          </div>

          <!-- Vertical Divider -->
          <div class="controls-divider"></div>

          <!-- Topic Filter Tabs -->
          <div class="filter-topic-group" id="topicFilterGroup">
            <button class="filter-topic-btn active" data-cat="all" onclick="setTopicCategory('all', this)">
              <span>All Topics</span>
              <span class="filter-topic-count">19</span>
            </button>
            <button class="filter-topic-btn" data-cat="code" onclick="setTopicCategory('code', this)">
              <span>The ASCI Code</span>
              <span class="filter-topic-count">7</span>
            </button>
            <button class="filter-topic-btn" data-cat="complaints" onclick="setTopicCategory('complaints', this)">
              <span>Complaints &amp; Appeals</span>
              <span class="filter-topic-count">4</span>
            </button>
            <button class="filter-topic-btn" data-cat="governance" onclick="setTopicCategory('governance', this)">
              <span>Governance &amp; Enforcement</span>
              <span class="filter-topic-count">4</span>
            </button>
            <button class="filter-topic-btn" data-cat="initiatives" onclick="setTopicCategory('initiatives', this)">
              <span>Initiatives &amp; Academy</span>
              <span class="filter-topic-count">2</span>
            </button>
            <button class="filter-topic-btn" data-cat="mandate" onclick="setTopicCategory('mandate', this)">
              <span>Mandate &amp; Framework</span>
              <span class="filter-topic-count">2</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Gallery Meta Header -->
      <div class="gallery-header-meta">
        <div class="gallery-count-badge">
          Showing <strong id="visibleCount">{len(videos_data)}</strong> explainer videos
        </div>
      </div>

      <!-- Videos Gallery Grid -->
      <div class="gallery-grid" id="explainedGrid">
        <!-- Rendered dynamically via JavaScript -->
      </div>

      <div class="gallery-empty-state" id="galleryEmpty" style="display: none;">
        <svg class="gallery-empty-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="8" y1="12" x2="16" y2="12"></line>
        </svg>
        <h3 class="gallery-empty-title">No explainer videos found</h3>
        <p class="gallery-empty-desc">Try searching for terms like &lsquo;Code&rsquo;, &lsquo;Misleading&rsquo;, or select &lsquo;All Topics&rsquo;.</p>
      </div>
    </div>
  </section>

  <!-- Video Lightbox Modal with Left & Right Navigation Arrows -->
  <div class="media-modal-backdrop" id="mediaModal" onclick="closeModalOnBackdrop(event)">
    <div class="media-modal-container">
      <div class="media-modal-header">
        <div class="media-modal-header-left">
          <div class="media-modal-title" id="modalTitle">ASCI Explainer Video</div>
          <div class="media-modal-counter" id="modalCounter">1 of 19</div>
        </div>
        <button class="media-modal-close-btn" onclick="closeMediaModal()" aria-label="Close modal">✕</button>
      </div>

      <div class="media-modal-player-wrap" id="modalPlayerContent">
        <!-- Injected dynamically -->
      </div>

      <!-- Previous & Next Navigation Arrows -->
      <button class="modal-nav-btn modal-prev-btn" onclick="navigateModal(-1)" aria-label="Previous video">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      <button class="modal-nav-btn modal-next-btn" onclick="navigateModal(1)" aria-label="Next video">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>

      <div class="media-modal-footer">
        <span id="modalMetaTopic">Topic: Overview</span>
        <div class="media-modal-footer-nav-hint">Tip: Use &larr; &rarr; arrow keys to browse, Esc to close</div>
        <a href="#" target="_blank" rel="noopener noreferrer" class="btn-external-link" id="modalExternalLink">
          <span>Watch on YouTube</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="7" y1="17" x2="17" y2="7"></line>
            <polyline points="7 7 17 7 17 17"></polyline>
          </svg>
        </a>
      </div>
    </div>
  </div>
'''

    # JavaScript logic
    script_html = f'''
  <script>
    const explainerVideos = {items_json};

    let currentCategory = 'all';
    let currentSearchQuery = '';
    let currentFilteredVideos = [];
    let currentModalIndex = 0;

    function renderGallery() {{
      const grid = document.getElementById('explainedGrid');
      const emptyState = document.getElementById('galleryEmpty');
      const countLabel = document.getElementById('visibleCount');
      if (!grid || !emptyState || !countLabel) return;

      currentFilteredVideos = explainerVideos.filter(item => {{
        if (currentCategory !== 'all' && item.category !== currentCategory) return false;
        if (currentSearchQuery.trim() !== '') {{
          const q = currentSearchQuery.toLowerCase();
          const matchTitle = item.title.toLowerCase().includes(q);
          const matchTopic = item.topic.toLowerCase().includes(q);
          const matchDesc = item.description.toLowerCase().includes(q);
          if (!matchTitle && !matchTopic && !matchDesc) return false;
        }}
        return true;
      }});

      countLabel.textContent = currentFilteredVideos.length;

      if (currentFilteredVideos.length === 0) {{
        grid.style.display = 'none';
        emptyState.style.display = 'block';
        return;
      }}

      grid.style.display = 'grid';
      emptyState.style.display = 'none';

      grid.innerHTML = currentFilteredVideos.map((item, idx) => {{
        const thumbUrl = `https://img.youtube.com/vi/${{item.id}}/hqdefault.jpg`;
        return `
          <div class="gallery-card" onclick="openMediaModalByIndex(${{idx}})">
            <div class="gallery-thumb-wrap">
              <span class="gallery-category-badge">${{item.category_label}}</span>
              <span class="gallery-format-badge">HD Explainer</span>
              <img src="${{thumbUrl}}" alt="${{item.title}}" class="gallery-thumb-img" loading="lazy" onerror="this.src='https://i.ytimg.com/vi/${{item.id}}/hqdefault.jpg'" />
              <div class="video-play-overlay">
                <div class="play-btn-circle">
                  <div class="play-icon-tri"></div>
                </div>
              </div>
            </div>
            <div class="gallery-card-body">
              <div class="gallery-topic-sub">${{item.topic}}</div>
              <h3 class="gallery-card-title">${{item.title}}</h3>
              <p class="gallery-card-desc">${{item.description}}</p>
              <div class="gallery-card-footer">
                <span>Watch Explainer Film</span>
                <span>&rarr;</span>
              </div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function setTopicCategory(cat, btn) {{
      currentCategory = cat;
      document.querySelectorAll('#topicFilterGroup .filter-topic-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderGallery();
    }}

    function handleSearch(val) {{
      currentSearchQuery = val;
      renderGallery();
    }}

    function openMediaModalByIndex(index) {{
      if (!currentFilteredVideos || currentFilteredVideos.length === 0) return;
      if (index < 0) index = currentFilteredVideos.length - 1;
      if (index >= currentFilteredVideos.length) index = 0;
      currentModalIndex = index;

      const item = currentFilteredVideos[currentModalIndex];
      if (!item) return;

      const modal = document.getElementById('mediaModal');
      const playerWrap = document.getElementById('modalPlayerContent');
      const titleEl = document.getElementById('modalTitle');
      const counterEl = document.getElementById('modalCounter');
      const metaTopicEl = document.getElementById('modalMetaTopic');
      const extLink = document.getElementById('modalExternalLink');

      titleEl.textContent = item.title;
      counterEl.textContent = `${{currentModalIndex + 1}} of ${{currentFilteredVideos.length}}`;
      metaTopicEl.textContent = `Topic: ${{item.category_label}} · ${{item.topic}}`;

      playerWrap.innerHTML = `
        <iframe class="media-modal-iframe" src="https://www.youtube-nocookie.com/embed/${{item.id}}?autoplay=1&rel=0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      `;
      extLink.href = 'https://www.youtube.com/watch?v=' + item.id;

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

    // Immediate gallery rendering on load
    renderGallery();
    document.addEventListener('DOMContentLoaded', renderGallery);
  </script>
'''

    full_page = f"{head_custom}\n{header_clean}\n{body_html}\n{script_html}\n{footer_part}\n{footer_scripts}"

    with open('asci-explained.html', 'w', encoding='utf-8') as f:
        f.write(full_page)
    print("asci-explained.html successfully generated! Size:", len(full_page))

    # Also update header_part.html with the new menu item
    with open('header_part.html', 'w', encoding='utf-8') as f:
        f.write(header_clean)
    print("header_part.html updated with ASCI Explained link!")

    # Update other major HTML files
    target_files = [
        'campaigns.html',
        'ad-campaigns.html',
        'index.html',
        'about-us.html',
        'people.html',
        'annual-reports.html'
    ]

    for filename in target_files:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            updated = inject_menu_item(content)
            if updated != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(updated)
                print(f"Updated {filename} with ASCI Explained link in About Us dropdown!")
            else:
                print(f"{filename} already has link or match not found.")
        except Exception as e:
            print(f"Error updating {filename}: {e}")

if __name__ == '__main__':
    build_asci_explained()
