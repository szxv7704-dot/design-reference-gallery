# 장표에 쓰인 글꼴 원본을 google/fonts 저장소에서 받아 fonts/{가족}-{굵기}.ttf 로 둔다(OFL).
# 가변 글꼴은 필요한 굵기로 고정해 저장. 실행: python3 scripts/fetch_fonts.py
import json, os, re, sys, urllib.request, io
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEED = json.load(open(os.path.join(ROOT, 'fonts', 'needed.json')))   # {"Gothic A1": ["500","700"], ...}
API = 'https://api.github.com/repos/google/fonts/contents/ofl/'
RAW = 'https://raw.githubusercontent.com/google/fonts/main/ofl/'
def get(u):
    req = urllib.request.Request(u, headers={'User-Agent': 'fetch-fonts'})
    return urllib.request.urlopen(req, timeout=120).read()
lic = {}
for fam, weights in NEED.items():
    d = re.sub(r'[^a-z0-9]', '', fam.lower())
    base = fam.replace(' ', '')
    files = []
    for cand in [base + '[wght].ttf', base + '[wdth,wght].ttf', base + '-Regular.ttf']:
        try:
            urllib.request.urlopen(urllib.request.Request(RAW + d + '/' + urllib.request.quote(cand), method='HEAD', headers={'User-Agent': 'f'}), timeout=60); files.append(cand)
            if '[' in cand: break
        except Exception: pass
    if files and '[' not in files[0]:
        for nm in ['Thin', 'ExtraLight', 'Light', 'Medium', 'SemiBold', 'Bold', 'ExtraBold', 'Black']:
            try: urllib.request.urlopen(urllib.request.Request(RAW + d + '/' + base + '-' + nm + '.ttf', method='HEAD', headers={'User-Agent': 'f'}), timeout=60); files.append(base + '-' + nm + '.ttf')
            except Exception: pass
    if not files: print('파일 못 찾음', fam); continue
    var = [f for f in files if '[' in f and 'Italic' not in f]
    for w in weights:
        out = os.path.join(ROOT, 'fonts', '%s-%s.ttf' % (fam.replace(' ', ''), w))
        if os.path.exists(out): continue
        try:
            if var:
                f = TTFont(io.BytesIO(get(RAW + d + '/' + urllib.request.quote(var[0]))))
                axes = {a.axisTag: a for a in f['fvar'].axes}
                loc = {'wght': max(axes['wght'].minValue, min(axes['wght'].maxValue, int(w)))}
                for t, a in axes.items():
                    if t != 'wght': loc[t] = a.defaultValue
                instancer.instantiateVariableFont(f, loc, inplace=True); f.save(out)
            else:
                names = {'100': 'Thin', '200': 'ExtraLight', '300': 'Light', '400': 'Regular', '500': 'Medium', '600': 'SemiBold', '700': 'Bold', '800': 'ExtraBold', '900': 'Black'}
                cand = [f for f in files if f.endswith('-' + names[w] + '.ttf')] or ([f for f in files if f.endswith('-Regular.ttf')] if w == '400' else [])
                if not cand and len(files) == 1: cand = files
                if not cand: print('굵기 없음', fam, w, files[:6]); continue
                open(out, 'wb').write(get(RAW + d + '/' + urllib.request.quote(cand[0])))
            print('ok', fam, w)
        except Exception as e: print('실패', fam, w, e)
