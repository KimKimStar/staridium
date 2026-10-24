import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

topic_names = []
for i in range(1429, 1623):
    line = lines[i]
    if line.strip().startswith('//') and '.' in line:
        print(line.strip())
