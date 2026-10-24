# -*- coding: utf-8 -*-
import os

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update fetchRealYouTubeShorts to completely eliminate chart=mostPopular and implement MASTER_VIDEO_POOL
old_fetch_fn = """    async function fetchRealYouTubeShorts(query, timeFilter) {
      if (!userApiKey) return null;
      try {
        var now = new Date();
        var publishedAfter = new Date();
        if (timeFilter === '1d') publishedAfter.setDate(now.getDate() - 1);
        else if (timeFilter === '1w') publishedAfter.setDate(now.getDate() - 7);
        else if (timeFilter === '1m') publishedAfter.setMonth(now.getMonth() - 1);
        else if (timeFilter === '3m') publishedAfter.setMonth(now.getMonth() - 3);
        else if (timeFilter === '6m') publishedAfter.setMonth(now.getMonth() - 6);
        else publishedAfter.setFullYear(now.getFullYear() - 1);

        var publishedAfterIso = publishedAfter.toISOString();
        var isOverallTopic = (currentTopicKey === 'total_kr');
        var convertedVideos = [];

        // 1. If overall ranking AND timeFilter is '1y' (all-time), call mostPopular chart:
        if (isOverallTopic && timeFilter === '1y') {
          var chartUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=KR&maxResults=50&key=' + userApiKey;
          var chartRes = await fetch(chartUrl);
          if (chartRes.ok) {
            var chartJson = await chartRes.json();
            if (chartJson.items && chartJson.items.length > 0) {
              convertedVideos = parseYouTubeVideoItems(chartJson.items, now);
            }
          }
        }

        // 2. Topic Search: Clean search for Korean accounts WITHOUT any '#쇼츠' or '#shorts' tags!
        if (convertedVideos.length < 20) {
          var cleanQuery = query.replace(/#쇼츠/g, '').replace(/#shorts/g, '').replace(/인기 랭킹/g, '').trim();
          if (!cleanQuery) cleanQuery = "한국";

          // Use videoDuration=short to capture vertical shorts by duration, strictly in region KR with Korean language!
          var searchUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&videoDuration=short&regionCode=KR&relevanceLanguage=ko&order=viewCount&publishedAfter=' + encodeURIComponent(publishedAfterIso) + '&q=' + encodeURIComponent(cleanQuery) + '&maxResults=50&key=' + userApiKey;

          var searchRes = await fetch(searchUrl);
          if (searchRes.ok) {
            var searchJson = await searchRes.json();
            if (searchJson.items && searchJson.items.length > 0) {
              var videoIds = searchJson.items.map(function(item) { return item.id.videoId; }).filter(Boolean).join(',');
              var detailsUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails&id=' + videoIds + '&key=' + userApiKey;
              var detailsRes = await fetch(detailsUrl);
              if (detailsRes.ok) {
                var detailsJson = await detailsRes.json();
                var searchConverted = parseYouTubeVideoItems(detailsJson.items, now);
                convertedVideos = convertedVideos.concat(searchConverted);
              }
            }
          }
        }

        // 3. Deduplicate by youtubeId
        var seenIds = {};
        convertedVideos = convertedVideos.filter(function(v) {
          if (seenIds[v.youtubeId]) return false;
          seenIds[v.youtubeId] = true;
          return true;
        });

        // 4. STRICT KOREAN ACCOUNT FILTER: Title or Channel must have Korean Hangul!
        var hangulRegex = /[가-힣]/;
        convertedVideos = convertedVideos.filter(function(v) {
          return hangulRegex.test(v.title) || hangulRegex.test(v.author);
        });

        // 5. STRICT REAL-TIME DATE VERIFICATION: Absolutely block videos that do not match the requested timeframe!
        if (timeFilter === '1d') {
          // Strictly published within the last 24 hours! (Never allow 5-day old videos!)
          convertedVideos = convertedVideos.filter(function(v) {
            return v.diffHours <= 24 && v.daysAgo === 0;
          });
        } else if (timeFilter === '1w') {
          convertedVideos = convertedVideos.filter(function(v) { return v.daysAgo <= 7; });
        } else if (timeFilter === '1m') {
          convertedVideos = convertedVideos.filter(function(v) { return v.daysAgo <= 30; });
        } else if (timeFilter === '3m') {
          convertedVideos = convertedVideos.filter(function(v) { return v.daysAgo <= 90; });
        } else if (timeFilter === '6m') {
          convertedVideos = convertedVideos.filter(function(v) { return v.daysAgo <= 180; });
        } else {
          convertedVideos = convertedVideos.filter(function(v) { return v.daysAgo <= 365; });
        }

        // 5. STRICT SORT BY VIEWS DESCENDING (조회수가 가장 많은 영상이 무조건 1위!)
        convertedVideos.sort(function(a, b) { return b.views - a.views; });

        for (var r = 0; r < convertedVideos.length; r++) {
          convertedVideos[r].rank = r + 1;
        }

        return convertedVideos;
      } catch (err) {
        console.error('YouTube Live Fetch Error:', err);
        return null;
      }
    }"""

new_fetch_fn = """    // Universal Real-Time Master Video Pool to ensure mathematical period consistency:
    // Any video valid for 6 months (e.g. 22.58M views) is automatically included in 1-year ranking!
    window.MASTER_VIDEO_POOL = window.MASTER_VIDEO_POOL || {};

    async function fetchRealYouTubeShorts(query, timeFilter) {
      if (!userApiKey) return null;
      try {
        var now = new Date();
        var publishedAfter = new Date();
        if (timeFilter === '1d') publishedAfter.setDate(now.getDate() - 1);
        else if (timeFilter === '1w') publishedAfter.setDate(now.getDate() - 7);
        else if (timeFilter === '1m') publishedAfter.setMonth(now.getMonth() - 1);
        else if (timeFilter === '3m') publishedAfter.setMonth(now.getMonth() - 3);
        else if (timeFilter === '6m') publishedAfter.setMonth(now.getMonth() - 6);
        else publishedAfter.setFullYear(now.getFullYear() - 1);

        var publishedAfterIso = publishedAfter.toISOString();
        var isOverallTopic = (currentTopicKey === 'total_kr');

        var cleanQuery = query.replace(/#쇼츠/g, '').replace(/#shorts/g, '').replace(/인기 랭킹/g, '').trim();
        if (!cleanQuery) cleanQuery = "한국";

        // Query YouTube Data API search endpoint strictly ordered by viewCount descending:
        // NEVER use chart=mostPopular because it returns trending velocity, not view count!
        var searchUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&videoDuration=short&regionCode=KR&relevanceLanguage=ko&order=viewCount&publishedAfter=' + encodeURIComponent(publishedAfterIso) + '&q=' + encodeURIComponent(cleanQuery) + '&maxResults=50&key=' + userApiKey;

        var searchRes = await fetch(searchUrl);
        if (searchRes.ok) {
          var searchJson = await searchRes.json();
          if (searchJson.items && searchJson.items.length > 0) {
            var videoIds = searchJson.items.map(function(item) { return item.id.videoId; }).filter(Boolean).join(',');
            var detailsUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails&id=' + videoIds + '&key=' + userApiKey;
            var detailsRes = await fetch(detailsUrl);
            if (detailsRes.ok) {
              var detailsJson = await detailsRes.json();
              var newVideos = parseYouTubeVideoItems(detailsJson.items, now);

              // STRICT KOREAN ACCOUNT FILTER: Title or Channel must have Korean Hangul!
              var hangulRegex = /[가-힣]/;
              for (var k = 0; k < newVideos.length; k++) {
                var v = newVideos[k];
                if (hangulRegex.test(v.title) || hangulRegex.test(v.author)) {
                  // Add to Master Video Pool so videos are preserved across all broader periods
                  window.MASTER_VIDEO_POOL[v.youtubeId] = v;
                }
              }
            }
          }
        }

        // Aggregate candidates from Master Video Pool matching the requested period:
        var allPoolVideos = Object.values(window.MASTER_VIDEO_POOL);
        var filteredList = [];

        if (timeFilter === '1d') {
          // Strictly uploaded within the last 24 hours! (Never allow 5-day old videos!)
          filteredList = allPoolVideos.filter(function(v) {
            return v.diffHours <= 24 && v.daysAgo === 0;
          });
        } else if (timeFilter === '1w') {
          filteredList = allPoolVideos.filter(function(v) { return v.daysAgo <= 7; });
        } else if (timeFilter === '1m') {
          filteredList = allPoolVideos.filter(function(v) { return v.daysAgo <= 30; });
        } else if (timeFilter === '3m') {
          filteredList = allPoolVideos.filter(function(v) { return v.daysAgo <= 90; });
        } else if (timeFilter === '6m') {
          filteredList = allPoolVideos.filter(function(v) { return v.daysAgo <= 180; });
        } else {
          // 1y: Any video up to 365 days. Mathematically guaranteed to include 6m, 3m, 1m, 1w, 1d videos!
          filteredList = allPoolVideos.filter(function(v) { return v.daysAgo <= 365; });
        }

        // Filter by topic query relevance if not overall topic
        if (!isOverallTopic && cleanQuery && cleanQuery !== "한국") {
          var kw = cleanQuery.split(/\s+/)[0];
          var topicFiltered = filteredList.filter(function(v) {
            return v.title.indexOf(kw) !== -1 || v.author.indexOf(kw) !== -1;
          });
          if (topicFiltered.length >= 10) filteredList = topicFiltered;
        }

        // STRICT SORT BY VIEWS DESCENDING (조회수가 가장 많은 영상이 무조건 1위!)
        // Guarantees: 1-Year #1 views >= 6-Month #1 views >= 3-Month #1 views!
        filteredList.sort(function(a, b) { return b.views - a.views; });

        for (var r = 0; r < filteredList.length; r++) {
          filteredList[r].rank = r + 1;
        }

        return filteredList;
      } catch (err) {
        console.error('YouTube Live Fetch Error:', err);
        return null;
      }
    }"""

if old_fetch_fn in code:
    code = code.replace(old_fetch_fn, new_fetch_fn)
    print("Updated fetchRealYouTubeShorts with MASTER_VIDEO_POOL & strictly eliminated chart=mostPopular.")
else:
    print("WARNING: old_fetch_fn not found in update_dashboard.py.")

# 2. Update baseViews in generateVideosForFilter to guarantee strict hierarchy: 1y > 6m > 3m > 1m > 1w > 1d
old_base_views = """        if (topicKey === "total_kr") {
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

new_base_views = """        if (topicKey === "total_kr") {
          // Strictly Monotonic Hierarchy: 1y (6,800만) > 6m (4,200만) > 3m (2,600만) > 1m (1,500만) > 1w (750만) > 1d (320만)
          if (timeFilter === "1d") {
            baseViews = Math.max(1200000, 3200000 - ((i - 1) * 35000) + Math.floor(Math.random() * 20000));
          } else if (timeFilter === "1w") {
            baseViews = Math.max(2500000, 7500000 - ((i - 1) * 80000) + Math.floor(Math.random() * 40000));
          } else if (timeFilter === "1m") {
            baseViews = Math.max(4500000, 15000000 - ((i - 1) * 160000) + Math.floor(Math.random() * 70000));
          } else if (timeFilter === "3m") {
            baseViews = Math.max(7500000, 26000000 - ((i - 1) * 280000) + Math.floor(Math.random() * 100000));
          } else if (timeFilter === "6m") {
            baseViews = Math.max(12000000, 42000000 - ((i - 1) * 450000) + Math.floor(Math.random() * 150000));
          } else {
            // 1y: 대한민국 종합 1위는 6,800만회! (절대로 6개월 4,200만회보다 작지 않음!)
            baseViews = Math.max(18000000, 68000000 - ((i - 1) * 720000) + Math.floor(Math.random() * 250000));
          }
        } else {
          // Strictly Monotonic Category Hierarchy: 1y (3,200만) > 6m (2,100만) > 3m (1,250만) > 1m (720만) > 1w (360만) > 1d (150만)
          if (timeFilter === "1d") {
            baseViews = Math.max(350000, 1500000 - ((i - 1) * 18000) + Math.floor(Math.random() * 10000));
          } else if (timeFilter === "1w") {
            baseViews = Math.max(650000, 3600000 - ((i - 1) * 42000) + Math.floor(Math.random() * 20000));
          } else if (timeFilter === "1m") {
            baseViews = Math.max(1200000, 7200000 - ((i - 1) * 85000) + Math.floor(Math.random() * 30000));
          } else if (timeFilter === "3m") {
            baseViews = Math.max(2200000, 12500000 - ((i - 1) * 145000) + Math.floor(Math.random() * 50000));
          } else if (timeFilter === "6m") {
            baseViews = Math.max(3500000, 21000000 - ((i - 1) * 235000) + Math.floor(Math.random() * 70000));
          } else {
            // 1y: 3,200만회! (6개월 2,100만회보다 무조건 큼!)
            baseViews = Math.max(5000000, 32000000 - ((i - 1) * 360000) + Math.floor(Math.random() * 90000));
          }
        }"""

if old_base_views in code:
    code = code.replace(old_base_views, new_base_views)
    print("Updated baseViews with strictly monotonic hierarchy across all periods.")
else:
    print("WARNING: old_base_views not found in update_dashboard.py.")

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved update_dashboard.py. Rebuilding index.html and preview.html...")
os.system(r'python "c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py"')
