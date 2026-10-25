import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'function selectCategory(' in l or 'function resetSearchToCategory(' in l:
        print(f'{i+1}: {l.strip()}')
