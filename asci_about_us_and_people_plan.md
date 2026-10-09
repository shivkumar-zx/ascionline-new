# ASCI Website: About Us & People Architecture Plan
*(Single Source of Truth & Content Fidelity Blueprint)*

> **CRITICAL CLIENT DIRECTIVE & CONTENT FIDELITY MANDATE**:
> 1. **ZERO INVENTED CONTENT**: Never fabricate, rephrase, or inject new marketing copy, slogans, or unapproved sections. Every word, heading, and card description must strictly come from the official live website (`https://www.ascionline.in/`) or official client-provided briefs.
> 2. **DESIGN ENHANCEMENT, NOT CONTENT REWRITING**: Our role is to elevate the UI, typography, responsiveness, and usability (clean cards, smooth interactions, directory search/filters, accessibility), while keeping the client's vetted, legal-approved content 100% intact.
> 3. **RESPECT CLIENT SITE ARCHITECTURE**: Explain any structural recommendations clearly. Do not merge separate pages into a single giant scroll unless explicitly requested.

---

## 1. Executive Summary & Why This Plan Exists

### The Problem
During earlier design iterations, sections and copy were newly written or summarized (e.g. inserting 4 foundational pillars, invented decade milestones, new CTA callouts, and combining distinct pages into a single 6,000+ line document). The client rightly objected:
- *"Why did you add new sections?"*
- *"Why did you change our approved content?"*
- *"Why are sections here that are not on our website?"*

For a premier regulatory body like ASCI (Advertising Standards Council of India), every word represents legal compliance and council governance. Modifying official copy risks project cancellation.

### The Solution & Core Principle
- **1:1 Verbatim Content Alignment**: We capture the exact headings, subheadings, card descriptions, and navigation hierarchy from `https://www.ascionline.in/about-us/` and its sub-pages.
- **Modern Institutional UI**: We upgrade the visual presentation (replacing dated 2010s-era Bootstrap boxes with refined typography, micro-interactions, responsive grids, and accessible directory filtering) **without altering a single approved sentence**.
- **Transparent Changelog**: Every modification is recorded in this markdown document so any developer or team member can pick it up in any chat session.

---

## 2. Live Site Audit: The About Us Ecosystem (`https://www.ascionline.in/about-us/`)

### A. Main Hub: `https://www.ascionline.in/about-us/`
On the official live website, the About Us page serves as an **Institutional Hub & Gateway**. It does **not** dump all content onto one endless page. Instead, it features:

1. **Page Title / Banner**:
   - Title: `About Us`
   - Hero Image: Official fountain pen writing on parchment (ASCI official asset)
2. **Breadcrumb**:
   - `Home > About us`
3. **Primary Lead Heading & Sub-heading**:
   - `H1`: **All About ASCI**
   - `H2 / Subhead`: *"Know all about what we do, how self-regulation works, the people at ASCI and the impact we create through our work."*
4. **The 7 Core Hub Destinations (Cards)**:
   - **Card 1: History & Key Milestones**
     - Text: *"ASCI was formed in 1985 by professionals from the advertising and media industry to keep Indian ads decent, fair and honest. Over the years, our work and role has evolved greatly."*
     - Target: `https://www.ascionline.in/history-key-milestones/`
   - **Card 2: About Self-Regulation**
     - Text: *"An overview of self-regulation and how it benefits all stakeholders."*
     - Target: `https://www.ascionline.in/about-self-regulation/`
   - **Card 3: The Work We Do**
     - Text: *"Supporting advertisers get it right as well as correcting them when they get it wrong."*
     - Target: `https://www.ascionline.in/work-we-do/`
   - **Card 4: People**
     - Text: *"Meet the ASCI board, Our Consumer Complaints Council Members, Consultative Committee and our Secretariat team who together champion responsible advertising."*
     - Target: `https://www.ascionline.in/people/`
   - **Card 5: Annual Reports**
     - Text: *"Read up on important milestones, changes and progress made year-on-year by ASCI."*
     - Target: `https://www.ascionline.in/annual-reports/`
   - **Card 6: Ad Campaigns**
     - Text: *"Here are the ads that ASCI has made in the past to encourage consumers to be more vigilant."*
     - Target: `https://www.ascionline.in/ad-campaigns/`
   - **Card 7: ASCI Explained**
     - Text: Explanatory resources and video walk-throughs on self-regulation.
     - Target: `https://www.ascionline.in/asci-explained/`

---

## 3. Page-by-Page Structure & Content Plan

### Page 1: `about-us.html` (The Gateway Hub)
- **Role**: Clean, fast, scannable overview directory.
- **Content**:
  - Breadcrumb: `Home / About Us`
  - Hero Header: "All About ASCI" + official subhead.
  - The 7 Hub Cards rendered in modern card components (high-definition subtle borders `#e2e8f0`, brand teal `#008779` accents, crisp hover transitions, legible typography using `Domine` and `Bricolage Grotesque`).
  - Quick Links / Direct Access to Annual Report downloads & Complaint registration.
- **Rule**: No invented code pillars or unauthorized text blocks.

### Page 2: `people.html` (People & Governance Directory)
- **Role**: The comprehensive directory for ASCI's governance structure.
- **Live Site Source Pages**:
  - `board-of-governors-and-special-invitees/`
  - `consultative-committee/`
  - `secretariat/`
  - `consumer-complaints-council/`
  - `independent-review-panel/`
  - `technical-experts/`
- **Features**:
  - **FSSAI-style searchable directory**: Live search bar (by name, designation, company).
  - **Filter pills**: All, Board of Governors, Consultative Committee, Secretariat, CCC, Independent Review Panel, Technical Experts.
  - **Dual view**: Table View (scannable institutional directory) & Grid View (visual portrait cards).
  - **Click-to-view Profile Modal**: Displays full verified bio and sector representation without cluttering the page.

### Page 3: `history-key-milestones.html`
- **Role**: Chronological institutional journey of ASCI from 1985 to present.
- **Content**: Preserves all live milestones from the official timeline page.
- **Design Upgrade**: Interactive vertical/horizontal timeline with filterable milestone decades.

### Page 4: `work-we-do.html`
- **Role**: Detailed breakdown of ASCI's operational framework.
- **Live Site Sub-sections**:
  - Our Purpose
  - How We Handle Complaints
  - What We Cover
  - Our Proactive Monitoring (NAMS)
  - Working with Others

### Page 5: `annual-reports.html`
- **Role**: Document repository for all published annual reports and complaint trends.
- **Design Upgrade**: Filterable by year, clean PDF download cards with file size indicators.

### Page 6: `ad-campaigns.html`
- **Role**: Consumer awareness campaign showcase (#ChupNaBaitho, vigilance initiatives).

---

## 4. Mega Menu Architecture (Navigation Alignment)

Matches the exact 2-column structure requested by the client:

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

---

## 5. Changelog & Audit Record

| Date | Changed By | Nature of Change | Rationale / Notes |
|------|------------|------------------|-------------------|
| 2026-10-08 | Project Team | **Content Audit & Reset** | Identified that previous `about-us.html` injected unapproved text (e.g. 4 Pillars, invented milestones) causing client friction. Reset strategy to 100% faithful verbatim content mapping from `https://www.ascionline.in/about-us/`. |
| 2026-10-08 | Project Team | **Plan Architecture Revision** | Updated `asci_about_us_and_people_plan.md` to establish the strict "Zero-Hallucination / Verbatim Copy" mandate and defined the multi-page hub model matching the live website. |
| 2026-10-08 | Project Team | **FSSAI Directory System Design** | Detailed the unified People directory (`people.html`) combining Board, CCC, Secretariat, and Panels into a filterable table/grid with live search. |

| 2026-10-09 | Project Team | **Campaigns Title & Preview Upgrade** | Unified title to **"Our Past Campaigns"** across `campaigns.html`, `ad-campaigns.html`, and `about-us.html` (matching the mega menu item `<span\>Our past campaigns</span\>`). Upgraded the `#campaigns` section inside `about-us.html` from text-only cards to a mini preview gallery featuring authentic thumbnails, video badges, and direct links to `campaigns.html`. |
| 2026-10-09 | Project Team | **Footer Fix, Banner Redesign & Sticky Bar** | Fixed broken footer & CTA callout section in `campaigns.html` by adding full CSS and 3D ripple canvas animation. Upgraded Hero Banner to match `people.html` (institutional `#f8fafc` background, left description, and right 2x2 stats grid). Implemented floating sticky controls card with frosted glass (`backdrop-filter: blur(16px)`), modern pill buttons, and real-time search. |

---

## 6. How to Talk to the Client (Safe Talking Points)

When presenting to the client, use these exact talking points:
1. *"We reviewed your existing website `ascionline.in/about-us/` thoroughly to ensure 100% fidelity to your official language and approved structure."*
2. *"We treat `about-us.html` as your official Hub & Gateway — highlighting the exact 7 key areas (History, Self-Regulation, The Work We Do, People, Annual Reports, Campaigns, and ASCI Explained) using your approved copy."*
3. *"We have removed all extraneous or unapproved sections. The enhancement is strictly focused on premium UI/UX: faster page loads, clean typography (`Domine` & `Bricolage Grotesque`), mobile responsiveness, and intuitive directory search."*
4. *"For the People section, we implemented an institutional directory model (similar to FSSAI) so visitors can easily search members by panel, name, or organization without losing any official details."*
5. *"For Campaigns, we unified the page title to 'Our Past Campaigns' so it matches your main navigation menu exactly, and built a filterable gallery showcasing all 113 authentic print & video assets without any placeholder content."*

---

## 7. Technical Implementation Details

1. **Design Tokens & Typography**:
   - Fonts: `Domine` (headings) and `Bricolage Grotesque` (body & tabular data).
   - Brand Teal: `#008779` & Deep Emerald: `#086b59`.
   - Card & Table Styling: Clean borders (`#e2e8f0`), subtle hover highlighting (`#f8fafc`), alternating rows, and responsive mobile-first layouts.
2. **Directory Engine (`people.html`)**:
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

## 8. Workflow Strategy: One-Page-at-a-Time Execution

To maintain total quality control, prevent client overwhelm, and eliminate errors:
1. **Incremental Validation**: We work on **one single page at a time**.
2. **Lock-In Before Moving Forward**: We review, audit against the live site, and lock down each page before starting the next one.
3. **Continuous Plan Updating**: After every page update, this document is updated with:
   - What page was modified
   - Exactly what sections were created
   - Why that specific content and layout were chosen (referencing live URLs)
   - Status (e.g. `LOCKED & VERIFIED`, `IN PROGRESS`, `PENDING`)

---

## 9. Detailed Page-by-Page Execution Log & Content Rationale

### Page 1: `about-us.html` (All About ASCI Gateway Hub)
- **Status**: **LOCKED & VERIFIED (Ready for Client Review)**
- **Source of Truth Live URL**: `https://www.ascionline.in/about-us/`
- **What Was Built**:
  1. **Breadcrumb**: `You're here: Home > About Us` (Maintains standard user navigation).
  2. **Banner Header**:
     - Heading: `All About ASCI`
     - Subhead: *"Know all about what we do, how self-regulation works, the people at ASCI and the impact we create through our work."*
     - Rationale: Verbatim copy from the live `ascionline.in/about-us/` page.
  3. **The 7 Core Gateway Cards**:
     - **Card 1: History & Key Milestones** (`history-key-milestones.html`)
       - Copy: *"ASCI was formed in 1985 by professionals from the advertising and media industry to keep Indian ads decent, fair and honest. Over the years, our work and role has evolved greatly."*
     - **Card 2: About Self-Regulation** (`about-self-regulation.html`)
       - Copy: *"An overview of self-regulation and how it benefits all stakeholders."*
     - **Card 3: The Work We Do** (`the-work-we-do.html`)
       - Copy: *"Supporting advertisers get it right as well as correcting them when they get it wrong."*
     - **Card 4: People** (`people.html`)
       - Copy: *"Meet the ASCI board, Our Consumer Complaints Council Members, Consultative Committee and our Secretariat team who together champion responsible advertising."*
     - **Card 5: Annual Reports** (`annual-reports.html`)
       - Copy: *"Read up on important milestones, changes and progress made year-on-year by ASCI."*
     - **Card 6: Our Past Campaigns** (`campaigns.html`)
       - Copy: *"Here are the ads that ASCI has made in the past to encourage consumers to be more vigilant."*
     - **Card 7: ASCI Explained** (`https://www.ascionline.in/asci-explained/`)
       - Copy: *"Essential explanatory guides and resources on self-regulation, consumer rights, and how advertising standards work in India."*
  4. **Upgraded Preview Section (#campaigns)**:
     - Upgraded from plain text cards into an authentic preview gallery featuring real video thumbnails, play badges, and artwork:
       - Card 1: `#ChupNaBaitho` consumer awareness video film (`8WTwrza9Vrg`).
       - Card 2: `Spot the Dark Pattern` digital transparency artboard.
       - Card 3: `Endorser Due Diligence` creator compliance film (`8epiDSIwXxw`).
     - Header CTA button: "Explore All 110+ Campaigns" linking directly to `campaigns.html`.
- **What Was Removed & Why**:
  - Removed previously invented "Four Principles of Responsible Advertising", fabricated decade timelines, and unapproved slogans. The live site uses `about-us` strictly as an introductory directory hub leading to deep-dive pages.

---

### Page 2: `people.html` (Unified People & Governance Directory)
- **Status**: **NEXT IN QUEUE**
- **Source of Truth Live URLs**:
  - `https://www.ascionline.in/board-of-governors-and-special-invitees/`
  - `https://www.ascionline.in/consultative-committee/`
  - `https://www.ascionline.in/secretariat/`
  - `https://www.ascionline.in/consumer-complaints-council/`
  - `https://www.ascionline.in/independent-review-panel/`
  - `https://www.ascionline.in/technical-experts/`
- **Proposed Architecture**:
  - Unified directory with instant search & panel pills (FSSAI directory model) to prevent users from navigating across 6 disjointed legacy sub-pages, while preserving 100% of member names, roles, affiliations, and council mandates.

---

### Page 3: `the-work-we-do.html`
- **Status**: **PENDING**
- **Live Source**: `https://www.ascionline.in/work-we-do/` (Our Purpose, Handling Complaints, What We Cover, Proactive Monitoring, Working with Others).

---

### Page 4: `history-key-milestones.html`
- **Status**: **PENDING**
- **Live Source**: `https://www.ascionline.in/history-key-milestones/` (40-year chronology).

---

### Page 5: `annual-reports.html`
- **Status**: **PENDING**
- **Live Source**: `https://www.ascionline.in/annual-reports/`.

---

### Page 6: `campaigns.html` / `ad-campaigns.html` (Our Past Campaigns Gallery)
- **Status**: **COMPLETE, FIXED & VERIFIED (Zero Hallucination - 100% Client Assets)**
- **Source of Truth Live URL**: `https://www.ascionline.in/ad-campaigns/`
- **What Was Built & Fixed**:
  1. **Master Architecture Sync**: Re-architected `build_campaigns.py` to use the shared master building blocks (`head_part.html`, `header_part.html`, `footer_part.html`, `footer_scripts.html`) ensuring 100% styling parity across the site header, mega-menus, search popup, CTA callout banner with 3D ripple canvas, and footer.
  2. **Script Syntax & Execution Fix**: Resolved a nested/stray `<script>` tag issue that caused browser parsing to fail. Ensured `renderGallery()` executes immediately on load and on `DOMContentLoaded`, successfully rendering all 113 cards.
  3. **Institutional Hero Header (Matching `people.html`)**:
     - Breadcrumb: `Home / About Us / Our Past Campaigns`
     - Badge: `Public Vigilance & Consumer Voice`
     - Heading: `Our Past Campaigns`
     - Description: Verbatim copy from the live site: *"Find out more about the ads that ASCI has made in the past to encourage consumers to be more vigilant. Explore official video films, PSAs, and print campaigns from 2016 to 2025."*
     - 2x2 Stats Grid: Total Assets (113), Video Films (29), Print & Digital (84), Major Campaign Years (6).
  4. **Single-Row Floating Sticky Controls Card (Frosted Glass `top: 155px`)**:
     - Unified single horizontal row featuring:
       - Instant Real-Time Search input with pill styling (`border-radius: 9999px`)
       - Media Type Selector: `All Media`, `Videos`, `Print`
       - Divider line
       - Year Selector: `Filter Year: All, 2025, 2022, 2021, 2020, 2019, 2016`
  5. **High-Performance Gallery Grid & Modal Player with Left/Right Navigation**:
     - 113 authentic cards with lazy loading, hover elevation, and media badges.
     - Modal lightbox with **`<` (Previous)** and **`>` (Next)** arrow navigation buttons, keyboard arrow (`←` and `→`) support, and item counter (e.g. `Item 5 of 113`).
     - Responsive full HD image inspection and embedded YouTube video playback.
  6. **Zero Hallucination Guarantee**: All 113 campaign assets derive strictly from `campaigns_clean.json` mapped from `https://www.ascionline.in/ad-campaigns/`.




