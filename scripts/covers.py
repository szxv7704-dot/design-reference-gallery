# 표지마다 10장 덱: 표지(원본 장표) + 본문 여덟 역할(구성 모음 src/flows/var.html 에서 표지마다 다른 조합) + 마무리.
#   covers/{번호}.html   넘겨 보는 덱(열 때 인터넷 필요: 글꼴 · 표지 장표를 이 사이트에서 불러옴)
#   covers/{번호}.css    그 표지의 색 · 글꼴을 입힌 스타일 묶음(AI가 만든 덱이 불러옴)
#   data/cover_decks.json  표지별 덱 목록(바탕 스타일 · 구성 조합) — 화면(scripts/gallery.py)과 catalog.md 가 읽는다
# 본문의 배치 문법은 그 표지의 분위기 스타일(kit/{A..H}.css)에서 빌리고, 색 · 글꼴은 data/covers.json 의 값으로 바꾼다.
# 어두운 분위기(G) · 분위기 없는 표지는 B(미니멀)를 바탕으로 쓴다(본문은 늘 밝은 바탕). 스타일의 상징 그림(나이테 · 막새 등)은 넣지 않는다.
# 실행: python3 scripts/covers.py   (kit.py 다음, gallery.py 앞)
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import kit, build
OUT = os.path.join(ROOT, 'covers')
rounds = {int(r['no']): r for r in json.load(open(os.path.join(ROOT, 'data', 'rounds.json'), encoding='utf-8'))}
COV = json.load(open(os.path.join(ROOT, 'data', 'covers.json'), encoding='utf-8'))['covers']
name = lambda r: re.sub(r'^레퍼런스\s*#\d+\s*', '', r['title'])
def mix(a, b, t):
    A, B = [int(a[i:i + 2], 16) for i in (1, 3, 5)], [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02X%02X%02X' % tuple(round(x + (y - x) * t) for x, y in zip(A, B))
have = {}
for fn in os.listdir(os.path.join(ROOT, 'fonts')):
    m = re.match(r'(.+)-(\d+)\.woff2$', fn)
    if m: have.setdefault(m.group(1), []).append(m.group(2))

IMG = {9, 11, 106}   # 장표만 떼어 띄울 수 없는 표지(무대가 픽셀 고정 · 눌러야 나타남): 원본 화면을 떠낸 그림(covers/img/)으로 띄운다
def base_of(no): f = rounds[no].get('family'); return f if f and f in 'ABCDEFH' else 'B'
def picks(i): return ''.join('abc'[(i + (i // 3) * j + (i // 9) * (j * j) + j) % 3] for j in range(len(kit.VAR['order'])))
def tokens(no, base):
    c = COV[str(no)]; fb = '"Apple SD Gothic Neo","Malgun Gothic",sans-serif'
    t = {'--ds-stage': mix(c['bg'], c['ink'], .14), '--ds-bg': c['bg'], '--ds-ink': c['ink'], '--ds-sub': mix(c['ink'], c['bg'], .42), '--ds-line': mix(c['ink'], c['bg'], .84),
         '--ds-accent': c['accent'], '--ds-accent2': c['base'],
         '--ds-font-title': '"%s",%s' % (c['title'], fb), '--ds-font-body': '"%s",%s' % (c['body'], fb), '--ds-font-num': '"%s","%s",%s' % (c['num'], c['body'], fb)}
    if base == 'A':   # 픽셀 게임: 판(surface)이 어두운 창이고 창 안 글자가 밝다
        t.update({'--ds-surface': mix(c['ink'], c['base'], .25), '--ds-c1': mix(c['ink'], c['base'], .25), '--ds-c2': c['base'], '--ds-c3': mix(c['base'], '#FFFFFF', .35),
                  '--ds-c4': mix(c['base'], '#FFFFFF', .68), '--ds-c5': mix(c['bg'], '#FFFFFF', .5)})
    else:
        t.update({'--ds-surface': mix(c['bg'], '#FFFFFF', .7), '--ds-c1': mix(c['base'], c['ink'], .4), '--ds-c2': c['base'], '--ds-c3': mix(c['base'], '#FFFFFF', .32),
                  '--ds-c4': mix(c['base'], '#FFFFFF', .62), '--ds-c5': mix(c['base'], c['bg'], .86)})
    return t
def css_of(no, base):
    c = COV[str(no)]; faces = ''
    for n in dict.fromkeys((c['title'], c['body'], c['num'])):
        key = n.replace(' ', '')
        if key not in have: raise SystemExit('fonts/ 에 없는 글꼴: %s (#%s)' % (n, no))
        faces += ''.join('@font-face{font-family:"%s";font-weight:%s;font-display:swap;src:url("../fonts/%s-%s.woff2") format("woff2")}\n' % (n, w, key, w) for w in sorted(have[key]))
    fam = kit.rd(kit.K, base + '.css').replace('url("img/', 'url("../kit/img/')
    over = ':root{' + ';'.join('%s:%s' % kv for kv in tokens(no, base).items()) + '}\n' \
           '/* 표지 장: 원본 표지 장표를 그대로 띄운다 */\n.slide.c-orig{padding:0;background:#111}.slide.c-orig::before,.slide.c-orig::after{content:none}\n' \
           '.slide.c-orig img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}\n.slide.c-orig iframe{position:absolute;inset:0;width:100%;height:100%;border:0;pointer-events:none}\n'
    head = '/* 표지 #%d %s 의 색 · 글꼴을 입힌 스타일 묶음(scripts/covers.py 가 만듦, 고치지 말 것). 배치 문법은 %s %s 에서 빌렸다\n   글꼴: SIL Open Font License 1.1, 저작권 고지는 %sfonts/LICENSES.md */\n' % (no, name(rounds[no]), base, kit.NAMES[base], kit.BASE)
    return head + faces + kit.rd(kit.K, 'deck.css') + '\n' + kit.rd(kit.K, 'parts.css') + '\n' + fam + '\n' + over
def body_of(no, pk):
    src, n, num = kit.flow_src('var'); out = []
    if no in IMG:   # 그림으로 띄우는 표지
        out.append('<!-- 1. 표지 -->\n<section data-pattern="cover" class="slide c-orig"><img src="img/%d.jpg" alt="%s 표지"></section>' % (no, name(rounds[no])))
    else:
        out.append('<!-- 1. 표지 -->\n<section data-pattern="cover" class="slide c-orig"><iframe src="../light/%02d.html?slide=" title="%s 표지" loading="eager"></iframe></section>' % (no, name(rounds[no])))
    for role, v in list(zip(kit.VAR['order'], pk)) + [('closing', 'a')]:
        m = re.search(r'<!-- \d+\. ([^\n]+?) -->\n(<section data-pattern="[\w-]+" data-role="%s" data-var="%s".*?</section>)' % (role, v), src, re.S)
        out.append('<!-- %d. %s -->\n%s' % (len(out) + 1, m.group(1), m.group(2)))
    s = '\n\n'.join(out)
    s = re.sub(r'\n?\s*@@SIG:\w+(?::\d+)?@@', '', s)   # 스타일의 상징 그림은 표지 덱에 넣지 않는다
    return re.sub(r'@@IMG:([\w.-]+)@@', lambda m: '../src/flows/img/' + m.group(1), s)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for i, no in enumerate(sorted(int(k) for k in COV)):
        base, pk = base_of(no), picks(i)
        kit.wr(os.path.join(OUT, '%d.css' % no), css_of(no, base))
        html = kit.HEAD % {'fam': base, 'title': '%s — 표지에서 넓힌 10장 덱' % name(rounds[no]), 'body': body_of(no, pk),
                           'css': '<link rel="stylesheet" href="%d.css">' % no, 'js': '<script src="../kit/v1/deck.js"></script>'}
        kit.wr(os.path.join(OUT, '%d.html' % no), html.replace('<body>', '<body>\n<!-- scripts/covers.py 가 만든 파일. 예시 내용은 가상 -->'))
        meta.append({'no': no, 'name': name(rounds[no]), 'base': base, 'picks': pk, 'family': rounds[no].get('family'),
                     'combo': [next(v['name'] for v in kit.VAR['roles'][r] if v['v'] == x) for r, x in zip(kit.VAR['order'], pk)]})
    kit.wr(os.path.join(ROOT, 'data', 'cover_decks.json'), json.dumps(meta, ensure_ascii=False, indent=1) + '\n')
    print('covers/', len(meta), '벌 · 조합', len({m['picks'] for m in meta}), '가지')
