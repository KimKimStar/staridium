import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

test_id = "wsXipzlV6wc"
u = f"https://www.youtube-nocookie.com/embed/{test_id}"
req = urllib.request.Request(u, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://kimkimstar.github.io/'
})

with urllib.request.urlopen(req, timeout=5) as res:
    html = res.read().decode('utf-8', errors='ignore')

# Search for reason or error code in html
matches = re.findall(r'("reason":\s*"[^"]+")', html)
print("Reasons:", matches)

sub_matches = re.findall(r'("subreason":\s*"[^"]+")', html)
print("Subreasons:", sub_matches)

playability = re.findall(r'("status":\s*"[^"]+")', html)
print("Playability status:", playability[:5])

# Search for 153 in html
indices = [m.start() for m in re.finditer(r'153', html)]
for idx in indices:
    print("Found 153 at:", html[max(0, idx-50):min(len(html), idx+50)])
