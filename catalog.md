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

## 구성 (모든 스타일에 같은 이름으로 있다)

| 역할 | 구성 | 이럴 때 | 알맞은 분량 | 넘치면 | 이럴 땐 다른 구성 | 부품 |
|---|---|---|---|---|---|---|
| 표지 | 표지 | 발표의 이름과 분위기를 한 장으로 연다 | 제목 2줄 이하, 부제 1줄 | 부제를 뺀다 | — | `.cover` |
| 목차 · 전체 흐름 | 목차 | 오늘 무엇을 어떤 순서로 다루는지 먼저 보여 준다 | 3~5줄 | 큰 묶음으로 합친다 | 순서보다 날짜가 중요하면 일정(이정표)으로 | `.toc + .toc-list` |
|  | 일정 | (추진 일정 · 연혁 · 과정 지도) | 이정표 3~5개(.mile) 또는 줄 3~5개 × 12달(.gantt) | 분기 · 학기로 묶는다 |  | `.mile` |
| 핵심 개념 · 정의 | 용어 정의 | 모두가 같은 뜻으로 쓰도록 낱말 하나를 맞춘다 | 용어 1개 + 뜻 한 문장 + 예 1~2개 | 용어마다 한 장 | 정의가 아니라 주장 한 줄이면 한 문장으로 | `.define` |
|  | 한 문장 | (목적 · 비전 · 결론처럼 한 문장이 전부인 곳) | 40자 이하 한 문장 + 받치는 말 1줄 | 받치는 말을 다음 장으로 |  | `.say` |
| 비교 | 둘 비교 | 두 대상이나 전 · 후를 같은 줄에 놓고 견준다 | 2~3줄, 줄마다 왼쪽 · 오른쪽 한 짝 | 4줄부터 두 장 | 숫자가 있는 전 · 후면 전→후로, 셋 이상이면 표로 | `.fix (+ .stack)` |
|  | 전→후 | (현행 → 개선, 사업 전 → 사업 후(숫자가 있는 짝)) | 2~3짝, 같은 기준 · 같은 단위 | 가장 큰 변화 3짝만 |  | `.ba (+ .ba-head)` |
| 순서 · 절차 | 순서·단계 | 따라 할 차례를 단계로 나눈다 | 3~4단계, 단계마다 이름 + 할 일 3줄 이하 | 5단계부터 두 장 | 차례가 없고 갈래만 있으면 묶음 · 분류로 | `.road` |
| 사례 · 화면 설명 | 화면 짚기 | 실제 화면이나 현장을 보여 주고 짚을 곳을 표시한다 | 캡처 1장 + 번호 표시 3개 이하 | 동작 하나에 한 장 | 화면이 없고 사람의 말이 있으면 인용으로 | `.shot + .shot-img` |
|  | 사진+글 | (사례 · 현장 사진 · 활동 모습) | 사진 1~3장, 사진마다 제목 + 한 줄 + 말 한마디 | 사진마다 한 장 |  | `.case + .ph` |
|  | 인용 | (참여자 말 · 설문 서술 답 · 법령 조문) | 1~3개, 각 60자 이하, 말한 사람 | 가장 강한 것 하나만 |  | `.quote` |
| 실습 과제 · 행동 안내 | 할 일 | 청중이 지금 할 일 하나와 그 조건(시간 · 결과물)을 알린다 | 할 일 한 문장 + 조건 칸 2~3개(시간 · 결과물 · 도움) | 할 일마다 한 장 | 할 일이 아니라 생각할 거리면 질문으로 | `.todo` |
|  | 질문 | (여는 질문 · 토의 주제 · 퀴즈 · 자주 묻는 질문) | 질문 1개 + 보기 4개 이하(ol) 또는 답 1개(.a-a) | 질문마다 한 장 |  | `.ask` |
| 핵심 수치 · 근거 | 큰 숫자 | 주장을 받치는 숫자를 크게 보여 준다 | 1~4개, 숫자마다 단위 + 한 줄 | 가장 중요한 3개만 | 여러 해의 변화면 추이, 몫이면 구성비, 항목 비교면 막대로 | `.tile (+ .delta)` |
|  | 막대 비교 | (항목 간 크기 비교 · 순위 · 목표 대비 실적) | 3~5줄, 한 가지 단위 | 위 4개 + 나머지 합 |  | `.goal + .g-row` |
|  | 추이 | (여러 해 · 여러 달에 걸친 변화) | 3~8시점, 한 가지 값 | 시점을 줄인다 |  | `.trend` |
|  | 구성비 | (전체 중 몫 · 재원 비율) | 2~5조각, 합 100% | 작은 조각은 기타로 |  | `.share + .sh-bar` |
|  | 표 | (표로 된 지원 내용 · 항목 목록 · 예산 내역) | 3~5행 × 3~4열, 칸마다 1줄 | 6행부터 두 장, 또는 핵심 열만 |  | `.tbl` |
| 요약 | 항목 | 기억할 것을 세 줄 안팎으로 줄인다 | 3~5개, 이름 + 설명 1~2줄(5개면 1줄) | 6개부터 두 장, 또는 묶음·분류로 | 한 줄이면 한 문장으로 | `.points` |
| 마무리 · 다음 행동 | 맺음 | 마지막 한 문장과 문의 · 다음 일정을 남긴다 | 두 줄 문장 + 연락처 한 줄 | — | — | `.close` |
| 그 밖의 구성 | 묶음·분류 | 갈래로 나누기 · 체계 · 섹션 간지 | 2~4묶음, 묶음마다 3줄 이하 | 묶음마다 한 장 | — | `.card + .grid.g2/.g3/.g4` |
|  | 체계 | (비전 → 전략 → 과제, 추진 체계, 조직도) | 맨 위 1 + 갈래 2~4 + 갈래마다 2~3줄 | 갈래마다 한 장, 또는 표로 |  | `.tree` |
|  | 간지 | (큰 번호가 바뀌는 자리) | 번호 + 이름 + 한 줄 | — |  | `.divider` |

구성의 코드는 각 스타일의 적용 안내(`kit/{ID}.md`)에 들어 있다. 모든 구성을 다 쓸 필요는 없고, 같은 구성을 여러 번 써도 된다.

## 그 밖

- 표지만 있는 디자인 27개(이어지는 본문 없음, 참고용): https://szxv7704-dot.github.io/design-reference-gallery/catalog/refs.md
- 참고 본문 장표(도식 아이디어): https://szxv7704-dot.github.io/design-reference-gallery/catalog/body.md · 아이콘 85개: https://szxv7704-dot.github.io/design-reference-gallery/catalog/icons.md
- 사람용 이용 방법: https://szxv7704-dot.github.io/design-reference-gallery/guide.html
