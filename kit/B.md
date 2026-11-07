# B 미니멀 스튜디오 — 계획안 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **ChatGPT · Claude · Gemini 같은 채팅 AI**에게 통째로 주면, 이 디자인으로 계획안 발표 덱을 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 B 계열 장표(#19 · #26 · #28 · #37 · #46 · #116)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일을 첨부**합니다(안 되면 내용을 끝까지 복사해 붙여 넣기).
2. 만들 계획안을 말합니다. 예) "2027 ○○ 지원 계획(안), ○○교육청 ○○과. 현황 수치는 아래 표(출처: ○○ 통계), 세부과제 3개는 … 덱으로 만들어 줘. 결과는 .html 파일로."
3. AI가 먼저 **장별 구성안**(머리말 · 결론 제목 · 부품 · 수치와 출처)을 보여 줍니다. 고칠 곳을 말하거나 "좋아, 만들어 줘".
4. 받은 `슬라이드.html`을 내려받아 더블클릭합니다. → · Space로 넘기고, F는 전체 화면, 인쇄하면 장마다 한 쪽(16:9) PDF가 됩니다.
5. 고칠 곳은 "3장 제목을 ○○로"처럼 말합니다. 코드가 끊기면 "끊긴 곳부터 이어서".

알아 둘 점
- 열 때 **인터넷이 필요**합니다(공통 CSS · 엔진 · 글꼴을 `szxv7704-dot.github.io`에서 불러옴). 업무망처럼 인터넷이 막힌 곳에서 발표하려면 저장소에서 `python3 scripts/kit.py inline B 슬라이드.html`을 실행해 모든 것이 파일 안에 든 판을 만드세요.
- AI 화면 안의 미리보기에서는 색 · 모양이 안 나올 수 있습니다. 내려받아 브라우저(크롬 · 엣지)로 열면 정상입니다.
- 수치는 AI가 지어내지 않도록 계약에 적어 두었지만, **받은 덱의 숫자를 원자료와 꼭 대조**하세요.
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

당신은 계획안 발표 덱 제작 도우미입니다. 사용자가 준 계획안 내용으로, 아래 **디자인 규칙(1)** · **부품 사전(3)** · **HTML 뼈대(4)**를 지켜 **브라우저에서 바로 열리는 덱 HTML 파일 하나**를 만듭니다.
공통 CSS(글꼴 · 색 · 부품 모양)와 동작 엔진은 뼈대의 `<link>` · `<script src>` 두 줄이 불러옵니다. **당신이 쓰는 것은 `<section class="slide">`들과, 꼭 필요할 때만 '추가 부품' CSS뿐입니다.**

### 진행 순서
1. 사용자가 아직 말하지 않았다면 짧게 묻습니다: 계획안 이름 · 기관(부서) · 날짜, 섹션별 핵심 내용, **쓸 수치와 그 출처**, 원하는 장 수(없으면 내용에 맞게).
2. **장별 구성안을 먼저 보여 주고 확인을 받습니다.** 장마다 `머리말 | 결론 한 문장 제목 | 쓸 부품 | 쓸 수치(출처)`를 한 줄로. 이때 코드를 쓰지 않습니다. 사용자가 "구성 확인 없이 바로"라고 했으면 건너뜁니다.
3. 확인을 받으면 HTML을 만들고, 아래 '내보내기 전 점검'을 하나씩 확인한 뒤 내보냅니다.

### 반드시 지킬 것
1. **숫자 · 연도 · 예산 · 순위 · 출처를 지어내지 않습니다.** 사용자가 준 것만 씁니다. 모르면 묻거나 "(예시)"를 붙입니다. 사용자가 주지 않은 사실을 넣고 싶으면 구성안에 '추가 사실'로 따로 적어 확인을 받습니다.
2. **장 제목은 결론 한 문장**(`.title`)입니다. "현황" 같은 이름표는 머리말(`.kicker`)에 씁니다.
3. 수치가 있는 장에는 출처(`.src`)를 씁니다.
4. **주황 강조는 한 장에 한 곳**: 제목의 `<em>` 하나 또는 부품의 `.is-key` 하나.
5. 디자인 규칙(1)의 '하지 말 것'을 어기지 않습니다. 규칙에 없는 색 · 장식 · 애니메이션을 더하지 않습니다.
6. **클래스는 부품 사전(3)에 있는 것만** 씁니다. 없는 클래스는 아무 모양도 없어 배치가 무너집니다. 새 부품이 꼭 필요하면 `<style>`의 '추가 부품' 줄 아래에 정의합니다(토큰 변수만).
7. 뼈대의 공통 파일 두 줄(`<link>` · `<script src>`)은 주소 한 글자도 바꾸지 않습니다. 공통 CSS · 엔진을 HTML 안에 옮겨 쓰거나 `@font-face`를 새로 쓰지 않습니다.
8. **장 번호 · 쪽 표시 · 점은 쓰지 않습니다.** 엔진이 장 개수로 채웁니다(`<span class="page-no"></span>`는 빈 칸 그대로).
9. 글자 크기와 화면 채우기(무대는 1920 × 1080, 화면에 맞게 통째로 줄어듦)
   - 읽는 글 28px 이상, 보조 글 22px 이상(부품 CSS가 이미 지킴 — 크기를 줄이지 마세요).
   - **높이 예산**: 머리말과 두 줄 제목 아래 본문에 쓸 수 있는 높이는 약 **600~680px**. 넘친 부분은 잘려 보이지 않습니다.
   - 카드 · 타일을 4개 이상 놓으면 칸마다 글 **3줄 이하**. 글 칸 너비는 400px 이상.
   - 제목은 **두 줄 이내**, 표지 제목은 한 줄에 13자 안팎. 넘치면 글자를 줄이지 말고 문장을 줄입니다.
   - 내용이 적은 장은 장을 합치거나 부품을 키워 큰 빈 곳을 남기지 않습니다.
10. 인라인 `style`은 막대 값(`style="--v:42"`, 가장 큰 값 = 100) · 간트 기간(`style="--from:3;--to:6"`, 1~12월)에만 씁니다.
11. 그림 파일을 만들지 않습니다. 필요한 그림은 HTML 안에서 SVG로 그리되 색은 토큰만 씁니다.

### 구성은 내용이 정합니다
- 뼈대(4)의 8장은 **부품 견본**입니다. 장 순서 · 장 수 · 문장을 따라 하지 마세요. 예시 문구는 하나도 남기지 않습니다.
- 계획안의 흐름(현황 → 목표 및 지표 → 세부과제 → 추진체계 → 일정 및 예산)을 따르되, 내용이 없는 섹션은 빼고 목차도 그에 맞춥니다.
- 표지 · 목차 · 간지 · 마무리는 모형대 매스(`.mass`)를 씁니다. 목차 · 간지의 `.lit` 층 = 지금 섹션(아래층이 1섹션).
- 같은 모양의 장이 연달아 나오지 않게 합니다. 누를 때마다 하나씩 보이는 장(`data-steps`)은 덱 전체에서 1~2장.

### 출력 방식
- 결과는 **`.html` 파일 하나**(UTF-8)로 줍니다. 파일을 만들 수 있는 기능(아티팩트 · 캔버스 · 파일 첨부)이 있으면 반드시 그것으로 줍니다. 없을 때만 완성된 HTML 전체를 ```html 코드 블록 하나로 출력합니다.
- `...`, "(생략)", "(이하 동일)"을 쓰지 않습니다. `<!DOCTYPE html>`부터 `</html>`까지 전부 씁니다. 끊기면 사용자가 "이어서"라고 할 때 끊긴 글자 바로 다음부터 씁니다.
- **미리보기 창에서 색 · 모양이 안 보여도 고치지 마세요.** 공통 CSS · 엔진을 인터넷에서 불러오는데, 일부 미리보기는 바깥 파일을 막습니다. 내려받아 브라우저로 열면 정상입니다.

### 내보내기 전 점검 (하나라도 아니면 고친 뒤 내보내기)
1. 사용자가 주지 않았고 확인도 받지 않은 수치 · 사실이 없는가? 수치가 있는 장마다 `.src`가 있는가?
2. 모든 본문 장의 제목이 결론 한 문장이고, 두 줄 이내인가?
3. 주황 강조(`<em>` · `.is-key`)가 장마다 한 곳 이하인가?
4. 쓴 클래스가 모두 부품 사전(3) 또는 '추가 부품' 칸에 있는가? 인라인 style은 `--v` · `--from` · `--to`뿐인가?
5. 공통 파일 두 줄이 그대로이고, 장 번호 · 쪽 표시 · 점을 손으로 쓰지 않았는가?
6. 모든 장이 1920 × 1080 안에 들어가는가(높이 예산 · 카드 규칙)? 큰 빈 곳이 없는가?
7. 뼈대의 예시 문구가 남아 있지 않은가? 생략 없이 끝까지 썼는가?

---

## 1. 디자인 규칙 (`B` design.md)

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

## 장의 짜임 (계획안 본문)
모든 본문 장은 같은 순서다: **머리말(`.kicker`, 계획안 속 위치) → 결론 한 문장 제목(`.title`) → 도식 1~2개 → 출처(`.src`, 수치가 있으면 반드시)**.
- 제목은 이름표가 아니라 **결론 문장**이다. "현황"(×) → "참여 학교는 늘었지만, 지역 공간과 잇는 학교는 3곳 중 1곳뿐입니다"(○).
- 머리말은 계획안 목차와 같은 말을 쓴다: Ⅰ. 현황 · Ⅱ. 목표 및 지표 · Ⅲ. 세부과제 · Ⅳ. 추진체계 · Ⅴ. 일정 및 예산.
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
6. 인라인 `style`은 막대 값(`--v`) · 간트 기간(`--from` · `--to`) 말고는 쓰지 않는다.

## 새 부품을 만들 때
1. 먼저 부품 사전의 배치(`.grid` · `.split` · `.stack`)로 될지 본다. 직접 만든 배치는 화면을 못 보고 쓰는 것이라 깨지기 쉽다.
2. 면은 `surface` + `--ds-shadow` + 모서리 2px. 테두리를 두르지 않는다.
3. 글자는 위 크기 규칙(읽는 글 28px · 보조 22px 이상)을 따른다.
4. 강조는 `.is-key` 한 곳, 색은 `accent`.
5. 이름은 짧은 영문 소문자(`.xxx`), 장 안 모든 값은 1920 × 1080 무대 기준 px.

## 알려진 한계 (v1)
- 막대는 가로뿐. 세로 막대 · 선 · 도넛 · 지도 부품은 아직 없다. 필요하면 SVG로 그리되 색은 c4 · accent만.
- 사진 다루는 규칙이 없다(이 계열 표지 장표들은 사진 없이 모형으로 만든다).
- 교육행정 아이콘 세트(`icons/icons.html`)는 아직 키트에 묶이지 않았다.
- PPT · 한글로 옮기는 자동 경로는 없다. 인쇄(PDF, 장당 1쪽 16:9)로 내보낸 뒤 그림으로 붙이는 것이 지금의 방법이다.
````

---

## 2. 글씨체

- 제목 Gothic A1(800) · 본문 IBM Plex Sans KR(400/600) · 숫자 IBM Plex Mono(500/600). 공통 CSS가 불러오므로 설치하지 않아도 됩니다(열 때 인터넷 필요).
- 글꼴은 변수로만 지정합니다: `var(--ds-font-title)` · `var(--ds-font-body)` · `var(--ds-font-num)`(숫자 · 영문에만).

---

## 3. 부품 사전 (이 계열 CSS에 정의된 클래스)

이 목록에 있는 클래스만 씁니다. "예"는 뼈대(4)에서 그 클래스를 처음 쓴 태그입니다. 공용 클래스: `.slide`(장 하나) · `data-steps="n"`(장) + `data-step="k"`(안의 요소, 누를 때마다 하나씩) · `.page-no`(빈 칸, 엔진이 채움).

**공통: 머리말 · 결론 제목 · 쪽 번호 · 출처**
- `.s-body` — 예: `<div class="s-body">`
- `.kicker` — 예: `<p class="kicker">`
- `.title` — 예: `<h2 class="title">`
- `.lead`
- `.fill` — 예: `<div class="split fill">`
- `.src` — 예: `<p class="src">`
- `.page-no` — 예: `<span class="page-no">`

**모형대 매스: 흰 덩어리 층. .lit 한 층만 주황(진행 · 강조 한 곳)**
- `.mass` — 예: `<div class="mass" aria-hidden="true">`
- `.lit` — 예: `<i class="lit">`

**표지**
- `.cover` — 예: `<section class="slide cover">`
- `.c-text` — 예: `<div class="c-text">`
- `.c-tag` — 예: `<span class="c-tag">`
- `.c-sub` — 예: `<p class="c-sub">`
- `.c-org` — 예: `<p class="c-org">`
- `.mass` — 예: `<div class="mass" aria-hidden="true">`

**목차: 줄 높이 112px, 지금 장 한 줄만 주황**
- `.toc-list` — 예: `<ol class="toc-list">`
- `.is-now` — 예: `<li class="is-now">`
- `.toc` — 예: `<section class="slide toc">`
- `.mass` — 예: `<div class="mass" aria-hidden="true">`

**간지: 큰 번호 + 섹션 이름, 매스의 그 층만 점등**
- `.divider` — 예: `<section class="slide divider">`
- `.d-no` — 예: `<div class="d-no">`
- `.mass` — 예: `<div class="mass" aria-hidden="true">`

**마무리**
- `.close` — 예: `<section class="slide close">`
- `.spot` — 예: `<div class="spot" aria-hidden="true">`

**배치 격자**
- `.grid` — 예: `<div class="grid g2">`
- `.center` — 예: `<div class="grid g3 fill center">`
- `.g2` — 예: `<div class="grid g2">`
- `.g3` — 예: `<div class="grid g3 fill center">`
- `.g4`
- `.split` — 예: `<div class="split fill">`

**카드 묶음**
- `.card` — 예: `<div class="card">`
- `.c-foot` — 예: `<p class="c-foot">`
- `.c-no` — 예: `<span class="c-no">`
- `.is-key` — 예: `<div class="tile is-key">`

**수치 타일**
- `.tile` — 예: `<div class="tile">`
- `.is-key` — 예: `<div class="tile is-key">`

**막대(가로): style="--v:42" 는 최댓값 대비 %**
- `.bars` — 예: `<div class="bars">`
- `.bar` — 예: `<div class="bar" style="--v:69">`
- `.is-key` — 예: `<div class="tile is-key">`

**현안 → 해결 표**
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.stack` — 예: `<div class="fill stack">`
- `.q` — 예: `<p class="q">`
- `.a` — 예: `<p class="a">`
- `.is-key` — 예: `<div class="tile is-key">`

**간트(월 1~12): style="--from:3;--to:6"**
- `.gantt` — 예: `<div class="gantt">`
- `.g-h` — 예: `<span class="g-h">`
- `.g-name` — 예: `<span class="g-name">`
- `.g-bar` — 예: `<i class="g-bar" style="--from:1;--to:3">`
- `.is-key` — 예: `<div class="tile is-key">`

**표**
- `.tbl` — 예: `<table class="tbl">`
- `.n` — 예: `<td class="n">`
- `.is-key` — 예: `<div class="tile is-key">`

---

## 4. HTML 뼈대 (예시 덱 8장 — 부품 견본입니다. 장 구성은 따라 하지 말고, 공통 파일 두 줄은 그대로 두며, 장은 내용에 맞게 새로)

```html
<!DOCTYPE html>
<html lang="ko" data-kit="B">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>덱 키트 B · 미니멀 스튜디오 — 예시 덱</title>
<!-- 이 계열의 공통 CSS(글꼴 · 색 · 부품). 이 줄은 지우거나 바꾸지 마세요 -->
<link rel="stylesheet" href="https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/B.css">
<style>
/* === 추가 부품: 새 클래스가 꼭 필요할 때만 이 줄 아래에(토큰 변수만 사용) === */
</style>
</head>
<body>
<div class="deck"><main class="deck-stage">

<!-- 1. 표지 -->
<section class="slide cover">
  <div class="c-text">
    <span class="c-tag">2027 · 가상 예시</span>
    <h1>학교 문화예술교육<br><em>지역 연계</em> 지원 계획(안)</h1>
    <p class="c-sub">학교 안 수업을 지역 예술 공간과 잇는 3년 계획</p>
  </div>
  <div class="mass" aria-hidden="true"><i></i><i></i><i class="lit"></i><i></i><i></i></div>
  <p class="c-org"><span>○○교육청 교육과정과</span><span>2026. 12.</span></p>
</section>

<!-- 2. 목차 -->
<section class="slide toc">
  <div class="s-body">
    <p class="kicker">CONTENTS</p>
    <h2 class="title">차례</h2>
    <ol class="toc-list">
      <li class="is-now"><b>01</b><span>현황</span><span>03</span></li>
      <li><b>02</b><span>목표 및 지표</span><span>—</span></li>
      <li><b>03</b><span>세부과제</span><span>05</span></li>
      <li><b>04</b><span>추진체계</span><span>06</span></li>
      <li><b>05</b><span>일정 및 예산</span><span>07</span></li>
    </ol>
  </div>
  <div class="mass" aria-hidden="true"><i class="lit"></i><i></i><i></i><i></i><i></i></div>
  <span class="page-no"></span>
</section>

<!-- 3. 간지 -->
<section class="slide divider">
  <div class="d-no"><small>SECTION</small>01</div>
  <h2>현황</h2>
  <p>참여는 늘었지만 학교 밖과 이어지는 수업은 아직 적습니다.</p>
  <div class="mass" aria-hidden="true"><i class="lit"></i><i></i><i></i><i></i><i></i></div>
  <span class="page-no"></span>
</section>

<!-- 4. 본문 · 현황: 수치 타일 + 막대 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">Ⅰ. 현황</p>
    <h2 class="title">참여 학교는 늘었지만, 지역 공간과 잇는 학교는 <em>3곳 중 1곳</em>뿐입니다</h2>
    <div class="split fill">
      <div class="grid g2">
        <div class="tile"><span>참여 학교</span><b>214<small>교</small></b><p>2024년보다 38교 늘어남</p></div>
        <div class="tile is-key"><span>지역 공간 연계</span><b>33<small>%</small></b><p>214교 중 71교</p></div>
        <div class="tile"><span>연계 예술 공간</span><b>46<small>곳</small></b><p>공연장 · 전시관 · 공방</p></div>
        <div class="tile"><span>학생 만족도</span><b>4.2<small>/ 5</small></b><p>연계 수업 참여 학생</p></div>
      </div>
      <div class="bars">
        <h3>연도별 참여 학교(교)</h3>
        <div class="bar" style="--v:69"><span>2023</span><b>148</b></div>
        <div class="bar" style="--v:82"><span>2024</span><b>176</b></div>
        <div class="bar is-key" style="--v:100"><span>2025</span><b>214</b></div>
      </div>
    </div>
  </div>
  <p class="src">자료: ○○교육청 내부 집계(가상 예시 수치)</p>
  <span class="page-no"></span>
</section>

<!-- 5. 본문 · 세부과제: 현안 → 해결 (누를 때마다 한 줄씩) -->
<section class="slide" data-steps="3">
  <div class="s-body">
    <p class="kicker">Ⅲ. 세부과제</p>
    <h2 class="title">막힌 곳 세 군데를 풀어 <em>학교 밖 수업</em>을 기본값으로 만듭니다</h2>
    <div class="fill stack">
      <div class="fix" data-step="1"><p class="q"><b>현안 1</b>예술 공간 정보가 흩어져 학교가 직접 찾아야 함</p><i aria-hidden="true"></i><p class="a"><b>해결 1</b>지역 예술 공간 지도와 예약 창구를 한곳으로</p></div>
      <div class="fix is-key" data-step="2"><p class="q"><b>현안 2</b>이동 · 안전 부담으로 교외 수업을 꺼림</p><i aria-hidden="true"></i><p class="a"><b>해결 2</b>버스 · 보험 · 인솔 보조를 교육청이 묶어서 지원</p></div>
      <div class="fix" data-step="3"><p class="q"><b>현안 3</b>예술가와 교사가 수업을 함께 설계할 시간이 없음</p><i aria-hidden="true"></i><p class="a"><b>해결 3</b>학기 초 공동 설계 연수(6시간)를 연수 시간으로 인정</p></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>

<!-- 6. 본문 · 추진체계: 카드 묶음 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">Ⅳ. 추진체계</p>
    <h2 class="title">교육청이 잇고, 지원청이 묶고, 학교는 <em>수업만</em> 맡습니다</h2>
    <div class="grid g3 fill center">
      <div class="card"><span class="c-no">01 · 교육청</span><h3>잇기</h3><p>예술 공간 협약, 예산 배분, 공동 설계 연수 운영</p><p class="c-foot">협약 공간 <b>46</b>곳</p></div>
      <div class="card"><span class="c-no">02 · 교육지원청</span><h3>묶기</h3><p>권역별 이동 · 안전 지원, 학교와 공간 짝 맺기</p><p class="c-foot">권역 <b>6</b>곳</p></div>
      <div class="card is-key"><span class="c-no">03 · 학교</span><h3>수업하기</h3><p>교육과정에 연계 수업을 넣고 결과를 나눔</p><p class="c-foot">목표 학교 <b>120</b>교</p></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>

<!-- 7. 본문 · 일정 및 예산: 간트 + 표 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">Ⅴ. 일정 및 예산</p>
    <h2 class="title">상반기에 판을 깔고, 2학기에 <em>연계 수업</em>을 엽니다</h2>
    <div class="split fill">
      <div class="gantt">
        <span class="g-h">과제</span><span class="g-h">1</span><span class="g-h">2</span><span class="g-h">3</span><span class="g-h">4</span><span class="g-h">5</span><span class="g-h">6</span><span class="g-h">7</span><span class="g-h">8</span><span class="g-h">9</span><span class="g-h">10</span><span class="g-h">11</span><span class="g-h">12</span>
        <span class="g-name">공간 협약</span><i class="g-bar" style="--from:1;--to:3"></i>
        <span class="g-name">공동 설계 연수</span><i class="g-bar" style="--from:3;--to:4"></i>
        <span class="g-name">이동 · 안전 지원</span><i class="g-bar" style="--from:3;--to:12"></i>
        <span class="g-name">연계 수업</span><i class="g-bar is-key" style="--from:9;--to:12"></i>
        <span class="g-name">결과 나눔</span><i class="g-bar" style="--from:12;--to:12"></i>
      </div>
      <table class="tbl">
        <thead><tr><th>항목</th><th style="text-align:right">백만 원</th></tr></thead>
        <tbody>
          <tr><td>공간 협약 · 운영</td><td class="n">320</td></tr>
          <tr class="is-key"><td>이동 · 안전 지원</td><td class="n">540</td></tr>
          <tr><td>공동 설계 연수</td><td class="n">90</td></tr>
        </tbody>
        <tfoot><tr><td>합계</td><td class="n">950</td></tr></tfoot>
      </table>
    </div>
  </div>
  <p class="src">예산은 가상 예시</p>
  <span class="page-no"></span>
</section>

<!-- 8. 마무리 -->
<section class="slide close">
  <h2>학교 밖도<br>교실입니다</h2>
  <p>문의 · ○○교육청 교육과정과 문화예술교육 담당</p>
  <div class="spot" aria-hidden="true"></div>
  <span class="page-no"></span>
</section>

</main></div>
<!-- 동작 엔진. 이 줄은 지우거나 바꾸지 마세요 -->
<script src="https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/deck.js"></script>
</body>
</html>
```

---

## 5. 참고: 엔진 사용법과 계열 CSS (뼈대가 이미 불러옴 — HTML에 옮겨 쓰지 마세요)

```text
덱 키트 공용 엔진 v1 — 모든 계열이 같이 쓴다. 덱 HTML은 <section class="slide"> 만 쓰면 된다.
   - 1920 × 1080 무대를 창에 맞게 통째로 줄임(글자가 다시 흘러내리지 않음)
   - → · Space · PageDown · Enter = 다음, ← · PageUp = 이전, Home · End, F = 전체 화면, 화면 누르기 · 밀기
   - 장 수 · 점 · 쪽 표시(.page-no)는 장 개수로 자동(손으로 맞추지 않음), 주소 #3 = 3장
   - data-steps="n" 장: 안의 [data-step="1"…"n"] 를 누를 때마다 하나씩 보임
   - window.DECK = { go(장, 단계), next(), prev(), index, count }
```

부품 모양 · 크기를 이해하는 데만 쓰세요(`https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/B.css`의 계열 부분).

```css
/* B 미니멀 스튜디오 — 덱 키트 v1 (deck.css 다음에 불러옴)
   전시관 모형대 · 촬영 스튜디오처럼 밝은 청백 무광. 사물은 한 덩어리, 주황은 한 장에 한 곳.
   근거 장표: #19 · #26 · #28 · #37(표지), #46 · #116(목차·간지 키트) */
:root{
  --ds-stage:#D9DEE3;
  --ds-bg:#EEF1F4; --ds-surface:#FAFAF8; --ds-ink:#1F2B36; --ds-sub:#5E6974; --ds-line:#CDD4DB;
  --ds-accent:#E2571A; --ds-accent2:#2F5D86;
  --ds-c1:#2F4252; --ds-c2:#4F6679; --ds-c3:#7389A0; --ds-c4:#9DB0C1; --ds-c5:#C6D2DC;
  --ds-radius:2px; --ds-shadow:0 1px 0 rgba(31,43,54,.05),0 18px 40px -22px rgba(31,43,54,.30);
  --ds-font-title:"Gothic A1","Pretendard","Apple SD Gothic Neo","Malgun Gothic",sans-serif;
  --ds-font-body:"IBM Plex Sans KR","Pretendard","Apple SD Gothic Neo","Malgun Gothic",sans-serif;
  --ds-font-num:"IBM Plex Mono","SFMono-Regular",Consolas,monospace;
}
.slide{isolation:isolate;background:var(--ds-bg);color:var(--ds-ink);font:400 28px/1.55 var(--ds-font-body)}
/* 바닥이 벽으로 휘는 스튜디오 곡면: 아래 1/3 이 조금 밝다 */
.slide::before{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:linear-gradient(180deg,rgba(255,255,255,0) 58%,rgba(255,255,255,.55) 74%,rgba(255,255,255,.2) 100%)}

/* ── 공통: 머리말 · 결론 제목 · 쪽 번호 · 출처 ─────────────────── */
.s-body{position:absolute;inset:88px 120px 96px;display:flex;flex-direction:column;gap:40px}
.kicker{display:flex;align-items:center;gap:16px;margin:0;font:600 24px/1 var(--ds-font-body);letter-spacing:.02em;color:var(--ds-sub)}
.kicker::before{content:"";width:40px;height:2px;background:var(--ds-ink)}
.title{margin:0;max-width:1560px;font:800 56px/1.28 var(--ds-font-title);letter-spacing:-.01em;text-wrap:balance}
.title em{font-style:normal;color:var(--ds-accent)}
.lead{margin:-16px 0 0;max-width:1400px;font-size:28px;color:var(--ds-sub)}
.fill{flex:1;min-height:0}
.src{position:absolute;left:120px;bottom:40px;margin:0;font:400 22px/1 var(--ds-font-body);color:var(--ds-sub)}
.page-no{position:absolute;right:120px;bottom:40px;font:500 22px/1 var(--ds-font-num);letter-spacing:.08em;color:var(--ds-sub)}

/* ── 모형대 매스: 흰 덩어리 층. .lit 한 층만 주황(진행 · 강조 한 곳) ── */
.mass{display:flex;flex-direction:column-reverse;align-items:center;gap:0}
.mass i{display:block;height:64px;background:linear-gradient(180deg,#FFFFFF,#F1F3F5);border:1px solid #DCE1E6;border-bottom-color:#C9D0D7;
  box-shadow:0 1px 0 rgba(255,255,255,.9) inset,0 10px 24px -16px rgba(31,43,54,.35)}
.mass i:nth-child(1){width:420px}.mass i:nth-child(2){width:360px}.mass i:nth-child(3){width:300px}.mass i:nth-child(4){width:240px}.mass i:nth-child(5){width:180px}
.mass i.lit{background:linear-gradient(180deg,#F07338,var(--ds-accent));border-color:#C9481A;box-shadow:0 0 48px -6px rgba(226,87,26,.55),0 10px 24px -16px rgba(31,43,54,.35)}
.mass::after{content:"";order:-1;width:520px;height:22px;margin-top:-2px;background:radial-gradient(50% 100% at 50% 0,rgba(31,43,54,.22),transparent 70%)}

/* ── 표지 ─────────────────────────────────────────── */
.cover .c-text{position:absolute;left:120px;top:170px;width:1240px;display:flex;flex-direction:column;gap:28px}
.cover .c-tag{font:600 24px/1 var(--ds-font-body);letter-spacing:.04em;color:var(--ds-sub)}
.cover h1{margin:0;font:800 96px/1.16 var(--ds-font-title);letter-spacing:-.02em}
.cover h1 em{font-style:normal;color:var(--ds-accent)}
.cover .c-sub{margin:0;font-size:32px;color:var(--ds-sub);max-width:900px}
.cover .c-org{position:absolute;left:120px;bottom:96px;display:flex;gap:40px;margin:0;font:500 26px/1.4 var(--ds-font-body);color:var(--ds-c1)}
.cover .mass{position:absolute;right:200px;bottom:200px}

/* ── 목차: 줄 높이 112px, 지금 장 한 줄만 주황 ────────────────── */
.toc-list{list-style:none;margin:0;padding:0;border-top:2px solid var(--ds-ink);width:1080px}
.toc-list li{display:grid;grid-template-columns:120px 1fr 120px;align-items:center;height:112px;border-bottom:1px solid var(--ds-line);font:700 36px/1.2 var(--ds-font-title)}
.toc-list li b{font:600 28px/1 var(--ds-font-num);color:var(--ds-sub)}
.toc-list li span:last-child{justify-self:end;font:500 24px/1 var(--ds-font-num);color:var(--ds-sub)}
.toc-list li.is-now{color:var(--ds-accent)}.toc-list li.is-now b{color:var(--ds-accent)}
.toc .mass{position:absolute;right:180px;bottom:180px}

/* ── 간지: 큰 번호 + 섹션 이름, 매스의 그 층만 점등 ──────────────── */
.divider .d-no{position:absolute;left:120px;top:200px;font:600 220px/1 var(--ds-font-num);letter-spacing:-.04em;color:var(--ds-ink)}
.divider .d-no small{display:block;margin-bottom:24px;font-size:24px;letter-spacing:.16em;color:var(--ds-sub)}
.divider h2{position:absolute;left:120px;top:560px;margin:0;font:800 88px/1.2 var(--ds-font-title)}
.divider p{position:absolute;left:120px;top:690px;margin:0;width:900px;font-size:30px;color:var(--ds-sub)}
.divider .mass{position:absolute;right:240px;bottom:200px}

/* ── 마무리 ────────────────────────────────────────── */
.close h2{position:absolute;left:120px;top:380px;margin:0;font:800 80px/1.25 var(--ds-font-title)}
.close p{position:absolute;left:120px;top:600px;margin:0;font-size:30px;color:var(--ds-sub)}
.close .spot{position:absolute;right:280px;top:420px;width:180px;height:180px;background:var(--ds-surface);border:1px solid #DCE1E6;box-shadow:var(--ds-shadow)}
.close .spot::after{content:"";position:absolute;left:50%;top:50%;width:36px;height:36px;margin:-18px 0 0 -18px;border-radius:50%;background:var(--ds-accent);box-shadow:0 0 40px rgba(226,87,26,.5)}

/* ── 배치 격자 ─────────────────────────────────────── */
.grid{display:grid;gap:32px;align-items:stretch}
.grid.center{align-content:center}
.grid.g2{grid-template-columns:repeat(2,1fr)}.grid.g3{grid-template-columns:repeat(3,1fr)}.grid.g4{grid-template-columns:repeat(4,1fr)}
.split{display:grid;grid-template-columns:1.35fr 1fr;gap:48px;align-items:stretch}

/* ── 카드 묶음 ─────────────────────────────────────── */
.card{background:var(--ds-surface);border-radius:var(--ds-radius);box-shadow:var(--ds-shadow);border-top:3px solid var(--ds-c1);padding:40px 40px 36px;display:flex;flex-direction:column;gap:18px;min-width:0;min-height:440px}
.card .c-foot{margin-top:auto;padding-top:20px;border-top:1px solid var(--ds-line);font-size:24px;color:var(--ds-sub)}
.card .c-foot b{font:600 30px/1 var(--ds-font-num);color:var(--ds-ink)}
.card .c-no{font:600 24px/1 var(--ds-font-body);color:var(--ds-sub)}
.card h3{margin:0;font:800 44px/1.25 var(--ds-font-title)}
.card p{margin:0;font-size:28px;line-height:1.5;color:var(--ds-c1)}
.card.is-key{border-top-color:var(--ds-accent)}.card.is-key .c-no{color:var(--ds-accent)}

/* ── 수치 타일 ─────────────────────────────────────── */
.tile{background:var(--ds-surface);border-radius:var(--ds-radius);box-shadow:var(--ds-shadow);padding:36px;display:flex;flex-direction:column;gap:12px;min-width:0}
.tile span{font-size:26px;color:var(--ds-sub)}
.tile b{font:600 88px/1 var(--ds-font-num);letter-spacing:-.03em;color:var(--ds-ink)}
.tile b small{margin-left:8px;font-size:32px;font-weight:500;letter-spacing:0;color:var(--ds-sub)}
.tile p{margin:0;font-size:24px;color:var(--ds-sub)}
.tile.is-key b{color:var(--ds-accent)}

/* ── 막대(가로): style="--v:42" 는 최댓값 대비 % ─────────────────── */
.bars{background:var(--ds-surface);border-radius:var(--ds-radius);box-shadow:var(--ds-shadow);padding:40px;display:flex;flex-direction:column;justify-content:center;gap:44px;min-width:0}
.bars h3{margin:0;font:700 30px/1.3 var(--ds-font-title)}
.bar{display:grid;grid-template-columns:110px 1fr 120px;align-items:center;gap:20px;font-size:28px}
.bar::before{content:"";grid-column:2;grid-row:1;height:64px;width:calc(var(--v) * 1%);background:var(--ds-c4)}
.bar span{grid-column:1;grid-row:1;font-family:var(--ds-font-num);color:var(--ds-sub)}
.bar b{grid-column:3;grid-row:1;justify-self:end;font:600 30px/1 var(--ds-font-num)}
.bar.is-key::before{background:var(--ds-accent)}.bar.is-key b{color:var(--ds-accent)}

/* ── 현안 → 해결 표 ─────────────────────────────────── */
.fix{display:grid;grid-template-columns:1fr 72px 1.25fr;gap:0;align-items:stretch}
.stack{display:flex;flex-direction:column;justify-content:center;gap:28px}
.fix > p{margin:0;padding:34px 36px;font-size:30px;line-height:1.45;border-radius:var(--ds-radius)}
.fix .q{background:#E3E8ED;color:var(--ds-c1)}
.fix .a{background:var(--ds-surface);box-shadow:var(--ds-shadow);font-weight:600}
.fix .q b,.fix .a b{display:block;margin-bottom:10px;font:600 24px/1 var(--ds-font-body);color:var(--ds-sub)}
.fix i{position:relative}
.fix i::after{content:"";position:absolute;left:18px;right:18px;top:50%;height:2px;background:var(--ds-ink)}
.fix i::before{content:"";position:absolute;right:16px;top:50%;width:14px;height:14px;margin-top:-7px;border-top:2px solid var(--ds-ink);border-right:2px solid var(--ds-ink);transform:rotate(45deg)}
.fix.is-key .a{box-shadow:inset 4px 0 0 var(--ds-accent),var(--ds-shadow)}

/* ── 간트(월 1~12): style="--from:3;--to:6" ────────────────────── */
.gantt{background:var(--ds-surface);border-radius:var(--ds-radius);box-shadow:var(--ds-shadow);padding:32px 36px;display:grid;grid-template-columns:260px repeat(12,1fr);row-gap:18px;align-items:center;min-width:0}
.gantt .g-h{font:500 22px/1 var(--ds-font-num);color:var(--ds-sub);text-align:center}
.gantt .g-h:first-child{text-align:left;font-family:var(--ds-font-body)}
.gantt .g-name{grid-column:1;font-size:26px;line-height:1.3}
.gantt .g-bar{grid-column:calc(var(--from) + 1) / calc(var(--to) + 2);height:30px;background:var(--ds-c3);border-radius:1px}
.gantt .g-bar.is-key{background:var(--ds-accent)}
.gantt .g-name,.gantt .g-bar{border-top:1px solid transparent}

/* ── 표 ────────────────────────────────────────────── */
.tbl{width:100%;border-collapse:collapse;background:var(--ds-surface);box-shadow:var(--ds-shadow);font-size:28px}
.tbl th{padding:20px 28px;text-align:left;font:600 24px/1.2 var(--ds-font-body);color:var(--ds-sub);border-bottom:2px solid var(--ds-ink)}
.tbl td{padding:18px 24px;border-bottom:1px solid var(--ds-line)}
.tbl td.n{text-align:right;font:500 28px/1 var(--ds-font-num)}
.tbl tr.is-key td{color:var(--ds-accent);font-weight:600}
.tbl tfoot td{font-weight:700;border-bottom:0;border-top:2px solid var(--ds-ink)}
```
