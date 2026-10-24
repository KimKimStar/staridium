# -*- coding: utf-8 -*-
import os

files_to_update = [
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\index.html',
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\3_바이럴분석_SaaS_ViralScope\preview.html',
    r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py'
]

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. In renderVideos, save the exact displayed list to window.currentDisplayedVideos
    old_grid_assign = 'grid.innerHTML = html;'
    new_grid_assign = 'grid.innerHTML = html;\n      window.currentDisplayedVideos = list;'

    if old_grid_assign in content and 'window.currentDisplayedVideos = list;' not in content:
        content = content.replace(old_grid_assign, new_grid_assign)
        print(f"Updated renderVideos with currentDisplayedVideos in {os.path.basename(file_path)}")

    # 2. In openAnatomyModal, first look up by vidId in window.currentDisplayedVideos
    old_modal_lookup = """    function openAnatomyModal(vidId) {
      var currentList = [];
      var cacheKey = currentTopicKey + "_" + activeTimeFilter;
      if (userApiKey && LIVE_API_CACHE[cacheKey] && (activePlatform === "shorts" || activePlatform === "all")) {
        currentList = LIVE_API_CACHE[cacheKey];
      } else {
        currentList = generateVideosForFilter(currentTopicKey, activeTimeFilter, activePlatform, activeSubId, activeSurgeFilter, activeSort, currentDisplayLimit).videos;
      }

      currentVideo = null;
      for (var i = 0; i < currentList.length; i++) {
        if (currentList[i].id === vidId) {
          currentVideo = currentList[i];
          break;
        }
      }
      if (!currentVideo) currentVideo = currentList[0];"""

    new_modal_lookup = """    function openAnatomyModal(vidId) {
      currentVideo = null;
      // 1. Direct lookup from currently displayed videos on screen (100% exact match!)
      if (window.currentDisplayedVideos && window.currentDisplayedVideos.length > 0) {
        for (var i = 0; i < window.currentDisplayedVideos.length; i++) {
          if (String(window.currentDisplayedVideos[i].id) === String(vidId)) {
            currentVideo = window.currentDisplayedVideos[i];
            break;
          }
        }
      }

      // 2. Fallback lookup if not found
      if (!currentVideo) {
        var currentList = [];
        var cacheKey = currentTopicKey + "_" + activeTimeFilter;
        if (userApiKey && LIVE_API_CACHE[cacheKey] && (activePlatform === "shorts" || activePlatform === "all")) {
          currentList = LIVE_API_CACHE[cacheKey];
        } else {
          currentList = generateVideosForFilter(currentTopicKey, activeTimeFilter, activePlatform, activeSubId, activeSurgeFilter, activeSort, currentDisplayLimit).videos;
        }
        for (var j = 0; j < currentList.length; j++) {
          if (String(currentList[j].id) === String(vidId)) {
            currentVideo = currentList[j];
            break;
          }
        }
        if (!currentVideo && window.currentDisplayedVideos && window.currentDisplayedVideos.length > 0) {
          currentVideo = window.currentDisplayedVideos[0];
        } else if (!currentVideo && currentList.length > 0) {
          currentVideo = currentList[0];
        }
      }"""

    if old_modal_lookup in content:
        content = content.replace(old_modal_lookup, new_modal_lookup)
        print(f"Updated openAnatomyModal lookup in {os.path.basename(file_path)}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished applying modal sync fix.")
