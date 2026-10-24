import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for fetchRealYouTubeShorts or API key in index.html
m = re.search(r'function fetchRealYouTubeShorts.*?\n    \}', text, re.DOTALL)
if m:
    print("Found fetchRealYouTubeShorts:")
    print(m.group(0)[:1000])

m2 = re.search(r'userApiKey.*?;', text)
if m2:
    print("Found userApiKey:", m2.group(0))
