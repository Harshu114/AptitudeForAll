#!/usr/bin/env python3
import os

root = os.path.dirname(os.path.abspath(__file__))
categories = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)) and not d.startswith('.')]
html = ['<!DOCTYPE html><html><head><meta charset="utf-8"><title>AptitudeForAll</title>',
        '<style>body{font-family:Arial,sans-serif;margin:2rem;} h1{color:#2c3e50;} ul{list-style:none;padding:0;} li{margin:0.5rem 0;} a{text-decoration:none;color:#2980b9;} a:hover{text-decoration:underline;}</style>',
        '</head><body>',
        '<h1>AptitudeForAll - Quiz PDFs</h1>']

for cat in sorted(categories):
    cat_path = os.path.join(root, cat)
    pdfs = [f for f in os.listdir(cat_path) if f.lower().endswith('.pdf')]
    if not pdfs:
        continue
    html.append(f'<h2>{cat}</h2><ul>')
    for pdf in sorted(pdfs):
        rel = os.path.join(cat, pdf).replace('\\', '/')
        html.append(f'<li><a href="{rel}" target="_blank">{pdf}</a></li>')
    html.append('</ul>')

html.append('</body></html>')
with open(os.path.join(root, 'index.html'), 'w') as f:
    f.write('\n'.join(html))
print('index.html generated')