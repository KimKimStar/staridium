import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(min(30, len(lines))):
    print(lines[i], end='')
