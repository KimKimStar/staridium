import sys, json, os, glob
sys.stdout.reconfigure(encoding='utf-8')

for p in glob.glob('3_바이럴분석_SaaS_ViralScope/scripts/*.json'):
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f'File: {p}, type: {type(data)}')
            if isinstance(data, dict):
                print('  keys:', list(data.keys())[:6])
                for k in list(data.keys())[:3]:
                    val = data[k]
                    if isinstance(val, list):
                        print(f'    {k}: {len(val)} items')
                        if val and isinstance(val[0], dict) and 'youtubeId' in val[0]:
                            print(f'      first: {val[0]["youtubeId"]} - {val[0].get("title", "")[:30]}')
            elif isinstance(data, list):
                print(f'  list of length {len(data)}')
                if data and isinstance(data[0], dict):
                    print(f'  sample: {data[0]}')
    except Exception as e:
        print(f'Error reading {p}: {e}')
