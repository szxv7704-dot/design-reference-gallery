# 참고 변주 한 장 넣기(루틴이 쓴다. 절차는 docs/routine.md)
#   python3 scripts/variant.py next              다음 회차 번호 · 채울 기본 장표 · 계열을 알려 준다
#   python3 scripts/variant.py new 122 B points  src/122/ 를 만든다(그 기본 장표의 키트 견본 장이 들어 있다 → 변주로 고친다)
#   python3 scripts/variant.py add 122           빌드 → 썸네일 → 검사 → rounds.json 의 v → 판정표 → 첫 화면. 하나라도 실패하면 종료 코드 1
import hashlib, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import build, kit
RP = os.path.join(ROOT, 'data', 'rounds.json')
def run(*a, **k): return subprocess.run(a, cwd=ROOT, **k).returncode
def rounds(): return json.load(open(RP, encoding='utf-8'))

def nxt():
    rs = rounds(); no = max(int(r['no']) for r in rs) + 1
    tri = json.load(open(os.path.join(ROOT, 'data', 'triage.json'), encoding='utf-8'))
    name = {p['name']: p['id'] for p in kit.PATTERNS}; name['목차·간지·맺음'] = 'toc'
    cnt = {p['id']: 0 for p in kit.PATTERNS if p['group'] != '뼈대'}   # 뼈대(표지 · 목차 · 간지 · 맺음)는 계열 키트가 맡는다
    for r in rs:
        t = tri.get(str(r['no']), {})
        pid = r.get('pattern') if r.get('pattern') in cnt else name.get(t.get('pattern'))
        if pid in cnt and not r.get('hidden') and t.get('judge', '변주') in ('변주', '기본 후보'): cnt[pid] += 1
    pid = min(cnt, key=lambda k: (cnt[k], list(cnt).index(k)))
    fam = kit.FAMS[no % len(kit.FAMS)]
    print(json.dumps({'no': no, 'pattern': pid, 'pattern_name': kit.PNAME[pid], 'family': fam, 'counts': {kit.PNAME[k]: v for k, v in cnt.items()}}, ensure_ascii=False, indent=1))

def new(no, fam, pid):
    d = os.path.join(ROOT, 'src', str(no))
    if os.path.exists(d): raise SystemExit('이미 있음: src/%s' % no)
    fid, s = kit.samples(pid)[0]
    body = '<!-- 1. %s 변주 -->\n%s' % (kit.PNAME[pid], kit.code_of(fam, fid, s))
    page = kit.HEAD % {'fam': fam, 'title': '레퍼런스 #%s' % no, 'body': body,
                       'css': '<style>\n/*@@FONTS@@*/\n/*@@KIT:%s@@*/\n/* === 변주 부품: 이 줄 아래에(토큰 변수 --ds-* 만 사용) === */\n</style>' % fam,
                       'js': '<script>\n/*@@KITJS@@*/\n</script>'}
    os.makedirs(d); open(os.path.join(d, 'page.html'), 'w', encoding='utf-8').write(page)
    cfg = json.load(open(os.path.join(ROOT, 'src', 'kit-' + fam, 'build.json'), encoding='utf-8'))
    json.dump(cfg, open(os.path.join(d, 'build.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('src/%s/page.html — 견본 장(%s)이 들어 있다. 변주로 고친 뒤 rounds.json 에 항목을 넣고 add' % (no, kit.PNAME[pid]))

def add(no):
    rs = rounds(); r = next((x for x in rs if str(x['no']) == str(no)), None)
    if not r: raise SystemExit('data/rounds.json 에 #%s 항목이 없다' % no)
    ids = [p['id'] for p in kit.PATTERNS]
    if r.get('pattern') not in ids: raise SystemExit('pattern 은 기본 장표 id 여야 한다: %s' % r.get('pattern'))
    for k in ('title', 'takeaway', 'file', 'thumb', 'role', 'motion', 'family', 'date'):
        if not r.get(k): raise SystemExit('rounds.json #%s 에 %s 가 없다' % (no, k))
    build.build(no, os.path.join(ROOT, 'refs'))
    if run('node', 'scripts/thumb.js', r['file'], r['thumb'], env=dict(os.environ, WAIT='1500')): raise SystemExit('썸네일 실패')
    if run('node', 'scripts/check.js', 'refs', str(no)): raise SystemExit('검사 실패: check/report.json 을 보고 고친다')
    h = open(os.path.join(ROOT, r['file']), 'rb').read() + open(os.path.join(ROOT, r['thumb']), 'rb').read()
    r['v'] = hashlib.md5(h).hexdigest()[:8]
    open(RP, 'w', encoding='utf-8').write(json.dumps(rs, ensure_ascii=False, indent=1) + '\n')
    if run(sys.executable, 'scripts/triage.py', stdout=subprocess.DEVNULL) or run(sys.executable, 'scripts/site.py'): raise SystemExit('판정표 · 첫 화면 생성 실패')
    print('통과 #%s — 커밋할 것: src/%s refs/%s.html %s data/ docs/triage.md index.html' % (no, no, no, r['thumb']))

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['next']: nxt()
    elif a[:1] == ['new'] and len(a) == 4: new(a[1], a[2], a[3])
    elif a[:1] == ['add'] and len(a) == 2: add(a[1])
    else: raise SystemExit(__doc__ or '사용법: variant.py next | new 번호 계열 기본장표 | add 번호')
