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
    os.makedirs(os.path.join(ROOT, 'light'), exist_ok=True)
    open(os.path.join(ROOT, 'light', d + '.html'), 'w', encoding='utf-8').write(s); return len(s.encode('utf-8'))
if __name__ == '__main__':
    ds = sys.argv[1:] or sorted(d for d in os.listdir(os.path.join(ROOT, 'src')) if d.isdigit())
    sizes = [light(('%02d' % int(d)) if os.path.isdir(os.path.join(ROOT, 'src', '%02d' % int(d))) else d) for d in ds]
    print('light/', len(sizes), '개 · 평균', sum(sizes) // len(sizes) // 1024, 'KB · 가장 큰 것', max(sizes) // 1024, 'KB')
