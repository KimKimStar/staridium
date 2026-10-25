import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract all <script> blocks
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', text, re.DOTALL)
print(f"Found {len(scripts)} script blocks.")

# Save scripts to a temp js file and run node --check
for idx, s in enumerate(scripts):
    temp_file = f"3_바이럴분석_SaaS_ViralScope/scripts/temp_check_{idx}.js"
    with open(temp_file, "w", encoding="utf-8") as tf:
        tf.write(s)

print("Saved script blocks for node validation.")
