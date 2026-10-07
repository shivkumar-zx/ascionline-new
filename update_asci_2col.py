# Update ASCI (3).html with 2-column Organisation and 2-column People in aboutMegaPanel

with open('ASCI (3).html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update CSS if needed
old_css_target = """.about-mega-grid-3col {
  display: grid;
  grid-template-columns: 1.1fr 1.5fr 1.5fr;
  gap: 36px;
  align-items: start;
}"""

new_css = """.about-mega-grid-3col {
  display: grid;
  grid-template-columns: 280px 1.5fr 1.5fr;
  gap: 40px;
  align-items: start;
}

.megamenu-2col-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 28px;
  row-gap: 0;
}

@media (max-width: 1200px) {
  .about-mega-grid-3col {
    grid-template-columns: 240px 1.4fr 1.4fr;
    gap: 28px;
  }
  .megamenu-2col-list {
    grid-template-columns: 1fr;
  }
}"""

if old_css_target in text:
    text = text.replace(old_css_target, new_css, 1)
    print("CSS updated successfully.")
else:
    print("Warning: old CSS target not found exactly, will check if already updated.")

# 2. Update aboutMegaPanel HTML
panel_start = text.find('id="aboutMegaPanel"')
panel_end = text.find('id="codesMegaPanel"')
assert panel_start != -1 and panel_end != -1

old_panel = text[panel_start:panel_end]

new_panel = """id="aboutMegaPanel">
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

          <!-- Col 2: Organisation (2 Sub-Columns) -->
          <div class="megamenu-col">
            <h4 class="megamenu-col-title">Organisation</h4>
            <div class="megamenu-2col-list">
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
              </ul>
              <ul class="megamenu-links-list">
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
          </div>

          <!-- Col 3: People (2 Sub-Columns) -->
          <div class="megamenu-col">
            <h4 class="megamenu-col-title">People</h4>
            <div class="megamenu-2col-list">
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
              </ul>
              <ul class="megamenu-links-list">
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
      </div>
    </div>

    <div class="megamenu-panel" """

text = text[:panel_start] + new_panel + text[panel_end + len('id="codesMegaPanel"'):]

with open('ASCI (3).html', 'w', encoding='utf-8') as f:
    f.write(text)

print("ASCI (3).html successfully updated with 2-column Organisation and 2-column People!")
