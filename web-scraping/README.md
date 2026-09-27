# Web Scraping — My Learning Story

## Where I started

I've spent 4+ years working as a Python developer — Web Scraping, Web Automation, Data Extraction, API Integration, and Data Processing across e-commerce, aviation, B2B, and healthcare domains. Requests, BeautifulSoup, lxml, XPath, Selenium, Playwright, Scrapy, REST APIs, SQL, PostgreSQL, MongoDB — I've used all of it in production.

This repo isn't me learning scraping from zero. It's me going back and **formalizing** years of picked-up-on-the-job knowledge into something structured — filling gaps I never had time to fill, writing down the "why" behind habits I built through trial and error, and building a reference I (and hopefully others) can actually follow start to finish. I'm also using it to push further into advanced automation, software testing, and SDET practices — the parts of this space I want to go deeper on next.

## The arc

```
Foundations  →  Static Scraping  →  Dynamic/Browser Automation  →  Scale  →  APIs  →  Storage  →  Testing Crossover  →  Capstones
```

Each phase is a real folder, each folder is ~20% theory / 80% code — I'm not interested in writing essays, I want working scripts and projects I can point to.

## Progress

- [x] `00_introduction` — fundamentals, workflow, legal/ethical grounding
- [ ] `01_web_fundamentals` — HTTP, headers, cookies, sessions
- [ ] `02_html_dom` — HTML structure, DOM relationships
- [ ] `03_url_website_analysis` — URL patterns, DevTools, network analysis
- [ ] `04_requests`
- [ ] `05_beautifulsoup`
- [ ] `06_lxml_xpath`
- [ ] `07_css_selectors`
- [ ] `08_data_extraction`
- [ ] `09_pagination`
- [ ] `10_scraping_patterns`
- [ ] `11_api_scraping`
- [ ] `12_selenium`
- [ ] `13_playwright`
- [ ] `14_scrapy`
- [ ] `15_data_cleaning`
- [ ] `16_data_validation`
- [ ] `17_output_formats`
- [ ] `18_database`
- [ ] `19_operational_challenges`
- [ ] `20_logging_error_handling`
- [ ] `21_automation`
- [ ] `22_performance`
- [ ] `23_advanced_scraping`
- [ ] `25_real_world_projects`
- [ ] `26_advanced_projects`

*(Updated as each module gets built — this list is the honest state of the repo, not a promise.)*

## The actual diary

The commit history and [`LEARNING_LOG.md`](LEARNING_LOG.md) are where the real story lives — what was easy, what wasn't, what I got wrong the first time. The folders are the destination; the log is the route.

## Setup

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## What's next

Working through `01_web_fundamentals`, then straight into HTML/DOM and URL analysis before touching any scraping library — I want the foundations solid before the tools.
