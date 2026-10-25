import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

classes = ['.modal-overlay', '.modal-container', '.modal-header', '.modal-body-split', '.modal-video-pane', '.modal-analysis-pane', '.modal-tabs-bar']

for cls in classes:
    m = re.search(r'(' + re.escape(cls) + r'\s*\{[^}]+\})', text)
    if m:
        print(f'{cls}:')
        print(m.group(1))
        print('-'*30)
