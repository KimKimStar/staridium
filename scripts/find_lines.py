import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'var TOPIC_SPECIFIC_ITEMS =' in l:
        print('start:', i+1)
    if 'var VERIFIED_YT_IDS =' in l:
        print('end:', i+1)
