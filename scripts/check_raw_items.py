import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('var TOPIC_SPECIFIC_ITEMS =')
print("TOPIC_SPECIFIC_ITEMS index:", idx)
if idx != -1:
    print(html[idx:idx+1500])
