# 05 — Static vs Dynamic Websites

This is the single most important classification decision in scraping — it determines which tool category you'll need, and getting it wrong is the #1 reason beginners reach for Selenium when `requests` would've done the job in a fraction of the time (or vice versa: fight `requests` for hours against a page that was never going to hand over its data without a browser).

## Static websites

The server sends back a complete HTML page — everything you see in "View Page Source" is everything that's actually there. No JavaScript needs to run for the content to exist.

- **Tools needed:** `requests` (or `httpx`) + BeautifulSoup/lxml — no browser required
- **Speed:** fast — no browser overhead, just HTTP calls
- **Examples:** many blogs, older e-commerce sites, documentation sites, server-rendered content

## Dynamic websites

The server sends a mostly-empty HTML shell, and JavaScript (running in the browser) fetches data afterward and injects it into the page — often via calls to a backend JSON API. "View Page Source" shows little to nothing useful; the real content only exists after the JS executes.

- **Tools needed:** Selenium or Playwright (a real/headless browser that executes JS) — **or**, often better, find and call the underlying JSON API directly with `requests` (see `06_api_scraping/`)
- **Speed:** slower with a browser; fast again if you bypass the browser and hit the API directly
- **Examples:** most modern single-page apps (React/Vue/Angular sites), infinite-scroll feeds, interactive dashboards

## How to tell which one you're dealing with

1. Open the target page in your browser.
2. Right-click → **View Page Source** (not "Inspect" — that shows the live, JS-modified DOM).
3. Search (Ctrl+F) for a piece of text you can see on the rendered page — a product name, a price.
4. **Found it in the raw source?** → Static. `requests` + parsing will work.
5. **Not found?** → Dynamic. The content was injected by JS after load. Check the Network tab (see `08_website_analysis.md`) for a JSON API before reaching for a browser tool — it's usually there and it's usually faster.

## The nuance: hybrid sites

Many real sites are a mix — the initial listing might be server-rendered (static) while "load more" content or interactive filters are JS-driven (dynamic). Test each part of the page you need separately; don't assume the whole site behaves one way.

---
**Next:** [06 — Scraping Approaches](06_scraping_approaches.md)
