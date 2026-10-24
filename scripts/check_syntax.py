import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check script tags
scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
print(f"Total <script> blocks: {len(scripts)}")

main_script = scripts[0] if scripts else ""
open_curly = main_script.count('{')
close_curly = main_script.count('}')
open_paren = main_script.count('(')
close_paren = main_script.count(')')
open_bracket = main_script.count('[')
close_bracket = main_script.count(']')

print(f"Curlys: {open_curly} vs {close_curly} (diff: {open_curly - close_curly})")
print(f"Parens: {open_paren} vs {close_paren} (diff: {open_paren - close_paren})")
print(f"Brackets: {open_bracket} vs {close_bracket} (diff: {open_bracket - close_bracket})")

# Check if node can parse it (or test with node if available)
print("File length:", len(text))
