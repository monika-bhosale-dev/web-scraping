"""
05 — Redirects & Encoding

Shows how requests handles redirect chains automatically, how to
inspect where you actually ended up (useful for detecting bounces to
a login/CAPTCHA page), and how response encoding affects the text
you get back.

Run: python 05_redirects_and_encoding.py
"""

import requests

BASE_URL = "https://httpbin.org"


def demo_auto_follow_redirect():
    """By default, requests follows redirects and hands you the final response."""
    # /redirect/3 bounces through 3 redirects before landing on /get
    response = requests.get(f"{BASE_URL}/redirect/3")
    print("Final status code:", response.status_code)
    print("Final URL landed on:", response.url)
    print("Number of redirects followed:", len(response.history))
    for i, hop in enumerate(response.history, start=1):
        print(f"  hop {i}: {hop.status_code} -> {hop.headers.get('Location')}")
    print()


def demo_disable_auto_follow():
    """Sometimes you want to inspect the redirect itself instead of following it."""
    response = requests.get(f"{BASE_URL}/redirect/1", allow_redirects=False)
    print("With allow_redirects=False:")
    print("  status:", response.status_code)  # will be 302, not 200
    print("  Location header (where it WOULD have gone):", response.headers.get("Location"))
    print()


def demo_detect_unexpected_redirect():
    """
    A practical scraping pattern: compare the URL you requested to the URL
    you ended up on. A mismatch can mean you got bounced to a login page,
    a CAPTCHA page, or a 'blocked' page instead of real content.
    """
    requested_url = f"{BASE_URL}/redirect-to?url=https://httpbin.org/status/403"
    response = requests.get(requested_url)
    if response.url != requested_url:
        print(f"Redirected! Requested {requested_url}")
        print(f"  ended up at: {response.url} (status {response.status_code})")
        print("  -> in a real scraper, this pattern often means: blocked or login-walled")
    print()


def demo_encoding():
    """Response encoding determines how raw bytes become readable text."""
    response = requests.get(f"{BASE_URL}/encoding/utf8")
    print("Detected encoding:", response.encoding)
    print("First 100 chars of decoded text:")
    print(" ", response.text[:100].replace("\n", " "))


if __name__ == "__main__":
    demo_auto_follow_redirect()
    demo_disable_auto_follow()
    demo_detect_unexpected_redirect()
    demo_encoding()
