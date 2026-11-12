# 첫 화면(index.html) 만들기: 사람이 보는 화면이면서, 채팅 AI가 주소만으로 글로 읽는 안내.
# 내용은 모두 HTML 안에 미리 들어 있다(스크립트는 분위기 바꾸기 · 빠르게 보기 · 복사만 한다).
# 재료: data/patterns.json · data/flows.json · data/kit_slides.json · data/triage.json · data/rounds.json · scripts/kit.py 의 안내문
# 실행: python3 scripts/site.py   (kit.py · triage.py 다음에)
import html, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import kit
E = lambda s: html.escape(str(s), quote=True)
J = lambda *p: json.load(open(os.path.join(ROOT, *p), encoding='utf-8'))
rounds = J('data', 'rounds.json'); tri = J('data', 'triage.json')
P, F = kit.PATTERNS, kit.FLOWS
PID = {p['name']: p['id'] for p in P}; PID['목차·간지·맺음'] = 'toc'

def inline(s):
    s = E(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return re.sub(r'(https://[^\s<)]+)', r'<a href="\1">\1</a>', s)
def md(text):
    """안내문에 쓰는 만큼의 마크다운: 제목 · 번호/점 목록 · 표 · 코드 블록 · 문단"""
    out, lines, i = [], text.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            j = i + 1
            while not lines[j].startswith('```'): j += 1
            out.append('<pre><code>%s</code></pre>' % E('\n'.join(lines[i + 1:j]))); i = j + 1; continue
        if l.startswith('|'):
            j = i
            while j < len(lines) and lines[j].startswith('|'): j += 1
            rows = [[c.strip() for c in r.strip('|').split(' | ')] for r in lines[i:j] if not re.match(r'^\|\s*-', r)]
            out.append('<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
                ''.join('<th>%s</th>' % inline(c) for c in rows[0]), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c) for c in r) for r in rows[1:]))); i = j; continue
        m = re.match(r'^(\d+)\. (.*)', l)
        if m or l.startswith('- '):
            tag, pat = ('ol', r'^\d+\. (.*)') if m else ('ul', r'^- (.*)'); items = []
            while i < len(lines) and re.match(pat, lines[i]): items.append(re.match(pat, lines[i]).group(1)); i += 1
            out.append('<%s>%s</%s>' % (tag, ''.join('<li>%s</li>' % inline(x) for x in items), tag)); continue
        if l.startswith('### '): out.append('<h4>%s</h4>' % inline(l[4:]))
        elif l.strip(): out.append('<p>%s</p>' % inline(l))
        i += 1
    return '\n'.join(out)

# 안내문(kit.guide)을 번호 붙은 절로 나눈다
sec = {}
for part in re.split(r'\n(?=## )', kit.guide()):
    m = re.match(r'## (\d+)\. (.+?)\n(.*)', part, re.S)
    if m: sec[int(m.group(1))] = (m.group(2).strip(), m.group(3).strip())

thumb = lambda fid, n: 'kit/thumbs/B%s-%d.jpg' % (next(f['deck'] for f in F if f['id'] == fid), n)
kimg = lambda fid, n, alt='': '<img src="%s" data-k="%s" alt="%s" loading="lazy" width="640" height="360">' % (
    thumb(fid, n), thumb(fid, n).replace('thumbs/B', 'thumbs/{k}'), E(alt))
deck_url = lambda fid, n=0: 'kit/B%s.html%s' % (next(f['deck'] for f in F if f['id'] == fid), '#%d' % n if n else '')
name_of = lambda r: re.sub(r'^레퍼런스\s*#\d+\s*', '', r['title'])
vis = [r for r in rounds if not r.get('hidden')]
def judged(j): return [r for r in vis if tri.get(str(r['no']), {}).get('judge') == j]
def ref_card(r, why=True):
    t = tri.get(str(r['no']), {})
    return ('<a class="ref" href="%s" data-ql><img src="%s" alt="" loading="lazy" width="640" height="360"><b>%s <small>#%s</small></b>%s</a>' % (
        E(r['file']) + ('?v=' + E(r['v']) if r.get('v') else ''), E(r['thumb']) + ('?v=' + E(r['v']) if r.get('v') else ''), E(name_of(r)), r['no'],
        '<span>%s</span>' % E((r.get('takeaway') or t.get('why', '')).split(':')[0][:60]) if why else ''))

H = []
# ── 머리: 무엇인지 · 쓰는 법 ──
prompt = '%s 을(를) 읽고, 첨부한 문서를 16:9 발표 덱 HTML로 만들어 줘. 먼저 장별 구성안을 보여 줘.' % kit.BASE
H.append('''<header>
  <h1>디자인 레퍼런스</h1>
  <p class="lead">한글 문서(계획안 · 연수 강의안 · 성과 보고)를 <b>16:9 발표 덱</b>으로 바꿀 때 채팅 AI가 읽는 디자인 안내이자 재료입니다.
  이 주소와 문서를 AI에게 주면, 여기 있는 기본 장표 23가지와 분위기 넷으로 덱을 만듭니다.</p>
  <ol class="how">
    <li><b>문서를 올립니다</b><span>Claude · ChatGPT 대화창에 한글 문서(또는 PDF)를 첨부합니다. 개인정보는 지우고.</span></li>
    <li><b>이 주소를 줍니다</b><span>아래 문장을 붙여 넣습니다. 분위기를 정했으면 "B 분위기로"를 덧붙입니다.</span></li>
    <li><b>구성안을 확인합니다</b><span>AI가 장별 구성안을 먼저 보여 줍니다. 고친 뒤 "만들어 줘". 받은 .html은 → 키로 넘깁니다.</span></li>
  </ol>
  <div class="prompt"><code id="prompt">%s</code><button type="button" id="copy">복사</button></div>
  <p class="ai">AI에게: 이 페이지 전체가 안내입니다. <a href="#rules">지킬 것</a> → <a href="#flows">흐름</a> → <a href="#patterns">기본 장표와 견본 코드</a> → <a href="#shell">뼈대</a> 순서로 읽으세요.
  같은 내용의 글 파일은 <a href="guide.md">guide.md</a>, 계열 하나만 쓰는 지시서는 <a href="kit/A.md">A</a> · <a href="kit/B.md">B</a> · <a href="kit/C.md">C</a> · <a href="kit/D.md">D</a>입니다. 모든 예시 내용은 가상입니다.</p>
</header>''' % E(prompt))

# ── 분위기(화면의 견본 그림을 바꾸는 스위치이기도 하다) ──
H.append('<section id="moods"><h2>분위기 넷 <small>겉모습만 다르고 부품 이름은 같습니다. 고르면 아래 견본 그림이 그 분위기로 바뀝니다</small></h2><div class="moods">')
for f in kit.FAMS:
    m = kit.META[f]
    H.append('''<article class="mood" data-fam="%s">
  <button type="button" class="pick" data-fam="%s" aria-pressed="%s"><img src="kit/thumbs/%s-1.jpg" alt="" loading="lazy" width="640" height="360"><b>%s %s</b></button>
  <p>%s. <span>어울리는 자리: %s</span></p>
  <p class="links">예시 덱 %s · <a href="kit/%s.md">지시서</a></p>
</article>''' % (f, f, 'true' if f == 'B' else 'false', f, f, E(kit.NAMES[f]), E(m['desc']), E(m['fit']),
                 ' · '.join('<a href="kit/%s%s.html" data-ql>%s</a>' % (f, d['deck'], E(d['name'])) for d in kit.DECKS), f))
H.append('</div></section>')

# ── AI가 지킬 것(0 · 1 · 2) ──
H.append('<section id="rules"><h2>AI가 지킬 것 <small>사람은 읽지 않아도 됩니다</small></h2>')
for k, op in ((0, ''), (1, ''), (2, '')):
    H.append('<details%s><summary>%d. %s</summary>%s</details>' % (op, k, E(sec[k][0]), md(sec[k][1])))
H.append('</section>')

# ── 흐름 ──
H.append('<section id="flows"><h2>흐름 <small>문서 종류에 맞는 자리 순서. 자리마다 쓰는 기본 장표가 정해져 있습니다</small></h2>')
slides = J('data', 'kit_slides.json')
for f in F:
    H.append('<article class="flow" id="flow-%s"><h3>%s <small>%s</small></h3><ol class="slots">' % (f['id'], E(f['name']), E(f['say'])))
    for sname, pids in f['slots']:
        H.append('<li><b>%s</b>%s</li>' % (E(sname), ''.join('<a href="#p-%s">%s</a>' % (x, E(kit.PNAME[x])) for x in pids)))
    H.append('</ol>')
    if f['deck'] is not None:
        mine = [s for s in slides if s['flow'] == f['id']]
        H.append('<p class="decknote">예시 덱 %d장 — 가상 내용 하나로 처음부터 끝까지 엮은 것입니다. 누르면 그 장에서 열립니다.</p><div class="strip">' % len(mine))
        for s in mine:
            H.append('<a href="%s" data-ql data-k="%s" title="%s">%s<span>%d. %s</span></a>' % (
                deck_url(f['id'], s['n']), deck_url(f['id'], s['n']).replace('kit/B', 'kit/{k}'), E(s['title']), kimg(f['id'], s['n']), s['n'], E(kit.PNAME[s['pattern']])))
        H.append('</div>')
    else:
        H.append('<p class="decknote">예시 덱은 아직 없습니다. 위 자리 순서대로 기본 장표를 엮습니다.</p>')
    H.append('</article>')
H.append('<p class="decknote">여러 차시 과정이면 맨 앞에 일정 장표를 과정 지도로 쓰고(차시마다 이정표 하나), 차시마다 연수 한 차시 흐름을 되풀이합니다.</p></section>')

# ── 기본 장표 23 + 견본 코드 + 변주 ──
H.append('<section id="patterns"><h2>기본 장표 23가지 <small>내용의 모양으로 고릅니다. 한 장에 하나</small></h2>')
order = sec[3][1].split('**고르는 순서**', 1)[1]
H.append('<details class="pickorder" open><summary>고르는 순서 — 한 문단이 둘 이상에 맞으면 위에서부터</summary>%s</details>' % md(order.split('\n', 1)[1].strip()))
variants = {}
for r in judged('변주') + judged('기본 후보'):
    variants.setdefault(PID.get(tri[str(r['no'])]['pattern']), []).append(r)
group = None
for p in P:
    if p['group'] != group:
        if group: H.append('</div>')
        group = p['group']; H.append('<h3 class="grp">%s</h3><div class="pats">' % E(group))
    sm = kit.samples(p['id']); fid, s = sm[0]
    vs = sorted(variants.get(p['id'], []), key=lambda r: -int(r['no']))
    H.append('''<article class="pat" id="p-%s">
  <a class="shot" href="%s" data-ql data-k="%s">%s</a>
  <h4>%s <code>%s</code></h4>
  <p class="when">%s</p>
  <dl><dt>내용 조건</dt><dd>%s</dd><dt>넘치면</dt><dd>%s</dd><dt>부품</dt><dd>%s%s</dd></dl>
  <details class="code"><summary>견본 코드</summary>%s</details>''' % (
        p['id'], deck_url(fid, s[0]), deck_url(fid, s[0]).replace('kit/B', 'kit/{k}'), kimg(fid, s[0], p['name'] + ' 견본'), E(p['name']), p['id'], E(p['when']),
        E(p['cond']), E(p['overflow']), inline(kit.part_md(p)), (' — ' + inline(p['note'])) if p['note'] else '',
        ''.join('<pre><code>%s</code></pre>' % E(kit.code_of(None, a, b)) for a, b in sm)))
    if vs:
        H.append('<details class="vars"><summary>참고할 변주 %d개</summary><div class="refs">%s</div></details>' % (len(vs), ''.join(ref_card(r) for r in vs)))
    H.append('</article>')
H.append('</div></section>')

# ── 뼈대 · 상징 부품 · 점검 ──
H.append('<section id="shell"><h2>HTML 뼈대와 상징 부품 <small>AI가 덱을 쓸 때 그대로 가져다 씁니다</small></h2>')
for k in (6, 7, 9):
    H.append('<details><summary>%d. %s</summary>%s</details>' % (k, E(sec[k][0]), md(sec[k][1])))
H.append('</section>')

# ── 참고 서랍: 덱 재료가 아닌 것 ──
insp, out = judged('영감'), judged('범위 밖'); hidden = [r for r in rounds if r.get('hidden')]
H.append('''<section id="more"><h2>참고 서랍 <small>덱에 조립하는 재료가 아닙니다. AI는 건너뛰어도 됩니다</small></h2>
<details><summary>영감 %d개 — 눌러서 조작하는 표지 · 재질 질감 · 자체 진행 방식</summary><div class="refs">%s</div></details>
<details><summary>인쇄 · 홍보물 %d개 — 포스터 · 리플렛 · 소식지(16:9 덱이 아님)</summary><div class="refs">%s</div></details>
<details><summary>곁들이는 것 — 발표 연출 · 아이콘</summary><p><a href="wow/wow.html">와우 포인트 24</a>(발표 연출 기법 9장 덱) · <a href="icons/icons.html">아이콘 세트</a>(교육행정 85개, SVG) · <a href="kit/index.html">덱 키트 모음</a></p></details>
<p class="decknote">제작 기준에 걸려 숨긴 장표 %d개(%s)는 목록에서 뺐습니다. 분류 틀은 <a href="docs/patterns.md">기본 장표 틀</a>, 판정은 <a href="docs/triage.md">판정표</a>, 만드는 규칙은 <a href="docs/criteria.md">제작 기준</a>.</p>
</section>''' % (len(insp), ''.join(ref_card(r, False) for r in sorted(insp, key=lambda r: -int(r['no']))),
                len(out), ''.join(ref_card(r, False) for r in sorted(out, key=lambda r: -int(r['no']))),
                len(hidden), ' · '.join('#%s' % r['no'] for r in hidden)))

CSS = r'''
:root{--bg:#F5F4F0;--card:#FFFFFF;--ink:#1C1E22;--soft:#5E626A;--line:#E2E0DA;--key:#2563A8;--chip:#ECEAE4;
  --f:"Noto Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif;--m:ui-monospace,SFMono-Regular,Consolas,monospace}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:16px}
html,body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f);word-break:keep-all;line-height:1.6}
a{color:inherit}
img{max-width:100%;height:auto;display:block;background:var(--chip)}
.wrap{max-width:1240px;margin:0 auto;padding:40px 16px 80px}
h1{font-size:clamp(26px,4vw,40px);font-weight:900;letter-spacing:-.02em;margin:0}
h2{font-size:22px;font-weight:900;margin:56px 0 14px;letter-spacing:-.01em}
h2 small,h3 small{display:inline-block;margin-left:8px;font-size:13.5px;font-weight:400;color:var(--soft);letter-spacing:0}
h3{font-size:17px;margin:0 0 10px}
.lead{margin:10px 0 0;color:var(--soft);max-width:70ch}.lead b{color:var(--ink)}
.how{list-style:none;margin:22px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;counter-reset:h}
.how li{counter-increment:h;border-top:2px solid var(--ink);padding-top:10px;font-size:14px}
.how b{display:block;font-size:15px}.how b::before{content:counter(h) ". "}
.how span{color:var(--soft)}
.prompt{margin:16px 0 0;display:flex;gap:8px;align-items:stretch}
.prompt code{flex:1;min-width:0;padding:12px 14px;background:var(--card);border:1px solid var(--line);border-radius:10px;font:13.5px/1.6 var(--m);overflow-wrap:anywhere}
button{font-family:var(--f);cursor:pointer}
.prompt button{flex:none;padding:0 18px;border-radius:10px;border:1px solid var(--ink);background:var(--ink);color:#fff;font-weight:700;font-size:14px}
.ai{margin:14px 0 0;font-size:13.5px;color:var(--soft)}
.moods{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.mood{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;font-size:13.5px}
.mood .pick{display:block;width:100%;padding:0;border:0;background:none;text-align:left;color:var(--ink)}
.mood .pick b{display:block;padding:10px 12px 0;font-size:15px}
.mood .pick[aria-pressed=true] b::after{content:" · 지금 보는 분위기";font-weight:500;font-size:12px;color:var(--key)}
.mood:has(.pick[aria-pressed=true]){border-color:var(--key);box-shadow:inset 0 0 0 1px var(--key)}
.mood p{margin:4px 12px 0;color:var(--soft)}.mood p span{display:block}
.mood .links{margin-bottom:12px;color:var(--ink)}
details{background:var(--card);border:1px solid var(--line);border-radius:10px;margin:8px 0}
summary{padding:11px 14px;font-weight:700;font-size:14.5px;cursor:pointer}
details > :not(summary){margin-left:14px;margin-right:14px}
details ol,details ul{padding-left:1.4em;font-size:14px}details li{margin:6px 0}details p{font-size:14px}
code{font-family:var(--m);font-size:.92em;background:var(--chip);padding:1px 5px;border-radius:4px}
pre{margin:10px 14px 14px;padding:12px 14px;background:#1F2227;color:#E9E7E1;border-radius:8px;overflow:auto;font:12.5px/1.55 var(--m);max-height:420px}
pre code{background:none;padding:0;font-size:inherit}
.tw{overflow-x:auto;margin-bottom:14px}table{border-collapse:collapse;font-size:13px;min-width:100%}
th,td{padding:7px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}th{white-space:nowrap}
.flow{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 16px 14px;margin:12px 0}
.slots{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.slots li{display:flex;flex-direction:column;gap:5px;padding:9px 11px;border-radius:8px;background:var(--bg);position:relative;font-size:13px;min-width:104px}
.slots li b{font-size:14px}
.slots a{display:inline-block;margin-right:4px;padding:1px 8px;border-radius:999px;background:var(--card);border:1px solid var(--line);text-decoration:none;white-space:nowrap}
.slots a:hover{border-color:var(--ink)}
.decknote{margin:12px 0 8px;font-size:13px;color:var(--soft)}
.strip{display:flex;gap:8px;overflow-x:auto;padding-bottom:6px;scroll-snap-type:x proximity}
.strip a{flex:0 0 190px;text-decoration:none;font-size:12px;color:var(--soft);scroll-snap-align:start}
.strip img{border-radius:6px;border:1px solid var(--line);aspect-ratio:16/9;object-fit:cover}
.strip span{display:block;margin-top:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.grp{margin:26px 0 10px;font-size:14px;color:var(--soft);font-weight:700}
.pats{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,290px),1fr));gap:14px}
.pat{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column}
.pat:target{border-color:var(--key);box-shadow:0 0 0 2px var(--key)}
.pat .shot img{aspect-ratio:16/9;object-fit:cover;border-bottom:1px solid var(--line)}
.pat h4{margin:12px 14px 0;font-size:17px}.pat h4 code{margin-left:4px;font-size:12px;font-weight:400}
.pat .when{margin:4px 14px 0;font-size:13.5px;color:var(--soft)}
.pat dl{margin:10px 14px 12px;display:grid;grid-template-columns:64px 1fr;gap:4px 8px;font-size:13px}
.pat dt{color:var(--soft)}.pat dd{margin:0}
.pat details{margin:0;border:0;border-top:1px solid var(--line);border-radius:0}
.pat summary{font-size:13.5px;padding:9px 14px}
.refs{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;padding-bottom:14px}
.ref{text-decoration:none;font-size:12px;line-height:1.45}
.ref img{border-radius:6px;border:1px solid var(--line);aspect-ratio:16/9;object-fit:cover}
.ref b{display:block;margin-top:4px;font-size:12.5px}.ref small{font-weight:400;color:var(--soft)}.ref span{color:var(--soft)}
footer{margin-top:48px;font-size:13px;color:var(--soft)}
dialog.ql{width:min(1280px,calc(100vw - 32px));padding:0;border:0;border-radius:14px;background:#111;box-shadow:0 30px 80px -20px rgba(0,0,0,.5)}
dialog.ql::backdrop{background:rgba(20,22,26,.6)}
.ql iframe{display:block;width:100%;aspect-ratio:16/9;max-height:calc(100vh - 110px);border:0;background:#fff}
.ql .acts{display:flex;gap:8px;justify-content:flex-end;padding:8px 10px;background:#111}
.ql .acts a,.ql .acts button{padding:7px 14px;border-radius:999px;border:1px solid #555;background:none;color:#fff;font:700 13px var(--f);text-decoration:none}
:focus-visible{outline:2px solid var(--key);outline-offset:2px}
@media (max-width:900px){.moods{grid-template-columns:repeat(2,minmax(0,1fr))}.how{grid-template-columns:1fr}}
@media (max-width:520px){.prompt{flex-direction:column}.prompt button{padding:10px}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''
JS = r'''
const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
// 분위기 바꾸기: 견본 그림과 예시 덱 주소를 그 계열 것으로(주소 ?fam=B 에 남는다)
function setFam(k){
  $$('.pick').forEach(b => b.setAttribute('aria-pressed', b.dataset.fam === k));
  $$('img[data-k]').forEach(i => { i.src = i.dataset.k.replace('{k}', k); });
  $$('a[data-k]').forEach(a => { a.href = a.dataset.k.replace('{k}', k); });
  history.replaceState(null, '', (k === 'B' ? location.pathname : '?fam=' + k) + location.hash);
}
$$('.pick').forEach(b => b.addEventListener('click', () => setFam(b.dataset.fam)));
const f0 = new URLSearchParams(location.search).get('fam'); if (f0 && 'ABCD'.includes(f0) && f0.length === 1) setFam(f0);
// 복사
$('#copy').addEventListener('click', async () => { try { await navigator.clipboard.writeText($('#prompt').textContent); $('#copy').textContent = '복사됨'; setTimeout(() => $('#copy').textContent = '복사', 1500); } catch (e) {} });
// 빠르게 보기: 장표 · 예시 덱을 그 자리에서 띄운다(새 탭 · 가운데 단추는 그대로 원본)
const ql = $('#ql'), fr = $('#qlFrame');
document.addEventListener('click', e => {
  const a = e.target.closest('a[data-ql]'); if (!a || e.ctrlKey || e.metaKey || e.shiftKey || e.button) return;
  e.preventDefault(); fr.src = a.href; $('#qlOpen').href = a.href; ql.showModal(); $('#qlClose').focus();
});
fr.addEventListener('load', () => { try { fr.contentWindow.addEventListener('keydown', e => { if (e.key === 'Escape') ql.close(); }); } catch (e) {} });
ql.addEventListener('close', () => { fr.src = 'about:blank'; });
ql.addEventListener('click', e => { if (e.target.id === 'qlClose' || e.target === ql) ql.close(); });
// 흐름의 기본 장표 이름을 누르면 그 카드로 가서 견본 코드를 편다
addEventListener('hashchange', () => { const t = location.hash.startsWith('#p-') && document.getElementById(location.hash.slice(1)); if (t) t.querySelector('details.code').open = true; });
'''
page = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>디자인 레퍼런스 — 문서를 발표 덱으로</title>
<meta name="description" content="한글 문서를 16:9 발표 덱 HTML로 바꿀 때 채팅 AI가 읽는 디자인 안내와 재료. 기본 장표 23가지 · 흐름 넷 · 분위기 넷. 모든 내용은 가상 예시입니다.">
<link rel="alternate" type="text/markdown" href="guide.md" title="AI용 안내(글)">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap">
<style>%s</style>
</head>
<body>
<!-- 이 파일은 scripts/site.py 가 만든다. 손으로 고치지 말 것 -->
<div class="wrap">
%s
<footer>모든 기관명 · 수치는 가상 예시이고, 사진은 AI로 만든 것입니다. 글꼴은 모두 SIL Open Font License 1.1(<a href="fonts/LICENSES.md">저작권 고지</a>).</footer>
</div>
<dialog class="ql" id="ql" aria-label="미리보기"><iframe id="qlFrame" title="미리보기"></iframe><div class="acts"><a id="qlOpen" target="_blank" rel="noopener">새 창으로 열기</a><button type="button" id="qlClose">닫기</button></div></dialog>
<script>%s</script>
</body>
</html>
''' % (CSS, '\n'.join(H), JS)
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page)
text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style).*?</\1>', '', page, flags=re.S)))
print('index.html', len(page.encode('utf-8')) // 1024, 'KB · 글로 읽히는 분량', len(text), '자')
