import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for target in ['modal-video-pane', 'modal-analysis-pane', 'modal-tabs-bar', 'btn-modal-tab']:
    m = re.search(r'(\.' + re.escape(target) + r'\s*\{[^}]+\})', text)
    if m:
        print(f'{target}:')
        print(m.group(1))
        print('-'*30)
