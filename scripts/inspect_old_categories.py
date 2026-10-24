import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/scripts/apply_authentic_thumbnails.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the categories and their thumbnails in apply_authentic_thumbnails.py
matches = re.findall(r'(\w+):\s*\[(.*?)\]', text, re.DOTALL)
print(f"Categories found in apply_authentic_thumbnails.py: {len(matches)}")
for k, content in matches:
    thumbs = re.findall(r'thumbnail:\s*"([^"]+)"', content)
    titles = re.findall(r'title:\s*"([^"]+)"', content)
    print(f"{k:12}: {len(thumbs)} thumbnails, {len(titles)} titles")
