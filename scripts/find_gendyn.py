import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'function generateDynamicKeywordVideos' in l:
        print(f'Start line: {i+1}')
        for j in range(i, min(len(lines), i+80)):
            print(f'{j+1}: {lines[j]}', end='')
            if lines[j].strip() == '}' and j > i+35:
                print(f'\nEnd line: {j+1}')
                break
        break
