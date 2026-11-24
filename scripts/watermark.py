# 전북특별자치도교육청 로고 워터마크: 이 저장소에서 만든 모든 장표 · 화면의 오른쪽 아래에 로고를 박는다.
#  - 상업적 이용을 막기 위한 표시다. 지우거나 끄지 않는다(docs/criteria.md 0 · AGENTS.md).
#  - 모양: <style id="jbe-wm"> 한 덩이. html::after 에 로고(icons/ci/국문로고타입.png)를 data: 로 넣어 오른쪽 아래에 고정한다.
#    DOM 요소가 아니라서 장표 스크립트 · 장표만 보기(light/slide.js) · 넘침 검사에 걸리지 않고, 인터넷 없이도 보이며, 인쇄에도 찍힌다.
#    스스로 전체 화면으로 들어가는 장표(무대 요소를 전체 화면으로)는 그 무대의 ::after 에도 같은 로고를 단다.
#  - 장표를 만드는 스크립트(build · kit · covers · light · wow · gallery · site)가 쓰기 직전에 stamp() 를 부른다.
#    손으로 만든 화면(deck.html · wow/wow.html 등)과 이미 만들어진 파일은 이 스크립트로 한 번에 박는다.
# 실행: python3 scripts/watermark.py            대상 파일 전부에 박기(이미 있으면 최신 모양으로 바꿈)
#       python3 scripts/watermark.py --check    빠졌거나 옛 모양인 파일을 적고, 하나라도 있으면 종료 코드 1
import base64, glob, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(ROOT, 'icons', 'ci', '국문로고타입.png')
NAME = '전북특별자치도교육청'
# 박는 대상: 장표(refs · light · kit · covers · wow · assets 오프라인판)와 그것을 보여 주는 화면
TARGETS = ['refs/*.html', 'light/*.html', 'kit/*.html', 'covers/*.html', 'wow/*.html', 'assets/*.html',
           'styles/*.html', 'icons/icons.html', '*.html']
BLOCK = re.compile(r'<style id="jbe-wm">.*?</style>\n?', re.S)

def css():
    img = 'url(data:image/png;base64,%s)' % base64.b64encode(open(LOGO, 'rb').read()).decode()
    look = ('content:""!important;display:block!important;visibility:visible!important;opacity:.92!important;'
            'position:fixed!important;right:clamp(6px,1.1vw,18px)!important;bottom:clamp(6px,1.1vw,18px)!important;left:auto!important;top:auto!important;'
            'z-index:2147483647!important;box-sizing:content-box!important;width:clamp(84px,13vw,230px)!important;height:auto!important;aspect-ratio:351/50!important;'
            'padding:clamp(4px,.55vw,9px) clamp(6px,.85vw,14px)!important;margin:0!important;border:0!important;border-radius:clamp(4px,.5vw,8px)!important;'
            'background:rgba(255,255,255,.82) %s center/contain no-repeat content-box padding-box!important;'
            'box-shadow:0 1px 6px rgba(0,0,0,.22)!important;pointer-events:none!important;transform:none!important;filter:none!important;'
            'animation:none!important;transition:none!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important') % img
    return ('<style id="jbe-wm">/* %s 로고 워터마크 — 상업적 이용 금지. 이 블록을 지우거나 고치지 마세요(scripts/watermark.py) */\n'
            'html::after,html :not(html):fullscreen::after{%s}\n</style>\n') % (NAME, look)
CSS = css()

def stamp(s):
    """HTML 글에 워터마크를 박는다(있으면 최신 모양으로 바꾼다). 첫 </head> 앞, 없으면 첫 <body 앞, 그것도 없으면 맨 앞."""
    s = BLOCK.sub('', s, count=1)
    m = re.search(r'</head\s*>', s, re.I) or re.search(r'<body[\s>]', s, re.I)
    if m: return s[:m.start()] + CSS + s[m.start():]
    d = re.match(r'\s*<!doctype[^>]*>\s*', s, re.I)
    return s[:d.end()] + CSS + s[d.end():] if d else CSS + s
def strip(s): return BLOCK.sub('', s, count=1)
def has(s): return CSS in s

def files():
    out = []
    for g in TARGETS: out += [p for p in sorted(glob.glob(os.path.join(ROOT, g))) if p not in out]
    return out

if __name__ == '__main__':
    check = '--check' in sys.argv; bad = []; n = 0
    for p in files():
        s = open(p, encoding='utf-8').read()
        if has(s): continue
        if check: bad.append(os.path.relpath(p, ROOT)); continue
        open(p, 'w', encoding='utf-8').write(stamp(s)); n += 1
    if check:
        print('워터마크 검사: 대상 %d개, 빠짐 %d개' % (len(files()), len(bad)))
        for b in bad: print(' 빠짐', b)
        sys.exit(1 if bad else 0)
    print('워터마크를 박은 파일 %d개 (대상 %d개)' % (n, len(files())))
