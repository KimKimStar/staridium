import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Test fetching embed page of a video from youtube-nocookie and youtube
test_id = "wsXipzlV6wc" # 삐약스핏 다이어트
urls = [
    f"https://www.youtube-nocookie.com/embed/{test_id}",
    f"https://www.youtube-nocookie.com/embed/{test_id}?autoplay=1&mute=1&playsinline=1&rel=0",
    f"https://www.youtube-nocookie.com/embed/{test_id}?autoplay=1&mute=1&playsinline=1&rel=0&loop=1&playlist={test_id}",
    f"https://www.youtube.com/embed/{test_id}?autoplay=1&mute=1&playsinline=1&rel=0"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://kimkimstar.github.io/'
        })
        with urllib.request.urlopen(req, timeout=5) as res:
            content = res.read().decode('utf-8', errors='ignore')
            has_error = "153" in content or "error-screen" in content or "UNPLAYABLE" in content
            print(f"URL: {u[:60]}... -> Status: {res.status}, Error in html: {has_error}")
    except Exception as e:
        print(f"URL: {u[:60]}... -> Failed: {e}")
