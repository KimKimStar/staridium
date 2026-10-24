import re

text = open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\index.html', encoding='utf-8').read()
pos = text.find('TOPIC_SPECIFIC_ITEMS = {')
pos2 = text.find('function generateVideosForFilter')
topic_block = text[pos:pos2]
ids = re.findall(r'id:\s*["\']([^"\']+)["\']', topic_block)
print('Unique video IDs in TOPIC_SPECIFIC_ITEMS:', set(ids))

for vid in list(set(ids))[:5]:
    print('Sample URL:', f'https://i.ytimg.com/vi/{vid}/hqdefault.jpg')
