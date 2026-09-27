# 06 — Scraping Approaches

There isn't one way to scrape a site — there are four broad approaches, and choosing the right one is a direct consequence of what you learned in `05_static_vs_dynamic_websites.md`. This repo's `01`–`06` folders each cover one of these in depth.

## 1. HTTP requests + HTML parsing
Send raw HTTP requests (`requests`/`httpx`), parse the returned HTML with BeautifulSoup/lxml/XPath. No browser involved.
- **Best for:** static sites, server-rendered content
- **Pros:** fast, lightweight, easy to scale/concurrent
- **Cons:** can't execute JavaScript — useless against dynamic content
- **Covered in:** `01_requests/`, `02_parsing_bs4_lxml_xpath/`

## 2. Browser automation
Drive an actual (or headless) browser — Selenium or Playwright — which executes JavaScript exactly like a real user's browser would, then extract data from the fully rendered DOM.
- **Best for:** JS-heavy dynamic sites, sites requiring clicks/scrolls/logins to reveal content
- **Pros:** works on almost anything a human can see
- **Cons:** slower, heavier resource usage, more detectable as a bot
- **Covered in:** `03_selenium/`, `04_playwright/`

## 3. Direct API calls
Skip HTML entirely — find the JSON API the site's own JavaScript calls (via DevTools Network tab) and call it yourself with `requests`.
- **Best for:** dynamic sites where the underlying data comes from a clean internal or public API
- **Pros:** fast, stable (JSON structure changes less often than HTML/CSS), no browser needed
- **Cons:** APIs can be undocumented, may require auth tokens/signing, can change without notice
- **Covered in:** `06_api_scraping/`

## 4. Framework-based crawling
Use a purpose-built crawling framework (Scrapy) that combines requests, parsing, pipelines, and concurrency into one structured project — with optional browser rendering plugged in (`scrapy-playwright`) when needed.
- **Best for:** large-scale, multi-page, production-grade crawling jobs
- **Pros:** built-in concurrency, retries, pipelines, middleware, scales to millions of pages
- **Cons:** steeper learning curve, more setup than a single script
- **Covered in:** `05_scrapy/`

## Decision guide

| Situation | Approach |
|---|---|
| Content visible in page source | Requests + parsing |
| Content only appears after JS runs, but a JSON API is visible in Network tab | Direct API calls |
| Content only appears after JS runs, no clean API found | Browser automation |
| Need to log in, click, scroll to reveal content | Browser automation |
| Thousands+ of pages, ongoing/production job | Scrapy (with browser plugin if needed) |

In practice, real projects often combine these — e.g., Scrapy for the crawl structure, with `scrapy-playwright` middleware for the handful of pages that need JS rendering.

---
**Next:** [07 — Scraping Tools Overview](07_scraping_tools_overview.md)
