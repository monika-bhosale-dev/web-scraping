# 12 — Scraping Challenges

Real websites actively resist automated access, and even ones that don't will still throw structural and operational problems at you. This is a map of the challenges you'll hit — each gets its own hands-on treatment later in the relevant tool module.

## Anti-bot & access challenges

- **IP-based rate limiting/blocking** — too many requests from one IP gets you throttled or banned → addressed with rate limiting + proxy rotation (`01_requests/`, `03_selenium/`, `04_playwright/`, `05_scrapy/`)
- **User-Agent / header fingerprinting** — requests missing realistic browser headers get flagged → header spoofing/rotation
- **Browser fingerprinting** — headless browsers can be detected via JS-level signals (missing plugins, `navigator.webdriver` flag, etc.) → stealth tools (`undetected-chromedriver`, `playwright-stealth`)
- **CAPTCHAs** — explicit human-verification challenges → largely a "stop and reconsider" signal rather than something to defeat; covered honestly in `08_testing_sdet_crossover/8.5`
- **Login walls / session requirements** — data only visible after authentication → session/cookie management, or `storage_state` reuse in Playwright

## Structural/dynamic content challenges

- **JavaScript-rendered content** — handled via browser automation or finding the underlying API (`05_static_vs_dynamic_websites.md`)
- **Infinite scroll / lazy loading** — content loads incrementally as you scroll → simulate scroll events or find the paginated API call behind it
- **Inconsistent HTML across pages** — same "type" of page rendered slightly differently → defensive selectors, `contains()`, fallback logic
- **A/B tested layouts** — some sites serve different HTML structures to different visitors → selectors that need to handle multiple variants

## Operational challenges

- **Scale** — thousands/millions of pages requires concurrency, queuing, and infrastructure planning, not just a for-loop
- **Maintenance** — sites redesign; scrapers silently break; needs monitoring/alerting, not "set and forget"
- **Data quality drift** — a selector matching the *wrong* element (not zero elements) is worse than an obvious failure — validate values, not just presence
- **Legal/ethical boundaries** — not every challenge is technical; some data simply shouldn't be scraped, or needs explicit permission (`13_legal_and_ethical_considerations.md`)

## The right mindset

None of these challenges mean "scraping doesn't work" — they mean scraping is an engineering discipline with failure modes like any other, and production-grade scrapers are built assuming things will go wrong, not hoping they won't.

---
**Next:** [13 — Legal and Ethical Considerations](13_legal_and_ethical_considerations.md)
