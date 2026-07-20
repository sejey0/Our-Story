from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')
pattern = re.compile(r'(<img\s+)(?=src="images/Tarlac/2026/images/July 2026/")')
new_text, count = pattern.subn(r'\1data-date="July 2026" ', text)
path.write_text(new_text, encoding='utf-8')
print(f'Inserted data-date for {count} image tags')
