# fonts/*.ttf(원본, 저장소 밖) → fonts/*.woff2: 한글 2,350자(KS X 1001) + 영문 · 숫자 · 문장부호 + 갤러리 전체에 실제 쓰인 글자.
# 저장소에는 woff2 만 둔다. 실행: python3 scripts/fetch_fonts.py && python3 scripts/pack_fonts.py
import glob, os, re, io
from fontTools.ttLib import TTFont
from fontTools import subset
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ks = ''.join(bytes([a, b]).decode('euc-kr') for a in range(0xB0, 0xC9) for b in range(0xA1, 0xFF))
sym = ''.join(chr(c) for c in list(range(0x20, 0x7F)) + list(range(0xA0, 0x180)) + list(range(0x2000, 0x2070)) + list(range(0x2190, 0x21FF)) + list(range(0x2460, 0x24FF)) + list(range(0x25A0, 0x2600)) + list(range(0x3000, 0x3040)) + list(range(0x3131, 0x318F)) + list(range(0xFF01, 0xFF5F)))
used = set()
for f in glob.glob(os.path.join(ROOT, 'refs', '*.html')): used |= set(re.sub(r'data:[^)"\']+', '', open(f).read()))
text = ''.join(sorted(set(ks + sym) | used))
for p in sorted(glob.glob(os.path.join(ROOT, 'fonts', '*.ttf'))):
    out = p[:-4] + '.woff2'
    if os.path.exists(out) and '--all' not in __import__('sys').argv: continue
    f = TTFont(p); o = subset.Options(); o.flavor = 'woff2'; o.layout_features = ['*']; o.name_IDs = ['*']; o.notdef_outline = True
    s = subset.Subsetter(o); s.populate(text=text); s.subset(f); f.flavor = 'woff2'; f.save(out)
    print(os.path.basename(out), os.path.getsize(out) // 1024, 'KB')
