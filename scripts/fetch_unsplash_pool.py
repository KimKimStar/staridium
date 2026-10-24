import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Search Unsplash for high-quality photos per keyword
keywords = [
    ('diet', 'fitness diet salad workout food'),
    ('finance', 'stock market money business charts'),
    ('cooking', 'cooking food recipe delicious pasta'),
    ('beauty', 'skincare makeup cosmetics beauty face'),
    ('tech', 'smartphone tech computer gadget iphone'),
    ('pets', 'cute dog puppy cat kitten'),
    ('psychology', 'portrait person conversation facial expression'),
    ('humor', 'funny reaction expression actor face'),
    ('growth', 'morning routine book coffee journal meditation'),
    ('fashion', 'fashion model ootd outfit streetstyle'),
    ('travel', 'travel landscape nature resort ocean'),
    ('english', 'city conversation study language newyork'),
    ('total_kr', 'korea viral trend popular lifestyle')
]

print("Starting Unsplash photo search...")
