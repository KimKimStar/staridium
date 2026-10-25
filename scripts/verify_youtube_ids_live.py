import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Test IDs from SEARCH_DOMAIN_DATABASE
test_ids = [
    # golf
    "F0sCTlc5Ubo", "tHES7NyxA-I", "G4yOoVsDn6g", "JRJtg4-sDYQ", "PWqpBvfLgpQ", "AGaJ2eWsoiI", "whWLBNJ7U7s", "YenRrrKyVew",
    # soccer
    "uK7K7qD4iLw", "3eN9i4gW2kI", "bL0i9kE7w2Y", "8hK3nL9vW1e",
    # camping
    "nE4kO9pL2vY", "9iL2bW8eN4k", "vW3nK8oL2bE", "2eB7nL3wO9k",
    # music
    "IYrsSmYHmnM", "AgZzx8GTsDg", "pSUydWEqKwE", "ArmDp-zijuc", "YwPxl1M09l4", "XkS80VOHsQY", "9bZkp7q19f0", "gdZLi9oWNZg"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for vid in test_ids:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=3) as res:
            data = json.loads(res.read().decode('utf-8'))
            print(f"[VALID] {vid}: {data.get('title')} ({data.get('author_name')})")
    except Exception as e:
        print(f"[INVALID/FAIL] {vid}: {e}")
