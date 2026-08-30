# 📝 Changelog

All notable changes to **Web Development Mastery** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2.1.0] — 2026-08-30

### 🐛 Bug Fixes
- Fixed truncated GitHub SVG icon in creator section of landing page
- Fixed footer quick links pointing to `#` instead of actual page files (privacy.html, terms.html, thanks.html, 404.html)
- Fixed LinkedIn social link with invalid leading space in href attribute
- Fixed broken `JS/index.html` module links across developer.html, support.html, and Follow-Sanskar.html (changed to `JavaScript/index.html`)
- Fixed theme localStorage key inconsistency in support.html (`hub-theme` → `hubMasteryTheme`)

### ✨ New Features
- **Keyboard Shortcuts Modal** — Press `Ctrl+K` to open a navigation shortcut guide (module jumps, theme toggle, donate)
- **Learning Roadmap Timeline** — Step-by-step visual timeline showing HTML → CSS → JavaScript → React progression path
- **Testimonials Section** — Social proof section with developer quotes and avatar cards
- **FAQ Accordion** — 6 collapsible frequently asked questions with smooth animations and ARIA accessibility
- **Newsletter Signup** — Client-side email subscription form with localStorage persistence
- **Cookie Consent Banner** — Non-intrusive localStorage consent banner
- **Enhanced Stats Counter** — Additional stat cards for themes (25+) and pages (42)

### 🎨 UI/UX Improvements
- **Smooth Scroll Reveal Animations** — IntersectionObserver-based fade-up animations for all sections
- **Progress Ring Scroll-to-Top** — Circular SVG progress indicator replacing simple scroll button
- **Prefers-Reduced-Motion Support** — Respects user accessibility preferences to disable animations
- **Print Stylesheet** — Clean print layout hiding interactive elements
- **Active Navbar Highlighting** — Highlights the currently visible section's navigation link

### 📄 Secondary Pages
- Added scroll-to-top button to all 7 secondary pages
- Fixed developer.html placeholder social links and missing footer bottom bar
- Added missing meta tags (favicon, theme-color, og:image, JSON-LD) across all pages
- Added ARIA accessibility attributes across all pages
- Fixed improperly nested BMC buttons in privacy.html and terms.html
- Added missing X/Twitter social icon in thanks.html and 404.html footers
- Added Follow-Sanskar link to developer.html and support.html navigation

### 🔧 SEO & Performance
- Added `sitemap.xml` with complete page listing for search engines
- Added `robots.txt` with sitemap reference
- Added security meta tags (X-Content-Type-Options, Referrer-Policy) across all pages

### 📖 Documentation
- Added `CONTRIBUTING.md` — open-source contributor guide with development guidelines
- Added `CHANGELOG.md` — this file

---

## [2.0.0] — 2026-08-01

### ✨ Major Features
- Complete platform with 4 modules: HTML, CSS, JavaScript, React
- 500+ concepts with deep-dive explanations
- Live code sandboxes with CodeMirror integration
- 25+ premium themes with custom theme builder
- Gamified progress tracking with XP and levels
- Quiz system with score tracking
- Cheat sheets for all modules
- Mastery Center with interview Q&A and flashcards
- Command Palette (Ctrl+K) for module navigation
- Zen Mode for distraction-free learning
- Text-to-Speech accessibility
- Export/Import progress across devices
- Full responsive design for all screen sizes
- Premium glassmorphic dark UI
- Splash screen with logo animation
- Donate overlay with Razorpay integration
- Buy Me a Coffee integration across all pages

### 📄 Pages
- Landing page (index.html) with module cards
- About page with developer profile
- Developer documentation hub
- Privacy policy
- Support & FAQ portal
- Terms of service
- Thanks & acknowledgements page
- Custom 404 error page
- Follow Sanskar social links page
- Module-specific versions of all secondary pages (×4 modules = 28 pages)

---

## [1.0.0] — 2026-01-01

### ✨ Initial Release
- HTML Mastery module with 100 tags
- Basic progress tracking
- Single theme support
- Core code playground
