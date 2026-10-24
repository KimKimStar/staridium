import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update modal nav tabs order in HTML
old_nav = """      <div class="modal-nav">
        <button class="m-tab-btn active" id="tabBtnAction" onclick="switchModalTab('action')">🚀 내 채널 즉시 적용 (떡상 기획안 3선)</button>
        <button class="m-tab-btn" id="tabBtnHook" onclick="switchModalTab('hook')">① 3초 훅 & 성공 요인</button>
        <button class="m-tab-btn" id="tabBtnEditing" onclick="switchModalTab('editing')">② 컷전환 · 편집 방식 · 노래(BGM)</button>
        <button class="m-tab-btn" id="tabBtnScript" onclick="switchModalTab('script')">③ 타임라인별 대사 스크립트</button>
      </div>"""

new_nav = """      <div class="modal-nav">
        <button class="m-tab-btn active" id="tabBtnHook" onclick="switchModalTab('hook')">① 3초 훅 & 성공 요인</button>
        <button class="m-tab-btn" id="tabBtnEditing" onclick="switchModalTab('editing')">② 컷전환 · 편집 방식 · 노래(BGM)</button>
        <button class="m-tab-btn" id="tabBtnScript" onclick="switchModalTab('script')">③ 타임라인별 대사 스크립트</button>
        <button class="m-tab-btn" id="tabBtnAction" onclick="switchModalTab('action')">🚀 내 채널 즉시 적용 (떡상 기획안 3선)</button>
      </div>"""

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    print("Updated modal-nav order!")
else:
    print("old_nav not found")

# Update openAnatomyModal default tab to "hook"
html = html.replace('switchModalTab("action");', 'switchModalTab("hook");')
print("Updated openAnatomyModal to switchModalTab('hook')")

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
