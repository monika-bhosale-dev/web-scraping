# 07 — Scraping Tools Overview

A quick reference map of the tools this repo covers, what each one actually does, and where it fits in the approaches from `06_scraping_approaches.md`.

## HTTP clients

| Tool | What it does | Notes |
|---|---|---|
| `requests` | Sends HTTP requests, returns raw response | The standard, simplest choice |
| `httpx` | Modern alternative to `requests` | Supports async natively, HTTP/2 |
| `aiohttp` | Async HTTP client/server | Used for high-concurrency scraping |

## HTML parsers

| Tool | What it does | Notes |
|---|---|---|
| BeautifulSoup (`bs4`) | Parses HTML, lets you search by tag/class/CSS selector | Beginner-friendly, very forgiving of broken HTML |
| `lxml` | Fast C-based HTML/XML parser | Faster than bs4; supports XPath natively |
| `cssselect` | CSS selector support for lxml | Bridges CSS selectors → XPath under the hood |

## Browser automation

| Tool | What it does | Notes |
|---|---|---|
| Selenium | Drives real browsers via WebDriver protocol | Mature, huge ecosystem, also the standard for test automation (SDET overlap) |
| Playwright | Modern browser automation by Microsoft | Faster, built-in auto-waiting, native network interception |
| `undetected-chromedriver` | Selenium variant that evades common bot detection | Used when standard Selenium gets blocked |

## Crawling frameworks

| Tool | What it does | Notes |
|---|---|---|
| Scrapy | Full crawling framework: spiders, items, pipelines, middleware | Best for large, production-scale crawls |
| `scrapy-playwright` | Plugs Playwright's browser rendering into Scrapy | For the JS-heavy pages inside a larger Scrapy crawl |

## Data storage

| Tool | What it does | Notes |
|---|---|---|
| PostgreSQL (`psycopg2`/SQLAlchemy) | Relational database | Best when your data has a consistent schema |
| MongoDB (`pymongo`) | Document database | Best when your data's shape varies across sources/pages |

## Supporting utilities

| Tool | What it does | Notes |
|---|---|---|
| `tenacity` | Retry logic with backoff | Wraps flaky network calls |
| `fake-useragent` | Generates realistic User-Agent strings | Used for header rotation |
| `loguru` | Simplified structured logging | Easier than stdlib `logging` for scraper logs |
| `python-dotenv` | Loads config/secrets from `.env` files | Keeps API keys/credentials out of code |

## How this maps to the repo folders

- `01_requests/` → `requests`, `httpx`, `aiohttp`, `tenacity`
- `02_parsing_bs4_lxml_xpath/` → `beautifulsoup4`, `lxml`, `cssselect`
- `03_selenium/` → `selenium`, `webdriver-manager`, `undetected-chromedriver`
- `04_playwright/` → `playwright`, `playwright-stealth`
- `05_scrapy/` → `scrapy`, `scrapy-playwright`, `scrapy-rotating-proxies`
- `07_storage_sql_mongo/` → `sqlalchemy`, `psycopg2-binary`, `pymongo`
- `08_testing_sdet_crossover/` → `pytest`, `pytest-html`

---
**Next:** [08 — Website Analysis](08_website_analysis.md)
