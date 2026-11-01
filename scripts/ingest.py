# 새 회차 한 번에 넣기: refs/{번호}.html(아티팩트에서 받은 원본) → src/ 추출 → 없는 글꼴 받기 → 인터넷 없이 빌드 → 검사
# 순서: refs/{번호}.html 저장 → (data/rounds.json · thumbs 갱신) → node scripts/add-code.js refs/{번호}.html → 이 스크립트
# 실행: python3 scripts/ingest.py 111 [112 …]   (끝 상태 코드 0 = 모두 통과, 통과한 회차는 v 도 다시 계산)
# 필요한 것: pip install fonttools brotli · node + playwright
import hashlib, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import extract, build
def run(*a): return subprocess.run(a, cwd=ROOT).returncode
bad = []
for no in sys.argv[1:]:
    extract.extract(no)
    need = json.load(open(os.path.join(ROOT, 'fonts', 'needed.json')))
    cfg = json.load(open(os.path.join(ROOT, 'src', no, 'build.json')))
    miss = [(f, w) for f, w in cfg['fonts'] if not os.path.exists(os.path.join(ROOT, 'fonts', '%s-%s.woff2' % (f.replace(' ', ''), w)))]
    if miss:
        for f, w in miss: need.setdefault(f, []); need[f] = sorted(set(need[f]) | {w})
        json.dump(dict(sorted(need.items())), open(os.path.join(ROOT, 'fonts', 'needed.json'), 'w'), ensure_ascii=False, indent=1)
        run(sys.executable, 'scripts/fetch_fonts.py'); run(sys.executable, 'scripts/pack_fonts.py')
    try: build.build(no, os.path.join(ROOT, 'refs'))
    except SystemExit as e: print('빌드 실패', no, e); bad.append(no); continue
    if run('node', 'scripts/check.js', 'refs', no) != 0: bad.append(no); continue
    rep = json.load(open(os.path.join(ROOT, 'check', 'report.json')))
    if not rep.get(no, {}).get('ok'): bad.append(no); print('검사 실패', no, rep.get(no)); continue
    # 통과한 회차만 rounds.json 의 v(= md5(html+썸네일) 앞 8자리)를 다시 계산
    rp = os.path.join(ROOT, 'data', 'rounds.json'); rounds = json.load(open(rp))
    for r in rounds:
        if str(r['no']) == no:
            h = open(os.path.join(ROOT, 'refs', no + '.html'), 'rb').read()
            t = open(os.path.join(ROOT, r['thumb']), 'rb').read() if r.get('thumb') and os.path.exists(os.path.join(ROOT, r['thumb'])) else b''
            r['v'] = hashlib.md5(h + t).hexdigest()[:8]
    open(rp, 'w').write(json.dumps(rounds, ensure_ascii=False, indent=1) + '\n')
print('통과' if not bad else '실패: ' + ' '.join(bad)); sys.exit(1 if bad else 0)
