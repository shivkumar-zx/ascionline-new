import os
import re

# Load base parts
with open("head_part.html", "r", encoding="utf-8") as f:
    head_part = f.read()

# Make sure academy.css is linked inside head_part
if "assets/academy.css" not in head_part:
    head_part = head_part.replace("</head>", '  <link rel="stylesheet" href="assets/academy.css">\n</head>')

with open("academy_standalone_header.html", "r", encoding="utf-8") as f:
    academy_header = f.read()

with open("footer_clean.html", "r", encoding="utf-8") as f:
    footer_part = f.read()

def make_page(title, breadcrumbs, content_html, filename):
    # Adjust title in head
    page_head = re.sub(r'<title>.*?</title>', f'<title>{title} – ASCI Academy</title>', head_part)
    
    full_html = f"""{page_head}
{academy_header}

<main class="academy-main-content">
{content_html}
</main>

{footer_part}
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated {filename} ({len(full_html):,} bytes)")

# -------------------------------------------------------------
# 1. ACADEMY HUB / LANDING PAGE: academy.html
# -------------------------------------------------------------
hub_content = """<!-- 1. FULL-WIDTH HERO BANNER CAROUSEL (CLEAN, WIDESCREEN, AUTHENTIC) -->
<section class="academy-hero-carousel-section" style="padding: 24px 0 0 0; background: #ffffff;">
  <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 20px;">
    
    <!-- Carousel Box -->
    <div id="academyHeroCarousel" style="position: relative; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 32px rgba(0, 33, 71, 0.08); background: #001a3a;">
      
      <!-- Slide 1: What The Sigma -->
      <a href="academy-reports.html#what-the-sigma" class="academy-hero-slide" style="display: block; text-decoration: none;" aria-label="What The Sigma Report">
        <img src="assets/images/academy/What-The-Sigma-Website-Banner-png.avif" alt="What The Sigma Banner" style="width: 100%; height: clamp(240px, 34vw, 440px); object-fit: cover; display: block;">
      </a>

      <!-- Slide 2: Ethical UI/UX Designs -->
      <a href="academy-courses.html#ethical-ui-ux" class="academy-hero-slide" style="display: none; text-decoration: none;" aria-label="Ethical UI/UX Designs Course">
        <img src="assets/images/academy/ethical-ui-ux-designs-building-consumer-trust-homepage-banner-desktop.webp" alt="Ethical UI/UX Banner" style="width: 100%; height: clamp(240px, 34vw, 440px); object-fit: cover; display: block;">
      </a>

      <!-- Slide 3: Conscious Patterns 11 -->
      <a href="academy-reports.html#ad-next" class="academy-hero-slide" style="display: none; text-decoration: none;" aria-label="Conscious Patterns AD Next AI Edition">
        <img src="assets/images/academy/ASCI-Academy-Website-Banner-Conscious-Patterns-11.jpg" alt="Conscious Patterns Banner 11" style="width: 100%; height: clamp(240px, 34vw, 440px); object-fit: cover; display: block;">
      </a>

      <!-- Slide 4: Conscious Patterns 9 -->
      <a href="academy-reports.html#gender-next" class="academy-hero-slide" style="display: none; text-decoration: none;" aria-label="Manifest Masculinities Beyond The Mask Report">
        <img src="assets/images/academy/ASCI-Academy-Website-Banner-Conscious-Patterns-9.jpg" alt="Conscious Patterns Banner 9" style="width: 100%; height: clamp(240px, 34vw, 440px); object-fit: cover; display: block;">
      </a>

      <!-- Prev / Next Glassmorphism Chevrons -->
      <button onclick="changeHeroSlide(-1)" aria-label="Previous Slide" style="position: absolute; top: 50%; left: 16px; transform: translateY(-50%); background: rgba(0, 26, 58, 0.65); backdrop-filter: blur(8px); color: #fff; border: 1px solid rgba(255,255,255,0.25); width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.2s ease;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>
      <button onclick="changeHeroSlide(1)" aria-label="Next Slide" style="position: absolute; top: 50%; right: 16px; transform: translateY(-50%); background: rgba(0, 26, 58, 0.65); backdrop-filter: blur(8px); color: #fff; border: 1px solid rgba(255,255,255,0.25); width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.2s ease;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>

      <!-- Bottom Pagination Dots -->
      <div style="position: absolute; bottom: 14px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px; z-index: 10;">
        <button onclick="setHeroSlide(0)" class="hero-dot" style="width: 28px; height: 7px; border-radius: 4px; background: #ffffff; border: none; cursor: pointer; transition: all 0.2s ease;"></button>
        <button onclick="setHeroSlide(1)" class="hero-dot" style="width: 10px; height: 7px; border-radius: 4px; background: rgba(255,255,255,0.45); border: none; cursor: pointer; transition: all 0.2s ease;"></button>
        <button onclick="setHeroSlide(2)" class="hero-dot" style="width: 10px; height: 7px; border-radius: 4px; background: rgba(255,255,255,0.45); border: none; cursor: pointer; transition: all 0.2s ease;"></button>
        <button onclick="setHeroSlide(3)" class="hero-dot" style="width: 10px; height: 7px; border-radius: 4px; background: rgba(255,255,255,0.45); border: none; cursor: pointer; transition: all 0.2s ease;"></button>
      </div>

    </div>

  </div>
</section>

<!-- 2. ACADEMY MISSION & METRICS BAR (ELEGANT, SPACIOUS & PROFESSIONAL) -->
<section class="academy-mission-metrics-section" style="padding: 44px 0 48px 0; background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); border-bottom: 1px solid #e2e8f0;">
  <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 20px;">
    
    <div style="display: grid; grid-template-columns: 1.25fr 0.95fr; gap: 48px; align-items: center;">
      
      <!-- Left: Purpose & CTAs -->
      <div>
        <div style="display: inline-flex; align-items: center; gap: 8px; padding: 4px 12px; background: rgba(224, 88, 41, 0.08); border: 1px solid rgba(224, 88, 41, 0.2); border-radius: 9999px; margin-bottom: 14px;">
          <span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #e05829;"></span>
          <span style="font-family: var(--font-sans); font-size: 0.78rem; font-weight: 700; color: #e05829; text-transform: uppercase; letter-spacing: 0.08em;">
            ASCI Academy · Education &amp; Standards
          </span>
        </div>

        <h1 style="font-family: var(--font-serif); font-size: clamp(2rem, 3.2vw, 2.7rem); font-weight: 700; line-height: 1.2; color: #002d62; margin: 0 0 16px 0;">
          Build advertising people can trust.
        </h1>

        <p style="font-family: var(--font-sans); font-size: 1.05rem; line-height: 1.65; color: #475569; margin: 0 0 24px 0; max-width: 620px;">
          India's premier institution for responsible advertising education, ethical digital design, and research-backed creator standards. Empowering industry professionals, university students, and creators to shape ethical consumer journeys.
        </p>

        <div style="display: flex; flex-wrap: wrap; gap: 12px; align-items: center;">
          <a href="#courses" style="display: inline-flex; align-items: center; gap: 8px; background: #e05829; color: #ffffff; padding: 12px 24px; border-radius: 8px; font-weight: 700; font-size: 0.92rem; text-decoration: none; box-shadow: 0 4px 14px rgba(224, 88, 41, 0.25); transition: all 0.2s ease;">
            <span>Explore Certification Courses</span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
              <line x1="7" y1="17" x2="17" y2="7"></line>
              <polyline points="7 7 17 7 17 17"></polyline>
            </svg>
          </a>
          <a href="academy-programs.html" style="display: inline-flex; align-items: center; gap: 6px; background: #002d62; color: #ffffff; padding: 12px 20px; border-radius: 8px; font-weight: 600; font-size: 0.92rem; text-decoration: none; transition: all 0.2s ease;">
            <span>Our Programs</span>
          </a>
          <a href="academy-login.html" style="display: inline-flex; align-items: center; gap: 6px; background: #ffffff; color: #002d62; border: 1.5px solid #002d62; padding: 11px 18px; border-radius: 8px; font-weight: 700; font-size: 0.92rem; text-decoration: none; transition: all 0.2s ease;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            <span>Learner Portal</span>
          </a>
        </div>
      </div>

      <!-- Right: 4 High-Impact Metrics Card -->
      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 26px; box-shadow: 0 8px 24px rgba(0, 45, 98, 0.05);">
        <div style="font-size: 0.78rem; font-weight: 800; color: #002d62; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 16px; display: flex; align-items: center; gap: 6px;">
          <span style="width: 6px; height: 6px; border-radius: 50%; background: #086b59;"></span>
          Institutional Footprint &amp; Impact
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div style="padding: 14px 16px; background: #f8fafc; border-radius: 10px; border-left: 3.5px solid #002d62;">
            <div style="font-size: 1.85rem; font-weight: 800; color: #002d62; font-family: var(--font-serif); line-height: 1;">100K+</div>
            <div style="font-size: 0.8rem; color: #64748b; font-weight: 600; margin-top: 4px;">Learners Target</div>
          </div>
          <div style="padding: 14px 16px; background: #f8fafc; border-radius: 10px; border-left: 3.5px solid #e05829;">
            <div style="font-size: 1.85rem; font-weight: 800; color: #e05829; font-family: var(--font-serif); line-height: 1;">50+</div>
            <div style="font-size: 0.8rem; color: #64748b; font-weight: 600; margin-top: 4px;">Partner Universities</div>
          </div>
          <div style="padding: 14px 16px; background: #f8fafc; border-radius: 10px; border-left: 3.5px solid #086b59;">
            <div style="font-size: 1.85rem; font-weight: 800; color: #086b59; font-family: var(--font-serif); line-height: 1;">3</div>
            <div style="font-size: 0.8rem; color: #64748b; font-weight: 600; margin-top: 4px;">Industry Certifications</div>
          </div>
          <div style="padding: 14px 16px; background: #f8fafc; border-radius: 10px; border-left: 3.5px solid #7c3aed;">
            <div style="font-size: 1.85rem; font-weight: 800; color: #7c3aed; font-family: var(--font-serif); line-height: 1;">100%</div>
            <div style="font-size: 0.8rem; color: #64748b; font-weight: 600; margin-top: 4px;">Self-Regulation Backed</div>
          </div>
        </div>
      </div>

    </div>

  </div>
</section>

<script>
var currentHeroSlide = 0;
var heroInterval;

function showHeroSlide(idx) {
  var slides = document.querySelectorAll('.academy-hero-slide');
  var dots = document.querySelectorAll('.hero-dot');
  if (!slides || !slides.length) return;

  if (idx >= slides.length) idx = 0;
  if (idx < 0) idx = slides.length - 1;
  currentHeroSlide = idx;

  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = (i === idx) ? 'block' : 'none';
  }

  for (var j = 0; j < dots.length; j++) {
    if (j === idx) {
      dots[j].style.width = '28px';
      dots[j].style.background = '#ffffff';
    } else {
      dots[j].style.width = '10px';
      dots[j].style.background = 'rgba(255,255,255,0.45)';
    }
  }
}

function changeHeroSlide(step) {
  clearInterval(heroInterval);
  showHeroSlide(currentHeroSlide + step);
  startHeroTimer();
}

function setHeroSlide(idx) {
  clearInterval(heroInterval);
  showHeroSlide(idx);
  startHeroTimer();
}

function startHeroTimer() {
  clearInterval(heroInterval);
  heroInterval = setInterval(function() {
    showHeroSlide(currentHeroSlide + 1);
  }, 5000);
}

window.addEventListener('load', function() {
  showHeroSlide(0);
  startHeroTimer();
  var box = document.getElementById('academyHeroCarousel');
  if (box) {
    box.addEventListener('mouseenter', function() { clearInterval(heroInterval); });
    box.addEventListener('mouseleave', function() { startHeroTimer(); });
  }
});
</script>

<!-- 2. FEATURED CERTIFICATION COURSES (WITH REAL LIVE THUMBNAIL IMAGES) -->
<section id="courses" style="padding: 72px 0; background: #ffffff;">
  <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 20px;">
    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 40px; flex-wrap: wrap; gap: 16px;">
      <div>
        <div style="font-family: var(--font-sans); font-size: 0.82rem; font-weight: 700; color: #e05829; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px;">
          Accredited Self-Paced E-Learning
        </div>
        <h2 style="font-family: var(--font-serif); font-size: clamp(1.9rem, 3vw, 2.5rem); font-weight: 700; color: #002d62; margin: 0;">
          Featured Certification Courses
        </h2>
      </div>
      <a href="academy-courses.html" style="display: inline-flex; align-items: center; gap: 6px; font-weight: 700; color: #002d62; text-decoration: none; font-size: 0.92rem;">
        <span>View All Courses</span>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
          <line x1="5" y1="12" x2="19" y2="12"></line>
          <polyline points="12 5 19 12 12 19"></polyline>
        </svg>
      </a>
    </div>

    <!-- 3 Core Courses Grid with Real Scraped Course Visuals -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 28px;">
      
      <!-- Course 1: Ethical UI/UX Designs (With Live Thumbnail) -->
      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 4px 16px rgba(0,0,0,0.04); transition: transform 0.2s ease;">
        <div style="position: relative; height: 180px; overflow: hidden; background: #0f172a;">
          <img src="assets/images/academy/ethical-ui-ux-designs-building-consumer-trust-thumbnail.webp" alt="Ethical UI/UX Designs Course Thumbnail" style="width: 100%; height: 100%; object-fit: cover; display: block;">
          <span style="position: absolute; top: 12px; left: 12px; background: rgba(0, 45, 98, 0.9); color: #fff; font-size: 0.72rem; font-weight: 700; padding: 4px 8px; border-radius: 4px; text-transform: uppercase;">
            Brand &amp; UX Teams
          </span>
        </div>
        <div style="padding: 22px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h3 style="font-family: var(--font-serif); font-size: 1.3rem; font-weight: 700; color: #002d62; margin-bottom: 10px; line-height: 1.35;">
              Ethical UI/UX Designs: Building Consumer Trust
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.55; color: #475569; margin-bottom: 16px;">
              Equips Brand, Legal, and Product Designers to spot online dark patterns before consumer backlash or regulatory action. Features simulated app case studies.
            </p>
            <ul style="padding-left: 18px; margin: 0 0 20px 0; font-size: 0.86rem; color: #64748b; line-height: 1.6;">
              <li>10 Online Dark Pattern Archetypes</li>
              <li>Drip Pricing &amp; False Urgency Avoidance</li>
              <li>Compliant Digital Interface Blueprints</li>
            </ul>
          </div>
          <div style="border-top: 1px solid #f1f5f9; padding-top: 16px; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.82rem; font-weight: 600; color: #086b59;">Self-Paced • Certified</span>
            <a href="academy-courses.html#ethical-ui-ux" style="display: inline-flex; align-items: center; gap: 5px; background: #002d62; color: #fff; padding: 8px 16px; border-radius: 6px; font-size: 0.85rem; font-weight: 700; text-decoration: none;">
              <span>Course Details</span>
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </a>
          </div>
        </div>
      </div>

      <!-- Course 2: ASCI Guide to Responsible Advertising (With Live Rectangle-102.png Visual) -->
      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 4px 16px rgba(0,0,0,0.04); transition: transform 0.2s ease;">
        <div style="position: relative; height: 180px; overflow: hidden; background: #1e293b;">
          <img src="assets/images/academy/Rectangle-102.png" alt="ASCI Guide to Responsible Advertising Visual" style="width: 100%; height: 100%; object-fit: cover; display: block;">
          <span style="position: absolute; top: 12px; left: 12px; background: rgba(224, 88, 41, 0.95); color: #fff; font-size: 0.72rem; font-weight: 700; padding: 4px 8px; border-radius: 4px; text-transform: uppercase;">
            Foundational Program
          </span>
        </div>
        <div style="padding: 22px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h3 style="font-family: var(--font-serif); font-size: 1.3rem; font-weight: 700; color: #002d62; margin-bottom: 10px; line-height: 1.35;">
              The ASCI Guide to Responsible Advertising
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.55; color: #475569; margin-bottom: 16px;">
              Interactive eLearning navigating the core tenets of the ASCI Code for advertising self-regulation with landmark real-world campaigns across TV, print, and social media.
            </p>
            <ul style="padding-left: 18px; margin: 0 0 20px 0; font-size: 0.86rem; color: #64748b; line-height: 1.6;">
              <li>Core Tenets of Truthful &amp; Decent Claims</li>
              <li>Comparative &amp; Technical Ad Substantiation</li>
              <li>Navigating Complaints &amp; the CCC Review</li>
            </ul>
          </div>
          <div style="border-top: 1px solid #f1f5f9; padding-top: 16px; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.82rem; font-weight: 600; color: #e05829;">Case-Based • Certified</span>
            <a href="academy-courses.html#guide-advertising" style="display: inline-flex; align-items: center; gap: 5px; background: #e05829; color: #fff; padding: 8px 16px; border-radius: 6px; font-size: 0.85rem; font-weight: 700; text-decoration: none;">
              <span>Course Details</span>
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </a>
          </div>
        </div>
      </div>

      <!-- Course 3: Responsible Influencing Playbook (With Live Cover Image) -->
      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 4px 16px rgba(0,0,0,0.04); transition: transform 0.2s ease;">
        <div style="position: relative; height: 180px; overflow: hidden; background: #002d62;">
          <img src="assets/images/academy/Responsible-Influencing-Playbook.png" alt="Responsible Influencing Playbook Cover" style="width: 100%; height: 100%; object-fit: cover; display: block;">
          <span style="position: absolute; top: 12px; left: 12px; background: rgba(8, 107, 89, 0.95); color: #fff; font-size: 0.72rem; font-weight: 700; padding: 4px 8px; border-radius: 4px; text-transform: uppercase;">
            Creators &amp; Agencies
          </span>
        </div>
        <div style="padding: 22px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h3 style="font-family: var(--font-serif); font-size: 1.3rem; font-weight: 700; color: #002d62; margin-bottom: 10px; line-height: 1.35;">
              The Responsible Influencing Playbook
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.55; color: #475569; margin-bottom: 16px;">
              Tailored for today’s digital storytellers and talent agencies. Delves into advertising guidelines, consumer protection laws, and transparent commercial promotions in English &amp; Hindi.
            </p>
            <ul style="padding-left: 18px; margin: 0 0 20px 0; font-size: 0.86rem; color: #64748b; line-height: 1.6;">
              <li>Offered in English &amp; Hindi Modules</li>
              <li>Clear Disclosure Labels: #ad, #collab, #partner</li>
              <li>Due Diligence in BFSI, Gaming &amp; Health</li>
            </ul>
          </div>
          <div style="border-top: 1px solid #f1f5f9; padding-top: 16px; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.82rem; font-weight: 600; color: #002d62;">Bilingual • Certified</span>
            <a href="academy-courses.html#influencing-playbook" style="display: inline-flex; align-items: center; gap: 5px; background: #002d62; color: #fff; padding: 8px 16px; border-radius: 6px; font-size: 0.85rem; font-weight: 700; text-decoration: none;">
              <span>Course Details</span>
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- 3. WORKSHOPS & INSTITUTIONAL PROGRAMS (WITH REAL WORKSHOP PHOTOS) -->
<section id="workshops" style="padding: 72px 0; background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
  <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 20px;">
    <div style="text-align: center; max-width: 720px; margin: 0 auto 48px auto;">
      <div style="font-family: var(--font-sans); font-size: 0.82rem; font-weight: 700; color: #086b59; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px;">
        In-Person &amp; Hybrid Training
      </div>
      <h2 style="font-family: var(--font-serif); font-size: clamp(1.9rem, 3vw, 2.5rem); font-weight: 700; color: #002d62; margin-bottom: 12px;">
        Workshops, Masterclasses &amp; Campus Programs
      </h2>
      <p style="font-size: 1.05rem; color: #64748b; line-height: 1.6;">
        Real photos and programs from university faculty sessions to customized corporate bootcamps.
      </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 28px;">
      
      <!-- Workshop 1: Faculty Development Program (With Real Photo) -->
      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
        <div>
          <img src="assets/images/academy/SUH_9281-1024x682.jpg" alt="Faculty Development Program in Session" style="width: 100%; height: 170px; object-fit: cover; display: block;">
          <div style="padding: 22px;">
            <span style="font-size: 0.75rem; font-weight: 700; color: #086b59; background: rgba(8, 107, 89, 0.1); padding: 3px 8px; border-radius: 999px; text-transform: uppercase;">
              In-Person / Hybrid • For Educators
            </span>
            <h3 style="font-family: var(--font-serif); font-size: 1.25rem; font-weight: 700; color: #002d62; margin: 10px 0;">
              Empowering Ethical Advertising (FDP)
            </h3>
            <p style="font-size: 0.9rem; line-height: 1.6; color: #475569; margin: 0;">
              ASCI partners with institutions and universities to train and certify educators in ASCI’s Faculty Development Program with classroom case banks and teaching modules.
            </p>
          </div>
        </div>
        <div style="padding: 0 22px 22px 22px;">
          <a href="academy-programs.html#fdp" style="display: inline-flex; align-items: center; gap: 6px; font-weight: 700; color: #086b59; text-decoration: none; font-size: 0.9rem;">
            <span>Learn More About FDP &rarr;</span>
          </a>
        </div>
      </div>

      <!-- Workshop 2: Corporate Masterclasses (With Real Castrol Masterclass Photo) -->
      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
        <div>
          <img src="assets/images/academy/masterclass-at-castrol.jpg" alt="Masterclass Session at Castrol" style="width: 100%; height: 170px; object-fit: cover; display: block;">
          <div style="padding: 22px;">
            <span style="font-size: 0.75rem; font-weight: 700; color: #002d62; background: rgba(0, 45, 98, 0.08); padding: 3px 8px; border-radius: 999px; text-transform: uppercase;">
              On-Site Corporate Workshop
            </span>
            <h3 style="font-family: var(--font-serif); font-size: 1.25rem; font-weight: 700; color: #002d62; margin: 10px 0;">
              Corporate Masterclass &amp; Executive Training
            </h3>
            <p style="font-size: 0.9rem; line-height: 1.6; color: #475569; margin: 0;">
              Deep-dive on-site masterclasses tailored for marketing, creative, legal, and compliance leaders. Illustrated above at Castrol India headquarters.
            </p>
          </div>
        </div>
        <div style="padding: 0 22px 22px 22px;">
          <a href="academy-programs.html#corporates" style="display: inline-flex; align-items: center; gap: 6px; font-weight: 700; color: #002d62; text-decoration: none; font-size: 0.9rem;">
            <span>Explore Masterclasses &rarr;</span>
          </a>
        </div>
      </div>

      <!-- Workshop 3: University Placement Program (With Real APP Visual) -->
      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
        <div>
          <img src="assets/images/academy/Academic-Partnership-Program-Thumbnail-1.webp" alt="Academic Partnership Program Visual" style="width: 100%; height: 170px; object-fit: cover; display: block;">
          <div style="padding: 22px;">
            <span style="font-size: 0.75rem; font-weight: 700; color: #e05829; background: rgba(224, 88, 41, 0.1); padding: 3px 8px; border-radius: 999px; text-transform: uppercase;">
              Campus Program • Media Students
            </span>
            <h3 style="font-family: var(--font-serif); font-size: 1.25rem; font-weight: 700; color: #002d62; margin: 10px 0;">
              ASCI Placement Program (APP)
            </h3>
            <p style="font-size: 0.9rem; line-height: 1.6; color: #475569; margin: 0;">
              Direct curriculum integration connecting media and marketing students with accredited self-regulatory skills, verified certificates, and industry placement.
            </p>
          </div>
        </div>
        <div style="padding: 0 22px 22px 22px;">
          <a href="academy-programs.html#colleges" style="display: inline-flex; align-items: center; gap: 6px; font-weight: 700; color: #e05829; text-decoration: none; font-size: 0.9rem;">
            <span>Explore Campus Programs &rarr;</span>
          </a>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- 4. REPORTS & EVENTS (WITH REAL REPORT COVERS AND LAUNCH EVENT PHOTO) -->
<section id="reports" style="padding: 72px 0; background: #ffffff;">
  <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 20px;">
    <div style="display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 40px; align-items: start;">
      
      <!-- Left Column: Reports with Real Live Report Cover Thumbnails -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 24px; border-bottom: 2px solid #086b59; padding-bottom: 10px;">
          <h2 style="font-family: var(--font-serif); font-size: 1.75rem; font-weight: 700; color: #002d62; margin: 0;">
            Featured Reports &amp; Whitepapers
          </h2>
          <a href="academy-reports.html" style="font-size: 0.88rem; font-weight: 700; color: #086b59; text-decoration: none;">View All &rarr;</a>
        </div>

        <div style="display: flex; flex-direction: column; gap: 18px;">
          
          <!-- Report 1 with Live Cover Thumbnail -->
          <div style="display: flex; gap: 18px; padding: 18px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; align-items: center;">
            <img src="assets/images/academy/DI_thumbnail.png" alt="D&I Landscape Report Cover" style="width: 100px; height: 130px; object-fit: cover; border-radius: 6px; flex-shrink: 0; box-shadow: 0 3px 8px rgba(0,0,0,0.1);">
            <div>
              <span style="font-size: 0.72rem; font-weight: 700; color: #086b59; background: rgba(8, 107, 89, 0.1); padding: 2px 8px; border-radius: 999px; text-transform: uppercase;">
                Diversity &amp; Inclusion Benchmark
              </span>
              <h3 style="font-family: var(--font-serif); font-size: 1.15rem; font-weight: 700; color: #002d62; margin: 6px 0 6px 0;">
                D&amp;I Landscape of Indian Advertising
              </h3>
              <p style="font-size: 0.88rem; color: #64748b; line-height: 1.5; margin: 0 0 10px 0;">
                A comprehensive study assessing diversity and gender portrayal across mainstream Indian ad campaigns.
              </p>
              <a href="academy-reports.html#annual-trust" style="font-size: 0.84rem; font-weight: 700; color: #002d62; text-decoration: none;">
                <span>Read Report Summary &rarr;</span>
              </a>
            </div>
          </div>

          <!-- Report 2 with Live What The Sigma Cover Thumbnail -->
          <div style="display: flex; gap: 18px; padding: 18px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; align-items: center;">
            <img src="assets/images/academy/Report-Thumbnail-What-The-Sigma.webp" alt="What The Sigma Report Cover" style="width: 100px; height: 130px; object-fit: cover; border-radius: 6px; flex-shrink: 0; box-shadow: 0 3px 8px rgba(0,0,0,0.1);">
            <div>
              <span style="font-size: 0.72rem; font-weight: 700; color: #e05829; background: rgba(224, 88, 41, 0.1); padding: 2px 8px; border-radius: 999px; text-transform: uppercase;">
                E-Commerce UX Compliance
              </span>
              <h3 style="font-family: var(--font-serif); font-size: 1.15rem; font-weight: 700; color: #002d62; margin: 6px 0 6px 0;">
                What The Sigma: Dark Patterns in E-Commerce
              </h3>
              <p style="font-size: 0.88rem; color: #64748b; line-height: 1.5; margin: 0 0 10px 0;">
                Empirical investigation uncovering deceptive UI mechanisms and drip pricing tactics in top consumer apps.
              </p>
              <a href="academy-reports.html#dark-patterns" style="font-size: 0.84rem; font-weight: 700; color: #e05829; text-decoration: none;">
                <span>Read Report Summary &rarr;</span>
              </a>
            </div>
          </div>

        </div>
      </div>

      <!-- Right Column: Events with Real Live Launch Photo & Video Player -->
      <div id="events">
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 24px; border-bottom: 2px solid #e05829; padding-bottom: 10px;">
          <h2 style="font-family: var(--font-serif); font-size: 1.75rem; font-weight: 700; color: #002d62; margin: 0;">
            Academy Events &amp; Milestones
          </h2>
          <span style="font-size: 0.85rem; font-weight: 700; color: #e05829;">Inaugural Charter</span>
        </div>

        <div style="background: #fff8f5; border: 1px solid #ffd8c7; border-radius: 14px; padding: 24px; box-shadow: 0 4px 16px rgba(224, 88, 41, 0.06);">
          
          <!-- Real Launch Photo from Live Site -->
          <div style="position: relative; border-radius: 10px; overflow: hidden; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <img src="assets/images/academy/ASCI-Academy-Launch.jpg" alt="ASCI Academy Launch Stage" style="width: 100%; height: 210px; object-fit: cover; display: block;">
            <span style="position: absolute; top: 12px; left: 12px; background: #e05829; color: #fff; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; text-transform: uppercase;">
              Live Launch Milestone
            </span>
          </div>

          <!-- Video Player Keynote -->
          <div style="position: relative; border-radius: 8px; overflow: hidden; background: #0f172a; margin-bottom: 18px; aspect-ratio: 16/9;">
            <video controls poster="https://www.ascionline.in/academy/wp-content/uploads/2026/04/What-The-Sigma-Website-Banner-png.avif" preload="metadata" style="width: 100%; height: 100%; object-fit: cover;">
              <source src="https://www.ascionline.in/wp-content/uploads/2026/03/ASCI-Ad-Trust-Summit-2026-Desktop-.mp4" type="video/mp4">
            </video>
            <div style="position: absolute; top: 10px; left: 10px; background: rgba(0, 45, 98, 0.9); color: #fff; font-size: 0.72rem; font-weight: 700; padding: 3px 8px; border-radius: 4px; text-transform: uppercase; pointer-events: none;">
              Summit Keynote
            </div>
          </div>

          <h3 style="font-family: var(--font-serif); font-size: 1.35rem; font-weight: 700; color: #002d62; margin-bottom: 10px;">
            ASCI Academy Official Launch Event
          </h3>
          <p style="font-size: 0.92rem; color: #475569; line-height: 1.55; margin-bottom: 16px;">
            Inaugurated in the presence of industry leadership and media councils, setting the mission to train 100,000 future advertising practitioners.
          </p>

          <!-- Real Launch Photo Gallery Thumbnails from Live Media -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 18px;">
            <img src="assets/images/academy/DSC4471-1024x682.jpg" alt="Launch Gallery 1" style="width: 100%; height: 60px; object-fit: cover; border-radius: 6px;">
            <img src="assets/images/academy/DSC4380-1024x682.jpg" alt="Launch Gallery 2" style="width: 100%; height: 60px; object-fit: cover; border-radius: 6px;">
            <img src="assets/images/academy/DSC4546-1024x682.jpg" alt="Launch Gallery 3" style="width: 100%; height: 60px; object-fit: cover; border-radius: 6px;">
          </div>

          <a href="academy-about.html#genesis" style="display: inline-flex; align-items: center; gap: 6px; background: #002d62; color: #fff; padding: 9px 18px; border-radius: 6px; font-size: 0.88rem; font-weight: 700; text-decoration: none;">
            <span>Read Launch Story &rarr;</span>
          </a>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- 5. HOW CAN I COLLABORATE? -->
<section id="collaborate" style="padding: 72px 0; background: linear-gradient(180deg, #f8fafc 0%, #eef4f9 100%); border-top: 1px solid #e2e8f0;">
  <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 20px;">
    <div style="text-align: center; max-width: 720px; margin: 0 auto 44px auto;">
      <span style="font-family: var(--font-sans); font-size: 0.82rem; font-weight: 700; color: #086b59; text-transform: uppercase; letter-spacing: 0.08em; display: inline-block; margin-bottom: 6px;">
        Partner With The Academy
      </span>
      <h2 style="font-family: var(--font-serif); font-size: clamp(2rem, 3.2vw, 2.6rem); font-weight: 700; color: #002d62; margin-bottom: 12px;">
        How Can I Collaborate?
      </h2>
      <p style="font-size: 1.05rem; color: #475569; line-height: 1.6;">
        Join forces with ASCI Academy to build advertising people can trust. Select your path below.
      </p>
    </div>

    <!-- 3 Collaboration Tracks Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
      
      <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
        <div style="width: 40px; height: 40px; border-radius: 8px; background: rgba(0, 45, 98, 0.1); color: #002d62; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; margin-bottom: 14px;">
          1
        </div>
        <h3 style="font-family: var(--font-serif); font-size: 1.2rem; font-weight: 700; color: #002d62; margin-bottom: 8px;">
          Universities &amp; Colleges
        </h3>
        <p style="font-size: 0.9rem; color: #64748b; line-height: 1.55; margin: 0;">
          Bring ASCI-certified curriculum to your campus, host faculty workshops, and give students an accredited edge.
        </p>
      </div>

      <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
        <div style="width: 40px; height: 40px; border-radius: 8px; background: rgba(224, 88, 41, 0.1); color: #e05829; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; margin-bottom: 14px;">
          2
        </div>
        <h3 style="font-family: var(--font-serif); font-size: 1.2rem; font-weight: 700; color: #002d62; margin-bottom: 8px;">
          Brands &amp; Creative Agencies
        </h3>
        <p style="font-size: 0.9rem; color: #64748b; line-height: 1.55; margin: 0;">
          Book customized corporate masterclasses, train creative review teams, and integrate ethical UI/UX compliance.
        </p>
      </div>

      <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
        <div style="width: 40px; height: 40px; border-radius: 8px; background: rgba(8, 107, 89, 0.1); color: #086b59; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; margin-bottom: 14px;">
          3
        </div>
        <h3 style="font-family: var(--font-serif); font-size: 1.2rem; font-weight: 700; color: #002d62; margin-bottom: 8px;">
          Creators &amp; Talent Agencies
        </h3>
        <p style="font-size: 0.9rem; color: #64748b; line-height: 1.55; margin: 0;">
          Certify creator rosters in the Responsible Influencing standard and build transparent commercial disclosures.
        </p>
      </div>

    </div>

    <!-- Interactive Collaboration Form -->
    <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 36px; max-width: 780px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0, 45, 98, 0.06);">
      <h3 style="font-family: var(--font-serif); font-size: 1.35rem; font-weight: 700; color: #002d62; margin-bottom: 18px; text-align: center;">
        Inquire / Register Your Interest
      </h3>

      <form onsubmit="event.preventDefault(); alert('Thank you for reaching out to ASCI Academy! An Academy representative will connect with you shortly.'); this.reset();" style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 5px;">
          <label style="font-size: 0.86rem; font-weight: 700; color: #334155;">Full Name *</label>
          <input type="text" required placeholder="Your full name" style="padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 0.92rem; font-family: inherit;">
        </div>

        <div style="display: flex; flex-direction: column; gap: 5px;">
          <label style="font-size: 0.86rem; font-weight: 700; color: #334155;">Email Address *</label>
          <input type="email" required placeholder="name@organization.com" style="padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 0.92rem; font-family: inherit;">
        </div>

        <div style="display: flex; flex-direction: column; gap: 5px;">
          <label style="font-size: 0.86rem; font-weight: 700; color: #334155;">Organization / University *</label>
          <input type="text" required placeholder="Company or Institution name" style="padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 0.92rem; font-family: inherit;">
        </div>

        <div style="display: flex; flex-direction: column; gap: 5px;">
          <label style="font-size: 0.86rem; font-weight: 700; color: #334155;">Collaboration Area *</label>
          <select required style="padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 0.92rem; font-family: inherit; background: #fff;">
            <option value="">-- Please choose an option --</option>
            <option value="masterclass">Masterclass (Corporate / Agency)</option>
            <option value="fdp">Faculty Development Program (FDP)</option>
            <option value="app">College / University Curriculum Integration</option>
            <option value="reports">Research &amp; Reports Partnership</option>
            <option value="events">Events &amp; Webinars Collaboration</option>
            <option value="other">Other Inquiry</option>
          </select>
        </div>

        <div style="grid-column: 1 / -1; display: flex; flex-direction: column; gap: 5px;">
          <label style="font-size: 0.86rem; font-weight: 700; color: #334155;">Your Message / Objectives *</label>
          <textarea required rows="3" placeholder="Tell us about your team, student cohort, or collaboration goals..." style="padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 0.92rem; font-family: inherit; resize: vertical;"></textarea>
        </div>

        <div style="grid-column: 1 / -1; text-align: center; margin-top: 8px;">
          <button type="submit" style="background: #e05829; color: #ffffff; border: none; padding: 12px 32px; border-radius: 6px; font-size: 0.95rem; font-weight: 700; cursor: pointer; box-shadow: 0 4px 14px rgba(224, 88, 41, 0.3);">
            Submit Collaboration Request
          </button>
        </div>
      </form>
    </div>

  </div>
</section>

<!-- 6. FINAL ENROLLMENT CALLOUT BANNER -->
<section style="background: #002d62; padding: 56px 0; color: #ffffff; text-align: center;">
  <div class="container" style="max-width: 800px; margin: 0 auto; padding: 0 20px;">
    <h2 style="font-family: var(--font-serif); font-size: clamp(1.9rem, 3.2vw, 2.5rem); font-weight: 700; color: #ffffff; margin-bottom: 14px;">
      Ready to Champion Responsible Advertising?
    </h2>
    <p style="font-size: 1.08rem; color: #cbd5e1; line-height: 1.6; margin-bottom: 28px;">
      Join 50+ partner institutions and future leaders across India. An ASCI Academy credential sets you apart.
    </p>
    <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
      <a href="academy-courses.html" style="background: #e05829; color: #fff; padding: 12px 28px; border-radius: 6px; font-weight: 700; text-decoration: none; font-size: 0.95rem;">
        Explore All Courses
      </a>
      <a href="academy-about.html" style="background: transparent; color: #ffffff; border: 1.5px solid #ffffff; padding: 12px 24px; border-radius: 6px; font-weight: 600; text-decoration: none; font-size: 0.95rem;">
        About the Academy
      </a>
    </div>
  </div>
</section>"""

make_page(
    title="ASCI Academy – Courses, Workshops & Training in Advertising",
    breadcrumbs=[("Home", "index.html"), ("ASCI Academy", "")],
    content_html=hub_content,
    filename="academy.html"
)

# -------------------------------------------------------------
# 2. ABOUT ASCI ACADEMY: academy-about.html
# -------------------------------------------------------------
about_content = """
<!-- Hero Section -->
<section class="academy-hero">
  <div class="container">
    <div class="academy-hero-grid">
      <div class="academy-hero-text">
        <div class="academy-hero-badge">
          <span class="academy-hero-badge-dot"></span>
          <span>About Us · Governance &amp; Purpose</span>
        </div>
        <h1 class="academy-hero-title">Shaping the future of <span>ethical advertising</span>.</h1>
        <p class="academy-hero-subtitle">
          ASCI Academy is the specialized education, training, and research arm of The Advertising Standards Council of India (ASCI), established to cultivate a nationwide culture of honest, decent, and fair advertising.
        </p>
        <div class="academy-hero-actions">
          <a href="#vision-mission" class="btn-academy-primary">
            <span>Vision &amp; Mission</span>
          </a>
          <a href="#councils" class="btn-academy-secondary">
            <span>Governing Councils</span>
          </a>
          <a href="#partners" class="btn-academy-secondary">
            <span>Our Partners</span>
          </a>
        </div>
      </div>
      <div class="academy-hero-visual">
        <div class="academy-hero-card">
          <img src="assets/images/academy/ASCI-Academy-Launch.jpg" alt="ASCI Academy Launch" class="academy-hero-img">
          <div style="margin-top: 14px; color: #cbd5e1; font-size: 0.85rem;">
            <span>Launched in Mumbai with industry stalwarts and educators</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Vision & Mission -->
<section class="academy-section" id="vision-mission">
  <div class="container">
    <div class="academy-section-header">
      <span class="academy-section-kicker">Guiding Principles</span>
      <h2 class="academy-section-title">Vision, Mission &amp; Objectives</h2>
      <p class="academy-section-desc">
        Proactively embedding consumer protection and compliance values into every creative thought, marketing strategy, and technological design.
      </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px;">
      <div class="academy-program-card" style="padding: 36px 28px;">
        <div class="academy-program-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
        </div>
        <h3 class="academy-program-title">Our Vision</h3>
        <p class="academy-program-desc">
          To cultivate an advertising environment where voluntary compliance, honesty, and consumer welfare are intuitive cornerstones for every brand, platform, agency, and creator.
        </p>
      </div>

      <div class="academy-program-card" style="padding: 36px 28px;">
        <div class="academy-program-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        </div>
        <h3 class="academy-program-title">Our Mission</h3>
        <p class="academy-program-desc">
          To build industry-wide capability through certified courses, faculty enablement, academic curriculums, and deep empirical research in emerging advertising frontiers.
        </p>
      </div>

      <div class="academy-program-card" style="padding: 36px 28px;">
        <div class="academy-program-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        </div>
        <h3 class="academy-program-title">Core Objectives</h3>
        <p class="academy-program-desc">
          Equip next-generation practitioners, mitigate digital deceptive patterns, provide expert ad advisory, and safeguard consumer trust across Indian media channels.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Governing Councils -->
<section class="academy-section-alt" id="councils">
  <div class="container">
    <div class="academy-section-header">
      <span class="academy-section-kicker">Leadership</span>
      <h2 class="academy-section-title">Apex Council &amp; Advisory Board</h2>
      <p class="academy-section-desc">
        Guided by seasoned leaders spanning global FMCGs, media conglomerates, academia, consumer law, and digital platforms.
      </p>
    </div>

    <div class="academy-council-grid">
      <div class="academy-member-card">
        <img src="assets/images/academy/S.-Subramanyeswar.webp" alt="S. Subramanyeswar" class="academy-member-avatar">
        <h3 class="academy-member-name">S. Subramanyeswar</h3>
        <div class="academy-member-title">Apex Council Member</div>
        <div class="academy-member-org">Group CEO, MullenLowe Lintas Group</div>
      </div>

      <div class="academy-member-card">
        <img src="assets/images/academy/Manoj-Gadgil.jpg" alt="Manoj Gadgil" class="academy-member-avatar">
        <h3 class="academy-member-name">Manoj Gadgil</h3>
        <div class="academy-member-title">Apex Council Member</div>
        <div class="academy-member-org">VP &amp; Business Head, Britannia Industries</div>
      </div>

      <div class="academy-member-card">
        <img src="assets/images/academy/Amit-Kumar-Nanchahal.webp" alt="Amit Kumar Nanchahal" class="academy-member-avatar">
        <h3 class="academy-member-name">Amit Kumar Nanchahal</h3>
        <div class="academy-member-title">Apex Council Member</div>
        <div class="academy-member-org">Head of Corporate Communications, PepsiCo India</div>
      </div>

      <div class="academy-member-card">
        <img src="assets/images/academy/Kaustubh-Jha.webp" alt="Kaustubh Jha" class="academy-member-avatar">
        <h3 class="academy-member-name">Kaustubh Jha</h3>
        <div class="academy-member-title">Apex Council Member</div>
        <div class="academy-member-org">Marketing Lead &amp; Digital Strategist</div>
      </div>
    </div>
  </div>
</section>

<!-- Partners Ecosystem -->
<section class="academy-section" id="partners">
  <div class="container">
    <div class="academy-section-header">
      <span class="academy-section-kicker">Collaborative Network</span>
      <h2 class="academy-section-title">Academic &amp; Knowledge Partners</h2>
      <p class="academy-section-desc">
        Over 50 leading universities, colleges, and research institutes co-developing responsible advertising practices.
      </p>
    </div>

    <div class="academy-logos-grid">
      <div class="academy-logo-item"><img src="assets/images/academy/Jamia-Millia.png" alt="Jamia Millia"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/Symbiosis-Institute.png" alt="Symbiosis"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/IILM-University.png" alt="IILM"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/MDI-Gurgaon_23_11zon.png" alt="MDI"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/XLRI_8_11zon.png" alt="XLRI"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/TISS_4_11zon.png" alt="TISS"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/Bennett_10_11zon.png" alt="Bennett"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/Christ_12_11zon.png" alt="Christ University"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/BITS-LAW-School.png" alt="BITS Law School"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/Shaheed-Sukhdev_28_11zon.png" alt="Shaheed Sukhdev"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/Jesus-and-Mary-College_21_11zon.png" alt="Jesus and Mary"></div>
      <div class="academy-logo-item"><img src="assets/images/academy/St-Joseph-University_30_11zon.png" alt="St Joseph University"></div>
    </div>
  </div>
</section>
"""

make_page(
    title="About ASCI Academy – Vision, Governance & Partners",
    breadcrumbs=[("Home", "index.html"), ("ASCI Academy", "academy.html"), ("About Us", "")],
    content_html=about_content,
    filename="academy-about.html"
)

# -------------------------------------------------------------
# 3. OUR PROGRAMS: academy-programs.html
# -------------------------------------------------------------
programs_content = """
<!-- Hero Section -->
<section class="academy-hero">
  <div class="container">
    <div class="academy-hero-grid">
      <div class="academy-hero-text">
        <div class="academy-hero-badge">
          <span class="academy-hero-badge-dot"></span>
          <span>Education &amp; Training Programs</span>
        </div>
        <h1 class="academy-hero-title">Custom programs for <span>campuses, schools &amp; corporates</span>.</h1>
        <p class="academy-hero-subtitle">
          From university degree integrations and faculty development to interactive school media literacy and corporate regulatory masterclasses.
        </p>
        <div class="academy-hero-actions">
          <a href="#colleges" class="btn-academy-primary">
            <span>Higher Education</span>
          </a>
          <a href="#fdp" class="btn-academy-secondary">
            <span>Faculty Training</span>
          </a>
          <a href="#schools" class="btn-academy-secondary">
            <span>AdWise for Schools</span>
          </a>
          <a href="#corporates" class="btn-academy-secondary">
            <span>Corporate Masterclasses</span>
          </a>
        </div>
      </div>
      <div class="academy-hero-visual">
        <div class="academy-hero-card">
          <img src="assets/images/academy/Academic-Partnership-Program-Thumbnail-1.webp" alt="Academic Partnership Program" class="academy-hero-img">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Pillar 1: Colleges & Universities -->
<section class="academy-section" id="colleges">
  <div class="container">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center;">
      <div>
        <span class="academy-section-kicker">For Institutes &amp; Universities</span>
        <h2 class="academy-section-title">Academic Partnership Program (APP)</h2>
        <p class="academy-section-desc" style="margin-bottom: 20px;">
          The Academic Partnership Program (APP) bridges academic theory with live industry self-regulation. We partner with universities to embed certified modules on truthfulness, legal compliance, social decency, and digital ethics directly into undergraduate and postgraduate curricula.
        </p>
        <ul style="color: #475569; line-height: 1.8; margin-bottom: 24px; padding-left: 20px;">
          <li>Curriculum co-design with ASCI experts</li>
          <li>Access to 40+ years of ASCI case studies and complaints history</li>
          <li>Joint certification upon student course completion</li>
          <li>Guest lectures by advertising councils and regulatory authorities</li>
        </ul>
        <a href="academy.html#collaborate" class="btn-enroll-course">
          <span>Inquire for Your University</span>
        </a>
      </div>
      <div>
        <img src="assets/images/academy/DSC4569-1024x682.jpg" alt="University Training" style="width: 100%; border-radius: 16px; box-shadow: 0 12px 30px rgba(0,0,0,0.08);">
      </div>
    </div>
  </div>
</section>

<!-- Pillar 2: Faculty Development Program -->
<section class="academy-section-alt" id="fdp">
  <div class="container">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center;">
      <div>
        <img src="assets/images/academy/DSC4721-1024x682.jpg" alt="Faculty Development Program" style="width: 100%; border-radius: 16px; box-shadow: 0 12px 30px rgba(0,0,0,0.08);">
      </div>
      <div>
        <span class="academy-section-kicker">Educator Enablement</span>
        <h2 class="academy-section-title">Empowering Ethical Advertising – FDP</h2>
        <p class="academy-section-desc" style="margin-bottom: 20px;">
          The Faculty Development Program (FDP) trains professors, senior lecturers, and departmental deans in contemporary advertising laws, deceptive design patterns, influencer disclosure mandates, and case analysis methodologies.
        </p>
        <ul style="color: #475569; line-height: 1.8; margin-bottom: 24px; padding-left: 20px;">
          <li>Multi-day intensive certification sessions</li>
          <li>Practical workshops analyzing disputed campaigns</li>
          <li>Exclusive pedagogical toolkits and slide libraries</li>
          <li>Formal ASCI Certified Educator credentials</li>
        </ul>
        <a href="academy.html#collaborate" class="btn-enroll-course">
          <span>Join Faculty Program</span>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- Pillar 3: Schools & AdWise -->
<section class="academy-section" id="schools">
  <div class="container">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center;">
      <div>
        <span class="academy-section-kicker">Youth Digital Literacy</span>
        <h2 class="academy-section-title">The AdWise Program for Schools</h2>
        <p class="academy-section-desc" style="margin-bottom: 20px;">
          Children and adolescents encounter thousands of commercial messages daily across games, social apps, and online video. AdWise instills critical thinking, helping students distinguish between objective content, paid promotions, sponsored trends, and deceptive claims.
        </p>
        <ul style="color: #475569; line-height: 1.8; margin-bottom: 24px; padding-left: 20px;">
          <li>Age-appropriate interactive workshops</li>
          <li>Gamified exercises on spotting hidden ads</li>
          <li>Digital privacy and safe consumerism tips</li>
        </ul>
        <a href="academy.html#collaborate" class="btn-enroll-course">
          <span>Bring AdWise to Your School</span>
        </a>
      </div>
      <div>
        <img src="assets/images/academy/adwise-feat.webp" alt="AdWise School Program" style="width: 100%; border-radius: 16px; box-shadow: 0 12px 30px rgba(0,0,0,0.08);">
      </div>
    </div>
  </div>
</section>

<!-- Pillar 4: Corporate Masterclasses & Ad Advisory -->
<section class="academy-section-alt" id="corporates">
  <div class="container">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center;">
      <div>
        <img src="assets/images/academy/masterclass-at-castrol.jpg" alt="Corporate Masterclass" style="width: 100%; border-radius: 16px; box-shadow: 0 12px 30px rgba(0,0,0,0.08);">
      </div>
      <div>
        <span class="academy-section-kicker">Enterprise Solutions</span>
        <h2 class="academy-section-title">Corporate Masterclasses &amp; Ad Advisory</h2>
        <p class="academy-section-desc" style="margin-bottom: 20px;">
          On-site and hybrid customized workshops for corporate marketing, agency creative teams, brand custodians, and legal departments.
        </p>
        <ul style="color: #475569; line-height: 1.8; margin-bottom: 24px; padding-left: 20px;">
          <li>Sector-specific compliance (FMCG, Healthcare, EdTech, BFSI, Gaming)</li>
          <li>Dark patterns and UI/UX compliance audit training</li>
          <li>Ad Advisory: Pre-release non-binding guidance on draft campaign concepts</li>
          <li>Endorser due diligence advisory</li>
        </ul>
        <a href="academy.html#collaborate" class="btn-enroll-course">
          <span>Book Corporate Workshop</span>
        </a>
      </div>
    </div>
  </div>
</section>
"""

make_page(
    title="Our Programs – Universities, Schools & Corporate Masterclasses",
    breadcrumbs=[("Home", "index.html"), ("ASCI Academy", "academy.html"), ("Programs", "")],
    content_html=programs_content,
    filename="academy-programs.html"
)

# -------------------------------------------------------------
# 4. COURSES & CERTIFICATIONS: academy-courses.html
# -------------------------------------------------------------
courses_content = """
<!-- Hero Section -->
<section class="academy-hero">
  <div class="container">
    <div class="academy-hero-grid">
      <div class="academy-hero-text">
        <div class="academy-hero-badge">
          <span class="academy-hero-badge-dot"></span>
          <span>Online Learning &amp; Certification</span>
        </div>
        <h1 class="academy-hero-title">Certified courses in <span>advertising compliance &amp; ethics</span>.</h1>
        <p class="academy-hero-subtitle">
          Interactive eLearning modules designed by industry experts. Learn real-world regulatory compliance, dark pattern mitigation, and responsible influencer practices at your own pace.
        </p>
      </div>
      <div class="academy-hero-visual">
        <div class="academy-hero-card">
          <img src="assets/images/academy/Ethical_UI_UX_Designs_Certificate_UID.webp" alt="ASCI Academy Certificate" class="academy-hero-img">
          <div style="margin-top: 14px; color: #cbd5e1; font-size: 0.85rem;">
            <span>Digital verifiable certificates issued upon completion</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Courses Full Catalog -->
<section class="academy-section">
  <div class="container">

    <!-- Course 1 Detailed Card -->
    <div id="ethical-ui-ux" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; overflow: hidden; margin-bottom: 48px; box-shadow: 0 8px 24px rgba(0,0,0,0.04);">
      <div style="display: grid; grid-template-columns: 1fr 1.3fr; gap: 40px; padding: 40px; align-items: center;">
        <div>
          <img src="assets/images/academy/ethical-ui-ux-designs-building-consumer-trust-homepage-banner-desktop.webp" alt="Ethical UI UX" style="width: 100%; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.08);">
          <div style="margin-top: 20px;">
            <img src="assets/images/academy/Ethical_UI_UX_Designs_Certificate_UID.webp" alt="Certificate Preview" style="width: 100%; border-radius: 8px; border: 1px solid #e2e8f0;">
          </div>
        </div>
        <div>
          <span class="academy-course-badge" style="position: static; margin-bottom: 12px; display: inline-block;">Featured Course</span>
          <h2 class="academy-section-title" style="font-size: 1.85rem; margin-bottom: 14px;">Ethical UI/UX Designs: Building Consumer Trust</h2>
          <p class="academy-section-desc" style="margin-bottom: 20px;">
            Designed for Brand, Legal, and UI/UX professionals, this essential course equips you to spot online dark patterns before they trigger consumer backlash or regulatory action. Through real-world app simulations, you’ll learn to identify manipulative design tactics and explore ethical alternatives.
          </p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px; font-size: 0.9rem; color: #475569;">
            <div>✔ Deceptive Design Detection</div>
            <div>✔ Basket Sneaking &amp; Drip Pricing</div>
            <div>✔ Forced Action &amp; Interface Interference</div>
            <div>✔ Real-world App Simulations</div>
            <div>✔ Self-paced Online eLearning</div>
            <div>✔ Verifiable ASCI Certificate</div>
          </div>
          <div style="display: flex; gap: 16px; align-items: center;">
            <a href="https://www.ascionline.in/academy/product/ethical-ui-ux-designs-building-consumer-trust/" target="_blank" class="btn-enroll-course" style="font-size: 1rem; padding: 12px 28px;">
              <span>Enroll on ASCI Academy</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Course 2 Detailed Card -->
    <div id="influencing-playbook" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; overflow: hidden; margin-bottom: 48px; box-shadow: 0 8px 24px rgba(0,0,0,0.04);">
      <div style="display: grid; grid-template-columns: 1.3fr 1fr; gap: 40px; padding: 40px; align-items: center;">
        <div>
          <span class="academy-course-badge" style="position: static; margin-bottom: 12px; display: inline-block;">Creator Certification</span>
          <h2 class="academy-section-title" style="font-size: 1.85rem; margin-bottom: 14px;">The Responsible Influencing Playbook</h2>
          <p class="academy-section-desc" style="margin-bottom: 20px;">
            Elevate your influence with ASCI’s Responsible Influencing Playbook Certification Course. Tailored for today’s digital storytellers, this program delves into advertising codes, legal requirements, disclosure labels, and fostering responsible brand collaborations.
          </p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px; font-size: 0.9rem; color: #475569;">
            <div>✔ Mandatory Disclosure Rules (#Ad / #Sponsored)</div>
            <div>✔ Endorsement Due Diligence</div>
            <div>✔ Financial &amp; Health Claim Guardrails</div>
            <div>✔ Offered in English &amp; Hindi</div>
            <div>✔ Self-paced Video Lessons &amp; Quizzes</div>
            <div>✔ ASCI Certified Influencer Badge</div>
          </div>
          <div style="display: flex; gap: 16px; align-items: center;">
            <a href="https://www.ascionline.in/academy/course/the-responsible-influencing-playbook/" target="_blank" class="btn-enroll-course" style="font-size: 1rem; padding: 12px 28px;">
              <span>Enroll on ASCI Academy</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
        </div>
        <div>
          <img src="assets/images/academy/Responsible-Influencing-Playbook.png" alt="Responsible Influencing Playbook" style="width: 100%; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.08);">
          <div style="margin-top: 20px;">
            <img src="assets/images/academy/The_Responsible_Influencing_Playbook_UID_Certificate.webp" alt="Certificate Preview" style="width: 100%; border-radius: 8px; border: 1px solid #e2e8f0;">
          </div>
        </div>
      </div>
    </div>

    <!-- Course 3 Detailed Card -->
    <div id="guide-advertising" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.04);">
      <div style="display: grid; grid-template-columns: 1fr 1.3fr; gap: 40px; padding: 40px; align-items: center;">
        <div>
          <img src="assets/images/academy/guide-to-responsible-advertising.png" alt="Guide to Responsible Advertising" style="width: 100%; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.08);">
          <div style="margin-top: 20px;">
            <img src="assets/images/academy/Responsible_Advertising_Certificate_UID.webp" alt="Certificate Preview" style="width: 100%; border-radius: 8px; border: 1px solid #e2e8f0;">
          </div>
        </div>
        <div>
          <span class="academy-course-badge" style="position: static; margin-bottom: 12px; display: inline-block;">Foundational Course</span>
          <h2 class="academy-section-title" style="font-size: 1.85rem; margin-bottom: 14px;">The ASCI Guide to Responsible Advertising</h2>
          <p class="academy-section-desc" style="margin-bottom: 20px;">
            Explore this interactive eLearning experience that navigates through the core principles of the ASCI Code for advertising self-regulation. Immerse yourself in real-world advertisements and scenarios that bring these principles to life.
          </p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px; font-size: 0.9rem; color: #475569;">
            <div>✔ Truthful &amp; Honest Representations</div>
            <div>✔ Non-Offensive &amp; Decent Content</div>
            <div>✔ Safeguards Against Harmful Products</div>
            <div>✔ Fairness in Competition</div>
            <div>✔ Case Law &amp; Precedents</div>
            <div>✔ ASCI Certificate of Completion</div>
          </div>
          <div style="display: flex; gap: 16px; align-items: center;">
            <a href="https://www.ascionline.in/academy/product/the-ascis-guide-to-responsible-advertising/" target="_blank" class="btn-enroll-course" style="font-size: 1rem; padding: 12px 28px;">
              <span>Enroll on ASCI Academy</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
        </div>
      </div>
    </div>

  </div>
</section>
"""

make_page(
    title="Courses & Certifications – ASCI Academy",
    breadcrumbs=[("Home", "index.html"), ("ASCI Academy", "academy.html"), ("Courses", "")],
    content_html=courses_content,
    filename="academy-courses.html"
)

# -------------------------------------------------------------
# 5. RESEARCH REPORTS: academy-reports.html
# -------------------------------------------------------------
reports_content = """
<!-- Hero Section -->
<section class="academy-hero">
  <div class="container">
    <div class="academy-hero-grid">
      <div class="academy-hero-text">
        <div class="academy-hero-badge">
          <span class="academy-hero-badge-dot"></span>
          <span>Knowledge &amp; Evidence</span>
        </div>
        <h1 class="academy-hero-title">Research reports &amp; <span>white papers</span>.</h1>
        <p class="academy-hero-subtitle">
          Empirical studies and thought leadership publications examining generative AI, deceptive patterns, influencer credibility, and societal representation in Indian advertising.
        </p>
      </div>
      <div class="academy-hero-visual">
        <div class="academy-hero-card">
          <img src="assets/images/academy/Report-Thumbnail-What-The-Sigma.webp" alt="Latest Research Report" class="academy-hero-img">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Reports Full Library -->
<section class="academy-section">
  <div class="container">
    <div class="academy-section-header">
      <span class="academy-section-kicker">Publications</span>
      <h2 class="academy-section-title">Complete Research Library</h2>
      <p class="academy-section-desc">
        All reports are available for direct digital download in PDF format.
      </p>
    </div>

    <div class="academy-reports-grid">
      <!-- Report 1 -->
      <div class="academy-report-card" id="what-the-sigma">
        <div class="academy-report-thumb-wrap">
          <img src="assets/images/academy/Report-Thumbnail-What-The-Sigma.webp" alt="What The Sigma" class="academy-report-thumb">
        </div>
        <div class="academy-report-body">
          <span class="academy-report-tag">Youth &amp; Culture</span>
          <h3 class="academy-report-title">What The Sigma: Decoding Gen Z &amp; Gen Alpha</h3>
          <p class="academy-report-desc">
            A comprehensive study on slang, digital psychology, content consumption patterns, and commercial trust drivers among India's youngest consumers.
          </p>
          <a href="https://www.ascionline.in/wp-content/uploads/2026/03/What-The-Sigma-Report.pdf" target="_blank" class="btn-download-report">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Report (PDF)</span>
          </a>
        </div>
      </div>

      <!-- Report 2 -->
      <div class="academy-report-card" id="adnext">
        <div class="academy-report-thumb-wrap">
          <img src="assets/images/academy/ADnext-Thumbnail.jpg" alt="ADNext" class="academy-report-thumb">
        </div>
        <div class="academy-report-body">
          <span class="academy-report-tag">Digital Compliance</span>
          <h3 class="academy-report-title">ADNext: Navigating the Future of Digital Advertising</h3>
          <p class="academy-report-desc">
            An in-depth framework for advertisers and platforms addressing dark patterns, algorithmic consent, and consumer privacy safeguards.
          </p>
          <a href="https://www.ascionline.in/academy/wp-content/uploads/2025/03/ADNext-Report-digital.pdf" target="_blank" class="btn-download-report">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Report (PDF)</span>
          </a>
        </div>
      </div>

      <!-- Report 3 -->
      <div class="academy-report-card">
        <div class="academy-report-thumb-wrap">
          <img src="assets/images/academy/Manifest-Report-Thumnail.jpg" alt="Manifest Masculinities" class="academy-report-thumb">
        </div>
        <div class="academy-report-body">
          <span class="academy-report-tag">Representation</span>
          <h3 class="academy-report-title">Manifest Masculinities: Beyond The Mask</h3>
          <p class="academy-report-desc">
            A nationwide investigation into evolving male identities, non-stereotypical storytelling, and emotional vulnerability in contemporary Indian media.
          </p>
          <a href="https://www.ascionline.in/academy/wp-content/uploads/2025/03/Manifest-Masculinities-Beyond-The-Mask-Report-2025_Digital-Version.pdf" target="_blank" class="btn-download-report">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Report (PDF)</span>
          </a>
        </div>
      </div>

      <!-- Report 4 -->
      <div class="academy-report-card">
        <div class="academy-report-thumb-wrap">
          <img src="assets/images/academy/ASCI-Academy-Report-Thumbnail.jpg" alt="Navigating Cookies" class="academy-report-thumb">
        </div>
        <div class="academy-report-body">
          <span class="academy-report-tag">Data &amp; Privacy</span>
          <h3 class="academy-report-title">Navigating Cookies: Privacy in the Digital Age</h3>
          <p class="academy-report-desc">
            Guide on cookie deprecation, digital tracking transparency, consent banners, and ethical user data collection.
          </p>
          <a href="https://www.ascionline.in/academy/wp-content/uploads/2025/01/Navigating-Cookies-Digital-1.pdf" target="_blank" class="btn-download-report">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Report (PDF)</span>
          </a>
        </div>
      </div>

      <!-- Report 5 -->
      <div class="academy-report-card">
        <div class="academy-report-thumb-wrap">
          <img src="assets/images/academy/ASCI-Academy-Report-Thumbnail-4.jpg" alt="Conscious Patterns" class="academy-report-thumb">
        </div>
        <div class="academy-report-body">
          <span class="academy-report-tag">UX Ethics</span>
          <h3 class="academy-report-title">Conscious Patterns: Ethical Alternatives to Dark UX</h3>
          <p class="academy-report-desc">
            Comprehensive handbook detailing ethical design patterns, transparent checkout flows, and consumer-first digital architecture.
          </p>
          <a href="https://www.ascionline.in/academy/wp-content/uploads/2024/08/Consious-Patterns-Report-Summary.pdf" target="_blank" class="btn-download-report">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Report (PDF)</span>
          </a>
        </div>
      </div>

      <!-- Report 6 -->
      <div class="academy-report-card">
        <div class="academy-report-thumb-wrap">
          <img src="assets/images/academy/ASCI-Academy-joins-hands-with-Lexplosion-on-a-whitepaper-_Privacy-Progress_-Pillars-of-Digital-Bharat.jpg" alt="Privacy Progress" class="academy-report-thumb">
        </div>
        <div class="academy-report-body">
          <span class="academy-report-tag">Digital Bharat</span>
          <h3 class="academy-report-title">Privacy Progress: Pillars of Digital Bharat</h3>
          <p class="academy-report-desc">
            White paper on data protection in emerging tier-2 and rural consumer markets across India.
          </p>
          <a href="https://www.ascionline.in/academy/wp-content/uploads/2024/03/Report-Privacy-Progress_-Pillars-of-Digital-Bharat.pdf" target="_blank" class="btn-download-report">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Report (PDF)</span>
          </a>
        </div>
      </div>

      <!-- Report 7 -->
      <div class="academy-report-card" id="diversity-inclusion">
        <div class="academy-report-thumb-wrap">
          <img src="assets/images/academy/DI_thumbnail.png" alt="Diversity & Inclusion" class="academy-report-thumb">
        </div>
        <div class="academy-report-body">
          <span class="academy-report-tag">Diversity &amp; Inclusion</span>
          <h3 class="academy-report-title">D&amp;I Landscape of Indian Advertising</h3>
          <p class="academy-report-desc">
            Benchmark study evaluating gender parity, regional diversity, and age inclusivity across top advertising campaigns.
          </p>
          <a href="https://www.ascionline.in/academy/wp-content/uploads/2024/02/DI-and-Indian-Advertising-2023_Final_07.12.23.pdf" target="_blank" class="btn-download-report">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Report (PDF)</span>
          </a>
        </div>
      </div>

      <!-- Report 8 -->
      <div class="academy-report-card">
        <div class="academy-report-thumb-wrap">
          <img src="assets/images/academy/influencer-trust-300x232.png" alt="Influencer Trust" class="academy-report-thumb">
        </div>
        <div class="academy-report-body">
          <span class="academy-report-tag">Creator Trust</span>
          <h3 class="academy-report-title">Influencer Trust Report: Consumer Perceptions</h3>
          <p class="academy-report-desc">
            Evaluating Indian consumer perception of paid influencer disclosures, authenticity, and credibility of creator promotions.
          </p>
          <a href="https://www.ascionline.in/academy/wp-content/uploads/2023/08/influencer-trust-report.pdf" target="_blank" class="btn-download-report">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Report (PDF)</span>
          </a>
        </div>
      </div>

      <!-- Report 9 -->
      <div class="academy-report-card">
        <div class="academy-report-thumb-wrap">
          <img src="assets/images/academy/generative-ai-300x232.png" alt="Generative AI" class="academy-report-thumb">
        </div>
        <div class="academy-report-body">
          <span class="academy-report-tag">Artificial Intelligence</span>
          <h3 class="academy-report-title">Generative AI in Advertising: Opportunities &amp; Guardrails</h3>
          <p class="academy-report-desc">
            White paper on deepfakes, synthetic media disclosure, intellectual property, and ethical AI deployment in marketing.
          </p>
          <a href="https://www.ascionline.in/academy/wp-content/uploads/2023/08/Kco-WhitePaper-GenAI-D11-DIGITAL_LowRes-2.pdf" target="_blank" class="btn-download-report">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Report (PDF)</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

make_page(
    title="Research Reports & Whitepapers – ASCI Academy",
    breadcrumbs=[("Home", "index.html"), ("ASCI Academy", "academy.html"), ("Reports", "")],
    content_html=reports_content,
    filename="academy-reports.html"
)

# -------------------------------------------------------------
# 6. LEARNER LOGIN & ACCOUNT PORTAL: academy-login.html
# -------------------------------------------------------------
login_content = """
<!-- LEARNER PORTAL & DASHBOARD SHOWCASE -->
<section style="background: linear-gradient(180deg, #f0f7ff 0%, #ffffff 100%); padding: 60px 0 80px 0; min-height: 80vh;">
  <div class="container" style="max-width: 1040px;">

    <!-- Page Header -->
    <div style="text-align: center; margin-bottom: 40px;">
      <div style="display: inline-flex; align-items: center; gap: 8px; padding: 6px 14px; background: rgba(0, 45, 98, 0.08); border-radius: 999px; margin-bottom: 14px;">
        <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #002d62;"></span>
        <span style="font-size: 0.82rem; font-weight: 700; color: #002d62; text-transform: uppercase; letter-spacing: 0.08em;">
          ASCI Academy LMS &amp; Student Portal
        </span>
      </div>
      <h1 style="font-family: var(--font-serif); font-size: clamp(2.2rem, 3.8vw, 3rem); font-weight: 700; color: #002d62; margin-bottom: 12px;">
        Learner Account &amp; Course Portal
      </h1>
      <p style="font-size: 1.1rem; color: #64748b; max-width: 620px; margin: 0 auto;">
        Access your enrolled self-paced certifications, watch video lectures, track course progress, and download verified certificates.
      </p>
    </div>

    <!-- Tab Switcher (Showcase Design) -->
    <div style="display: flex; justify-content: center; margin-bottom: 36px;">
      <div style="background: #e2e8f0; padding: 4px; border-radius: 10px; display: inline-flex; gap: 4px;">
        <button id="tabBtnLogin" onclick="switchPortalTab('login')" style="padding: 10px 24px; border-radius: 8px; border: none; font-size: 0.95rem; font-weight: 700; cursor: pointer; background: #002d62; color: #fff; transition: all 0.2s ease;">
          Learner Sign In
        </button>
        <button id="tabBtnDashboard" onclick="switchPortalTab('dashboard')" style="padding: 10px 24px; border-radius: 8px; border: none; font-size: 0.95rem; font-weight: 700; cursor: pointer; background: transparent; color: #475569; transition: all 0.2s ease;">
          Student Dashboard Preview
        </button>
      </div>
    </div>

    <!-- VIEW 1: SIGN IN FORM -->
    <div id="viewLogin" style="max-width: 520px; margin: 0 auto; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 40px; box-shadow: 0 10px 30px rgba(0, 45, 98, 0.08);">
      <h2 style="font-family: var(--font-serif); font-size: 1.5rem; font-weight: 700; color: #002d62; margin-bottom: 8px; text-align: center;">
        Sign In to Your Courses
      </h2>
      <p style="font-size: 0.92rem; color: #64748b; text-align: center; margin-bottom: 28px;">
        Use your registered email or institutional credentials.
      </p>

      <form onsubmit="event.preventDefault(); switchPortalTab('dashboard');" style="display: flex; flex-direction: column; gap: 18px;">
        <div>
          <label style="display: block; font-size: 0.88rem; font-weight: 700; color: #334155; margin-bottom: 6px;">
            Email Address or Student ID
          </label>
          <input type="email" required value="priya.sharma@agency.com" placeholder="name@organization.com" style="width: 100%; box-sizing: border-box; padding: 12px 14px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; font-family: inherit;">
        </div>

        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <label style="font-size: 0.88rem; font-weight: 700; color: #334155;">Password</label>
            <a href="#" onclick="alert('Password reset link sent to your registered email.'); return false;" style="font-size: 0.82rem; color: #e05829; font-weight: 600; text-decoration: none;">Forgot password?</a>
          </div>
          <input type="password" required value="••••••••••••" placeholder="Enter your password" style="width: 100%; box-sizing: border-box; padding: 12px 14px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; font-family: inherit;">
        </div>

        <div style="display: flex; align-items: center; gap: 8px;">
          <input type="checkbox" id="rememberMe" checked style="width: 16px; height: 16px; accent-color: #002d62; cursor: pointer;">
          <label for="rememberMe" style="font-size: 0.88rem; color: #64748b; cursor: pointer;">Keep me logged in on this browser</label>
        </div>

        <button type="submit" style="background: #002d62; color: #fff; padding: 13px; border-radius: 8px; border: none; font-size: 1rem; font-weight: 700; cursor: pointer; transition: background 0.2s ease; margin-top: 6px; box-shadow: 0 4px 12px rgba(0, 45, 98, 0.25);">
          Log In &amp; Access Dashboard
        </button>
      </form>

      <div style="display: flex; align-items: center; gap: 12px; margin: 26px 0;">
        <div style="flex-grow: 1; height: 1px; background: #e2e8f0;"></div>
        <span style="font-size: 0.82rem; color: #94a3b8; font-weight: 600; text-transform: uppercase;">Or Login With</span>
        <div style="flex-grow: 1; height: 1px; background: #e2e8f0;"></div>
      </div>

      <div style="display: flex; flex-direction: column; gap: 10px;">
        <button onclick="switchPortalTab('dashboard')" style="display: flex; align-items: center; justify-content: center; gap: 10px; width: 100%; padding: 11px; border: 1px solid #cbd5e1; border-radius: 8px; background: #f8fafc; font-size: 0.9rem; font-weight: 600; color: #334155; cursor: pointer;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#002d62" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
          <span>University Campus / Institutional SSO</span>
        </button>
      </div>

      <div style="margin-top: 28px; text-align: center; border-top: 1px solid #f1f5f9; padding-top: 20px;">
        <span style="font-size: 0.9rem; color: #64748b;">Not enrolled yet?</span>
        <a href="academy-courses.html" style="font-size: 0.9rem; color: #e05829; font-weight: 700; text-decoration: none; margin-left: 6px;">Browse All Courses &rarr;</a>
      </div>
    </div>

    <!-- VIEW 2: INTERACTIVE STUDENT DASHBOARD SHOWCASE -->
    <div id="viewDashboard" style="display: none;">
      
      <!-- Learner Welcome Header -->
      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; box-shadow: 0 4px 16px rgba(0,0,0,0.04); margin-bottom: 28px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
        <div style="display: flex; align-items: center; gap: 18px;">
          <div style="width: 58px; height: 58px; border-radius: 50%; background: #002d62; color: #ffffff; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; font-weight: 800; font-family: var(--font-serif);">
            PS
          </div>
          <div>
            <div style="font-size: 0.85rem; font-weight: 700; color: #e05829; text-transform: uppercase; letter-spacing: 0.05em;">Learner Portal • Enrolled Member</div>
            <h2 style="font-family: var(--font-serif); font-size: 1.55rem; font-weight: 700; color: #002d62; margin: 4px 0;">
              Welcome back, Priya Sharma
            </h2>
            <div style="font-size: 0.9rem; color: #64748b;">Member ID: <b>ASCI-LRN-2026-8812</b> • Enterprise Brand License</div>
          </div>
        </div>

        <div style="display: flex; gap: 10px;">
          <a href="academy-courses.html" style="display: inline-flex; align-items: center; gap: 6px; background: #e05829; color: #fff; padding: 10px 18px; border-radius: 8px; font-size: 0.88rem; font-weight: 700; text-decoration: none;">
            <span>Enroll in New Course</span>
          </a>
          <button onclick="switchPortalTab('login')" style="background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; padding: 10px 16px; border-radius: 8px; font-size: 0.88rem; font-weight: 600; cursor: pointer;">
            Sign Out
          </button>
        </div>
      </div>

      <!-- Course Progress Grid -->
      <div style="display: grid; grid-template-columns: 1.3fr 0.7fr; gap: 28px; align-items: start;">
        
        <!-- Left Column: Active Enrolled Courses -->
        <div style="display: flex; flex-direction: column; gap: 20px;">
          <h3 style="font-family: var(--font-serif); font-size: 1.35rem; font-weight: 700; color: #002d62; margin: 0;">
            My Enrolled Certifications
          </h3>

          <!-- Course 1 (In Progress) -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-size: 0.78rem; font-weight: 800; color: #086b59; background: rgba(8, 107, 89, 0.1); padding: 3px 10px; border-radius: 999px; text-transform: uppercase;">
                In Progress • 65% Completed
              </span>
              <span style="font-size: 0.85rem; color: #64748b; font-weight: 600;">Module 3 of 4</span>
            </div>
            
            <h4 style="font-family: var(--font-serif); font-size: 1.25rem; font-weight: 700; color: #002d62; margin: 8px 0;">
              Ethical UI/UX Designs: Building Consumer Trust
            </h4>
            
            <div style="width: 100%; height: 8px; background: #e2e8f0; border-radius: 999px; overflow: hidden; margin: 14px 0 16px 0;">
              <div style="width: 65%; height: 100%; background: #086b59; border-radius: 999px;"></div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.88rem; color: #475569;">
              <span>Next Lesson: <b>Simulated E-Commerce Checkout Dark Patterns</b></span>
              <a href="academy-courses.html#ethical-ui-ux" style="display: inline-flex; align-items: center; gap: 6px; background: #002d62; color: #fff; padding: 8px 16px; border-radius: 6px; font-weight: 700; text-decoration: none;">
                <span>Resume Lesson</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </a>
            </div>
          </div>

          <!-- Course 2 (Completed with Verified Certificate) -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
              <span style="font-size: 0.78rem; font-weight: 800; color: #002d62; background: #e0f2fe; padding: 3px 10px; border-radius: 999px; text-transform: uppercase;">
                &#10003; 100% Completed • Certified
              </span>
              <span style="font-size: 0.85rem; color: #059669; font-weight: 700;">Grade: Distinction (94%)</span>
            </div>
            
            <h4 style="font-family: var(--font-serif); font-size: 1.25rem; font-weight: 700; color: #002d62; margin: 8px 0;">
              The Responsible Influencing Playbook
            </h4>
            
            <div style="width: 100%; height: 8px; background: #e2e8f0; border-radius: 999px; overflow: hidden; margin: 14px 0 16px 0;">
              <div style="width: 100%; height: 100%; background: #002d62; border-radius: 999px;"></div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.88rem; color: #475569;">
              <span>Credential: <b>ASCI-CERT-2026-7731</b></span>
              <button onclick="alert('Downloading Official ASCI Academy Certificate PDF for Priya Sharma (Credential ID: ASCI-CERT-2026-7731)...')" style="display: inline-flex; align-items: center; gap: 6px; background: #086b59; color: #fff; padding: 8px 16px; border-radius: 6px; font-weight: 700; border: none; cursor: pointer;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
                <span>Download Certificate (PDF)</span>
              </button>
            </div>
          </div>

        </div>

        <!-- Right Column: Digital Verification & Upcoming Masterclasses -->
        <div style="display: flex; flex-direction: column; gap: 20px;">
          
          <!-- Verifiable Credential Box -->
          <div style="background: #fff8f5; border: 1px solid #ffd8c7; border-radius: 14px; padding: 24px;">
            <div style="font-size: 0.78rem; font-weight: 800; color: #e05829; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;">
              Digital Credential Vault
            </div>
            <h4 style="font-family: var(--font-serif); font-size: 1.15rem; font-weight: 700; color: #002d62; margin-bottom: 10px;">
              Verifiable Blockchain Certificate
            </h4>
            <p style="font-size: 0.88rem; color: #475569; line-height: 1.55; margin-bottom: 16px;">
              All ASCI Academy certificates carry cryptographic verification recognized by leading advertising agencies, brands, and law firms.
            </p>
            <div style="display: flex; gap: 8px;">
              <button onclick="alert('Certificate link copied to clipboard! You can paste it on LinkedIn or your CV.')" style="flex: 1; padding: 9px; background: #e05829; color: #fff; border: none; border-radius: 6px; font-weight: 700; font-size: 0.85rem; cursor: pointer;">
                Copy Shareable Link
              </button>
              <button onclick="window.open('https://www.linkedin.com', '_blank')" style="padding: 9px 14px; background: #0077b5; color: #fff; border: none; border-radius: 6px; font-weight: 700; font-size: 0.85rem; cursor: pointer;">
                Add to LinkedIn
              </button>
            </div>
          </div>

          <!-- Upcoming Live Sessions -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 24px;">
            <h4 style="font-family: var(--font-serif); font-size: 1.15rem; font-weight: 700; color: #002d62; margin-bottom: 14px;">
              Upcoming Live Masterclasses
            </h4>
            <div style="border-left: 3px solid #002d62; padding-left: 12px; margin-bottom: 14px;">
              <div style="font-size: 0.82rem; color: #e05829; font-weight: 700;">Live Webinar • Next Tuesday, 4 PM</div>
              <div style="font-size: 0.92rem; font-weight: 700; color: #002d62; margin-top: 2px;">Generative AI Claims Substantiation</div>
            </div>
            <div style="border-left: 3px solid #086b59; padding-left: 12px;">
              <div style="font-size: 0.82rem; color: #086b59; font-weight: 700;">Workshop • Dec 5, 11 AM</div>
              <div style="font-size: 0.92rem; font-weight: 700; color: #002d62; margin-top: 2px;">Green Claims &amp; ESG Advertising Law</div>
            </div>
          </div>

        </div>

      </div>

    </div>

  </div>
</section>

<script>
function switchPortalTab(tab) {
  const btnLogin = document.getElementById('tabBtnLogin');
  const btnDash = document.getElementById('tabBtnDashboard');
  const viewLogin = document.getElementById('viewLogin');
  const viewDash = document.getElementById('viewDashboard');

  if (tab === 'dashboard') {
    btnLogin.style.background = 'transparent';
    btnLogin.style.color = '#475569';
    btnDash.style.background = '#002d62';
    btnDash.style.color = '#fff';
    viewLogin.style.display = 'none';
    viewDash.style.display = 'block';
  } else {
    btnDash.style.background = 'transparent';
    btnDash.style.color = '#475569';
    btnLogin.style.background = '#002d62';
    btnLogin.style.color = '#fff';
    viewDash.style.display = 'none';
    viewLogin.style.display = 'block';
  }
}
</script>
"""

make_page(
    title="Learner Account & LMS Portal",
    breadcrumbs=[("Home", "index.html"), ("ASCI Academy", "academy.html"), ("Learner Portal", "")],
    content_html=login_content,
    filename="academy-login.html"
)

print("\n=== ALL ACADEMY PAGES BUILT SUCCESSFULLY ===")
