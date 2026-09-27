# 01 — What is Web Scraping

Web scraping is the automated process of visiting a web page, pulling out specific pieces of information from it, and saving that information somewhere useful — a CSV file, a database, a spreadsheet, another system entirely.

Think about what you do manually when you research something online: you open a page, scan for the price, the title, the rating, maybe the seller name, and copy it into a note. Web scraping is that same action, done by code, at a speed and scale no human could match — thousands or millions of pages, on a schedule, without fatigue or typos.

## How it works, at a high level

1. **Request** — your script asks a server for a page, the same way a browser does when you type a URL and hit enter.
2. **Response** — the server sends back the page's content, usually as HTML (sometimes JSON, if you're hitting an API directly).
3. **Parse** — your script reads through that HTML/JSON and picks out the specific fields you care about (price, name, date, etc.) using selectors or patterns.
4. **Store** — the extracted data gets saved — to a file, a database, or passed into another process.

That's the entire loop. Everything you'll learn in this repo — Selenium, Playwright, Scrapy, XPath, proxies — exists to make one or more of those four steps work reliably against real, messy, defensive websites.

## What scraping is *not*

- It's not hacking. You're reading publicly rendered content, not breaking into systems or bypassing authentication you don't have rights to.
- It's not always about HTML. A huge amount of "scraping" today is really just calling the same internal APIs a website's own JavaScript calls — which is often faster and more reliable than parsing HTML at all (covered in `06_api_scraping/`).
- It's not one-size-fits-all. A static blog and a JavaScript-heavy dashboard require completely different tools, which is why this repo is organized by method rather than treating "scraping" as a single skill.

## A simple example

A request to a page, and pulling the page's `<title>` out of the response, is the smallest possible scraper:

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)
```

Everything from here builds outward from this same shape: request → parse → extract → store.

---
**Next:** [02 — Why Web Scraping](02_why_web_scraping.md)
