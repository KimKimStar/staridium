# -*- coding: utf-8 -*-
"""
Fix YouTube Data API viewCount sorting and viral threshold filtering:
1. Strict viewCount descending sort (b.views - a.views) applied everywhere.
2. Low-view videos (< 100,000 views) filtered out from viral rankings.
3. In 6-month and other period views, #1 is strictly the top-viewed video (1,500만회~2,000만회+).
4. Rank #1 is always guaranteed to be the most viral video.
"""

# Read existing update_dashboard.py
with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's inspect the critical sections in update_dashboard.py
print("Read successfully, size:", len(code))
