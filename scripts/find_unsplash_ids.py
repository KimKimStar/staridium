import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

unsplash_ids = set()
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.py') or f.endswith('.html') or f.endswith('.ts') or f.endswith('.json'):
            path = os.path.join(root, f)
            try:
                content = open(path, encoding='utf-8', errors='ignore').read()
                matches = re.findall(r'photo-([a-zA-Z0-9_-]+)', content)
                for m in matches:
                    unsplash_ids.add(m)
            except Exception:
                pass

print(f"Total unique Unsplash photo IDs found in workspace: {len(unsplash_ids)}")
print(list(unsplash_ids)[:10])
