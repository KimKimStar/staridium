# -*- coding: utf-8 -*-
import os
import urllib.request
import zipfile
import shutil
import subprocess

target_dir = os.path.expanduser('~') + r'\AppData\Local\Programs\Git'
zip_path = os.path.expanduser('~') + r'\AppData\Local\Temp\MinGit.zip'

url = 'https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/MinGit-2.47.1-64-bit.zip'

print(f"Downloading MinGit from {url}...")
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as resp, open(zip_path, 'wb') as out_file:
    shutil.copyfileobj(resp, out_file)

print("Download complete. Extracting to", target_dir)
os.makedirs(target_dir, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(target_dir)

git_exe = os.path.join(target_dir, 'cmd', 'git.exe')
print("Git executable:", git_exe, "Exists:", os.path.exists(git_exe))

# Test running git
res = subprocess.run([git_exe, '--version'], capture_output=True, text=True)
print("Git version output:", res.stdout.strip())
