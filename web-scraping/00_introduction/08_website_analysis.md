# 08 — Website Analysis

Before writing any scraper, spend time in the browser's DevTools understanding exactly how the target site delivers its data. This single habit prevents most wasted effort in scraping projects.

## The DevTools workflow

Open DevTools (F12 or right-click → Inspect) and work through these tabs:

### 1. Elements tab
Shows the **live DOM** — HTML as currently rendered, including anything JavaScript injected after load. Use this to:
- Identify the CSS classes/IDs/structure around the data you need
- Hover over elements to see them highlighted on the page
- Right-click any element → **Copy → Copy selector** or **Copy XPath** as a starting point (usually needs cleanup, but saves time)

### 2. Network tab
The most valuable tab for scraping. Reload the page with this tab open and Filter set to **Fetch/XHR**. You're looking for:
- Requests returning JSON — this is often the site's actual data source, callable directly (see `06_api_scraping/`)
- The exact URL, method (GET/POST), headers, and payload each request uses
- Whether requests need auth tokens/cookies, and where those come from

If you find a clean JSON endpoint here, you very likely don't need a browser automation tool at all.

### 3. View Page Source (not the Elements tab)
Shows the **raw HTML** the server actually sent, before any JavaScript runs. Compare this against the Elements tab:
- Same content in both? → static page, `requests` + parsing will work
- Content missing here but present in Elements? → dynamic, JS-injected (see `05_static_vs_dynamic_websites.md`)

### 4. Console tab
Useful for testing selectors quickly: `document.querySelectorAll('.product-price')` lets you validate a CSS selector directly in the live page before writing any Python.

## What you're trying to answer by the end of this process

- Is this page static or dynamic?
- Is there a hidden JSON API I can call directly?
- What are the exact selectors/XPath for each field I need?
- Does accessing this data require login, cookies, or specific headers?
- Is there a consistent pattern across similar pages (so one scraper can handle all of them)?

## A practical habit

Save example responses (a sample HTML file, or a sample JSON response) locally while you're analyzing — write and test your parsing logic against that static local copy first. It's faster to iterate against a saved file than to re-request the live site on every test run, and it's kinder to the target server.

---
**Next:** [09 — URL Analysis](09_url_analysis.md)
