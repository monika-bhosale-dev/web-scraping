"""
02 — Headers & User-Agent

Shows the default (dead giveaway) User-Agent requests sends, how to
replace it with a realistic browser UA, and how to inspect response
headers. httpbin.org's /headers endpoint echoes back every header
the server received — useful for confirming what a target site
actually sees from you.

Run: python 02_headers_and_user_agent.py
"""

import requests

BASE_URL = "https://httpbin.org"

REALISTIC_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def show_default_user_agent():
    """The default UA requests sends — trivially identifiable as a script."""
    response = requests.get(f"{BASE_URL}/headers")
    ua = response.json()["headers"]["User-Agent"]
    print("Default User-Agent (this is what gives scrapers away):")
    print(" ", ua)
    print()


def show_spoofed_headers():
    """Same request, with a realistic browser header set attached."""
    response = requests.get(f"{BASE_URL}/headers", headers=REALISTIC_HEADERS)
    received = response.json()["headers"]
    print("Headers the server actually received, with spoofing:")
    for key, value in received.items():
        print(f"  {key}: {value}")
    print()


def inspect_response_headers():
    """Response headers matter too — Content-Type tells you how to parse the body."""
    response = requests.get(f"{BASE_URL}/json")
    print("Response Content-Type:", response.headers.get("Content-Type"))
    print("Response Server header:", response.headers.get("Server"))
    print()


if __name__ == "__main__":
    show_default_user_agent()
    show_spoofed_headers()
    inspect_response_headers()
