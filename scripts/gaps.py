# 정형 장표 빈칸 표: data/rounds.json(숨김 제외) + data/kit_slides.json 을 정형 유형별로 세어 docs/gaps.md 로
# 정형 유형 · 옮겨 세는 규칙은 docs/criteria.md 3 · index.html 의 KINDS / KIND_OF_INFO 와 같다.
# 실행: python3 scripts/gaps.py
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KINDS = ['사업 개요', '추진 체계', '추진 경과', '주요 추진 내용', '핵심 성과', '목표 대비 달성', '전년 대비·비교', '추이', '구성비', '참여 분포',
         '우수 사례', '참여자 목소리', '만족도', '전후 비교', '시사점·과제', '향후 계획', '단계·절차', '요약표', '자주 묻는 질문']
KIND_OF_INFO = {'배경·목적': '사업 개요', '비전 체계도': '사업 개요', '조직·체계': '추진 체계', '일정': '추진 경과', '분류·유목화': '주요 추진 내용',
                '핵심 수치': '핵심 성과', '비교·순위': '전년 대비·비교', '추이': '추이', '구성비': '구성비', '지도·분포': '참여 분포', '현안→해결방안': '시사점·과제',
                '흐름·절차': '단계·절차', '표·목록': '요약표'}
# 성과 공유회에서 얼마나 자주 쓰나(채울 순서의 무게): 3 = 거의 매번, 2 = 자주, 1 = 가끔(설명회 위주)
WEIGHT = {'사업 개요': 3, '추진 경과': 3, '핵심 성과': 3, '목표 대비 달성': 3, '우수 사례': 3, '참여자 목소리': 3, '만족도': 3, '전후 비교': 3, '향후 계획': 3,
          '전년 대비·비교': 2, '추이': 2, '구성비': 2, '참여 분포': 2, '시사점·과제': 2, '주요 추진 내용': 2, '추진 체계': 1, '단계·절차': 1, '요약표': 1, '자주 묻는 질문': 1}
rounds = [r for r in json.load(open(os.path.join(ROOT, 'data', 'rounds.json'))) if not r.get('hidden')]
kits = json.load(open(os.path.join(ROOT, 'data', 'kit_slides.json'))) if os.path.exists(os.path.join(ROOT, 'data', 'kit_slides.json')) else []
kind = lambda r: r.get('kind') or KIND_OF_INFO.get(r.get('info_type'), '')
rows = []
for k in KINDS:
    refs = [r for r in rounds if kind(r) == k]; ks = [s for s in kits if s['kind'] == k]
    n = len(refs)
    state = '빈칸' if n + len(ks) == 0 else '키트만' if n == 0 else '얇음' if n < 3 else '있음'
    # 채울 순서: 자주 쓰는데 장표가 적을수록 먼저
    score = WEIGHT[k] * 10 - min(n, 6) * 3 - len(ks) * 2
    rows.append((score, k, n, ks, refs, state))
order = {k: i + 1 for i, (_, k, *_r) in enumerate(sorted(rows, key=lambda x: -x[0]))}
L = ['# 정형 장표 빈칸 표', '',
     '`python3 scripts/gaps.py`로 만든다(손으로 고치지 말 것). 레퍼런스 장표는 숨긴 것을 빼고 센다. 유형 정의는 [제작 기준](criteria.md) 3.', '',
     '- **채울 순서**: 성과 공유회에서 자주 쓰는 유형(무게 3) 중 장표가 적은 것부터. 키트 장표는 부품이 생겼다는 뜻이라 순서를 조금 늦춘다.',
     '- **상태**: 빈칸(0) · 키트만(레퍼런스 0, 키트 장표만) · 얇음(1~2) · 있음(3 이상).', '',
     '| 순서 | 정형 유형 | 성과 공유회 무게 | 레퍼런스 장표 | 키트 장표 | 상태 |', '|---|---|---|---|---|---|']
for score, k, n, ks, refs, state in sorted(rows, key=lambda x: order[x[1]]):
    L.append('| %d | %s | %s | %s | %s | %s |' % (order[k], k, '●' * WEIGHT[k], ('%d (%s)' % (n, ' · '.join('#%s' % r['no'] for r in sorted(refs, key=lambda r: -int(r['no']))[:6]))) if n else '0',
                                            ' · '.join('%s %d장' % (s['kit'], s['slide']) for s in ks) or '—', state))
L += ['', '레퍼런스 장표 합계 %d개(숨김 제외), 정형 유형이 정해진 것 %d개, 키트 장표 %d개.' % (len(rounds), sum(1 for r in rounds if kind(r)), len(kits))]
open(os.path.join(ROOT, 'docs', 'gaps.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('\n'.join(L[6:]))
