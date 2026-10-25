import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find css block
style_match = re.search(r'<style>(.*?)</style>', text, re.DOTALL)
if style_match:
    css = style_match.group(1)
    # find fixed widths >= 250px
    for m in re.finditer(r'([a-zA-Z0-9_\-\.\#\s,]+)\{[^}]*?width:\s*([2-9][0-9]{2,}px|1[0-9]{3,}px)[^}]*?\}', css):
        selector = m.group(1).strip().replace('\n', ' ')
        width = m.group(2)
        print(f'{width:8} -> {selector[:50]}')
