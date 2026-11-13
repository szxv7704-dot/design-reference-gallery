# B 미니멀 스튜디오 — 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **Claude · ChatGPT 같은 채팅 AI**에게 자기 문서와 함께 주면, 문서 내용을 이 디자인의 16:9 발표 덱으로 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 B 계열 장표(#19 · #26 · #28 · #37 · #46 · #116)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일과 발표할 문서**(한글 · PDF · 붙여 넣은 글)를 넣습니다.
2. 어떤 자리인지 말합니다. 예) "이 계획안으로 10분짜리 발표 덱을 만들어 줘. 결과는 .html 파일로."
3. AI가 먼저 **장별 구성안**을 보여 줍니다. 고칠 곳을 말하거나 "좋아, 만들어 줘".
4. 받은 `.html`을 내려받아 더블클릭합니다. → · Space로 넘기고, F는 전체 화면, 인쇄하면 장마다 한 쪽(16:9) PDF가 됩니다.
5. 고칠 곳은 "3장 제목을 ○○로"처럼 말합니다. 코드가 끊기면 "끊긴 곳부터 이어서".

알아 둘 점
- 열 때 **인터넷이 필요**합니다(공통 CSS · 엔진 · 글꼴을 `szxv7704-dot.github.io`에서 불러옴). 인터넷이 막힌 곳에서 발표하려면 저장소에서 `python3 scripts/kit.py inline B 슬라이드.html`을 실행해 모든 것이 파일 안에 든 판을 만드세요.
- 수치는 AI가 지어내지 않도록 적어 두었지만, **받은 덱의 숫자를 원문과 꼭 대조**하세요.
- 개인정보(학생 이름 · 사진 등)는 AI에게 넣지 마세요.

## 라이선스

- 글꼴: 모두 SIL Open Font License 1.1(전문 https://szxv7704-dot.github.io/design-reference-gallery/fonts/OFL.txt). 이 계열이 쓰는 글꼴의 저작권 고지:

| 글꼴 | 굵기 | 저작권 | 예약 이름 | 라이선스 |
|---|---|---|---|---|
| GothicA1 | 300 · 400 · 500 · 600 · 700 · 800 · 900 | (C) Copyright HanYang I&C Co.,Ltd. All rights reserved. | — | SIL OFL 1.1 |
| IBMPlexMono | 400 · 500 · 600 · 700 | Copyright 2017 IBM Corp. All rights reserved. | — | SIL OFL 1.1 |
| IBMPlexSansKR | 300 · 400 · 500 · 600 · 700 | Copyright 2018 IBM Corp. All rights reserved. | — | SIL OFL 1.1 |

- 공통 CSS · 엔진 · 이 지시서: 디자인 레퍼런스 갤러리 저장소의 일부(가상 예시 자료).

---

# ▼▼▼ 여기부터 AI에게 주는 지시서 ▼▼▼

(위의 "사용법"과 "라이선스"는 사람을 위한 안내입니다. AI는 아래를 따르세요.)

## 0. 당신(AI)의 일

사용자가 준 **문서**(한글 계획안 · 연수 강의안 · 성과 보고 등)의 내용으로 **16:9 발표 덱 HTML 파일 하나**를 만듭니다.
이 안내의 **기본 장표(3)** · **흐름(4)** · **견본 코드(8)**를 재료로 씁니다. 색 · 글꼴 · 부품 모양은 뼈대(6)의 두 줄이 인터넷에서 불러오므로, **당신이 쓰는 것은 `<section class="slide">`들뿐**입니다.

## 1. 진행 순서

1. **문서를 읽습니다.** 문서가 없으면 달라고 합니다. 발표 자리(계획안 발표 · 성과 공유회 · 설명회 · 연수)와 발표 시간을 모르면 짧게 묻습니다.
2. **흐름을 고릅니다(4).** 문서 종류에 맞는 흐름의 자리 순서를 따르되, 문서에 없는 자리는 뺍니다.
3. **문단마다 기본 장표를 고릅니다(3).** 한 장에 기본 장표 하나. 내용 조건을 넘치면 장을 나눕니다.
4. 분위기 계열은 **B 미니멀 스튜디오**입니다.
5. **구성안을 먼저 보여 주고 확인을 받습니다.** 장마다 `자리 | 기본 장표 | 제목 한 문장 | 쓸 내용(문서의 어느 부분) | 수치와 출처`를 표 한 줄로. 이때 코드를 쓰지 않습니다. 사용자가 "구성 확인 없이 바로"라고 했으면 건너뜁니다.
6. 확인을 받으면 HTML을 만들고, 점검(9)을 거쳐 내보냅니다.

## 2. 반드시 지킬 것

1. **문서에 없는 숫자 · 연도 · 예산 · 이름 · 출처를 지어내지 않습니다.** 비어 있으면 묻거나 그 장을 뺍니다. 문서에 없는 사실을 넣고 싶으면 구성안에 '추가 사실'로 따로 적어 확인을 받습니다.
2. **한 장에 기본 장표 하나.** 도식 두 개가 필요하면 두 장으로 나눕니다. 글자를 줄여 한 장에 밀어 넣지 않습니다.
3. 본문 장은 `머리말(.kicker) + 제목(.title) + 부품` 순서입니다. **제목은 결론 한 문장**, 두 줄 이내. "현황" 같은 이름표는 머리말에 씁니다. 한 문장 · 질문 · 할 일 장만 제목 없이 머리말 아래에 부품을 둡니다.
4. 수치가 있는 장에는 출처(`.src`)를 씁니다.
5. **강조색은 한 장에 한 곳**: 제목의 `<em>` 하나 또는 부품의 `.is-key` 하나(둘 다 쓰면 같은 내용을 가리켜야 함).
6. **클래스는 견본 코드(8)에 나온 것만** 씁니다. 없는 클래스는 모양이 없어 배치가 무너집니다. 새 부품이 꼭 필요하면 뼈대 `<style>`의 '추가 부품' 줄 아래에 토큰 변수(`--ds-*`)만으로 정의합니다.
7. 뼈대의 공통 파일 두 줄(`<link>` · `<script src>`)은 주소 한 글자도 바꾸지 않습니다. 공통 CSS · 엔진을 HTML 안에 옮겨 쓰거나 `@font-face`를 새로 쓰지 않습니다.
8. 장 번호 · 쪽 표시 · 점은 쓰지 않습니다. 엔진이 채웁니다(`<span class="page-no"></span>`는 빈 칸 그대로).
9. 무대는 1920 × 1080이고 화면에 맞게 통째로 줄어듭니다. 글자 크기를 바꾸지 않습니다. 머리말과 두 줄 제목 아래 **본문 높이는 약 600~680px**이고 넘친 부분은 잘립니다. 넘치면 문장을 줄이거나 장을 나눕니다.
10. 인라인 `style`은 값 전달에만 씁니다: 막대 `--v`(가장 큰 값 = 100) · 목표선 `--t` · 간트 `--from` `--to`(1~12월) · 체계 갈래 수 `--n` · 화면 짚기 번호 자리 `--x` `--y`(%).
11. **그림을 코드로 그리지 않습니다.** SVG · CSS · 캔버스로 사물 · 인물 · 풍경 · 캐릭터 · 지도를 그리지 마세요. 사진 · 화면 캡처는 사용자가 준 이미지를 `.ph` 안에 `<img>`로 넣고, 없으면 `<div class="ph" data-need="사진 자리 · 4:3 · 무슨 장면"></div>`로 자리만 두고 무엇이 필요한지 말해 줍니다.
12. 누를 때마다 하나씩 보이는 장(`data-steps` + `data-step`)은 덱 전체에서 1~3장. 같은 기본 장표가 세 장 넘게 연달아 나오지 않게 합니다.

## 3. 기본 장표 23가지 (내용의 모양으로 고릅니다)

| 기본 장표 | `id` | 문서에서 이런 내용이면 | 내용 조건 | 부품 |
| --- | --- | --- | --- | --- |
| 표지 | `cover` | 문서 제목 · 기관 · 날짜 | 제목 2줄 이하, 부제 1줄 | `.cover` |
| 목차 | `toc` | 문서의 큰 번호(Ⅰ · Ⅱ · Ⅲ), 차시 순서 | 3~5줄 | `.toc` + `.toc-list` |
| 간지 | `divider` | 큰 번호가 바뀌는 자리 | 번호 + 이름 + 한 줄 | `.divider` |
| 맺음 | `closing` | 문의처 · 담당 · 다음 차시 예고 | 두 줄 문장 + 연락처 한 줄 | `.close` |
| 한 문장 | `statement` | 목적 · 비전 · 결론처럼 한 문장이 전부인 곳 | 40자 이하 한 문장 + 받치는 말 1줄 | `.say` |
| 항목 | `points` | 개조식(□ · ○ · -) 항목 3~5개, 학습 목표, 기대 효과 | 3~5개, 이름 + 설명 1~2줄(5개면 1줄) | `.points` |
| 용어 정의 | `define` | "○○란", 용어 풀이, 개념 설명 | 용어 1개 + 뜻 한 문장 + 예 1~2개 | `.define` |
| 인용 | `quote` | 참여자 말 · 설문 서술 답 · 법령 조문 | 1~3개, 각 60자 이하, 말한 사람 | `.quote` |
| 순서·단계 | `steps` | 절차 · 신청 방법 · 따라 하기 · 단계별 추진 · 향후 계획 | 3~4단계, 단계마다 이름 + 할 일 3줄 이하 | `.road` |
| 둘 비교 | `compare` | 문제점 ↔ 개선 방안, 문단 ↔ 고른 장표, 기존안 ↔ 새 안 | 2~3줄, 줄마다 왼쪽 · 오른쪽 한 짝 | `.fix` (+ `.stack`) |
| 전→후 | `before-after` | 현행 → 개선, 사업 전 → 사업 후(숫자가 있는 짝) | 2~3짝, 같은 기준 · 같은 단위 | `.ba` (+ `.ba-head`) |
| 묶음·분류 | `groups` | 과제 · 프로그램을 갈래로 나눈 것 | 2~4묶음, 묶음마다 3줄 이하 | `.card` + `.grid.g2/.g3/.g4` |
| 체계 | `tree` | 비전 → 전략 → 과제, 추진 체계, 조직도 | 맨 위 1 + 갈래 2~4 + 갈래마다 2~3줄 | `.tree` |
| 큰 숫자 | `numbers` | 핵심 실적 · 규모 · 예산 총액 | 1~4개, 숫자마다 단위 + 한 줄 | `.tile` (+ `.delta`) |
| 막대 비교 | `bars` | 항목 간 크기 비교 · 순위 · 목표 대비 실적 | 3~5줄, 한 가지 단위 | `.goal` + `.g-row` |
| 추이 | `trend` | 여러 해 · 여러 달에 걸친 변화 | 3~8시점, 한 가지 값 | `.trend` |
| 구성비 | `share` | 전체 중 몫 · 재원 비율 | 2~5조각, 합 100% | `.share` + `.sh-bar` |
| 표 | `table` | 표로 된 지원 내용 · 항목 목록 · 예산 내역 | 3~5행 × 3~4열, 칸마다 1줄 | `.tbl` |
| 일정 | `timeline` | 추진 일정 · 연혁 · 과정 지도 | 이정표 3~5개(.mile) 또는 줄 3~5개 × 12달(.gantt) | `.mile` |
| 사진+글 | `photo` | 사례 · 현장 사진 · 활동 모습 | 사진 1~3장, 사진마다 제목 + 한 줄 + 말 한마디 | `.case` + `.ph` |
| 화면 짚기 | `screen` | 프로그램 화면 · 서식 · 누리집 사용법 | 캡처 1장 + 번호 표시 3개 이하 | `.shot` + `.shot-img` |
| 질문 | `ask` | 여는 질문 · 토의 주제 · 퀴즈 · 자주 묻는 질문 | 질문 1개 + 보기 4개 이하(ol) 또는 답 1개(.a-a) | `.ask` |
| 할 일 | `todo` | 실습 안내 · 과제 · 제출 서류 · 신청 기한 | 할 일 한 문장 + 조건 칸 2~3개(시간 · 결과물 · 도움) | `.todo` |

**역할마다 배치가 다른 구성 셋** — 같은 역할이라도 내용에 따라 배치를 고릅니다. 코드는 8에서 `구성: 역할 · 이름`으로 찾습니다. ★ = 이 스타일의 10장 예시가 쓴 구성(따라 할 필요는 없고, 내용에 맞는 것을 고릅니다).

| 역할 | 구성 | 모습 | 이럴 때 | 분량 | 부품 |
| --- | --- | --- | --- | --- | --- |
| 목차 · 전체 흐름 | 줄 목록 ★ | 번호 · 이름 · 시간이 한 줄씩, 옆에 스타일의 상징 | 차례만 알리면 될 때. 가장 무난하다 | 3~5줄 | `.toc-list` |
|  | 가로 이정표 | 가로선 위에 점을 찍고 시간 · 이름 · 한 줄 | 시간 배분이나 날짜가 중요할 때 | 3~5개 | `.mile` |
|  | 번호 카드 | 큰 번호가 붙은 카드를 가로로 나란히 | 단계마다 이름을 또렷이 기억시키고 싶을 때 | 3~5칸 | `.agenda` |
| 핵심 개념 · 정의 | 낱말과 뜻 ★ | 왼쪽에 낱말, 오른쪽에 뜻 한 문장과 예 | 낯선 낱말 하나를 사전처럼 풀 때 | 낱말 1 + 뜻 1문장 + 예 1~2 | `.define` |
|  | 세 요소로 풀기 | 개념을 이루는 요소를 카드 셋으로 | 개념이 몇 가지 요소로 이루어져 있을 때 | 2~4칸, 칸마다 3줄 이하 | `.card` + `.grid.g3` |
|  | 맞는 예와 아닌 예 | 위에 낱말, 아래 두 칸에 ○ 예와 × 예 | 자주 헷갈리는 것과 선을 그어야 할 때 | 쪽마다 예 2~3개 | `.yesno` |
| 비교 | 짝 줄 | 줄마다 왼쪽 → 오른쪽 한 짝 | 같은 것을 이렇게 바꾸라고 보여 줄 때 | 2~3줄 | `.fix` + `.stack` |
|  | 전과 후 수치 | 같은 지표의 숫자를 좌우에 크게 | 두 쪽을 숫자로 견줄 수 있을 때 | 2~3짝, 같은 단위 | `.ba` + `.ba-head` |
|  | 기준별 두 열 ★ | 기준 | 왼쪽 | 오른쪽 세 열의 대조표 | 여러 기준으로 두 대상을 따질 때 | 기준 3~4줄, 칸마다 1줄 | `.vs` |
| 순서 · 절차 | 가로 세 칸 ★ | 단계마다 한 칸, 칸 안에 할 일 목록 | 단계마다 할 일이 여러 줄일 때 | 3~4단계, 단계마다 3줄 이하 | `.road` |
|  | 세로 단계 | 번호 동그라미를 세로선으로 잇고 이름 + 한 줄 | 단계가 4~5개이고 단계마다 한 줄이면 될 때 | 3~5단계, 단계마다 1줄 | `.stepper` |
|  | 단계 표 | 단계 | 할 일 | 쓰는 것 | 시간의 표 | 단계마다 같은 항목(담당 · 도구 · 시간)을 견줄 때 | 3~5행 × 3~4열 | `.tbl` |
| 사례 · 화면 설명 | 화면 짚기 ★ | 캡처 한 장에 번호를 찍고 옆에 설명 | 실제 화면의 어디를 누르는지 보여 줄 때 | 캡처 1장 + 번호 3개 이하 | `.shot` + `.shot-img` |
|  | 사람의 말 | 말 풍선 세 개, 가장 중요한 말 하나를 강조 | 화면이 없고 써 본 사람의 말이 있을 때 | 1~3개, 각 60자 이하 | `.quote` |
|  | 한 건 이야기 | 상황 → 한 일 → 결과 세 칸 | 한 사례를 처음부터 끝까지 들려줄 때 | 세 칸, 칸마다 이름 + 2줄 | `.story` |
| 실습 과제 · 행동 안내 | 할 일과 조건 ★ | 할 일 한 문장을 크게, 아래에 시간 · 결과물 · 도움 | 과제가 하나이고 조건을 알려야 할 때 | 한 문장 + 조건 2~3칸 | `.todo` |
|  | 질문과 보기 | 질문 하나와 고를 보기 넷 | 하기 전에 먼저 고르거나 생각하게 할 때 | 질문 1 + 보기 4개 이하 | `.ask` |
|  | 체크 목록 | 네모 칸이 달린 확인 목록 | 하면서 스스로 확인할 것이 여럿일 때 | 3~5줄 | `.check` |
| 핵심 수치 · 근거 | 숫자 셋 | 숫자 타일 셋을 나란히 | 받치는 숫자가 둘 이상일 때 | 2~4개, 숫자마다 단위 + 한 줄 | `.tile` + `.grid.g3` |
|  | 숫자 하나 크게 ★ | 왼쪽에 아주 큰 숫자 하나, 오른쪽에 뜻과 받치는 두 줄 | 기억시킬 숫자가 딱 하나일 때 | 숫자 1 + 뜻 1문장 + 2줄 | `.big` |
|  | 목표 대비 막대 | 지표마다 막대와 목표선 | 여러 지표의 달성 정도를 견줄 때 | 3~5줄, 한 가지 단위 | `.goal` + `.g-row` |
| 요약 | 세 줄 ★ | 번호가 붙은 세 줄, 이름 + 설명 | 기억할 것이 서너 가지일 때 | 3~5개 | `.points` |
|  | 네 칸 정리 | 이름표가 붙은 네 칸 | 누가 · 무엇을 · 언제처럼 항목이 정해져 있을 때 | 3~4칸, 칸마다 2줄 | `.brief` |
|  | 한 문장 | 화면 가운데 큰 한 문장과 받치는 말 | 한 줄로 줄일 수 있을 때 | 40자 이하 한 문장 + 1줄 | `.say` |

같은 역할이 한 덱에 여러 번 나오면 구성을 바꿔 가며 씁니다(모든 장이 같은 배치가 되지 않게).

**고르는 순서** — 한 문단이 둘 이상에 맞으면 위에서부터 먼저 맞는 것:

1. 숫자가 주인공이면 수 묶음(하나면 큰 숫자, 시간 축이 있으면 추이, 합이 100%면 구성비, 나머지는 막대 비교).
2. 날짜가 주인공이면 일정.
3. 두 쪽이 맞서면 둘 비교, 같은 것이 달라졌으면 전→후.
4. 차례가 있으면 순서·단계, 위아래가 있으면 체계, 갈래만 있으면 묶음·분류.
5. 칸이 3열 이상 필요하면 표.
6. 어디에도 안 맞으면 항목. 항목이 한 개면 한 문장.

## 4. 흐름 (문서 종류에 맞는 자리 순서)

자리 이름은 머리말(`.kicker`)과 목차에 씁니다. 장 수는 내용이 정하고, 문서에 없는 자리는 뺍니다.

**10장 세트 예시** — 세트의 열 가지 역할을 한 장씩. 스타일마다 구성 조합이 다르다(가상 주제: 생성형 AI 업무 활용 연수) · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/B-set.html

| 자리 | 기본 장표 |
| --- | --- |
| 표지 | 표지 |
| 전체 흐름 | 목차 · 일정 |
| 핵심 개념 · 정의 | 용어 정의 · 묶음·분류 |
| 비교 | 둘 비교 · 전→후 |
| 순서 · 절차 | 순서·단계 · 표 |
| 사례 · 화면 | 화면 짚기 · 인용 · 순서·단계 |
| 실습 · 행동 안내 | 할 일 · 질문 |
| 핵심 수치 · 근거 | 큰 숫자 · 막대 비교 |
| 요약 | 항목 · 한 문장 |
| 마무리 | 맺음 |

**다른 주제 시험** — 다른 내용에도 쓰이는지 보는 본문 다섯 장(가상 주제: 학교 독서 활동 소개) · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/B-set2.html

| 자리 | 기본 장표 |
| --- | --- |
| 프로그램 묶음 | 묶음·분류 |
| 추이 | 추이 |
| 인용 | 인용 |
| 일정 | 일정 |
| 질문 | 질문 |

**계획안 발표** — 계획안 문서의 내용을 발표로 옮길 때 · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/B-plan.html

| 자리 | 기본 장표 |
| --- | --- |
| 여는 장 | 표지 · 목차 |
| 추진 배경 | 한 문장 · 큰 숫자 · 막대 비교 · 추이 |
| 목표 · 추진 체계 | 한 문장 · 체계 |
| 세부 추진 과제 | 묶음·분류 · 항목 · 둘 비교 · 순서·단계 |
| 추진 일정 | 일정 |
| 예산 | 표 · 구성비 |
| 기대 효과 | 전→후 · 항목 |
| 맺는 장 | 맺음 |

**성과 공유회** — 한 해 사업의 결과를 알릴 때 · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/B.html

| 자리 | 기본 장표 |
| --- | --- |
| 여는 장 | 표지 · 목차 |
| 사업 개요 | 항목 |
| 추진 경과 | 일정 |
| 핵심 성과 | 큰 숫자 · 막대 비교 · 추이 · 구성비 |
| 우수 사례 | 사진+글 · 인용 |
| 변화 · 만족도 | 전→후 · 구성비 |
| 시사점 | 둘 비교 |
| 향후 계획 | 순서·단계 |
| 맺는 장 | 맺음 |

## 5. 분위기 계열: B 미니멀 스튜디오

전시관 모형대처럼 밝은 청백 무광. 주황은 한 장에 한 곳. 어울리는 자리: 어디에나 무난하다. 정하지 않았으면 이것. 자세한 규칙은 아래 '디자인 규칙'.

## 6. HTML 뼈대

```html
<!DOCTYPE html>
<html lang="ko" data-kit="B">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>발표 제목</title>
<!-- 이 계열의 공통 CSS(글꼴 · 색 · 부품). 주소를 바꾸지 마세요 -->
<link rel="stylesheet" href="https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/B.css">
<style>
/* === 추가 부품: 새 클래스가 꼭 필요할 때만 이 줄 아래에(토큰 변수만 사용) === */
</style>
</head>
<body>
<div class="deck"><main class="deck-stage">

<!-- 여기에 <section class="slide"> 를 장 수만큼 -->

</main></div>
<!-- 동작 엔진. 주소를 바꾸지 마세요 -->
<script src="https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/deck.js"></script>
</body>
</html>
```

- 공통 파일 두 줄은 그대로 둡니다.
- 열 때 인터넷이 필요합니다. AI 화면 안 미리보기에서 색 · 모양이 안 보여도 고치지 마세요(바깥 파일을 막는 미리보기가 있습니다). 내려받아 브라우저로 열면 정상입니다.

## 7. 상징 부품 (표지 · 목차 · 간지 · 맺음에 넣는 계열의 얼굴)

이 계열은 모형대 매스(`.mass`)를 씁니다. 목차 · 간지의 `.lit` 층 = 지금 섹션(아래층이 1섹션). 맺음은 `.spot`.

## 8. 기본 장표별 견본 코드

문구는 모두 가상 예시입니다. **구조와 클래스만 가져오고 문구는 하나도 남기지 않습니다.**

### 표지 · `cover`

- 이런 내용일 때: 문서 제목 · 기관 · 날짜
- 내용 조건: 제목 2줄 이하, 부제 1줄. 넘치면: 부제를 뺀다
- 부품: `.cover`

구성: **표지**

```html
<section data-pattern="cover" data-role="cover" data-var="a" class="slide cover">
  <div class="c-text">
    <span class="c-tag">교직원 연수 · 가상 예시</span>
    <h1>생성형 AI,<br><em>업무에 쓰는</em> 첫걸음</h1>
    <p class="c-sub">요청 한 줄을 바꾸면 결과가 달라집니다</p>
  </div>
  <div class="mass" aria-hidden="true"><i></i><i></i><i class="lit"></i><i></i><i></i></div>
  <p class="c-org"><span>○○교육청 교육연수원</span><span>2027. 3. 12.</span></p>
</section>
```

### 목차 · `toc`

- 이런 내용일 때: 문서의 큰 번호(Ⅰ · Ⅱ · Ⅲ), 차시 순서
- 내용 조건: 3~5줄. 넘치면: 큰 묶음으로 합친다
- 부품: `.toc` + `.toc-list`

구성: **목차 · 전체 흐름 · 줄 목록**

```html
<section data-pattern="toc" data-role="flow" data-var="a" class="slide toc">
  <div class="s-body">
    <p class="kicker">오늘의 흐름</p>
    <h2 class="title">50분 동안 다섯 걸음</h2>
    <ol class="toc-list">
      <li class="is-now"><b>01</b><span>개념 맞추기</span><span>5분</span></li>
      <li><b>02</b><span>좋은 요청과 나쁜 요청</span><span>10분</span></li>
      <li><b>03</b><span>따라 하기</span><span>10분</span></li>
      <li><b>04</b><span>실습</span><span>20분</span></li>
      <li><b>05</b><span>정리</span><span>5분</span></li>
    </ol>
  </div>
  <div class="mass" aria-hidden="true"><i class="lit"></i><i></i><i></i><i></i><i></i></div>
  <span class="page-no"></span>
</section>
```

구성: **목차 · 전체 흐름 · 번호 카드**

```html
<section data-pattern="toc" data-role="flow" data-var="c" class="slide">
  <div class="s-body">
    <p class="kicker">오늘의 흐름</p>
    <h2 class="title">50분 동안 <em>다섯 걸음</em>을 걷습니다</h2>
    <ol class="agenda fill">
      <li><b>01</b><span>개념 맞추기</span><small>5분</small></li>
      <li><b>02</b><span>좋은 요청과 나쁜 요청</span><small>10분</small></li>
      <li><b>03</b><span>따라 하기</span><small>10분</small></li>
      <li class="is-key"><b>04</b><span>실습</span><small>20분 · 가장 길게</small></li>
      <li><b>05</b><span>정리</span><small>5분</small></li>
    </ol>
  </div>
  <span class="page-no"></span>
</section>
```

### 간지 · `divider`

- 이런 내용일 때: 큰 번호가 바뀌는 자리
- 내용 조건: 번호 + 이름 + 한 줄. 넘치면: —
- 부품: `.divider`

```html
<section data-pattern="divider" class="slide divider">
  <div class="d-no"><small>SECTION</small>03</div>
  <h2>세부 추진 과제</h2>
  <p>여섯 과제를 세 묶음으로 나눠 맡습니다.</p>
  <div class="mass" aria-hidden="true"><i></i><i></i><i class="lit"></i><i></i><i></i></div>
  <span class="page-no"></span>
</section>
```

### 맺음 · `closing`

- 이런 내용일 때: 문의처 · 담당 · 다음 차시 예고
- 내용 조건: 두 줄 문장 + 연락처 한 줄. 넘치면: —
- 부품: `.close`

구성: **마무리**

```html
<section data-pattern="closing" data-role="closing" data-var="a" class="slide close">
  <h2>오늘 쓴 요청문을<br>내일 업무에</h2>
  <p>문의 · ○○교육청 교육연수원 연수 담당</p>
  <div class="spot" aria-hidden="true"></div>
  <span class="page-no"></span>
</section>
```

### 한 문장 · `statement`

- 이런 내용일 때: 목적 · 비전 · 결론처럼 한 문장이 전부인 곳
- 내용 조건: 40자 이하 한 문장 + 받치는 말 1줄. 넘치면: 받치는 말을 다음 장으로
- 부품: `.say` — 이 장만 .title 없이 .kicker 아래에 둔다

구성: **요약 · 한 문장**

```html
<section data-pattern="statement" data-role="summary" data-var="c" class="slide">
  <div class="s-body">
    <p class="kicker">05 정리</p>
    <div class="say fill">
      <p>요청문에는 <em>누구에게 · 무엇으로 · 어떤 모양으로</em><br>세 가지를 적습니다</p>
      <small>받은 초안의 사실과 숫자는 꼭 원문과 다시 맞춰 봅니다.</small>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 항목 · `points`

- 이런 내용일 때: 개조식(□ · ○ · -) 항목 3~5개, 학습 목표, 기대 효과
- 내용 조건: 3~5개, 이름 + 설명 1~2줄(5개면 1줄). 넘치면: 6개부터 두 장, 또는 묶음·분류로
- 부품: `.points` — 네 칸으로 한눈에 보일 때는 .brief(목적 · 대상 · 기간 · 규모)

구성: **요약 · 세 줄**

```html
<section data-pattern="points" data-role="summary" data-var="a" class="slide">
  <div class="s-body">
    <p class="kicker">05 정리</p>
    <h2 class="title">오늘 배운 것은 <em>세 줄</em>입니다</h2>
    <ol class="points fill">
      <li class="is-key"><b>누구에게</b><p>읽을 사람과 말투를 먼저 적는다</p></li>
      <li><b>무엇으로</b><p>근거 자료를 붙이고 개인정보는 지운다</p></li>
      <li><b>어떤 모양으로</b><p>분량과 형식을 정하고, 받은 초안은 꼭 다시 읽는다</p></li>
    </ol>
  </div>
  <span class="page-no"></span>
</section>
```

구성: **요약 · 네 칸 정리**

```html
<section data-pattern="points" data-role="summary" data-var="b" class="slide">
  <div class="s-body">
    <p class="kicker">05 정리</p>
    <h2 class="title">오늘 내용은 <em>네 칸</em>에 담깁니다</h2>
    <div class="brief fill">
      <div><span>누구에게</span><b>읽을 사람과 말투</b><p>학부모 · 학생 · 동료</p></div>
      <div><span>무엇으로</span><b>근거 자료</b><p>개인정보는 지우고</p></div>
      <div><span>어떤 모양으로</span><b>분량과 형식</b><p>문단 · 표 · 목록</p></div>
      <div class="is-key"><span>마지막에</span><b>다시 읽기</b><p>숫자는 원문과 대조</p></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 용어 정의 · `define`

- 이런 내용일 때: "○○란", 용어 풀이, 개념 설명
- 내용 조건: 용어 1개 + 뜻 한 문장 + 예 1~2개. 넘치면: 용어마다 한 장
- 부품: `.define`

구성: **핵심 개념 · 낱말과 뜻**

```html
<section data-pattern="define" data-role="concept" data-var="a" class="slide">
  <div class="s-body">
    <p class="kicker">01 개념 맞추기</p>
    <h2 class="title">먼저 <em>프롬프트</em>라는 말부터 맞춥니다</h2>
    <dl class="define fill">
      <dt>프롬프트<small>AI에게 건네는 요청문</small></dt>
      <dd>
        <p>무엇을, 누구를 위해, 어떤 모양으로 쓸지 AI에게 알려 주는 글입니다.</p>
        <ul><li>가정통신문 초안을 학부모 눈높이로 써 줘</li><li>회의록을 결정 사항 세 줄로 줄여 줘</li></ul>
      </dd>
    </dl>
  </div>
  <span class="page-no"></span>
</section>
```

구성: **핵심 개념 · 맞는 예와 아닌 예**

```html
<section data-pattern="define" data-role="concept" data-var="c" class="slide">
  <div class="s-body">
    <p class="kicker">01 개념 맞추기</p>
    <div class="yesno fill">
      <p class="yn-term">프롬프트<small>AI에게 건네는 요청문</small></p>
      <div class="yn-yes"><h3>이런 것이 프롬프트</h3><ul><li>가정통신문 초안을 학부모 눈높이로 써 줘</li><li>회의록을 결정 사항 세 줄로 줄여 줘</li></ul></div>
      <div class="yn-no"><h3>이런 것은 아님</h3><ul><li>검색창에 넣는 낱말 몇 개</li><li>AI가 내놓은 답 그 자체</li></ul></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 인용 · `quote`

- 이런 내용일 때: 참여자 말 · 설문 서술 답 · 법령 조문
- 내용 조건: 1~3개, 각 60자 이하, 말한 사람. 넘치면: 가장 강한 것 하나만
- 부품: `.quote`

구성: **사례 · 사람의 말**

```html
<section data-pattern="quote" data-role="case" data-var="b" class="slide">
  <div class="s-body">
    <p class="kicker">03 따라 하기 · 써 본 사람들</p>
    <h2 class="title">가장 많이 나온 말은 <em>"다시 읽는 일이 남는다"</em>였습니다</h2>
    <div class="quote fill">
      <figure class="is-key"><blockquote>초안은 금방 나오지만, 숫자는 꼭 원문과 다시 맞춰 봐야 했어요.</blockquote><figcaption>초등학교 교무 담당</figcaption></figure>
      <figure><blockquote>읽을 사람을 적었더니 말투를 고칠 일이 줄었습니다.</blockquote><figcaption>중학교 담임 교사</figcaption></figure>
      <figure><blockquote>표로 달라고 하니 바로 붙여 쓸 수 있었습니다.</blockquote><figcaption>행정실 주무관</figcaption></figure>
    </div>
  </div>
  <p class="src">가상 예시</p>
  <span class="page-no"></span>
</section>
```

### 순서·단계 · `steps`

- 이런 내용일 때: 절차 · 신청 방법 · 따라 하기 · 단계별 추진 · 향후 계획
- 내용 조건: 3~4단계, 단계마다 이름 + 할 일 3줄 이하. 넘치면: 5단계부터 두 장
- 부품: `.road`

구성: **순서 · 절차 · 가로 세 칸**

```html
<section data-pattern="steps" data-role="steps" data-var="a" class="slide">
  <div class="s-body">
    <p class="kicker">03 따라 하기</p>
    <h2 class="title">요청문은 <em>세 걸음</em>으로 씁니다</h2>
    <div class="road fill">
      <div class="is-key"><h3><small>1</small>누구에게</h3><ul><li>읽을 사람을 적는다</li><li>학부모 · 학생 · 동료</li><li>말투도 함께</li></ul></div>
      <div><h3><small>2</small>무엇으로</h3><ul><li>근거 자료를 붙인다</li><li>계획서 · 설문 · 회의록</li><li>개인정보는 지우고</li></ul></div>
      <div><h3><small>3</small>어떤 모양으로</h3><ul><li>분량을 정한다</li><li>문단 · 표 · 목록</li><li>빠지면 안 될 것</li></ul></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

구성: **순서 · 절차 · 세로 단계**

```html
<section data-pattern="steps" data-role="steps" data-var="b" class="slide">
  <div class="s-body">
    <p class="kicker">03 따라 하기</p>
    <h2 class="title">요청문은 <em>네 단계</em>로 다듬습니다</h2>
    <ol class="stepper fill">
      <li><b>읽을 사람 적기</b><p>학부모 · 학생 · 동료 가운데 누구인지</p></li>
      <li><b>자료 붙이기</b><p>계획서 · 설문 · 회의록, 개인정보는 지우고</p></li>
      <li><b>모양 정하기</b><p>문단 · 표 · 목록과 분량</p></li>
      <li class="is-key"><b>초안 다시 읽기</b><p>사실과 숫자를 원문과 대조</p></li>
    </ol>
  </div>
  <span class="page-no"></span>
</section>
```

구성: **사례 · 한 건 이야기**

```html
<section data-pattern="steps" data-role="case" data-var="c" class="slide">
  <div class="s-body">
    <p class="kicker">03 따라 하기 · 한 학교의 사례</p>
    <h2 class="title">체험학습 안내문 한 장이 <em>40분에서 15분</em>이 됐습니다</h2>
    <div class="story fill">
      <div><span>상황</span><b>해마다 새로 쓰는 안내문</b><p>지난 문서를 찾아 고치는 데 40분이 걸렸습니다.</p></div>
      <div><span>한 일</span><b>세 걸음으로 요청</b><p>학부모에게, 올해 계획서로, 세 문단으로 써 달라고 했습니다.</p></div>
      <div class="is-key"><span>결과</span><b>15분 만에 발송</b><p>초안 5분, 날짜와 금액 대조 10분.</p></div>
    </div>
  </div>
  <p class="src">가상 예시</p>
  <span class="page-no"></span>
</section>
```

### 둘 비교 · `compare`

- 이런 내용일 때: 문제점 ↔ 개선 방안, 문단 ↔ 고른 장표, 기존안 ↔ 새 안
- 내용 조건: 2~3줄, 줄마다 왼쪽 · 오른쪽 한 짝. 넘치면: 4줄부터 두 장
- 부품: `.fix` (+ `.stack`) — 누를 때마다 한 줄씩 보이려면 data-step

구성: **비교 · 짝 줄**

```html
<section data-pattern="compare" data-role="compare" data-var="a" class="slide" data-steps="2">
  <div class="s-body">
    <p class="kicker">02 좋은 요청과 나쁜 요청</p>
    <h2 class="title">막연한 요청에 <em>대상과 모양</em>을 더하면 달라집니다</h2>
    <div class="fill stack">
      <div class="fix" data-step="1"><p class="q"><b>막연한 요청</b>안내문 써 줘</p><i aria-hidden="true"></i><p class="a"><b>분명한 요청</b>학부모에게 보낼 체험학습 안내문을 세 문단으로</p></div>
      <div class="fix is-key" data-step="2"><p class="q"><b>막연한 요청</b>이 자료 정리해 줘</p><i aria-hidden="true"></i><p class="a"><b>분명한 요청</b>첨부한 설문 결과를 학년별 표로, 눈에 띄는 점 세 줄</p></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

구성: **비교 · 기준별 두 열**

```html
<section data-pattern="compare" data-role="compare" data-var="c" class="slide">
  <div class="s-body">
    <p class="kicker">02 좋은 요청과 나쁜 요청</p>
    <h2 class="title">두 요청은 <em>세 가지 기준</em>에서 갈립니다</h2>
    <div class="vs fill">
      <b></b><h3>막연한 요청</h3><h3 class="is-key">분명한 요청</h3>
      <b>읽을 사람</b><p>적지 않음</p><p>학부모 · 학생 · 동료 중 하나</p>
      <b>근거 자료</b><p>없이 맡김</p><p>계획서 · 설문을 붙임</p>
      <b>결과 모양</b><p>정하지 않음</p><p>세 문단 · 표 · 목록으로 정함</p>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 전→후 · `before-after`

- 이런 내용일 때: 현행 → 개선, 사업 전 → 사업 후(숫자가 있는 짝)
- 내용 조건: 2~3짝, 같은 기준 · 같은 단위. 넘치면: 가장 큰 변화 3짝만
- 부품: `.ba` (+ `.ba-head`)

구성: **비교 · 전과 후 수치**

```html
<section data-pattern="before-after" data-role="compare" data-var="b" class="slide">
  <div class="s-body">
    <p class="kicker">02 좋은 요청과 나쁜 요청</p>
    <h2 class="title">요청을 분명히 쓰면 <em>다시 묻는 횟수</em>가 줄어듭니다</h2>
    <div class="fill stack">
      <p class="ba-head"><span>막연한 요청</span><span>분명한 요청</span></p>
      <div class="ba">
        <div><span>다시 요청한 횟수</span><p>문서 하나당</p><b>5<small>회</small></b></div><i aria-hidden="true"></i><div class="is-key"><span>다시 요청한 횟수</span><p>문서 하나당</p><b>2<small>회</small></b></div>
        <div><span>초안 작성 시간</span><p>문서 하나당</p><b>40<small>분</small></b></div><i aria-hidden="true"></i><div><span>초안 작성 시간</span><p>문서 하나당</p><b>15<small>분</small></b></div>
      </div>
    </div>
  </div>
  <p class="src">자료: ○○교육청 교육연수원 수료자 설문(가상 예시)</p>
  <span class="page-no"></span>
</section>
```

### 묶음·분류 · `groups`

- 이런 내용일 때: 과제 · 프로그램을 갈래로 나눈 것
- 내용 조건: 2~4묶음, 묶음마다 3줄 이하. 넘치면: 묶음마다 한 장
- 부품: `.card` + `.grid.g2/.g3/.g4`

구성: **핵심 개념 · 세 요소로 풀기**

```html
<section data-pattern="groups" data-role="concept" data-var="b" class="slide">
  <div class="s-body">
    <p class="kicker">01 개념 맞추기</p>
    <h2 class="title">프롬프트는 <em>세 가지</em>를 알려 주는 글입니다</h2>
    <div class="grid g3 fill center">
      <div class="card is-key"><span class="c-no">하나</span><h3>누구에게</h3><p>읽을 사람과<br>말투</p><p class="c-foot">예 <b>학부모께</b></p></div>
      <div class="card"><span class="c-no">둘</span><h3>무엇으로</h3><p>근거가 되는<br>자료</p><p class="c-foot">예 <b>계획서</b></p></div>
      <div class="card"><span class="c-no">셋</span><h3>어떤 모양으로</h3><p>분량과<br>형식</p><p class="c-foot">예 <b>세 문단</b></p></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 체계 · `tree`

- 이런 내용일 때: 비전 → 전략 → 과제, 추진 체계, 조직도
- 내용 조건: 맨 위 1 + 갈래 2~4 + 갈래마다 2~3줄. 넘치면: 갈래마다 한 장, 또는 표로
- 부품: `.tree` — 갈래 수는 style="--n:3"

```html
<section data-pattern="tree" class="slide">
  <div class="s-body">
    <p class="kicker">02 목표 · 추진 체계</p>
    <h2 class="title">세 전략 가운데 <em>찾아가는 교실</em>에 먼저 힘을 싣습니다</h2>
    <div class="tree fill" style="--n:3">
      <div class="t-top"><small>목표</small>어느 학교에서든 30분 안에 닿는 학교 밖 교실</div>
      <div class="t-mid is-key"><small>전략 1</small>찾아가는 교실</div>
      <div class="t-mid"><small>전략 2</small>함께 짜는 수업</div>
      <div class="t-mid"><small>전략 3</small>한 번에 하는 행정</div>
      <ul><li>예술 공간 버스 2대</li><li>군 지역 거점 6곳</li></ul>
      <ul><li>공동 설계 연수 연 4회</li><li>학년별 수업 모델</li></ul>
      <ul><li>이동 · 보험 일괄 계약</li><li>신청 서류 한 장으로</li></ul>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 큰 숫자 · `numbers`

- 이런 내용일 때: 핵심 실적 · 규모 · 예산 총액
- 내용 조건: 1~4개, 숫자마다 단위 + 한 줄. 넘치면: 가장 중요한 3개만
- 부품: `.tile` (+ `.delta`)

구성: **핵심 수치 · 숫자 셋**

```html
<section data-pattern="numbers" data-role="numbers" data-var="a" class="slide">
  <div class="s-body">
    <p class="kicker">05 정리 · 지난 연수 결과</p>
    <h2 class="title">초안 쓰는 시간이 <em>40분에서 15분</em>으로 줄었습니다</h2>
    <div class="grid g3 fill center">
      <div class="tile is-key"><span>초안 작성 시간</span><b>15<small>분</small></b><p>연수 전 평균 40분</p></div>
      <div class="tile"><span>다시 요청한 횟수</span><b>2<small>회</small></b><p>한 문서당 평균</p></div>
      <div class="tile"><span>업무에 계속 쓰겠다</span><b>92<small>%</small></b><p>수료자 설문</p></div>
    </div>
  </div>
  <p class="src">자료: ○○교육청 교육연수원 수료자 설문(가상 예시)</p>
  <span class="page-no"></span>
</section>
```

구성: **핵심 수치 · 숫자 하나 크게**

```html
<section data-pattern="numbers" data-role="numbers" data-var="b" class="slide">
  <div class="s-body">
    <p class="kicker">05 정리 · 지난 연수 결과</p>
    <div class="big fill">
      <b>15<small>분</small></b>
      <div><p>초안 한 건을 쓰는 데 걸린 시간</p><ul><li>연수 전 평균 40분</li><li>다시 요청한 횟수는 문서당 2회</li></ul></div>
    </div>
  </div>
  <p class="src">자료: ○○교육청 교육연수원 수료자 설문(가상 예시)</p>
  <span class="page-no"></span>
</section>
```

### 막대 비교 · `bars`

- 이런 내용일 때: 항목 간 크기 비교 · 순위 · 목표 대비 실적
- 내용 조건: 3~5줄, 한 가지 단위. 넘치면: 위 4개 + 나머지 합
- 부품: `.goal` + `.g-row` — 목표선이 없으면 .bars + .bar

구성: **핵심 수치 · 목표 대비 막대**

```html
<section data-pattern="bars" data-role="numbers" data-var="c" class="slide">
  <div class="s-body">
    <p class="kicker">05 정리 · 지난 연수 결과</p>
    <h2 class="title">네 지표 중 <em>계속 쓰겠다</em>는 응답만 목표에 못 미쳤습니다</h2>
    <div class="goal fill">
      <div class="g-row" style="--v:92.3;--t:76.9"><span>수료 인원</span><i></i><b>120%<small>144 / 120명</small></b></div>
      <div class="g-row" style="--v:84.6;--t:76.9"><span>실습 제출</span><i></i><b>110%<small>132 / 120건</small></b></div>
      <div class="g-row" style="--v:80.8;--t:76.9"><span>시간 단축</span><i></i><b>105%<small>25 / 24분</small></b></div>
      <div class="g-row is-key" style="--v:74.4;--t:76.9"><span>계속 쓰겠다</span><i></i><b>97%<small>92 / 95%</small></b></div>
      <p class="g-key"><span><i class="v"></i>달성률</span><span><i class="t"></i>목표(100%)</span></p>
    </div>
  </div>
  <p class="src">자료: ○○교육청 교육연수원 수료자 설문(가상 예시)</p>
  <span class="page-no"></span>
</section>
```

### 추이 · `trend`

- 이런 내용일 때: 여러 해 · 여러 달에 걸친 변화
- 내용 조건: 3~8시점, 한 가지 값. 넘치면: 시점을 줄인다
- 부품: `.trend` — 가장 큰 값 = --v:100

```html
<section data-pattern="trend" class="slide">
  <div class="s-body">
    <p class="kicker">독서 활동 소개 · 달라진 점</p>
    <h2 class="title">한 사람이 빌린 책이 3년 새 <em>두 배</em>가 됐습니다</h2>
    <div class="trend fill">
      <div style="--v:48"><b>11<small>권</small></b><i></i><span>2023</span></div>
      <div style="--v:61"><b>14<small>권</small></b><i></i><span>2024</span></div>
      <div style="--v:83"><b>19<small>권</small></b><i></i><span>2025</span></div>
      <div class="is-key" style="--v:100"><b>23<small>권</small></b><i></i><span>2026</span></div>
    </div>
  </div>
  <p class="src">자료: ○○초등학교 도서관 대출 기록, 학생 1인당 연간(가상 예시)</p>
  <span class="page-no"></span>
</section>
```

### 구성비 · `share`

- 이런 내용일 때: 전체 중 몫 · 재원 비율
- 내용 조건: 2~5조각, 합 100%. 넘치면: 작은 조각은 기타로
- 부품: `.share` + `.sh-bar` — 설문 다섯 단계 응답은 .likert

```html
<section data-pattern="share" class="slide">
  <div class="s-body">
    <p class="kicker">04 일정 · 예산</p>
    <h2 class="title">재원의 <em>45%</em>는 교육청 자체 예산으로 맡습니다</h2>
    <div class="share fill">
      <div class="sh-bar"><i class="is-key" style="--v:45"></i><i style="--v:30"></i><i style="--v:25"></i></div>
      <ul>
        <li class="is-key"><span>교육청 자체</span><b>45<small>%</small></b><p>5.4억 원 · 이동 지원 전액</p></li>
        <li><span>국고 보조</span><b>30<small>%</small></b><p>3.6억 원 · 수업 운영</p></li>
        <li><span>지자체 대응</span><b>25<small>%</small></b><p>3.0억 원 · 계약 · 보험</p></li>
      </ul>
    </div>
  </div>
  <p class="src">자료: ○○교육청 2027 예산안(가상 예시)</p>
  <span class="page-no"></span>
</section>
```

### 표 · `table`

- 이런 내용일 때: 표로 된 지원 내용 · 항목 목록 · 예산 내역
- 내용 조건: 3~5행 × 3~4열, 칸마다 1줄. 넘치면: 6행부터 두 장, 또는 핵심 열만
- 부품: `.tbl`

구성: **순서 · 절차 · 단계 표**

```html
<section data-pattern="table" data-role="steps" data-var="c" class="slide">
  <div class="s-body">
    <p class="kicker">03 따라 하기</p>
    <h2 class="title">단계마다 <em>할 일과 걸리는 시간</em>이 다릅니다</h2>
    <div class="fill stack">
      <table class="tbl">
        <thead><tr><th>단계</th><th>할 일</th><th>쓰는 것</th><th>시간</th></tr></thead>
        <tbody>
          <tr><td>1 누구에게</td><td>읽을 사람과 말투 적기</td><td>—</td><td class="n">1분</td></tr>
          <tr><td>2 무엇으로</td><td>근거 자료 붙이기</td><td>계획서 · 설문</td><td class="n">2분</td></tr>
          <tr><td>3 어떤 모양으로</td><td>분량과 형식 정하기</td><td>세 걸음 카드</td><td class="n">2분</td></tr>
          <tr class="is-key"><td>4 다시 읽기</td><td>사실 · 숫자 대조</td><td>원문</td><td class="n">10분</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 일정 · `timeline`

- 이런 내용일 때: 추진 일정 · 연혁 · 과정 지도
- 내용 조건: 이정표 3~5개(.mile) 또는 줄 3~5개 × 12달(.gantt). 넘치면: 분기 · 학기로 묶는다
- 부품: `.mile` — 달 단위 기간이 겹치면 .gantt

구성: **목차 · 전체 흐름 · 가로 이정표**

```html
<section data-pattern="timeline" data-role="flow" data-var="b" class="slide">
  <div class="s-body">
    <p class="kicker">오늘의 흐름</p>
    <h2 class="title">50분 가운데 <em>실습 20분</em>이 가장 깁니다</h2>
    <ol class="mile fill">
      <li><time>5분</time><b>개념 맞추기</b><p>프롬프트라는 말</p></li>
      <li><time>10분</time><b>좋은 요청과 나쁜 요청</b><p>두 요청 견주기</p></li>
      <li><time>10분</time><b>따라 하기</b><p>세 걸음으로 쓰기</p></li>
      <li class="is-key"><time>20분</time><b>실습</b><p>내 문서로 써 보기</p></li>
      <li><time>5분</time><b>정리</b><p>세 줄 요약</p></li>
    </ol>
  </div>
  <span class="page-no"></span>
</section>
```

### 사진+글 · `photo`

- 이런 내용일 때: 사례 · 현장 사진 · 활동 모습
- 내용 조건: 사진 1~3장, 사진마다 제목 + 한 줄 + 말 한마디. 넘치면: 사진마다 한 장
- 부품: `.case` + `.ph` — 사진은 사용자에게 받는다. 없으면 .ph data-need 로 자리만

```html
<section data-pattern="photo" class="slide">
  <div class="s-body">
    <p class="kicker">04 우수 사례</p>
    <h2 class="title">세 학교는 <em>교과 시간 안에서</em> 학교 밖 수업을 정례화했습니다</h2>
    <div class="case fill">
      <div><div class="ph" data-need="사진 자리 · 4:3 · 공방에서 도자기를 빚는 초등학생"></div><div class="c-body"><span>○○초 · 5학년 미술</span><b>공방에서 빚은 도자기로 학년 전시</b><blockquote>흙을 직접 만져 보니 교과서 사진이 달라 보였어요.<cite>5학년 학생</cite></blockquote></div></div>
      <div class="is-key"><div class="ph" data-need="사진 자리 · 4:3 · 극장 무대에서 낭독하는 중학생"></div><div class="c-body"><span>△△중 · 2학년 국어</span><b>극장 무대에서 낭독극 발표</b><blockquote>무대에 서 보니 글을 읽는 목소리가 달라졌어요.<cite>2학년 학생</cite></blockquote></div></div>
      <div><div class="ph" data-need="사진 자리 · 4:3 · 오케스트라와 함께 연주하는 초등학생"></div><div class="c-body"><span>□□초 · 4학년 음악</span><b>지역 오케스트라와 합동 연주</b><blockquote>아이들이 처음으로 진짜 악기 소리를 가까이에서 들었습니다.<cite>담당 교사</cite></blockquote></div></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 화면 짚기 · `screen`

- 이런 내용일 때: 프로그램 화면 · 서식 · 누리집 사용법
- 내용 조건: 캡처 1장 + 번호 표시 3개 이하. 넘치면: 동작 하나에 한 장
- 부품: `.shot` + `.shot-img` — 번호 자리는 style="--x:%;--y:%"

구성: **사례 · 화면 짚기**

```html
<section data-pattern="screen" data-role="case" data-var="a" class="slide">
  <div class="s-body">
    <p class="kicker">03 따라 하기 · 화면</p>
    <h2 class="title">대화창에서는 <em>세 곳</em>만 보면 됩니다</h2>
    <div class="shot fill">
      <div class="shot-img"><div class="ph"><img src="화면-캡처.png" alt="채팅 AI 대화창 예시 화면"></div><b style="--x:15;--y:88">1</b><b class="is-key" style="--x:42;--y:88">2</b><b style="--x:27;--y:61">3</b></div>
      <ol>
        <li><b>자료 붙이기</b><span>+ 단추로 문서를 첨부</span></li>
        <li class="is-key"><b>요청 쓰기</b><span>누구에게 · 무엇으로 · 어떤 모양</span></li>
        <li><b>다시 다듬기</b><span>더 짧게, 표로, 말투 바꾸기</span></li>
      </ol>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 질문 · `ask`

- 이런 내용일 때: 여는 질문 · 토의 주제 · 퀴즈 · 자주 묻는 질문
- 내용 조건: 질문 1개 + 보기 4개 이하(ol) 또는 답 1개(.a-a). 넘치면: 질문마다 한 장
- 부품: `.ask` — 퀴즈 답은 .a-a 에 data-step="1" 을 붙여 가렸다 연다. 이 장은 .title 없이

구성: **실습 · 질문과 보기**

```html
<section data-pattern="ask" data-role="practice" data-var="b" class="slide">
  <div class="s-body">
    <p class="kicker">04 실습</p>
    <div class="ask fill">
      <p class="a-q">이번 주에 쓸 문서 가운데 무엇으로 연습해 볼까요?</p>
      <ol>
        <li>가정통신문</li>
        <li>회의록 요약</li>
        <li>행사 계획서 초안</li>
        <li>설문 결과 정리</li>
      </ol>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

### 할 일 · `todo`

- 이런 내용일 때: 실습 안내 · 과제 · 제출 서류 · 신청 기한
- 내용 조건: 할 일 한 문장 + 조건 칸 2~3개(시간 · 결과물 · 도움). 넘치면: 할 일마다 한 장
- 부품: `.todo` — 이 장은 .title 없이

구성: **실습 · 할 일과 조건**

```html
<section data-pattern="todo" data-role="practice" data-var="a" class="slide">
  <div class="s-body">
    <p class="kicker">04 실습</p>
    <div class="todo fill">
      <p class="t-do">이번 주에 쓸 문서 <em>하나</em>를 골라<br>세 걸음으로 요청문을 써 봅니다</p>
      <dl>
        <div><dt>시간</dt><dd>20분<small>15분 혼자, 5분 옆 사람과</small></dd></div>
        <div><dt>결과물</dt><dd>요청문 + 받은 초안<small>실습지 1쪽에 붙입니다</small></dd></div>
        <div><dt>막히면</dt><dd>세 걸음 카드<small>책상 위에 있습니다</small></dd></div>
      </dl>
    </div>
  </div>
  <span class="page-no"></span>
</section>
```

구성: **실습 · 체크 목록**

```html
<section data-pattern="todo" data-role="practice" data-var="c" class="slide">
  <div class="s-body">
    <p class="kicker">04 실습 · 20분</p>
    <h2 class="title">요청문을 쓰면서 <em>네 가지</em>를 확인합니다</h2>
    <ul class="check fill">
      <li>읽을 사람과 말투를 적었다</li>
      <li>근거 자료를 붙였다<small>개인정보는 지우고</small></li>
      <li>분량과 형식을 정했다</li>
      <li class="is-key">받은 초안의 숫자를 원문과 대조했다<small>가장 중요</small></li>
    </ul>
  </div>
  <span class="page-no"></span>
</section>
```

## 9. 출력과 점검

- 결과는 **`.html` 파일 하나**(UTF-8)로 줍니다. 파일을 만들 수 있는 기능(아티팩트 · 캔버스 · 파일 첨부)이 있으면 그것으로, 없을 때만 HTML 전체를 코드 블록 하나로 출력합니다.
- `...`, "(생략)", "(이하 동일)"을 쓰지 않습니다. `<!DOCTYPE html>`부터 `</html>`까지 전부 씁니다.

내보내기 전에 하나씩 확인합니다.

1. 문서에 없고 확인도 받지 않은 숫자 · 사실이 없는가? 수치가 있는 장마다 `.src`가 있는가?
2. 장마다 기본 장표가 하나이고, 내용 조건(항목 수 · 줄 수)을 넘지 않는가?
3. 제목이 결론 한 문장이고 두 줄 이내인가? 강조(`<em>` · `.is-key`)가 장마다 한 곳인가?
4. 쓴 클래스가 모두 견본 코드(8) 또는 '추가 부품' 칸에 있는가? 인라인 style은 허용된 값뿐인가? 코드로 그린 그림이 없는가?
5. 공통 파일 두 줄이 그대로이고, 장 번호 · 쪽 표시를 손으로 쓰지 않았는가?
6. 견본의 예시 문구가 남아 있지 않은가? 생략 없이 끝까지 썼는가?
7. 사진 · 캡처 자리(`data-need`)가 있으면, 어떤 이미지가 필요한지 사용자에게 목록으로 알려 주었는가?

---

## 디자인 규칙 (`B` design.md)

````markdown
---
kit: B
name: 미니멀 스튜디오
version: v1
stage: 1920x1080
colors:
  bg: "#EEF1F4"        # 무대 바탕(밝은 청백 무광 벽)
  surface: "#FAFAF8"   # 카드 · 타일 · 표 면(흰 모형 재질)
  ink: "#1F2B36"       # 제목 · 본문 글자, 굵은 선
  sub: "#5E6974"       # 보조 글자 · 라벨 · 출처
  line: "#CDD4DB"      # 가는 구분선
  accent: "#E2571A"    # 주황 — 한 장에 한 곳만
  c1: "#2F4252"        # 카드 윗변 · 진한 본문
  c3: "#7389A0"        # 간트 막대
  c4: "#9DB0C1"        # 막대(보통 값)
fonts:
  title: "Gothic A1 800"          # 표지 96 · 간지 88 · 마무리 80 · 장 제목 56 · 카드 제목 44
  body: "IBM Plex Sans KR 400/600" # 본문 28 · 보조 22~26
  num: "IBM Plex Mono 500/600"    # 수치 88 · 막대 값 30 · 쪽 번호 22 (숫자 · 영문에만)
space:
  side: 120px      # 좌우 여백
  top: 88px
  bottom: 96px
  gap: 32px        # 격자 칸 사이
  block: 40px      # 머리말 → 제목 → 본문 사이
radius: 2px
shadow: "0 1px 0 rgba(31,43,54,.05), 0 18px 40px -22px rgba(31,43,54,.30)"
---

## 분위기
전시관 모형대, 촬영 스튜디오. 밝은 청백 무광 벽 앞에 흰 덩어리 하나가 놓여 있고, 조명이 그중 **한 곳만** 비춘다.
- 사물은 한 덩어리로 둔다. 여러 개의 작은 장식으로 흩지 않는다.
- 주황(`accent`)은 **한 장에 한 곳**: 제목의 핵심 낱말 하나(`<em>`) 또는 부품 하나(`.is-key`). 둘 다 쓰면 같은 내용을 가리켜야 한다.
- 바닥이 벽으로 휘는 곡면처럼, 장 아래 1/3이 조금 밝다(공통 CSS가 그림).
- 근거 장표: 표지 #19 · #26 · #28 · #37, 목차 · 간지 키트 #46 · #116.

## 색의 역할
| 이름 | 쓰는 곳 | 쓰지 않는 곳 |
|---|---|---|
| bg | 모든 장의 바탕 | 카드 면 |
| surface | 카드 · 수치 타일 · 막대 판 · 표 · 간트 판 | 바탕 |
| ink | 제목 · 본문 · 굵은 선(목차 위 선, 표 머리 아래 선, 화살표) | 넓은 면 채우기 |
| sub | 머리말 · 라벨 · 단위 · 출처 · 쪽 번호 | 결론 문장 |
| accent | 한 장에 한 곳(핵심 낱말, 핵심 수치, 핵심 막대 · 줄 · 카드, 지금 섹션) | 배경 · 장식 · 두 곳 이상 |
| c1 · c3 · c4 | 카드 윗변 · 간트 막대 · 보통 막대 | 글자 강조 |

새 색을 만들지 않는다. 빨강 · 초록으로 좋고 나쁨을 나타내지 않는다(이 계열에 의미 색은 없다. 강조는 주황 하나).

## 글자
- 제목은 Gothic A1 800, 본문은 IBM Plex Sans KR, 숫자는 IBM Plex Mono. 글꼴은 변수(`--ds-font-title` · `--ds-font-body` · `--ds-font-num`)로만 부른다.
- **한글에 고정폭 글꼴과 넓은 자간을 쓰지 않는다.** 고정폭 글꼴에는 한글이 없어 다른 글꼴로 바뀌고, 넓은 자간은 "현 황"처럼 낱자를 벌려 놓는다. 고정폭은 숫자 · 영문 라벨(`CONTENTS`, `SECTION`, `2025`, `04 / 08`)에만 쓴다.
- 자간은 0에서 -0.02em 사이. 영문 원본 템플릿의 "대문자 + 넓은 자간" 같은 장치는 한글에 옮기지 않는다.
- 줄바꿈은 낱말 단위(`word-break:keep-all`, 공통 CSS에 있음). 제목은 `text-wrap:balance`로 두 줄 길이를 맞춘다.
- 크기: 읽는 글 28px 이상, 보조 글(라벨 · 단위 · 출처) 22px 이상. 1920 무대가 통째로 줄어들기 때문에 이보다 작으면 회의실 화면에서 읽히지 않는다.

## 장의 짜임 (성과 공유회 · 설명회 본문)
모든 본문 장은 같은 순서다: **머리말(`.kicker`, 덱 속 자리) → 결론 한 문장 제목(`.title`) → 도식 1~2개 → 출처(`.src`, 수치가 있으면 반드시)**.
- 제목은 결론 문장이다. "핵심 성과"(×) → "참여 학교 138교, 연계 수업 1,240회가 열렸습니다"(○).
- 머리말은 덱 목차와 같은 말을 쓴다. 성과 공유회: 01 사업 개요 · 02 추진 경과 · 03 핵심 성과 · 04 우수 사례 · 05 시사점 · 향후 계획.
- 도식은 한 장에 1~2개. 막대 + 타일, 간트 + 표처럼 서로 다른 종류를 짝짓는다. 같은 모양 장이 연달아 나오지 않게 한다.

## 모형대 매스(.mass)
흰 층 덩어리. 이 계열의 얼굴이다.
- **표지 · 목차 · 간지에만** 쓴다. 본문 장에는 쓰지 않는다(본문의 주인공은 도식).
- 층 수 = 섹션 수(최대 5). 아래층이 1섹션이다. `.lit` 한 층이 **지금 섹션**(목차 · 간지) 또는 **핵심 섹션**(표지).
- 크기 · 위치는 부품 CSS 그대로. 층을 회전 · 기울이지 않는다.

## 깊이와 모양
- 그림자는 하나뿐(`--ds-shadow`). 카드는 테두리 대신 그림자로 띄운다. 그림자를 겹치거나 색을 넣지 않는다.
- 모서리 2px. 둥근 알약 · 큰 둥근 모서리는 쓰지 않는다(쪽 표시 도구 제외).
- 카드 윗변 3px 선(c1). 핵심 카드만 주황.

## 성과 공유회 부품(공용 parts.css)
사업 개요 `.brief` · 추진 경과 `.mile` · 증감 `.delta` · 목표 대비 달성 `.goal` · 만족도 `.likert` · 전후 비교 `.ba` · 우수 사례 `.case`(사진 `.ph` + 목소리) · 향후 계획 `.road`. 모양은 이 계열의 토큰을 따른다.
- **그림을 코드로 그리지 않는다.** 사물 · 인물 · 풍경 · 캐릭터가 필요하면 사용자에게 이미지를 요청하고, 사진은 `.ph` 자리에 넣는다(docs/criteria.md 4).

## 해야 할 것
1. 장마다 결론 한 문장 제목을 쓴다.
2. 수치에는 단위(`<small>`)와 출처(`.src`)를 붙인다.
3. 주황은 한 장에 한 곳.
4. 화면을 채운다. 큰 빈 곳이 남으면 글자 · 도식을 키우거나 장을 합친다.
5. 누르면 하나씩 보이는 장(`data-steps`)은 한 장에 하나, 3단계 이하.

## 하지 말 것
1. 새 색 · 그라데이션 · 그림 파일 만들기.
2. 한글에 고정폭 글꼴 · 넓은 자간.
3. 본문 장에 모형대 매스 넣기.
4. 장 번호 · 쪽 표시 · 점을 손으로 쓰기(엔진이 장 개수로 채운다. `.page-no`는 빈 칸으로 둔다).
5. 공통 CSS · 엔진을 HTML 안에 옮겨 쓰기, `@font-face` 새로 쓰기.
6. 인라인 `style`은 막대 값(`--v`) · 목표선(`--t`) · 간트 기간(`--from` · `--to`) 말고는 쓰지 않는다.
7. 사물 · 인물 · 풍경을 SVG · CSS로 그리기(이미지를 요청한다).

## 새 부품을 만들 때
1. 먼저 부품 사전의 배치(`.grid` · `.split` · `.stack`)로 될지 본다. 직접 만든 배치는 화면을 못 보고 쓰는 것이라 깨지기 쉽다.
2. 면은 `surface` + `--ds-shadow` + 모서리 2px. 테두리를 두르지 않는다.
3. 글자는 위 크기 규칙(읽는 글 28px · 보조 22px 이상)을 따른다.
4. 강조는 `.is-key` 한 곳, 색은 `accent`.
5. 이름은 짧은 영문 소문자(`.xxx`), 장 안 모든 값은 1920 × 1080 무대 기준 px.

## 알려진 한계 (v1)
- 막대는 가로뿐. 세로 막대 · 선 · 도넛 · 지도 부품은 아직 없다.
- 사진 다루는 규칙이 없다(이 계열 표지 장표들은 사진 없이 모형으로 만든다).
- 교육행정 아이콘 세트(`icons/icons.html`)는 아직 키트에 묶이지 않았다.
````

- 글꼴: 제목 Gothic A1(800) · 본문 IBM Plex Sans KR(400/600) · 숫자 IBM Plex Mono(500/600). 공통 CSS가 불러오므로 설치하지 않아도 됩니다.
- 글꼴은 변수로만 지정합니다: `var(--ds-font-title)` · `var(--ds-font-body)` · `var(--ds-font-num)`(숫자 · 영문에만).

---

## 부품 사전 (이 계열 CSS에 정의된 클래스 전부)

"예"는 예시 덱에서 그 클래스를 처음 쓴 태그입니다. 공용: `.slide`(장 하나) · `data-steps="n"`(장) + `data-step="k"`(안의 요소, 누를 때마다 하나씩) · `.page-no`(빈 칸, 엔진이 채움).

**공통: 머리말 · 결론 제목 · 쪽 번호 · 출처**
- `.s-body` — 예: `<div class="s-body">`
- `.kicker` — 예: `<p class="kicker">`
- `.title` — 예: `<h2 class="title">`
- `.lead`
- `.fill` — 예: `<dl class="define fill">`
- `.src` — 예: `<p class="src">`
- `.page-no` — 예: `<span class="page-no">`

**모형대 매스: 흰 덩어리 층. .lit 한 층만 주황(진행 · 강조 한 곳)**
- `.mass` — 예: `<div class="mass" aria-hidden="true">`
- `.lit` — 예: `<i class="lit">`

**표지**
- `.cover` — 예: `<section data-pattern="cover" data-role="cover" data-var="a" class="slide cover">`
- `.c-text` — 예: `<div class="c-text">`
- `.c-tag` — 예: `<span class="c-tag">`
- `.c-sub` — 예: `<p class="c-sub">`
- `.c-org` — 예: `<p class="c-org">`
- `.mass` — 예: `<div class="mass" aria-hidden="true">`

**목차: 줄 높이 112px, 지금 장 한 줄만 주황**
- `.toc-list` — 예: `<ol class="toc-list">`
- `.is-now` — 예: `<li class="is-now">`
- `.toc` — 예: `<section data-pattern="toc" data-role="flow" data-var="a" class="slide toc">`
- `.mass` — 예: `<div class="mass" aria-hidden="true">`

**간지: 큰 번호 + 섹션 이름, 매스의 그 층만 점등**
- `.divider` — 예: `<section data-pattern="divider" class="slide divider">`
- `.d-no` — 예: `<div class="d-no">`
- `.mass` — 예: `<div class="mass" aria-hidden="true">`

**마무리**
- `.close` — 예: `<section data-pattern="closing" data-role="closing" data-var="a" class="slide close">`
- `.spot` — 예: `<div class="spot" aria-hidden="true">`

**배치 격자**
- `.grid` — 예: `<div class="grid g3 fill center">`
- `.center` — 예: `<div class="grid g3 fill center">`
- `.g2`
- `.g3` — 예: `<div class="grid g3 fill center">`
- `.g4` — 예: `<div class="grid g4 fill center">`
- `.split`

**카드 묶음**
- `.card` — 예: `<div class="card is-key">`
- `.c-foot` — 예: `<p class="c-foot">`
- `.c-no` — 예: `<span class="c-no">`
- `.is-key` — 예: `<h3 class="is-key">`

**수치 타일**
- `.tile` — 예: `<div class="tile is-key">`
- `.is-key` — 예: `<h3 class="is-key">`

**막대(가로): style="--v:42" 는 최댓값 대비 %**
- `.bars`
- `.bar`
- `.is-key` — 예: `<h3 class="is-key">`

**현안 → 해결 표**
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.stack` — 예: `<div class="fill stack">`
- `.q` — 예: `<p class="q">`
- `.a` — 예: `<p class="a">`
- `.is-key` — 예: `<h3 class="is-key">`

**간트(월 1~12): style="--from:3;--to:6"**
- `.gantt` — 예: `<div class="gantt fill">`
- `.g-h` — 예: `<span class="g-h">`
- `.g-name` — 예: `<span class="g-name">`
- `.g-bar` — 예: `<span class="g-bar" style="--from:1;--to:3">`
- `.is-key` — 예: `<h3 class="is-key">`

**표**
- `.tbl` — 예: `<table class="tbl">`
- `.n` — 예: `<td class="n">`
- `.is-key` — 예: `<h3 class="is-key">`

**사업 개요: 목적 · 대상 · 기간 · 규모 네 칸**
- `.brief` — 예: `<div class="brief fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**추진 경과: 가로 시간선 위 이정표. 날짜는 <time>**
- `.mile` — 예: `<ol class="mile fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**증감 표시: 수치 타일 안 <span class="delta">▲ 38교</span> (줄면 .down)**
- `.delta` — 예: `<span class="delta">`
- `.down`

**목표 대비 달성: 실적 막대 + 목표선. style="--v:92;--t:80"(최댓값 대비 %)**
- `.goal` — 예: `<div class="goal fill">`
- `.g-row` — 예: `<div class="g-row" style="--v:88.5;--t:76.9">`
- `.is-key` — 예: `<h3 class="is-key">`
- `.g-key` — 예: `<p class="g-key">`
- `.v` — 예: `<i class="v">`
- `.t` — 예: `<i class="t">`

**만족도: 문항마다 다섯 단계 100% 막대. <i style="--v:%"> 다섯 개(매우 불만 → 매우 만족)**
- `.likert` — 예: `<div class="likert fill">`
- `.lk` — 예: `<div class="lk is-key">`
- `.is-key` — 예: `<h3 class="is-key">`
- `.lk-key` — 예: `<p class="lk-key">`

**전후 비교: 사업 전 → 사업 후, 짝마다 한 줄**
- `.ba` — 예: `<div class="ba">`
- `.is-key` — 예: `<h3 class="is-key">`
- `.ba-head` — 예: `<p class="ba-head">`

**우수 사례: 사진 자리 + 학교 · 한 줄 성과 + 참여자 목소리**
- `.case` — 예: `<div class="case fill">`
- `.ph` — 예: `<div class="ph">`
- `.c-body` — 예: `<div class="c-body">`
- `.is-key` — 예: `<h3 class="is-key">`

**향후 계획: 단계 머리(화살 띠) + 단계별 할 일**
- `.road` — 예: `<div class="road fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**한 문장: 장 가운데 큰 문장 하나 + 받치는 말 한 줄(.title 없이 .kicker 아래에)**
- `.say` — 예: `<div class="say fill">`

**항목: 번호 + 이름 + 설명. 3~5줄(5줄이면 설명은 한 줄)**
- `.points` — 예: `<ol class="points fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**용어 정의: 왼쪽 용어, 오른쪽 뜻 한 문장 + 예 한두 개**
- `.define` — 예: `<dl class="define fill">`

**인용: 말 1~3개. 말한 사람은 figcaption**
- `.quote` — 예: `<div class="quote fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**체계: 맨 위 하나(.t-top) → 가운데 갈래(.t-mid) → 갈래마다 할 일 목록(ul). 갈래 수는 style="--n:3"**
- `.tree` — 예: `<div class="tree fill" style="--n:3">`
- `.t-top` — 예: `<div class="t-top">`
- `.t-mid` — 예: `<div class="t-mid is-key">`
- `.is-key` — 예: `<h3 class="is-key">`

**추이: 시점마다 세로 막대. style="--v:62"(가장 큰 값 = 100). 3~8시점**
- `.trend` — 예: `<div class="trend fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**구성비: 100% 막대 하나(.sh-bar, <i style="--v:%"> 합 100) + 조각 설명(ul, 같은 순서)**
- `.share` — 예: `<div class="share fill">`
- `.sh-bar` — 예: `<div class="sh-bar">`
- `.is-key` — 예: `<h3 class="is-key">`

**화면 짚기: 화면 캡처 자리(.shot-img 안 .ph) + 번호 표시(<b style="--x:%;--y:%">) + 번호별 설명(ol)**
- `.shot` — 예: `<div class="shot fill">`
- `.shot-img` — 예: `<div class="shot-img">`
- `.ph` — 예: `<div class="ph">`
- `.is-key` — 예: `<h3 class="is-key">`

**질문: 큰 질문(.a-q) + 보기(ol, 4개까지) 또는 답(.a-a). 답은 data-step 으로 가렸다 연다**
- `.ask` — 예: `<div class="ask fill">`
- `.a-q` — 예: `<p class="a-q">`
- `.a-a`

**할 일: 지금 할 일 한 문장(.t-do) + 시간 · 결과물 · 도움 받을 곳 같은 조건 칸(dl)**
- `.todo` — 예: `<div class="todo fill">`
- `.t-do` — 예: `<p class="t-do">`

**흐름 · 번호 카드: 단계마다 큰 번호 + 이름 + 한 줄(시간 · 쪽). 3~5칸, 지금 칸은 .is-key**
- `.agenda` — 예: `<ol class="agenda fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**개념 · 맞는 예와 아닌 예: 위에 낱말(.yn-term), 아래 두 칸(.yn-yes · .yn-no)**
- `.yesno` — 예: `<div class="yesno fill">`
- `.yn-term` — 예: `<p class="yn-term">`
- `.yn-yes` — 예: `<div class="yn-yes">`
- `.yn-no` — 예: `<div class="yn-no">`

**비교 · 기준별 두 열: 줄마다 기준 | 왼쪽 | 오른쪽. 고른 쪽 머리에 .is-key**
- `.vs` — 예: `<div class="vs fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**절차 · 세로 단계: 번호 동그라미를 세로선으로 잇고, 단계마다 이름 + 한 줄. 3~5단계**
- `.stepper` — 예: `<ol class="stepper fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**사례 · 한 건 이야기: 상황 → 한 일 → 결과 세 칸. 결과 칸에 .is-key**
- `.story` — 예: `<div class="story fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**실습 · 체크 목록: 할 일을 네모 칸 목록으로. 3~5줄, 가장 중요한 줄에 .is-key**
- `.check` — 예: `<ul class="check fill">`
- `.is-key` — 예: `<h3 class="is-key">`

**수치 · 숫자 하나 크게: 왼쪽 큰 숫자 하나, 오른쪽에 뜻 한 문장 + 받치는 두 줄**
- `.big` — 예: `<div class="big fill">`

---

## 참고: 엔진 사용법

```text
덱 키트 공용 엔진 v1 — 모든 계열이 같이 쓴다. 덱 HTML은 <section class="slide"> 만 쓰면 된다.
   - 1920 × 1080 무대를 창에 맞게 통째로 줄임(글자가 다시 흘러내리지 않음)
   - → · Space · PageDown · Enter = 다음, ← · PageUp = 이전, Home · End, F = 전체 화면, 화면 누르기 · 밀기
   - 장 수 · 점 · 쪽 표시(.page-no)는 장 개수로 자동(손으로 맞추지 않음), 주소 #3 = 3장
   - data-steps="n" 장: 안의 [data-step="1"…"n"] 를 누를 때마다 하나씩 보임
   - window.DECK = { go(장, 단계), next(), prev(), index, count }
```

부품 모양 · 크기가 궁금하면 `https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/B.css`를 봅니다(HTML에 옮겨 쓰지 마세요).
