# 02 — Headers, Cookies & Sessions

These three concepts are where most beginner scrapers get blocked or return wrong/empty data — not because the parsing logic is wrong, but because the request itself didn't look enough like a real browser's.

## Headers

Headers are metadata attached to every request and response — key-value pairs describing the request/response itself, not the actual content.

**Common request headers you'll set as a scraper:**
- `User-Agent` — identifies the client (browser/OS/device). Missing or default library UAs (`python-requests/2.31.0`) are one of the easiest ways to get flagged as a bot — see below.
- `Accept` — what content types the client can handle (`text/html`, `application/json`, etc.)
- `Referer` — the URL the request claims to have come from; some sites check this to block direct/non-browser access
- `Authorization` — carries auth tokens/API keys (`Bearer <token>`)
- `Cookie` — sends stored cookies back to the server (see below)

**Common response headers you'll read:**
- `Content-Type` — tells you whether the body is HTML, JSON, an image, etc.
- `Set-Cookie` — the server asking the client to store a cookie
- `Retry-After` — on rate-limited (429) responses, how long to wait before retrying

## User-Agent, specifically

The `User-Agent` header is worth calling out on its own because it's the single most common reason a scraper gets treated differently than a browser. A real Chrome browser sends something like:
```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
```
`requests`' default is `python-requests/2.31.0` — trivially identifiable, and many sites filter on it. Setting a realistic UA (and keeping it consistent across a session) is often step one of not getting blocked, well before proxies or anything more advanced.

## Cookies

Cookies are small pieces of data the server asks the client to store (via `Set-Cookie`) and send back on every subsequent request (via the `Cookie` header). HTTP itself is stateless — cookies are the mechanism that creates continuity across requests: staying logged in, remembering cart contents, tracking a session ID.

For scraping, cookies matter whenever:
- You need to log in and stay logged in across multiple requests
- A site sets an anti-bot/session cookie on first visit that subsequent requests are expected to carry
- You're maintaining cart/filter state across a multi-step flow

## Sessions

A "session," in the scraping-library sense (`requests.Session()`), is an object that automatically persists cookies (and can persist headers) across multiple requests — so you don't have to manually track and re-attach cookies yourself on every call. Under the hood it's just: make a request, capture any `Set-Cookie` headers, automatically attach them to the `Cookie` header on the next request to the same domain.

This is the difference between:
```python
# Without a session — cookies from the login response are lost
requests.post(login_url, data=creds)
requests.get(protected_url)   # not logged in — no cookie was carried over

# With a session — cookies persist automatically
s = requests.Session()
s.post(login_url, data=creds)
s.get(protected_url)          # logged in — session cookie carried automatically
```

Almost any scraper that involves logging in, or that hits more than one page on the same site, should use a session rather than bare `requests.get()`/`requests.post()` calls.

---
**Next:** [03 — URLs, Status Codes & Redirects](03_urls_status_codes_redirects.md)
