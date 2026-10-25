import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/scripts/validated_yt_pool.json', 'r', encoding='utf-8') as f:
    pool = json.load(f)
    print('validated_yt_pool length:', len(pool))
    for it in pool[:10]:
        print(' ', it)

with open('3_바이럴분석_SaaS_ViralScope/scripts/verified_category_photos.json', 'r', encoding='utf-8') as f:
    photos = json.load(f)
    print('verified_category_photos categories:', list(photos.keys()))
    for k, v in photos.items():
        print(f'  {k}: {len(v)} photos')
        if v:
            print('    sample:', v[0])
