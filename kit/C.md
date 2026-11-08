# C 경쾌한 놀이 오브젝트 — 계획안 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **ChatGPT · Claude · Gemini 같은 채팅 AI**에게 통째로 주면, 이 디자인으로 계획안 발표 덱을 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 C 계열 장표(#7 · #24 · #29 · #39 · #82)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일을 첨부**합니다(안 되면 내용을 끝까지 복사해 붙여 넣기).
2. 만들 계획안을 말합니다. 예) "2027 ○○ 지원 계획(안), ○○교육청 ○○과. 현황 수치는 아래 표(출처: ○○ 통계), 세부과제 3개는 … 덱으로 만들어 줘. 결과는 .html 파일로."
3. AI가 먼저 **장별 구성안**(머리말 · 결론 제목 · 부품 · 수치와 출처)을 보여 줍니다. 고칠 곳을 말하거나 "좋아, 만들어 줘".
4. 받은 `슬라이드.html`을 내려받아 더블클릭합니다. → · Space로 넘기고, F는 전체 화면, 인쇄하면 장마다 한 쪽(16:9) PDF가 됩니다.
5. 고칠 곳은 "3장 제목을 ○○로"처럼 말합니다. 코드가 끊기면 "끊긴 곳부터 이어서".

알아 둘 점
- 열 때 **인터넷이 필요**합니다(공통 CSS · 엔진 · 글꼴을 `szxv7704-dot.github.io`에서 불러옴). 업무망처럼 인터넷이 막힌 곳에서 발표하려면 저장소에서 `python3 scripts/kit.py inline C 슬라이드.html`을 실행해 모든 것이 파일 안에 든 판을 만드세요.
- AI 화면 안의 미리보기에서는 색 · 모양이 안 나올 수 있습니다. 내려받아 브라우저(크롬 · 엣지)로 열면 정상입니다.
- 수치는 AI가 지어내지 않도록 계약에 적어 두었지만, **받은 덱의 숫자를 원자료와 꼭 대조**하세요.
- 개인정보(학생 이름 · 사진 등)는 AI에게 넣지 마세요.

## 라이선스

- 글꼴: 모두 SIL Open Font License 1.1(전문 https://szxv7704-dot.github.io/design-reference-gallery/fonts/OFL.txt). 이 계열이 쓰는 글꼴의 저작권 고지:

| 글꼴 | 굵기 | 저작권 | 예약 이름 | 라이선스 |
|---|---|---|---|---|
| BlackHanSans | 400 | Copyright 2015 The Black Han Sans Project Authors (https://github.com/zesstype/Black-Han-Sans) | — | SIL OFL 1.1 |
| Fredoka | 500 · 600 · 700 | Copyright 2016 The Fredoka Project Authors (https://github.com/hafontia/Fredoka-One) | — | SIL OFL 1.1 |
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
4. **강조색은 한 장에 한 곳**: 제목의 `<em>` 하나 또는 부품의 `.is-key` 하나(둘 다 쓰면 같은 내용을 가리켜야 함).
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
- 표지 · 목차 · 간지 · 마무리에는 이 계열의 상징 부품인 블록 탑(`.blocks`)을 씁니다. 블록 수 = 섹션 수(아래가 1섹션), 간지는 지금 층까지만 놓고 남은 층은 `.ghost`, 마무리는 `.flag`.
- 같은 모양의 장이 연달아 나오지 않게 합니다. 누를 때마다 하나씩 보이는 장(`data-steps`)은 덱 전체에서 1~2장.

### 출력 방식
- 결과는 **`.html` 파일 하나**(UTF-8)로 줍니다. 파일을 만들 수 있는 기능(아티팩트 · 캔버스 · 파일 첨부)이 있으면 반드시 그것으로 줍니다. 없을 때만 완성된 HTML 전체를 ```html 코드 블록 하나로 출력합니다.
- `...`, "(생략)", "(이하 동일)"을 쓰지 않습니다. `<!DOCTYPE html>`부터 `</html>`까지 전부 씁니다. 끊기면 사용자가 "이어서"라고 할 때 끊긴 글자 바로 다음부터 씁니다.
- **미리보기 창에서 색 · 모양이 안 보여도 고치지 마세요.** 공통 CSS · 엔진을 인터넷에서 불러오는데, 일부 미리보기는 바깥 파일을 막습니다. 내려받아 브라우저로 열면 정상입니다.

### 내보내기 전 점검 (하나라도 아니면 고친 뒤 내보내기)
1. 사용자가 주지 않았고 확인도 받지 않은 수치 · 사실이 없는가? 수치가 있는 장마다 `.src`가 있는가?
2. 모든 본문 장의 제목이 결론 한 문장이고, 두 줄 이내인가?
3. 강조(`<em>` · `.is-key`)가 장마다 한 곳이고, 둘을 함께 썼다면 같은 내용을 가리키는가?
4. 쓴 클래스가 모두 부품 사전(3) 또는 '추가 부품' 칸에 있는가? 인라인 style은 `--v` · `--from` · `--to`뿐인가?
5. 공통 파일 두 줄이 그대로이고, 장 번호 · 쪽 표시 · 점을 손으로 쓰지 않았는가?
6. 모든 장이 1920 × 1080 안에 들어가는가(높이 예산 · 카드 규칙)? 큰 빈 곳이 없는가?
7. 뼈대의 예시 문구가 남아 있지 않은가? 생략 없이 끝까지 썼는가?

---

## 1. 디자인 규칙 (`C` design.md)

````markdown
---
kit: C
name: 경쾌한 놀이 오브젝트
version: v1
stage: 1920x1080
colors:
  bg: "#F3F7FC"        # 밝은 하늘빛 흰 바탕
  surface: "#FFFFFF"   # 둥근 흰 카드 · 타일 · 표
  ink: "#1D2B4F"       # 글자 · 머리말 띠(3px 먹선)
  sub: "#56607A"       # 보조 글자
  line: "#D3DCE8"      # 구분선
  number: "#2F62C8"    # 숫자 · 쪽 번호(파랑)
  pale: "#DCE9FC"      # 현안 칸 · 표 머리
  accent: "#F2463C"    # 빨강 — 한 장에 한 곳
  toy: ["#2F7BF5", "#FFC22E", "#22B573", "#FF8A2A", "#F2463C"]   # 섹션 1~5 색. 섹션 표시에만
fonts:
  title: "Black Han Sans 400"        # 표지 100 · 간지 · 마무리 96 · 장 제목 58 · 카드 제목 48
  body: "IBM Plex Sans KR 400/700"   # 본문 28 · 보조 22~26
  num: "Fredoka 600"                 # 숫자에만(한글 없음) · 수치 92 · 간지 번호 240
space: {side: 120px, top: 80px, bottom: 96px, gap: 32px}
radius: 14px
shadow: "0 2px 0 rgba(29,43,79,.06), 0 18px 36px -22px rgba(29,43,79,.35)"
---

## 분위기
밝은 하늘빛 바탕에 광택 있는 장난감 블록. 하나씩 딱 맞춰 쌓아 완성하는 성취감.
- **섹션 수 = 블록 수, 층 순서 = 목차 순서.** 목차(다 쌓인 탑) → 간지(지금 층까지 놓이고 남은 층은 점선) → 마무리(깃발 꽂은 탑)가 한 물체의 진행으로 이어진다.
- 원색 다섯(`toy`)은 **섹션 표시에만** 쓴다(블록 · 목차 칩 · 카드 칩). 내용 강조에 쓰지 않는다.
- 강조 빨강은 한 장에 한 곳: 제목 한 낱말(`<em>`) 또는 부품 하나(`.is-key`).
- 근거 장표: 표지 #7 · #24 · #29 · #39, 목차 · 간지 키트 #82.

## 색의 역할
| 이름 | 쓰는 곳 | 쓰지 않는 곳 |
|---|---|---|
| bg | 모든 장의 바탕 | 카드 면 |
| surface | 카드 · 타일 · 막대 판 · 간트 · 표 · 기관 이름표 | 바탕 |
| ink | 제목 · 본문 · 머리말 띠 3px 선 | 넓은 면 |
| number(파랑) | 숫자 · 로마 숫자 · 쪽 번호 · 보통 막대 | 문장 |
| toy 1~5 | 섹션 1~5의 블록 · 칩 | 강조, 막대 색 |
| accent(빨강) | 한 장에 한 곳(제목 낱말 또는 `.is-key`) | 배경 · 장식 |

5섹션 블록 색과 강조 빨강이 같은 색이다(#82 그대로). 그래서 5섹션 블록이 보이는 장에서는 강조를 제목 낱말 하나로만 둔다.

## 글자
- 제목은 Black Han Sans(굵기 하나), 본문은 IBM Plex Sans KR, **숫자는 Fredoka**(둥근 숫자).
- **Fredoka에는 한글이 없다.** 숫자 · 영문에만 쓴다. 단위(교 · %)는 본문 글꼴(`small`)로.
- 자간은 0 안팎. 영문 대문자 + 넓은 자간 같은 장치는 쓰지 않는다.
- 크기: 읽는 글 28px 이상, 보조 글 22px 이상.
- 한글 줄바꿈은 낱말 단위(공통 CSS).

## 장의 짜임 (계획안 본문)
모든 본문 장은 같은 순서다: **머리말 띠(`.kicker`, 아래 3px 먹선) → 결론 한 문장 제목(`.title`) → 도식 1~2개 → 출처(`.src`)**.
- 제목은 결론 문장이다. "현황"(×) → "참여 학교는 늘었지만, 지역 공간과 잇는 학교는 3곳 중 1곳뿐입니다"(○).
- 카드 묶음은 카드 순서 = 섹션 색 순서로 칩이 붙는다(1번째 파랑, 2번째 노랑…). 순서에 의미가 없는 카드 묶음이면 칩 색도 순서대로 바뀐다는 점을 받아들이거나 카드 3개 이하로 쓴다.

## 블록 탑(.blocks) — 이 계열의 얼굴
- 표지 · 목차 · 간지 · 마무리에만 쓴다. 블록 수 = 섹션 수(최대 5), 아래가 1섹션. 색은 자동(파랑 · 노랑 · 초록 · 주황 · 빨강).
- 표지 · 목차: 다 쌓인 탑 / 간지: 지금 층까지 놓고 남은 층은 `.ghost`(점선) / 마무리: `.blocks.flag`(깃발).
- 블록을 기울이거나 회전하지 않는다. 본문 장에는 쓰지 않는다.

## 깊이와 모양
- 모서리 14px, 그림자는 하나(`--ds-shadow`). 블록만 윗면 광택 · 아래 음영을 갖는다.
- 강조 카드는 4px 빨강 안테.

## 해야 할 것
1. 장마다 결론 한 문장 제목.
2. 수치에는 단위와 출처.
3. 원색은 섹션 표시에만, 빨강 강조는 한 곳.
4. 화면을 채운다.

## 하지 말 것
1. 새 색, 원색을 내용 강조에 쓰기.
2. Fredoka로 한글 쓰기.
3. 본문 장에 블록 탑 넣기, 블록 기울이기.
4. 장 번호 · 쪽 표시 · 점을 손으로 쓰기(엔진이 채운다).
5. 공통 CSS · 엔진을 HTML 안에 옮겨 쓰기, `@font-face` 새로 쓰기.
6. 인라인 `style`은 `--v` · `--from` · `--to`만.

## 새 부품을 만들 때
1. 먼저 `.grid` · `.split` · `.stack`과 기존 부품으로 될지 본다.
2. 새 상자는 흰 면 + 모서리 14px + `--ds-shadow`.
3. 섹션을 가리키면 그 섹션의 toy 색 칩을, 아니면 색 없이.
4. 강조는 `.is-key` 한 곳, 빨강.

## 알려진 한계 (v1)
- 블록은 CSS로 그린 정면 블록이다. 근거 장표(#7 · #82)의 캔버스 축측 블록(윗면 · 옆면 입체)만큼 입체감이 깊지 않다.
- 막대는 가로뿐. 세로 막대 · 선 · 도넛 · 지도 부품은 없다.
- 섹션이 6개 이상이면 블록 색이 모자란다(최대 5).
````

---

## 2. 글씨체

- 제목 Black Han Sans(400) · 본문 IBM Plex Sans KR(400/700) · 숫자 Fredoka(600). 공통 CSS가 불러오므로 설치하지 않아도 됩니다(열 때 인터넷 필요).
- 글꼴은 변수로만 지정합니다: `var(--ds-font-title)` · `var(--ds-font-body)` · `var(--ds-font-num)`(숫자 · 영문에만).

---

## 3. 부품 사전 (이 계열 CSS에 정의된 클래스)

이 목록에 있는 클래스만 씁니다. "예"는 뼈대(4)에서 그 클래스를 처음 쓴 태그입니다. 공용 클래스: `.slide`(장 하나) · `data-steps="n"`(장) + `data-step="k"`(안의 요소, 누를 때마다 하나씩) · `.page-no`(빈 칸, 엔진이 채움).

**공통: 머리말 띠(3px 먹선) · 결론 제목 · 쪽 번호 · 출처**
- `.s-body` — 예: `<div class="s-body">`
- `.kicker` — 예: `<p class="kicker">`
- `.title` — 예: `<h2 class="title">`
- `.lead`
- `.fill` — 예: `<div class="split fill">`
- `.src` — 예: `<p class="src">`
- `.page-no` — 예: `<span class="page-no">`

**블록 탑: 블록 수 = 섹션 수, 아래가 1섹션. .ghost 아직 안 놓인 층(점선), .flag 깃발(마무리)**
- `.blocks` — 예: `<div class="blocks" aria-hidden="true">`
- `.ghost` — 예: `<i class="ghost">`
- `.flag` — 예: `<div class="blocks flag" aria-hidden="true">`
- `.toc-list` — 예: `<ol class="toc-list">`
- `.card` — 예: `<div class="card">`
- `.c-no` — 예: `<span class="c-no">`
- `.grid` — 예: `<div class="grid g2">`

**표지**
- `.cover` — 예: `<section class="slide cover">`
- `.c-text` — 예: `<div class="c-text">`
- `.c-tag` — 예: `<span class="c-tag">`
- `.c-sub` — 예: `<p class="c-sub">`
- `.c-org` — 예: `<p class="c-org">`
- `.blocks` — 예: `<div class="blocks" aria-hidden="true">`

**목차: 줄마다 섹션 색 블록 칩**
- `.toc-list` — 예: `<ol class="toc-list">`
- `.is-now` — 예: `<li class="is-now">`
- `.toc` — 예: `<section class="slide toc">`
- `.blocks` — 예: `<div class="blocks" aria-hidden="true">`

**간지: 지금 층까지만 놓이고 남은 층은 점선**
- `.divider` — 예: `<section class="slide divider">`
- `.d-no` — 예: `<div class="d-no">`
- `.blocks` — 예: `<div class="blocks" aria-hidden="true">`

**마무리: 깃발 꽂은 탑**
- `.close` — 예: `<section class="slide close">`
- `.blocks` — 예: `<div class="blocks" aria-hidden="true">`

**배치 격자**
- `.grid` — 예: `<div class="grid g2">`
- `.center` — 예: `<div class="grid g3 fill center">`
- `.g2` — 예: `<div class="grid g2">`
- `.g3` — 예: `<div class="grid g3 fill center">`
- `.g4`
- `.split` — 예: `<div class="split fill">`
- `.stack` — 예: `<div class="fill stack">`

**카드 묶음**
- `.card` — 예: `<div class="card">`
- `.c-no` — 예: `<span class="c-no">`
- `.c-foot` — 예: `<p class="c-foot">`
- `.is-key` — 예: `<div class="tile is-key">`

**수치 타일**
- `.tile` — 예: `<div class="tile">`
- `.is-key` — 예: `<div class="tile is-key">`

**막대(가로, 둥근 끝): style="--v:42" 는 최댓값 대비 %**
- `.bars` — 예: `<div class="bars">`
- `.bar` — 예: `<div class="bar" style="--v:69">`
- `.is-key` — 예: `<div class="tile is-key">`

**현안 → 해결**
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.q` — 예: `<p class="q">`
- `.a` — 예: `<p class="a">`
- `.is-key` — 예: `<div class="tile is-key">`

**간트(월 1~12, 둥근 막대): style="--from:3;--to:6"**
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
<html lang="ko" data-kit="C">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>덱 키트 C · 경쾌한 놀이 오브젝트 — 예시 덱</title>
<!-- 이 계열의 공통 CSS(글꼴 · 색 · 부품). 이 줄은 지우거나 바꾸지 마세요 -->
<link rel="stylesheet" href="https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/C.css">
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
  <div class="blocks" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
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
  <div class="blocks" aria-hidden="true"><i class="now"></i><i></i><i></i><i></i><i></i></div>
  <span class="page-no"></span>
</section>

<!-- 3. 간지 -->
<section class="slide divider">
  <div class="d-no"><small>SECTION</small>01</div>
  <h2>현황</h2>
  <p>참여는 늘었지만 학교 밖과 이어지는 수업은 아직 적습니다.</p>
  <div class="blocks" aria-hidden="true"><i class="now"></i><i class="ghost"></i><i class="ghost"></i><i class="ghost"></i><i class="ghost"></i></div>
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
  <div class="blocks flag" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
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

부품 모양 · 크기를 이해하는 데만 쓰세요(`https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/C.css`의 계열 부분).

```css
/* C 경쾌한 놀이 오브젝트 — 덱 키트 v1 (deck.css 다음에 불러옴)
   밝은 하늘빛 흰 바탕 + 장난감 블록. 원색 다섯은 섹션 표시에만, 빨강 강조는 한 곳.
   근거 장표: #7 · #24 · #29 · #39(표지), #82(목차·간지 키트) */
:root{
  --ds-stage:#DCE6F2;
  --ds-bg:#F3F7FC; --ds-surface:#FFFFFF; --ds-ink:#1D2B4F; --ds-sub:#56607A; --ds-line:#D3DCE8;
  --ds-accent:#F2463C; --ds-accent2:#2F7BF5;
  --ds-c1:#1C3B7A; --ds-c2:#2F62C8; --ds-c3:#5B8FEA; --ds-c4:#A9C7F7; --ds-c5:#DCE9FC;
  --ds-toy1:#2F7BF5; --ds-toy2:#FFC22E; --ds-toy3:#22B573; --ds-toy4:#FF8A2A; --ds-toy5:#F2463C;
  --ds-radius:14px; --ds-shadow:0 2px 0 rgba(29,43,79,.06),0 18px 36px -22px rgba(29,43,79,.35);
  --ds-font-title:"Black Han Sans","Gmarket Sans","Apple SD Gothic Neo","Malgun Gothic",sans-serif;
  --ds-font-body:"IBM Plex Sans KR","Pretendard","Apple SD Gothic Neo","Malgun Gothic",sans-serif;
  --ds-font-num:"Fredoka","Arial Rounded MT Bold","Black Han Sans",sans-serif;
}
.slide{isolation:isolate;background:var(--ds-bg);color:var(--ds-ink);font:400 28px/1.55 var(--ds-font-body)}
.slide::before{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:radial-gradient(70% 55% at 75% 70%,rgba(255,255,255,.9),rgba(255,255,255,0) 70%)}

/* ── 공통: 머리말 띠(3px 먹선) · 결론 제목 · 쪽 번호 · 출처 ─────────── */
.s-body{position:absolute;inset:80px 120px 96px;display:flex;flex-direction:column;gap:36px}
.kicker{margin:0;padding-bottom:16px;border-bottom:3px solid var(--ds-ink);font:700 24px/1 var(--ds-font-body);color:var(--ds-ink)}
.title{margin:0;max-width:1600px;font:400 58px/1.3 var(--ds-font-title);letter-spacing:-.01em;text-wrap:balance}
.title em{font-style:normal;color:var(--ds-accent)}
.lead{margin:-12px 0 0;max-width:1400px;font-size:28px;color:var(--ds-sub)}
.fill{flex:1;min-height:0}
.src{position:absolute;left:120px;bottom:40px;margin:0;font:400 22px/1 var(--ds-font-body);color:var(--ds-sub)}
.page-no{position:absolute;right:120px;bottom:40px;font:600 24px/1 var(--ds-font-num);color:var(--ds-c2)}

/* ── 블록 탑: 블록 수 = 섹션 수, 아래가 1섹션. .ghost 아직 안 놓인 층(점선), .flag 깃발(마무리) ── */
.blocks{display:flex;flex-direction:column-reverse;align-items:center}
.blocks i{--c:var(--ds-toy1);position:relative;display:block;width:320px;height:84px;margin-top:-2px;border-radius:12px;background:var(--c);
  box-shadow:inset 0 -14px 0 rgba(0,0,0,.16),inset 0 10px 0 rgba(255,255,255,.28),0 2px 0 rgba(29,43,79,.08)}
.blocks i::before{content:"";position:absolute;left:30px;right:30px;top:-20px;height:26px;
  background:radial-gradient(ellipse 25px 13px at 50% 40%,rgba(255,255,255,.35),transparent 70%) 0 0/25% 100%,
             radial-gradient(ellipse 25px 13px at 50% 50%,var(--c) 92%,transparent 100%) 0 0/25% 100%,
             radial-gradient(ellipse 25px 13px at 50% 75%,rgba(0,0,0,.22) 92%,transparent 100%) 0 0/25% 100%}
.blocks i:nth-child(2){--c:var(--ds-toy2)}.blocks i:nth-child(3){--c:var(--ds-toy3)}.blocks i:nth-child(4){--c:var(--ds-toy4)}.blocks i:nth-child(5){--c:var(--ds-toy5)}
.blocks i.ghost{background:transparent;box-shadow:none;border:4px dashed var(--ds-c4)}
.blocks i.ghost::before{display:none}
.blocks::before{content:"";order:-1;width:440px;height:26px;margin-top:-6px;background:radial-gradient(50% 100% at 50% 0,rgba(29,43,79,.22),transparent 70%)}
.blocks.flag::after{content:"";width:130px;height:180px;margin:0 0 -6px 100px;
  background:linear-gradient(var(--ds-ink),var(--ds-ink)) 0 0/8px 100% no-repeat,linear-gradient(var(--ds-accent),var(--ds-accent)) 8px 6px/112px 76px no-repeat;
  clip-path:polygon(0 0,8px 0,8px 6px,120px 44px,8px 82px,8px 100%,0 100%)}

/* 섹션 색 칩(목차 줄 · 카드 머리): 작은 블록 하나 */
.toc-list li::before,.card .c-no::before{content:"";flex:none;width:44px;height:32px;border-radius:7px;background:var(--c,var(--ds-toy1));
  box-shadow:inset 0 -6px 0 rgba(0,0,0,.16),inset 0 4px 0 rgba(255,255,255,.3)}
.toc-list li:nth-child(2),.grid > .card:nth-child(2){--c:var(--ds-toy2)}
.toc-list li:nth-child(3),.grid > .card:nth-child(3){--c:var(--ds-toy3)}
.toc-list li:nth-child(4),.grid > .card:nth-child(4){--c:var(--ds-toy4)}
.toc-list li:nth-child(5),.grid > .card:nth-child(5){--c:var(--ds-toy5)}

/* ── 표지 ─────────────────────────────────────────── */
.cover .c-text{position:absolute;left:120px;top:170px;width:1180px;display:flex;flex-direction:column;gap:28px}
.cover .c-tag{font:600 26px/1 var(--ds-font-num);color:var(--ds-c2)}
.cover h1{margin:0;font:400 100px/1.16 var(--ds-font-title);letter-spacing:-.01em}
.cover h1 em{font-style:normal;color:var(--ds-accent)}
.cover .c-sub{margin:0;font-size:32px;color:var(--ds-sub);max-width:900px}
.cover .c-org{position:absolute;left:120px;bottom:96px;display:flex;gap:40px;margin:0;padding:24px 36px;border-radius:var(--ds-radius);background:var(--ds-surface);box-shadow:var(--ds-shadow);font:600 26px/1.4 var(--ds-font-body);color:var(--ds-ink)}
.cover .blocks{position:absolute;right:220px;bottom:170px}

/* ── 목차: 줄마다 섹션 색 블록 칩 ─────────────────────────── */
.toc-list{list-style:none;margin:0;padding:0;width:1100px}
.toc-list li{display:grid;grid-template-columns:44px 90px 1fr 100px;column-gap:28px;align-items:center;height:108px;border-bottom:2px solid var(--ds-line);font:400 40px/1.2 var(--ds-font-title)}
.toc-list li b{font:600 34px/1 var(--ds-font-num);color:var(--ds-c2)}
.toc-list li span:last-child{justify-self:end;font:600 34px/1 var(--ds-font-num);color:var(--ds-c2)}
.toc-list li.is-now{color:var(--ds-accent)}.toc-list li.is-now b,.toc-list li.is-now span:last-child{color:var(--ds-accent)}
.toc .blocks{position:absolute;right:190px;bottom:170px}

/* ── 간지: 지금 층까지만 놓이고 남은 층은 점선 ─────────────────── */
.divider .d-no{position:absolute;left:120px;top:190px;font:600 240px/1 var(--ds-font-num);color:var(--ds-toy1)}
.divider .d-no small{display:block;margin-bottom:20px;font-size:26px;letter-spacing:.08em;color:var(--ds-sub)}
.divider h2{position:absolute;left:120px;top:560px;margin:0;font:400 96px/1.2 var(--ds-font-title)}
.divider p{position:absolute;left:120px;top:700px;margin:0;width:900px;font-size:30px;color:var(--ds-sub)}
.divider .blocks{position:absolute;right:240px;bottom:170px}

/* ── 마무리: 깃발 꽂은 탑 ───────────────────────────────── */
.close h2{position:absolute;left:120px;top:360px;margin:0;font:400 96px/1.2 var(--ds-font-title)}
.close p{position:absolute;left:120px;top:620px;margin:0;padding:22px 32px;border-radius:var(--ds-radius);background:var(--ds-surface);box-shadow:var(--ds-shadow);font-size:28px;color:var(--ds-ink)}
.close .blocks{position:absolute;right:240px;bottom:150px}

/* ── 배치 격자 ─────────────────────────────────────── */
.grid{display:grid;gap:32px;align-items:stretch}
.grid.center{align-content:center}
.grid.g2{grid-template-columns:repeat(2,1fr)}.grid.g3{grid-template-columns:repeat(3,1fr)}.grid.g4{grid-template-columns:repeat(4,1fr)}
.split{display:grid;grid-template-columns:1.35fr 1fr;gap:44px;align-items:stretch}
.stack{display:flex;flex-direction:column;justify-content:center;gap:24px}

/* ── 카드 묶음 ─────────────────────────────────────── */
.card{background:var(--ds-surface);border-radius:var(--ds-radius);box-shadow:var(--ds-shadow);padding:40px 40px 36px;display:flex;flex-direction:column;gap:18px;min-width:0;min-height:440px}
.card .c-no{display:flex;align-items:center;gap:16px;font:700 24px/1 var(--ds-font-body);color:var(--ds-sub)}
.card h3{margin:0;font:400 48px/1.25 var(--ds-font-title)}
.card p{margin:0;font-size:28px;line-height:1.5;color:var(--ds-ink)}
.card .c-foot{margin-top:auto;padding-top:20px;border-top:2px dashed var(--ds-line);font-size:24px;color:var(--ds-sub)}
.card .c-foot b{font:600 36px/1 var(--ds-font-num);color:var(--ds-c2)}
.card.is-key{box-shadow:inset 0 0 0 4px var(--ds-accent),var(--ds-shadow)}.card.is-key .c-foot b{color:var(--ds-accent)}

/* ── 수치 타일 ─────────────────────────────────────── */
.tile{background:var(--ds-surface);border-radius:var(--ds-radius);box-shadow:var(--ds-shadow);padding:36px;display:flex;flex-direction:column;gap:12px;min-width:0}
.tile span{font-size:26px;font-weight:700;color:var(--ds-sub)}
.tile b{font:600 92px/1 var(--ds-font-num);color:var(--ds-ink)}
.tile b small{margin-left:8px;font:700 32px/1 var(--ds-font-body);color:var(--ds-sub)}
.tile p{margin:0;font-size:24px;color:var(--ds-sub)}
.tile.is-key b{color:var(--ds-accent)}

/* ── 막대(가로, 둥근 끝): style="--v:42" 는 최댓값 대비 % ───────────── */
.bars{background:var(--ds-surface);border-radius:var(--ds-radius);box-shadow:var(--ds-shadow);padding:40px;display:flex;flex-direction:column;justify-content:center;gap:44px;min-width:0}
.bars h3{margin:0;font:400 34px/1.3 var(--ds-font-title)}
.bar{display:grid;grid-template-columns:110px 1fr 120px;align-items:center;gap:20px;font-size:28px}
.bar::before{content:"";grid-column:2;grid-row:1;height:60px;width:calc(var(--v) * 1%);border-radius:30px;background:var(--ds-c4);box-shadow:inset 0 -8px 0 rgba(0,0,0,.08)}
.bar span{grid-column:1;grid-row:1;font:600 30px/1 var(--ds-font-num);color:var(--ds-sub)}
.bar b{grid-column:3;grid-row:1;justify-self:end;font:600 36px/1 var(--ds-font-num);color:var(--ds-c2)}
.bar.is-key::before{background:var(--ds-accent)}.bar.is-key b{color:var(--ds-accent)}

/* ── 현안 → 해결 ───────────────────────────────────── */
.fix{display:grid;grid-template-columns:1fr 80px 1.25fr;gap:0;align-items:stretch}
.fix > p{margin:0;padding:32px 36px;font-size:30px;line-height:1.45;border-radius:var(--ds-radius)}
.fix .q{background:var(--ds-c5);color:var(--ds-c1)}
.fix .a{background:var(--ds-surface);box-shadow:var(--ds-shadow);font-weight:600}
.fix .q b,.fix .a b{display:block;margin-bottom:10px;font:700 24px/1 var(--ds-font-body);color:var(--ds-c2)}
.fix i{position:relative}
.fix i::after{content:"";position:absolute;left:50%;top:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;background:var(--ds-toy2);box-shadow:inset 0 -5px 0 rgba(0,0,0,.14)}
.fix i::before{content:"";position:absolute;left:50%;top:50%;z-index:1;width:12px;height:12px;margin:-7px 0 0 -9px;border-top:4px solid var(--ds-ink);border-right:4px solid var(--ds-ink);transform:rotate(45deg)}
.fix.is-key .a{box-shadow:inset 0 0 0 4px var(--ds-accent),var(--ds-shadow)}

/* ── 간트(월 1~12, 둥근 막대): style="--from:3;--to:6" ───────────────── */
.gantt{background:var(--ds-surface);border-radius:var(--ds-radius);box-shadow:var(--ds-shadow);padding:32px 36px;display:grid;grid-template-columns:250px repeat(12,1fr);row-gap:20px;align-items:center;min-width:0}
.gantt .g-h{font:600 24px/1 var(--ds-font-num);color:var(--ds-sub);text-align:center}
.gantt .g-h:first-child{text-align:left;font:700 24px/1 var(--ds-font-body)}
.gantt .g-name{grid-column:1;font-size:26px;line-height:1.3;font-weight:700}
.gantt .g-bar{grid-column:calc(var(--from) + 1) / calc(var(--to) + 2);height:34px;border-radius:17px;background:var(--ds-c3)}
.gantt .g-bar.is-key{background:var(--ds-accent)}

/* ── 표 ────────────────────────────────────────────── */
.tbl{width:100%;border-collapse:separate;border-spacing:0;background:var(--ds-surface);border-radius:var(--ds-radius);box-shadow:var(--ds-shadow);overflow:hidden;font-size:28px}
.tbl th{padding:22px 28px;text-align:left;font:700 24px/1.2 var(--ds-font-body);color:var(--ds-sub);background:var(--ds-c5)}
.tbl td{padding:20px 28px;border-bottom:2px solid var(--ds-line)}
.tbl td.n{text-align:right;font:600 32px/1 var(--ds-font-num);color:var(--ds-c2)}
.tbl tr.is-key td{color:var(--ds-accent);font-weight:700}.tbl tr.is-key td.n{color:var(--ds-accent)}
.tbl tfoot td{font-weight:700;border-bottom:0;background:var(--ds-c5)}
```
