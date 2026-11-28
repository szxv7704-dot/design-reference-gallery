# 표지 덱 CSS(src/covers/*.css)가 정의한 부품 이름이 공용 부품 · 바탕 스타일 이름과 겹치는지 찾는다.
# 겹치면 공용 규칙이 함께 걸려 장이 깨진다(#58 .ph · #106 .bar · #24 .split 에서 실제로 깨졌다).
# 실행: python3 scripts/cover_names.py   → 겹치는 이름이 없으면 아무것도 출력하지 않는다
import glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: open(p, encoding='utf-8').read()
shared = set()
for f in ['kit/parts.css', 'kit/deck.css'] + glob.glob(os.path.join(ROOT, 'kit', '[A-L].css')):
    shared |= set(re.findall(r'\.([a-z][\w-]*)', rd(os.path.join(ROOT, f))))
# 일부러 같은 이름으로 덮어쓰는 공용 부품(모양만 그 표지 말투로 바꾼다)
OVERRIDE = {'slide', 'title', 'kicker', 's-body', 'page-no', 'src', 'fill', 'tile', 'card', 'grid', 'points', 'check', 'stepper', 'vs', 'yesno', 'big',
            'story', 'agenda', 'define', 'say', 'quote', 'ask', 'todo', 'road', 'fix', 'ba', 'mile', 'goal', 'brief', 'tbl', 'tree', 'trend', 'share', 'shot',
            'dev', 'r-win', 'is-key', 'end', 'c-orig', 'ref', 'g3', 'g4', 'c-no', 'c-foot', 'center', 'stack', 'g-row', 'g-key'}
bad = 0
for f in sorted(glob.glob(os.path.join(ROOT, 'src', 'covers', '*.css'))):
    mine = set(re.findall(r'^\.([a-z][\w-]*)[{ ,.:>]', rd(f), re.M))
    hit = sorted(mine & shared - OVERRIDE)
    if hit: bad += 1; print(os.path.relpath(f, ROOT), hit)
raise SystemExit(1 if bad else 0)
