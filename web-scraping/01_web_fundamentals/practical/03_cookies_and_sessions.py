"""
03 — Cookies & Sessions

Demonstrates the exact problem a requests.Session() solves: without
one, cookies set by the server on one request are lost by the next.
With one, they persist automatically — the foundation of any scraper
that needs to log in and then hit multiple pages while staying
authenticated.

Run: python 03_cookies_and_sessions.py
"""

import requests

BASE_URL = "https://httpbin.org"


def without_session():
    """Each requests.get() call is independent — no cookie persistence."""
    # /cookies/set sets a cookie and redirects to /cookies, which echoes
    # whatever cookies were sent on THIS request.
    requests.get(f"{BASE_URL}/cookies/set", params={"scraper_id": "abc123"})

    # A fresh, unrelated call — the cookie set above is gone.
    check = requests.get(f"{BASE_URL}/cookies")
    print("Without a session, cookies on next request:", check.json()["cookies"])
    print()


def with_session():
    """A Session object carries cookies forward automatically."""
    session = requests.Session()

    session.get(f"{BASE_URL}/cookies/set", params={"scraper_id": "abc123"})

    # Same session, new request — the cookie set earlier is carried automatically.
    check = session.get(f"{BASE_URL}/cookies")
    print("With a session, cookies on next request:", check.json()["cookies"])
    print()


def session_with_persistent_headers():
    """Sessions can also persist headers across every request, not just cookies."""
    session = requests.Session()
    session.headers.update({"User-Agent": "learning-repo-scraper/1.0"})

    r1 = session.get(f"{BASE_URL}/headers")
    r2 = session.get(f"{BASE_URL}/headers")

    print("Header persisted across two separate calls on the same session:")
    print("  Call 1 UA:", r1.json()["headers"]["User-Agent"])
    print("  Call 2 UA:", r2.json()["headers"]["User-Agent"])
    print()


def simulated_login_flow():
    """The realistic pattern: log in once, reuse the session for protected pages."""
    session = requests.Session()

    # httpbin's /cookies/set simulates "the server just gave us a session cookie"
    # (this is what a real login POST response would trigger via Set-Cookie).
    session.get(f"{BASE_URL}/cookies/set", params={"session_token": "logged_in_demo"})

    protected_page = session.get(f"{BASE_URL}/cookies")
    print("Simulated 'protected page' request, cookie carried from login:")
    print(" ", protected_page.json()["cookies"])


if __name__ == "__main__":
    without_session()
    with_session()
    session_with_persistent_headers()
    simulated_login_flow()
