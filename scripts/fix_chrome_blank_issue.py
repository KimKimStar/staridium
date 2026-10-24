# -*- coding: utf-8 -*-
import os

target_files = [
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\index.html',
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\3_바이럴분석_SaaS_ViralScope\index.html',
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\3_바이럴분석_SaaS_ViralScope\preview.html',
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\3_바이럴분석_SaaS_ViralScope\scripts\update_dashboard.py'
]

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. FIX FATAL BUG: Define subTopics inside generateVideosForFilter
    old_subtopics_decl = """      var catSubTopics = cat.subTopics || [
        { id: "sub-1", name: topicName + " 1티어 치트키" },
        { id: "sub-2", name: "한국인이 가장 많이 저지르는 실수 TOP 3" },
        { id: "sub-3", name: "7일 단기 챌린지 검증형" }
      ];"""

    new_subtopics_decl = """      var subTopics = cat.subTopics || [
        { id: "sub-1", name: topicName + " 1티어 치트키" },
        { id: "sub-2", name: "한국인이 가장 많이 저지르는 실수 TOP 3" },
        { id: "sub-3", name: "7일 단기 챌린지 검증형" }
      ];
      var catSubTopics = subTopics;"""

    if old_subtopics_decl in content:
        content = content.replace(old_subtopics_decl, new_subtopics_decl)
        print(f"Fixed fatal subTopics definition in {os.path.basename(file_path)}")

    # 2. Wrap top-level userApiKey access in try-catch (prevents Chrome file:/// SecurityError crash)
    old_key_decl = 'var userApiKey = localStorage.getItem("viralscope_yt_key") || "";'
    new_key_decl = 'var userApiKey = ""; try { userApiKey = localStorage.getItem("viralscope_yt_key") || ""; } catch(e) { userApiKey = ""; }'
    if old_key_decl in content:
        content = content.replace(old_key_decl, new_key_decl)
        print(f"Wrapped userApiKey in try-catch in {os.path.basename(file_path)}")

    # 3. Robust initialization with DOMContentLoaded & load fallback
    old_init_call = """    // Initialization: Loads saved 1-hour view counts immediately!
    async function init() {
      updateApiStatusUI();
      loadHourlySnapshot();
      renderSidebar();
      renderSubtopics();
      renderVideos();
      startRefreshTimer();

      // Only perform network sync if API key exists AND 1 hour has expired!
      if (userApiKey && isSnapshotExpired()) {
        await syncHourlyData(false);
      }
    }

    window.onload = init;"""

    new_init_call = """    // Initialization: Loads saved 1-hour view counts immediately!
    async function init() {
      if (window.isDashboardInitialized) return;
      window.isDashboardInitialized = true;
      try {
        updateApiStatusUI();
        loadHourlySnapshot();
        renderSidebar();
        renderSubtopics();
        renderVideos();
        startRefreshTimer();

        // Only perform network sync if API key exists AND 1 hour has expired!
        if (userApiKey && isSnapshotExpired()) {
          syncHourlyData(false).catch(function(e) { console.error(e); });
        }
      } catch (err) {
        console.error("Dashboard Init Error:", err);
        try {
          renderSidebar();
          renderVideos();
        } catch(e) {}
      }
    }

    // Chrome & Modern Browsers: Execute on DOMContentLoaded without waiting for external images
    if (document.readyState === "complete" || document.readyState === "interactive") {
      init();
    } else {
      document.addEventListener("DOMContentLoaded", init);
      window.addEventListener("load", function() {
        if (!window.isDashboardInitialized) init();
      });
    }"""

    if old_init_call in content:
        content = content.replace(old_init_call, new_init_call)
        print(f"Updated init trigger for Chrome & modern browsers in {os.path.basename(file_path)}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished applying Chrome blank fix across all files.")
