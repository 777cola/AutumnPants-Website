#!/usr/bin/env python3
"""Post-build: rename index.html → 舞台时光.html and copy images."""
import os, shutil

dist = os.path.dirname(os.path.abspath(__file__)) + '/dist'
src = os.path.dirname(dist) + '/public/images'
dst = dist + '/images'

# Copy images to dist
if os.path.isdir(src):
    os.makedirs(dst, exist_ok=True)
    for f in os.listdir(src):
        shutil.copy2(os.path.join(src, f), os.path.join(dst, f))

# Rename HTML
old = os.path.join(dist, 'index.html')
new = os.path.join(dist, '舞台时光.html')
if os.path.exists(old):
    if os.path.exists(new):
        os.remove(new)          # 重新构建时覆盖旧产物，避免留下上一次的版本
    os.rename(old, new)

# 注入自托管字体的样式表（构建产物不会自带；相对路径 ../../fonts/ 指回仓库根目录）
FONT_LINK = '<link rel="stylesheet" href="../../fonts/fonts.css">'
if os.path.exists(new):
    with open(new, encoding='utf-8') as f:
        html = f.read()
    if 'fonts/fonts.css' not in html:
        i = html.lower().rfind('</head>')
        html = (html[:i] + FONT_LINK + '\n' + html[i:]) if i != -1 else (FONT_LINK + html)
        with open(new, 'w', encoding='utf-8', newline='') as f:
            f.write(html)
        print('   + 已注入 ../../fonts/fonts.css')

print(f"✅ Done: {new}")
