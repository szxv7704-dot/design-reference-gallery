# 발표 디자인 라이브러리 — AI가 읽는 목록

> 사용자가 발표 내용과 함께 이 주소를 주면, 아래 순서로 스타일을 고르고 적용합니다. 모든 예시의 기관명 · 수치 · 사례는 가상이니 새 발표에 가져오지 마세요.
> `scripts/gallery.py`가 `data/styles.json` · `data/roles.json` · `data/patterns.json`에서 만든 파일입니다. 사이트 화면과 같은 데이터입니다.

## 적용 순서

1. 발표 내용과 각 장이 전하려는 것을 파악한다(누구에게, 몇 분, 장마다 한 가지).
2. 전체 스타일 하나를 고른다. 기본은 아래 표의 **검증된 세트** 중에서.
3. 장마다 알맞은 본문 구성을 고른다(아래 "구성" 표). 한 장에 구성 하나.
4. 고른 스타일의 **적용 안내**(표의 주소)를 열어 디자인 규칙 · 구성별 코드 · HTML 뼈대를 확인한다.
5. 유지할 요소를 지키면서 실제 내용을 넣는다. 내용이 넘치면 글자를 줄이지 말고 장을 나눈다. 사용자의 핵심 내용을 임의로 빼지 않는다.
6. 꼭 기억시킬 한두 장(표지 · 결론)에는 "와우 포인트" 표에서 기법 하나를 골라 쓸 수 있다. 덱 전체에 한두 번만.
7. 전체가 한 디자인으로 보이는지, 글자가 잘리지 않는지, 장이 넘어가는지 확인한다.

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
| I | 원과 반원 | 무난한 | 부드럽지만 가볍지 않게 전할 때. 설명회 · 업무보고 등 어디에나 무난하다 | 검증된 세트 | https://szxv7704-dot.github.io/design-reference-gallery/kit/I.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/I-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/I.html |
| J | 사선 띠 | 무난한 | 격식 있게 정리해 보고할 때. 업무보고 · 계획 보고 | 검증된 세트 | https://szxv7704-dot.github.io/design-reference-gallery/kit/J.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/J-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/J.html |
| K | 모듈 격자 | 무난한 | 수치 · 실적이 많은 보고를 정돈되게 보일 때 | 검증된 세트 | https://szxv7704-dot.github.io/design-reference-gallery/kit/K.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/K-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/K.html |
| L | 점 격자 | 무난한 | 정책 · 비전을 차분하고 단정하게 전할 때 | 검증된 세트 | https://szxv7704-dot.github.io/design-reference-gallery/kit/L.md | https://szxv7704-dot.github.io/design-reference-gallery/kit/L-set.html | https://szxv7704-dot.github.io/design-reference-gallery/styles/L.html |

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

### I 원과 반원
- 유지할 것: 청록 한 계열의 명도 다섯 단계 + 산호 한 곳 / 원 · 반원 · 사분원은 표지 · 목차 · 간지 · 맺음에만 / 카드 · 막대 · 번호도 둥근 모양
- 바꿔도 되는 것: 강조할 낱말이나 칸 / 칸 수와 배치
- 피할 것: 다른 색 계열 섞기 / 원을 본문 장식으로 흩어 놓기

### J 사선 띠
- 유지할 것: 먹 · 회색 한 계열 + 빨강 한 곳 / 모든 사선은 같은 각도(-24°) / 카드 모서리 · 막대 끝을 같은 각도로 자름
- 바꿔도 되는 것: 강조할 낱말이나 칸 / 칸 수와 배치
- 피할 것: 빨강을 두 곳 이상 / 각도가 다른 사선 섞기

### K 모듈 격자
- 유지할 것: 쪽빛 한 계열 + 겨자 한 칸 / 모서리는 모두 직각, 칸 크기 · 간격 일정 / 제목 강조는 겨자 형광펜 띠
- 바꿔도 되는 것: 채울 칸의 위치 / 칸 수와 배치
- 피할 것: 겨자를 글자색으로 쓰기(대비 부족) / 칸 크기 섞기

### L 점 격자
- 유지할 것: 자주 한 계열 + 금빛 점 하나 / 점은 120px 격자 교차점에만 / 명조 제목 · 가는 선
- 바꿔도 되는 것: 강조할 낱말이나 점 / 칸 수와 배치
- 피할 것: 점 · 선을 규칙 없이 잇기 / 금빛을 글자색으로 쓰기(대비 부족)

## 표지에서 넓힌 덱 (27벌)

표지 하나마다 10장: 원본 표지 + 본문 여덟 역할 + 마무리. 표지의 색 · 글꼴을 입혔고 배치는 "바탕" 스타일에서 빌렸다. 표지마다 구성 조합이 다르다.
적용하려면: 바탕 스타일의 적용 안내(`kit/{바탕}.md`)를 따르되 **`<link>` 주소만 아래 CSS로 바꾸고**, 상징 부품(표지 · 목차 · 마무리에 넣는 그림)은 넣지 않는다. 표지 장은 사용자의 제목으로 새로 쓴다(원본 표지 장표는 그대로 가져오지 않는다).

| 번호 | 이름 | 바탕 | 10장 덱 | CSS | 상태 — 장치 또는 구성 조합 |
|---|---|---|---|---|---|
| #4 | 가온 야간편 탑승권 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/4.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/4.css | **표지의 장치를 본문까지** — 분홍 항공사 띠 · 절취선과 보관용 쪽 · 한글+영문 필드 라벨 · 출발→경유→도착 여정 · 노란 강조 칸 · 리소 어긋남 · 빌린 본문 #118 #84 #120 |
| #7 | 블록 빌드 유아학교 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/7.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/7.css | **표지의 장치를 본문까지** — 과제 블록 핫바 · 과제 색 완성률 막대 · BUILD STAGE 두 색 칩 · 흰 알약 이름표 · '+ =' 등식 · 표지에서 떠낸 블록 그림 · 빌린 본문 #121 #85 #113 |
| #9 | 늘봄 퀘스트 일지 | A | https://szxv7704-dot.github.io/design-reference-gallery/covers/9.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/9.css | **표지의 장치를 본문까지** — 위 상태 바 · 아래 의뢰인 대화창(결론을 의뢰인의 말로) · 커서 놓인 퀘스트 목록 · 체크 목표 · 보상 슬롯 · 진행 단계 · 표지에서 떠낸 초상화와 아이콘 · 빌린 본문 #78 #92 #111 |
| #10 | 안개 걷는 영토도 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/10.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/10.css | **표지의 장치를 본문까지** — 양피지 제목 띠와 자원 표시 · 오른쪽 지역 진척 패널(단계 색 칸) · 아래 빨간 '!' 과제 알림 띠(결론) · 가지 않은 곳은 안개 · 표지에서 떠낸 지도 · 빌린 본문 #51 #49 #114 |
| #11 | 디딤 타워 | A | https://szxv7704-dot.github.io/design-reference-gallery/covers/11.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/11.css | **표지의 장치를 본문까지** — 왼쪽 층 표시줄(B1~RF, 지금 층은 노란 칸) · 어두운 제목 띠 · 층 번호판 · 걸림돌→보물 짝 · 파티 칸 · 진척 칸 막대 · 표지에서 떠낸 탑 단면과 초상화 · 빌린 본문 #88 #55 #73 |
| #12 | 협력 항로 해도 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/12.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/12.css | **표지의 장치를 본문까지** — 해도 눈금 테두리(A~F · 1~4) · 두루마리 제목 · 순환 항로 구간 n/7 · 남색 이름표(섬 노랑 · 위험 분홍) · 항해 일지 · 좌표 달린 과제 상자 · 나침반 네 낱말 · 표지에서 떠낸 나침반과 배 · 빌린 본문 #86 #119 #48 |
| #17 | 두 개의 심 | E | https://szxv7704-dot.github.io/design-reference-gallery/covers/17.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/17.css | **표지의 장치를 본문까지** — 자간 넓은 청록 머리말 · 명조 제목 · 가는 나무색 줄과 부제 · 점 이름표(청록 · 황금 · 나무색) · 두 심이 하나의 띠로 · 해마다 넓어지는 겹 · 표지에서 떠낸 나무 단면 · 빌린 본문 #53 #79 #97 |
| #18 | 함께 도는 궤도 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/18.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/18.css | **표지의 장치를 본문까지** — 왼쪽 하늘 면 + 오른쪽 흰 면의 좌우 분할 · 고정폭 파란 머리말 · 명조 제목과 파란 부제 · 행성 아이콘 범례 줄 · 서로 다른 주기의 궤도 줄 · 표지에서 떠낸 행성 아이콘 · 빌린 본문 #57 #94 #61 |
| #19 | 화이트 단지 모형 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/19.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/19.css | **표지의 장치를 본문까지** — 번호 단추 조작 목록(고른 곳만 주황) · 경로 머리말 · 설명 카드와 고정폭 규격 칩 · 흰색 = 기존, 주황 = 계획 · 표지에서 공간별로 떠낸 모형 · 빌린 본문 #80 #54 #47 |
| #24 | 같은 사물, 아이의 눈 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/24.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/24.css | **표지의 장치를 본문까지** — 가운데 세로선과 손잡이 · 왼쪽 '알기 전 · 어른의 눈'(회청색) / 오른쪽 '알고 난 후 · 아이의 눈'(주황) · 같은 것을 좌우에 나란히 · 표지에서 전 · 후로 떠낸 사물 여섯 쌍 · 빌린 본문 #83 #76 #112 |
| #25 | 늘봄 수요 일기도 | F | https://szxv7704-dot.github.io/design-reference-gallery/covers/25.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/25.css | **표지의 장치를 본문까지** — 일기도 머리띠(제n호 · 도면 이름 · 분석 시각) · 시간대 토글(아침 · 오후 · 저녁) · 6단 수요 눈금 색 · 파란 H(거점)와 빨간 L(과밀 · 공백) · 학교 관측소 줄 · 표지에서 시간대별로 떠낸 지도 · 빌린 본문 #72 #50 #89 |
| #26 | 손 닿는 구명튜브 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/26.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/26.css | **표지의 장치를 본문까지** — 박물관 도판 형식(위 가는 줄 · 자간 넓은 기관명 · FIG. 번호) · 아주 굵은 남색 제목과 짧은 주황 줄 · 제원 캡션(항목 + 고정폭 값) · 네 고정점 = 과제 넷 · 표지에서 떠낸 구명튜브 · 빌린 본문 #115 #56 #93 |
| #27 | 일요판 1면 약속 | D | https://szxv7704-dot.github.io/design-reference-gallery/covers/27.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/27.css | **표지의 장치를 본문까지** — 날짜 띠와 호 · 면 · 제호 '배움일요' · 굵고 가는 이중 괘선 · 12단 눈금 · 남색 작은 라벨과 큰 명조 헤드라인 · 세로 괘선으로 나눈 단 · 오른쪽 짧은 라벨 단 · 빌린 본문 #77 #87 #85 |
| #28 | 기준음 A440 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/28.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/28.css | **표지의 장치를 본문까지** — 고정폭 머리말 'A4 = 440 Hz —— …' · 네 직군의 색 점과 네 줄 · 오른쪽 끝에서 하나로 모이는 남색 칸 · 파란 부제 · 표지에서 떠낸 소리굽쇠와 파형 · 빌린 본문 #22 #41 #121 |
| #29 | 회전 레일 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/29.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/29.css | **표지의 장치를 본문까지** — 시간 상자(가는 줄 사이 고정폭 시간) · 접시 테 색 고리 = 활동(놀이 초록 · 간식 주황 · 쉼 파랑 · 특성화 빨강) · 시간 칸이 이어진 하루 레일 · 고리 달린 차림표 · 표지에서 떠낸 접시와 레일 · 빌린 본문 #115 #79 #112 |
| #30 | 꺼지지 않는 창구 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/30.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/30.css | **표지의 장치를 본문까지** — 밤의 벽(어두운 바탕) · 얇은 글자와 분홍 네온 강조 · 줄에 매달린 약속 간판 셋(지금 것만 켜짐: 하늘 · 분홍 · 호박색) · 유리관 윤곽 상자 · 켜진 것은 하나 · 빌린 본문 #83 #76 #113 |
| #31 | 한 칸씩 켜지는 돔 | F | https://szxv7704-dot.github.io/design-reference-gallery/covers/31.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/31.css | **표지의 장치를 본문까지** — 왼쪽 흰 면 + 오른쪽 돔 사진의 좌우 분할 · 굵은 남색 줄 아래 참여 숫자판(장마다 숫자가 오름) · 금빛으로 켜지는 삼각 칸 · 주황 강조 한 곳 · 표지에서 단계별로 떠낸 돔 사진 · 빌린 본문 #111 #50 #84 |
| #32 | 재생지 콜라주 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/32.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/32.css | **표지의 장치를 본문까지** — 종이 조각(흰 찢긴 테 · 조금씩 다른 기울기) · 크라프트 꼬리표 머리말 · 초록 종이 위 흰 제목 · 영역마다 다른 종이 색 · 면적이 곧 비중인 조각 · 영수증식 점선 목록 · 빌린 본문 #120 #88 #118 |
| #37 | 분광 프리즘 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/37.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/37.css | **표지의 장치를 본문까지** — 자간 넓은 고정폭 머리말 · 광학대 눈금자와 빨간 위치 표시(장마다 옮겨 감) · 하나 → 다섯 갈래 · 다섯 색 띠(의료 빨강 · 요양 노랑 · 주거 초록 · 식사 파랑 · 마음돌봄 보라) · 표지에서 떠낸 프리즘 · 빌린 본문 #97 #61 #73 |
| #39 | 전술 자석 보드 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/39.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/39.css | **표지의 장치를 본문까지** — 화이트 전술판(회색 테 · 검은 모서리 받침 · 흐린 경기장 선) · 압정 두 개로 붙인 흰 카드 = 결론 · 번호 자석(골키퍼 금색) · 상황실 검은 네모 C · 마커 손글씨(빨강 상대 · 파랑 우리) · 대형 '1 · 4 · 3 · 3' 손글씨 줄 · 표지에서 떠낸 비구름과 감독석 · 빌린 본문 #87 #49 #56 |
| #58 | 처마 끝 수막새 | H | https://szxv7704-dot.github.io/design-reference-gallery/covers/58.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/58.css | **표지의 장치를 본문까지** — 자간 넓은 명조 머리말과 큰 명조 제목 · 짧은 먹 줄 · 지시선 끝 점과 해설(굵은 이름 + 흐린 설명) · 흰 테 원형 확대창 · 처마 끝선 · 주홍 인장 하나(유일한 강조) · 기와 네 장으로 잇는 4단계 · 표지에서 떠낸 처마 사진과 수막새 · 빌린 본문 #81 #95 #54 |
| #59 | 범 내려온다 | C | https://szxv7704-dot.github.io/design-reference-gallery/covers/59.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/59.css | **표지의 장치를 본문까지** — 한지빛 바탕 · 큰 붓글씨 결론 · 자간 넓은 작은 명조 머리말 · 아래 출처 두 줄 · 먹 붓선 칸 · 장마다 자세가 바뀌며 다가오는 범(원화의 자세 12컷) · 옅은 산수 배경 · 빌린 본문 #81 #119 #93 |
| #71 | 미래교육 설계도 | F | https://szxv7704-dot.github.io/design-reference-gallery/covers/71.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/71.css | **표지의 장치를 본문까지** — 청사진 바탕과 격자 · 모서리 십자와 가는 테 · 도면 표제란(PROJECT · DRAWING · STATUS · 번호) · 영문 고정폭 머리말 · 큰 주황 층 번호 · 층 표시줄(지금 층에 주황 점) · 빨간 펜 손그림 · 표지 원화의 층별 청사진 · 빌린 본문 #114 #57 |
| #74 | 별을 잇다 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/74.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/74.css | **표지의 장치를 본문까지** — 밤하늘 · '○○ EDUCATION'과 짧은 금빛 줄 · 얇은 명조 결론 · 영문 학명 · 아래 '별을 잇다'와 다섯 별자리 메뉴(지금 별자리에 금빛 밑줄) · 별자리 = 사업, 별 = 세부과제(번호로 맞춤) · 표지 원화의 별자리 확대판 · 빌린 본문 #86 #93 |
| #96 | 익숙함에 틈을 내다 | D | https://szxv7704-dot.github.io/design-reference-gallery/covers/96.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/96.css | **표지의 장치를 본문까지** — 미색 종이 · 위 기관 줄과 가는 선 · 아주 큰 바탕체 결론 · 두 번째 크기 부제와 밑줄 · 작은 카피 · 종이가 찢겨 열린 틈(장마다 조금씩 더 열림)과 그 너머 하늘 · 주황 계단 = 다음 단계 · 표지 원화의 틈 사진 · 빌린 본문 #53 #76 #47 |
| #106 | 새로운 일상이 도착했습니다 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/106.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/106.css | **표지의 장치를 본문까지** — 고정폭 'DELIVERED · …' 줄 · 주황 테이프 띠(화살표 + OPEN NEW POSSIBILITIES) · 송장 라벨(바코드 · 보내는 분 · 받는 분 · 물품명 · NXT 번호 · 주황 도장) · 위 테두리 주황인 꺼낸 카드 세 장 · 표지 원화의 택배 상자 · 빌린 본문 #87 #76 #73 |
| #109 | 피사체는 그대로, 시선은 새로 | B | https://szxv7704-dot.github.io/design-reference-gallery/covers/109.html | https://szxv7704-dot.github.io/design-reference-gallery/covers/109.css | **표지의 장치를 본문까지** — 전시 포스터 틀(위 가는 줄 'NEW WAYS OF SEEING ··· EXHIBITION / 0n', 아래 질문과 'PERSPECTIVE / ANALOG STUDY') · 아주 굵은 고딕 결론 · 렌즈 조각 줄(장마다 하나씩 끼워짐) · 빨간 뷰파인더 꺾쇠 · 표지 원화의 렌즈 조각과 고양이 · 카메라 사진 · 빌린 본문 #53 #94 |

## 와우 포인트 (24가지, 기법 하나 = 덱 하나)

발표 연출 기법. 덱마다 3장(표지 · 크게 보기 · 쓰는 법). 한 발표에 한두 번만 쓴다.

| 번호 | 기법 | 묶음 | 한 줄 | 이럴 때 | 쓰는 곳 | 덱 |
|---|---|---|---|---|---|---|
| 01 | 리빌 | 드러내기·이동 | 가려 둔 만큼, 열릴 때 커진다. | "다음 단계로 넘어갑니다" / "새로 시작합니다" | 표지, 슬로건 공개, 새 출발 선언 | https://szxv7704-dot.github.io/design-reference-gallery/wow/01.html |
| 02 | 점진적 공개 | 드러내기·이동 | 청중이 발표자 속도로 읽게 된다. | "구조가 복잡하지만 따라오세요" | 비전 체계도, 단계 절차, 복잡한 구조 | https://szxv7704-dot.github.io/design-reference-gallery/wow/02.html |
| 03 | 줌 인 | 드러내기·이동 | 지도를 먼저 쥐여 주고 한 곳으로 데려간다. | "구조가 복잡하지만 따라오세요" | 공간·시설 계획, 세부 과제 설명 | https://szxv7704-dot.github.io/design-reference-gallery/wow/03.html |
| 04 | 허브 이동 | 드러내기·이동 | 고른 곳으로 들어갔다 나온다. 질문에 바로 답한다. | — | 업무보고, 질의응답이 많은 자리 | https://szxv7704-dot.github.io/design-reference-gallery/wow/04.html |
| 05 | 비포/애프터 | 대비·전환 | 구도가 같으면 눈은 바뀐 곳만 본다. | "이만큼 바뀝니다" | 현행 대비 개선, 공간·환경 개선, 서식 간소화 | https://szxv7704-dot.github.io/design-reference-gallery/wow/05.html |
| 06 | 연속 변형 | 대비·전환 | 같은 도형이 모양만 바꿔 '같은 돈'임을 증명한다. | "이만큼 바뀝니다" | 예산 재분할, 구성비 변화, 조직 개편 | https://szxv7704-dot.github.io/design-reference-gallery/wow/06.html |
| 07 | 수미상관 | 대비·전환 | 첫 장면으로 돌아오면 이야기가 닫힌다. | "해마다 돌며 나아집니다" | 순환·환류 체계, 덱의 마지막 장 | https://szxv7704-dot.github.io/design-reference-gallery/wow/07.html |
| 08 | 큰 숫자 하나 | 숫자 체감 | 하나만 크게. 나머지는 조연으로 물린다. | "이 숫자가 심각합니다" / "이게 결론입니다" | 핵심 현황, 결론 장표 | https://szxv7704-dot.github.io/design-reference-gallery/wow/08.html |
| 09 | 단위 차트 | 숫자 체감 | 41%를 '100칸 중 41칸'으로 바꿔 몸으로 느끼게. | "이 숫자가 심각합니다" | 비율, 발생률, 참여율 | https://szxv7704-dot.github.io/design-reference-gallery/wow/09.html |
| 10 | 카운트업 | 숫자 체감 | 올라가는 동안 긴장이 쌓이고, 멈출 때 터진다. | "목표에 닿았습니다(닿을 겁니다)" | 참여 인원, 목표 달성, 누적 성과 | https://szxv7704-dot.github.io/design-reference-gallery/wow/10.html |
| 11 | 데이터 레이스 | 숫자 체감 | 순위가 뒤집히는 순간이 곧 드라마다. | "순위·흐름이 뒤집혔습니다" | 연도별 추이, 기관·지역 순위 변화 | https://szxv7704-dot.github.io/design-reference-gallery/wow/11.html |
| 12 | 시각 은유 | 은유·세계관 | 추상적인 정책이 사물 하나로 한 번에 이해된다. | "여럿이 함께 만듭니다" | 표지, 비전, 추진 체계 | https://szxv7704-dot.github.io/design-reference-gallery/wow/12.html |
| 13 | 생활 서식 빌려 오기 | 은유·세계관 | 익숙한 틀을 엉뚱한 자리에 두면 눈이 멈춘다. | — | 표지, 홍보물, 연수 안내 | https://szxv7704-dot.github.io/design-reference-gallery/wow/13.html |
| 14 | 게임화 | 은유·세계관 | 다년 계획을 레벨처럼 '깨 나가는' 이야기로. | "목표에 닿았습니다(닿을 겁니다)" | 다년 계획, 단계별 확대, 학생·연수 대상 | https://szxv7704-dot.github.io/design-reference-gallery/wow/14.html |
| 15 | 물리 모션 | 은유·세계관 | 무게와 충돌이 '진짜 같다'는 실감을 준다. | "여럿이 함께 만듭니다" | 분류, 선후 관계, 결합 구조 | https://szxv7704-dot.github.io/design-reference-gallery/wow/15.html |
| 16 | 키네틱 타이포 | 감각·형식 | 그림 없이 글자만으로 장면이 된다. | — | 제목, 슬로건, 간지 | https://szxv7704-dot.github.io/design-reference-gallery/wow/16.html |
| 17 | 재질·질감 | 감각·형식 | 매끈한 화면 사이에서 만질 수 있을 것 같은 장면. | — | 친환경, 지역·문화, 아동 대상 | https://szxv7704-dot.github.io/design-reference-gallery/wow/17.html |
| 18 | 3D·깊이 | 감각·형식 | 평면 장표들 사이에서 깊이 하나가 튀어 오른다. | "해마다 돌며 나아집니다" | 누적 지원, 층위 구조, 지형·분포 | https://szxv7704-dot.github.io/design-reference-gallery/wow/18.html |
| 19 | 극단적 여백 | 감각·형식 | 남은 하나에 시선이 전부 모인다. | "새로 시작합니다" | 표지, 간지, 결론 한 문장 | https://szxv7704-dot.github.io/design-reference-gallery/wow/19.html |
| 20 | 팡! 터뜨리기 | 소리가 보이는 모션 | 터지는 순간 화면이 축제가 된다. | "목표에 닿았습니다(닿을 겁니다)" | 목표 달성, 개막, 마무리 장 | https://szxv7704-dot.github.io/design-reference-gallery/wow/20.html |
| 21 | 칙칙폭폭 지나가기 | 소리가 보이는 모션 | 입체 글자 하나하나가 객차가 되어 들어와 멈추며 읽힌다. | "다음 단계로 넘어갑니다" | 연도별 일정, 단계 전환, 슬로건 공개 | https://szxv7704-dot.github.io/design-reference-gallery/wow/21.html |
| 22 | 또롱또롱 떨어지기 | 소리가 보이는 모션 | 같은 박자로 하나씩 생겨 개수와 순서가 몸에 남는다. | "구조가 복잡하지만 따라오세요" | 과제 목록, 절차 단계, 핵심어 나열 | https://szxv7704-dot.github.io/design-reference-gallery/wow/22.html |
| 23 | 쿵! 내려앉기 | 소리가 보이는 모션 | 무거운 착지와 흔들림이 '이게 결론'이라고 알린다. | "이게 결론입니다" | 결론 한 문장, 핵심 숫자 | https://szxv7704-dot.github.io/design-reference-gallery/wow/23.html |
| 24 | 타이포 조립 | 소리가 보이는 모션 | "무슨 글자지?" 하다가 한순간 맞춰지며 "아!" 하게 된다. | "새로 시작합니다" | 표지 제목, 연도·슬로건 공개, 간지 | https://szxv7704-dot.github.io/design-reference-gallery/wow/24.html |

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
| I 원과 반원 | 가로 이정표 | 낱말과 뜻 | 기준별 두 열 | 세로 단계 | 한 건 이야기 | 할 일과 조건 | 숫자 셋 | 네 칸 정리 |
| J 사선 띠 | 번호 카드 | 낱말과 뜻 | 짝 줄 | 세로 단계 | 사람의 말 | 체크 목록 | 숫자 하나 크게 | 한 문장 |
| K 모듈 격자 | 줄 목록 | 맞는 예와 아닌 예 | 전과 후 수치 | 단계 표 | 화면 짚기 | 질문과 보기 | 숫자 하나 크게 | 세 줄 |
| L 점 격자 | 가로 이정표 | 세 요소로 풀기 | 짝 줄 | 단계 표 | 한 건 이야기 | 할 일과 조건 | 목표 대비 막대 | 네 칸 정리 |

## 그 밖

- 표지 레퍼런스 설명(분위기 · 가져갈 장치): https://szxv7704-dot.github.io/design-reference-gallery/catalog/refs.md
- 참고 본문 장표(도식 아이디어): https://szxv7704-dot.github.io/design-reference-gallery/catalog/body.md · 아이콘 85개: https://szxv7704-dot.github.io/design-reference-gallery/catalog/icons.md
- 사람용 이용 방법: https://szxv7704-dot.github.io/design-reference-gallery/ai.html
