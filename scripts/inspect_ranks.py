import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# search rank badge classes
for m in re.finditer(r'class="[^"]*rank[^"]*"', text):
    print(m.group())

# search id="modal..." or where rank is used
for m in re.finditer(r'#[0-9]+', text):
    start = max(0, m.start() - 30)
    end = min(len(text), m.end() + 30)
    print(text[start:end].replace('\n', ' '))
