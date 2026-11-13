# 첫 화면(index.html) · 글 목록(catalog.md) · 덱 순서(data/decks.json) 만들기.
# 첫 화면은 참고용 목록이다: 기존 장표를 분위기별로 모으고(표지 → 목차·간지·맺음 → 본문), 공용 본문은 자리 순서로 묶는다.
# 내용은 모두 HTML 안에 미리 들어 있어 채팅 AI가 주소만으로 글로 읽는다(스크립트는 빠르게 보기만 한다).
# 재료: data/rounds.json · data/triage.json(본문의 '내용의 모양') · scripts/kit.py 의 계열 이름
# 실행: python3 scripts/site.py     (triage.py · light.py 다음에)
import html, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import kit
BASE = kit.BASE
E = lambda s: html.escape(str(s), quote=True)
J = lambda *p: json.load(open(os.path.join(ROOT, *p), encoding='utf-8'))
rounds = J('data', 'rounds.json'); tri = J('data', 'triage.json')
for r in rounds: r['no'] = int(r['no'])
FAMS = 'ABCDEFGH'
SECTIONS = [('현황', '배경 · 현황'), ('목표 및 지표', '목표 · 지표'), ('세부과제', '세부 과제'), ('추진체계', '추진 체계'), ('일정 및 예산', '일정 · 예산'), (None, '그 밖')]
SEC_NAME = dict(SECTIONS); SEC_ORDER = {k: i for i, (k, _) in enumerate(SECTIONS)}
MO = {'모션': '▶ 저절로 움직임', '인터랙션': '◉ 눌러서 조작', '정지': ''}
vis = sorted([r for r in rounds if not r.get('hidden')], key=lambda r: r['no'])
name = lambda r: re.sub(r'^레퍼런스\s*#\d+\s*', '', r['title'])
shape = lambda r: (tri.get(str(r['no']), {}).get('pattern') or '').replace('—', '')
light = lambda r: 'light/' + os.path.basename(r['file'])
ver = lambda r: ('?v=' + r['v']) if r.get('v') else ''
def one(r):
    t = re.split(r'(?<=[다요음함])\. | / ', (r.get('takeaway') or r.get('topic') or r.get('summary') or '').strip())[0]
    return t if len(t) <= 78 else t[:76].rstrip() + '…'
fits = lambda r, f: r.get('family') == f or (not r.get('family') and f in (r.get('families') or []))
by = lambda role: [r for r in vis if r['role'] == role]
body_ok = [r for r in by('본문') if r.get('deck_ok') is not False]
shared = [r for r in body_ok if len(r.get('families') or []) >= 4]            # 여러 분위기에 갈아 끼우는 공용 본문
own = lambda f: [r for r in body_ok if r not in shared and fits(r, f)]       # 그 분위기에만 맞는 본문
sec_sort = lambda rs: sorted(rs, key=lambda r: (SEC_ORDER.get(r.get('section'), 9), r['no']))
# 덱에 넣는 대표 본문(모양마다 하나, 손으로 고른다): 한 장에 도식이 적고 담백한 것, 분위기 색이 깨끗하게 입는 것
REPS = [80, 118, 120, 111, 85, 119, 121, 76, 84, 113, 86, 79]
SHAPES = [p['name'] for p in kit.PATTERNS]
NO_SHARED = {'G': '공용 본문은 밝은 바탕 기준으로 만들어져, 어두운 G에서는 일부 글자가 흐리다. 그래서 G 덱에는 넣지 않았다'}   # 분위기 색이 안 맞는 계열
slide = lambda r, f='': '%s?slide=%s' % (light(r), f)

def card(r, tag=''):
    bits = [x for x in (tag or (shape(r) if r['role'] == '본문' else ''), MO.get(r.get('motion'), '')) if x]
    return ('<article class="c"><a class="th" href="%s%s" data-ql data-code="%s"><img src="%s%s" alt="" loading="lazy" width="640" height="360"></a>'
            '<h4>%s <small>#%d</small></h4>%s<p>%s</p><p class="lk"><a href="%s%s" data-ql data-code="%s">원본</a> · <a href="%s">가벼운 코드</a></p></article>') % (
        E(r['file']), ver(r), light(r), E(r['thumb']), ver(r), E(name(r)), r['no'],
        ('<p class="tg">%s</p>' % ' · '.join(E(b) for b in bits)) if bits else '', E(one(r)), E(r['file']), ver(r), light(r), light(r))
grid = lambda rs, tag='': '<div class="g">%s</div>' % ''.join(card(r, tag) for r in rs)

H = []
H.append('''<header>
  <h1>디자인 레퍼런스</h1>
  <p class="lead">발표 덱을 만들 때 참고하는 장표 모음입니다. 장표 %d개를 <b>분위기 여덟</b>으로 묶었고, 분위기마다 표지 → 목차·간지·맺음 → 본문 순서로 한 덱처럼 볼 수 있습니다.
  모든 기관명 · 수치는 가상 예시이고, 사진은 AI로 만든 것입니다.</p>
  <p class="ai">AI가 읽을 때: 이 페이지는 글로 된 목록입니다. 장표마다 <b>가벼운 코드</b>(<code>light/번호.html</code>, 글꼴 · 그림을 박지 않아 평균 50KB)가 있고, <b>원본</b>(<code>refs/번호.html</code>)은 인터넷 없이 도는 완성본이라 큽니다.
  색 · 글꼴 · 설명까지 적은 글 목록은 <a href="catalog.md">catalog.md</a>(분위기별로 <code>catalog/A.md</code>~<code>H.md</code>, 공용 본문 <code>catalog/body.md</code>)입니다.</p>
  <nav class="moods">%s</nav>
</header>''' % (len(vis), ''.join('<a href="#m-%s"><img src="%s" alt="" loading="lazy" width="640" height="360"><b>%s %s</b><span>%s</span></a>' % (
    f, E(next((r['thumb'] + ver(r) for r in by('표지') if r.get('family') == f), 'kit/thumbs/%s-1.jpg' % f)), f, E(kit.NAMES[f]),
    '표지 %d · 덱 %d장' % (sum(1 for r in by('표지') if r.get('family') == f), 0)) for f in FAMS)))

decks = {}
for f in FAMS:
    covers = [r for r in by('표지') if r.get('family') == f]; kits = [r for r in by('목차·간지') if r.get('family') == f]
    mine = sec_sort(own(f)); common = sec_sort([r for r in shared if fits(r, f) and r['no'] in REPS and f not in NO_SHARED]); n_all = sum(1 for r in shared if fits(r, f))
    extra = [r for r in vis if r['role'] in ('발표 틀', '인쇄·홍보물') and r.get('family') == f]
    # 덱에는 전용 본문 중 그대로 넣을 수 있는 것만(눌러서 조작 · 재질 질감은 목록에만 둔다)
    in_deck = [r for r in mine if tri.get(str(r['no']), {}).get('judge') != '영감']
    deck = [(r, '표지') for r in covers] + [(r, '목차·간지·맺음') for r in kits] + [(r, '본문 · ' + SEC_NAME.get(r.get('section'), '그 밖')) for r in sec_sort(in_deck + common)]
    # 덱 화면은 장표만 띄운다(light/NN.html?slide=). 공용 본문에는 그 분위기의 색 · 글꼴을 입힌다(?slide=B)
    decks[f] = [{'no': r['no'], 'title': name(r), 'group': g, 'file': slide(r, f if r in shared else ''), 'orig': r['file'] + ver(r), 'code': light(r)} for r, g in deck]
    H.append('<section class="mood" id="m-%s"><h2>%s %s <small>%s</small></h2>' % (f, f, E(kit.NAMES[f]), E(kit.META[f]['desc'])))
    H.append('<p class="deckline"><a class="btn" href="deck.html?fam=%s">덱으로 넘겨 보기 · %d장</a> <span>표지 %d → 목차·간지·맺음 %d → 본문 %d(전용 %d + 공용에서 고른 %d, 이 분위기 색을 입힘). 뼈대만 따로: <a href="kit/%s.html">덱 키트 %s 예시 덱</a></span></p>' % (
        f, len(deck), len(covers), len(kits), len(in_deck) + len(common), len(in_deck), len(common), f, f))
    if covers: H.append('<h3>표지 <small>%d개 — 덱의 첫 장, 분위기를 정한다</small></h3>%s' % (len(covers), grid(covers)))
    if kits: H.append('<h3>목차 · 간지 · 맺음 <small>세 장이 한 벌</small></h3>%s' % grid(kits))
    if mine: H.append('<h3>이 분위기 전용 본문 <small>%d개</small></h3>%s' % (len(mine), grid(mine)))
    H.append('<p class="note">%s</p>' % (E(NO_SHARED[f]) + '.' if f in NO_SHARED else '이 분위기에 맞는 공용 본문 %d개 가운데 모양마다 하나씩 %d개를 덱에 넣었습니다. 나머지는 <a href="#body">아래 본문 모음</a>에 있습니다.' % (n_all, len(common)) if n_all else '공용 본문은 이 분위기에 맞게 만들어지지 않았습니다.'))
    if extra: H.append('<h3>같은 분위기의 발표 틀 · 인쇄물 <small>%d개 — 넘기는 덱은 아님</small></h3>%s' % (len(extra), grid(extra)))
    H.append('</section>')
# 머리 타일의 덱 장 수 채우기
for f in FAMS: H[0] = H[0].replace('표지 %d · 덱 0장' % sum(1 for r in by('표지') if r.get('family') == f) + '</span></a>', '표지 %d · 덱 %d장</span></a>' % (sum(1 for r in by('표지') if r.get('family') == f), len(decks[f])), 1)

H.append('<section id="body"><h2>본문 모음 <small>공용 %d개 — 색 · 글꼴을 변수로 받아 여러 분위기에 갈아 끼우는 장표. 모양별로 묶었고, 맨 앞이 덱에 넣은 대표</small></h2>' % len(shared))
for sh in SHAPES:
    rs = sorted([r for r in shared if shape(r) == sh], key=lambda r: (r['no'] not in REPS, -r['no']))
    if rs: H.append('<h3>%s <small>%d개</small></h3><div class="g">%s</div>' % (E(sh), len(rs), ''.join(
        card(r, ('덱 대표 · ' if r['no'] in REPS else '') + SEC_NAME.get(r.get('section'), '')) for r in rs)))
rest = [r for r in shared if shape(r) not in SHAPES]
if rest: H.append('<h3>그 밖의 모양 <small>%d개</small></h3>%s' % (len(rest), grid(rest)))
H.append('</section>')

rest_cover = [r for r in by('표지') if not r.get('family')]
rest_frame = [r for r in by('발표 틀') if not r.get('family')]
rest_print = [r for r in by('인쇄·홍보물') if not r.get('family')]
rest_body = [r for r in by('본문') if r not in shared and not any(fits(r, f) for f in FAMS) or r.get('deck_ok') is False]
H.append('<section id="more"><h2>그 밖 <small>분위기에 묶이지 않은 것</small></h2>')
for label, rs in (('표지', rest_cover), ('본문 — 덱에 그대로 넣기 어려운 것(눌러서 조작 · 재질 질감)', rest_body), ('발표 틀 — 넘기는 덱이 아니라 자체 진행 방식', rest_frame), ('인쇄 · 홍보물', rest_print)):
    if rs: H.append('<h3>%s <small>%d개</small></h3>%s' % (label, len(rs), grid(rs)))
hidden = [r for r in rounds if r.get('hidden')]
H.append('<p class="note">곁들이는 것: <a href="kit/index.html">덱 키트</a>(분위기별 뼈대와 부품) · <a href="wow/wow.html">와우 포인트 24</a>(발표 연출) · <a href="icons/icons.html">아이콘 세트</a>. 제작 기준에 걸려 숨긴 장표 %d개(%s).</p></section>' % (
    len(hidden), ' · '.join('#%d' % r['no'] for r in hidden)))
shown = set(); [shown.add(int(m)) for m in re.findall(r'<small>#(\d+)</small>', '\n'.join(H))]
missing = [r['no'] for r in vis if r['no'] not in shown]
if missing: raise SystemExit('목록에서 빠진 장표: %s' % missing)

CSS = r'''
:root{--bg:#F5F4F0;--card:#FFFFFF;--ink:#1C1E22;--soft:#5E626A;--line:#E2E0DA;--key:#2563A8;--chip:#ECEAE4;
  --f:"Noto Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif;--m:ui-monospace,SFMono-Regular,Consolas,monospace}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:12px}
html,body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f);word-break:keep-all;line-height:1.6}
a{color:inherit}
img{max-width:100%;height:auto;display:block;background:var(--chip)}
.wrap{max-width:1280px;margin:0 auto;padding:40px 16px 80px}
h1{font-size:clamp(26px,4vw,40px);font-weight:900;letter-spacing:-.02em;margin:0}
h2{font-size:24px;font-weight:900;margin:64px 0 6px;letter-spacing:-.01em;padding-top:18px;border-top:2px solid var(--ink)}
h3{font-size:16px;margin:26px 0 10px}
h2 small,h3 small{margin-left:8px;font-size:13.5px;font-weight:400;color:var(--soft);letter-spacing:0}
.lead{margin:10px 0 0;color:var(--soft);max-width:74ch}.lead b{color:var(--ink)}
.ai{margin:10px 0 0;font-size:13.5px;color:var(--soft);max-width:90ch}.ai b{color:var(--ink)}
code{font-family:var(--m);font-size:.92em;background:var(--chip);padding:1px 5px;border-radius:4px}
.moods{margin:22px 0 0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.moods a{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;font-size:13px;color:var(--soft)}
.moods a:hover{border-color:var(--ink)}
.moods img{aspect-ratio:16/9;object-fit:cover}
.moods b{display:block;padding:8px 12px 0;font-size:15px;color:var(--ink)}.moods span{display:block;padding:0 12px 10px}
.deckline{margin:8px 0 0;font-size:13.5px;color:var(--soft);display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center}
.btn{display:inline-flex;align-items:center;min-height:40px;padding:6px 16px;border-radius:999px;background:var(--ink);color:#fff;font-weight:700;font-size:14px;text-decoration:none}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,230px),1fr));gap:14px}
.c{background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden;font-size:12.5px;display:flex;flex-direction:column}
.c .th img{aspect-ratio:16/9;object-fit:cover;border-bottom:1px solid var(--line)}
.c h4{margin:9px 11px 0;font-size:14.5px;line-height:1.4}.c h4 small{font-weight:400;color:var(--soft);font-size:12px}
.c p{margin:3px 11px 0;color:var(--soft);line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.c .tg{color:var(--key);font-weight:700}
.c .lk{margin-top:auto;padding:8px 0 10px;color:var(--ink)}
.note{margin:14px 0 0;font-size:13.5px;color:var(--soft)}
footer{margin-top:48px;font-size:13px;color:var(--soft)}
dialog.ql{width:min(1280px,calc(100vw - 32px));padding:0;border:0;border-radius:14px;background:#111;box-shadow:0 30px 80px -20px rgba(0,0,0,.5)}
dialog.ql::backdrop{background:rgba(20,22,26,.6)}
.ql iframe{display:block;width:100%;height:min(76vh,760px);border:0;background:#fff}
.ql .acts{display:flex;gap:8px;justify-content:flex-end;padding:8px 10px}
.ql .acts a,.ql .acts button{padding:7px 14px;border-radius:999px;border:1px solid #555;background:none;color:#fff;font:700 13px var(--f);text-decoration:none;cursor:pointer}
:focus-visible{outline:2px solid var(--key);outline-offset:2px}
@media (max-width:820px){.moods{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''
JS = r'''
const $ = s => document.querySelector(s), ql = $('#ql'), fr = $('#qlFrame');
// 빠르게 보기: 장표를 그 자리에서 띄운다(새 탭 · 가운데 단추는 그대로 원본)
document.addEventListener('click', e => {
  const a = e.target.closest('a[data-ql]'); if (!a || e.ctrlKey || e.metaKey || e.shiftKey || e.button) return;
  e.preventDefault(); fr.src = a.href; $('#qlOpen').href = a.href; $('#qlCode').href = a.dataset.code; ql.showModal(); $('#qlClose').focus();
});
fr.addEventListener('load', () => { try { fr.contentWindow.addEventListener('keydown', e => { if (e.key === 'Escape') ql.close(); }); } catch (e) {} });
ql.addEventListener('close', () => { fr.src = 'about:blank'; });
ql.addEventListener('click', e => { if (e.target.id === 'qlClose' || e.target === ql) ql.close(); });
'''
page = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>디자인 레퍼런스 — 발표 덱 장표 모음</title>
<meta name="description" content="발표 덱을 만들 때 참고하는 장표 모음. 분위기 여덟으로 묶은 표지 · 목차·간지 · 본문. 모든 내용은 가상 예시입니다.">
<link rel="alternate" type="text/markdown" href="catalog.md" title="전체 목록(글)">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap">
<style>%s</style>
</head>
<body>
<!-- 이 파일은 scripts/site.py 가 만든다. 손으로 고치지 말 것 -->
<div class="wrap">
%s
<footer>글꼴은 모두 SIL Open Font License 1.1(<a href="fonts/LICENSES.md">저작권 고지</a>). 분류 기준은 <a href="docs/patterns.md">docs/patterns.md</a>.</footer>
</div>
<dialog class="ql" id="ql" aria-label="미리보기"><iframe id="qlFrame" title="미리보기"></iframe><div class="acts"><a id="qlCode" target="_blank" rel="noopener">가벼운 코드</a><a id="qlOpen" target="_blank" rel="noopener">새 창으로 열기</a><button type="button" id="qlClose">닫기</button></div></dialog>
<script>%s</script>
</body>
</html>
''' % (CSS, '\n'.join(H), JS)
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page)
open(os.path.join(ROOT, 'data', 'decks.json'), 'w', encoding='utf-8').write(json.dumps({f: {'name': kit.NAMES[f], 'slides': decks[f]} for f in FAMS}, ensure_ascii=False, indent=1) + '\n')

# ── catalog.md: 같은 목록을 글로(색 · 글꼴 · 설명까지). AI가 한 번에 읽는 파일
def entry(r):
    L = ['### #%d %s' % (r['no'], name(r)),
         '- 쓰임: %s%s%s%s' % (r['role'], ' · 모양 ' + shape(r) if r['role'] == '본문' and shape(r) else '', ' · 자리 ' + SEC_NAME[r['section']] if r.get('section') else '', ' · ' + r['motion'] if r.get('motion') else ''),
         '- 분위기: %s' % (('%s %s' % (r['family'], kit.NAMES[r['family']])) if r.get('family') else (' · '.join(r.get('families') or []) + ' 에 갈아 끼움' if r.get('families') else '정해지지 않음'))]
    if r.get('takeaway'): L.append('- 가져갈 장치: %s' % r['takeaway'])
    cut = lambda t, n: t if len(t) <= n else t[:n].rstrip() + '…'
    if r.get('summary'): L.append('- 설명: %s' % cut(r['summary'], 220))
    if r.get('style'): L.append('- 겉모습: %s' % cut(r['style'], 160))
    if r.get('palette'): L.append('- 색: %s' % ' '.join(r['palette']))
    if r.get('fonts'): L.append('- 글꼴: %s' % r['fonts'])
    L.append('- 코드: %s%s · 원본: %s%s' % (BASE, light(r), BASE, r['file']))
    return '\n'.join(L)
def write(path, lines):
    os.makedirs(os.path.dirname(os.path.join(ROOT, path)), exist_ok=True); open(os.path.join(ROOT, path), 'w', encoding='utf-8').write('\n'.join(lines) + '\n'); return os.path.getsize(os.path.join(ROOT, path)) // 1024
HEAD = '> 디자인 레퍼런스(%s)의 장표 목록입니다. 모든 기관명 · 수치는 가상 예시입니다. **코드**는 글꼴 · 그림을 박지 않은 가벼운 판, **원본**은 인터넷 없이 도는 완성본입니다. `scripts/site.py`가 만든 파일입니다.' % BASE
sizes = {}
C = ['# 디자인 레퍼런스 — 장표 목록', '', HEAD, '',
     '장표 %d개를 분위기 여덟으로 묶었습니다. 자세한 목록은 분위기별 파일에 있습니다.' % len(vis), '',
     '| 계열 | 겉모습 | 표지 | 목차·간지·맺음 | 전용 본문 | 자세한 목록 |', '|---|---|---|---|---|---|']
for f in FAMS:
    C.append('| %s %s | %s | %s | %s | %s | %scatalog/%s.md |' % (f, kit.NAMES[f], kit.META[f]['desc'], ' '.join('#%d' % r['no'] for r in by('표지') if r.get('family') == f) or '—',
                                             ' '.join('#%d' % r['no'] for r in by('목차·간지') if r.get('family') == f) or '—', ' '.join('#%d' % r['no'] for r in own(f)) or '—', BASE, f))
    rs = [r for r in vis if r.get('family') == f and r['role'] in ('표지', '목차·간지')] + own(f) + [r for r in vis if r['role'] in ('발표 틀', '인쇄·홍보물') and r.get('family') == f]
    sizes[f] = write('catalog/%s.md' % f, ['# %s %s — 장표 목록' % (f, kit.NAMES[f]), '', HEAD, '', kit.META[f]['desc'] + '.', '',
        '덱 순서: ' + ' → '.join('#%d %s' % (x['no'], x['title']) for x in decks[f]), ''] + [entry(r) + '\n' for r in rs])
C += ['', '한 덱은 `표지 → 목차·간지·맺음 → 본문(배경 · 현황 → 목표 · 지표 → 세부 과제 → 추진 체계 → 일정 · 예산)` 순서입니다.',
      '공용 본문은 색 · 글꼴을 변수(`--ds-*`)로 받아 여러 분위기에 갈아 끼웁니다. 덱에는 모양마다 하나씩 고른 대표(%s)가 들어갑니다.' % ' '.join('#%d' % n for n in REPS), '',
      '- 공용 본문(모양별): %scatalog/body.md' % BASE, '- 그 밖(발표 틀 · 인쇄 · 홍보물 · 분위기 없는 것): %scatalog/etc.md' % BASE,
      '- 분위기별 덱 넘겨 보기: %sdeck.html?fam=B (장표만: `light/번호.html?slide=B` — 뒤의 계열 글자를 바꾸면 그 분위기 색으로)' % BASE, '']
B_ = ['# 공용 본문 — 모양별 목록', '', HEAD, '']
for sh in SHAPES:
    rs = sorted([r for r in shared if shape(r) == sh], key=lambda r: (r['no'] not in REPS, -r['no']))
    if rs: B_ += ['## %s (%d)' % (sh, len(rs)), ''] + [entry(r) + ('\n- 덱 대표' if r['no'] in REPS else '') + '\n' for r in rs]
sizes['body'] = write('catalog/body.md', B_)
taken = {r['no'] for r in shared} | {r['no'] for f in FAMS for r in own(f)} | {r['no'] for r in vis if r.get('family') and r['role'] in ('표지', '목차·간지', '발표 틀', '인쇄·홍보물')}
sizes['etc'] = write('catalog/etc.md', ['# 그 밖 — 분위기에 묶이지 않은 장표', '', HEAD, ''] + [entry(r) + '\n' for r in vis if r['no'] not in taken])
write('catalog.md', C)
text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style).*?</\1>', '', page, flags=re.S)))
print('index.html', len(page.encode('utf-8')) // 1024, 'KB · 글', len(text), '자 · catalog/ KB', sizes, '· 덱', {f: len(decks[f]) for f in FAMS})
