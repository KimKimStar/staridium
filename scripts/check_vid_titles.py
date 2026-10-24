import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

test_ids = [
    ("F0sCTlc5Ubo", "유튜브 인기급상승 동영상"),
    ("AgZzx8GTsDg", "엄지원 직캠"),
    ("IYrsSmYHmnM", "newjeans"),
    ("wsXipzlV6wc", "삐약스핏"),
    ("BEDwfDQai3A", "오프빈"),
    ("pcWmS1qANPU", "머니치트키"),
    ("wKJcJOBA0XA", "계란 레시피")
]

for vid, label in test_ids:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as res:
            data = json.loads(res.read().decode('utf-8'))
            print(f"[{vid}] ({label}): Title in YouTube: '{data.get('title')}' by '{data.get('author_name')}'")
    except Exception as e:
        print(f"[{vid}] ({label}): Error: {e}")
