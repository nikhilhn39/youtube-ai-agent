import moviepy, os
from pathlib import Path
p = Path(moviepy.__file__).parent
for root, dirs, files in os.walk(p):
    for f in files:
        if f.endswith('.py'):
            path = Path(root)/f
            try:
                txt = path.read_text(errors='ignore')
            except Exception:
                continue
            if 'VideoFileClip' in txt:
                print(path)
                # print a snippet
                idx = txt.find('VideoFileClip')
                print(txt[max(0, idx-80):idx+200])
                raise SystemExit
print('not found')
