"""
01 — GET, POST, PUT, PATCH, DELETE

Demonstrates every core HTTP method against httpbin.org, a free public
test API that echoes back exactly what you sent — the safest place to
see the request/response cycle without touching a real target site.

Run: python 01_get_post_put_patch_delete.py
"""

import requests

BASE_URL = "https://httpbin.org"


def demo_get():
    """GET — the method you'll use for ~90% of actual scraping."""
    response = requests.get(f"{BASE_URL}/get", params={"category": "shoes", "page": 2})
    print("GET status:", response.status_code)
    print("GET final URL (params appended):", response.url)
    print("GET response JSON args:", response.json()["args"])
    print()


def demo_post():
    """POST — submitting data: logins, search forms, API payloads."""
    payload = {"username": "demo_user", "password": "demo_pass"}
    response = requests.post(f"{BASE_URL}/post", data=payload)
    print("POST status:", response.status_code)
    print("POST echoed form data:", response.json()["form"])
    print()


def demo_post_json():
    """POST with a JSON body — common when calling internal/REST APIs directly."""
    payload = {"query": "web scraping", "limit": 10}
    response = requests.post(f"{BASE_URL}/post", json=payload)
    print("POST (json) status:", response.status_code)
    print("POST (json) echoed body:", response.json()["json"])
    print()


def demo_put():
    """PUT — replace a resource entirely. Rare in scraping, common when building APIs."""
    response = requests.put(f"{BASE_URL}/put", json={"id": 1, "name": "updated-resource"})
    print("PUT status:", response.status_code)
    print()


def demo_patch():
    """PATCH — partially update a resource. Rare in scraping."""
    response = requests.patch(f"{BASE_URL}/patch", json={"name": "partially-updated"})
    print("PATCH status:", response.status_code)
    print()


def demo_delete():
    """DELETE — remove a resource. Essentially never used in scraping."""
    response = requests.delete(f"{BASE_URL}/delete")
    print("DELETE status:", response.status_code)
    print()


if __name__ == "__main__":
    demo_get()
    demo_post()
    demo_post_json()
    demo_put()
    demo_patch()
    demo_delete()
