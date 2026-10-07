# Update about-us.html with full sections matching asci_about_us_and_people_plan.md

new_sections_css = """
/* ================= AWARDS, CAMPAIGNS, CAREERS & NEWSLETTER ================= */
.awards-grid,
.campaigns-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.award-card,
.campaign-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 28px 24px;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}

.award-card:hover,
.campaign-card:hover {
  transform: translateY(-4px);
  border-color: #008779;
  box-shadow: 0 12px 24px rgba(0, 135, 121, 0.08);
}

.award-badge-year {
  display: inline-block;
  align-self: flex-start;
  background: #f0fdfa;
  color: #007367;
  font-size: 0.8125rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 6px;
  margin-bottom: 14px;
  border: 1px solid rgba(0, 135, 121, 0.15);
}

.award-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  background: #f8fafc;
  color: #008779;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
  border: 1px solid #e2e8f0;
}

.award-title,
.campaign-title {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 10px;
}

.award-desc,
.campaign-desc {
  font-size: 0.925rem;
  color: #475569;
  line-height: 1.6;
  flex: 1;
  margin: 0;
}

.campaign-tag {
  display: inline-block;
  align-self: flex-start;
  background: #f1f5f9;
  color: #334155;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 3px 10px;
  border-radius: 9999px;
  margin-bottom: 14px;
}

.campaign-meta {
  display: block;
  margin-top: 16px;
  font-size: 0.8125rem;
  font-weight: 600;
  color: #008779;
}

/* Careers Card */
.careers-banner-card {
  background: linear-gradient(135deg, #093b32 0%, #008779 100%);
  border-radius: 20px;
  padding: 44px 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 36px;
  color: #ffffff;
  box-shadow: 0 12px 32px rgba(9, 59, 50, 0.15);
}

.careers-content {
  flex: 1;
}

.careers-roles-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.career-pill {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(8px);
  color: #ffffff;
  font-size: 0.8125rem;
  font-weight: 500;
  padding: 6px 14px;
  border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.25);
}

.btn-careers-apply {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: #ffffff;
  color: #093b32;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 13px 26px;
  border-radius: 9999px;
  text-decoration: none;
  transition: all 0.18s ease;
  white-space: nowrap;
}

.btn-careers-apply:hover {
  background: #f1f5f9;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Newsletter Strip */
.newsletter-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  padding: 40px 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.03);
}

.newsletter-content {
  flex: 1;
  max-width: 520px;
}

.newsletter-form {
  flex: 1;
  max-width: 460px;
}

.newsletter-input-group {
  display: flex;
  gap: 10px;
}

.newsletter-input {
  flex: 1;
  padding: 12px 18px;
  font-size: 0.9375rem;
  border-radius: 9999px;
  border: 1.2px solid #cbd5e1;
  outline: none;
  font-family: inherit;
  transition: var(--transition);
}

.newsletter-input:focus {
  border-color: #008779;
  box-shadow: 0 0 0 3px rgba(0, 135, 121, 0.12);
}

.btn-newsletter-submit {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #0f172a;
  color: #ffffff;
  font-weight: 600;
  font-size: 0.9375rem;
  padding: 12px 24px;
  border-radius: 9999px;
  border: none;
  cursor: pointer;
  transition: all 0.18s ease;
  white-space: nowrap;
}

.btn-newsletter-submit:hover {
  background: #008779;
}

@media (max-width: 991px) {
  .awards-grid,
  .campaigns-grid {
    grid-template-columns: 1fr;
  }
  .careers-banner-card {
    flex-direction: column;
    align-items: flex-start;
    padding: 32px 24px;
  }
  .newsletter-card {
    flex-direction: column;
    align-items: stretch;
    padding: 32px 24px;
  }
  .newsletter-content,
  .newsletter-form {
    max-width: 100%;
  }
}

@media (max-width: 640px) {
  .newsletter-input-group {
    flex-direction: column;
  }
  .btn-newsletter-submit {
    justify-content: center;
  }
}
"""

new_sections_html = """
  <!-- 6. Awards & Recognition Section -->
  <section class="about-section" id="awards">
    <div class="container">
      <div class="section-eyebrow">Excellence &amp; Global Standing</div>
      <h2 class="section-heading">Awards &amp; Institutional Recognition</h2>
      <p class="section-intro-text">
        ASCI's self-regulatory framework and transparent dispute resolution mechanisms have earned national statutory integration and prestigious international accolades.
      </p>

      <div class="awards-grid">
        <div class="award-card">
          <div class="award-badge-year">2025</div>
          <div class="award-icon-wrap">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
          </div>
          <h3 class="award-title">ICAS Global Honors</h3>
          <p class="award-desc">
            Received two international awards at the International Council for Advertising Self-Regulation (ICAS) Global Summit in Mumbai for excellence in digital advertising education through the ASCI Academy.
          </p>
        </div>

        <div class="award-card">
          <div class="award-badge-year">2013</div>
          <div class="award-icon-wrap">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
          </div>
          <h3 class="award-title">EASA Best Practice Gold Award</h3>
          <p class="award-desc">
            Conferred the prestigious Gold Award by the European Advertising Standards Alliance (EASA) for benchmark complaints-handling procedures, speed of resolution, and cross-border cooperation.
          </p>
        </div>

        <div class="award-card">
          <div class="award-badge-year">Statutory Mandate</div>
          <div class="award-icon-wrap">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          </div>
          <h3 class="award-title">Government Co-Regulation</h3>
          <p class="award-desc">
            Officially recognized under the Cable Television Networks Rules, with active co-regulatory partnerships alongside the Department of Consumer Affairs (DoCA), FSSAI, AYUSH, and Maha RERA.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- 7. Our Past Campaigns Section -->
  <section class="about-section" id="campaigns">
    <div class="container">
      <div class="section-eyebrow">Public Awareness &amp; Consumer Voice</div>
      <h2 class="section-heading">Our Past Campaigns</h2>
      <p class="section-intro-text">
        ASCI regularly runs high-impact nationwide campaigns empowering citizens, youth, and digital influencers to recognize deceptive commercial communications and foster ethical practices.
      </p>

      <div class="campaigns-grid">
        <div class="campaign-card">
          <span class="campaign-tag">Consumer Awareness</span>
          <h3 class="campaign-title">#ChupNaBaitho</h3>
          <p class="campaign-desc">
            A high-visibility public movement encouraging consumers across India to stand up against misleading advertisements and lodge instant complaints via digital and WhatsApp channels.
          </p>
          <span class="campaign-meta">Over 10M+ Consumer Impressions</span>
        </div>

        <div class="campaign-card">
          <span class="campaign-tag">Digital Transparency</span>
          <h3 class="campaign-title">Spot the Dark Pattern (2026)</h3>
          <p class="campaign-desc">
            A creator-led initiative exposing sneaky subscription traps, false urgency countdown clocks, and covert user interface trickery across mobile applications and e-commerce platforms.
          </p>
          <span class="campaign-meta">In Partnership with Nasscom &amp; Creators</span>
        </div>

        <div class="campaign-card">
          <span class="campaign-tag">Influencer Compliance</span>
          <h3 class="campaign-title">#AdDisclosed</h3>
          <p class="campaign-desc">
            Driving mandatory commercial disclosures on social media feeds and the launch of the ASCI.Social creator verification portal, keeping influencer promotions truthful and transparent.
          </p>
          <span class="campaign-meta">Over 90% Digital Compliance Rate</span>
        </div>
      </div>
    </div>
  </section>

  <!-- 8. Explore Careers with ASCI Section -->
  <section class="about-section" id="careers">
    <div class="container">
      <div class="careers-banner-card">
        <div class="careers-content">
          <div class="section-eyebrow" style="color: rgba(255,255,255,0.85); margin-bottom: 8px;">Join Our Mission</div>
          <h2 style="font-family: var(--font-serif); font-size: 2rem; color: #ffffff; margin-bottom: 12px; font-weight: 700;">
            Explore Careers with ASCI
          </h2>
          <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.05rem; line-height: 1.6; max-width: 680px; margin-bottom: 24px;">
            Work at the intersection of law, technology, creative media, and consumer protection. Help us uphold truth, decency, and fairness in advertising for over 1.4 billion citizens across India.
          </p>
          <div class="careers-roles-pills">
            <span class="career-pill">Legal &amp; Regulatory Review</span>
            <span class="career-pill">AI &amp; Digital Monitoring</span>
            <span class="career-pill">Consumer Advocacy</span>
            <span class="career-pill">ASCI Academy Training</span>
          </div>
        </div>
        <div class="careers-action-side">
          <a href="mailto:careers@ascionline.in" class="btn-careers-apply">
            <span>Apply &amp; Send CV</span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="7" y1="17" x2="17" y2="7"></line>
              <polyline points="7 7 17 7 17 17"></polyline>
            </svg>
          </a>
          <span style="font-size: 0.8125rem; color: rgba(255,255,255,0.75); display: block; margin-top: 10px; text-align: center;">
            careers@ascionline.in
          </span>
        </div>
      </div>
    </div>
  </section>

  <!-- 9. Newsletter Subscription Section -->
  <section class="about-section" id="newsletter" style="background: #f8fafc; border-bottom: none;">
    <div class="container">
      <div class="newsletter-card">
        <div class="newsletter-content">
          <div class="section-eyebrow">Knowledge &amp; Insights</div>
          <h2 class="section-heading" style="font-size: 1.85rem; margin-bottom: 10px;">
            Subscribe to ASCI Newsletter
          </h2>
          <p style="font-size: 0.95rem; color: #475569; line-height: 1.6; margin: 0;">
            Get quarterly complaint trends, emerging ad-law alerts, dark patterns research, and ASCI Academy masterclass schedules delivered directly to your inbox.
          </p>
        </div>
        <form class="newsletter-form" onsubmit="event.preventDefault(); document.getElementById('nlSuccessMsg').style.display = 'block'; this.reset();">
          <div class="newsletter-input-group">
            <input type="email" required placeholder="Enter your official or personal email..." class="newsletter-input">
            <button type="submit" class="btn-newsletter-submit">
              <span>Subscribe</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
          </div>
          <div id="nlSuccessMsg" style="display: none; color: #008779; font-size: 0.875rem; font-weight: 600; margin-top: 10px;">
            ✓ Thank you for subscribing to ASCI updates!
          </div>
        </form>
      </div>
    </div>
  </section>
"""

with open('about-us.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add CSS
css_insert_pt = text.find('</style>')
if css_insert_pt != -1:
    text = text[:css_insert_pt] + new_sections_css + '\n' + text[css_insert_pt:]
    print("CSS added to about-us.html")

# 2. Add HTML right after id="annual-reports" section and before cta-callout-section
idx_annual = text.find('id="annual-reports"')
idx_annual_end = text.find('</section>', idx_annual) + len('</section>')

text = text[:idx_annual_end] + '\n' + new_sections_html + '\n' + text[idx_annual_end:]
print("HTML sections added to about-us.html")

# 3. Clean up the comments above footer if needed
text = text.replace('<!-- Footer -->\n    <!-- Hero Callout Banner', '<!-- Hero Callout Banner')

with open('about-us.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("about-us.html successfully updated!")
