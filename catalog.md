# 발표 디자인 라이브러리 — AI가 읽는 목록

> 사용자가 발표 내용과 함께 이 주소를 주면, 아래 순서로 스타일을 고르고 적용합니다. 모든 예시의 기관명 · 수치 · 사례는 가상이니 새 발표에 가져오지 마세요.
> `scripts/gallery.py`가 `data/styles.json` · `data/roles.json` · `data/patterns.json`에서 만든 파일입니다. 사이트 화면과 같은 데이터입니다.

## 적용 순서

1. 발표 내용과 각 장이 전하려는 것을 파악한다(누구에게, 몇 분, 장마다 한 가지).
2. 전체 스타일 하나를 고른다. 기본은 아래 표의 **검증된 세트** 중에서.
3. 장마다 알맞은 본문 구성을 고른다(아래 "구성" 표). 한 장에 구성 하나.
4. 고른 스타일의 **적용 안내**(표의 주소)를 열어 디자인 규칙 · 구성별 코드 · HTML 뼈대를 확인한다.
5. 유지할 요소를 지키면서 실제 내용을 넣는다. 내용이 넘치면 글자를 줄이지 말고 장을 나눈다. 사용자의 핵심 내용을 임의로 빼지 않는다.
6. 전체가 한 스타일로 보이는지, 글자가 잘리지 않는지, 장이 넘어가는지 확인한다.

**자료를 실제로 열어 읽지 못했다면 읽고 적용한 것처럼 말하지 않는다.** 열 수 없는 주소가 있으면 사용자에게 그 파일을 첨부해 달라고 한다. 사용자가 주지 않은 숫자 · 사실을 지어내지 않는다.

## 스타일

| ID | 이름 | 분위기 | 알맞은 전달 목적 | 상태 | 적용 안내 | 10장 예시 | 화면 |
|---|---|---|---|---|---|---|---|
| A | 픽셀 게임 | 경쾌한 | 단계를 하나씩 깨 나가는 과정을 보여 줄 때. 참여를 끌어내는 연수 · 학생 행사 | 검증된 세트 | https://szxv7704-dot.github.io/design-reference-gallery/kit/A.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/A-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/A.html |
| B | 미니멀 스튜디오 | 단정한 | 개념과 비교를 군더더기 없이 전할 때. 어떤 주제에도 무난하다 | 검증된 세트 | https://szxv7704-dot.github.io/design-reference-gallery/kit/B.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/B.html |
| C | 경쾌한 놀이 오브젝트 | 경쾌한 | 하나씩 쌓아 가는 과정을 밝게 전할 때. 유아 · 초등 대상 안내 | 확장 중 | https://szxv7704-dot.github.io/design-reference-gallery/kit/C.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/C-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/C.html |
| D | 인쇄·종이 에디토리얼 | 단정한 | 근거와 수치를 차분히 읽힐 때. 정책 · 계획 보고 | 검증된 세트 | https://szxv7704-dot.github.io/design-reference-gallery/kit/D.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/D-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/D.html |
| E | 자연 재질 | 감성적인 | 천천히 자라는 변화를 이야기할 때. 환경 · 생태 · 마을 교육 | 확장 중 | https://szxv7704-dot.github.io/design-reference-gallery/kit/E.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/E-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/E.html |
| F | 관측·중계 인포그래픽 | 몰입감 있는 | 실적 · 순위 · 진행 상황을 중계하듯 보여 줄 때 | 검증된 세트 | https://szxv7704-dot.github.io/design-reference-gallery/kit/F.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/F-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/F.html |
| G | 어두운 콘셉트 | 몰입감 있는 | 흩어진 것을 하나로 잇는 이야기. 비전 선포 · 불을 끄고 하는 발표 | 확장 중 | https://szxv7704-dot.github.io/design-reference-gallery/kit/G.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/G-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/G.html |
| H | 전통 공예·문양 | 전통적인 | 역사 · 문화 · 지역을 다루는 격식 있는 자리 | 검증된 세트 | https://szxv7704-dot.github.io/design-reference-gallery/kit/H.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/H-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/H.html |

상태: **검증된 세트** = 10장 예시 · 다른 주제 시험 · 넘침 검사를 통과 / **확장 중** = 10장 예시는 있으나 검증이 끝나지 않음.

### A 픽셀 게임
- 유지할 것: 남색 게임 창 안에 정보를 담는다 / 픽셀 글꼴 하나로 쓰고 크기는 11의 배수 / 진행 칸으로 지금 위치를 보인다
- 바꿔도 되는 것: 창 안의 내용과 칸 수 / 강조할 창 하나
- 피할 것: 격식 있는 보고 · 긴 문장 / 창 밖에 장식 더하기

### B 미니멀 스튜디오
- 유지할 것: 밝은 청백 바탕에 흰 면, 그림자 하나 / 주황은 한 장에 한 곳 / 흰 덩어리(모형대)는 표지 · 흐름 · 마무리에만
- 바꿔도 되는 것: 강조할 낱말이나 칸 / 칸 수와 배치
- 피할 것: 색을 더 쓰기 / 본문에 상징 부품 넣기

### C 경쾌한 놀이 오브젝트
- 유지할 것: 하늘빛 흰 바탕과 굵은 제목 / 블록 수 = 섹션 수 / 빨강 강조는 한 곳
- 바꿔도 되는 것: 블록 층 수 / 카드 수
- 피할 것: 원색을 본문 글자에 쓰기 / 무거운 통계 위주 발표

### D 인쇄·종이 에디토리얼
- 유지할 것: 먹 명조 제목과 이중 괘선 / 남색과 주홍 2도 / 판 번호는 표지 · 흐름 · 마무리에만
- 바꿔도 되는 것: 강조할 숫자나 줄 / 표 · 목록의 행 수
- 피할 것: 둥근 모서리 · 그림자 강조 / 주홍을 두 곳 이상

### E 자연 재질
- 유지할 것: 회녹 종이 바탕에 나무색 농담 / 나무 단면 그림은 표지 · 흐름 · 마무리에만 / 청록 강조 한 곳
- 바꿔도 되는 것: 겹(섹션) 수는 5개까지 / 강조할 칸
- 피할 것: 다른 색상 더하기 / 본문에 질감 그림 깔기

### F 관측·중계 인포그래픽
- 유지할 것: 청백 바탕에 남색 기록판 / 숫자는 좁은 숫자 글꼴 / 구간 띠로 지금 위치를 보인다
- 바꿔도 되는 것: 구간 수 / 빨강으로 짚을 한 줄
- 피할 것: 한글에 숫자 글꼴 쓰기 / 감성적인 이야기 위주 발표

### G 어두운 콘셉트
- 유지할 것: 밤하늘 그림은 표지 · 흐름 · 간지 · 마무리에만 / 본문은 남색 단색 바탕 / 금빛은 한 곳
- 바꿔도 되는 것: 이어진 별(섹션)은 5개까지 / 강조할 칸
- 피할 것: 밝은 회의실 화면 / 빛 번짐 효과 더하기

### H 전통 공예·문양
- 유지할 것: 한지 바탕에 먹 명조 / 면마다 쌍변(굵은 선 + 가는 선) / 주홍은 인장처럼 한 곳
- 바꿔도 되는 것: 막새(섹션) 수는 5개까지 / 강조할 칸
- 피할 것: 그림자 · 둥근 모서리 / 문양을 새로 그려 넣기

## 표지에서 넓힌 덱 (27벌)

표지 하나마다 10장: 원본 표지 + 본문 여덟 역할 + 마무리. 표지의 색 · 글꼴을 입혔고 배치는 "바탕" 스타일에서 빌렸다. 표지마다 구성 조합이 다르다.
적용하려면: 바탕 스타일의 적용 안내(`kit/{바탕}.md`)를 따르되 **`<link>` 주소만 아래 CSS로 바꾸고**, 상징 부품(표지 · 목차 · 마무리에 넣는 그림)은 넣지 않는다. 표지 장은 사용자의 제목으로 새로 쓴다(원본 표지 장표는 그대로 가져오지 않는다).

| 번호 | 이름 | 바탕 | 10장 덱 | CSS | 상태 — 장치 또는 구성 조합 |
|---|---|---|---|---|---|
| #4 | 가온 야간편 탑승권 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/4.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/4.css | **표지의 장치를 본문까지** — 분홍 항공사 띠 · 절취선과 보관용 쪽 · 한글+영문 필드 라벨 · 출발→경유→도착 여정 · 노란 강조 칸 · 리소 어긋남 · 빌린 본문 #118 #84 #120 |
| #7 | 블록 빌드 유아학교 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/7.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/7.css | 색 · 글꼴만 맞춤 — 가로 이정표 / 맞는 예와 아닌 예 / 짝 줄 / 세로 단계 / 한 건 이야기 / 할 일과 조건 / 숫자 하나 크게 / 한 문장 |
| #9 | 늘봄 퀘스트 일지 | A | https://szxv7704-dot.github.io/design-reference-gallery/covers/9.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/9.css | 색 · 글꼴만 맞춤 — 번호 카드 / 낱말과 뜻 / 전과 후 수치 / 단계 표 / 화면 짚기 / 질문과 보기 / 목표 대비 막대 / 세 줄 |
| #10 | 안개 걷는 영토도 | A | https://szxv7704-dot.github.io/design-reference-gallery/covers/10.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/10.css | 색 · 글꼴만 맞춤 — 줄 목록 / 맞는 예와 아닌 예 / 전과 후 수치 / 가로 세 칸 / 한 건 이야기 / 질문과 보기 / 숫자 셋 / 한 문장 |
| #11 | 디딤 타워 | A | https://szxv7704-dot.github.io/design-reference-gallery/covers/11.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/11.css | 색 · 글꼴만 맞춤 — 가로 이정표 / 낱말과 뜻 / 기준별 두 열 / 세로 단계 / 화면 짚기 / 체크 목록 / 숫자 하나 크게 / 세 줄 |
| #12 | 협력 항로 해도 | A | https://szxv7704-dot.github.io/design-reference-gallery/covers/12.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/12.css | 색 · 글꼴만 맞춤 — 번호 카드 / 세 요소로 풀기 / 짝 줄 / 단계 표 / 사람의 말 / 할 일과 조건 / 목표 대비 막대 / 네 칸 정리 |
| #17 | 두 개의 심 | E | https://szxv7704-dot.github.io/design-reference-gallery/covers/17.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/17.css | 색 · 글꼴만 맞춤 — 줄 목록 / 낱말과 뜻 / 짝 줄 / 가로 세 칸 / 화면 짚기 / 할 일과 조건 / 숫자 셋 / 세 줄 |
| #18 | 함께 도는 궤도 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/18.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/18.css | 색 · 글꼴만 맞춤 — 가로 이정표 / 세 요소로 풀기 / 전과 후 수치 / 세로 단계 / 사람의 말 / 질문과 보기 / 숫자 하나 크게 / 네 칸 정리 |
| #19 | 화이트 단지 모형 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/19.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/19.css | 색 · 글꼴만 맞춤 — 번호 카드 / 맞는 예와 아닌 예 / 기준별 두 열 / 단계 표 / 한 건 이야기 / 체크 목록 / 목표 대비 막대 / 한 문장 |
| #24 | 같은 사물, 아이의 눈 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/24.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/24.css | 색 · 글꼴만 맞춤 — 줄 목록 / 맞는 예와 아닌 예 / 짝 줄 / 가로 세 칸 / 한 건 이야기 / 할 일과 조건 / 숫자 셋 / 한 문장 |
| #25 | 늘봄 수요 일기도 | F | https://szxv7704-dot.github.io/design-reference-gallery/covers/25.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/25.css | 색 · 글꼴만 맞춤 — 가로 이정표 / 낱말과 뜻 / 전과 후 수치 / 세로 단계 / 화면 짚기 / 질문과 보기 / 숫자 하나 크게 / 세 줄 |
| #26 | 손 닿는 구명튜브 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/26.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/26.css | 색 · 글꼴만 맞춤 — 번호 카드 / 세 요소로 풀기 / 기준별 두 열 / 단계 표 / 사람의 말 / 체크 목록 / 목표 대비 막대 / 네 칸 정리 |
| #27 | 일요판 1면 약속 | D | https://szxv7704-dot.github.io/design-reference-gallery/covers/27.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/27.css | 색 · 글꼴만 맞춤 — 줄 목록 / 낱말과 뜻 / 기준별 두 열 / 가로 세 칸 / 화면 짚기 / 체크 목록 / 숫자 셋 / 세 줄 |
| #28 | 기준음 A440 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/28.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/28.css | 색 · 글꼴만 맞춤 — 가로 이정표 / 세 요소로 풀기 / 짝 줄 / 세로 단계 / 사람의 말 / 할 일과 조건 / 숫자 하나 크게 / 네 칸 정리 |
| #29 | 회전 레일 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/29.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/29.css | 색 · 글꼴만 맞춤 — 번호 카드 / 맞는 예와 아닌 예 / 전과 후 수치 / 단계 표 / 한 건 이야기 / 질문과 보기 / 목표 대비 막대 / 한 문장 |
| #30 | 꺼지지 않는 창구 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/30.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/30.css | 색 · 글꼴만 맞춤 — 줄 목록 / 세 요소로 풀기 / 전과 후 수치 / 가로 세 칸 / 사람의 말 / 질문과 보기 / 숫자 셋 / 네 칸 정리 |
| #31 | 한 칸씩 켜지는 돔 | F | https://szxv7704-dot.github.io/design-reference-gallery/covers/31.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/31.css | 색 · 글꼴만 맞춤 — 가로 이정표 / 맞는 예와 아닌 예 / 기준별 두 열 / 세로 단계 / 한 건 이야기 / 체크 목록 / 숫자 하나 크게 / 한 문장 |
| #32 | 재생지 콜라주 | D | https://szxv7704-dot.github.io/design-reference-gallery/covers/32.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/32.css | 색 · 글꼴만 맞춤 — 번호 카드 / 낱말과 뜻 / 짝 줄 / 단계 표 / 화면 짚기 / 할 일과 조건 / 목표 대비 막대 / 세 줄 |
| #37 | 분광 프리즘 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/37.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/37.css | 색 · 글꼴만 맞춤 — 줄 목록 / 낱말과 뜻 / 전과 후 수치 / 가로 세 칸 / 화면 짚기 / 질문과 보기 / 숫자 셋 / 세 줄 |
| #39 | 전술 자석 보드 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/39.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/39.css | 색 · 글꼴만 맞춤 — 가로 이정표 / 세 요소로 풀기 / 기준별 두 열 / 세로 단계 / 사람의 말 / 체크 목록 / 숫자 하나 크게 / 네 칸 정리 |
| #58 | 처마 끝 수막새 | H | https://szxv7704-dot.github.io/design-reference-gallery/covers/58.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/58.css | 색 · 글꼴만 맞춤 — 번호 카드 / 맞는 예와 아닌 예 / 짝 줄 / 단계 표 / 한 건 이야기 / 할 일과 조건 / 목표 대비 막대 / 한 문장 |
| #59 | 범 내려온다 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/59.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/59.css | 색 · 글꼴만 맞춤 — 줄 목록 / 세 요소로 풀기 / 짝 줄 / 가로 세 칸 / 사람의 말 / 할 일과 조건 / 숫자 셋 / 네 칸 정리 |
| #71 | 미래교육 설계도 | F | https://szxv7704-dot.github.io/design-reference-gallery/covers/71.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/71.css | 색 · 글꼴만 맞춤 — 가로 이정표 / 맞는 예와 아닌 예 / 전과 후 수치 / 세로 단계 / 한 건 이야기 / 질문과 보기 / 숫자 하나 크게 / 한 문장 |
| #74 | 별을 잇다 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/74.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/74.css | 색 · 글꼴만 맞춤 — 번호 카드 / 낱말과 뜻 / 기준별 두 열 / 단계 표 / 화면 짚기 / 체크 목록 / 목표 대비 막대 / 세 줄 |
| #96 | 익숙함에 틈을 내다 | D | https://szxv7704-dot.github.io/design-reference-gallery/covers/96.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/96.css | 색 · 글꼴만 맞춤 — 줄 목록 / 맞는 예와 아닌 예 / 기준별 두 열 / 가로 세 칸 / 한 건 이야기 / 체크 목록 / 숫자 셋 / 한 문장 |
| #106 | 새로운 일상이 도착했습니다 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/106.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/106.css | 색 · 글꼴만 맞춤 — 가로 이정표 / 낱말과 뜻 / 짝 줄 / 세로 단계 / 화면 짚기 / 할 일과 조건 / 숫자 하나 크게 / 세 줄 |
| #109 | 피사체는 그대로, 시선은 새로 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/109.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/109.css | 색 · 글꼴만 맞춤 — 번호 카드 / 세 요소로 풀기 / 전과 후 수치 / 단계 표 / 사람의 말 / 질문과 보기 / 목표 대비 막대 / 네 칸 정리 |

## 구성 (역할마다 배치가 다른 셋. 모든 스타일에서 같은 이름으로 쓴다)

| 역할 | 구성 | 모습 | 이럴 때 | 알맞은 분량 | 부품 | 보기(B 스타일) |
|---|---|---|---|---|---|---|
| 목차 · 전체 흐름 | 줄 목록 | 번호 · 이름 · 시간이 한 줄씩, 옆에 스타일의 상징 | 차례만 알리면 될 때. 가장 무난하다 | 3~5줄 | `.toc-list` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#2 |
|  | 가로 이정표 | 가로선 위에 점을 찍고 시간 · 이름 · 한 줄 | 시간 배분이나 날짜가 중요할 때 | 3~5개 | `.mile` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#3 |
|  | 번호 카드 | 큰 번호가 붙은 카드를 가로로 나란히 | 단계마다 이름을 또렷이 기억시키고 싶을 때 | 3~5칸 | `.agenda` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#4 |
| 핵심 개념 · 정의 | 낱말과 뜻 | 왼쪽에 낱말, 오른쪽에 뜻 한 문장과 예 | 낯선 낱말 하나를 사전처럼 풀 때 | 낱말 1 + 뜻 1문장 + 예 1~2 | `.define` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#5 |
|  | 세 요소로 풀기 | 개념을 이루는 요소를 카드 셋으로 | 개념이 몇 가지 요소로 이루어져 있을 때 | 2~4칸, 칸마다 3줄 이하 | `.card + .grid.g3` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#6 |
|  | 맞는 예와 아닌 예 | 위에 낱말, 아래 두 칸에 ○ 예와 × 예 | 자주 헷갈리는 것과 선을 그어야 할 때 | 쪽마다 예 2~3개 | `.yesno` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#7 |
| 비교 | 짝 줄 | 줄마다 왼쪽 → 오른쪽 한 짝 | 같은 것을 이렇게 바꾸라고 보여 줄 때 | 2~3줄 | `.fix + .stack` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#8 |
|  | 전과 후 수치 | 같은 지표의 숫자를 좌우에 크게 | 두 쪽을 숫자로 견줄 수 있을 때 | 2~3짝, 같은 단위 | `.ba + .ba-head` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#9 |
|  | 기준별 두 열 | 기준 | 왼쪽 | 오른쪽 세 열의 대조표 | 여러 기준으로 두 대상을 따질 때 | 기준 3~4줄, 칸마다 1줄 | `.vs` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#10 |
| 순서 · 절차 | 가로 세 칸 | 단계마다 한 칸, 칸 안에 할 일 목록 | 단계마다 할 일이 여러 줄일 때 | 3~4단계, 단계마다 3줄 이하 | `.road` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#11 |
|  | 세로 단계 | 번호 동그라미를 세로선으로 잇고 이름 + 한 줄 | 단계가 4~5개이고 단계마다 한 줄이면 될 때 | 3~5단계, 단계마다 1줄 | `.stepper` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#12 |
|  | 단계 표 | 단계 | 할 일 | 쓰는 것 | 시간의 표 | 단계마다 같은 항목(담당 · 도구 · 시간)을 견줄 때 | 3~5행 × 3~4열 | `.tbl` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#13 |
| 사례 · 화면 설명 | 화면 짚기 | 캡처 한 장에 번호를 찍고 옆에 설명 | 실제 화면의 어디를 누르는지 보여 줄 때 | 캡처 1장 + 번호 3개 이하 | `.shot + .shot-img` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#14 |
|  | 사람의 말 | 말 풍선 세 개, 가장 중요한 말 하나를 강조 | 화면이 없고 써 본 사람의 말이 있을 때 | 1~3개, 각 60자 이하 | `.quote` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#15 |
|  | 한 건 이야기 | 상황 → 한 일 → 결과 세 칸 | 한 사례를 처음부터 끝까지 들려줄 때 | 세 칸, 칸마다 이름 + 2줄 | `.story` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#16 |
| 실습 과제 · 행동 안내 | 할 일과 조건 | 할 일 한 문장을 크게, 아래에 시간 · 결과물 · 도움 | 과제가 하나이고 조건을 알려야 할 때 | 한 문장 + 조건 2~3칸 | `.todo` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#17 |
|  | 질문과 보기 | 질문 하나와 고를 보기 넷 | 하기 전에 먼저 고르거나 생각하게 할 때 | 질문 1 + 보기 4개 이하 | `.ask` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#18 |
|  | 체크 목록 | 네모 칸이 달린 확인 목록 | 하면서 스스로 확인할 것이 여럿일 때 | 3~5줄 | `.check` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#19 |
| 핵심 수치 · 근거 | 숫자 셋 | 숫자 타일 셋을 나란히 | 받치는 숫자가 둘 이상일 때 | 2~4개, 숫자마다 단위 + 한 줄 | `.tile + .grid.g3` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#20 |
|  | 숫자 하나 크게 | 왼쪽에 아주 큰 숫자 하나, 오른쪽에 뜻과 받치는 두 줄 | 기억시킬 숫자가 딱 하나일 때 | 숫자 1 + 뜻 1문장 + 2줄 | `.big` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#21 |
|  | 목표 대비 막대 | 지표마다 막대와 목표선 | 여러 지표의 달성 정도를 견줄 때 | 3~5줄, 한 가지 단위 | `.goal + .g-row` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#22 |
| 요약 | 세 줄 | 번호가 붙은 세 줄, 이름 + 설명 | 기억할 것이 서너 가지일 때 | 3~5개 | `.points` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#23 |
|  | 네 칸 정리 | 이름표가 붙은 네 칸 | 누가 · 무엇을 · 언제처럼 항목이 정해져 있을 때 | 3~4칸, 칸마다 2줄 | `.brief` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#24 |
|  | 한 문장 | 화면 가운데 큰 한 문장과 받치는 말 | 한 줄로 줄일 수 있을 때 | 40자 이하 한 문장 + 1줄 | `.say` | https://szxv7704-dot.github.io/design-reference-gallery/kit/B-var.html#25 |

그 밖의 구성(갈래 · 체계 · 추이 · 구성비 · 표 · 일정 · 사진 · 간지)과 모든 구성의 코드는 각 스타일의 적용 안내(`kit/{ID}.md`)에 들어 있다.
**장마다 내용에 맞는 구성을 고른다.** 같은 역할이 여러 번 나오면 구성을 바꿔 쓴다. 넘치면 글자를 줄이지 말고 장을 나눈다.

### 스타일별 10장 예시의 구성 조합

스타일마다 예시의 짜임이 다르다. 참고일 뿐이고 그대로 따를 필요는 없다.

| 스타일 | 목차 | 핵심 개념 | 비교 | 순서 | 사례 | 실습 과제 | 핵심 수치 | 요약 |
|---|---|---|---|---|---|---|---|---|
| A 픽셀 게임 | 번호 카드 | 맞는 예와 아닌 예 | 짝 줄 | 단계 표 | 한 건 이야기 | 체크 목록 | 숫자 셋 | 네 칸 정리 |
| B 미니멀 스튜디오 | 줄 목록 | 낱말과 뜻 | 기준별 두 열 | 가로 세 칸 | 화면 짚기 | 할 일과 조건 | 숫자 하나 크게 | 세 줄 |
| C 경쾌한 놀이 오브젝트 | 번호 카드 | 세 요소로 풀기 | 짝 줄 | 세로 단계 | 사람의 말 | 질문과 보기 | 숫자 셋 | 한 문장 |
| D 인쇄·종이 에디토리얼 | 줄 목록 | 낱말과 뜻 | 전과 후 수치 | 세로 단계 | 한 건 이야기 | 체크 목록 | 목표 대비 막대 | 세 줄 |
| E 자연 재질 | 가로 이정표 | 세 요소로 풀기 | 전과 후 수치 | 가로 세 칸 | 사람의 말 | 할 일과 조건 | 숫자 하나 크게 | 한 문장 |
| F 관측·중계 인포그래픽 | 가로 이정표 | 맞는 예와 아닌 예 | 기준별 두 열 | 가로 세 칸 | 화면 짚기 | 질문과 보기 | 목표 대비 막대 | 네 칸 정리 |
| G 어두운 콘셉트 | 가로 이정표 | 세 요소로 풀기 | 짝 줄 | 세로 단계 | 화면 짚기 | 할 일과 조건 | 숫자 하나 크게 | 세 줄 |
| H 전통 공예·문양 | 줄 목록 | 낱말과 뜻 | 기준별 두 열 | 단계 표 | 사람의 말 | 체크 목록 | 숫자 셋 | 네 칸 정리 |

## 그 밖

- 표지 레퍼런스 설명(분위기 · 가져갈 장치): https://szxv7704-dot.github.io/design-reference-gallery/catalog/refs.md
- 참고 본문 장표(도식 아이디어): https://szxv7704-dot.github.io/design-reference-gallery/catalog/body.md · 아이콘 85개: https://szxv7704-dot.github.io/design-reference-gallery/catalog/icons.md
- 사람용 이용 방법: https://szxv7704-dot.github.io/design-reference-gallery/guide.html
