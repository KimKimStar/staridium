import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'id=\"(pricingModal|apiModal)\"', text):
    idx = m.start()
    print('Found modal:', m.group())
    print(text[max(0, idx-50):min(len(text), idx+200)])
    print('='*40)
