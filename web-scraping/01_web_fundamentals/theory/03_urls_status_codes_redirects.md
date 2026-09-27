# 03 — URLs, Status Codes & Redirects

## URL structure recap

Already covered in depth in `00_introduction/09_url_analysis.md` — quick recap for this module's context:
```
https://example.com/products?category=shoes&page=2
└scheme┘└──host───┘└──path──┘└─────query string─────┘
```
Query parameters (`?key=value&key2=value2`) are how most filtering, sorting, and pagination gets expressed — and how you'll construct URLs directly in scrapers rather than always simulating clicks.

## HTTP status codes

The status code is the single most important piece of information in a response for a scraper — it tells you, before you even look at the body, whether the request actually worked.

### 2xx — Success
- `200 OK` — standard success, body contains the expected content
- `201 Created` — resource created (relevant mostly for POST to APIs)
- `204 No Content` — success, but no body returned

### 3xx — Redirection
- `301 Moved Permanently` / `302 Found` — the resource has moved; see redirects below
- `304 Not Modified` — used with caching; content hasn't changed since last fetch

### 4xx — Client error (you did something wrong, or you're being blocked)
- `400 Bad Request` — malformed request
- `401 Unauthorized` — missing/invalid authentication
- `403 Forbidden` — authenticated or not, you don't have access — **very commonly the signal a scraper has been detected/blocked**, even when the request "looks" correct
- `404 Not Found` — the URL doesn't exist
- `429 Too Many Requests` — rate limited — back off, check for a `Retry-After` header

### 5xx — Server error (not your fault, usually)
- `500 Internal Server Error` — something broke server-side
- `502`/`503`/`504` — gateway/service unavailable/timeout — often transient, worth retrying with backoff

### Why this matters for scraper reliability
A scraper that only checks "did I get a body back" and blindly parses it will silently fail on a `403` or `429` page (which often still returns HTML — just an error/block page, not your data) and either crash on missing selectors or, worse, quietly store garbage. Always check `response.status_code` before parsing.

## Redirects

A redirect (`301`/`302`) tells the client "the resource you asked for is actually somewhere else — go there instead." Browsers (and `requests`, by default) follow redirects automatically and hand you the *final* destination's response.

Things worth knowing as a scraper:
- `requests` follows redirects by default; `response.url` after the call tells you where you actually ended up (useful for detecting bounces to a login page or a block/CAPTCHA page in disguise)
- `response.history` gives you the chain of redirects that occurred
- You can disable auto-following with `allow_redirects=False` if you need to inspect the redirect itself (e.g., debugging why a URL isn't resolving where expected)

## Content-Type & encoding

The `Content-Type` response header tells you how to interpret the body: `text/html`, `application/json`, `image/png`, etc. — check this before assuming a response is HTML you can parse. Encoding (usually UTF-8, occasionally not) determines how raw bytes become readable text; `requests` generally detects this automatically via `response.encoding`, but it's worth knowing it exists for the rare case a page renders as garbled text (mojibake) and you need to override it manually.

---
**Back to:** [01_web_fundamentals README](../README.md)
