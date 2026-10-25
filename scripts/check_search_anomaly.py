import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract TOPIC_SPECIFIC_ITEMS
m = re.search(r'var TOPIC_SPECIFIC_ITEMS = (\{.*?\n    \});', text, re.DOTALL)
if m:
    json_str = m.group(1)
    try:
        data = json.loads(json_str)
        print('Successfully parsed TOPIC_SPECIFIC_ITEMS as JSON!')
        for k, v in data.items():
            print(f'Category: {k}, item count: {len(v)}')
    except Exception as e:
        print('JSON parse failed:', e)
        # Regex search for keys
        keys = re.findall(r'"([a-zA-Z0-9_]+)":\s*\[', json_str)
        print('Found keys via regex:', keys)
