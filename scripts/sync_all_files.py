import shutil
import hashlib
import sys

sys.stdout.reconfigure(encoding='utf-8')

src = '3_바이럴분석_SaaS_ViralScope/index.html'
dest_preview = '3_바이럴분석_SaaS_ViralScope/preview.html'
dest_root = 'index.html'

shutil.copyfile(src, dest_preview)
shutil.copyfile(src, dest_root)

def get_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

h_src = get_hash(src)
h_prev = get_hash(dest_preview)
h_root = get_hash(dest_root)

print(f"src hash:  {h_src[:16]}")
print(f"prev hash: {h_prev[:16]}")
print(f"root hash: {h_root[:16]}")
assert h_src == h_prev == h_root, "Files are not identical!"
print("All 3 files are 100% IDENTICAL and synchronized!")
