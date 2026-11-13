# 가벼운 장표(light/NN.html): src/NN/page.html 에서 글꼴 · 그림을 파일 안에 박지 않고 주소로 불러오는 판.
# refs/NN.html(인터넷 없이 도는 완성본)은 평균 800KB라 채팅 AI가 주소로 읽지 못한다. 이 판은 평균 40KB라 코드를 그대로 읽을 수 있다.
# 실행: python3 scripts/light.py        (모든 회차) · python3 scripts/light.py 121
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def light(d):
    src = os.path.join(ROOT, 'src', d)
    s = open(os.path.join(src, 'page.html'), encoding='utf-8').read(); cfg = json.load(open(os.path.join(src, 'build.json'), encoding='utf-8'))
    faces = ''.join('@font-face{font-family:"%s";font-weight:%s;font-display:swap;src:url("../fonts/%s-%s.woff2") format("woff2")}\n' % (f, w, f.replace(' ', ''), w) for f, w in cfg['fonts'])
    s = s.replace('/*@@FONTS@@*/', '/* 글꼴: 갤러리 저장소의 SIL OFL 글꼴을 주소로 불러온다 */\n' + faces, 1)
    s = re.sub(r'@@ASSET:([^@]+)@@', lambda m: '../src/%s/assets/%s' % (d, m.group(1)), s)
    if '@@IMPORTMAP:three@@' in s:
        V = '../vendor/three/'
        s = s.replace('@@IMPORTMAP:three@@', json.dumps({'imports': {'three': V + 'build/three.module.min.js',
            'three/addons/loaders/FontLoader.js': V + 'examples/jsm/loaders/FontLoader.js', 'three/addons/geometries/TextGeometry.js': V + 'examples/jsm/geometries/TextGeometry.js',
            'three/addons/environments/RoomEnvironment.js': V + 'examples/jsm/environments/RoomEnvironment.js'}}))
    # 장표만 보기(light/NN.html?slide=B): light/slide.js 가 무대만 남기고 그 분위기의 색 · 글꼴 변수를 입힌다
    # 맨 마지막 </body> 앞에(코드 칸의 글 안에도 </body> 가 있을 수 있다)
    head, sep, tail = s.rpartition('</body>')
    s = head + '<script src="slide.js"></script>\n' + sep + tail if sep else s + '<script src="slide.js"></script>'
    os.makedirs(os.path.join(ROOT, 'light'), exist_ok=True)
    open(os.path.join(ROOT, 'light', d + '.html'), 'w', encoding='utf-8').write(s); return len(s.encode('utf-8'))
SLIDE_JS = r"""// 장표만 보기: light/NN.html?slide=B  (분위기별 덱 deck.html 이 쓴다)
//  ① 페이지에서 16:9 무대만 남기고 창에 꽉 차게
//  ② slide=c17 처럼 표지 번호를 주면 그 표지에 맞춘 색 · 글꼴 변수(--ds-*)를 입힌다(공용 본문용). slide=B 는 계열 키트의 값
//  이 파일은 scripts/light.py 가 data/covers.json(표지별) · kit/{계열}.css 의 :root(계열별)에서 만든다.
(function(){
  var q = new URLSearchParams(location.search); if (!q.has('slide')) return;
  var T = @@TOKENS@@, fam = (/^(c\d+|[A-H])$/.exec(q.get('slide') || '') || [''])[0];
  function stage(){
    // 페이지 맨 위의 16:9 요소. 테두리 · 여백을 두른 틀(.stage-frame)이 먼저 잡히면, 그 안에서 16:9 에 더 가까운 진짜 무대로 내려간다
    var diff = function(el){ var r = el.getBoundingClientRect(); return r.width >= 600 && r.height > 0 ? Math.abs(r.width / r.height - 16 / 9) : 9; };
    var all = document.querySelectorAll('body *'), E = null;
    for (var i = 0; i < all.length; i++) if (diff(all[i]) < 0.06) { E = all[i]; break; }
    while (E) {   // 안쪽에 보이는 자식이 하나뿐이고(틀이 무대 하나만 감쌈) 그 자식이 16:9 에 더 가까우면 내려간다
      var kids = [].filter.call(E.children, function(c){ var r = c.getBoundingClientRect(); return r.width > 0 && r.height > 0 && c.tagName !== 'SCRIPT' && c.tagName !== 'STYLE'; });
      if (kids.length !== 1 || diff(kids[0]) >= diff(E) - 0.002) break;
      E = kids[0];
    }
    return E;
  }
  function run(){
    var E = stage(); if (!E) return;
    if (fam && T[fam]){
      var st = document.createElement('style'); st.textContent = T[fam].faces; document.head.appendChild(st);
      var targets = [document.documentElement], base = getComputedStyle(E.parentElement || E).getPropertyValue('--ds-bg');
      for (var a = E; a && a !== document.documentElement; a = a.parentElement) targets.push(a);
      // 무대 안에서 변수를 다시 선언한 요소(계열 값 묶음)도 덮는다
      [].forEach.call(E.querySelectorAll('*'), function(el){ var p = el.parentElement; if (p && getComputedStyle(el).getPropertyValue('--ds-bg') !== getComputedStyle(p).getPropertyValue('--ds-bg')) targets.push(el); });
      targets.forEach(function(el){ for (var k in T[fam].vars) el.style.setProperty(k, T[fam].vars[k], 'important'); });
    }
    // 무대만 남기기: 조상의 다른 자식은 숨기고, 조상의 여백 · 폭 제한을 푼다
    for (var a = E; a && a !== document.body; a = a.parentElement){
      var p = a.parentElement; [].forEach.call(p.children, function(c){ if (c !== a && c.tagName !== 'SCRIPT' && c.tagName !== 'STYLE') c.style.setProperty('display', 'none', 'important'); });
      if (a !== E) a.classList.add('ds-anc');   // 페이지 스크립트가 style 속성을 다시 써도 남도록 클래스로
    }
    var sa = document.createElement('style'); sa.textContent = '.ds-anc{margin:0!important;padding:0!important;max-width:none!important;width:100%!important;border:0!important;box-shadow:none!important;background:none!important;border-radius:0!important;outline:0!important}'; document.head.appendChild(sa);
    document.documentElement.style.cssText += ';margin:0;height:100%;overflow:hidden;background:#111';
    document.body.style.cssText += ';margin:0!important;padding:0!important;height:100%;overflow:hidden;background:#111!important;display:flex!important;align-items:center;justify-content:center';
    function fit(){ var w = Math.min(innerWidth, innerHeight * 16 / 9); E.style.setProperty('width', w + 'px', 'important'); E.style.setProperty('max-width', 'none', 'important'); E.style.setProperty('margin', '0 auto', 'important'); E.style.setProperty('border-radius', '0', 'important'); E.style.setProperty('box-shadow', 'none', 'important'); }
    fit(); addEventListener('resize', fit); scrollTo(0, 0);
  }
  if (document.readyState === 'complete') run(); else addEventListener('load', run);
})();
"""
def slide_js():
    """kit/{계열}.css 의 :root 토큰과 글꼴을 light/slide.js 에 넣는다"""
    T = {}
    for f in 'ABCDEFGH':
        css = open(os.path.join(ROOT, 'kit', f + '.css'), encoding='utf-8').read()
        root = re.search(r':root\{(.*?)\}', css, re.S).group(1)
        vars_ = {m.group(1): m.group(2).strip() for m in re.finditer(r'(--ds-[\w-]+)\s*:\s*([^;]+);', root)}
        fonts = json.load(open(os.path.join(ROOT, 'src', 'kit-' + f, 'build.json'), encoding='utf-8'))['fonts']
        faces = ''.join('@font-face{font-family:"%s";font-weight:%s;font-display:swap;src:url("../fonts/%s-%s.woff2") format("woff2")}' % (n, w, n.replace(' ', ''), w) for n, w in fonts)
        T[f] = {'vars': vars_, 'faces': faces}
    # 표지별 값: data/covers.json 의 다섯 값에서 --ds-* 묶음을 푼다(본문은 늘 밝은 바탕, 위계는 base 한 색의 농담)
    def mix(a, b, t):
        A, B = [int(a[i:i + 2], 16) for i in (1, 3, 5)], [int(b[i:i + 2], 16) for i in (1, 3, 5)]
        return '#%02X%02X%02X' % tuple(round(x + (y - x) * t) for x, y in zip(A, B))
    have = {}
    for fn in os.listdir(os.path.join(ROOT, 'fonts')):
        m = re.match(r'(.+)-(\d+)\.woff2$', fn)
        if m: have.setdefault(m.group(1), []).append(m.group(2))
    for no, c in json.load(open(os.path.join(ROOT, 'data', 'covers.json'), encoding='utf-8'))['covers'].items():
        fb = '"Apple SD Gothic Neo","Malgun Gothic",sans-serif'
        vars_ = {'--ds-bg': c['bg'], '--ds-surface': mix(c['bg'], '#FFFFFF', .7), '--ds-ink': c['ink'], '--ds-sub': mix(c['ink'], c['bg'], .42), '--ds-line': mix(c['ink'], c['bg'], .84),
                 '--ds-accent': c['accent'], '--ds-accent2': c['base'], '--ds-c1': mix(c['base'], c['ink'], .4), '--ds-c2': c['base'], '--ds-c3': mix(c['base'], '#FFFFFF', .32),
                 '--ds-c4': mix(c['base'], '#FFFFFF', .62), '--ds-c5': mix(c['base'], c['bg'], .86),
                 '--ds-font-title': '"%s",%s' % (c['title'], fb), '--ds-font-body': '"%s",%s' % (c['body'], fb), '--ds-font-num': '"%s","%s",%s' % (c['num'], c['body'], fb)}
        faces = ''
        for n in dict.fromkeys((c['title'], c['body'], c['num'])):
            key = n.replace(' ', '')
            if key not in have: raise SystemExit('fonts/ 에 없는 글꼴: %s (#%s)' % (n, no))
            faces += ''.join('@font-face{font-family:"%s";font-weight:%s;font-display:swap;src:url("../fonts/%s-%s.woff2") format("woff2")}' % (n, w, key, w) for w in sorted(have[key]))
        T['c' + no] = {'vars': vars_, 'faces': faces}
    open(os.path.join(ROOT, 'light', 'slide.js'), 'w', encoding='utf-8').write(SLIDE_JS.replace('@@TOKENS@@', json.dumps(T, ensure_ascii=False)))

if __name__ == '__main__':
    ds = sys.argv[1:] or sorted(d for d in os.listdir(os.path.join(ROOT, 'src')) if d.isdigit())
    sizes = [light(('%02d' % int(d)) if os.path.isdir(os.path.join(ROOT, 'src', '%02d' % int(d))) else d) for d in ds]
    slide_js()
    print('light/', len(sizes), '개 · 평균', sum(sizes) // len(sizes) // 1024, 'KB · 가장 큰 것', max(sizes) // 1024, 'KB')
