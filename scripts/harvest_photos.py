import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

all_photo_ids = {}

for root, dirs, files in os.walk('3_바이럴분석_SaaS_ViralScope'):
    for f in files:
        if f.endswith('.py') or f.endswith('.html') or f.endswith('.ts') or f.endswith('.json'):
            path = os.path.join(root, f)
            try:
                content = open(path, encoding='utf-8', errors='ignore').read()
                # find category blocks like diet: [...], finance: [...]
                for cat in ['diet', 'finance', 'cooking', 'beauty', 'tech', 'pets', 'psychology', 'humor', 'growth', 'fashion', 'travel', 'english', 'total_kr']:
                    m = re.search(r'' + cat + r':\s*\[(.*?)\]', content, re.DOTALL)
                    if m:
                        block = m.group(1)
                        p_ids = re.findall(r'photo-([a-zA-Z0-9_-]+)', block)
                        if p_ids:
                            if cat not in all_photo_ids:
                                all_photo_ids[cat] = set()
                            for pid in p_ids:
                                all_photo_ids[cat].add(pid)
            except Exception:
                pass

for cat, pids in all_photo_ids.items():
    print(f"{cat:12}: {len(pids)} unique photo IDs found in project history")
