import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/scripts/scrape_youtube_shorts.py', 'r', encoding='utf-8') as f:
    pass

import urllib.request
import urllib.parse
query = "다이어트 쇼츠"
url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
})
with urllib.request.urlopen(req, timeout=10) as res:
    html = res.read().decode('utf-8', errors='ignore')

# Search for /shorts/ or videoId in html
shorts_ids = re.findall(r'/shorts/([a-zA-Z0-9_-]{11})', html)
print("Shorts IDs from href:", len(shorts_ids), list(dict.fromkeys(shorts_ids))[:10])

video_ids = re.findall(r'"videoId":\s*"([a-zA-Z0-9_-]{11})"', html)
print("Video IDs from json in html:", len(video_ids), list(dict.fromkeys(video_ids))[:10])
