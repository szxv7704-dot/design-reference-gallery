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
    s = s.replace('</body>', '<script src="slide.js"></script>\n</body>', 1) if '</body>' in s else s + '<script src="slide.js"></script>'
    os.makedirs(os.path.join(ROOT, 'light'), exist_ok=True)
    open(os.path.join(ROOT, 'light', d + '.html'), 'w', encoding='utf-8').write(s); return len(s.encode('utf-8'))
SLIDE_JS = r"""// 장표만 보기: light/NN.html?slide=B  (분위기별 덱 deck.html 이 쓴다)
//  ① 페이지에서 16:9 무대만 남기고 창에 꽉 차게  ② slide= 뒤에 계열(A~H)을 주면 그 계열의 색 · 글꼴 변수(--ds-*)를 입힌다(공용 본문용)
//  이 파일은 scripts/light.py 가 kit/{계열}.css 의 :root 값에서 만든다.
(function(){
  var q = new URLSearchParams(location.search); if (!q.has('slide')) return;
  var T = @@TOKENS@@, fam = (q.get('slide') || '').replace(/[^A-H]/g, '');
  function stage(){
    var all = document.querySelectorAll('body *');
    for (var i = 0; i < all.length; i++){ var r = all[i].getBoundingClientRect(); if (r.width >= 600 && Math.abs(r.width / r.height - 16 / 9) < 0.06) return all[i]; }
    return null;
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
      if (a !== E) a.style.cssText += ';margin:0!important;padding:0!important;max-width:none!important;width:100%!important;border:0!important;box-shadow:none!important;background:none!important;border-radius:0!important';
    }
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
    open(os.path.join(ROOT, 'light', 'slide.js'), 'w', encoding='utf-8').write(SLIDE_JS.replace('@@TOKENS@@', json.dumps(T, ensure_ascii=False)))

if __name__ == '__main__':
    ds = sys.argv[1:] or sorted(d for d in os.listdir(os.path.join(ROOT, 'src')) if d.isdigit())
    sizes = [light(('%02d' % int(d)) if os.path.isdir(os.path.join(ROOT, 'src', '%02d' % int(d))) else d) for d in ds]
    slide_js()
    print('light/', len(sizes), '개 · 평균', sum(sizes) // len(sizes) // 1024, 'KB · 가장 큰 것', max(sizes) // 1024, 'KB')
