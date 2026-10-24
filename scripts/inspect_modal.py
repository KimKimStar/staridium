import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="anatomyModal"')
if idx != -1:
    print("Found anatomyModal at", idx)
    print(html[idx:idx+2500])
else:
    print("anatomyModal not found")
