import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("function generateVideosForFilter(")
print(text[pos:pos+2000])
