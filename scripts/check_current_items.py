import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect what is in TOPIC_SPECIFIC_ITEMS right now
m = re.search(r'var TOPIC_SPECIFIC_ITEMS = \{.*?\n    \};', html, re.DOTALL)
if m:
    block = m.group(0)
    # Check diet items
    m_diet = re.search(r'diet: \[(.*?)\]', block, re.DOTALL)
    if m_diet:
        diet_str = m_diet.group(1)
        items = re.findall(r'\{\s*id:\s*"([^"]+)",\s*youtubeId:\s*"([^"]+)",\s*thumbnail:\s*"([^"]+)",\s*title:\s*"([^"]+)",\s*ytChannel:\s*"([^"]+)",\s*subIndex:\s*(\d+)\s*\}', diet_str)
        print(f"Diet items count: {len(items)}")
        for itm in items[:5]:
            print(f"ID: {itm[0]} | YT: {itm[1]} | Title: {itm[3][:40]} | URL: https://www.youtube.com/shorts/{itm[1]}")
