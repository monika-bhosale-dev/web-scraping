# 01 — Client-Server Model & HTTP Basics

## The client-server model

Every web interaction — a browser loading a page, a scraper hitting a URL — follows the same pattern:

```
CLIENT (your script / browser)  --request-->  SERVER (the website)
CLIENT                          <--response--  SERVER
```

The client initiates; the server responds. When you write `requests.get("https://example.com")`, your script *is* the client — no different in principle from a browser, just without a rendering engine attached (that distinction is exactly why `05_static_vs_dynamic_websites.md` in `00_introduction` matters).

## HTTP: the protocol underneath everything

HTTP (HyperText Transfer Protocol) is the agreed-upon format both sides use to talk. Every request and every response has the same basic shape:

**A request has:**
- A **method** (GET, POST, etc. — see below)
- A **path** (`/products/shoes`)
- **Headers** (metadata — see `02_headers_cookies_sessions.md`)
- Optionally, a **body** (data being sent, e.g. form fields or JSON)

**A response has:**
- A **status code** (200, 404, 500 — see `03_urls_status_codes_redirects.md`)
- **Headers**
- A **body** (the actual HTML/JSON/file content)

## HTTPS

HTTPS is HTTP wrapped in TLS encryption — the connection between client and server is encrypted so a third party on the network can't read or tamper with the traffic. For scraping purposes, it behaves identically to HTTP; `requests` and every other tool handle the encryption transparently. The only practical scraping-relevant wrinkle is certificate verification, which occasionally needs handling on sites with misconfigured or self-signed certs (`requests.get(url, verify=False)` — use sparingly and only when you understand why verification is failing).

## HTTP methods

| Method | Purpose | Typical scraping use |
|---|---|---|
| `GET` | Retrieve a resource | The vast majority of scraping — fetching pages/data |
| `POST` | Submit data (create something, or trigger an action) | Logging in, submitting search forms, calling APIs that require a payload |
| `PUT` | Replace a resource entirely | Rare in scraping — mostly relevant if you're *building* an API, not consuming one |
| `PATCH` | Partially update a resource | Same — rare in scraping, common in API development |
| `DELETE` | Remove a resource | Essentially never used in scraping |

For scraping specifically, you'll live in `GET` and `POST` almost exclusively — `GET` for fetching pages and calling read-only APIs, `POST` for logins, form submissions, and any API that requires sending a payload (search filters, GraphQL queries, etc.).

## Why this matters before touching a scraping library

Every scraping tool you'll use later — `requests`, Selenium's underlying network calls, Scrapy's `Request` objects — is just a structured way of constructing and sending exactly these things: a method, a path, headers, and sometimes a body. Understanding the raw protocol means every library's API afterward reads as "a convenient wrapper around this," not as separate magic to memorize per tool.

---
**Next:** [02 — Headers, Cookies & Sessions](02_headers_cookies_sessions.md)
