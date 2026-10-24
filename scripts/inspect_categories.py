import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('var CATEGORIES =')
if idx != -1:
    print(html[idx:idx+2000])
