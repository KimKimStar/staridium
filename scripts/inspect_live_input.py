import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'function handleSearchLiveInput[\s\S]*?\n    \}', text)
if m:
    print(m.group(0))
