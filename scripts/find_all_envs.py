import os, sys
sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk('.'):
    for f in files:
        if '.env' in f:
            full = os.path.join(root, f)
            print("Found env file:", full)
            try:
                with open(full, 'r', encoding='utf-8') as ef:
                    for line in ef:
                        if 'YOUTUBE' in line or 'API_KEY' in line:
                            print("  ", line.strip())
            except Exception as e:
                print("  error:", e)
