import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(2460, min(2520, len(lines))):
    print(f'{j+1}: {lines[j]}', end='')
