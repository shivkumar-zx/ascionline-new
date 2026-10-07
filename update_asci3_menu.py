# Fix aboutMegaPanel in ASCI (3).html

with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the current aboutMegaPanel in ASCI (3).html
start_tag = '<div class="megamenu-panel" id="aboutMegaPanel">'
idx = text.find(start_tag)
if idx == -1:
    print("Could not find aboutMegaPanel")
    exit(1)

# Find where aboutMegaPanel ends (before codesMegaPanel)
next_panel = '<div class="megamenu-panel" id="codesMegaPanel">'
end_idx = text.find(next_panel, idx)
if end_idx == -1:
    print("Could not find next panel")
    exit(1)

old_panel = text[idx:end_idx]

new_panel = '''<div class="megamenu-panel" id="aboutMegaPanel">
      <div class="container">
        <div class="about-mega-grid-3col">
          <!-- Col 1: Highlight box (Standard styling matching other panels) -->
          <div class="megamenu-highlight-col">
            <h3 class="megamenu-highlight-title">Know ASCI, our people and our journey.</h3>
            <p class="megamenu-highlight-desc">
              Independent, voluntary self-regulation for responsible, truthful, and decent advertising across India.
            </p>
            <a href="about-us.html" class="btn-megamenu-explore">
              <span>Explore About ASCI</span>
              <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round"
                stroke-linejoin="round">
                <line x1="7" y1="17" x2="17" y2="7"></line>
                <polyline points="7 7 17 7 17 17"></polyline>
              </svg>
            </a>
          </div>

          <!-- Col 2: Organisation -->
          <div class="megamenu-col">
            <h4 class="megamenu-col-title">Organisation</h4>
            <ul class="megamenu-links-list">
              <li class="megamenu-link-item">
                <a href="about-us.html#purpose">
                  <span>Purpose &amp; vision</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="the-work-we-do.html">
                  <span>The work we do &amp; its impact</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="history-key-milestones.html">
                  <span>History &amp; key milestones</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="about-us.html#awards">
                  <span>Awards &amp; recognition</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="about-us.html#annual-reports">
                  <span>Annual reports</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="about-us.html#campaigns">
                  <span>Our past campaigns</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="about-us.html#careers">
                  <span>Explore careers with ASCI</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="about-us.html#newsletter">
                  <span>Subscribe to our newsletter</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
            </ul>
          </div>

          <!-- Col 3: People -->
          <div class="megamenu-col">
            <h4 class="megamenu-col-title">People</h4>
            <ul class="megamenu-links-list">
              <li class="megamenu-link-item">
                <a href="people.html?panel=board">
                  <span>Board of Governors &amp; Consultative Committee</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="people.html?panel=leadership">
                  <span>ASCI Leadership Team</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="people.html?panel=ccc">
                  <span>Consumer Complaints Council</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="people.html?panel=review-panel">
                  <span>Independent Review Panel</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="people.html?panel=technical-experts">
                  <span>Technical experts</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="people.html?panel=ad-advisory">
                  <span>Ad advisory expert panel</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
              <li class="megamenu-link-item">
                <a href="people.html?panel=ad-advisory-tech">
                  <span>Ad Advisory technical experts</span>
                  <svg class="arrow-diag-icon" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="7" y1="17" x2="17" y2="7"></line>
                    <polyline points="7 7 17 7 17 17"></polyline>
                  </svg>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>\n\n    '''

text = text[:idx] + new_panel + text[end_idx:]

# Also update CSS for .about-mega-grid-3col
css_pattern = '.about-mega-grid-3col {'
css_idx = text.find(css_pattern)
if css_idx != -1:
    css_end = text.find('}', css_idx)
    updated_css = '''.about-mega-grid-3col {
  display: grid;
  grid-template-columns: 1.1fr 1.5fr 1.5fr;
  gap: 36px;
  align-items: start;
}'''
    text = text[:css_idx] + updated_css + text[css_end+1:]

with open('ASCI (3).html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated ASCI (3).html with clean aboutMegaPanel and matching CSS!")
