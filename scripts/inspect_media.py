import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'@media', text)]
print('Total @media rules found:', len(matches))
for idx in matches:
    print('--- @MEDIA RULE ---')
    print(text[idx:min(len(text), idx+300)])
