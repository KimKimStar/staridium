import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's verify:
# 1. generateDetailedVideoAnalysis exists
assert "function generateDetailedVideoAnalysis" in text, "generateDetailedVideoAnalysis missing!"
# 2. generateVideosForFilter exists
assert "function generateVideosForFilter" in text, "generateVideosForFilter missing!"
# 3. realYtId assignment exists
assert "var realYtId = baseItem.youtubeId" in text, "realYtId assignment missing!"
# 4. youtubeId: realYtId exists
assert "youtubeId: realYtId" in text, "youtubeId: realYtId missing!"
# 5. videoUrl: exactUrl exists
assert "videoUrl: exactUrl" in text, "videoUrl: exactUrl missing!"
# 6. thumbnail: realThumbnail exists
assert "thumbnail: realThumbnail" in text, "thumbnail: realThumbnail missing!"
# 7. hookAnalysis: analysis.hookAnalysis exists
assert "hookAnalysis: analysis.hookAnalysis" in text, "hookAnalysis: analysis.hookAnalysis missing!"
# 8. editingAnalysis: analysis.editingAnalysis exists
assert "editingAnalysis: analysis.editingAnalysis" in text, "editingAnalysis: analysis.editingAnalysis missing!"
# 9. timelineScript: analysis.timelineScript exists
assert "timelineScript: analysis.timelineScript" in text, "timelineScript: analysis.timelineScript missing!"
# 10. successFactors: analysis.successFactors exists
assert "successFactors: analysis.successFactors" in text, "successFactors: analysis.successFactors missing!"
# 11. sfx display in switchModalTab exists
assert "v.editingAnalysis.sfx" in text, "v.editingAnalysis.sfx missing!"

print("ALL 11 INTEGRITY CHECKS PASSED PERFECTLY!")
