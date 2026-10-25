import subprocess
import os
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_profile = r"C:\Users\kwang\AppData\Local\Temp\chrome_mobile_test"
os.makedirs(temp_profile, exist_ok=True)

# Test 1: Mobile Viewport 390x844 (iPhone)
file_url = "file:///c:/Users/kwang/OneDrive/Desktop/제미나이 바이블코딩/3_바이럴분석_SaaS_ViralScope/index.html"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={temp_profile}",
    "--window-size=390,844",
    "--dump-dom",
    file_url
]

proc = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
dom = proc.stdout

print(f"Chrome Dump DOM length: {len(dom)} chars")

# Check DOM elements
checks = [
    ("mobileMenuBtn", 'id="mobileMenuBtn"' in dom),
    ("sidebarBackdrop", 'id="sidebarBackdrop"' in dom),
    ("mobileSidebarClose", 'id="mobileSidebarClose"' in dom),
    ("videoGrid", 'id="videoGrid"' in dom),
    ("SEARCH_DOMAIN_DATABASE", 'SEARCH_DOMAIN_DATABASE' in dom),
    ("SEARCH_CATALOG_POOL", 'SEARCH_CATALOG_POOL' in dom)
]

for name, res in checks:
    print(f"  [{'PASS' if res else 'FAIL'}] {name} in DOM: {res}")

if all(r for _, r in checks):
    print("\nHEADLESS CHROME DOM VERIFICATION PASSED!")
else:
    print("\nHEADLESS CHROME DOM VERIFICATION HAD ISSUES.")
