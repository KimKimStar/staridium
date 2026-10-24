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

    # 1. Replace selectCategory with instant 0s navigation (no API spam)
    old_select_cat = """async function selectCategory(key) {
      currentTopicKey = key;
      currentDisplayLimit = 75; // reset limit
      var cat = CATEGORIES.find(function(c) { return c.key === key; }) || CATEGORIES[0];

      document.getElementById("currentTopicLabel").innerText = cat.name;
      activeSubId = "all";
      renderSidebar();
      renderSubtopics();

      if (userApiKey && (activePlatform === "shorts" || activePlatform === "all")) {
        showToast("🔄 유튜브 공식 서버에서 '" + cat.searchQ + "' 최신 데이터 수집 중...", "success");
        var liveVideos = await fetchRealYouTubeShorts(cat.searchQ, activeTimeFilter);
        if (liveVideos && liveVideos.length > 0) {
          LIVE_API_CACHE[currentTopicKey + "_" + activeTimeFilter] = liveVideos;
          showToast("✅ YouTube Data API 실시간 연동 완료: 실제 썸네일 & 공식 URL 반영!", "success");
        }
      }

      renderVideos();
    }"""

    new_select_cat = """function selectCategory(key) {
      currentTopicKey = key;
      currentDisplayLimit = 75; // reset limit
      var cat = CATEGORIES.find(function(c) { return c.key === key; }) || CATEGORIES[0];

      document.getElementById("currentTopicLabel").innerText = cat.name;
      activeSubId = "all";
      renderSidebar();
      renderSubtopics();
      renderVideos();
    }"""

    if old_select_cat in content:
        content = content.replace(old_select_cat, new_select_cat)
        print(f"Updated selectCategory (instant navigation) in {os.path.basename(file_path)}")

    # 2. Replace setTimeFilter with instant 0s navigation (no API spam)
    old_set_time = """async function setTimeFilter(filter, btn) {
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

    new_set_time = """function setTimeFilter(filter, btn) {
      activeTimeFilter = filter;
      activeSurgeFilter = null;
      var buttons = document.querySelectorAll(".time-filter-section .t-btn");
      for (var i = 0; i < buttons.length; i++) buttons[i].classList.remove("active");
      btn.classList.add("active");

      renderVideos();
    }"""

    if old_set_time in content:
        content = content.replace(old_set_time, new_set_time)
        print(f"Updated setTimeFilter (instant navigation) in {os.path.basename(file_path)}")

    # 3. Add 1-Hour Hourly Snapshot Engine
    old_refresh_section = """    async function triggerRefreshNow() {
      refreshSecondsLeft = 3600;
      var status = document.getElementById("countStatus");
      status.innerText = "🔄 실시간 최신 랭킹 데이터 동기화 중...";
      status.style.color = "var(--accent-emerald)";

      var cat = CATEGORIES.find(function(c) { return c.key === currentTopicKey; }) || CATEGORIES[0];

      if (userApiKey && (activePlatform === "shorts" || activePlatform === "all")) {
        showToast("🔄 유튜브 공식 서버에서 '" + cat.searchQ + "' 실시간 데이터 수집 중...", "success");
        var liveVideos = await fetchRealYouTubeShorts(cat.searchQ, activeTimeFilter);
        if (liveVideos && liveVideos.length > 0) {
          LIVE_API_CACHE[currentTopicKey + "_" + activeTimeFilter] = liveVideos;
          showToast("✅ 유튜브 공식 API 실시간 연동 성공!", "success");
        }
      }

      renderVideos();
      status.style.color = "";
    }"""

    new_refresh_section = """    // 1-Hour Periodic Snapshot System (No API spamming on click/refresh!)
    function loadHourlySnapshot() {
      try {
        var raw = localStorage.getItem("viralscope_hourly_snapshot");
        if (raw) {
          var obj = JSON.parse(raw);
          if (obj && obj.timestamp) {
            var diffMs = Date.now() - obj.timestamp;
            if (diffMs < 3600 * 1000) {
              refreshSecondsLeft = Math.max(10, 3600 - Math.floor(diffMs / 1000));
              if (obj.data) LIVE_API_CACHE = obj.data;
              if (obj.masterPool) window.MASTER_VIDEO_POOL = obj.masterPool;
            }
          }
        }
      } catch(e) {}
    }

    function isSnapshotExpired() {
      try {
        var raw = localStorage.getItem("viralscope_hourly_snapshot");
        if (!raw) return true;
        var obj = JSON.parse(raw);
        if (!obj || !obj.timestamp) return true;
        return (Date.now() - obj.timestamp) >= (3600 * 1000);
      } catch(e) {
        return true;
      }
    }

    var isSyncingHourly = false;
    async function syncHourlyData(isManual) {
      if (!userApiKey || isSyncingHourly) return;
      isSyncingHourly = true;
      var status = document.getElementById("countStatus");
      if (status) {
        status.innerText = "🔄 1시간 정기 데이터 동기화 중...";
        status.style.color = "var(--accent-emerald)";
      }
      if (isManual) {
        showToast("🔄 1시간 정기 업데이트: 최신 유튜브 조회수를 갱신 중입니다...", "info");
      }

      try {
        var cat = CATEGORIES.find(function(c) { return c.key === currentTopicKey; }) || CATEGORIES[0];
        var liveVideos = await fetchRealYouTubeShorts(cat.searchQ, activeTimeFilter);
        if (liveVideos && liveVideos.length > 0) {
          LIVE_API_CACHE[currentTopicKey + "_" + activeTimeFilter] = liveVideos;
        }

        var snapshot = {
          timestamp: Date.now(),
          data: LIVE_API_CACHE,
          masterPool: window.MASTER_VIDEO_POOL || {}
        };
        try {
          localStorage.setItem("viralscope_hourly_snapshot", JSON.stringify(snapshot));
        } catch(e) {}

        refreshSecondsLeft = 3600;
        renderVideos();
        if (isManual) {
          showToast("✅ 1시간 동기화 완료! 앞으로 1시간 동안 저장된 조회수로 즉시 표시됩니다.", "success");
        }
      } catch(err) {
        console.error("Hourly sync error:", err);
      } finally {
        isSyncingHourly = false;
        if (status) status.style.color = "";
      }
    }

    async function triggerRefreshNow() {
      await syncHourlyData(true);
    }"""

    if old_refresh_section in content:
        content = content.replace(old_refresh_section, new_refresh_section)
        print(f"Updated refresh & hourly snapshot engine in {os.path.basename(file_path)}")

    # 4. Update init() to load hourly snapshot and only sync when 1 hour has expired
    old_init = """    // Initialization
    async function init() {
      updateApiStatusUI();
      renderSidebar();
      renderSubtopics();
      renderVideos();
      startRefreshTimer();

      if (userApiKey) {
        var cat = CATEGORIES[0];
        var liveVideos = await fetchRealYouTubeShorts(cat.searchQ, "1y");
        if (liveVideos && liveVideos.length > 0) {
          LIVE_API_CACHE["total_kr_1y"] = liveVideos;
          renderVideos();
          showToast("✅ YouTube 공식 API 실시간 연동 성공 (최신 쇼츠 자동 반영됨)", "success");
        }
      }
    }"""

    new_init = """    // Initialization: Loads saved 1-hour view counts immediately!
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
    }"""

    if old_init in content:
        content = content.replace(old_init, new_init)
        print(f"Updated init with hourly snapshot loader in {os.path.basename(file_path)}")

    # 5. Update countStatus label in renderVideos
    old_count_status = 'document.getElementById("countStatus").innerText = "[" + timeLabelText + " · " + platLabelText + "] 1위(" + list[0].viewsFormatted + ")부터 조회수 순위 정렬 완료 (" + list.length + "개)";'
    new_count_status = 'document.getElementById("countStatus").innerText = "[" + timeLabelText + " · " + platLabelText + "] 1시간 저장 조회수 랭킹 (총 " + list.length + "개)";'
    if old_count_status in content:
        content = content.replace(old_count_status, new_count_status)
        print(f"Updated countStatus text in {os.path.basename(file_path)}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished applying hourly snapshot system across all files.")
