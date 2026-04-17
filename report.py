from pathlib import Path

nfo_files = list(Path('./examples').glob('*.nfo'))
xml_files = list(Path('./examples').glob('*.xml'))
print(nfo_files)
print(xml_files)

for file in nfo_files:
    pass

for file in xml_files:
    pass