import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'var TOPIC_SPECIFIC_ITEMS = \{(.*?)\};\s*var VERIFIED_YT_IDS', html, re.DOTALL)
if m:
    topic_text = m.group(1)
    keys = re.findall(r'(\w+):\s*\[', topic_text)
    print("Found keys in TOPIC_SPECIFIC_ITEMS:", keys)
    for k in keys:
        # count items in each key
        km = re.search(r'' + k + r':\s*\[(.*?)\n\s*\]', topic_text, re.DOTALL)
        if km:
            items = re.findall(r'\{[^\}]+\}', km.group(1))
            print(f'{k:15}: {len(items)} items')
