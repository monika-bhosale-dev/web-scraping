# 14 — Learning Roadmap

This ties the fundamentals in this module to the rest of the repo, in the order it's meant to be worked through.

## Suggested path

### Phase 1 — Foundations (you are here)
`00_introduction/` — mental model, workflow, legal/ethical grounding. No code required, but don't skip it; every later decision assumes this context.

### Phase 2 — Static content
`01_requests/` → `02_parsing_bs4_lxml_xpath/`
Learn to fetch and parse static HTML end to end: sessions, headers, pagination, proxy rotation, retries, then CSS/XPath extraction, table parsing, and cleanup. By the end: a full static-site scraper, request-to-storage.

### Phase 3 — Dynamic content (pick one first, learn both eventually)
`03_selenium/` and `04_playwright/`
Browser automation for JS-heavy sites — waits, form interaction, infinite scroll, proxy/stealth handling in a browser context. Playwright's network interception (`04.3`) is worth reaching early — it often removes the need for browser automation entirely once you see how to grab the API call directly.

### Phase 4 — Direct APIs
`06_api_scraping/`
Once comfortable finding hidden APIs via DevTools (from `08_website_analysis.md`), formalize it: auth patterns, pagination, rate-limit handling, GraphQL. This is often the fastest, most stable extraction method when available — worth prioritizing over browser automation when both are options.

### Phase 5 — Scale
`05_scrapy/`
Bring requests + parsing + concurrency + error handling into one structured framework, for multi-page/production-scale crawling. Layer in `scrapy-playwright` for the JS-heavy pages within a larger crawl.

### Phase 6 — Persistence
`07_storage_sql_mongo/`
Move from CSV files to real storage — schema design, bulk inserts, dedup, choosing SQL vs. Mongo per project shape.

### Phase 7 — Quality & crossover
`08_testing_sdet_crossover/`
Treat scrapers like tested software: Page Object Model, pytest fixtures, data validation suites, CI integration. This phase is also where scraping skills most directly transfer into SDET/test-automation work.

### Phase 8 — Capstones
`10_capstone_projects/`
Combine everything into 2–3 full projects spanning your actual domain experience (e-commerce, aviation, B2B) — each one deliberately mixing methods (e.g., API + Selenium fallback + database) the way real projects do.

## How to actually use this roadmap

- Don't wait to feel "ready" to move phases — each phase's mini-projects are the readiness check.
- Revisit `12_scraping_challenges.md` and `13_legal_and_ethical_considerations.md` mentally every time you start a new target site, not just once at the start.
- Track progress per-module in each folder's own `README.md` (mark what's built, what's still open) rather than only here.

This roadmap is deliberately sequential but not rigid — if a real project pulls you into Scrapy before you've finished Selenium, follow the project; come back and fill gaps afterward.
