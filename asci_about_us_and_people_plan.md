# ASCI Website: About Us & People Architecture Plan
*(Updated with FSSAI-Style Institutional Directory Model)*

> **Design & Tone Mandate**:
> *"Keep the overall approach simple, minimalistic, and easy to navigate, in line with the rest of the website framework. Avoid overly high-end language, jargon, or anything promotional or chest-thumping. The tone should feel straightforward, credible, and informative."*

---

## 1. Executive Summary & Page Distribution

Rather than fragmenting the site into dozens of thin pages (many containing only 1–2 paragraphs), the content is structured into **focused, purposeful destinations**:

1. **`about-us.html` (Main Overview Page)**:
   - The primary gateway providing high-level context: ASCI's mandate, foundation (1985), 4 core code pillars (Honest, Decent, Safe, Fair), high-level impact metrics, an interactive timeline teaser, governance summary, and quick links to deep-dive resources.
2. **`people.html` (Unified People & Governance Directory Hub)**:
   - **FSSAI Directory Reference Model**: A single unified directory featuring:
     - **Live Search & Filter Bar** (search by name, designation, company, panel/committee).
     - **View Toggle**: Switch between **Directory Table View** (compact, scannable institutional format) and **Grid/Card View** (visual profiles).
     - **Click-to-View Full Details**: Clicking any row or card triggers an elegant, accessible **Profile Modal / Detail Drawer** with the member's complete bio, role, and sector background.
3. **`history-key-milestones.html`**:
   - The complete chronological journey from 1985 to 2026 (including recent landmarks: Dark Patterns study, Greenwashing guidelines, Generative AI whitepaper, ASCI Academy).
4. **`the-work-we-do.html`**:
   - Practical walkthrough of ASCI's operations: Pre-production advisory (preventative), complaint management (corrective), proactive AI monitoring (NAMS), and consumer advocacy.
5. **`annual-reports.html` & `campaigns.html`**:
   - Dedicated archives for transparent annual disclosures, complaint outcome trends, and public awareness campaigns (#ChupNaBaitho, etc.).

---

## 2. Updated Mega Menu Structure

The Mega Menu for **About Us** directly matches the approved structure:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Know ASCI, our people and our journey.                                                │
│                                                                                        │
│  ORGANISATION                               PEOPLE                                     │
│  • Purpose & vision                         • Board of Governors & Consultative        │
│  • The work we do & its impact                Committee                                │
│  • History & key milestones                 • ASCI Leadership Team                     │
│  • Awards & recognition                     • Consumer Complaints Council (CCC)        │
│  • Annual reports                           • Independent Review Panel                 │
│  • Our past campaigns                       • Technical experts                        │
│  • Explore careers with ASCI                • Ad advisory expert panel                 │
│  • Subscribe to our newsletter              • Ad Advisory technical experts            │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Mega Menu Routing:
- **Organisation Links**:
  - `Purpose & vision` ➔ `about-us.html#purpose`
  - `The work we do & its impact` ➔ `the-work-we-do.html`
  - `History & key milestones` ➔ `history-key-milestones.html`
  - `Awards & recognition` ➔ `about-us.html#awards`
  - `Annual reports` ➔ `annual-reports.html`
  - `Our past campaigns` ➔ `campaigns.html`
  - `Explore careers with ASCI` ➔ `careers.html`
  - `Subscribe to our newsletter` ➔ `about-us.html#newsletter`
- **People Links** (All anchor directly into filtered directory views on `people.html`):
  - `Board of Governors & Consultative Committee` ➔ `people.html?panel=board#directory`
  - `ASCI Leadership Team` ➔ `people.html?panel=leadership#directory`
  - `Consumer Complaints Council` ➔ `people.html?panel=ccc#directory`
  - `Independent Review Panel` ➔ `people.html?panel=review-panel#directory`
  - `Technical experts` ➔ `people.html?panel=technical-experts#directory`
  - `Ad advisory expert panel` ➔ `people.html?panel=ad-advisory#directory`
  - `Ad Advisory technical experts` ➔ `people.html?panel=advisory-tech-experts#directory`

---

## 3. Blueprint: `people.html` with FSSAI Directory System

Inspired by the **FSSAI Directory structure** (`fssai.gov.in/about-us/directory`), the ASCI People page provides both institutional efficiency and modern UX.

### Key Functional Features:
1. **Live Search Bar**:
   - Real-time search by person’s name, role (e.g. *Chairman*, *Secretary General*, *Civil Society Member*), or organisation (e.g. *Pidilite*, *DoCA*, *HUL*, *Google*).
2. **Category / Panel Pills**:
   - `[ All (35+) ]`
   - `[ ASCI Leadership (Secretariat) ]`
   - `[ Board of Governors ]`
   - `[ Consultative Committee ]`
   - `[ Consumer Complaints Council (CCC) ]`
   - `[ Independent Review Panel (Judiciary) ]`
   - `[ Technical & Ad Advisory Experts ]`
3. **Dual View Toggle**:
   - **Table View (Default / FSSAI style)**: Compact, scannable table ideal for quick directory lookups.
   - **Card / Grid View**: Modern responsive profile cards with member portraits and titles.
4. **Click-to-View Detail Drawer / Modal**:
   - Clicking any table row or card opens a clean slide-over drawer / modal showing:
     - High-resolution photo & full name
     - Official designation within ASCI & primary organization
     - Sector representation (e.g. *Civil Society / Legal / Advertiser / Media*)
     - Detailed professional biographical summary
     - Specific committee tenure and governance mandate

---

### Directory Table Schema (FSSAI-Inspired):

| # | Name & Portrait | ASCI Designation | Primary Organization / Affiliation | Panel / Body | Action |
|---|---|---|---|---|---|
| 1 | **Sudhanshu Vats** | Chairman | Managing Director, Pidilite Industries Ltd | Board of Governors | `[ View Details → ]` |
| 2 | **Manisha Kapoor** | CEO & Secretary General | ASCI Secretariat / VP, ICAS | Leadership Team | `[ View Details → ]` |
| 3 | **S. Subramanyeswar** | Vice Chairman | Group CEO & CSO-APAC, MullenLowe Lintas | Board of Governors | `[ View Details → ]` |
| 4 | **Paritosh Joshi** | Hon. Treasurer | Principal, Provocateur Advisory | Board of Governors | `[ View Details → ]` |
| 5 | **Barnita Dasgupta** | Chief Financial & Admin Officer | ASCI Secretariat | Leadership Team | `[ View Details → ]` |
| 6 | **Saheli Sinha** | Director, Operations | ASCI Secretariat | Leadership Team | `[ View Details → ]` |
| 7 | **Rohit Kumar Singh** | Eminent Member | Member, NCDRC; Former Secretary, DoCA | Board / Eminent | `[ View Details → ]` |
| 8 | **Civil Society Reps** | CCC Member | Independent panelist (Legal, Medicine, Consumer) | Consumer Complaints Council | `[ View Details → ]` |
| ... | *(30+ Verified Members)* | ... | ... | ... | `[ View Details → ]` |

---

## 4. Blueprint: Main `about-us.html` Page

A clean, minimalist gateway highlighting ASCI's mandate, principles, and direct paths to the directories and reports.

### Section-by-Section Wireframe:
```
┌──────────────────────────────────────────────────────────────────────┐
│ 1. Header & Breadcrumb                                               │
│    - Home > About Us                                                 │
│    - Title: "About ASCI"                                             │
│    - Subhead: "The Advertising Standards Council of India –          │
│      Established in 1985 as an independent self-regulatory body      │
│      committed to honest, decent, safe, and fair advertising."       │
├──────────────────────────────────────────────────────────────────────┤
│ 2. Foundational Pillars (Clean 4-Card Grid)                          │
│    - 1. Honest Representations (Claims backed by substantiation)     │
│    - 2. Non-Offensive to Public Decency (Respectful community norms) │
│    - 3. Safeguard Against Harm (Protection of minors, safety rules)  │
│    - 4. Fairness in Competition (Truthful comparison, no disparaging)│
├──────────────────────────────────────────────────────────────────────┤
│ 3. What We Do (Preventive & Corrective Framework)                    │
│    - Left: Preventive (Advisory services, training, guidelines)      │
│    - Right: Corrective (Complaint processing, independent CCC review)│
│    - CTA Link: "Explore The Work We Do & Its Impact →"               │
├──────────────────────────────────────────────────────────────────────┤
│ 4. Key Milestones at a Glance (Minimalist Decade Timeline)           │
│    - 1985: Foundation by advertisers, agencies, and media            │
│    - 2000s: Official statutory alignment & broadcaster adoption      │
│    - 2020: NAMS proactive digital tracking & influencer guidelines  │
│    - 2024–2026: Greenwashing guidelines, AI studies & ASCI Academy   │
│    - CTA Link: "View Full 40-Year Timeline & Milestones →"           │
├──────────────────────────────────────────────────────────────────────┤
│ 5. People & Governance Spotlight                                     │
│    - Explaining the tri-fold institutional balance:                  │
│      * Board of Governors (Strategy & industry stewardship)          │
│      * Consumer Complaints Council (Independent, 50%+ civil society) │
│      * Secretariat (Daily operations & complaint processing)         │
│    - CTA Link: "Open Institutional Directory & Member Search →"      │
├──────────────────────────────────────────────────────────────────────┤
│ 6. Annual Reports, Inquiries & Newsletter Strip                      │
│    - Download link for latest Complaints Report                      │
│    - One-click newsletter subscription input                         │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 5. Technical Implementation Details

1. **Design Tokens & Typography**:
   - Fonts: `Domine` (headings) and `Bricolage Grotesque` (body & tabular data).
   - Brand Teal: `#008779` & Deep Emerald: `#086b59`.
   - Table Styling: Clean borders (`#e2e8f0`), subtle hover highlighting (`#f8fafc`), alternating rows, and responsive horizontal scroll on mobile.
2. **Search & Filter Engine**:
   - Lightweight, instant client-side JavaScript filter:
     ```javascript
     function filterDirectory(query, panel) {
       // Filters members instantly without page reloads
     }
     ```
3. **Modal / Detail Drawer**:
   - Accessible, ESC-closable modal with smooth slide-up animation.
   - Preserves state and allows sharing direct member profiles via URL hash (e.g. `people.html#vats`).

---

## 6. Execution Roadmap

1. **Phase 1: Update Mega Menu in `ASCI (3).html`**
   - Implement the exact 2-column layout + left highlight box from your screenshot.
2. **Phase 2: Build `people.html` (The FSSAI-Inspired Directory Hub)**
   - Complete directory table with instant search, category pill filters, table/grid toggle, and the detailed profile modal.
3. **Phase 3: Build `about-us.html` (Overview Gateway)**
   - Minimalist structure, 4 pillars, timeline teaser, work & impact overview, and direct links to `people.html`.
4. **Phase 4: Build Supporting Pages**
   - `history-key-milestones.html` (interactive chronological timeline).
   - `the-work-we-do.html` (preventative vs. corrective operational guide).
5. **Phase 5: Verification & Review**
   - Test search, modal popups, responsive table scrolling on mobile, and menu navigation.
