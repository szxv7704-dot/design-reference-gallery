# 덱 키트 만들기: kit/deck.css · kit/deck.js · kit/parts.css · kit/{계열}.css · kit/{계열}.design.md · src/flows/{흐름}.html 에서
#   kit/v1/{계열}.css        배포용 묶음(글꼴 @font-face + 공용 바탕 + 부품) — 채팅 AI가 만든 덱이 불러옴
#   kit/v1/deck.js           공용 엔진
#   kit/{계열}.html           성과 공유회 예시 덱 · kit/{계열}-plan.html 계획안 발표 (인터넷 없이 돎)
#   kit/{계열}.md             그 계열 하나로 덱을 만드는 채팅 AI용 지시서(첨부용)
#   data/kit_slides.json     예시 덱의 장 목록(흐름 · 장 · 기본 장표)
# 예시 덱 원본은 계열 공용(src/flows/)이고, 계열마다 다른 상징 부품은 @@SIG:…@@ 자리에 넣는다.
# 실행: python3 scripts/kit.py A B C D
#       python3 scripts/kit.py inline B 슬라이드.html [결과.html]   ← AI가 만든 덱을 인터넷 없이 도는 파일 하나로
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import build
BASE = 'https://szxv7704-dot.github.io/design-reference-gallery/'
K = os.path.join(ROOT, 'kit')
FAMS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
NAMES = {'A': '픽셀 게임', 'B': '미니멀 스튜디오', 'C': '경쾌한 놀이 오브젝트', 'D': '인쇄·종이 에디토리얼', 'E': '자연 재질', 'F': '관측·중계 인포그래픽', 'G': '어두운 콘셉트', 'H': '전통 공예·문양'}
# 계열마다 다른 것: 근거 장표 · 글꼴 역할 · 한 줄 소개 · 어울리는 자리 · 상징 부품(표지 · 목차 · 간지 · 맺음에 쓰는 이 계열의 얼굴)
META = {
 'A': {'refs': '#9 · #10 · #11 · #12 · #90', 'roles': ('Galmuri11', 'Galmuri11', 'Galmuri11'),
       'desc': '크림 바탕 위 남색 게임 창, 픽셀 글꼴. 강조는 빨강 낱말 하나와 창 안 금색 한 곳', 'fit': '학생 · 체험 행사, 가벼운 연수',
       'sig': '진행 칸(`.prog`)을 씁니다. 칸 수 = 섹션 수, 목차는 다음 칸 `.next`, 간지는 지난 칸 `.done` · 지금 칸 `.now`, 맺음은 모두 `.done`.'},
 'B': {'refs': '#19 · #26 · #28 · #37 · #46 · #116', 'roles': ('Gothic A1', 'IBM Plex Sans KR', 'IBM Plex Mono'),
       'desc': '전시관 모형대처럼 밝은 청백 무광. 주황은 한 장에 한 곳', 'fit': '어디에나 무난하다. 정하지 않았으면 이것',
       'sig': '모형대 매스(`.mass`)를 씁니다. 목차 · 간지의 `.lit` 층 = 지금 섹션(아래층이 1섹션). 맺음은 `.spot`.'},
 'C': {'refs': '#7 · #24 · #29 · #39 · #82', 'roles': ('Black Han Sans', 'IBM Plex Sans KR', 'Fredoka'),
       'desc': '하늘빛 흰 바탕에 장난감 블록, 굵은 제목. 빨강 강조 한 곳', 'fit': '유아 · 초등, 밝은 분위기의 행사',
       'sig': '블록 탑(`.blocks`)을 씁니다. 블록 수 = 섹션 수(아래가 1섹션), 간지는 지금 층까지만 놓고 남은 층은 `.ghost`, 맺음은 `.flag`.'},
 'D': {'refs': '#4 · #27 · #32 · #60 · #62', 'roles': ('Noto Serif KR', 'IBM Plex Sans KR', 'Noto Serif KR'),
       'desc': '백상지에 먹 명조 제목, 남색과 주홍 2도. 이중 괘선으로 지면을 짠다', 'fit': '계획안 · 정책 보고, 차분한 자리',
       'sig': '판 번호(`.reg`)를 씁니다. 큰 명조 숫자 하나에 주홍 판이 4px 어긋나는 곳은 덱 전체에서 간지뿐, 재단 표시(`.crop`)도 간지에만.'},
 'E': {'refs': '#17 · #91', 'roles': ('Hahmlet', 'IBM Plex Sans KR', 'Hahmlet'),
       'desc': '밝은 회녹 종이에 따뜻한 나무색 농담, 명조 제목. 청록 강조 한 곳', 'fit': '환경 · 생태 · 마을 교육, 차분하고 따뜻한 자리',
       'sig': '나무 단면 그림(`.rings`, 이미지)을 씁니다. 표지 · 목차 · 맺음은 다 자란 단면 `.rings`, 간지는 그 섹션까지 자란 단면 `.rings s1`~`s5`(다섯 단계. 섹션이 5개가 아니면 비율로 고름: 4개 중 2번째 → `s3`).'},
 'F': {'refs': '#20 · #25 · #31 · #52 · #71', 'roles': ('Gothic A1', 'Gothic A1', 'Saira Semi Condensed'),
       'desc': '맑은 청백 바탕에 남색 기록판, 좁은 숫자 글꼴. 빨강 강조 한 곳', 'fit': '실적 · 통계가 많은 성과 보고, 체육 · 진로 행사',
       'sig': '구간 띠(`.lane`)를 씁니다. 칸 수 = 섹션 수, 지난 구간 `.done` · 지금 구간 `.now` · 남은 구간 `.ghost`.'},
 'G': {'refs': '#18 · #30 · #74 · #103', 'roles': ('Noto Serif KR', 'Noto Sans KR', 'IBM Plex Mono'),
       'desc': '깊은 남색 밤하늘에 따뜻한 흰 글자, 명조 제목. 금빛 강조 한 곳', 'fit': '저녁 행사 · 비전 선포, 불을 끄고 하는 발표(밝은 회의실에는 맞지 않음)',
       'sig': '밤하늘과 별자리 그림(이미지)을 씁니다. 표지 · 목차 · 간지 · 맺음의 바탕은 밤하늘(공통 CSS가 넣음)이고, 그 위에 별자리 겹 `.stars`를 놓습니다: 표지 · 맺음은 다 이어진 `.stars all`, 목차 · 간지는 그 섹션까지 이어진 `.stars s1`~`s5`(다섯 단계, 섹션 수에 맞춰 비율로).'},
 'H': {'refs': '#58 · #59 · #110', 'roles': ('Nanum Myeongjo', 'Noto Sans KR', 'Nanum Myeongjo'),
       'desc': '밝은 한지에 먹 명조 제목, 면마다 쌍변, 진녹 농담. 주홍 강조 한 곳', 'fit': '역사 · 문화 · 지역 행사, 격식 있는 자리',
       'sig': '수막새 그림(`.tiles`, 이미지)을 씁니다. 표지는 큰 막새 `.tiles big`, 목차 · 간지는 처마 줄 `.tiles s1`~`s5`(그 섹션의 막새에 주홍 고리. 다섯 단계, 섹션 수에 맞춰 비율로), 맺음은 처마 끝 `.tiles roof`.'},
}
rd = lambda *p: open(os.path.join(*p), encoding='utf-8').read()
def wr(p, s): os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w', encoding='utf-8').write(s)
def fonts_of(fam): return json.load(open(os.path.join(ROOT, 'src', 'kit-' + fam, 'build.json')))['fonts']
LINK = lambda fam: '<link rel="stylesheet" href="%skit/v1/%s.css">' % (BASE, fam)
SCRIPT = '<script src="%skit/v1/deck.js"></script>' % BASE
PATTERNS = json.load(open(os.path.join(ROOT, 'data', 'patterns.json'), encoding='utf-8'))
FLOWS = json.load(open(os.path.join(ROOT, 'data', 'flows.json'), encoding='utf-8'))
PNAME = {p['id']: p['name'] for p in PATTERNS}
# 예시 덱: 흐름마다 하나 + 'more'(같은 흐름의 다른 덱 — 연수 2 · 3차시). id = src/flows/{id}.html, deck = 파일 이름 꼬리
DECKS = []
for _f in FLOWS:
    if _f['deck'] is not None: DECKS.append({'id': _f['id'], 'name': _f['name'], 'deck': _f['deck'], 'flow': _f['id']})
    for _m in _f.get('more', []): DECKS.append({'id': _m['id'], 'name': _m['name'], 'deck': _m['deck'], 'flow': _f['id']})

# ── 상징 부품: 계열마다 다른 표지 · 목차 · 간지 · 맺음의 얼굴 ──
def sig(fam, kind, i=0, n=5, num=''):
    """kind = cover | toc | divider | close, i = 지금 섹션(1부터), n = 섹션 수, num = 표지에 놓는 숫자(D)"""
    cells = lambda f: ''.join('<i%s></i>' % (' class="%s"' % f(k) if f(k) else '') for k in range(1, n + 1))
    hid = ' aria-hidden="true"'
    if fam == 'A':
        f = {'cover': lambda k: '', 'toc': lambda k: 'next' if k == i else '', 'divider': lambda k: 'done' if k < i else 'now' if k == i else '', 'close': lambda k: 'done'}[kind]
        return '<div class="prog"%s>%s</div>' % (hid, cells(f))
    if fam == 'B':
        if kind == 'close': return '<div class="spot"%s></div>' % hid
        at = (n + 1) // 2 if kind == 'cover' else i
        return '<div class="mass"%s>%s</div>' % (hid, cells(lambda k: 'lit' if k == at else ''))
    if fam == 'C':
        f = {'cover': lambda k: '', 'toc': lambda k: 'now' if k == i else '', 'divider': lambda k: 'now' if k == i else 'ghost' if k > i else '', 'close': lambda k: ''}[kind]
        return '<div class="blocks%s"%s>%s</div>' % (' flag' if kind == 'close' else '', hid, cells(f))
    if fam == 'F':   # 구간 띠: 목차는 지금 칸 .now, 간지는 지난 칸 .done · 지금 .now · 남은 칸 .ghost, 맺음은 모두 .done
        f = {'cover': lambda k: '', 'toc': lambda k: 'now' if k == i else '', 'divider': lambda k: 'done' if k < i else 'now' if k == i else 'ghost', 'close': lambda k: 'done'}[kind]
        return '<div class="lane"%s>%s</div>' % (hid, cells(f))
    if fam in 'EGH':   # 그림(kit/img/, 근거 키트 장표에서 떠낸 이미지). 상태 그림은 다섯 단계라 섹션 수에 맞춰 고른다
        st = 's%d' % max(1, min(5, round(i * 5 / n))) if i else ''
        if fam == 'E': return '<div class="rings%s"%s></div>' % (' ' + st if kind == 'divider' else '', hid)
        if fam == 'G': return '<div class="stars %s"%s></div>' % (st if kind in ('toc', 'divider') else 'all', hid)
        return '<div class="tiles %s"%s></div>' % ({'cover': 'big', 'close': 'roof'}.get(kind, st), hid)
    if fam == 'D':
        if kind == 'divider': return '<div class="reg is-off"%s><b>%02d</b><i class="crop"></i></div>' % (hid, i)
        return '<div class="reg"%s><b>%s</b></div>' % (hid, {'cover': num, 'toc': '%02d' % i, 'close': '끝'}[kind])
def flow_src(fid):
    s = rd(ROOT, 'src', 'flows', fid + '.html'); m = re.match(r'<!-- 흐름: (.+?) · 섹션 (\d+) · 표지 숫자 (\S+)', s)
    return s.split('-->', 1)[1].strip(), int(m.group(2)), m.group(3)
def sections(fam, fid):
    body, n, num = flow_src(fid)
    return re.sub(r'@@SIG:(\w+)(?::(\d+))?@@', lambda m: sig(fam, m.group(1), int(m.group(2) or 0), n, num), body)
def slides_of(fid):
    """[(장 번호, 기본 장표 id, 원본 주석의 장 이름, 그 장의 원본 HTML)]"""
    body = flow_src(fid)[0]; out = []
    for m in re.finditer(r'<!-- (\d+)\. (.+?) -->\n(<section data-pattern="([\w-]+)".*?</section>)', body, re.S):
        out.append((int(m.group(1)), m.group(4), m.group(2), m.group(3)))
    return out
HEAD = '''<!DOCTYPE html>
<html lang="ko" data-kit="%(fam)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
%(css)s
</head>
<body>
<div class="deck"><main class="deck-stage">

%(body)s

</main></div>
%(js)s
</body>
</html>
'''
def page(fam, fid):
    name = next(f['name'] for f in DECKS if f['id'] == fid)
    return HEAD % {'fam': fam, 'title': '덱 키트 %s · %s — %s 예시 덱' % (fam, NAMES[fam], name), 'body': sections(fam, fid),
                   'css': '<style>\n/*@@FONTS@@*/\n/*@@KIT:%s@@*/\n</style>' % fam, 'js': '<script>\n/*@@KITJS@@*/\n</script>'}
def shell(fam=None):
    """AI가 채울 빈 뼈대. fam 이 없으면 계열 자리는 {계열}"""
    link = LINK(fam) if fam else LINK('{계열}')
    return HEAD % {'fam': fam or '{계열}', 'title': '발표 제목', 'body': '<!-- 여기에 <section class="slide"> 를 장 수만큼 -->',
                   'css': '<!-- 이 계열의 공통 CSS(글꼴 · 색 · 부품). 주소를 바꾸지 마세요 -->\n' + link +
                          '\n<style>\n/* === 추가 부품: 새 클래스가 꼭 필요할 때만 이 줄 아래에(토큰 변수만 사용) === */\n</style>',
                   'js': '<!-- 동작 엔진. 주소를 바꾸지 마세요 -->\n' + SCRIPT}

def hosted(fam):
    faces = ''.join('@font-face{font-family:"%s";font-weight:%s;font-display:swap;src:url("../../fonts/%s-%s.woff2") format("woff2")}\n' % (f, w, f.replace(' ', ''), w) for f, w in fonts_of(fam))
    head = '/* %s %s — 덱 키트 v1 배포용 묶음(scripts/kit.py 가 만듦, 고치지 말 것)\n   글꼴: SIL Open Font License 1.1, 저작권 고지는 %sfonts/LICENSES.md */\n' % (fam, NAMES[fam], BASE)
    # 계열 그림(kit/img/)은 배포판(kit/v1/)에서 한 칸 위에 있다
    wr(os.path.join(K, 'v1', fam + '.css'), head + faces + rd(K, 'deck.css') + '\n' + rd(K, 'parts.css') + '\n' + rd(K, fam + '.css').replace('url("img/', 'url("../img/'))
    wr(os.path.join(K, 'v1', 'deck.js'), rd(K, 'deck.js'))

def parts(fam, sample):
    """계열 CSS + 공용 부품의 '── 이름 ──' 묶음마다 클래스 목록과, 예시 덱에서 그 클래스를 처음 쓴 태그"""
    css = rd(K, fam + '.css') + '\n' + rd(K, 'parts.css'); out = []
    for m in re.finditer(r'/\* ── (.+?) ─+.*?\*/\n(.*?)(?=/\* ── |\Z)', css, re.S):
        title, body = m.group(1).strip(), re.sub(r'/\*.*?\*/', '', m.group(2), flags=re.S)
        sel = ' '.join(re.findall(r'([^{}]+)\{', body))
        cls = []
        for c in re.findall(r'\.([a-z][a-z0-9-]*)', sel):
            if c not in cls: cls.append(c)
        rows = []
        for c in cls:
            ex = re.search(r'<[a-z0-9]+[^>]*class="(?:[^"]* )?%s(?: [^"]*)?"[^>]*>' % re.escape(c), sample)
            rows.append('- `.%s`' % c + (' — 예: `%s`' % (ex.group(0)[:140] + ('…' if len(ex.group(0)) > 140 else '')) if ex else ''))
        out.append('**%s**\n%s' % (title, '\n'.join(rows)))
    return '\n\n'.join(out)

# ── AI용 안내: 계열 공통(guide.md · 첫 화면) 또는 계열 하나(kit/{계열}.md) ──
SNIPPET_FROM = ['plan', 'share']   # 기본 장표의 견본 코드를 찾는 순서
def samples(pid):
    """그 기본 장표의 견본 장: [(흐름 id, (장 번호, 기본 장표 id, 장 이름, HTML))]. 질문은 보기형 + 답 공개형 둘"""
    hit = [(fid, s) for fid in SNIPPET_FROM for s in slides_of(fid) if s[1] == pid]
    if not hit: return []   # 예시 덱에 쓰이지 않은 기본 장표(부품은 parts.css 에 있다)
    if pid == 'ask': return [h for h in hit if 'a-a' not in h[1][3]][:1] + [h for h in hit if 'a-a' in h[1][3]][:1]
    return hit[:1]
def code_of(fam, fid, s):
    _, n, num = flow_src(fid)
    return re.sub(r'@@SIG:(\w+)(?::(\d+))?@@', (lambda m: sig(fam, m.group(1), int(m.group(2) or 0), n, num)) if fam else
                  (lambda m: '<!-- 상징 부품: 7의 계열 표에서 %s 코드 -->' % {'cover': '표지', 'toc': '목차', 'divider': '간지', 'close': '맺음'}[m.group(1)]), s[3])
def part_md(p): return ' '.join('`%s`' % w if w.startswith('.') else w for w in p['part'].replace('(', '( ').replace(')', ' )').split()).replace('( ', '(').replace(' )', ')')
def snippets(fam=None):
    L = []
    for p in PATTERNS:
        L += ['### %s · `%s`' % (p['name'], p['id']), '', '- 이런 내용일 때: %s' % p['when'], '- 내용 조건: %s. 넘치면: %s' % (p['cond'], p['overflow']),
              '- 부품: %s%s' % (part_md(p), (' — ' + p['note']) if p['note'] else ''), '']
        for fid, s in samples(p['id']): L += ['```html', code_of(fam, fid, s), '```', '']
    return '\n'.join(L)

def guide(fam=None):
    one = bool(fam)
    T = lambda rows: '\n'.join('| ' + ' | '.join(r) + ' |' for r in rows)
    L = []
    L += ['## 0. 당신(AI)의 일', '',
          '사용자가 준 **문서**(한글 계획안 · 연수 강의안 · 성과 보고 등)의 내용으로 **16:9 발표 덱 HTML 파일 하나**를 만듭니다.',
          '이 안내의 **기본 장표(3)** · **흐름(4)** · **견본 코드(8)**를 재료로 씁니다. 색 · 글꼴 · 부품 모양은 뼈대(6)의 두 줄이 인터넷에서 불러오므로, **당신이 쓰는 것은 `<section class="slide">`들뿐**입니다.', '',
          '## 1. 진행 순서', '',
          '1. **문서를 읽습니다.** 문서가 없으면 달라고 합니다. 발표 자리(계획안 발표 · 성과 공유회 · 설명회 · 연수)와 발표 시간을 모르면 짧게 묻습니다.',
          '2. **흐름을 고릅니다(4).** 문서 종류에 맞는 흐름의 자리 순서를 따르되, 문서에 없는 자리는 뺍니다.',
          '3. **문단마다 기본 장표를 고릅니다(3).** 한 장에 기본 장표 하나. 내용 조건을 넘치면 장을 나눕니다.',
          '4. **분위기 계열을 정합니다(5).** 사용자가 정하지 않았으면 B를 권하고 한 번 묻습니다.' if not one else '4. 분위기 계열은 **%s %s**입니다.' % (fam, NAMES[fam]),
          '5. **구성안을 먼저 보여 주고 확인을 받습니다.** 장마다 `자리 | 기본 장표 | 제목 한 문장 | 쓸 내용(문서의 어느 부분) | 수치와 출처`를 표 한 줄로. 이때 코드를 쓰지 않습니다. 사용자가 "구성 확인 없이 바로"라고 했으면 건너뜁니다.',
          '6. 확인을 받으면 HTML을 만들고, 점검(9)을 거쳐 내보냅니다.', '',
          '## 2. 반드시 지킬 것', '',
          '1. **문서에 없는 숫자 · 연도 · 예산 · 이름 · 출처를 지어내지 않습니다.** 비어 있으면 묻거나 그 장을 뺍니다. 문서에 없는 사실을 넣고 싶으면 구성안에 \'추가 사실\'로 따로 적어 확인을 받습니다.',
          '2. **한 장에 기본 장표 하나.** 도식 두 개가 필요하면 두 장으로 나눕니다. 글자를 줄여 한 장에 밀어 넣지 않습니다.',
          '3. 본문 장은 `머리말(.kicker) + 제목(.title) + 부품` 순서입니다. **제목은 결론 한 문장**, 두 줄 이내. "현황" 같은 이름표는 머리말에 씁니다. 한 문장 · 질문 · 할 일 장만 제목 없이 머리말 아래에 부품을 둡니다.',
          '4. 수치가 있는 장에는 출처(`.src`)를 씁니다.',
          '5. **강조색은 한 장에 한 곳**: 제목의 `<em>` 하나 또는 부품의 `.is-key` 하나(둘 다 쓰면 같은 내용을 가리켜야 함).',
          '6. **클래스는 견본 코드(8)에 나온 것만** 씁니다. 없는 클래스는 모양이 없어 배치가 무너집니다. 새 부품이 꼭 필요하면 뼈대 `<style>`의 \'추가 부품\' 줄 아래에 토큰 변수(`--ds-*`)만으로 정의합니다.',
          '7. 뼈대의 공통 파일 두 줄(`<link>` · `<script src>`)은 주소 한 글자도 바꾸지 않습니다. 공통 CSS · 엔진을 HTML 안에 옮겨 쓰거나 `@font-face`를 새로 쓰지 않습니다.',
          '8. 장 번호 · 쪽 표시 · 점은 쓰지 않습니다. 엔진이 채웁니다(`<span class="page-no"></span>`는 빈 칸 그대로).',
          '9. 무대는 1920 × 1080이고 화면에 맞게 통째로 줄어듭니다. 글자 크기를 바꾸지 않습니다. 머리말과 두 줄 제목 아래 **본문 높이는 약 600~680px**이고 넘친 부분은 잘립니다. 넘치면 문장을 줄이거나 장을 나눕니다.',
          '10. 인라인 `style`은 값 전달에만 씁니다: 막대 `--v`(가장 큰 값 = 100) · 목표선 `--t` · 간트 `--from` `--to`(1~12월) · 체계 갈래 수 `--n` · 화면 짚기 번호 자리 `--x` `--y`(%).',
          '11. **그림을 코드로 그리지 않습니다.** SVG · CSS · 캔버스로 사물 · 인물 · 풍경 · 캐릭터 · 지도를 그리지 마세요. 사진 · 화면 캡처는 사용자가 준 이미지를 `.ph` 안에 `<img>`로 넣고, 없으면 `<div class="ph" data-need="사진 자리 · 4:3 · 무슨 장면"></div>`로 자리만 두고 무엇이 필요한지 말해 줍니다.',
          '12. 누를 때마다 하나씩 보이는 장(`data-steps` + `data-step`)은 덱 전체에서 1~3장. 같은 기본 장표가 세 장 넘게 연달아 나오지 않게 합니다.', '',
          '## 3. 기본 장표 23가지 (내용의 모양으로 고릅니다)', '',
          T([['기본 장표', '`id`', '문서에서 이런 내용이면', '내용 조건', '부품']] + [['---'] * 5] +
            [[p['name'], '`%s`' % p['id'], p['when'], p['cond'], part_md(p)] for p in PATTERNS]), '',
          '**고르는 순서** — 한 문단이 둘 이상에 맞으면 위에서부터 먼저 맞는 것:', '',
          '1. 숫자가 주인공이면 수 묶음(하나면 큰 숫자, 시간 축이 있으면 추이, 합이 100%면 구성비, 나머지는 막대 비교).',
          '2. 날짜가 주인공이면 일정.',
          '3. 두 쪽이 맞서면 둘 비교, 같은 것이 달라졌으면 전→후.',
          '4. 차례가 있으면 순서·단계, 위아래가 있으면 체계, 갈래만 있으면 묶음·분류.',
          '5. 칸이 3열 이상 필요하면 표.',
          '6. 어디에도 안 맞으면 항목. 항목이 한 개면 한 문장.', '',
          '## 4. 흐름 (문서 종류에 맞는 자리 순서)', '',
          '자리 이름은 머리말(`.kicker`)과 목차에 씁니다. 장 수는 내용이 정하고, 문서에 없는 자리는 뺍니다.', '']
    for f in FLOWS:
        L += ['**%s** — %s%s' % (f['name'], f['say'], ' · 예시 덱 %skit/%s%s.html' % (BASE, fam or 'B', f['deck']) if f['deck'] is not None else ''), '',
              T([['자리', '기본 장표']] + [['---'] * 2] + [[s[0], ' · '.join(PNAME[x] for x in s[1])] for s in f['slots']]), '']
    if one:
        L += ['## 5. 분위기 계열: %s %s' % (fam, NAMES[fam]), '', '%s. 어울리는 자리: %s. 자세한 규칙은 아래 \'디자인 규칙\'.' % (META[fam]['desc'], META[fam]['fit']), '']
    else:
        L += ['## 5. 분위기 계열 여덟 (겉모습만 다르고 부품 이름은 같습니다)', '',
              T([['계열', '겉모습', '어울리는 자리', '자세한 규칙 · 지시서']] + [['---'] * 4] +
                [['**%s %s**' % (f, NAMES[f]), META[f]['desc'], META[f]['fit'], '%skit/%s.md' % (BASE, f)] for f in FAMS]), '',
              '계열을 정하면 그 계열의 지시서(위 주소)를 읽을 수 있을 때 읽고 \'디자인 규칙\'을 따릅니다. 읽을 수 없으면 이 안내만으로 만듭니다.', '']
    L += ['## 6. HTML 뼈대', '', '```html', shell(fam).strip(), '```', '',
          '- `{계열}` 두 곳을 A ~ H 중 하나로 바꿉니다.' if not one else '- 공통 파일 두 줄은 그대로 둡니다.',
          '- 열 때 인터넷이 필요합니다. AI 화면 안 미리보기에서 색 · 모양이 안 보여도 고치지 마세요(바깥 파일을 막는 미리보기가 있습니다). 내려받아 브라우저로 열면 정상입니다.', '',
          '## 7. 상징 부품 (표지 · 목차 · 간지 · 맺음에 넣는 계열의 얼굴)', '']
    if one:
        L += ['이 계열은 ' + META[fam]['sig'], '']
    else:
        L += ['견본 코드(8)의 `<!-- 상징 부품 -->` 자리에 고른 계열의 코드를 넣습니다. 아래는 섹션이 5개이고 지금 2섹션일 때입니다. A · B · C · F는 칸(`<i>`) 수 = 섹션 수(5개까지), E · G · H는 그림이라 칸이 없고 상태 클래스(`s1`~`s5`)만 바꿉니다.', '',
              T([['계열', '표지', '목차(지금 2섹션)', '간지(지금 2섹션)', '맺음']] + [['---'] * 5] +
                [['%s' % f] + ['`%s`' % sig(f, k, 2, 5, '2027') for k in ('cover', 'toc', 'divider', 'close')] for f in FAMS]), '',
              '\n'.join('- %s: %s' % (f, META[f]['sig']) for f in FAMS), '']
    L += ['## 8. 기본 장표별 견본 코드', '', '문구는 모두 가상 예시입니다. **구조와 클래스만 가져오고 문구는 하나도 남기지 않습니다.**', '', snippets(fam),
          '## 9. 출력과 점검', '',
          '- 결과는 **`.html` 파일 하나**(UTF-8)로 줍니다. 파일을 만들 수 있는 기능(아티팩트 · 캔버스 · 파일 첨부)이 있으면 그것으로, 없을 때만 HTML 전체를 코드 블록 하나로 출력합니다.',
          '- `...`, "(생략)", "(이하 동일)"을 쓰지 않습니다. `<!DOCTYPE html>`부터 `</html>`까지 전부 씁니다.', '',
          '내보내기 전에 하나씩 확인합니다.', '',
          '1. 문서에 없고 확인도 받지 않은 숫자 · 사실이 없는가? 수치가 있는 장마다 `.src`가 있는가?',
          '2. 장마다 기본 장표가 하나이고, 내용 조건(항목 수 · 줄 수)을 넘지 않는가?',
          '3. 제목이 결론 한 문장이고 두 줄 이내인가? 강조(`<em>` · `.is-key`)가 장마다 한 곳인가?',
          '4. 쓴 클래스가 모두 견본 코드(8) 또는 \'추가 부품\' 칸에 있는가? 인라인 style은 허용된 값뿐인가? 코드로 그린 그림이 없는가?',
          '5. 공통 파일 두 줄이 그대로이고, 장 번호 · 쪽 표시를 손으로 쓰지 않았는가?',
          '6. 견본의 예시 문구가 남아 있지 않은가? 생략 없이 끝까지 썼는가?',
          '7. 사진 · 캡처 자리(`data-need`)가 있으면, 어떤 이미지가 필요한지 사용자에게 목록으로 알려 주었는가?', '']
    return '\n'.join(L)

def md(fam):
    sample = '\n'.join(sections(fam, f['id']) for f in DECKS)
    lic = rd(ROOT, 'fonts', 'LICENSES.md')
    fl = [l for l in lic.splitlines() if l.startswith('| ') and any(l.startswith('| %s ' % f.replace(' ', '')) for f, _ in fonts_of(fam))]
    eng = re.match(r'/\*(.*?)\*/', rd(K, 'deck.js'), re.S).group(1).strip()
    roles = META[fam]['roles']
    L = ['# %s %s — 발표 덱 지시서 (채팅 AI용)' % (fam, NAMES[fam]), '',
         '> 이 파일을 **Claude · ChatGPT 같은 채팅 AI**에게 자기 문서와 함께 주면, 문서 내용을 이 디자인의 16:9 발표 덱으로 만들어 주도록 쓴 지시서입니다.',
         '> 디자인 레퍼런스 갤러리(%s)의 %s 계열 장표(%s)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.' % (BASE, fam, META[fam]['refs']), '',
         '## 사용법 (사람이 읽는 안내)', '',
         '1. 채팅 AI 대화창에 **이 파일과 발표할 문서**(한글 · PDF · 붙여 넣은 글)를 넣습니다.',
         '2. 어떤 자리인지 말합니다. 예) "이 계획안으로 10분짜리 발표 덱을 만들어 줘. 결과는 .html 파일로."',
         '3. AI가 먼저 **장별 구성안**을 보여 줍니다. 고칠 곳을 말하거나 "좋아, 만들어 줘".',
         '4. 받은 `.html`을 내려받아 더블클릭합니다. → · Space로 넘기고, F는 전체 화면, 인쇄하면 장마다 한 쪽(16:9) PDF가 됩니다.',
         '5. 고칠 곳은 "3장 제목을 ○○로"처럼 말합니다. 코드가 끊기면 "끊긴 곳부터 이어서".', '',
         '알아 둘 점',
         '- 열 때 **인터넷이 필요**합니다(공통 CSS · 엔진 · 글꼴을 `szxv7704-dot.github.io`에서 불러옴). 인터넷이 막힌 곳에서 발표하려면 저장소에서 `python3 scripts/kit.py inline %s 슬라이드.html`을 실행해 모든 것이 파일 안에 든 판을 만드세요.' % fam,
         '- 수치는 AI가 지어내지 않도록 적어 두었지만, **받은 덱의 숫자를 원문과 꼭 대조**하세요.',
         '- 개인정보(학생 이름 · 사진 등)는 AI에게 넣지 마세요.', '',
         '## 라이선스', '',
         '- 글꼴: 모두 SIL Open Font License 1.1(전문 %sfonts/OFL.txt). 이 계열이 쓰는 글꼴의 저작권 고지:' % BASE, '',
         '| 글꼴 | 굵기 | 저작권 | 예약 이름 | 라이선스 |', '|---|---|---|---|---|', *fl, '',
         '- 공통 CSS · 엔진 · 이 지시서: 디자인 레퍼런스 갤러리 저장소의 일부(가상 예시 자료).', '',
         '---', '', '# ▼▼▼ 여기부터 AI에게 주는 지시서 ▼▼▼', '',
         '(위의 "사용법"과 "라이선스"는 사람을 위한 안내입니다. AI는 아래를 따르세요.)', '',
         guide(fam), '---', '',
         '## 디자인 규칙 (`%s` design.md)' % fam, '', '````markdown', rd(K, fam + '.design.md').strip(), '````', '',
         ('- 글꼴: 모든 글자(제목 · 본문 · 숫자) %s' if len(set(roles)) == 1 else '- 글꼴: 제목 %s · 본문 %s · 숫자 %s') % tuple(
             '%s(%s)' % (n, '/'.join(w for f, w in fonts_of(fam) if f == n)) for n in (roles[:1] if len(set(roles)) == 1 else roles)) + '. 공통 CSS가 불러오므로 설치하지 않아도 됩니다.',
         '- 글꼴은 변수로만 지정합니다: `var(--ds-font-title)` · `var(--ds-font-body)` · `var(--ds-font-num)`(숫자 · 영문에만).', '', '---', '',
         '## 부품 사전 (이 계열 CSS에 정의된 클래스 전부)', '',
         '"예"는 예시 덱에서 그 클래스를 처음 쓴 태그입니다. 공용: `.slide`(장 하나) · `data-steps="n"`(장) + `data-step="k"`(안의 요소, 누를 때마다 하나씩) · `.page-no`(빈 칸, 엔진이 채움).', '',
         parts(fam, sample), '', '---', '',
         '## 참고: 엔진 사용법', '', '```text', eng, '```', '',
         '부품 모양 · 크기가 궁금하면 `%skit/v1/%s.css`를 봅니다(HTML에 옮겨 쓰지 마세요).' % (BASE, fam), '']
    wr(os.path.join(K, fam + '.md'), '\n'.join(L))

def write_guide():
    L = ['# 디자인 레퍼런스 — AI용 안내', '',
         '> 이 문서는 **채팅 AI가 읽고 따르는 안내**입니다. 사용자가 이 문서(또는 %s 주소)와 자기 문서를 주면, 아래를 따라 16:9 발표 덱 HTML을 만듭니다.' % BASE,
         '> 모든 예시 내용은 가상입니다. `scripts/kit.py`가 만든 파일이므로 손으로 고치지 않습니다.', '', guide(), '']
    wr(os.path.join(ROOT, 'guide.md'), '\n'.join(L)); return len('\n'.join(L).encode('utf-8'))

def write_slides():
    out = []
    for f in DECKS:
        for n, pid, title, _ in slides_of(f['id']):
            out.append({'flow': f['flow'], 'id': f['id'], 'flow_name': f['name'], 'n': n, 'pattern': pid, 'title': title, 'deck': f['deck']})
    wr(os.path.join(ROOT, 'data', 'kit_slides.json'), json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    return len(out)

def inline(fam, src, out):
    s = open(src, encoding='utf-8').read()
    if LINK(fam) not in s or SCRIPT not in s: raise SystemExit('공통 파일 두 줄(<link> · <script src>)을 찾지 못했습니다: ' + src)
    s = s.replace(LINK(fam), '<style>\n/*@@FONTS@@*/\n' + build.kit_css(fam) + '\n</style>').replace(SCRIPT, '<script>\n' + rd(K, 'deck.js') + '\n</script>')
    text = re.sub(r'<script>.*?</script>', '', s, flags=re.S)
    notes = {}; faces = ''.join(build.face(f, w, text, notes) for f, w in fonts_of(fam))
    faces = '/* 글꼴: SIL Open Font License 1.1 (https://openfontlicense.org)\n   ' + '\n   '.join(notes.values()) + ' */\n' + faces
    open(out, 'w', encoding='utf-8').write(s.replace('/*@@FONTS@@*/', faces, 1))
    print('인터넷 없이 도는 파일:', out, os.path.getsize(out) // 1024, 'KB')

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['inline']:
        fam, src = a[1], a[2]; inline(fam, src, a[3] if len(a) > 3 else re.sub(r'\.html?$', '', src) + '-오프라인.html')
    else:
        print('data/kit_slides.json', write_slides())
        for fam in a or FAMS:
            hosted(fam); md(fam)
            sizes = [build.build('kit-' + fam, K, fam + f['deck'], page=page(fam, f['id'])) // 1024 for f in DECKS]
            print(fam, 'v1/%s.css' % fam, '%s.md' % fam, os.path.getsize(os.path.join(K, fam + '.md')) // 1024, 'KB', '예시 덱', sizes, 'KB')
