# -*- coding: utf-8 -*-
import os

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update CATEGORIES[0] searchQ:
code = code.replace(
    '{ key: "total_kr", name: "🏆 대한민국 종합 숏폼 통합 랭킹", searchQ: "한국 인기 쇼츠 떡상", count: "75+" },',
    '{ key: "total_kr", name: "🏆 대한민국 종합 숏폼 통합 랭킹", searchQ: "#shorts 인기 급상승", count: "75+" },'
)

# 2. Update generateVideosForFilter view calculation to give total_kr mega-viral views (6800만회~1200만회):
old_views_block = """        // Realistic High-Viral Views strictly scaled by period (6m #1 is 1500만회+, NEVER 2300회)
        if (timeFilter === "1d") {
          baseViews = Math.max(350000, 3200000 - ((i - 1) * 38000) + Math.floor(Math.random() * 20000));
        } else if (timeFilter === "1w") {
          baseViews = Math.max(650000, 5800000 - ((i - 1) * 68000) + Math.floor(Math.random() * 30000));
        } else if (timeFilter === "1m") {
          baseViews = Math.max(1200000, 8500000 - ((i - 1) * 98000) + Math.floor(Math.random() * 40000));
        } else if (timeFilter === "3m") {
          baseViews = Math.max(1800000, 11800000 - ((i - 1) * 132000) + Math.floor(Math.random() * 50000));
        } else if (timeFilter === "6m") {
          baseViews = Math.max(2500000, 15500000 - ((i - 1) * 172000) + Math.floor(Math.random() * 60000));
        } else {
          baseViews = Math.max(3800000, 22000000 - ((i - 1) * 242000) + Math.floor(Math.random() * 80000));
        }"""

new_views_block = """        // Realistic High-Viral Views: total_kr is 대한민국 1위 메가 바이럴 (6,800만회~), NEVER 34만회!
        if (topicKey === "total_kr") {
          if (timeFilter === "1d") {
            baseViews = Math.max(1500000, 8500000 - ((i - 1) * 92000) + Math.floor(Math.random() * 40000));
          } else if (timeFilter === "1w") {
            baseViews = Math.max(3500000, 18500000 - ((i - 1) * 195000) + Math.floor(Math.random() * 70000));
          } else if (timeFilter === "1m") {
            baseViews = Math.max(5800000, 32000000 - ((i - 1) * 340000) + Math.floor(Math.random() * 110000));
          } else if (timeFilter === "3m") {
            baseViews = Math.max(8500000, 46000000 - ((i - 1) * 480000) + Math.floor(Math.random() * 150000));
          } else if (timeFilter === "6m") {
            baseViews = Math.max(12000000, 58000000 - ((i - 1) * 610000) + Math.floor(Math.random() * 200000));
          } else {
            // 1y: 대한민국 종합 1위는 6,800만회!
            baseViews = Math.max(15000000, 68000000 - ((i - 1) * 710000) + Math.floor(Math.random() * 250000));
          }
        } else {
          if (timeFilter === "1d") {
            baseViews = Math.max(350000, 3200000 - ((i - 1) * 38000) + Math.floor(Math.random() * 20000));
          } else if (timeFilter === "1w") {
            baseViews = Math.max(650000, 5800000 - ((i - 1) * 68000) + Math.floor(Math.random() * 30000));
          } else if (timeFilter === "1m") {
            baseViews = Math.max(1200000, 8500000 - ((i - 1) * 98000) + Math.floor(Math.random() * 40000));
          } else if (timeFilter === "3m") {
            baseViews = Math.max(1800000, 11800000 - ((i - 1) * 132000) + Math.floor(Math.random() * 50000));
          } else if (timeFilter === "6m") {
            baseViews = Math.max(2500000, 15500000 - ((i - 1) * 172000) + Math.floor(Math.random() * 60000));
          } else {
            baseViews = Math.max(3800000, 22000000 - ((i - 1) * 242000) + Math.floor(Math.random() * 80000));
          }
        }"""

if old_views_block in code:
    code = code.replace(old_views_block, new_views_block)
    print("Replaced views block with total_kr mega viral numbers (6,800만회).")
else:
    print("WARNING: old_views_block not found.")

# 3. In fetchRealYouTubeShorts, if topic is total_kr or query has "인기" or "종합", use chart=mostPopular or search #shorts
old_search_url = """        var publishedAfterIso = publishedAfter.toISOString();
        var searchUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&videoDuration=short&regionCode=KR&relevanceLanguage=ko&order=viewCount&publishedAfter=' + encodeURIComponent(publishedAfterIso) + '&q=' + encodeURIComponent(query) + '&maxResults=50&key=' + userApiKey;"""

new_search_url = """        var publishedAfterIso = publishedAfter.toISOString();
        var isOverallTopic = (currentTopicKey === 'total_kr' || query.indexOf('종합') !== -1 || query.indexOf('인기') !== -1);
        
        // For total_kr, use YouTube official Korea Most Popular chart or pure viral #shorts query to avoid small tutorial videos!
        var actualQuery = isOverallTopic ? '#shorts' : query;
        var searchUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&videoDuration=short&regionCode=KR&relevanceLanguage=ko&order=viewCount&publishedAfter=' + encodeURIComponent(publishedAfterIso) + '&q=' + encodeURIComponent(actualQuery) + '&maxResults=50&key=' + userApiKey;"""

if old_search_url in code:
    code = code.replace(old_search_url, new_search_url)
    print("Replaced search URL logic.")
else:
    print("WARNING: old_search_url not found.")

# Write back
with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved update_dashboard.py. Now executing...")
os.system(r'python "c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py"')
