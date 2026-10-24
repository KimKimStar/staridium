# -*- coding: utf-8 -*-
import os

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the view count logic in generateVideosForFilter:
old_views_code = """        if (timeFilter === "1d") {
          baseViews = Math.max(90000, 2100000 - ((i - 1) * 22000) + Math.floor(Math.random() * 15000));
        } else if (timeFilter === "1w") {
          baseViews = Math.max(280000, 3950000 - ((i - 1) * 42000) + Math.floor(Math.random() * 25000));
        } else if (timeFilter === "1m") {
          baseViews = Math.max(550000, 5800000 - ((i - 1) * 62000) + Math.floor(Math.random() * 35000));
        } else if (timeFilter === "3m") {
          baseViews = Math.max(780000, 7400000 - ((i - 1) * 80000) + Math.floor(Math.random() * 45000));
        } else if (timeFilter === "6m") {
          baseViews = Math.max(980000, 8600000 - ((i - 1) * 92000) + Math.floor(Math.random() * 55000));
        } else {
          baseViews = Math.max(1200000, 9900000 - ((i - 1) * 105000) + Math.floor(Math.random() * 65000));
        }"""

new_views_code = """        // Realistic High-Viral Views strictly scaled by period (6m #1 is 1500만회+, NEVER 2300회)
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

# Replace in fetchRealYouTubeShorts:
old_api_return = """        return convertedVideos;
      } catch (err) {"""

new_api_return = """        // Filter out non-viral videos (< 100,000 views)
        var viralOnly = convertedVideos.filter(function(v) { return v.views >= 100000; });
        if (viralOnly.length >= 8) {
          convertedVideos = viralOnly;
        }

        // STRICT SORT BY VIEWS DESCENDING (가장 조회수 높은 영상이 무조건 1위!)
        convertedVideos.sort(function(a, b) { return b.views - a.views; });

        for (var r = 0; r < convertedVideos.length; r++) {
          convertedVideos[r].rank = r + 1;
        }

        return convertedVideos;
      } catch (err) {"""

# Replace in renderVideos:
old_render_sort = """      document.getElementById("countStatus").innerText = "[" + timeLabelText + " · " + platLabelText + "] 랭킹 정렬 완료 (" + list.length + "개)";

      if (list.length === 0) {
        var fallbackGen = generateVideosForFilter(currentTopicKey, activeTimeFilter, activePlatform, "all", null, "views", currentDisplayLimit);
        list = fallbackGen.videos;
      }"""

new_render_sort = """      // STRICT UNIVERSAL SORT BY USER CRITERIA (Default: Views Descending - 1500만회가 1위, 2300회는 절대 1위 불가)
      if (activeSurgeFilter === "surge_1d") {
        list.sort(function(a, b) { return b.surgeScore - a.surgeScore; });
      } else if (activeSurgeFilter === "surge_1w") {
        list.sort(function(a, b) { return (b.views / Math.max(1, b.daysAgo)) - (a.views / Math.max(1, a.daysAgo)); });
      } else {
        if (activeSort === "views") {
          list.sort(function(a, b) { return b.views - a.views; });
        } else if (activeSort === "surge") {
          list.sort(function(a, b) { return b.surgeScore - a.surgeScore; });
        } else {
          list.sort(function(a, b) { return b.viralScore - a.viralScore; });
        }
      }

      // Re-assign 1위 ~ N위 strictly based on sorted view order
      for (var r = 0; r < list.length; r++) {
        list[r].rank = r + 1;
      }

      document.getElementById("countStatus").innerText = "[" + timeLabelText + " · " + platLabelText + "] 1위(" + list[0].viewsFormatted + ")부터 조회수 순위 정렬 완료 (" + list.length + "개)";

      if (list.length === 0) {
        var fallbackGen = generateVideosForFilter(currentTopicKey, activeTimeFilter, activePlatform, "all", null, "views", currentDisplayLimit);
        list = fallbackGen.videos;
      }"""

if old_views_code in code:
    code = code.replace(old_views_code, new_views_code)
    print("Replaced views code successfully.")
else:
    print("WARNING: old_views_code not matched exactly.")

if old_api_return in code:
    code = code.replace(old_api_return, new_api_return)
    print("Replaced api return code successfully.")
else:
    print("WARNING: old_api_return not matched exactly.")

if old_render_sort in code:
    code = code.replace(old_render_sort, new_render_sort)
    print("Replaced render sort code successfully.")
else:
    print("WARNING: old_render_sort not matched exactly.")

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("update_dashboard.py updated. Now executing it...")
os.system(r'python "c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py"')
