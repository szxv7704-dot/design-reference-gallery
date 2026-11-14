# 갤러리 화면 만들기: 사람이 스타일을 고르고, AI가 그 스타일을 읽어 적용하게 하는 화면들.
#   index.html        전체 스타일(검증된 세트가 먼저, 표지만 있는 디자인은 그 아래)
#   styles/{id}.html  스타일 하나: 10장 미리보기 · 구성별 쓰는 법 · 내려받기 · AI 요청문
#   body.html         본문 구성(전하려는 내용으로 찾기) · motion.html 모션·강조 · print.html 인쇄·홍보물 · guide.html 이용 방법
#   catalog.md        AI가 읽는 차례: 적용 순서 · 스타일 목록 · 구성 목록
# 원천: data/styles.json · data/roles.json · data/patterns.json · data/kit_slides.json · data/rounds.json. 화면과 AI용 목록이 같은 데이터에서 나온다.
# 실행: python3 scripts/gallery.py     (kit.py · kit_thumbs.js · site.py 다음에)
import html, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import kit
BASE = kit.BASE
E = lambda s: html.escape(str(s), quote=True)
J = lambda *p: json.load(open(os.path.join(ROOT, *p), encoding='utf-8'))
SD = J('data', 'styles.json'); STYLES = SD['styles']; MOODS = SD['moods']
ROLES = J('data', 'roles.json')['roles']; PAT = {p['id']: p for p in kit.PATTERNS}
slides = J('data', 'kit_slides.json'); rounds = J('data', 'rounds.json')
for r in rounds: r['no'] = int(r['no'])
vis = [r for r in rounds if not r.get('hidden')]
name = lambda r: re.sub(r'^레퍼런스\s*#\d+\s*', '', r['title'])
ver = lambda r: ('?v=' + r['v']) if r.get('v') else ''
VAR = kit.VAR; RN = {r['id']: r for r in ROLES}
SETS = {f: [s for s in slides if s['id'] == 'set' and s.get('fam') == f] for f in kit.FAMS}; SET2 = [s for s in slides if s['id'] == 'set2']
VARN = {(s['role'], s['var']): s['n'] for s in slides if s['id'] == 'var'}   # 구성 모음(kit/{ID}-var.html)의 장 번호
def users(role, v): return [s for s in STYLES if kit.pick(s['id'], role) == v]   # 그 구성을 10장 예시에 쓴 스타일
th = lambda f, deck, n: 'kit/thumbs/%s%s-%d.jpg' % (f, deck, n)
def status(s): return '검증된 세트' if s.get('verified') else '확장 중'
STATUS_NOTE = {'검증된 세트': '10장 예시 · 다른 주제 시험 · 넘침 검사를 통과', '확장 중': '10장 예시는 있으나 검증이 끝나지 않음', '표지 덱': '표지의 색 · 글꼴을 입힌 10장. 표지의 고유한 특징까지 본문에 이어받지는 않음'}
def role_slide(rid, f='B'):   # 그 역할을 맡은 10장 예시의 장 번호
    return next((s['n'] for s in SETS[f] if s.get('role') == rid), None)

NAV = [('index.html', '전체 스타일'), ('body.html', '본문 구성'), ('motion.html', '모션·강조'), ('print.html', '인쇄·홍보물'), ('guide.html', '이용 방법')]
CSS = r'''
:root{--bg:#F7F6F3;--card:#FFFFFF;--ink:#1B1E24;--soft:#5C616B;--line:#E3E1DB;--key:#1F5FD0;--keybg:#E8EFFC;--chip:#EDEBE5;--ok:#1E7B4F;--warn:#9A6400;
  --f:"Noto Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif;--m:ui-monospace,SFMono-Regular,Consolas,monospace}
*{box-sizing:border-box}
[hidden]{display:none!important}
html{scroll-behavior:smooth;scroll-padding-top:76px}
html,body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f);word-break:keep-all;line-height:1.6}
a{color:inherit}img{max-width:100%;height:auto;display:block;background:var(--chip)}
button{font-family:var(--f);cursor:pointer}
.top{position:sticky;top:0;z-index:10;background:rgba(247,246,243,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top div{max-width:1280px;margin:0 auto;padding:0 16px;display:flex;align-items:center;gap:8px 26px;flex-wrap:wrap}
.brand{font-weight:900;font-size:18px;text-decoration:none;padding:14px 0;margin-right:10px}
.top nav{display:flex;gap:4px 22px;flex-wrap:wrap}
.top nav a{padding:16px 2px 13px;text-decoration:none;font-size:15px;font-weight:500;border-bottom:3px solid transparent}
.top nav a[aria-current=page]{color:var(--key);border-bottom-color:var(--key);font-weight:700}
.wrap{max-width:1280px;margin:0 auto;padding:28px 16px 80px}
h1{font-size:clamp(28px,4.4vw,44px);font-weight:900;letter-spacing:-.02em;line-height:1.25;margin:0}
h2{font-size:26px;font-weight:900;margin:52px 0 6px;letter-spacing:-.01em}
h3{font-size:17px;margin:28px 0 10px}
h2 small,h3 small{margin-left:10px;font-size:14px;font-weight:400;color:var(--soft);letter-spacing:0}
.lead{margin:10px 0 0;font-size:17px;color:var(--soft);max-width:60ch}
.hero{display:grid;grid-template-columns:1fr auto;gap:20px 40px;align-items:start}
.ask{background:var(--keybg);border-radius:14px;padding:20px 22px;display:flex;gap:14px 20px;align-items:center;flex-wrap:wrap;font-weight:700;font-size:17px}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:8px 18px;border-radius:10px;border:2px solid var(--key);background:var(--card);color:var(--key);font:700 15px var(--f);text-decoration:none}
.btn.fill{background:var(--key);color:#fff}
.btn.small{min-height:36px;padding:4px 12px;font-size:14px;border-width:1.5px}
.steps{list-style:none;margin:24px 0 0;padding:0 0 22px;display:flex;flex-wrap:wrap;gap:10px 28px;border-bottom:1px solid var(--line);counter-reset:s;font-weight:700}
.steps li{counter-increment:s;display:flex;align-items:center;gap:10px}
.steps li::before{content:counter(s);width:30px;height:30px;border-radius:50%;background:var(--keybg);color:var(--key);display:grid;place-items:center}
.steps li + li{padding-left:0}
.tools{display:flex;flex-wrap:wrap;gap:10px 14px;align-items:center;margin:14px 0 18px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips button{border:1px solid #C9C6BE;background:var(--card);font:500 15px var(--f);padding:8px 18px;border-radius:999px;color:var(--ink)}
.chips button[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:#fff}
.tools input[type=search]{flex:1 1 220px;min-width:0;font:15px var(--f);padding:10px 14px;border:1px solid #C9C6BE;border-radius:10px;background:var(--card);color:var(--ink)}
.tools label{display:inline-flex;align-items:center;gap:8px;font-size:15px}
.tools input[type=checkbox],.cmp input{width:20px;height:20px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,380px),1fr));gap:20px}
.sc{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:10px;display:flex;flex-direction:column}
.sc .cv img{border-radius:8px;aspect-ratio:16/9;object-fit:cover}
.tri{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:6px}.mc .tri{gap:1px;margin:0;border-bottom:1px solid var(--line)}.mc .tri img{border:0}
.sc .tri img{border-radius:6px;aspect-ratio:16/9;object-fit:cover;border:1px solid var(--line)}
.sc h3{margin:12px 6px 0;font-size:20px}
.sc p{margin:2px 6px 0;font-size:14.5px;color:var(--soft)}
.sc .ft{margin:12px 6px 4px;display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center}
.badge{display:inline-block;padding:3px 10px;border-radius:999px;background:var(--chip);font-size:13px;font-weight:500;color:var(--soft)}
.badge.ok{background:#E2F2E9;color:var(--ok)}.badge.wip{background:#FBF0D9;color:var(--warn)}
.cmp{margin-left:auto;display:inline-flex;align-items:center;gap:6px;font-size:14px}
.minis{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,210px),1fr));gap:14px}
.mc{background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden;font-size:13px;display:flex;flex-direction:column}
.mc img{aspect-ratio:16/9;object-fit:cover;border-bottom:1px solid var(--line)}
.mc b{display:block;margin:8px 10px 0;font-size:14.5px;line-height:1.4}.mc small{font-weight:400;color:var(--soft)}
.mc p{margin:3px 10px 0;color:var(--soft);line-height:1.5}
a.mc{text-decoration:none}.mc > b:last-child{margin-bottom:10px}
.mc .lk{margin-top:auto;padding:8px 10px 10px;color:var(--ink)}
.short{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}
.short a{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;background:var(--card);border:1px solid var(--line);border-radius:10px;text-decoration:none;font-weight:500}
.short a::after{content:"›";color:var(--soft);font-size:20px}
.var3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.vc{text-decoration:none;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column;font-size:14px}
.vc img{aspect-ratio:16/9;object-fit:cover;border-bottom:1px solid var(--line);width:100%}
.vc b{display:block;margin:10px 12px 0;font-size:16.5px}.vc p{margin:4px 12px 0;color:var(--soft);line-height:1.55}.vc p:last-child{margin-bottom:12px}
.vc p.w{color:var(--ink)}.vc.on{border-color:var(--key);box-shadow:0 0 0 2px var(--key)}
.sw{position:sticky;top:58px;z-index:5;background:var(--bg);padding:10px 0;margin:18px 0 0;display:flex;gap:8px 12px;align-items:center;flex-wrap:wrap;font-size:14px;border-bottom:1px solid var(--line)}
.sw .chips button{padding:6px 14px;font-size:14px}
@media (max-width:820px){.short{grid-template-columns:1fr 1fr}.short a{padding:10px 12px;font-size:14px}.var3{grid-template-columns:1fr}.sw{top:0}.sw .chips{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;max-width:100%}.sw .chips button{white-space:nowrap}}
.note{margin:12px 0 0;font-size:14px;color:var(--soft)}
.empty{padding:40px 0;text-align:center;color:var(--soft)}
table{border-collapse:collapse;width:100%;font-size:14px;background:var(--card);border-radius:10px;overflow:hidden}
th,td{padding:10px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}th{white-space:nowrap;background:var(--chip);font-weight:700}
.tw{overflow-x:auto}
.view{background:#111;border-radius:12px;overflow:hidden}.view iframe{display:block;width:100%;aspect-ratio:16/9;border:0;background:#111}
.two{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:24px;align-items:start}
.kv{margin:0;display:grid;grid-template-columns:92px 1fr;gap:8px 12px;font-size:14.5px}.kv dt{color:var(--soft)}.kv dd{margin:0}
.kv ul{margin:0;padding-left:1.1em}
.acts{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
pre.req{white-space:pre-wrap;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;font:13.5px/1.6 var(--m);margin:10px 0 0;overflow-wrap:anywhere}
details{background:var(--card);border:1px solid var(--line);border-radius:10px;margin:10px 0;padding:0 14px}
summary{padding:12px 0;font-weight:700;cursor:pointer}
.tray{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:20;background:var(--ink);color:#fff;border-radius:999px;padding:8px 10px 8px 18px;display:flex;gap:12px;align-items:center;font-size:14.5px;box-shadow:0 12px 30px -10px rgba(0,0,0,.5)}
.tray[hidden]{display:none}.tray button{border:0;border-radius:999px;padding:8px 16px;font:700 14px var(--f);background:#fff;color:var(--ink)}
dialog{width:min(1240px,calc(100vw - 24px));max-height:calc(100vh - 24px);padding:18px;border:0;border-radius:14px;background:var(--bg);color:var(--ink)}
dialog::backdrop{background:rgba(20,22,26,.6)}
.cmpgrid{display:grid;gap:14px}.cmpgrid .row{display:grid;grid-template-columns:140px repeat(5,1fr);gap:6px;align-items:center}
.cmpgrid .row b{font-size:15px}.cmpgrid img{border-radius:6px;aspect-ratio:16/9;object-fit:cover;border:1px solid var(--line)}
:focus-visible{outline:3px solid var(--key);outline-offset:2px}
footer{margin-top:56px;font-size:13px;color:var(--soft)}
@media (max-width:820px){.top{position:static}.top div{flex-wrap:nowrap;gap:0 14px}.brand{font-size:15px;padding:10px 0;margin-right:0;white-space:nowrap}
  .top nav{flex-wrap:nowrap;gap:0 16px;overflow-x:auto;scrollbar-width:none;white-space:nowrap;min-width:0}.top nav::-webkit-scrollbar{display:none}.top nav a{padding:12px 2px 9px;font-size:14px}
  html{scroll-padding-top:12px}.hero,.two{grid-template-columns:1fr}.cmpgrid .row{grid-template-columns:repeat(3,1fr)}.cmpgrid .row b{grid-column:1 / -1}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''
COPY_JS = r'''
document.addEventListener('click', async e => {
  const b = e.target.closest('[data-copy]'); if (!b) return;
  const t = document.getElementById(b.dataset.copy).textContent, old = b.textContent;
  try { await navigator.clipboard.writeText(t); b.textContent = '요청문을 복사했습니다 — AI 대화창에 붙여 넣으세요'; }
  catch (err) { const r = document.createRange(); r.selectNodeContents(document.getElementById(b.dataset.copy)); getSelection().removeAllRanges(); getSelection().addRange(r); b.textContent = '아래 글을 직접 복사하세요'; }
  setTimeout(() => { b.textContent = old; }, 2600);
});
'''
def page(path, title, desc, cur, body, js='', up=''):
    nav = ''.join('<a href="%s%s"%s>%s</a>' % (up, h, ' aria-current="page"' if h == cur else '', E(t)) for h, t in NAV)
    s = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="alternate" type="text/markdown" href="%scatalog.md" title="AI가 읽는 목록">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap">
<style>%s</style>
</head>
<body>
<!-- 이 파일은 scripts/gallery.py 가 만든다. 손으로 고치지 말 것 -->
<header class="top"><div><a class="brand" href="%sindex.html">발표 디자인 라이브러리</a><nav aria-label="메뉴">%s</nav></div></header>
<main class="wrap">
%s
<footer>모든 기관명 · 수치 · 사례는 가상 예시입니다. 새 발표에 그대로 가져오지 마세요. 사진은 AI로 만든 것이고, 글꼴은 모두 SIL Open Font License 1.1(<a href="%sfonts/LICENSES.md">저작권 고지</a>).</footer>
</main>
<script>%s%s</script>
</body>
</html>
''' % (E(title), E(desc), up, CSS, up, nav, body, up, COPY_JS, js)
    os.makedirs(os.path.dirname(os.path.join(ROOT, path)) or ROOT, exist_ok=True)
    open(os.path.join(ROOT, path), 'w', encoding='utf-8').write(s)
    return len(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style).*?</\1>', '', s, flags=re.S))))

# ── AI 요청문 두 가지 ──
RULES = '''지킬 것:
- 자료를 실제로 열어 읽은 뒤에 적용해 주세요. 주소를 열 수 없으면 읽은 척하지 말고 열 수 없다고 말해 주세요.
- 먼저 장마다 "전하려는 것 · 고른 구성 · 제목"을 표로 보여 주고, 제가 확인하면 만들어 주세요.
- 스타일은 하나만 쓰고, 장마다 내용에 맞는 구성을 고릅니다. 한 장에 구성 하나.
- 예시에 들어 있는 기관명 · 수치 · 사례는 가상입니다. 제 발표에 가져오지 마세요. 제가 주지 않은 숫자를 지어내지 마세요.
- 내용이 많으면 글자를 줄이지 말고 장을 나눠 주세요. 제 핵심 내용을 임의로 빼지 마세요.'''
REQ_PICK = '''제가 올린 발표 내용에 어울리는 디자인을 아래 갤러리에서 골라 적용해 주세요.

1. 목록 읽기: %scatalog.md
2. 제 발표의 내용과 자리(누구에게, 몇 분)를 보고 '검증된 세트' 중에서 스타일 하나를 고르고, 이유를 한 줄로 말해 주세요.
3. 고른 스타일의 적용 안내(목록에 적힌 주소)를 읽고, 10장 안팎의 발표 HTML 파일 하나로 만들어 주세요.

%s''' % (BASE, RULES)
def req_apply(s):
    return '''제가 올린 발표 내용에 '%s' 스타일(ID: %s)을 적용해 발표 HTML 파일 하나로 만들어 주세요.

1. 적용 안내 읽기: %skit/%s.md  (디자인 규칙 · 구성별 코드 · HTML 뼈대가 들어 있습니다)
2. 완성 예시 보기: %skit/%s-set.html  (10장: 표지 · 흐름 · 개념 · 비교 · 절차 · 사례 · 실습 · 수치 · 요약 · 마무리)
   구성 모음: %skit/%s-var.html  (역할마다 배치가 다른 구성 셋. 예시의 조합을 따라 하지 말고 제 내용에 맞는 구성을 골라 주세요)
3. 유지할 것: %s
4. 바꿔도 되는 것: %s
5. 피할 것: %s

%s''' % (s['name'], s['id'], BASE, s['id'], BASE, s['id'], BASE, s['id'], ' / '.join(s['keep']), ' / '.join(s['change']), ' / '.join(s['avoid']), RULES)

# ── 표지 레퍼런스(이어지는 본문이 없는 디자인) ──
covers = sorted([r for r in vis if r['role'] == '표지'], key=lambda r: r['no'])
CDECK = {m['no']: m for m in J('data', 'cover_decks.json')}   # scripts/covers.py 가 만든 표지별 10장 덱
def cover_card(r, up=''):
    f = r.get('family'); no = r['no']; d = CDECK.get(no)
    if not d: return ''
    return ('<article class="mc item" data-kind="cover" data-mood="%s" data-q="%s"><a href="%scovers/%d.html" target="_blank" rel="noopener"><img src="%s%s%s" alt="%s 표지" loading="lazy" width="640" height="360">'
            '<span class="tri">%s</span></a>'
            '<b>%s <small>#%d</small></b><p>%s</p>'
            '<p class="lk"><a href="%scovers/%d.html" target="_blank" rel="noopener">10장 넘겨 보기</a> · <a href="%s%s%s">원본 표지</a></p></article>') % (
        E(next((s['mood'] for s in STYLES if s['id'] == f), '')), E(name(r) + ' ' + (kit.NAMES.get(f, '') if f else '')), up, no, up, E(r['thumb']), ver(r), E(name(r)),
        ''.join('<img src="%scovers/thumbs/%d-%d.jpg" alt="%s 본문 예" loading="lazy" width="640" height="360">' % (up, no, k, E(name(r))) for k in (2, 4, 8)),
        E(name(r)), no, ('<span class="badge ok">표지의 장치를 본문까지</span> %s' % E(d['device'])) if d.get('bespoke') else
        ('<span class="badge">색 · 글꼴만 맞춤</span> 배치는 <a href="%sstyles/%s.html">%s</a>에서' % (up, d['base'], E(kit.NAMES[d['base']]))), up, no, up, E(r['file']), ver(r))

# ── index.html ──
H = ['''<section class="hero"><div><h1>표지부터 마무리까지,<br>하나의 스타일로.</h1>
<p class="lead">발표자료 디자인을 고르고, AI에게 내 발표에 적용해 달라고 요청하는 곳입니다.</p></div>
<div class="ask"><span>어떤 스타일이 좋을지 고민되나요?</span><button type="button" class="btn fill" data-copy="reqPick">AI에게 추천 맡기기 — 요청문 복사</button></div></section>
<ol class="steps"><li>스타일 고르기</li><li>전체 장표 확인하기</li><li>AI에 적용 요청하기</li></ol>
<h2 id="styles">전체 스타일 <small>표지 · 본문 · 마무리를 함께 확인하세요</small></h2>
<div class="tools"><div class="chips" id="moods" role="group" aria-label="분위기"><button type="button" data-m="" aria-pressed="true">전체</button>%s</div>
<input type="search" id="q" placeholder="스타일이나 분위기 검색" aria-label="스타일 검색"><label><input type="checkbox" id="only"> 완성된 세트만</label></div>
<div class="cards" id="cards">''' % ''.join('<button type="button" data-m="%s" aria-pressed="false">%s</button>' % (m, m) for m in MOODS)]
for s in sorted(STYLES, key=lambda s: (not s.get('verified'), s['id'])):
    st = status(s)
    H.append('''<article class="sc item" data-kind="set" data-id="%s" data-mood="%s" data-ok="%d" data-q="%s">
<a class="cv" href="styles/%s.html"><img src="%s" alt="%s 표지" loading="lazy" width="640" height="360"></a>
<div class="tri">%s</div>
<h3>%s</h3><p>%s</p>
<div class="ft"><span class="badge %s" title="%s">%s</span><a class="btn small" href="styles/%s.html">전체 장표 보기 →</a>
<label class="cmp"><input type="checkbox" class="cmpbox" value="%s" aria-label="%s 비교에 담기"> 비교에 담기</label></div></article>''' % (
        s['id'], s['mood'], 1 if s.get('verified') else 0, E(s['name'] + ' ' + s['mood'] + ' ' + s['use']), s['id'], th(s['id'], '-set', 1), E(s['name']),
        ''.join('<img src="%s" alt="%s 본문 예" loading="lazy" width="640" height="360">' % (th(s['id'], '-set', n), E(s['name'])) for n in (role_slide('flow', s['id']), role_slide('compare', s['id']), role_slide('numbers', s['id']))),
        E(s['name']), E(s['use']), 'ok' if s.get('verified') else 'wip', E(STATUS_NOTE[st]), '10장 세트 · ' + st, s['id'], s['id'], E(s['name'])))
H.append('</div><p class="empty" id="none" hidden>조건에 맞는 스타일이 없습니다. 검색어를 지우거나 다른 분위기를 골라 보세요.</p>')
H.append('<div id="coverwrap"><h2 id="covers">표지에서 넓힌 덱 <small>%d벌 — 표지마다 10장, 구성 조합이 모두 다릅니다</small></h2>' % len(covers))
NB = sum(1 for d in CDECK.values() if d.get('bespoke'))
H.append('<p class="note"><b>표지의 장치를 본문까지</b> %d벌: 그 표지만의 장치(띠 · 절취선 · 이름표 같은 것)를 본문 틀로 옮기고, 기존 본문 장표를 빌려 섞었습니다. <b>색 · 글꼴만 맞춤</b> %d벌: 아직 색과 글꼴만 입힌 상태입니다. 하나씩 옮기는 중입니다.</p>' % (NB, len(CDECK) - NB) + '<div class="minis">%s</div></div>' % ''.join(cover_card(r) for r in sorted(covers, key=lambda r: (not CDECK.get(r['no'], {}).get('bespoke'), r['no']))))
H.append('<h2>필요한 본문만 찾고 싶다면</h2><div class="short">%s</div>' % ''.join('<a href="body.html#r-%s">%s</a>' % (r['id'], E(r['name'])) for r in ROLES if r['id'] not in ('cover', 'closing', 'more')))
H.append('<pre class="req" id="reqPick" hidden>%s</pre>' % E(REQ_PICK))
H.append('<div class="tray" id="tray" hidden><span id="trayN"></span><button type="button" id="trayGo">비교하기</button><button type="button" id="trayX" aria-label="비교 비우기">비우기</button></div>'
         '<dialog id="cmp" aria-label="스타일 비교"><div class="cmpgrid" id="cmpgrid"></div><div class="acts"><button type="button" class="btn" id="cmpClose">닫기</button></div></dialog>')
INDEX_JS = r'''
const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const S = %s;
let mood = '', picked = [];
// 고른 것은 주소에 남는다: 스타일 화면에 갔다 돌아와도 그대로(?mood=단정한&q=…&only=1)
function sync(){ const u = new URLSearchParams(); if (mood) u.set('mood', mood); if ($('#q').value.trim()) u.set('q', $('#q').value.trim()); if ($('#only').checked) u.set('only', '1');
  const qs = u.toString(); history.replaceState(null, '', qs ? '?' + qs + location.hash : location.pathname + location.hash); }
function apply(){
  const q = $('#q').value.trim().toLowerCase(), only = $('#only').checked; let n = 0;
  $$('.item').forEach(el => { const ok = (!mood || el.dataset.mood === mood) && (!q || el.dataset.q.toLowerCase().includes(q)) && (!only || el.dataset.ok === '1'); el.hidden = !ok; if (ok && el.dataset.kind === 'set') n++; });
  $('#none').hidden = n > 0; $('#coverwrap').hidden = only || !$$('#coverwrap .item').some(el => !el.hidden);
  $$('#moods button').forEach(b => b.setAttribute('aria-pressed', b.dataset.m === mood)); sync();
}
$('#moods').addEventListener('click', e => { const b = e.target.closest('button'); if (b) { mood = b.dataset.m; apply(); } });
$('#q').addEventListener('input', apply); $('#only').addEventListener('change', apply);
const u0 = new URLSearchParams(location.search); mood = u0.get('mood') || ''; $('#q').value = u0.get('q') || ''; $('#only').checked = u0.get('only') === '1'; apply();
// 비교: 스타일을 둘 이상 담아 같은 구성끼리 나란히 본다
function tray(){ picked = $$('.cmpbox:checked').map(c => c.value); $('#tray').hidden = picked.length < 1; $('#trayN').textContent = picked.length < 2 ? '비교할 스타일을 하나 더 담으세요' : picked.length + '개 담음'; $('#trayGo').disabled = picked.length < 2; }
document.addEventListener('change', e => { if (e.target.classList.contains('cmpbox')) tray(); });
$('#trayX').addEventListener('click', () => { $$('.cmpbox').forEach(c => c.checked = false); tray(); });
$('#trayGo').addEventListener('click', () => {
  $('#cmpgrid').innerHTML = picked.map(id => { const s = S[id]; return `<div class="row"><b><a href="styles/${id}.html">${s.name}</a></b>` + s.th.map((t, i) => `<img src="${t}" alt="${s.name} ${s.lab[i]}" loading="lazy">`).join('') + '</div>'; }).join('');
  $('#cmp').showModal(); $('#cmpClose').focus(); });
$('#cmp').addEventListener('click', e => { if (e.target.id === 'cmpClose' || e.target === $('#cmp')) $('#cmp').close(); });
''' % json.dumps({s['id']: {'name': s['name'], 'th': [th(s['id'], '-set', n) for n in (1, role_slide('flow', s['id']), role_slide('compare', s['id']), role_slide('numbers', s['id']), 10)], 'lab': ['표지', '흐름', '비교', '수치', '마무리']} for s in STYLES}, ensure_ascii=False)
sizes = {'index': page('index.html', '발표 디자인 라이브러리 — 표지부터 마무리까지 하나의 스타일로', '발표자료 디자인을 고르고 AI에게 내 발표에 적용해 달라고 요청하는 갤러리. 표지 · 본문 · 마무리가 한 벌인 스타일 세트.', 'index.html', '\n'.join(H), INDEX_JS)}

# ── 역할별 구성 셋(스타일 화면 · 본문 구성 · catalog 가 함께 쓴다) ──
def var_cards(role, f, up='', mark=False):
    """그 역할의 구성 셋을 스타일 f 로 나란히. mark = 그 스타일의 10장 예시가 쓴 구성에 표시"""
    out = []
    for v in VAR['roles'][role]:
        n = VARN[(role, v['v'])]; on = mark and kit.pick(f, role) == v['v']
        use = ' · '.join(u['name'] for u in users(role, v['v']))
        out.append('<a class="vc%s" href="%skit/%s-var.html#%d" target="_blank" rel="noopener" data-n="%d"><img src="%s%s" alt="%s · %s" loading="lazy" width="640" height="360">'
                   '<b>%s%s</b><p class="w">%s</p><p>이럴 때 · %s</p><p>분량 · %s%s</p></a>' % (
            ' on' if on else '', up, f, n, n, up, th(f, '-var', n), E(RN[role]['name']), E(v['name']), E(v['name']), ' <span class="badge ok">이 예시에 씀</span>' if on else '',
            E(v['look']), E(v['when']), E(v['cond']), '' if mark else ('<br>10장 예시에 쓴 스타일 · ' + E(use or '없음'))))
    return '<div class="var3">%s</div>' % ''.join(out)

# ── styles/{id}.html ──
for s in STYLES:
    f, st, up = s['id'], status(s), '../'
    fam_cov = [r for r in covers if r.get('family') == f]
    B = ['<p class="note"><a href="../index.html">← 전체 스타일</a></p><h1>%s</h1><p class="lead">%s</p><p class="note"><span class="badge %s">%s</span> %s%s</p>' % (
        E(s['name']), E(s['use']), 'ok' if s.get('verified') else 'wip', '10장 세트 · ' + st, E(STATUS_NOTE[st]), (' · 확인한 날 ' + E(s['verified']['date'])) if s.get('verified') else '')]
    if s.get('todo'): B.append('<p class="note"><b>남은 일</b> · %s</p>' % E(s['todo']))
    B.append('<div class="two"><div><div class="view"><iframe src="../kit/%s-set.html" title="%s 10장 예시 발표" loading="lazy"></iframe></div><p class="note">화면을 누르거나 → 키로 넘깁니다. <a href="../kit/%s-set.html" target="_blank" rel="noopener">새 창에서 크게 보기</a></p></div>' % (f, E(s['name']), f))
    B.append('<div><dl class="kv"><dt>분위기</dt><dd>%s</dd><dt>유지할 것</dt><dd><ul>%s</ul></dd><dt>바꿔도 됨</dt><dd><ul>%s</ul></dd><dt>피할 것</dt><dd><ul>%s</ul></dd></dl>' % (
        E(s['mood']), ''.join('<li>%s</li>' % E(x) for x in s['keep']), ''.join('<li>%s</li>' % E(x) for x in s['change']), ''.join('<li>%s</li>' % E(x) for x in s['avoid'])))
    B.append('<div class="acts"><button type="button" class="btn fill" data-copy="req">이 스타일 적용 요청문 복사</button><a class="btn" href="../kit/%s-set.html" download="%s-예시발표.html">예시 발표 내려받기(.html)</a></div>' % (f, E(s['name'])))
    B.append('<p class="note">내려받은 파일은 글꼴 · 그림이 안에 들어 있어 인터넷 없이 열립니다. AI가 새로 만든 발표는 열 때 인터넷이 필요합니다.</p></div></div>')
    B.append('<h2>전체 장표 <small>10장 — 역할마다 한 장. 예시 내용은 가상입니다</small></h2><div class="minis">%s</div>' % ''.join(
        '<a class="mc" href="../kit/%s-set.html#%d" target="_blank" rel="noopener"><img src="../%s" alt="%s %d장" loading="lazy" width="640" height="360"><b>%d. %s</b></a>' % (
            f, x['n'], th(f, '-set', x['n']), E(s['name']), x['n'], x['n'], E(x['title'])) for x in SETS[f]))
    B.append('<p class="note">이 스타일의 짜임 · %s. 스타일마다 구성 조합이 다릅니다.</p>' % ' / '.join('%s = %s' % (E(RN[r]['name'].split(' · ')[0]), E(next(v['name'] for v in VAR['roles'][r] if v['v'] == kit.pick(f, r)))) for r in VAR['order']))
    B.append('<h2>다른 내용에 써 보기 <small>성격이 다른 본문 %d장 — 가상 주제: 학교 독서 활동</small></h2><div class="minis">%s</div>' % (len(SET2), ''.join(
        '<a class="mc" href="../kit/%s-set2.html#%d" target="_blank" rel="noopener"><img src="../%s" alt="" loading="lazy" width="640" height="360"><b>%s</b></a>' % (f, x['n'], th(f, '-set2', x['n']), E(x['title'])) for x in SET2)))
    B.append('<h2>다른 구성으로 바꾸기 <small>역할마다 배치가 다른 구성 셋 — 내용에 맞는 것을 고릅니다</small></h2><p class="note">파란 테두리가 위 10장 예시에 쓴 구성입니다. 나머지 둘도 이 스타일로 그대로 쓸 수 있습니다. <a href="../kit/%s-var.html" target="_blank" rel="noopener">구성 모음 넘겨 보기</a></p>' % f)
    for r in VAR['order']: B.append('<h3>%s <small>%s</small></h3>%s' % (E(RN[r]['name']), E(RN[r]['purpose']), var_cards(r, f, '../', True)))
    B.append('<h2>AI에게 전달하기</h2><p class="note">아래 요청문을 복사해 발표 내용과 함께 AI 대화창에 붙여 넣으세요. 주소만 건네는 것으로는 적용이 끝나지 않습니다. AI가 구성안을 먼저 보여 주면 확인한 뒤 만들게 하세요.</p><pre class="req" id="req">%s</pre>' % E(req_apply(s)))
    B.append('<details><summary>파일과 자료</summary><ul><li>적용 안내(AI용, 디자인 규칙 · 구성별 코드 · 뼈대): <a href="../kit/%s.md">kit/%s.md</a></li><li>스타일 CSS: <a href="../kit/v1/%s.css">kit/v1/%s.css</a> · 넘김 엔진: <a href="../kit/v1/deck.js">kit/v1/deck.js</a></li>'
             '<li>더 많은 구성 예시: <a href="../kit/%s-plan.html">계획안 발표 12장</a>(체계 · 일정 · 표 · 구성비) · <a href="../kit/%s.html">성과 공유회 13장</a>(막대 · 전후 · 사진)</li>'
             '<li>글꼴: SIL OFL 1.1(<a href="../fonts/LICENSES.md">고지</a>)%s</li></ul></details>' % (f, f, f, f, f, f, ' · 그림: 이 갤러리의 기존 장표에서 떠낸 것(<code>kit/img/</code>)' if f in 'EGH' else ''))
    if fam_cov: B.append('<h2>같은 분위기의 표지 덱 <small>%d벌 — 표지마다 색 · 글꼴과 구성 조합이 다릅니다</small></h2><div class="minis">%s</div>' % (len(fam_cov), ''.join(cover_card(r, '../') for r in fam_cov)))
    sizes['styles/' + f] = page('styles/%s.html' % f, '%s — 발표 디자인 라이브러리' % s['name'], s['use'], 'index.html', '\n'.join(B), up='../')

# ── body.html: 역할마다 배치가 다른 구성을 나란히 ──
B = ['<h1>본문 구성</h1><p class="lead">같은 내용도 보여 주는 방식이 여럿입니다. 역할마다 <b>배치가 다른 구성 셋</b>을 나란히 놓았습니다. 내용에 맞는 구성을 고르세요.</p><div class="short" style="margin-top:20px">%s</div>' % ''.join(
    '<a href="#r-%s">%s</a>' % (r, E(RN[r]['name'])) for r in VAR['order'] + ['more']),
     '<div class="sw"><span>입혀 볼 스타일</span><div class="chips" id="sw" role="group" aria-label="입혀 볼 스타일">%s</div></div>' % ''.join(
         '<button type="button" data-f="%s" aria-pressed="%s">%s</button>' % (s['id'], 'true' if s['id'] == 'B' else 'false', E(s['name'])) for s in STYLES)]
for r in VAR['order']:
    B.append('<h2 id="r-%s">%s <small>%s</small></h2>%s' % (r, E(RN[r]['name']), E(RN[r]['purpose']), var_cards(r, 'B')))
    if RN[r]['instead'] != '—': B.append('<p class="note">이럴 땐 · %s</p>' % E(RN[r]['instead']))
# 구성 모음에 없는 모양(다른 예시 덱에 있는 것)
used = {s['pattern'] for s in slides if s['id'] == 'var'}
rest = [(p, next((x for x in slides if x['pattern'] == p['id'] and x['id'] != 'set'), None)) for p in kit.PATTERNS if p['id'] not in used]
B.append('<h2 id="r-more">그 밖의 구성 <small>갈래 · 체계 · 추이 · 구성비 · 사진 · 간지</small></h2><div class="minis">%s</div>' % ''.join(
    '<a class="mc" href="kit/B%s.html#%d" target="_blank" rel="noopener" data-n="%d" data-deck="%s"><img src="%s" alt="%s" loading="lazy" width="640" height="360"><b>%s</b><p>%s</p><p>분량 · %s</p></a>' % (
        x['deck'], x['n'], x['n'], x['deck'], th('B', x['deck'], x['n']), E(p['name']), E(p['name']), E(p['when']), E(p['cond'])) for p, x in rest if x))
B.append('<h2>참고 장표와 아이콘</h2><p class="note">스타일 세트와 따로 만든 본문 장표 %d개(도식 아이디어 참고용)와 아이콘 85개는 <a href="refs.html">참고 장표 모음</a>에 있습니다.</p>' % sum(1 for r in vis if r['role'] == '본문'))
BODY_JS = r"""
// 입혀 볼 스타일을 바꾸면 그림과 주소만 바뀐다(구성은 그대로). 고른 스타일은 주소에 남는다(?style=D)
const sw = document.getElementById('sw');
function skin(f){ if (!/^[A-H]$/.test(f)) f = 'B';
  document.querySelectorAll('[data-n]').forEach(a => { const d = a.dataset.deck === undefined ? '-var' : a.dataset.deck, n = a.dataset.n;
    a.href = 'kit/' + f + d + '.html#' + n; a.querySelector('img').src = 'kit/thumbs/' + f + d + '-' + n + '.jpg'; });
  sw.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', b.dataset.f === f));
  history.replaceState(null, '', (f === 'B' ? location.pathname : '?style=' + f) + location.hash); }
sw.addEventListener('click', e => { const b = e.target.closest('button'); if (b) skin(b.dataset.f); });
const f0 = new URLSearchParams(location.search).get('style'); if (f0) skin(f0);
"""
sizes['body'] = page('body.html', '본문 구성 — 발표 디자인 라이브러리', '흐름 · 개념 · 비교 · 절차 · 사례 · 실습 · 수치 · 요약마다 배치가 다른 구성 셋을 나란히 보고 고른다.', 'body.html', '\n'.join(B), BODY_JS)

# ── motion.html · print.html ──
def ref_card(r):
    return '<article class="mc"><a href="%s%s" target="_blank" rel="noopener"><img src="%s%s" alt="%s" loading="lazy" width="640" height="360"></a><b>%s <small>#%d</small></b><p>%s</p></article>' % (
        E(r['file']), ver(r), E(r['thumb']), ver(r), E(name(r)), E(name(r)), r['no'], E((r.get('takeaway') or r.get('topic') or '')[:70]))
mot = [r for r in covers if r.get('motion') == '인터랙션']
B = ['<h1>모션 · 강조</h1><p class="lead">청중의 눈을 붙잡는 연출과, 눌러서 조작하는 표지입니다. 일반 발표 세트와는 따로 씁니다.</p>',
     '<h2>와우 포인트 24 <small>발표 연출 기법 9장</small></h2><div class="minis"><a class="mc" href="wow/wow.html"><img src="thumbs/hub-wow-1.jpg" alt="와우 포인트 24" loading="lazy" width="640" height="360"><b>와우 포인트 24</b><p>드러내기 · 대비 · 숫자 체감 · 은유 · 감각 · 소리가 보이는 모션. 장마다 실제로 움직입니다</p></a></div>',
     '<h2>눌러서 조작하는 표지 <small>%d개 — 발표 중에 직접 눌러야 합니다</small></h2><div class="minis">%s</div>' % (len(mot), ''.join(ref_card(r) for r in mot))]
sizes['motion'] = page('motion.html', '모션 · 강조 — 발표 디자인 라이브러리', '발표 연출 기법과 눌러서 조작하는 표지.', 'motion.html', '\n'.join(B))
pr = [r for r in vis if r['role'] == '인쇄·홍보물']; fr = [r for r in vis if r['role'] == '발표 틀']
B = ['<h1>인쇄 · 홍보물</h1><p class="lead">화면 발표가 아닌 종이 · 게시용 디자인과, 넘기는 방식이 다른 특수 발표 틀입니다.</p>',
     '<h2>인쇄 · 홍보물 <small>%d개 — 포스터 · 리플렛 · 소식지</small></h2><div class="minis">%s</div>' % (len(pr), ''.join(ref_card(r) for r in pr)),
     '<h2>특수 발표 틀 <small>%d개 — 허브 · 스크롤 · 탐험처럼 자체 진행 방식을 가진 것</small></h2><div class="minis">%s</div>' % (len(fr), ''.join(ref_card(r) for r in fr))]
sizes['print'] = page('print.html', '인쇄 · 홍보물 — 발표 디자인 라이브러리', '포스터 · 리플렛 · 소식지와 특수 발표 틀.', 'print.html', '\n'.join(B))

# ── guide.html ──
n_ok = sum(1 for s in STYLES if s.get('verified'))
B = ['<h1>이용 방법</h1><p class="lead">발표 내용을 먼저 정하고, 스타일을 고른 다음, AI에게 적용을 요청합니다.</p>',
     '<h2>1. 스타일을 직접 고를 때</h2><ol><li><a href="index.html">전체 스타일</a>에서 마음에 드는 스타일의 <b>전체 장표 보기</b>를 누릅니다.</li><li>10장 예시를 넘겨 보고, <b>이 스타일 적용 요청문 복사</b>를 누릅니다.</li><li>AI 대화창에 발표 내용(문서)과 함께 붙여 넣습니다. AI가 장별 구성안을 먼저 보여 주면 확인하고 만들게 합니다.</li><li>받은 .html 파일을 열어 → 키로 넘겨 보고, 숫자를 원문과 대조합니다.</li></ol>',
     '<h2>2. 고르는 것도 AI에게 맡길 때</h2><p>아래 요청문을 복사해 발표 내용과 함께 붙여 넣습니다.</p><div class="acts"><button type="button" class="btn fill" data-copy="reqPick">선택을 맡기는 요청문 복사</button></div><pre class="req" id="reqPick">%s</pre>' % E(REQ_PICK),
     '<h2>알아 둘 점</h2><ul><li><b>완성 상태</b>: 검증된 세트(10장 예시 · 다른 주제 시험 · 넘침 검사 통과) %d개 · 확장 중 %d개 · 표지에서 넓힌 덱 %d벌(표지의 색 · 글꼴을 입힌 10장).</li><li>AI가 만든 발표는 열 때 인터넷이 필요합니다(글꼴 · 스타일을 이 사이트에서 불러옵니다). 내려받은 예시 발표는 인터넷 없이 열립니다.</li><li>개인정보(학생 이름 · 사진)는 AI에게 넣지 마세요.</li><li>AI가 주소를 열지 못하는 환경이면, 스타일 화면의 "파일과 자료"에서 적용 안내(.md)를 내려받아 첨부하세요.</li></ul>' % (n_ok, len(STYLES) - n_ok, len(covers)),
     '<details><summary>제작 정보(개발 · 관리용)</summary><ul><li>AI가 읽는 목록: <a href="catalog.md">catalog.md</a></li><li>작업 기록과 다음 할 일: <a href="docs/worklog.md">docs/worklog.md</a></li><li>분류 기준: <a href="docs/patterns.md">docs/patterns.md</a> · 제작 기준: <a href="docs/criteria.md">docs/criteria.md</a></li><li>참고 장표 모음(기존 장표 전체 · 아이콘): <a href="refs.html">refs.html</a> · 스타일 묶음 파일: <a href="kit/index.html">kit/</a></li><li>저장소 구조와 빌드: <a href="https://github.com/szxv7704-dot/design-reference-gallery#readme">README</a></li></ul></details>']
sizes['guide'] = page('guide.html', '이용 방법 — 발표 디자인 라이브러리', '스타일을 고르고 AI에게 적용을 요청하는 방법.', 'guide.html', '\n'.join(B))

# ── catalog.md: AI가 읽는 차례 ──
C = ['# 발표 디자인 라이브러리 — AI가 읽는 목록', '',
     '> 사용자가 발표 내용과 함께 이 주소를 주면, 아래 순서로 스타일을 고르고 적용합니다. 모든 예시의 기관명 · 수치 · 사례는 가상이니 새 발표에 가져오지 마세요.',
     '> `scripts/gallery.py`가 `data/styles.json` · `data/roles.json` · `data/patterns.json`에서 만든 파일입니다. 사이트 화면과 같은 데이터입니다.', '',
     '## 적용 순서', '',
     '1. 발표 내용과 각 장이 전하려는 것을 파악한다(누구에게, 몇 분, 장마다 한 가지).',
     '2. 전체 스타일 하나를 고른다. 기본은 아래 표의 **검증된 세트** 중에서.',
     '3. 장마다 알맞은 본문 구성을 고른다(아래 "구성" 표). 한 장에 구성 하나.',
     '4. 고른 스타일의 **적용 안내**(표의 주소)를 열어 디자인 규칙 · 구성별 코드 · HTML 뼈대를 확인한다.',
     '5. 유지할 요소를 지키면서 실제 내용을 넣는다. 내용이 넘치면 글자를 줄이지 말고 장을 나눈다. 사용자의 핵심 내용을 임의로 빼지 않는다.',
     '6. 전체가 한 스타일로 보이는지, 글자가 잘리지 않는지, 장이 넘어가는지 확인한다.', '',
     '**자료를 실제로 열어 읽지 못했다면 읽고 적용한 것처럼 말하지 않는다.** 열 수 없는 주소가 있으면 사용자에게 그 파일을 첨부해 달라고 한다. 사용자가 주지 않은 숫자 · 사실을 지어내지 않는다.', '',
     '## 스타일', '', '| ID | 이름 | 분위기 | 알맞은 전달 목적 | 상태 | 적용 안내 | 10장 예시 | 화면 |', '|---|---|---|---|---|---|---|---|']
for s in STYLES:
    C.append('| %s | %s | %s | %s | %s | %skit/%s.md | %skit/%s-set.html | %sstyles/%s.html |' % (s['id'], s['name'], s['mood'], s['use'], status(s), BASE, s['id'], BASE, s['id'], BASE, s['id']))
C += ['', '상태: **검증된 세트** = ' + STATUS_NOTE['검증된 세트'] + ' / **확장 중** = ' + STATUS_NOTE['확장 중'] + '.', '']
for s in STYLES:
    C += ['### %s %s' % (s['id'], s['name']), '- 유지할 것: ' + ' / '.join(s['keep']), '- 바꿔도 되는 것: ' + ' / '.join(s['change']), '- 피할 것: ' + ' / '.join(s['avoid']), '']
C += ['## 표지에서 넓힌 덱 (%d벌)' % len(CDECK), '',
      '표지 하나마다 10장: 원본 표지 + 본문 여덟 역할 + 마무리. 표지의 색 · 글꼴을 입혔고 배치는 "바탕" 스타일에서 빌렸다. 표지마다 구성 조합이 다르다.',
      '적용하려면: 바탕 스타일의 적용 안내(`kit/{바탕}.md`)를 따르되 **`<link>` 주소만 아래 CSS로 바꾸고**, 상징 부품(표지 · 목차 · 마무리에 넣는 그림)은 넣지 않는다. 표지 장은 사용자의 제목으로 새로 쓴다(원본 표지 장표는 그대로 가져오지 않는다).', '',
      '| 번호 | 이름 | 바탕 | 10장 덱 | CSS | 상태 — 장치 또는 구성 조합 |', '|---|---|---|---|---|---|']
for no in sorted(CDECK):
    d = CDECK[no]; C.append('| #%d | %s | %s | %scovers/%d.html | %scovers/%d.css | %s |' % (no, d['name'], d['base'], BASE, no, BASE, no,
        ('**표지의 장치를 본문까지** — ' + d['device'] + ' · 빌린 본문 ' + ' '.join('#%d' % x for x in d['refs'])) if d.get('bespoke') else '색 · 글꼴만 맞춤 — ' + ' / '.join(d['combo'])))
C += ['']
C += ['## 구성 (역할마다 배치가 다른 셋. 모든 스타일에서 같은 이름으로 쓴다)', '', '| 역할 | 구성 | 모습 | 이럴 때 | 알맞은 분량 | 부품 | 보기(B 스타일) |', '|---|---|---|---|---|---|---|']
for r in VAR['order']:
    for i, v in enumerate(VAR['roles'][r]): C.append('| %s | %s | %s | %s | %s | `%s` | %skit/B-var.html#%d |' % (RN[r]['name'] if i == 0 else '', v['name'], v['look'], v['when'], v['cond'], v['part'], BASE, VARN[(r, v['v'])]))
C += ['', '그 밖의 구성(갈래 · 체계 · 추이 · 구성비 · 표 · 일정 · 사진 · 간지)과 모든 구성의 코드는 각 스타일의 적용 안내(`kit/{ID}.md`)에 들어 있다.',
      '**장마다 내용에 맞는 구성을 고른다.** 같은 역할이 여러 번 나오면 구성을 바꿔 쓴다. 넘치면 글자를 줄이지 말고 장을 나눈다.', '',
      '### 스타일별 10장 예시의 구성 조합', '', '스타일마다 예시의 짜임이 다르다. 참고일 뿐이고 그대로 따를 필요는 없다.', '',
      '| 스타일 | ' + ' | '.join(RN[r]['name'].split(' · ')[0] for r in VAR['order']) + ' |', '|---|' + '---|' * len(VAR['order'])]
for s in STYLES: C.append('| %s %s | %s |' % (s['id'], s['name'], ' | '.join(next(v['name'] for v in VAR['roles'][r] if v['v'] == kit.pick(s['id'], r)) for r in VAR['order'])))
C += ['',
      '## 그 밖', '',
      '- 표지 레퍼런스 설명(분위기 · 가져갈 장치): %scatalog/refs.md' % BASE,
      '- 참고 본문 장표(도식 아이디어): %scatalog/body.md · 아이콘 85개: %scatalog/icons.md' % (BASE, BASE),
      '- 사람용 이용 방법: %sguide.html' % BASE, '']
open(os.path.join(ROOT, 'catalog.md'), 'w', encoding='utf-8').write('\n'.join(C))
print('화면(글자 수):', sizes, '· catalog.md', os.path.getsize(os.path.join(ROOT, 'catalog.md')) // 1024, 'KB')
