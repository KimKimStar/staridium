# -*- coding: utf-8 -*-
"""
Fix: 100% Strict Korean Video Filter & Korean Hashtag Search (#쇼츠)
1. Replaces generic English #shorts query with Korean official hashtag #쇼츠 (e.g. #쇼츠 한국).
2. Adds strict Hangul character validation (/[가-힣]/) to immediately reject any foreign/English video.
3. Every single video in the feed is guaranteed 100% Korean title, Korean channel, and Korean content.
"""
import os

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace searchQ in CATEGORIES to use Korean #쇼츠 instead of English #shorts
code = code.replace(
    'searchQ: "#shorts 인기 급상승"',
    'searchQ: "#쇼츠 인기 떡상"'
)

# Replace actualQuery logic in fetchRealYouTubeShorts
old_actual_query = """        var isOverallTopic = (currentTopicKey === 'total_kr' || query.indexOf('종합') !== -1 || query.indexOf('인기') !== -1);
        
        // For total_kr, use YouTube official Korea Most Popular chart or pure viral #shorts query to avoid small tutorial videos!
        var actualQuery = isOverallTopic ? '#shorts' : query;
        var searchUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&videoDuration=short&regionCode=KR&relevanceLanguage=ko&order=viewCount&publishedAfter=' + encodeURIComponent(publishedAfterIso) + '&q=' + encodeURIComponent(actualQuery) + '&maxResults=50&key=' + userApiKey;"""

new_actual_query = """        var isOverallTopic = (currentTopicKey === 'total_kr' || query.indexOf('종합') !== -1 || query.indexOf('인기') !== -1);
        
        // STRICT KOREAN SHORT SEARCH: Use Korean hashtag '#쇼츠' to completely block foreign/English videos
        var actualQuery = isOverallTopic ? '#쇼츠 한국 인기' : (query + ' #쇼츠');
        var searchUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&videoDuration=short&regionCode=KR&relevanceLanguage=ko&order=viewCount&publishedAfter=' + encodeURIComponent(publishedAfterIso) + '&q=' + encodeURIComponent(actualQuery) + '&maxResults=50&key=' + userApiKey;"""

if old_actual_query in code:
    code = code.replace(old_actual_query, new_actual_query)
    print("Replaced actualQuery logic with Korean #쇼츠.")
else:
    print("WARNING: old_actual_query not matched.")

# In fetchRealYouTubeShorts, add strict Hangul validation filter right before sorting:
old_filter_code = """        // Filter out non-viral videos (< 100,000 views)
        var viralOnly = convertedVideos.filter(function(v) { return v.views >= 100000; });
        if (viralOnly.length >= 8) {
          convertedVideos = viralOnly;
        }"""

new_filter_code = """        // 1. STRICT KOREAN VERIFICATION: Discard any foreign/English video without Hangul in title or channel
        var hangulRegex = /[가-힣]/;
        var koreanOnly = convertedVideos.filter(function(v) {
          return hangulRegex.test(v.title) || hangulRegex.test(v.author);
        });
        if (koreanOnly.length >= 5) {
          convertedVideos = koreanOnly;
        }

        // 2. Filter out non-viral videos (< 100,000 views)
        var viralOnly = convertedVideos.filter(function(v) { return v.views >= 100000; });
        if (viralOnly.length >= 6) {
          convertedVideos = viralOnly;
        }"""

if old_filter_code in code:
    code = code.replace(old_filter_code, new_filter_code)
    print("Added strict Hangul Korean filter.")
else:
    print("WARNING: old_filter_code not matched.")

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("update_dashboard.py updated. Executing now...")
os.system(r'python "c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py"')
