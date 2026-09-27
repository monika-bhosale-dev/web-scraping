# 03 — Web Scraping Workflow

Every scraping project, regardless of tool, follows roughly the same pipeline. Knowing this workflow lets you plan a scraper before writing a single line of code.

## The standard workflow

1. **Define the goal** — what exact fields do you need, from what pages, how often? ("Product name, price, rating from every listing page of category X, refreshed daily" is a real spec; "scrape the site" is not.)
2. **Analyze the target site** — is it static or dynamic (see `05_static_vs_dynamic_websites.md`)? Does it have a public/hidden API? What's the URL pattern for pagination? (See `08_website_analysis.md`, `09_url_analysis.md`.)
3. **Choose the approach & tools** — `requests`+BS4 for static, Selenium/Playwright for JS-heavy, Scrapy for large multi-page crawls, direct API calls where available (`06_scraping_approaches.md`).
4. **Fetch the content** — send the request (or drive the browser) and get raw HTML/JSON back. Handle headers, cookies, and session state as needed.
5. **Parse & extract** — use CSS selectors/XPath/regex to pull the exact fields out of the raw content.
6. **Clean & validate** — strip whitespace, fix types (strings → numbers/dates), handle missing fields, de-duplicate.
7. **Store** — write to CSV/JSON for small jobs, or a database (PostgreSQL/MongoDB) for anything ongoing or large.
8. **Handle errors & retries** — network failures, changed selectors, blocked requests — build for failure, not just the happy path.
9. **Respect the target & scale responsibly** — rate limiting, robots.txt, legal/ethical bounds (`13_legal_and_ethical_considerations.md`).
10. **Monitor & maintain** — websites change their HTML/structure over time; a scraper that works today can silently break next month. Logging and alerting matter here.

## Why this order matters

Steps 1–3 happen *before* code, and skipping them is the single biggest reason scrapers turn into rewrites. Spending 15 minutes in DevTools analyzing a site before writing code routinely saves hours of fighting the wrong tool for the job (e.g., writing Selenium automation for a page that actually has a clean JSON API underneath it).

## A quick mental checklist before coding

- [ ] I know exactly which fields I need
- [ ] I've opened DevTools and checked Network tab for a JSON API
- [ ] I know if the content is present in the initial HTML or injected by JavaScript
- [ ] I know the pagination/URL pattern
- [ ] I've checked robots.txt and the site's terms
- [ ] I know where the data is going to live once extracted

---
**Next:** [04 — Web Scraping vs Web Crawling](04_web_scraping_vs_web_crawling.md)
