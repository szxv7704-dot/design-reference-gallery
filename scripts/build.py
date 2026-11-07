# src/{번호}/ → refs/{번호}.html (인터넷 없이 도는 완성본)
#  글꼴: fonts/{가족}-{굵기}.woff2 에서 이 페이지에 쓰인 글자만 잘라 박아 넣는다
#        (OFL: 저작권 · 라이선스 이름표를 남기고 예약 이름은 바꾸며, 글꼴 앞에 고지 주석 — scripts/fontlic.py)
#  자산: assets/ 파일을 data: 로 · 외부 라이브러리: vendor/ 를 data: 로
#  덱 키트: /*@@KIT:B@@*/ = kit/deck.css + kit/B.css(주석 뺌) · /*@@KITJS@@*/ = kit/deck.js
# 실행: python3 scripts/build.py 99 100 … | all   (--out 폴더 로 다른 곳에 쓰기)
import base64, io, json, os, re, sys
from fontTools.ttLib import TTFont
from fontTools import subset
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fontlic
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
def face(fam, w, text, notes=None):
    p = os.path.join(ROOT, 'fonts', '%s-%s.woff2' % (fam.replace(' ', ''), w))
    if not os.path.exists(p): raise SystemExit('글꼴 없음: %s %s (scripts/fetch_fonts.py · pack_fonts.py)' % (fam, w))
    f = TTFont(p); o = subset.Options(); o.flavor = 'woff2'; o.layout_features = ['*']; o.name_IDs = fontlic.KEEP_NAME_IDS
    s = subset.Subsetter(o); s.populate(text=text + ''.join(chr(c) for c in range(32, 127))); s.subset(f)
    fontlic.clean(f)
    if notes is not None and fam not in notes: notes[fam] = fontlic.notice(fam, f)
    b = io.BytesIO(); f.flavor = 'woff2'; f.save(b)
    return '@font-face{font-family:"%s";font-weight:%s;font-display:block;src:url(data:font/woff2;base64,%s) format("woff2")}\n' % (fam, w, base64.b64encode(b.getvalue()).decode())
def importmap_three():
    V = os.path.join(ROOT, 'vendor', 'three')
    js = lambda p: 'data:text/javascript;base64,' + b64(os.path.join(V, p))
    return json.dumps({'imports': {
        'three': js('build/three.module.min.js'),
        'three/addons/loaders/FontLoader.js': js('examples/jsm/loaders/FontLoader.js'),
        'three/addons/geometries/TextGeometry.js': js('examples/jsm/geometries/TextGeometry.js'),
        'three/addons/environments/RoomEnvironment.js': js('examples/jsm/environments/RoomEnvironment.js')}})
def kit_css(fam):
    K = os.path.join(ROOT, 'kit')
    css = open(os.path.join(K, 'deck.css'), encoding='utf-8').read() + '\n' + open(os.path.join(K, fam + '.css'), encoding='utf-8').read()
    return re.sub(r'/\*.*?\*/\n?', '', css, flags=re.S)
def build(no, outdir, name=None):
    d = os.path.join(ROOT, 'src', str(no)); cfg = json.load(open(os.path.join(d, 'build.json')))
    s = open(os.path.join(d, 'page.html'), encoding='utf-8').read()
    s = re.sub(r'/\*@@KIT:([A-H])@@\*/', lambda m: kit_css(m.group(1)), s)
    if '/*@@KITJS@@*/' in s: s = s.replace('/*@@KITJS@@*/', open(os.path.join(ROOT, 'kit', 'deck.js'), encoding='utf-8').read())
    text = re.sub(r'@@[A-Z]+:[^@]+@@', '', s)
    notes = {}; faces = ''.join(face(f, w, text, notes) for f, w in cfg['fonts'])
    if notes: faces = ('/* 글꼴: 이 페이지에 쓰인 글자만 잘라 넣은 SIL Open Font License 1.1 글꼴(https://openfontlicense.org)\n   '
                       + '\n   '.join(notes.values()) + ' */\n') + faces
    s = s.replace('/*@@FONTS@@*/\n', faces, 1).replace('/*@@FONTS@@*/', faces, 1)
    s = re.sub(r'@@ASSET:([^@]+)@@', lambda m: 'data:%s;base64,%s' % (cfg['assets'][m.group(1)], b64(os.path.join(d, 'assets', m.group(1)))), s)
    if 'three' in cfg.get('vendor', []): s = s.replace('@@IMPORTMAP:three@@', importmap_three())
    os.makedirs(outdir, exist_ok=True); open(os.path.join(outdir, '%s.html' % (name or no)), 'w', encoding='utf-8').write(s)
    return len(s)
if __name__ == '__main__':
    a = sys.argv[1:]; outdir = os.path.join(ROOT, 'refs')
    if '--out' in a: i = a.index('--out'); outdir = a[i + 1]; del a[i:i + 2]
    if a == ['all']: a = sorted(os.listdir(os.path.join(ROOT, 'src')), key=lambda x: int(x) if x.isdigit() else 0)
    for no in a:
        if no.isdigit(): print(no, build(no, outdir))
