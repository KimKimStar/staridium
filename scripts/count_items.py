import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_topic = False
count = 0
items_by_cat = {}
current_cat = None

for l in lines[1429:1623]:
    m_cat = re.match(r'\s*(\w+):\s*\[', l)
    if m_cat:
        current_cat = m_cat.group(1)
        items_by_cat[current_cat] = []
    if '{ id:' in l and current_cat:
        items_by_cat[current_cat].append(l.strip())
        count += 1

print(f"Total items in TOPIC_SPECIFIC_ITEMS: {count}")
for cat, itms in items_by_cat.items():
    print(f"  {cat}: {len(itms)}")
