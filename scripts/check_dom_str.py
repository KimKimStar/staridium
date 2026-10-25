import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('var SEARCH_DOMAIN_DATABASE =')
print('Index:', idx)
if idx != -1:
    print(text[idx:idx+300])
