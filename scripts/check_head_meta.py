import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

head_match = re.search(r'<head>(.*?)</head>', text, re.DOTALL)
if head_match:
    print("Head content:")
    print(head_match.group(1)[:1500])

iframe_match = re.search(r'<iframe.*?>', text)
if iframe_match:
    print("iframe tag:", iframe_match.group(0))
