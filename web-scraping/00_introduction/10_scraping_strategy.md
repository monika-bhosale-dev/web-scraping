# 10 — Scraping Strategy

Once you've analyzed a target site (`08`, `09`), you need a plan before writing code. A scraping strategy answers: how will I discover pages, how will I fetch them, how will I handle scale and failure, and how will I keep this running over time?

## Key strategic decisions

### 1. Discovery strategy — how do you find every page you need?
- **Sitemap-based** — many sites expose `/sitemap.xml` listing every URL; fastest, most complete option when available
- **Crawl-based** — follow category → listing → detail page links (see `04_web_scraping_vs_web_crawling.md`)
- **URL-pattern-based** — construct URLs directly if IDs/pagination follow a predictable pattern (see `09_url_analysis.md`)
- **API-based** — call a paginated API endpoint until it stops returning results

### 2. Fetch strategy — sequential, concurrent, or scheduled?
- **One-off, small job** — a simple sequential script is fine
- **Large job, need speed** — concurrent requests (`asyncio`/`aiohttp`, or Scrapy's built-in concurrency)
- **Ongoing/recurring job** — needs scheduling (cron, Scrapyd, Airflow) and incremental logic (only fetch what's new/changed)

### 3. Resilience strategy — what happens when things go wrong?
- Network errors → retry with backoff (`tenacity`, Scrapy's `RetryMiddleware`)
- Blocked/rate-limited → slow down, rotate proxies/headers, respect `Retry-After`
- Selector no longer matches (site changed) → validation checks that alert you rather than silently returning empty data
- Partial failure → log failed URLs to a retry queue instead of losing them

### 4. Politeness strategy — how much load are you putting on the target?
- Add delay/jitter between requests
- Respect `robots.txt` crawl-delay directives where present
- Scale concurrency conservatively, especially against smaller sites without CDN protection
- See `13_legal_and_ethical_considerations.md` for the full picture

## A simple strategy template to fill out per project

```
Target: _______________________
Data needed: ___________________
Static or dynamic: _____________
Discovery method: ______________
Fetch method (tool): ___________
Estimated volume: ______________
Frequency (one-off / recurring): ___
Storage destination: ___________
Known risks/blockers: __________
```

Filling this out for every new scraping target, even informally, turns "let me just start coding" into a plan — and catches problems (like discovering you actually need Selenium, not requests) before you've written 200 lines of the wrong approach.

---
**Next:** [11 — Data Extraction Strategy](11_data_extraction_strategy.md)
