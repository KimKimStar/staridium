import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for cls in ['api-modal-box', 'pricing-modal-box']:
    m = re.search(r'(\.' + cls + r'\s*\{[^}]+\})', text)
    if m:
        print(f'{cls}:')
        print(m.group(1))
        print('-'*30)
