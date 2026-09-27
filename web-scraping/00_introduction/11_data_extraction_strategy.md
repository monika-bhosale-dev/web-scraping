# 11 — Data Extraction Strategy

Fetching the page is only half the job — extraction strategy is about reliably pulling clean, correct, structured fields out of messy real-world content, and keeping that extraction working as sites change.

## Choosing selectors that don't break easily

- **Prefer semantic attributes over generated classes.** A class like `data-testid="product-price"` or an `id` is far more stable than an auto-generated CSS class like `.css-1x2y3z` that build tools regenerate on every deploy.
- **Anchor on structure, not just position.** `//div[@class="price"]` is more robust than `//div[3]/span[2]`, which breaks the moment the layout shifts slightly.
- **Use `contains()` for partial/dynamic class names:** `//div[contains(@class, "product-card")]` survives sites that append extra classes dynamically (e.g., `product-card featured`).

## Defining your data schema upfront

Before extraction, define exactly what "done" looks like for one record:

```python
{
    "title": str,
    "price": float,
    "currency": str,
    "rating": float,       # nullable
    "in_stock": bool,
    "url": str,
    "scraped_at": datetime
}
```

Extraction code should aim to always produce this shape — with explicit `None`/defaults for missing fields — rather than silently dropping keys when something isn't found. Silent gaps are the hardest scraping bugs to catch later.

## Cleaning as part of extraction, not an afterthought

Raw extracted text is almost never ready to use directly:
- `"  $24.99  "` → strip whitespace, remove currency symbol, cast to `float`
- `"4.5 out of 5 stars"` → regex/split to pull out `4.5`
- `"In Stock (12 left)"` → parse into `in_stock: True, quantity: 12`
- Dates in inconsistent formats → normalize to ISO 8601 immediately, not later in analysis

## Validation before storage

Add lightweight checks right after extraction, before writing to storage:
- Required fields aren't `None`/empty
- Numeric fields are actually numeric after cleaning
- URLs are well-formed
- No duplicate unique keys (e.g., product ID) within the same run

This is the same mindset covered more formally in `08_testing_sdet_crossover/` — treating extracted data like something you test, not just something you trust.

## When extraction breaks

Sites change their HTML periodically. Build for it:
- Log a warning (not a silent `None`) when an expected selector returns nothing
- Keep selectors in one place (constants/config) so updates are a one-line fix, not a hunt through the codebase
- Consider a small daily "canary" check on a known page to catch breakage early

---
**Next:** [12 — Scraping Challenges](12_scraping_challenges.md)
