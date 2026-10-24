import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/scripts/apply_authentic_thumbnails.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of apply_authentic_thumbnails.py:", len(text))
print(text[:1500])
