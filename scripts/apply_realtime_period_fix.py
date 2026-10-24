# -*- coding: utf-8 -*-
import os

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update parseYouTubeVideoItems to calculate exact diffHours and diffDays:
old_parse_item = """        var pubDate = new Date(item.snippet.publishedAt);
        var diffDays = Math.floor((now - pubDate) / (1000 * 60 * 60 * 24));
        var timeString = diffDays === 0 ? '오늘 (실시간)' : diffDays < 7 ? diffDays + '일 전' : diffDays < 30 ? Math.floor(diffDays/7) + '주 전' : Math.floor(diffDays/30) + '개월 전';"""

new_parse_item = """        var pubDate = new Date(item.snippet.publishedAt);
        var diffMs = now - pubDate;
        var diffHours = Math.floor(diffMs / (1000 * 60 * 60));
        var diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

        var timeString = "";
        if (diffHours < 1) {
          timeString = "방금 전 (오늘)";
        } else if (diffHours < 24) {
          timeString = diffHours + "시간 전 (오늘)";
        } else if (diffDays <= 7) {
          timeString = diffDays + "일 전";
        } else if (diffDays <= 30) {
          timeString = Math.floor(diffDays / 7) + "주 전";
        } else {
          timeString = Math.floor(diffDays / 30) + "개월 전";
        }"""

if old_parse_item in code:
    code = code.replace(old_parse_item, new_parse_item)
    print("Updated parseYouTubeVideoItems timestamp calculation.")
else:
    print("WARNING: old_parse_item not found.")

# Also add diffHours to the returned item object:
old_item_return = """          daysAgo: diffDays,
          timeString: timeString,"""

new_item_return = """          diffHours: diffHours,
          publishedAt: pubDate,
          daysAgo: diffDays,
          timeString: timeString,"""

if old_item_return in code:
    code = code.replace(old_item_return, new_item_return)
    print("Added diffHours & publishedAt to returned item.")
else:
    print("WARNING: old_item_return not found.")

# 2. In fetchRealYouTubeShorts:
# Fix 'isOverallTopic' logic so that when timeFilter is '1d', '1w', '3m', etc., it does NOT just blindly dump chart=mostPopular without date filtering!
old_chart_block = """        // 1. If overall ranking: Call YouTube's official Korea Most Popular chart directly!
        if (isOverallTopic) {
          var chartUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=KR&maxResults=50&key=' + userApiKey;
          var chartRes = await fetch(chartUrl);
          if (chartRes.ok) {
            var chartJson = await chartRes.json();
            if (chartJson.items && chartJson.items.length > 0) {
              convertedVideos = parseYouTubeVideoItems(chartJson.items, now);
            }
          }
        }"""

new_chart_block = """        // 1. If overall ranking AND timeFilter is '1y' (all-time), call mostPopular chart:
        if (isOverallTopic && timeFilter === '1y') {
          var chartUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=KR&maxResults=50&key=' + userApiKey;
          var chartRes = await fetch(chartUrl);
          if (chartRes.ok) {
            var chartJson = await chartRes.json();
            if (chartJson.items && chartJson.items.length > 0) {
              convertedVideos = parseYouTubeVideoItems(chartJson.items, now);
            }
          }
        }"""

if old_chart_block in code:
    code = code.replace(old_chart_block, new_chart_block)
    print("Updated chart block to only run for all-time 1y, allowing strict date queries for 1d, 1w, 3m, 6m.")
else:
    print("WARNING: old_chart_block not found.")

# 3. Add STRICT DATE FILTERING to fetchRealYouTubeShorts right after Hangul filter:
old_date_filter_target = """        // 4. STRICT KOREAN ACCOUNT FILTER: Title or Channel must have Korean Hangul!
        var hangulRegex = /[가-힣]/;
        convertedVideos = convertedVideos.filter(function(v) {
          return hangulRegex.test(v.title) || hangulRegex.test(v.author);
        });"""

new_date_filter_target = """        // 4. STRICT KOREAN ACCOUNT FILTER: Title or Channel must have Korean Hangul!
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
        }"""

if old_date_filter_target in code:
    code = code.replace(old_date_filter_target, new_date_filter_target)
    print("Added strict real-time date verification.")
else:
    print("WARNING: old_date_filter_target not found.")

# 4. In setTimeFilter, always trigger live fetch when switching to 3m, 1d, etc.:
old_set_time = """    // Period Filter Click Handler
    async function setTimeFilter(filter, btn) {
      activeTimeFilter = filter;
      activeSurgeFilter = null;
      var buttons = document.querySelectorAll(".time-filter-section .t-btn");
      for (var i = 0; i < buttons.length; i++) buttons[i].classList.remove("active");
      btn.classList.add("active");

      showToast("📅 [" + getTimeFilterLabel(filter) + "] 기준으로 영상을 즉시 재정렬합니다...", "success");

      if (userApiKey && (activePlatform === "shorts" || activePlatform === "all")) {
        var cat = CATEGORIES.find(function(c) { return c.key === currentTopicKey; }) || CATEGORIES[0];
        var liveVideos = await fetchRealYouTubeShorts(cat.searchQ, activeTimeFilter);
        if (liveVideos && liveVideos.length > 0) {
          LIVE_API_CACHE[currentTopicKey + "_" + activeTimeFilter] = liveVideos;
        }
      }

      renderVideos();
    }"""

new_set_time = """    // Period Filter Click Handler: Real-Time Live Fetch & Strict Date Reflection
    async function setTimeFilter(filter, btn) {
      activeTimeFilter = filter;
      activeSurgeFilter = null;
      var buttons = document.querySelectorAll(".time-filter-section .t-btn");
      for (var i = 0; i < buttons.length; i++) buttons[i].classList.remove("active");
      btn.classList.add("active");

      var timeLabel = getTimeFilterLabel(filter);
      showToast("🔄 [" + timeLabel + "] 실시간 유튜브 서버 데이터를 조회 및 순위 반영 중...", "success");

      // Live Real-Time Fetch on EVERY Period Switch
      if (userApiKey) {
        var cat = CATEGORIES.find(function(c) { return c.key === currentTopicKey; }) || CATEGORIES[0];
        var liveVideos = await fetchRealYouTubeShorts(cat.searchQ, activeTimeFilter);
        if (liveVideos && liveVideos.length > 0) {
          LIVE_API_CACHE[currentTopicKey + "_" + activeTimeFilter] = liveVideos;
          showToast("✅ [" + timeLabel + "] 기준 실시간 순위가 성공적으로 반영되었습니다!", "success");
        } else {
          showToast("💡 [" + timeLabel + "] 실시간 랭킹 순위 정렬 완료!", "success");
        }
      }

      renderVideos();
    }"""

if old_set_time in code:
    code = code.replace(old_set_time, new_set_time)
    print("Updated setTimeFilter with real-time live fetch on click.")
else:
    print("WARNING: old_set_time not found.")

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved update_dashboard.py. Executing...")
os.system(r'python "c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py"')
