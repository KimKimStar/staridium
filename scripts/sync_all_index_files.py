import shutil
import os

ws_root = r"c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩"
proj_dir = os.path.join(ws_root, "3_바이럴분석_SaaS_ViralScope")
src_index = os.path.join(proj_dir, "index.html")

dest_preview = os.path.join(proj_dir, "preview.html")
dest_root_index = os.path.join(ws_root, "index.html")

shutil.copy2(src_index, dest_preview)
shutil.copy2(src_index, dest_root_index)

print("Synchronized index.html to preview.html and root index.html successfully!")
print("Source size:", os.path.getsize(src_index))
print("Preview size:", os.path.getsize(dest_preview))
print("Root index size:", os.path.getsize(dest_root_index))
