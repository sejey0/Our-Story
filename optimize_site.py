from pathlib import Path
import re

root = Path(r'C:/Users/mjhay/Desktop/Programming/Visual Studio Code/Projects/My Wife Websites and Our Websites/Compiled Website')
html_path = root / 'index.html'
text = html_path.read_text(encoding='utf-8')

# 1) Add preload for the main background image and favicon
background_url = 'images/Bataan/2025/IMG_20251015_170052_999 (1) (1).jpg'
favicon_url = 'images/1st Image Together/1000019984.jpg'
if '<link rel="preload" as="image" href="' + background_url + '"' not in text:
    text = text.replace(
        '<link rel="preconnect" href="https://fonts.googleapis.com" />\n    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />',
        '<link rel="preload" as="image" href="' + background_url + '" />\n    <link rel="preload" as="image" href="' + favicon_url + '" />\n    <link rel="preconnect" href="https://fonts.googleapis.com" />\n    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />'
    )

# 2) Make background scroll instead of fixed for smoother loading / mobile behavior
text = text.replace(
    '        background-attachment: fixed;\n      }',
    '        background-attachment: scroll;\n      }'
)

# 3) Add loading="lazy" and decoding="async" to image tags that don't already specify them
text = re.sub(
    r'<img\b([^>]*?)>',
    lambda m: m.group(0)
    if ('loading=' in m.group(1) or 'decoding=' in m.group(1))
    else m.group(0).replace('>', ' loading="lazy" decoding="async">', 1),
    text,
    flags=re.I,
)

html_path.write_text(text, encoding='utf-8')
print('Optimizations applied to index.html')
