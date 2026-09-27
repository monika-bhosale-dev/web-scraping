# 01 — Web Fundamentals

Before any scraping library matters, the underlying protocol does. Every `requests.get()`, every Selenium page load, every Scrapy request is HTTP underneath — this module covers the HTTP layer itself: methods, headers, cookies, sessions, status codes, and how URLs and redirects behave. ~30% theory, 70% practical — enough theory to know what's happening on the wire, then scripts that prove it against a real test API.

## Contents

### Theory
1. [Client-Server Model & HTTP Basics](theory/01_client_server_and_http_basics.md)
2. [Headers, Cookies & Sessions](theory/02_headers_cookies_sessions.md)
3. [URLs, Status Codes & Redirects](theory/03_urls_status_codes_redirects.md)

### Practical
1. [GET, POST, PUT, PATCH, DELETE](practical/01_get_post_put_patch_delete.py)
2. [Headers & User-Agent](practical/02_headers_and_user_agent.py)
3. [Cookies & Sessions](practical/03_cookies_and_sessions.py)
4. [Status Code Handling](practical/04_status_code_handling.py)
5. [Redirects & Encoding](practical/05_redirects_and_encoding.py)

## What ties it together
All five practical scripts hit [httpbin.org](https://httpbin.org) — a free public API built specifically for testing HTTP clients, echoing back exactly what you sent. It's the safest place to learn this layer without worrying about rate limits, blocking, or ethics questions.

## Learning log note
See the root [`LEARNING_LOG.md`](../LEARNING_LOG.md) for the dated entry on what actually tripped me up in this module.
