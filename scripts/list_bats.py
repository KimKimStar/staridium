import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in os.listdir('.'):
    if f.endswith('.bat'):
        print(f)
