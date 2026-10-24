import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# A large candidate list of well-known shorts and viral YouTube videos (K-pop, Korean creators, viral shorts, international hits)
candidates = [
    # K-pop & Korean viral hits
    "9bZkp7q19f0", "gdZLi9oWNZg", "pSUydWEqKwE", "ArmDp-zijuc", "mH0_XpSH0fk",
    "fJ9rUzIMcZQ", "3JZ_D3ELwOQ", "kJQP7kiw5Fk", "XqZsoesa55w", "2Vv-BfVoq4g",
    "OPf0YbXqDm0", "JGwWNGJdvx8", "e_04ZrNroTo", "fRh_vgS2dFE", "hT_nvWreIhg",
    "k2qgadSvNyU", "YQHsXMglC9A", "09R8_2nJtjg", "RgKAFK5djSk", "uelHwf8o7_U",
    "FTQbiNvZqaY", "YykjpeuMNEk", "aJOTlE1K90k", "CevxZvSJLk8", "papuvlVeZg8",
    "fLexgOxsZu0", "SlPhMPnQ58k", "IcrbM1l_BoI", "hLQl3WQQoQ0", "LsoLEjrDogU",
    "nfWlot6h_JM", "5qap5aO4i9A", "k7wZ2Y3gJ_o", "0tOXsn_b_3E", "L_LUpnjgPso",
    # Additional viral YouTube shorts & videos
    "D0UnqGm_miA", "ioNng23DkIM", "vRXZj0DzXIA", "7PCkvCPvDXk", "gNi_6U5Pm_o",
    "kJQP7kiw5Fk", "ZbZSe6N_BXs", "kXYiU_JCYtU", "s8Qe0z7n6-E", "F4tHL8reNCs",
    "JGwWNGJdvx8", "fKopy74weus", "RgKAFK5djSk", "uelHwf8o7_U", "hLQl3WQQoQ0",
    "e-ORhEE9VVg", "PT2_F-1esPk", "pRpeEdMmmQ0", "astISOttCQ0", "fRh_vgS2dFE",
    "CevxZvSJLk8", "SlPhMPnQ58k", "ArmDp-zijuc", "2Vv-BfVoq4g", "09R8_2nJtjg"
]

candidates = list(dict.fromkeys(candidates)) # deduplicate
valid_list = []

for vid in candidates:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as res:
            if res.status == 200:
                data = json.loads(res.read().decode('utf-8'))
                valid_list.append({
                    "id": vid,
                    "title": data.get("title", ""),
                    "author": data.get("author_name", "")
                })
    except Exception:
        pass

print(f"Total valid tested: {len(valid_list)}")
with open("3_바이럴분석_SaaS_ViralScope/scripts/validated_yt_pool.json", "w", encoding="utf-8") as out:
    json.dump(valid_list, out, ensure_ascii=False, indent=2)
print("Saved to validated_yt_pool.json")
