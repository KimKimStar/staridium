import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
for root, dirs, files in os.walk('3_바이럴분석_SaaS_ViralScope'):
    for f in files:
        if 'collector' in f or 'api' in f or 'fetch' in f or 'youtube' in f.lower():
            print(os.path.join(root, f))
