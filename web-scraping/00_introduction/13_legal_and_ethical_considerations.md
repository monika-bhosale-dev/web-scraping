# 13 — Legal and Ethical Considerations

This file is informational, not legal advice — laws vary by country and change over time, and specific projects (especially anything commercial or involving personal data) should get a real legal review. But there are well-established practices every scraper should follow regardless.

## robots.txt

Most sites publish a `robots.txt` file (`https://example.com/robots.txt`) declaring which paths automated agents are asked not to access, and sometimes a crawl-delay. It's not legally binding by itself in most jurisdictions, but it's the site's explicitly stated preference — respecting it is the baseline of good-faith scraping, and ignoring it can be used as evidence of bad intent if disputes arise later.

## Terms of Service (ToS)

Many sites' ToS explicitly prohibit automated scraping. Whether ToS violations carry legal weight is genuinely contested and varies by jurisdiction and specific case history — but from a practical/professional standpoint, scraping against explicit ToS carries real risk (account bans, IP bans, cease-and-desist letters, and in some jurisdictions and circumstances, legal action), and that risk should factor into any project decision, especially commercial ones.

## Personal / sensitive data

Scraping personal data (names, emails, health info, etc.) intersects with data protection law — GDPR (EU), CCPA (California), and similar regimes elsewhere. Key practical points:
- Publicly visible ≠ automatically legal to collect, store, and reuse at scale
- Purpose matters — aggregating public business directory data is very different from scraping and reselling individuals' personal details
- Healthcare-adjacent data (relevant given your domain background) often carries extra regulatory weight (HIPAA-adjacent concerns in the US, for example) even when sourced from public pages

## Rate limiting & server load

Even where scraping is entirely permitted, hammering a server with requests can degrade service for real users or rack up their infrastructure costs — this is the "ethical" half of "legal and ethical." Add delays, scale concurrency conservatively, and prefer off-peak hours for large jobs when practical.

## Copyright

Extracted data (text, images) may itself be copyrighted. Storing/republishing scraped content — as opposed to using facts/data extracted from it — raises separate copyright questions independent of scraping-access legality.

## A practical checklist before scraping a new target

- [ ] Checked `robots.txt`
- [ ] Reviewed the site's ToS for explicit scraping restrictions
- [ ] Confirmed whether the data involves personal/sensitive information
- [ ] Rate-limited requests to a reasonable level
- [ ] Considered whether an official API or data license exists as an alternative
- [ ] Clear on the intended use of the data (internal analysis vs. redistribution vs. commercial product — each carries different risk)

## The honest summary

Most scraping of publicly available, non-personal data, done at a reasonable rate, for legitimate purposes, is low-risk and widely practiced. The risk rises sharply with: personal/sensitive data, explicit ToS prohibition + high-value commercial use, aggressive request volume, and bypassing active technical protections. When in doubt on a real project — especially a paid/commercial one — get an actual legal opinion rather than relying on general guidance like this.

---
**Next:** [14 — Learning Roadmap](14_learning_roadmap.md)
