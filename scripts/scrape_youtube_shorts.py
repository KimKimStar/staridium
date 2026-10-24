import urllib.request
import urllib.parse
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Search YouTube without an API key by fetching YouTube search results HTML
query = "다이어트 쇼츠"
url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
})

try:
    with urllib.request.urlopen(req, timeout=10) as res:
        html = res.read().decode('utf-8', errors='ignore')
        # Look for ytInitialData
        m = re.search(r'var ytInitialData = ({.*?});</script>', html)
        if m:
            data = json.loads(m.group(1))
            print("ytInitialData extracted successfully!")
            
            # Extract video IDs, titles, thumbnails, channels
            text_data = json.dumps(data)
            video_ids = list(dict.fromkeys(re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', text_data)))
            print(f"Found {len(video_ids)} real video IDs!")
            print("Sample IDs:", video_ids[:10])
        else:
            print("ytInitialData not found via regex")
except Exception as e:
    print("Error:", e)
