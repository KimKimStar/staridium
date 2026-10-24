import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'function openAnatomyModal' in l:
        print('openAnatomyModal at line', i+1)
        for j in range(i, min(i+50, len(lines))):
            print(f'{j+1}: {lines[j]}', end='')
        break
