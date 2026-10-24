import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'var CATEGORIES = \[(.*?)\];', html, re.DOTALL)
if m:
    cat_text = m.group(1)
    keys = re.findall(r'key:\s*"([^"]+)",\s*name:\s*"([^"]+)"', cat_text)
    for k, n in keys:
        print(f'{k:15} : {n}')
