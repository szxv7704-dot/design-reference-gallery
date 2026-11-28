# 와우 포인트: 한 덱(wow/wow.html)에 모여 있던 기법 31가지를 기법 하나당 덱 하나로 나눈다.
#   wow/wow.css · wow/wow.js     공용(원래 덱의 스타일 · 움직임 엔진. 글꼴은 ../fonts/ 를 쓴다)
#   wow/{01..31}.html            기법 하나 = 덱 하나: 표지 · 크게 보기(실제로 움직임) · 쓰는 법
#   data/wow.json                목록(번호 · 이름 · 묶음 · 한 줄) — 화면(scripts/gallery.py)과 catalog.md 가 읽는다
# 원본은 wow/wow.html(9장 한눈에 덱)이고 그대로 둔다. 데모 마크업 · CSS · 엔진은 원본에서 그대로 가져온다(새로 그리지 않음).
# 실행: python3 scripts/wow.py
import html, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(ROOT, 'wow')
SRC = open(os.path.join(W, 'wow.html'), encoding='utf-8').read()
have = {f[:-6] for f in os.listdir(os.path.join(ROOT, 'fonts')) if f.endswith('.woff2')}

# ── 공용 CSS: 원본 스타일 두 덩이 + 글꼴은 ../fonts 로 ──
styles = re.findall(r'<style[^>]*>(.*?)</style>', SRC, re.S)
def face(m):
    fam, w = m.group(1), m.group(2); key = fam.replace(' ', '') + '-' + w
    return '@font-face{font-family:"%s";font-weight:%s;font-display:swap;src:url("../fonts/%s.woff2") format("woff2")}' % (fam, w, key) if key in have else m.group(0)
fonts = re.sub(r'@font-face\{font-family:"([^"]+)";font-weight:(\d+);[^}]*\}', face, styles[0])
EXTRA = r'''
/* ── 기법 하나 = 덱 하나(scripts/wow.py) ── */
.w1 .kick{position:absolute;left:96px;top:92px;font:500 18px var(--fm);color:var(--sub);letter-spacing:.06em}
.w1 .chip{position:absolute;left:96px;top:190px}
.w1 h1{position:absolute;left:92px;top:250px;margin:0;font:900 150px/1.02 var(--ft);letter-spacing:-.04em;color:var(--ink)}
.w1 h1 small{display:block;margin-top:26px;font:700 40px/1.2 var(--fb);letter-spacing:0;color:var(--gc)}
.w1 .sub{position:absolute;left:96px;top:640px;width:900px;margin:0;font:500 32px/1.5 var(--fb);color:var(--ink)}
.w1 .num{position:absolute;right:96px;bottom:70px;font:900 300px/.8 var(--ft);letter-spacing:-.06em;color:var(--gc);opacity:.12}
.w2 .stagebox{position:absolute;left:50%;top:196px;transform:translateX(-50%);height:610px;aspect-ratio:var(--ar,1/.9);display:flex}
.w2 .stagebox .demo{width:100%;height:100%;aspect-ratio:auto;border-radius:14px;box-shadow:0 30px 60px -36px rgba(0,0,0,.45)}
.w2 .stagebox .fullbtn{display:none}
.w2 .stepline{position:absolute;left:64px;right:64px;bottom:62px;margin:0;text-align:center;font:500 22px var(--fb);color:var(--sub)}
.w2 .stepline i{font-style:normal;color:var(--gc);font-weight:700}
.w3 .use{position:absolute;left:64px;right:64px;top:250px;display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.w3 .use > div{background:var(--surface);border-radius:12px;border-top:6px solid var(--gc);padding:26px 28px 30px}
.w3 .use dt{font:700 20px var(--fm);color:var(--gc);letter-spacing:.04em}
.w3 .use dd{margin:12px 0 0;font:500 28px/1.5 var(--fb);color:var(--ink)}
.w3 .when{position:absolute;left:64px;right:64px;top:560px;margin:0;display:flex;flex-wrap:wrap;gap:12px 14px;align-items:center;font:500 24px var(--fb);color:var(--sub)}
.w3 .when b{font:700 24px var(--fb);color:var(--ink);margin-right:6px}
.w3 .when span{padding:8px 16px;border-radius:999px;background:var(--surface);color:var(--ink)}
.w3 .sib{position:absolute;left:64px;right:64px;top:690px;margin:0;display:flex;flex-wrap:wrap;gap:10px 14px;align-items:center;font:500 22px var(--fb);color:var(--sub)}
.w3 .sib a{padding:8px 16px;border-radius:8px;border:2px solid var(--gc);color:var(--gc);text-decoration:none;font-weight:700}
'''
os.makedirs(W, exist_ok=True)
open(os.path.join(W, 'wow.css'), 'w', encoding='utf-8').write('/* scripts/wow.py 가 wow/wow.html 에서 뽑아 만든 공용 스타일. 고치지 말 것 */\n' + fonts + '\n' + styles[1] + EXTRA)

# ── 공용 JS: 원본 엔진 + 없는 요소가 있어도 돌게 ──
js = re.search(r'<script[^>]*>(.*?)</script>', SRC, re.S).group(1)
for a, b in [("const ug = document.getElementById('unitGrid');\n  for", "const ug = document.getElementById('unitGrid');\n  if (ug) for"),
             ("const fv = document.getElementById('fullv')", "const fv = document.getElementById('fullv') || document.createElement('div')"),
             ("fv.querySelector('[data-fv=replay]').onclick = replayFull;", "(fv.querySelector('[data-fv=replay]') || {}).onclick = replayFull;"),
             ("fv.querySelector('[data-fv=close]').onclick = closeFull;", "(fv.querySelector('[data-fv=close]') || {}).onclick = closeFull;")]:
    assert a in js, a; js = js.replace(a, b)
open(os.path.join(W, 'wow.js'), 'w', encoding='utf-8').write('/* scripts/wow.py 가 wow/wow.html 에서 뽑아 만든 공용 움직임 엔진. 고치지 말 것 */\n' + js)

# ── 기법 카드 나누기 ──
AR = {'c3': '4/3', 'c4': '1/.9', 'c5': '4/3'}
WIDE = {'d-pop', 'd-train', 'd-thud', 'd-asm'}   # 캔버스 데모는 넓은 화면에서 더 잘 보인다
picks = []   # (하고 싶은 말, [태그])
for tr in re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td></tr>', SRC, re.S):
    picks.append((html.unescape(re.sub('<[^>]+>', '', tr[0])), re.findall(r'<span class="tg[^"]*">([^<]+)</span>', tr[1])))
items = []
for sec in re.finditer(r'<section class="slide (g\d)" data-title="([^"]+)">(.*?)</section>', SRC, re.S):
    g, gtitle, body = sec.group(1), sec.group(2), sec.group(3)
    gname = re.search(r'<span class="chip"><b>\d</b>([^<]+)</span>', body).group(1)
    cols = re.search(r'class="cards (c\d)"', body).group(1)
    for art in re.findall(r'<article class="card">(.*?)</article>', body, re.S):
        demo = art[:art.index('<p class="steps">')].strip()
        demo = re.sub(r'\s*<button type="button" class="fullbtn"[^>]*>.*?</button>', '', demo)
        steps = re.search(r'<p class="steps">(.*?)</p>', art, re.S).group(1)
        name, small = re.search(r'<h3>(.*?)<small>(.*?)</small></h3>', art).groups()
        why = re.search(r'<p class="why">(.*?)</p>', art).group(1)
        dl = re.findall(r'<dt>(.*?)</dt><dd>(.*?)</dd>', art)
        kind = re.search(r'class="demo ([\w-]+)', demo).group(1)
        items.append(dict(g=g, gtitle=gtitle, gname=gname, ar='16/9' if kind in WIDE else AR[cols], demo=demo, steps=steps, name=name, small=small, why=why, dl=dl, kind=kind))
for i, it in enumerate(items, 1):
    it['no'] = '%02d' % i
    it['when'] = [m for m, tags in picks if any(it['name'].startswith(t) or t.startswith(it['name']) for t in tags)]

HEAD = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%(name)s — 와우 포인트 %(no)s</title>
<link rel="stylesheet" href="wow.css">
</head>
<body>
<!-- scripts/wow.py 가 만든 파일. 고치지 말 것 -->
<div class="viewport"><div class="stage" id="stage">
%(slides)s
</div></div>
<nav class="bar" aria-label="장표 넘기기">
  <button type="button" id="prev" aria-label="이전 장">←</button>
  <span class="count" id="count">1 / 3</span>
  <button type="button" id="next" aria-label="다음 장">→</button>
  <button type="button" id="replay">↻ 다시 재생</button>
  <a href="../wow.html">와우 포인트 목록</a>
</nav>
<script src="wow.js"></script>
</body>
</html>
'''
LAB = {'쓰는 곳': '쓰는 곳 · WHERE', '주의': '주의 · CAUTION', 'PPT': 'PPT로 만들 때 · HOW'}
for it in items:
    sib = [x for x in items if x['g'] == it['g'] and x is not it]
    s1 = '''<section class="slide %(g)s w1" data-title="표지">
  <div class="kick">WOW POINT %(no)s / %(total)d · 와우 포인트</div>
  <span class="chip"><b>%(gn)s</b>%(gname)s</span>
  <h1>%(name)s<small>%(small)s</small></h1>
  <p class="sub">%(why)s</p>
  <div class="num" aria-hidden="true">%(no)s</div>
  <div class="foot"><span>와우 포인트 %(no)s · %(name)s</span><span>1 / 3</span></div>
</section>''' % dict(it, gn=it['g'][1], total=len(items))
    s2 = '''<section class="slide %(g)s w2" data-title="크게 보기">
  <div class="head"><div><span class="chip"><b>%(gn)s</b>%(gname)s</span><h2>%(name)s</h2></div><div class="meta">↻ 다시 재생 · R</div></div>
  <div class="stagebox" style="--ar:%(ar)s">%(demo)s</div>
  <p class="stepline">%(steps)s</p>
  <div class="foot"><span>와우 포인트 %(no)s · %(name)s</span><span>2 / 3</span></div>
</section>''' % dict(it, gn=it['g'][1])
    s3 = '''<section class="slide %(g)s w3" data-title="쓰는 법">
  <div class="head"><div><span class="chip"><b>%(gn)s</b>%(gname)s</span><h2>%(why)s</h2></div><div class="meta">%(name)s · 쓰는 법</div></div>
  <dl class="use">%(dl)s</dl>
  %(when)s
  <p class="sib"><b style="color:var(--ink)">같은 묶음</b>%(sib)s</p>
  <div class="foot"><span>와우 포인트 %(no)s · %(name)s</span><span>3 / 3</span></div>
</section>''' % dict(it, gn=it['g'][1], dl=''.join('<div><dt>%s</dt><dd>%s</dd></div>' % (LAB.get(t, t), d) for t, d in it['dl']),
                      when=('<p class="when"><b>이럴 때</b>%s</p>' % ''.join('<span>%s</span>' % html.escape(w) for w in it['when'])) if it['when'] else '',
                      sib=''.join('<a href="%s.html">%s</a>' % (x['no'], x['name']) for x in sib))
    open(os.path.join(W, it['no'] + '.html'), 'w', encoding='utf-8').write(HEAD % dict(it, slides='\n\n'.join((s1, s2, s3))))
json.dump([{k: it[k] for k in ('no', 'name', 'small', 'why', 'g', 'gname')} | {'when': it['when'], 'use': dict(it['dl'])} for it in items],
          open(os.path.join(ROOT, 'data', 'wow.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wow/', len(items), '덱 · wow.css', os.path.getsize(os.path.join(W, 'wow.css')) // 1024, 'KB · wow.js', os.path.getsize(os.path.join(W, 'wow.js')) // 1024, 'KB')
