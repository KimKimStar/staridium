import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check where generateVideosForFilter starts
gen_func_start = html.find('function generateVideosForFilter(')
if gen_func_start == -1:
    print("Error: generateVideosForFilter not found")
    sys.exit(1)

print("Found generateVideosForFilter at index", gen_func_start)
