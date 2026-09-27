# 04 — Web Scraping vs Web Crawling

These two terms get used interchangeably a lot, but they describe different jobs — and in practice, real projects usually need both.

## Web Crawling

Crawling is about **discovery** — systematically following links from page to page to build a map of what exists. A crawler's main question is: *"What pages/URLs are out there?"* Search engines like Google are the canonical example: their crawlers ("spiders") follow billions of links to discover and index pages, largely without caring deeply about the content of any single page beyond indexing it.

## Web Scraping

Scraping is about **extraction** — given a page (or a set of pages you already know about), pulling specific structured data out of it. A scraper's main question is: *"What exact fields do I need from this page?"*

## How they combine in practice

Most real projects do both in sequence:
1. **Crawl** a site's category/listing pages to discover every individual product/article/listing URL.
2. **Scrape** each discovered URL for its detailed fields.

Scrapy is a good example of a tool that blurs this line cleanly — a `CrawlSpider` follows rules to discover pages (crawling) while its parse callbacks extract structured items from each page (scraping) in the same run.

## Quick comparison

| | Crawling | Scraping |
|---|---|---|
| Goal | Discover URLs/structure | Extract specific data |
| Depth | Breadth-first, many pages | Depth on known pages |
| Output | List of URLs / site map | Structured records (JSON/CSV/DB rows) |
| Example | Search engine indexing | Pulling price + rating from a product page |

## Why the distinction matters for you

When someone asks you to "scrape a site," clarify which part of the job that actually is. If there's no existing list of target URLs, you need a crawling phase first (discover listing pages → discover item URLs) before any extraction logic even runs. Conflating the two early is a common source of underestimating project scope.

---
**Next:** [05 — Static vs Dynamic Websites](05_static_vs_dynamic_websites.md)
