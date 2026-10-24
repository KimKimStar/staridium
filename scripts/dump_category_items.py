import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/scripts/apply_authentic_thumbnails.py', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'(\w+):\s*\[(.*?)\]', text, re.DOTALL)
for cat, content in matches:
    thumbs = re.findall(r'thumbnail:\s*"([^"]+)"', content)
    titles = re.findall(r'title:\s*"([^"]+)"', content)
    print(f"=== {cat} ({len(thumbs)} items) ===")
    for i in range(len(thumbs)):
        print(f"  {i+1}: {titles[i][:30]} -> {thumbs[i]}")
