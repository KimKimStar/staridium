import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'function openAnatomyModal(' in l:
        print(f'Line: {i+1}')
        for j in range(i, min(len(lines), i+90)):
            print(f'{j+1}: {lines[j]}', end='')
        break
