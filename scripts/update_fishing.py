import urllib.request
import urllib.parse
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

for q, dname in [("낚시 쇼츠", "fishing"), ("라면 레시피 꿀조합 쇼츠", "ramen")]:
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=8) as res:
        html = res.read().decode('utf-8', errors='ignore')
        vids = list(dict.fromkeys(re.findall(r'"videoId":\s*"([a-zA-Z0-9_-]{11})"', html)))
        valid = []
        for v in vids:
            if len(valid) >= 10: break
            try:
                ourl = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={v}&format=json"
                oreq = urllib.request.Request(ourl, headers=headers)
                with urllib.request.urlopen(oreq, timeout=3) as ores:
                    d = json.loads(ores.read().decode('utf-8'))
                    valid.append({"youtubeId": v, "title": d.get("title", ""), "author": d.get("author_name", ""), "thumbnail": f"https://i.ytimg.com/vi/{v}/hqdefault.jpg"})
                    print(f"[{dname}] {v}: {d.get('title')[:30]} ({d.get('author_name')})")
            except: pass

        # update verified_search_domains.json
        with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_search_domains.json", "r", encoding="utf-8") as f:
            all_domains = json.load(f)
        all_domains[dname] = valid
        with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_search_domains.json", "w", encoding="utf-8") as f:
            json.dump(all_domains, f, ensure_ascii=False, indent=2)

print("Fishing and ramen updated successfully!")
