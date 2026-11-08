# D 인쇄·종이 에디토리얼 — 계획안 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **ChatGPT · Claude · Gemini 같은 채팅 AI**에게 통째로 주면, 이 디자인으로 계획안 발표 덱을 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 D 계열 장표(#4 · #27 · #32 · #60 · #62)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일을 첨부**합니다(안 되면 내용을 끝까지 복사해 붙여 넣기).
2. 만들 계획안을 말합니다. 예) "2027 ○○ 지원 계획(안), ○○교육청 ○○과. 현황 수치는 아래 표(출처: ○○ 통계), 세부과제 3개는 … 덱으로 만들어 줘. 결과는 .html 파일로."
3. AI가 먼저 **장별 구성안**(머리말 · 결론 제목 · 부품 · 수치와 출처)을 보여 줍니다. 고칠 곳을 말하거나 "좋아, 만들어 줘".
4. 받은 `슬라이드.html`을 내려받아 더블클릭합니다. → · Space로 넘기고, F는 전체 화면, 인쇄하면 장마다 한 쪽(16:9) PDF가 됩니다.
5. 고칠 곳은 "3장 제목을 ○○로"처럼 말합니다. 코드가 끊기면 "끊긴 곳부터 이어서".

알아 둘 점
- 열 때 **인터넷이 필요**합니다(공통 CSS · 엔진 · 글꼴을 `szxv7704-dot.github.io`에서 불러옴). 업무망처럼 인터넷이 막힌 곳에서 발표하려면 저장소에서 `python3 scripts/kit.py inline D 슬라이드.html`을 실행해 모든 것이 파일 안에 든 판을 만드세요.
- AI 화면 안의 미리보기에서는 색 · 모양이 안 나올 수 있습니다. 내려받아 브라우저(크롬 · 엣지)로 열면 정상입니다.
- 수치는 AI가 지어내지 않도록 계약에 적어 두었지만, **받은 덱의 숫자를 원자료와 꼭 대조**하세요.
- 개인정보(학생 이름 · 사진 등)는 AI에게 넣지 마세요.

## 라이선스

- 글꼴: 모두 SIL Open Font License 1.1(전문 https://szxv7704-dot.github.io/design-reference-gallery/fonts/OFL.txt). 이 계열이 쓰는 글꼴의 저작권 고지:

| 글꼴 | 굵기 | 저작권 | 예약 이름 | 라이선스 |
|---|---|---|---|---|
| IBMPlexSansKR | 300 · 400 · 500 · 600 · 700 | Copyright 2018 IBM Corp. All rights reserved. | — | SIL OFL 1.1 |
| NotoSerifKR | 200 · 300 · 500 · 600 · 700 · 800 · 900 | (c) 2017-2024 Adobe (http://www.adobe.com/). | — | SIL OFL 1.1 |

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
- 표지 · 목차 · 간지 · 마무리에는 이 계열의 상징 부품인 판 번호(`.reg`)를 씁니다. 큰 명조 숫자 하나에 주홍 판이 4px 어긋나는 곳은 덱 전체에서 간지뿐, 재단 표시(`.crop`)도 간지에만.
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

## 1. 디자인 규칙 (`D` design.md)

````markdown
---
kit: D
name: 인쇄·종이 에디토리얼
version: v1
stage: 1920x1080
colors:
  bg: "#FBFAF6"        # 백상지
  surface: "#FFFFFF"   # 막대 판 · 간트 · 표(종이 위 한 장 더)
  paper2: "#F1EEE6"    # 현안 칸(재생지 톤)
  ink: "#1B1E24"       # 먹: 제목 · 본문 · 괘선
  sub: "#5C606A"       # 보조 글자
  line: "#CFCCC4"      # 가는 줄
  navy: "#1F3E6E"      # 남색 주판: 숫자 · 번호 · 막대
  bar: "#6D87AD"       # 보통 막대 · 간트
  accent: "#D9482B"    # 주홍 별색 — 한 장에 한 곳
fonts:
  title: "Noto Serif KR 700/900"     # 표지 104 · 간지 · 마무리 96 · 장 제목 58 · 카드 제목 48
  body: "IBM Plex Sans KR 400/600"   # 본문 28 · 보조 22~26
  num: "Noto Serif KR 700/900"       # 수치 96 · 간지 번호 280 · 목차 번호 48
space: {side: 120px, top: 80px, bottom: 96px, gap: 40px}
radius: 0
rules: "이중 괘선 = 굵은 3px + 4px 띄고 가는 1px"
---

## 분위기
밝고 단정한 지면. 신문 1면 · 잡지 특집처럼 **명조 제목과 괘선이 정보의 순서를 정한다**. 인쇄 공정의 흔적(이중 괘선 · 12단 눈금 · 재단 표시 · 맞춤 표지 · 판 어긋남)을 장식이 아니라 구조로 쓴다.
- 잉크는 두 판뿐: **남색 주판**(숫자 · 번호 · 막대)과 **주홍 별색**(한 장에 한 곳). 나머지는 먹.
- 근거 장표: 표지 #4 · #27 · #32 · #60, 목차 · 간지 키트 #62.

## 색의 역할
| 이름 | 쓰는 곳 | 쓰지 않는 곳 |
|---|---|---|
| bg | 모든 장의 바탕 | — |
| surface | 막대 판 · 간트 · 표 | 카드 · 타일(이들은 지면 위 단으로, 상자 없이) |
| ink | 제목 · 본문 · 모든 괘선 | 넓은 면 |
| navy | 숫자 · 번호 · 막대 | 문장 |
| accent(주홍) | 한 장에 한 곳(제목 낱말 또는 `.is-key`) + 간지의 판 어긋남 | 배경 · 두 곳 이상 |

## 글자
- 제목 · 숫자는 Noto Serif KR(명조) 700/900, 본문 · 라벨은 IBM Plex Sans KR(고딕).
- 명조는 크게(제목 · 숫자), 고딕은 작게(본문 · 라벨). 본문을 명조로 길게 쓰지 않는다(표지 부제 · 간지 설명 한 줄은 예외).
- 자간: 큰 명조는 -0.02~-0.04em, 본문은 0.
- 크기: 읽는 글 28px 이상, 보조 글 22px 이상.
- 한글 줄바꿈은 낱말 단위(공통 CSS).

## 장의 짜임 (계획안 본문)
모든 본문 장은 같은 순서다: **머리말(`.kicker`, 아래 이중 괘선) → 결론 한 문장 제목(`.title`, 명조) → 도식 1~2개 → 출처(`.src`)**.
- 제목은 결론 문장이다. "현황"(×) → "참여 학교는 늘었지만, 지역 공간과 잇는 학교는 3곳 중 1곳뿐입니다"(○).
- 카드 · 수치 타일은 **상자가 아니라 지면의 단**이다: 위에 이중 괘선, 그림자 · 테두리 없음.
- 막대 · 간트 · 표는 종이 위에 한 장 더 놓은 것처럼 흰 면 + 위 3px 먹선.

## 판 번호(.reg) — 이 계열의 얼굴
- 표지: 큰 명조 연도(남색) + 맞춤 표지(⊕).
- 목차: 12단 눈금(제목 아래) + 맞춤 표지. 목록은 오른쪽 8단, 왼쪽 4단은 비워 둔다.
- 간지: **재단 표시(`.crop`)와 주홍 판 어긋남(번호에 4~6px)은 덱 전체에서 간지에만.**
- 마무리: 맞춤 표지만. 문의는 겹 테두리 공지란.
- 본문 장에는 쓰지 않는다.

## 해야 할 것
1. 장마다 결론 한 문장 제목(명조).
2. 수치에는 단위와 출처.
3. 주홍은 한 장에 한 곳.
4. 괘선은 굵은 3px · 가는 1px 두 가지만.
5. 화면을 채운다. 단이 비면 장을 합친다.

## 하지 말 것
1. 새 색, 그라데이션, 둥근 모서리, 큰 그림자.
2. 카드 · 타일에 상자 테두리나 그림자.
3. 본문 장에 재단 표시 · 판 어긋남.
4. 장 번호 · 쪽 표시 · 점을 손으로 쓰기(엔진이 채운다).
5. 공통 CSS · 엔진을 HTML 안에 옮겨 쓰기, `@font-face` 새로 쓰기.
6. 인라인 `style`은 `--v` · `--from` · `--to`만.

## 새 부품을 만들 때
1. 먼저 `.grid` · `.split` · `.stack`과 기존 부품으로 될지 본다.
2. 새 묶음은 위 이중 괘선으로 시작한다(상자 대신).
3. 숫자는 명조 900 남색, 라벨은 고딕.
4. 강조는 `.is-key` 한 곳, 주홍.

## 알려진 한계 (v1)
- 종이 질감(재생지 섬유 · 망점 · 리소 판 어긋남 전체)은 키트에 없다. 근거 표지(#4 · #32 · #60)의 질감이 필요하면 그 장표를 직접 참고한다.
- 막대는 가로뿐. 세로 막대 · 선 · 도넛 · 지도 부품은 없다.
- 목차 왼쪽 4단의 '한 줄 요약(리드)' 칸은 v1 부품에 없다(#62에는 있음).
````

---

## 2. 글씨체

- 제목 Noto Serif KR(700/900) · 본문 IBM Plex Sans KR(400/600) · 숫자 Noto Serif KR(700/900). 공통 CSS가 불러오므로 설치하지 않아도 됩니다(열 때 인터넷 필요).
- 글꼴은 변수로만 지정합니다: `var(--ds-font-title)` · `var(--ds-font-body)` · `var(--ds-font-num)`(숫자 · 영문에만).

---

## 3. 부품 사전 (이 계열 CSS에 정의된 클래스)

이 목록에 있는 클래스만 씁니다. "예"는 뼈대(4)에서 그 클래스를 처음 쓴 태그입니다. 공용 클래스: `.slide`(장 하나) · `data-steps="n"`(장) + `data-step="k"`(안의 요소, 누를 때마다 하나씩) · `.page-no`(빈 칸, 엔진이 채움).

**공통: 머리말 띠(이중 괘선) · 결론 제목 · 쪽 번호 · 출처**
- `.s-body` — 예: `<div class="s-body">`
- `.kicker` — 예: `<p class="kicker">`
- `.title` — 예: `<h2 class="title">`
- `.lead`
- `.fill` — 예: `<div class="split fill">`
- `.src` — 예: `<p class="src">`
- `.page-no` — 예: `<span class="page-no">`

**판 번호(.reg): 큰 명조 숫자 + 맞춤 표지(⊕). 간지는 재단 표시 + 주홍 판 어긋남**
- `.reg` — 예: `<div class="reg" aria-hidden="true">`
- `.crop` — 예: `<i class="crop">`

**표지: 신문 1면처럼 제호 띠 → 큰 명조 → 날짜 줄**
- `.cover` — 예: `<section class="slide cover">`
- `.c-text` — 예: `<div class="c-text">`
- `.c-tag` — 예: `<span class="c-tag">`
- `.c-sub` — 예: `<p class="c-sub">`
- `.c-org` — 예: `<p class="c-org">`
- `.reg` — 예: `<div class="reg" aria-hidden="true">`

**목차: 12단 눈금 위 지면 안내. 로마 숫자 대신 큰 명조 번호**
- `.toc-list` — 예: `<ol class="toc-list">`
- `.is-now` — 예: `<li class="is-now">`
- `.toc` — 예: `<section class="slide toc">`
- `.reg` — 예: `<div class="reg" aria-hidden="true">`

**간지: 큰 명조 번호에 주홍 판 어긋남 한 곳 + 재단 표시**
- `.divider` — 예: `<section class="slide divider">`
- `.d-no` — 예: `<div class="d-no">`
- `.reg` — 예: `<div class="reg" aria-hidden="true">`

**마무리: 공지란 겹 테두리**
- `.close` — 예: `<section class="slide close">`
- `.reg` — 예: `<div class="reg" aria-hidden="true">`

**배치 격자**
- `.grid` — 예: `<div class="grid g2">`
- `.center` — 예: `<div class="grid g3 fill center">`
- `.g2` — 예: `<div class="grid g2">`
- `.g3` — 예: `<div class="grid g3 fill center">`
- `.g4`
- `.split` — 예: `<div class="split fill">`
- `.stack` — 예: `<div class="fill stack">`

**카드 묶음: 상자 대신 지면의 단(이중 괘선 머리)**
- `.card` — 예: `<div class="card">`
- `.c-no` — 예: `<span class="c-no">`
- `.c-foot` — 예: `<p class="c-foot">`
- `.is-key` — 예: `<div class="tile is-key">`

**수치 타일: 큰 명조 숫자**
- `.tile` — 예: `<div class="tile">`
- `.is-key` — 예: `<div class="tile is-key">`

**막대(가로, 남색 한 판): style="--v:42" 는 최댓값 대비 %**
- `.bars` — 예: `<div class="bars">`
- `.bar` — 예: `<div class="bar" style="--v:69">`
- `.is-key` — 예: `<div class="tile is-key">`

**현안 → 해결**
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.q` — 예: `<p class="q">`
- `.a` — 예: `<p class="a">`
- `.is-key` — 예: `<div class="tile is-key">`

**간트(월 1~12): style="--from:3;--to:6"**
- `.gantt` — 예: `<div class="gantt">`
- `.g-h` — 예: `<span class="g-h">`
- `.g-name` — 예: `<span class="g-name">`
- `.g-bar` — 예: `<i class="g-bar" style="--from:1;--to:3">`
- `.is-key` — 예: `<div class="tile is-key">`

**표: 신문 표(위 굵은 선 · 가는 줄 · 합계 위 이중 괘선)**
- `.tbl` — 예: `<table class="tbl">`
- `.n` — 예: `<td class="n">`
- `.is-key` — 예: `<div class="tile is-key">`

---

## 4. HTML 뼈대 (예시 덱 8장 — 부품 견본입니다. 장 구성은 따라 하지 말고, 공통 파일 두 줄은 그대로 두며, 장은 내용에 맞게 새로)

```html
<!DOCTYPE html>
<html lang="ko" data-kit="D">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>덱 키트 D · 인쇄·종이 에디토리얼 — 예시 덱</title>
<!-- 이 계열의 공통 CSS(글꼴 · 색 · 부품). 이 줄은 지우거나 바꾸지 마세요 -->
<link rel="stylesheet" href="https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/D.css">
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
  <div class="reg" aria-hidden="true"><b>2027</b></div>
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
  <div class="reg" aria-hidden="true"><b>01</b></div>
  <span class="page-no"></span>
</section>

<!-- 3. 간지 -->
<section class="slide divider">
  <div class="d-no"><small>SECTION</small>01</div>
  <h2>현황</h2>
  <p>참여는 늘었지만 학교 밖과 이어지는 수업은 아직 적습니다.</p>
  <div class="reg is-off" aria-hidden="true"><b>01</b><i class="crop"></i></div>
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
  <div class="reg" aria-hidden="true"><b>끝</b></div>
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

부품 모양 · 크기를 이해하는 데만 쓰세요(`https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/D.css`의 계열 부분).

```css
/* D 인쇄·종이 에디토리얼 — 덱 키트 v1 (deck.css 다음에 불러옴)
   밝은 백상지 + 먹 명조 제목 + 남색 주판 · 주홍 별색 2도. 이중 괘선(굵은 3 + 가는 1)과 12단 눈금으로 지면을 짠다.
   판 어긋남 · 재단 표시는 간지에만, 주홍은 한 장에 한 곳.
   근거 장표: #4 · #27 · #32 · #60(표지), #62(목차·간지 키트) */
:root{
  --ds-stage:#E4E1D8;
  --ds-bg:#FBFAF6; --ds-surface:#FFFFFF; --ds-ink:#1B1E24; --ds-sub:#5C606A; --ds-line:#CFCCC4;
  --ds-accent:#D9482B; --ds-accent2:#23467A;
  --ds-c1:#1F3E6E; --ds-c2:#3C5D8C; --ds-c3:#6D87AD; --ds-c4:#A5B5CD; --ds-c5:#D7DEE9;
  --ds-paper2:#F1EEE6;
  --ds-radius:0px; --ds-shadow:0 1px 2px rgba(27,30,36,.08),0 18px 40px -26px rgba(27,30,36,.32);
  --ds-font-title:"Noto Serif KR","Nanum Myeongjo","AppleMyungjo","Batang",serif;
  --ds-font-body:"IBM Plex Sans KR","Noto Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif;
  --ds-font-num:"Noto Serif KR","Nanum Myeongjo","Batang",Georgia,serif;
  --rule2:linear-gradient(var(--ds-ink),var(--ds-ink)) left top/100% 3px no-repeat,linear-gradient(var(--ds-ink),var(--ds-ink)) left 7px/100% 1px no-repeat;
}
.slide{isolation:isolate;background:var(--ds-bg);color:var(--ds-ink);font:400 28px/1.6 var(--ds-font-body)}

/* ── 공통: 머리말 띠(이중 괘선) · 결론 제목 · 쪽 번호 · 출처 ─────────── */
.s-body{position:absolute;inset:80px 120px 96px;display:flex;flex-direction:column;gap:36px}
.kicker{margin:0;padding-bottom:18px;font:600 24px/1 var(--ds-font-body);color:var(--ds-ink);
  background:linear-gradient(var(--ds-ink),var(--ds-ink)) left calc(100% - 5px)/100% 3px no-repeat,linear-gradient(var(--ds-ink),var(--ds-ink)) left bottom/100% 1px no-repeat}
.title{margin:0;max-width:1600px;font:900 58px/1.32 var(--ds-font-title);letter-spacing:-.02em;text-wrap:balance}
.title em{font-style:normal;color:var(--ds-accent)}
.lead{margin:-12px 0 0;max-width:1400px;font-size:28px;color:var(--ds-sub)}
.fill{flex:1;min-height:0}
.src{position:absolute;left:120px;bottom:40px;margin:0;font:400 22px/1 var(--ds-font-body);color:var(--ds-sub)}
.page-no{position:absolute;right:120px;bottom:40px;font:700 24px/1 var(--ds-font-num);color:var(--ds-ink)}

/* ── 판 번호(.reg): 큰 명조 숫자 + 맞춤 표지(⊕). 간지는 재단 표시 + 주홍 판 어긋남 ── */
.reg{position:absolute;pointer-events:none}
.reg b{display:block;font:900 300px/1 var(--ds-font-num);letter-spacing:-.04em;color:var(--ds-c1)}
.reg::after{content:"";position:absolute;width:56px;height:56px;border:2px solid var(--ds-ink);border-radius:50%;
  background:linear-gradient(var(--ds-ink),var(--ds-ink)) center/2px 100% no-repeat,linear-gradient(var(--ds-ink),var(--ds-ink)) center/100% 2px no-repeat}
.reg .crop{position:absolute;inset:-36px;
  background:
    linear-gradient(var(--ds-ink),var(--ds-ink)) 0 36px/28px 1px no-repeat,linear-gradient(var(--ds-ink),var(--ds-ink)) 36px 0/1px 28px no-repeat,
    linear-gradient(var(--ds-ink),var(--ds-ink)) 100% 36px/28px 1px no-repeat,linear-gradient(var(--ds-ink),var(--ds-ink)) calc(100% - 36px) 0/1px 28px no-repeat,
    linear-gradient(var(--ds-ink),var(--ds-ink)) 0 calc(100% - 36px)/28px 1px no-repeat,linear-gradient(var(--ds-ink),var(--ds-ink)) 36px 100%/1px 28px no-repeat,
    linear-gradient(var(--ds-ink),var(--ds-ink)) 100% calc(100% - 36px)/28px 1px no-repeat,linear-gradient(var(--ds-ink),var(--ds-ink)) calc(100% - 36px) 100%/1px 28px no-repeat}

/* ── 표지: 신문 1면처럼 제호 띠 → 큰 명조 → 날짜 줄 ─────────────────── */
.cover .c-text{position:absolute;left:120px;right:120px;top:110px;display:flex;flex-direction:column;gap:32px}
.cover .c-tag{padding-bottom:20px;font:600 24px/1 var(--ds-font-body);color:var(--ds-ink);
  background:linear-gradient(var(--ds-ink),var(--ds-ink)) left calc(100% - 5px)/100% 3px no-repeat,linear-gradient(var(--ds-ink),var(--ds-ink)) left bottom/100% 1px no-repeat}
.cover h1{margin:24px 0 0;max-width:1240px;font:900 104px/1.22 var(--ds-font-title);letter-spacing:-.03em}
.cover h1 em{font-style:normal;color:var(--ds-accent)}
.cover .c-sub{margin:0;max-width:1000px;font:400 34px/1.5 var(--ds-font-title);color:var(--ds-sub)}
.cover .c-org{position:absolute;left:120px;right:120px;bottom:96px;display:flex;gap:40px;margin:0;padding:22px 0;border-top:1px solid var(--ds-ink);border-bottom:1px solid var(--ds-ink);font:600 26px/1.4 var(--ds-font-body)}
.cover .reg{right:150px;bottom:210px}
.cover .reg::after{right:-12px;top:-40px}

/* ── 목차: 12단 눈금 위 지면 안내. 로마 숫자 대신 큰 명조 번호 ───────────── */
.toc-list{list-style:none;margin:0;padding:0;width:1240px;align-self:flex-end;border-top:3px solid var(--ds-ink)}
.toc-list li{display:grid;grid-template-columns:120px 1fr 140px;align-items:center;height:104px;border-bottom:1px solid var(--ds-line);font:700 40px/1.2 var(--ds-font-title)}
.toc-list li b{font:900 48px/1 var(--ds-font-num);color:var(--ds-c1)}
.toc-list li span:last-child{justify-self:end;font:700 28px/1 var(--ds-font-num)}
.toc-list li span:last-child::before{content:"p.";font-size:24px;color:var(--ds-sub)}
.toc-list li.is-now{color:var(--ds-accent)}.toc-list li.is-now b{color:var(--ds-accent)}
.toc .reg{left:120px;right:120px;top:246px;height:14px;
  background:repeating-linear-gradient(90deg,var(--ds-line) 0 1px,transparent 1px calc((1920px - 240px) / 12))}
.toc .reg b{display:none}
.toc .reg::after{left:0;top:200px}

/* ── 간지: 큰 명조 번호에 주홍 판 어긋남 한 곳 + 재단 표시 ──────────────── */
.divider .d-no{position:absolute;left:150px;top:150px;font:900 280px/1 var(--ds-font-num);letter-spacing:-.04em;color:var(--ds-c1);text-shadow:6px 5px 0 rgba(217,72,43,.8)}
.divider .d-no small{display:block;margin-bottom:24px;font:600 24px/1 var(--ds-font-body);letter-spacing:.06em;color:var(--ds-sub);text-shadow:none}
.divider h2{position:absolute;left:150px;top:560px;margin:0;font:900 96px/1.2 var(--ds-font-title);letter-spacing:-.02em}
.divider p{position:absolute;left:150px;top:700px;margin:0;width:1000px;font:400 32px/1.5 var(--ds-font-title);color:var(--ds-sub)}
.divider .reg{left:110px;top:110px;width:1700px;height:860px}
.divider .reg b{display:none}
.divider .reg::after{right:40px;top:40px}

/* ── 마무리: 공지란 겹 테두리 ───────────────────────────── */
.close h2{position:absolute;left:120px;top:330px;margin:0;font:900 96px/1.25 var(--ds-font-title);letter-spacing:-.02em}
.close p{position:absolute;left:120px;top:620px;margin:0;padding:24px 36px;border:4px double var(--ds-ink);font-size:28px}
.close .reg{right:160px;bottom:140px;width:56px;height:56px}
.close .reg b{display:none}
.close .reg::after{left:0;top:0}

/* ── 배치 격자 ─────────────────────────────────────── */
.grid{display:grid;gap:40px;align-items:stretch}
.grid.center{align-content:center}
.grid.g2{grid-template-columns:repeat(2,1fr)}.grid.g3{grid-template-columns:repeat(3,1fr)}.grid.g4{grid-template-columns:repeat(4,1fr)}
.split{display:grid;grid-template-columns:1.35fr 1fr;gap:56px;align-items:stretch}
.stack{display:flex;flex-direction:column;justify-content:center;gap:24px}

/* ── 카드 묶음: 상자 대신 지면의 단(이중 괘선 머리) ─────────────────── */
.card{background:var(--rule2);padding:30px 0 0;display:flex;flex-direction:column;gap:18px;min-width:0;min-height:440px}
.card .c-no{font:600 24px/1 var(--ds-font-body);color:var(--ds-c1)}
.card h3{margin:0;font:900 48px/1.25 var(--ds-font-title);letter-spacing:-.02em}
.card p{margin:0;font-size:28px;line-height:1.6;color:var(--ds-ink)}
.card .c-foot{margin-top:auto;padding-top:20px;border-top:1px solid var(--ds-line);font-size:24px;color:var(--ds-sub)}
.card .c-foot b{font:900 36px/1 var(--ds-font-num);color:var(--ds-c1)}
.card.is-key{background:linear-gradient(var(--ds-accent),var(--ds-accent)) left top/100% 3px no-repeat,linear-gradient(var(--ds-ink),var(--ds-ink)) left 7px/100% 1px no-repeat}
.card.is-key .c-no,.card.is-key .c-foot b{color:var(--ds-accent)}

/* ── 수치 타일: 큰 명조 숫자 ─────────────────────────────── */
.tile{background:var(--rule2);padding:28px 0 0;display:flex;flex-direction:column;gap:12px;min-width:0}
.tile span{font:600 24px/1.2 var(--ds-font-body);color:var(--ds-sub)}
.tile b{font:900 96px/1 var(--ds-font-num);letter-spacing:-.03em;color:var(--ds-c1)}
.tile b small{margin-left:8px;font:600 32px/1 var(--ds-font-body);letter-spacing:0;color:var(--ds-sub)}
.tile p{margin:0;font-size:24px;color:var(--ds-sub)}
.tile.is-key b{color:var(--ds-accent)}

/* ── 막대(가로, 남색 한 판): style="--v:42" 는 최댓값 대비 % ───────────── */
.bars{background:var(--ds-surface);box-shadow:var(--ds-shadow);border-top:3px solid var(--ds-ink);padding:40px;display:flex;flex-direction:column;justify-content:center;gap:44px;min-width:0}
.bars h3{margin:0;font:900 32px/1.3 var(--ds-font-title)}
.bar{display:grid;grid-template-columns:110px 1fr 120px;align-items:center;gap:20px;font-size:28px}
.bar::before{content:"";grid-column:2;grid-row:1;height:56px;width:calc(var(--v) * 1%);background:var(--ds-c3)}
.bar span{grid-column:1;grid-row:1;font:700 30px/1 var(--ds-font-num);color:var(--ds-sub)}
.bar b{grid-column:3;grid-row:1;justify-self:end;font:900 36px/1 var(--ds-font-num);color:var(--ds-c1)}
.bar.is-key::before{background:var(--ds-accent)}.bar.is-key b{color:var(--ds-accent)}

/* ── 현안 → 해결 ───────────────────────────────────── */
.fix{display:grid;grid-template-columns:1fr 72px 1.25fr;gap:0;align-items:stretch}
.fix > p{margin:0;padding:30px 34px;font-size:30px;line-height:1.5}
.fix .q{background:var(--ds-paper2);color:var(--ds-ink)}
.fix .a{background:var(--ds-surface);border:1px solid var(--ds-ink);font-weight:600}
.fix .q b,.fix .a b{display:block;margin-bottom:10px;font:700 24px/1 var(--ds-font-num);color:var(--ds-c1)}
.fix i{position:relative}
.fix i::after{content:"";position:absolute;left:16px;right:16px;top:50%;height:1px;background:var(--ds-ink)}
.fix i::before{content:"";position:absolute;right:14px;top:50%;width:14px;height:14px;margin-top:-7px;border-top:1px solid var(--ds-ink);border-right:1px solid var(--ds-ink);transform:rotate(45deg)}
.fix.is-key .a{border-color:var(--ds-accent);box-shadow:inset 3px 0 0 var(--ds-accent)}

/* ── 간트(월 1~12): style="--from:3;--to:6" ────────────────────── */
.gantt{background:var(--ds-surface);box-shadow:var(--ds-shadow);border-top:3px solid var(--ds-ink);padding:28px 36px;display:grid;grid-template-columns:250px repeat(12,1fr);row-gap:20px;align-items:center;min-width:0}
.gantt .g-h{font:700 24px/1 var(--ds-font-num);color:var(--ds-sub);text-align:center}
.gantt .g-h:first-child{text-align:left;font:600 24px/1 var(--ds-font-body)}
.gantt .g-name{grid-column:1;font-size:26px;line-height:1.3}
.gantt .g-bar{grid-column:calc(var(--from) + 1) / calc(var(--to) + 2);height:28px;background:var(--ds-c3)}
.gantt .g-bar.is-key{background:var(--ds-accent)}

/* ── 표: 신문 표(위 굵은 선 · 가는 줄 · 합계 위 이중 괘선) ─────────────── */
.tbl{width:100%;border-collapse:collapse;background:var(--ds-surface);box-shadow:var(--ds-shadow);border-top:3px solid var(--ds-ink);font-size:28px}
.tbl th{padding:20px 28px;text-align:left;font:600 24px/1.2 var(--ds-font-body);color:var(--ds-sub);border-bottom:1px solid var(--ds-ink)}
.tbl td{padding:18px 28px;border-bottom:1px solid var(--ds-line)}
.tbl td.n{text-align:right;font:900 32px/1 var(--ds-font-num);color:var(--ds-c1)}
.tbl tr.is-key td{color:var(--ds-accent);font-weight:600}.tbl tr.is-key td.n{color:var(--ds-accent)}
.tbl tfoot td{font-weight:700;border-bottom:0;border-top:4px double var(--ds-ink)}
```
