# -*- coding: utf-8 -*-
import os

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Make the Korean filter UNCONDITIONAL and strictly purge all foreign videos:
old_filter_block = """        // 1. STRICT KOREAN VERIFICATION: Discard any foreign/English video without Hangul in title or channel
        var hangulRegex = /[가-힣]/;
        var koreanOnly = convertedVideos.filter(function(v) {
          return hangulRegex.test(v.title) || hangulRegex.test(v.author);
        });
        if (koreanOnly.length >= 5) {
          convertedVideos = koreanOnly;
        }"""

new_filter_block = """        // 1. STRICT KOREAN VERIFICATION: 100% UNCONDITIONAL PURGE OF FOREIGN VIDEOS
        // Any video without Korean Hangul characters in either title or channel is instantly discarded!
        var hangulRegex = /[가-힣]/;
        convertedVideos = convertedVideos.filter(function(v) {
          return hangulRegex.test(v.title) || hangulRegex.test(v.author);
        });"""

if old_filter_block in code:
    code = code.replace(old_filter_block, new_filter_block)
    print("Replaced with unconditional Korean filter.")
else:
    print("WARNING: old_filter_block not found.")

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved. Executing update_dashboard.py...")
os.system(r'python "c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py"')
