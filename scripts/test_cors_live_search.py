import urllib.request
import urllib.parse
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

query = "골프 스윙"
yt_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query + ' 쇼츠')}"
cors_url = f"https://api.allorigins.win/raw?url={urllib.parse.quote(yt_url)}"

print("Testing CORS proxy live search...")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    req = urllib.request.Request(cors_url, headers=headers)
    with urllib.request.urlopen(req, timeout=8) as res:
        content = res.read().decode('utf-8', errors='ignore')
        print(f"Content length: {len(content)}")
        vids = list(dict.fromkeys(re.findall(r'"videoId":\s*"([a-zA-Z0-9_-]{11})"', content)))
        print(f"Found {len(vids)} video IDs via allorigins proxy!")
        if vids:
            print("Sample IDs:", vids[:5])
except Exception as e:
    print("Allorigins error:", e)

# Test corsproxy.io
cors_url2 = f"https://corsproxy.io/?{urllib.parse.quote(yt_url)}"
try:
    req2 = urllib.request.Request(cors_url2, headers=headers)
    with urllib.request.urlopen(req2, timeout=8) as res:
        content2 = res.read().decode('utf-8', errors='ignore')
        print(f"Corsproxy.io Content length: {len(content2)}")
        vids2 = list(dict.fromkeys(re.findall(r'"videoId":\s*"([a-zA-Z0-9_-]{11})"', content2)))
        print(f"Found {len(vids2)} video IDs via corsproxy.io!")
        if vids2:
            print("Sample IDs:", vids2[:5])
except Exception as e:
    print("Corsproxy.io error:", e)
