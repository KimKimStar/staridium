import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_category_photos.json", "r", encoding="utf-8") as f:
    photos = json.load(f)

# Ensure each category has at least 15~23 photos (trimming even lengths if needed to be co-prime with 4)
for cat, pool in photos.items():
    if len(pool) % 2 == 0:
        pool.pop() # make it odd so gcd(len(pool), 4) == 1!
    
    crops = ["entropy", "center", "faces", "top"]
    generated_urls = []
    for i in range(1, 76):
        p_idx = (i - 1) % len(pool)
        crop_mode = crops[(i - 1) % len(crops)]
        url = f"https://images.unsplash.com/photo-{pool[p_idx]}?w=600&h=1067&fit=crop&crop={crop_mode}&auto=format&q=80"
        generated_urls.append(url)
    
    unique_count = len(set(generated_urls))
    adjacent_dups = sum(1 for j in range(len(generated_urls)-1) if generated_urls[j] == generated_urls[j+1])
    print(f"{cat:12}: pool={len(pool):2d}, 75 cards unique={unique_count:2d}, adjacent duplicates={adjacent_dups}")
