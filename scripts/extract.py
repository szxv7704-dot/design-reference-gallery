# refs/{번호}.html(완성본) → src/{번호}/ (원본 소스)
#  page.html   : 완성본에서 ① 박아 넣은 글꼴(@font-face) ② 실시간 구글 글꼴 링크 ③ 큰 data: 그림 · 파일 ④ 외부 라이브러리 주소를 자리표시로 바꾼 것
#  assets/     : ③을 파일로
#  build.json  : 필요한 글꼴(가족 · 굵기) · 자산 목록 · 외부 라이브러리
# 실행: python3 scripts/extract.py 99 100 … | all
import base64, hashlib, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT = {'image/jpeg': 'jpg', 'image/png': 'png', 'image/webp': 'webp', 'image/gif': 'gif', 'image/svg+xml': 'svg', 'font/woff2': 'woff2', 'audio/mpeg': 'mp3', 'video/mp4': 'mp4', 'application/octet-stream': 'bin', 'text/javascript': 'js', 'application/json': 'json'}
FACE = re.compile(r'@font-face\{font-family:"([^"]+)";font-weight:(\d+);font-display:block;src:url\(data:font/woff2;base64,[A-Za-z0-9+/=]+\) format\("woff2"\)\}\n?')
GLINK = re.compile(r'<link\b[^>]*href="https://fonts\.(?:googleapis|gstatic)\.com[^"]*"[^>]*>\n?')
DATA = re.compile(r'data:([a-z]+/[a-z0-9.+-]+);base64,([A-Za-z0-9+/=]{1500,})')
CDN3 = re.compile(r'https://cdn\.jsdelivr\.net/npm/three@0\.160\.0/(build/three\.module\.js|examples/jsm/[A-Za-z/]+\.js|examples/jsm/)')
def script_ranges(s):
    return [(m.start(), m.end()) for m in re.finditer(r'<script\b[^>]*>.*?</script>', s, re.S)]
def inside(pos, rs): return any(a <= pos < b for a, b in rs)
def extract(no):
    s = open(os.path.join(ROOT, 'refs', '%s.html' % no), encoding='utf-8').read()
    out = os.path.join(ROOT, 'src', str(no)); os.makedirs(os.path.join(out, 'assets'), exist_ok=True)
    fonts = set(); assets = {}
    # ① 박아 넣은 글꼴: 첫 자리에 자리표시 하나만 남긴다
    first = [True]
    def face(m):
        fonts.add((m.group(1), m.group(2)))
        if first[0]: first[0] = False; return '/*@@FONTS@@*/\n'
        return ''
    s = FACE.sub(face, s)
    # ② 실시간 구글 글꼴(스크립트 문자열 안에 든 것은 '코드 복사'용이라 그대로 둔다)
    rs = script_ranges(s); parts = []; last = 0; placed = '/*@@FONTS@@*/' in s
    for m in GLINK.finditer(s):
        if inside(m.start(), rs): continue
        href = re.search(r'href="([^"]+)"', m.group(0)).group(1)
        for fam, w in re.findall(r'family=([^&:]+)(?::wght@([\d;]+))?', href):
            for x in (w or '400').split(';'): fonts.add((fam.replace('+', ' '), x))
        parts.append(s[last:m.start()]); parts.append('' if placed else '<style>/*@@FONTS@@*/</style>\n'); placed = True; last = m.end()
    parts.append(s[last:]); s = ''.join(parts)
    # ③ 큰 data: 자산
    def data(m):
        raw = base64.b64decode(m.group(2)); h = hashlib.sha1(raw).hexdigest()[:10]; name = '%s.%s' % (h, EXT.get(m.group(1), 'bin'))
        if name not in assets:
            open(os.path.join(out, 'assets', name), 'wb').write(raw); assets[name] = m.group(1)
        return '@@ASSET:%s@@' % name
    s = DATA.sub(data, s)
    # ④ 외부 라이브러리(스크립트 문자열 '코드 복사' 안이 아닌 실제 importmap 만)
    vendor = []
    m = re.search(r'<script type="importmap">.*?</script>', s, re.S)
    if m and CDN3.search(m.group(0)):
        imp = m.group(0)
        s = s[:m.start()] + '<script type="importmap">@@IMPORTMAP:three@@</script>' + s[m.end():]; vendor.append('three')
    open(os.path.join(out, 'page.html'), 'w', encoding='utf-8').write(s)
    json.dump({'fonts': sorted([list(f) for f in fonts]), 'assets': assets, 'vendor': vendor}, open(os.path.join(out, 'build.json'), 'w'), ensure_ascii=False, indent=1)
    return len(fonts), len(assets), vendor
if __name__ == '__main__':
    nos = sys.argv[1:]
    if nos == ['all']: nos = sorted([f[:-5] for f in os.listdir(os.path.join(ROOT, 'refs')) if f.endswith('.html')], key=lambda x: int(x))
    for no in nos: print(no, *extract(no))
