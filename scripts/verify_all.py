import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'function getDiverseCategoryThumbnail' in text
assert 'var CATEGORY_PHOTOS =' in text
assert 'getDiverseCategoryThumbnail(topicKey, i, pOffset, timeFilter)' in text
assert 'generateDetailedVideoAnalysis(baseItem, topicKey, i, timeFilter, topicName)' in text

print("All components verified successfully in index.html!")
