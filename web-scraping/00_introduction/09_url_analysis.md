# 09 — URL Analysis

URLs carry more information than most beginners realize — understanding their structure often lets you skip a lot of clicking-and-scraping by directly constructing the URLs you need.

## Anatomy of a URL

```
https://example.com/products/category/shoes?page=2&sort=price_asc&color=red#reviews
└─scheme┘└──host───┘└──────path──────────┘└──────query string───────┘└fragment┘
```

- **Scheme** — `http`/`https`
- **Host** — the domain
- **Path** — often encodes structure/hierarchy (`/products/category/shoes`)
- **Query string** — key-value pairs after `?`, separated by `&` — this is where pagination, filters, and sorting usually live
- **Fragment** — after `#`, usually client-side only (not sent to the server, often irrelevant for scraping)

## Why this matters for scraping

### Pagination patterns
Watch how the URL changes as you click "next page" or change a filter:
- `?page=2`, `?page=3` — simple offset-based pagination → easy to loop over in code
- `?offset=20&limit=20` — offset/limit pagination → same idea, different naming
- `?cursor=eyJpZCI6MTIzfQ==` — cursor-based pagination → you generally can't construct these yourself; you must follow the "next" cursor returned by the previous response

### Filters and search
Query parameters often let you skip UI interaction entirely:
- `?category=shoes&color=red&min_price=20` — once you know this pattern, you can construct URLs directly for any filter combination instead of automating clicks through a browser.

### Detail page patterns
Individual item pages often follow a predictable pattern:
- `/product/12345-blue-running-shoes` — the numeric ID is usually the stable, unique part; the slug text is often just for SEO and can sometimes be dropped or ignored.

## Practical exercise

Take any e-commerce or listing site you use regularly:
1. Change the page number in the URL manually and see if the page still loads correctly.
2. Try changing a filter directly in the URL instead of clicking the UI filter.
3. Note whether removing query parameters breaks the page or just resets to a default view.

This kind of URL manipulation is often the fastest way to get structured, predictable access to a full dataset — sometimes faster than any parsing logic at all.

---
**Next:** [10 — Scraping Strategy](10_scraping_strategy.md)
