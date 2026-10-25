import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("'toggleMobileSidebar' in text?", 'toggleMobileSidebar' in text)
idx = text.find('function selectCategory')
print('Index of function selectCategory:', idx)
if idx != -1:
    print(text[idx-50:idx+250])
