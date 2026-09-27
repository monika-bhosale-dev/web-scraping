"""
04 — Status Code Handling

A scraper that doesn't check status codes will happily try to parse
a 403/404/500 error page as if it were real data, and either crash
confusingly or silently store garbage. This script builds a small
reusable pattern for handling the status codes that actually matter.

Run: python 04_status_code_handling.py
"""

import requests

BASE_URL = "https://httpbin.org"


def fetch_and_classify(url, **kwargs):
    """
    A minimal 'safe fetch' pattern: classify the response instead of
    assuming success. Returns (ok: bool, response_or_none, reason: str).
    """
    try:
        response = requests.get(url, timeout=10, **kwargs)
    except requests.exceptions.RequestException as exc:
        return False, None, f"network error: {exc}"

    status = response.status_code

    if status == 200:
        return True, response, "success"
    elif status == 404:
        return False, response, "not found — bad URL or removed page"
    elif status == 403:
        return False, response, "forbidden — likely blocked/detected as a bot"
    elif status == 429:
        retry_after = response.headers.get("Retry-After", "unspecified")
        return False, response, f"rate limited — retry after: {retry_after}"
    elif 500 <= status < 600:
        return False, response, f"server error ({status}) — likely transient, worth retrying"
    else:
        return False, response, f"unhandled status code: {status}"


def demo_each_status():
    test_cases = [
        (f"{BASE_URL}/status/200", "expected success"),
        (f"{BASE_URL}/status/404", "expected not found"),
        (f"{BASE_URL}/status/403", "expected forbidden"),
        (f"{BASE_URL}/status/429", "expected rate limited"),
        (f"{BASE_URL}/status/500", "expected server error"),
    ]

    for url, label in test_cases:
        ok, response, reason = fetch_and_classify(url)
        status = response.status_code if response is not None else "N/A"
        print(f"[{label}] status={status} ok={ok} -> {reason}")


if __name__ == "__main__":
    demo_each_status()
