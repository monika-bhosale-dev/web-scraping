# Learning Log

Dated, honest entries as I work through this repo — what I built, what was easy, what wasn't, what clicked late. This file is the real story; the folders are just where the output lands.

---

## 2026-09-27 — Repo structure finalized

Spent today less on scraping itself and more on organizing *how* I want to learn it. Went through a few iterations of the folder structure — started broad, realized I had duplicate "choose your tool" theory scattered across three different folders (introduction, url analysis, and a dedicated strategy folder), and merged them down to one source of truth. Also converted a lot of pure-theory files (CSS selector types, HTML basics) into paired theory+practical folders — if I can't write a script proving I understand a concept, I probably don't understand it yet.

Landed on a 20% theory / 80% practical target for every module. Easy to say, will be the real test once I'm actually deep in Selenium waits and Scrapy pipelines.

## 2026-09-27 — 00_introduction written

Wrote all 14 files for the introduction module: what scraping is, why it matters, the full workflow, scraping vs. crawling, static vs. dynamic sites, the four scraping approaches, a tools overview, website/URL analysis, strategy, extraction strategy, challenges, and legal/ethical considerations.

Nothing here was new information given my background, but writing it down surfaced a few things I'd never articulated cleanly before — especially the scraping-vs-crawling distinction, and the fact that I've been defaulting to browser automation on some past projects when a hidden JSON API would've been faster. That's going straight into how I approach `03_url_website_analysis` — check the Network tab *before* reaching for Selenium, every time.

---

*Next entry: starting `01_web_fundamentals` — HTTP methods, headers, cookies, sessions.*
