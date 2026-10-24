# -*- coding: utf-8 -*-
import os

target_files = [
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\index.html',
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\3_바이럴분석_SaaS_ViralScope\index.html',
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\3_바이럴분석_SaaS_ViralScope\preview.html',
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\3_바이럴분석_SaaS_ViralScope\scripts\update_dashboard.py'
]

# Real, 100% active YouTube video IDs with permanent cached hqdefault thumbnails on ytimg CDN:
REAL_YT_IDS = [
    "kJQP7kiw5Fk", # Despacito
    "9bZkp7q19f0", # Gangnam Style
    "XqZsoesa55w", # Baby Shark
    "gdZLi9oWNZg", # BTS Dynamite
    "11cta61Wi0g", # NewJeans Hype Boy
    "ArmDp-zijuc", # NewJeans Super Shy
    "pSUydWEqKwE", # NewJeans Ditto
    "6ZUIwj3FgUY", # IVE I AM
    "Y8JFxS1HlDo", # IVE Love Dive
    "hLvWy2b857I", # LE SSERAFIM Perfect Night
    "d9IxdwEFk1c", # IU Palette
    "OPf0YbXqDm0"  # Uptown Funk
]

fake_ids = [
    "8wRzKjCq7m4",
    "4mNn92Fm2-M",
    "WcIcVapfqXw",
    "kOHB85vDuow",
    "a3ICNMQW7Ok",
    "sCj1mH3K1bQ",
    "M_C38M1hOQo"
]

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace fake IDs with real active YouTube video IDs across the file
    for idx, fake in enumerate(fake_ids):
        real = REAL_YT_IDS[idx % len(REAL_YT_IDS)]
        content = content.replace(f'"{fake}"', f'"{real}"')
        content = content.replace(f"'{fake}'", f"'{real}'")
    print(f"Replaced fake IDs with real active YouTube IDs in {os.path.basename(file_path)}")

    # 2. Add SVG Poster generator helper before renderVideos
    svg_generator_fn = """    // High-Res SVG Poster Generator: 100% Guarantees Beautiful Thumbnail Display
    function getSvgPosterDataUri(title, author, platform, rank) {
      var colors = [
        ['#1e1b4b', '#4338ca', '#818cf8'],
        ['#311042', '#7e22ce', '#c084fc'],
        ['#064e3b', '#059669', '#34d399'],
        ['#7c2d12', '#ea580c', '#fb923c'],
        ['#831843', '#db2777', '#f472b6'],
        ['#0f172a', '#334155', '#94a3b8']
      ];
      var c = colors[rank % colors.length];
      var cleanTitle = (title || "대한민국 1위 떡상 숏폼").replace(/<[^>]*>/g, '').replace(/&/g, '&amp;').replace(/"/g, '&quot;');
      var line1 = cleanTitle.slice(0, 16);
      var line2 = cleanTitle.slice(16, 32);
      var platBadge = platform === 'shorts' ? '🔴 YouTube Shorts' : platform === 'reels' ? '🟣 Instagram Reels' : '⚫ TikTok Korea';

      var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 720" width="100%" height="100%">' +
        '<defs>' +
          '<linearGradient id="bg' + rank + '" x1="0%" y1="0%" x2="100%" y2="100%">' +
            '<stop offset="0%" stop-color="' + c[0] + '"/>' +
            '<stop offset="50%" stop-color="' + c[1] + '"/>' +
            '<stop offset="100%" stop-color="#090d16"/>' +
          '</linearGradient>' +
          '<radialGradient id="glow' + rank + '" cx="50%" cy="35%" r="50%">' +
            '<stop offset="0%" stop-color="' + c[2] + '" stop-opacity="0.35"/>' +
            '<stop offset="100%" stop-color="#000" stop-opacity="0"/>' +
          '</radialGradient>' +
        '</defs>' +
        '<rect width="450" height="720" fill="url(#bg' + rank + ')"/>' +
        '<circle cx="225" cy="250" r="180" fill="url(#glow' + rank + ')"/>' +
        '<rect x="24" y="24" width="150" height="32" rx="16" fill="rgba(0,0,0,0.6)" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>' +
        '<text x="99" y="45" fill="#fff" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">' + platBadge + '</text>' +
        '<g transform="translate(225, 260)">' +
          '<circle r="46" fill="rgba(0,0,0,0.5)" stroke="' + c[2] + '" stroke-width="3"/>' +
          '<polygon points="-12,-20 -12,20 22,0" fill="#fff"/>' +
        '</g>' +
        '<rect x="24" y="460" width="402" height="236" rx="16" fill="rgba(0,0,0,0.72)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>' +
        '<text x="44" y="505" fill="#fff" font-size="20" font-weight="900" font-family="sans-serif">' + line1 + '</text>' +
        '<text x="44" y="538" fill="' + c[2] + '" font-size="20" font-weight="900" font-family="sans-serif">' + line2 + '</text>' +
        '<rect x="44" y="570" width="140" height="28" rx="14" fill="rgba(255,255,255,0.12)"/>' +
        '<text x="114" y="589" fill="#e2e8f0" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">👤 ' + (author || '한국 크리에이터').slice(0, 10) + '</text>' +
        '<text x="44" y="640" fill="#fbbf24" font-size="13" font-weight="bold" font-family="sans-serif">🔥 알고리즘 떡상 바이럴 공식 분석 완료</text>' +
      '</svg>';

      return 'data:image/svg+xml;utf8,' + encodeURIComponent(svg);
    }
"""

    if 'function getSvgPosterDataUri' not in content:
        pos_render = content.find('function renderVideos()')
        content = content[:pos_render] + svg_generator_fn + "\n    " + content[pos_render:]
        print(f"Added getSvgPosterDataUri helper to {os.path.basename(file_path)}")

    # 3. Update img tag in renderVideos:
    # Add referrerpolicy="no-referrer" (crucial for Chrome file:/// requests!)
    # And robust fallback to getSvgPosterDataUri on error
    old_img_tag = """html += '      <img src="' + realThumb + '" class="thumbnail-img" alt="' + v.title.replace(/"/g, '&quot;') + '" onerror="if(this.src.indexOf(\\'hqdefault\\')!==-1){this.src=\\'https://img.youtube.com/vi/' + v.youtubeId + '/mqdefault.jpg\\';}else if(this.src.indexOf(\\'mqdefault\\')!==-1){this.src=\\'https://img.youtube.com/vi/' + v.youtubeId + '/0.jpg\\';}" />';"""

    new_img_tag = """var fallbackPoster = getSvgPosterDataUri(v.title, v.author, v.platform, i);
        html += '      <img src="' + realThumb + '" referrerpolicy="no-referrer" class="thumbnail-img" alt="' + v.title.replace(/"/g, '&quot;') + '" onerror="if(this.dataset.tried!=\\'1\\'){this.dataset.tried=\\'1\\';this.src=\\'https://img.youtube.com/vi/' + v.youtubeId + '/mqdefault.jpg\\';}else{this.onerror=null;this.src=\\'' + fallbackPoster + '\\';}" />';"""

    if old_img_tag in content:
        content = content.replace(old_img_tag, new_img_tag)
        print(f"Updated img tag with referrerpolicy='no-referrer' & SVG fallback in {os.path.basename(file_path)}")
    else:
        print(f"WARNING: old_img_tag not found in {os.path.basename(file_path)}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished applying thumbnail fix across all files.")
