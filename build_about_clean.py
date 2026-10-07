import os
import json

# Read shared building blocks
with open('head_part.html', 'r', encoding='utf-8') as f:
    head_raw = f.read()

with open('header_part.html', 'r', encoding='utf-8') as f:
    header_clean = f.read()

with open('footer_part.html', 'r', encoding='utf-8') as f:
    footer_part = f.read()

with open('footer_scripts.html', 'r', encoding='utf-8') as f:
    footer_scripts = f.read()

def assemble_page(title, description, custom_css, body_html):
    # Inject title and description
    head_custom = head_raw
    # Replace title
    import re
    head_custom = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head_custom)
    head_custom = re.sub(r'<meta\s+name="description"\s+content=".*?"', f'<meta name="description" content="{description}"', head_custom, flags=re.DOTALL)
    
    # Inject custom CSS before </head>
    css_injection = f"\n<style>\n{custom_css}\n</style>\n</head>"
    head_custom = head_custom.replace('</head>', css_injection)
    
    full_html = f"{head_custom}\n{header_clean}\n{body_html}\n{footer_part}\n{footer_scripts}"
    return full_html

# =========================================================================
# 1. BUILD ABOUT-US.HTML
# =========================================================================
about_title = "About Us – The Advertising Standards Council of India (ASCI)"
about_desc = "Learn about ASCI, established in 1985 as an independent self-regulatory body ensuring advertising in India is honest, decent, safe, and fair."

about_css = """
/* ================= ABOUT US PAGE STYLES ================= */
.about-hero {
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
  padding: 56px 0 48px;
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

.about-page-title {
  font-family: var(--font-serif);
  font-size: 2.5rem;
  color: #0f172a;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 16px;
}

.about-page-lead {
  font-size: 1.125rem;
  color: #334155;
  max-width: 860px;
  line-height: 1.7;
  margin-bottom: 32px;
}

.badge-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.about-badge {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: var(--radius-pill);
  padding: 8px 18px;
  font-size: 0.875rem;
  font-weight: 600;
  color: #1e293b;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.about-badge-icon {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #008779;
}

/* Section Common */
.about-section {
  padding: 72px 0;
  border-bottom: 1px solid #f1f5f9;
}

.section-eyebrow {
  font-size: 0.825rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #008779;
  margin-bottom: 10px;
}

.section-heading {
  font-family: var(--font-serif);
  font-size: 2rem;
  font-weight: 700;
  color: #0f172a;
  line-height: 1.3;
  margin-bottom: 16px;
}

.section-intro-text {
  font-size: 1.025rem;
  color: #475569;
  max-width: 780px;
  line-height: 1.65;
  margin-bottom: 40px;
}

/* 4 Pillars Grid */
.pillars-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
}

.pillar-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 28px 24px;
  transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
}

.pillar-card:hover {
  transform: translateY(-4px);
  border-color: #008779;
  box-shadow: 0 12px 24px rgba(0, 135, 121, 0.08);
}

.pillar-number {
  font-family: var(--font-serif);
  font-size: 1.75rem;
  font-weight: 700;
  color: #008779;
  margin-bottom: 12px;
}

.pillar-title {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 10px;
}

.pillar-desc {
  font-size: 0.925rem;
  color: #475569;
  line-height: 1.6;
}

/* Work Two-Column Split */
.work-split-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  margin-bottom: 32px;
}

.work-col-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 32px;
}

.work-box-badge {
  display: inline-block;
  font-size: 0.775rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 4px 12px;
  border-radius: var(--radius-pill);
  margin-bottom: 16px;
}

.work-box-badge.preventive {
  background: #ccfbf1;
  color: #0f766e;
}

.work-box-badge.corrective {
  background: #fee2e2;
  color: #991b1b;
}

.work-box-title {
  font-family: var(--font-serif);
  font-size: 1.35rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 12px;
}

.work-box-desc {
  font-size: 0.95rem;
  color: #475569;
  line-height: 1.65;
  margin-bottom: 18px;
}

.work-bullet-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.work-bullet-list li {
  font-size: 0.925rem;
  color: #334155;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  line-height: 1.5;
}

.work-bullet-list li::before {
  content: '✓';
  color: #008779;
  font-weight: 700;
}

/* Governance Tripartite Section */
.governance-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
  margin-bottom: 36px;
}

.gov-summary-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 28px;
}

.gov-card-tag {
  font-size: 0.775rem;
  font-weight: 700;
  text-transform: uppercase;
  color: #008779;
  margin-bottom: 8px;
}

.gov-card-title {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 10px;
}

.gov-card-desc {
  font-size: 0.925rem;
  color: #475569;
  line-height: 1.6;
}

/* Decade Timeline Preview */
.timeline-preview-wrap {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 20px;
  margin-bottom: 32px;
}

.decade-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  padding: 22px;
  border-left: 4px solid #008779;
}

.decade-year {
  font-family: var(--font-serif);
  font-size: 1.35rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 6px;
}

.decade-text {
  font-size: 0.885rem;
  color: #475569;
  line-height: 1.55;
}

/* Resource Banner Card */
.resource-banner-card {
  background: #042f2e;
  border-radius: 20px;
  padding: 44px 40px;
  color: #ffffff;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.resource-banner-content h3 {
  font-family: var(--font-serif);
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: 8px;
}

.resource-banner-content p {
  color: #ccfbf1;
  font-size: 1rem;
  max-width: 600px;
  line-height: 1.6;
}

.btn-banner-action {
  background: #008779;
  color: #ffffff;
  padding: 12px 26px;
  border-radius: var(--radius-pill);
  font-size: 0.95rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: var(--transition);
  text-decoration: none;
}

.btn-banner-action:hover {
  background: #ffffff;
  color: #042f2e;
}

.btn-text-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.95rem;
  font-weight: 600;
  color: #008779;
  text-decoration: none;
}

.btn-text-link:hover {
  text-decoration: underline;
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .work-split-grid {
    grid-template-columns: 1fr;
  }
  .resource-banner-card {
    padding: 32px 24px;
  }
}
"""

about_body = """
  <!-- About Hero Section -->
  <section class="about-hero">
    <div class="container">
      <div class="breadcrumb-nav">
        <a href="ASCI (3).html">Home</a>
        <span>/</span>
        <span>About Us</span>
      </div>

      <h1 class="about-page-title">About ASCI</h1>
      <p class="about-page-lead">
        The Advertising Standards Council of India (ASCI), established in 1985, is a voluntary self-regulatory organisation committed to the cause of self-regulation in advertising. ASCI ensures the protection of consumer interests while maintaining fairness to the advertising industry.
      </p>

      <div class="badge-strip">
        <div class="about-badge">
          <span class="about-badge-icon"></span>
          Founded in 1985
        </div>
        <div class="about-badge">
          <span class="about-badge-icon"></span>
          Tripartite Industry Stewardship
        </div>
        <div class="about-badge">
          <span class="about-badge-icon"></span>
          Statutory Recognition Under Cable TV Act
        </div>
        <div class="about-badge">
          <span class="about-badge-icon"></span>
          EASA &amp; ICAS Global Affiliate
        </div>
      </div>
    </div>
  </section>

  <!-- 1. Purpose & 4 Foundational Pillars -->
  <section class="about-section" id="purpose">
    <div class="container">
      <div class="section-eyebrow">Our Purpose &amp; Code</div>
      <h2 class="section-heading">Four Principles of Responsible Advertising</h2>
      <p class="section-intro-text">
        Formed with the joint support of all key sectors connected with advertising—advertisers, advertising agencies, media (broadcasters, digital platforms, press), and market researchers—the ASCI Code is structured upon four enduring principles:
      </p>

      <div class="pillars-grid">
        <div class="pillar-card">
          <div class="pillar-number">01</div>
          <h3 class="pillar-title">Truthful &amp; Honest</h3>
          <p class="pillar-desc">
            Advertisements must be truthful and capable of objective substantiation. Claims must not mislead consumers through ambiguity, omission, or exaggeration.
          </p>
        </div>

        <div class="pillar-card">
          <div class="pillar-number">02</div>
          <h3 class="pillar-title">Non-Offensive to Decency</h3>
          <p class="pillar-desc">
            Commercial messages must respect prevailing standards of public decency and refrain from offensive, discriminatory, or derogatory depictions.
          </p>
        </div>

        <div class="pillar-card">
          <div class="pillar-number">03</div>
          <h3 class="pillar-title">Safeguard Against Harm</h3>
          <p class="pillar-desc">
            Advertisements must not promote hazardous practices, encourage unsafe behavior, or exploit the natural credulity of vulnerable groups, particularly children.
          </p>
        </div>

        <div class="pillar-card">
          <div class="pillar-number">04</div>
          <h3 class="pillar-title">Fair in Competition</h3>
          <p class="pillar-desc">
            Encouraging healthy commercial competition without unfair disparagement or attacks against competitors or other products in the market.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. What We Do & Our Impact -->
  <section class="about-section" id="work">
    <div class="container">
      <div class="section-eyebrow">Operational Framework</div>
      <h2 class="section-heading">How ASCI Protects Consumers &amp; Guides Advertisers</h2>
      <p class="section-intro-text">
        ASCI operates on both ends of the creative lifecycle: supporting creators to get it right before release, and correcting misleading advertisements after they appear.
      </p>

      <div class="work-split-grid">
        <!-- Preventive -->
        <div class="work-col-box">
          <span class="work-box-badge preventive">Preventive Support</span>
          <h3 class="work-box-title">Pre-Production Guidance &amp; Training</h3>
          <p class="work-box-desc">
            Minimizing regulatory risk and protecting consumer trust before campaigns reach the public:
          </p>
          <ul class="work-bullet-list">
            <li><strong>Advertising Advice:</strong> Confidential pre-release copy advice for brand teams.</li>
            <li><strong>Endorser Due Diligence:</strong> Regulatory verification tools for celebrity and influencer partnerships.</li>
            <li><strong>ASCI Academy:</strong> Sectoral courses on dark patterns, privacy, green claims, and ad literacy.</li>
            <li><strong>Topic Guidelines:</strong> Clear boundaries for emerging categories including AI, influencer disclosures, and green claims.</li>
          </ul>
        </div>

        <!-- Corrective -->
        <div class="work-col-box">
          <span class="work-box-badge corrective">Corrective Enforcement</span>
          <h3 class="work-box-title">Complaint Handling &amp; Active Monitoring</h3>
          <p class="work-box-desc">
            Ensuring speedy, fair redressal when advertisements violate standards:
          </p>
          <ul class="work-bullet-list">
            <li><strong>TARA Complaint Portal:</strong> Free, multilingual mechanism for consumers to lodge complaints.</li>
            <li><strong>Proactive Digital Monitoring (NAMS):</strong> Scanning over 3,000 digital platforms, websites, and TV broadcasts.</li>
            <li><strong>Consumer Complaints Council (CCC):</strong> Independent deliberation with 50%+ civil society representation.</li>
            <li><strong>Regulatory Coordination:</strong> Ongoing collaboration with the Department of Consumer Affairs (DoCA), MIB, and CCPA.</li>
          </ul>
        </div>
      </div>

      <a href="the-work-we-do.html" class="btn-text-link">
        <span>Read full details on how we handle complaints and monitor ads &rarr;</span>
      </a>
    </div>
  </section>

  <!-- 3. People & Governance Overview -->
  <section class="about-section" id="people">
    <div class="container">
      <div class="section-eyebrow">Governance &amp; Impartiality</div>
      <h2 class="section-heading">Tripartite Structure &amp; Civil Society Quorum</h2>
      <p class="section-intro-text">
        ASCI's credibility relies upon its strict separation of powers. Operational management, institutional policy, and case adjudication are maintained across distinct, independent bodies:
      </p>

      <div class="governance-card-grid">
        <div class="gov-summary-card">
          <div class="gov-card-tag">Strategic Leadership</div>
          <h3 class="gov-card-title">Board of Governors</h3>
          <p class="gov-card-desc">
            Composed of senior executives from advertisers, media networks, and advertising agencies who establish institutional policy, code updates, and financial governance.
          </p>
        </div>

        <div class="gov-summary-card">
          <div class="gov-card-tag">Independent Adjudication</div>
          <h3 class="gov-card-title">Consumer Complaints Council (CCC)</h3>
          <p class="gov-card-desc">
            The decision-making heart of ASCI. By constitution, at least 50% of the CCC consists of eminent civil society members—doctors, lawyers, consumer activists, and educators.
          </p>
        </div>

        <div class="gov-summary-card">
          <div class="gov-card-tag">Judicial Review</div>
          <h3 class="gov-card-title">Independent Review Panel</h3>
          <p class="gov-card-desc">
            Presided over by retired High Court Judges to independently hear appeals and procedural reviews, guaranteeing natural justice for both complainants and advertisers.
          </p>
        </div>
      </div>

      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px 32px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 20px;">
        <div>
          <h4 style="font-family: var(--font-serif); font-size: 1.25rem; color: #0f172a; margin-bottom: 6px;">Looking for specific leadership profiles or council rosters?</h4>
          <p style="color: #64748b; font-size: 0.95rem; margin: 0;">Access our FSSAI-style institutional directory with instant search and member details.</p>
        </div>
        <a href="people.html" style="background: #008779; color: #ffffff; padding: 10px 22px; border-radius: 9999px; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
          <span>Open People Directory &rarr;</span>
        </a>
      </div>
    </div>
  </section>

  <!-- 4. Milestones at a Glance -->
  <section class="about-section" id="milestones">
    <div class="container">
      <div class="section-eyebrow">Four Decades of Evolution</div>
      <h2 class="section-heading">Key Milestones: 1985 to 2026</h2>
      <p class="section-intro-text">
        From a voluntary initiative among 43 industry pioneers to a nationally recognized self-regulatory authority regulating digital, print, broadcast, and AI-driven commercial content.
      </p>

      <div class="timeline-preview-wrap">
        <div class="decade-card">
          <div class="decade-year">1985 – 1989</div>
          <p class="decade-text">
            ASCI founded on 21 October 1985 by 43 members. Code adopted into Doordarshan &amp; All India Radio commercial broadcast codes.
          </p>
        </div>

        <div class="decade-card">
          <div class="decade-year">2000 – 2009</div>
          <p class="decade-text">
            Statutory alignment with Cable TV Networks Act. Government officially recognizes ASCI as the primary advertising self-regulator in India.
          </p>
        </div>

        <div class="decade-card">
          <div class="decade-year">2010 – 2020</div>
          <p class="decade-text">
            National Advertising Monitoring Services (NAMS) launched. Guidelines introduced for healthcare, food, education, and digital influencers.
          </p>
        </div>

        <div class="decade-card">
          <div class="decade-year">2021 – 2026</div>
          <p class="decade-text">
            ASCI Academy inaugurated; guidelines issued on Dark Patterns, Environmental Claims (Greenwashing), and Generative AI transparency.
          </p>
        </div>
      </div>

      <a href="history-key-milestones.html" class="btn-text-link">
        <span>Explore the full interactive chronological timeline &rarr;</span>
      </a>
    </div>
  </section>

  <!-- 5. Transparency & Newsletter -->
  <section class="about-section" style="border-bottom: none;" id="annual-reports">
    <div class="container">
      <div class="resource-banner-card">
        <div class="resource-banner-content">
          <h3>Annual Complaints &amp; Trend Reports</h3>
          <p>
            ASCI publishes annual and half-yearly transparency reports tracking advertising compliance rates, digital violation trends, and consumer grievance outcomes across sectors.
          </p>
        </div>
        <div>
          <a href="https://www.ascionline.in/reports/" class="btn-banner-action">
            <span>Download Annual Reports</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="7" y1="17" x2="17" y2="7"></line>
              <polyline points="7 7 17 7 17 17"></polyline>
            </svg>
          </a>
        </div>
      </div>
    </div>
  </section>
"""

about_full = assemble_page(about_title, about_desc, about_css, about_body)
with open('about-us.html', 'w', encoding='utf-8') as f:
    f.write(about_full)
print("SUCCESS: about-us.html rebuilt cleanly!")
