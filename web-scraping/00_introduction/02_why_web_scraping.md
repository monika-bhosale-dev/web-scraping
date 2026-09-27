# 02 — Why Web Scraping

Data drives decisions, and a huge share of the world's useful data has no clean API, no downloadable dataset, no partnership agreement — it just sits rendered on a web page. Scraping is how that data becomes usable.

## Common real-world use cases

**E-commerce**
- Price monitoring and competitor tracking
- Product catalog aggregation across marketplaces
- Stock/availability alerts
- Review and rating sentiment collection

**Aviation**
- Flight status and delay tracking across airlines
- Fare monitoring across booking sites
- Airport/route data aggregation for analytics

**B2B**
- Lead generation (company directories, contact info, firmographic data)
- Market research and competitor intelligence
- Job posting aggregation for hiring trend analysis

**Healthcare**
- Public clinical trial data aggregation
- Drug pricing and availability tracking
- Provider directory and credential verification data

**Beyond industry-specific cases**
- News and content aggregation
- Real estate listing aggregation
- Academic/research data collection
- Feeding machine learning pipelines with training data
- Powering internal dashboards that no vendor API supports

## Why not "just use an API"?

Sometimes you can — and when you can, you should (see `06_api_scraping/`). But most websites simply don't expose a public API for the data they show you, or the API is heavily rate-limited, paywalled, or missing fields the front-end has. Scraping fills that gap: if a browser can render it, it can, with the right approach, be extracted.

## Why this matters for your own growth

Scraping sits at the intersection of several valuable, transferable skills: HTTP and web internals, HTML/DOM structure, automation, data cleaning, and increasingly — testing and QA (browser automation tools like Selenium/Playwright are the same tools used in SDET roles). Getting genuinely good at scraping builds a foundation that pays off in automation, QA, and data engineering work alike.

---
**Next:** [03 — Web Scraping Workflow](03_web_scraping_workflow.md)
