import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'(\.category-pills-bar\s*\{[^}]+\})', text)
if m:
    print(m.group(1))

m2 = re.search(r'(\.minimal-control-bar\s*\{[^}]+\})', text)
if m2:
    print(m2.group(1))
