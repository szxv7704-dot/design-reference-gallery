# A 픽셀 게임 — 계획안 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **ChatGPT · Claude · Gemini 같은 채팅 AI**에게 통째로 주면, 이 디자인으로 계획안 발표 덱을 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 A 계열 장표(#9 · #10 · #11 · #12 · #90)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일을 첨부**합니다(안 되면 내용을 끝까지 복사해 붙여 넣기).
2. 만들 계획안을 말합니다. 예) "2027 ○○ 지원 계획(안), ○○교육청 ○○과. 현황 수치는 아래 표(출처: ○○ 통계), 세부과제 3개는 … 덱으로 만들어 줘. 결과는 .html 파일로."
3. AI가 먼저 **장별 구성안**(머리말 · 결론 제목 · 부품 · 수치와 출처)을 보여 줍니다. 고칠 곳을 말하거나 "좋아, 만들어 줘".
4. 받은 `슬라이드.html`을 내려받아 더블클릭합니다. → · Space로 넘기고, F는 전체 화면, 인쇄하면 장마다 한 쪽(16:9) PDF가 됩니다.
5. 고칠 곳은 "3장 제목을 ○○로"처럼 말합니다. 코드가 끊기면 "끊긴 곳부터 이어서".

알아 둘 점
- 열 때 **인터넷이 필요**합니다(공통 CSS · 엔진 · 글꼴을 `szxv7704-dot.github.io`에서 불러옴). 업무망처럼 인터넷이 막힌 곳에서 발표하려면 저장소에서 `python3 scripts/kit.py inline A 슬라이드.html`을 실행해 모든 것이 파일 안에 든 판을 만드세요.
- AI 화면 안의 미리보기에서는 색 · 모양이 안 나올 수 있습니다. 내려받아 브라우저(크롬 · 엣지)로 열면 정상입니다.
- 수치는 AI가 지어내지 않도록 계약에 적어 두었지만, **받은 덱의 숫자를 원자료와 꼭 대조**하세요.
- 개인정보(학생 이름 · 사진 등)는 AI에게 넣지 마세요.

## 라이선스

- 글꼴: 모두 SIL Open Font License 1.1(전문 https://szxv7704-dot.github.io/design-reference-gallery/fonts/OFL.txt). 이 계열이 쓰는 글꼴의 저작권 고지:

| 글꼴 | 굵기 | 저작권 | 예약 이름 | 라이선스 |
|---|---|---|---|---|
| Galmuri11 | 400 · 700 | Copyright (c) 2019-2025 Lee Minseo (quiple@quiple.dev) | — | SIL OFL 1.1 |

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
- 표지 · 목차 · 간지 · 마무리에는 이 계열의 상징 부품인 진행 칸(`.prog`)을 씁니다. 칸 수 = 섹션 수, 목차는 다음 칸 `.next`, 간지는 지난 칸 `.done` · 지금 칸 `.now`, 마무리는 모두 `.done`.
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

## 1. 디자인 규칙 (`A` design.md)

````markdown
---
kit: A
name: 픽셀 게임
version: v1
stage: 1920x1080
dot: 4px              # 한 도트 = 4px. 선 · 테 · 간격 · 그림자는 모두 4의 배수
colors:
  bg: "#F1EBDC"       # 크림 바탕(낮)
  surface: "#1D2B53"  # 게임 창 안(남색)
  ink: "#1D1B2E"      # 바탕 위 글자 · 창 바깥 테
  sub: "#5E5870"      # 바탕 위 보조 글자 · 점선
  window-text: "#F7F2E4"  # 창 안 글자 · 창 안테
  window-sub: "#A9C8F5"   # 창 안 보조 글자
  head: "#2F4C8C"     # 창 머리줄 · 점선 구분
  accent: "#D23B52"   # 바탕 위 강조(제목 한 낱말)
  hi: "#FFCF4A"       # 창 안 강조(금색 선택 한 곳)
fonts:
  all: "Galmuri11 400/700"   # 제목 · 본문 · 숫자 모두
  sizes: "22 · 33 · 44 · 55 · 77 · 88 · 220px (11의 배수)"
space: {side: 120px, top: 80px, bottom: 96px, gap: 36px}
radius: 0
shadow: none
---

## 분위기
밝은 크림 바탕 위에 남색 게임 창이 뜬다. 16비트 RPG의 대화창 · 메뉴 · 진행 칸으로 계획안을 읽게 한다.
- 정보는 모두 **게임 창** 안에 둔다(카드 · 수치 타일 · 막대 판 · 간트 · 표). 창 밖 크림 바탕에는 머리말 · 제목 · 출처만.
- 강조는 두 자리뿐이고 **같은 내용**을 가리킨다: 바탕 위 제목의 한 낱말은 빨강(`<em>`), 창 안의 선택 한 곳은 금색(`.is-key`).
- 근거 장표: 표지 #9 · #10 · #11 · #12, 목차 · 간지 키트 #90.

## 색의 역할
| 이름 | 쓰는 곳 | 쓰지 않는 곳 |
|---|---|---|
| bg | 모든 장의 바탕 | 창 안 |
| surface(남색) | 게임 창 안 | 넓은 바탕 |
| ink | 바탕 위 글자, 창 바깥 테 | 창 안 글자 |
| window-text · window-sub | 창 안 글자 · 보조 글자 | 바탕 위 |
| head | 창 머리줄(디더), 창 안 점선 | 글자 |
| accent(빨강) | 바탕 위 강조 한 곳 | 창 안 |
| hi(금색) | 창 안 강조 한 곳, 진행 칸의 지금 · 다음 칸 | 바탕 위 글자 |

새 색을 만들지 않는다. 16색 제한이 이 계열의 맛이다.

## 글자
- **Galmuri11 하나로** 제목 · 본문 · 숫자를 모두 쓴다(픽셀 글꼴). 굵기는 400(본문)과 700(제목 · 라벨)뿐.
- **크기는 11의 배수**: 22(보조) · 33(본문) · 44(카드 제목) · 55(장 제목) · 77(간지) · 88(표지 · 수치) · 220(간지 번호). 11의 배수가 아니면 도트가 뭉개진다.
- 읽는 글은 33px 이상, 보조 글은 22px 이상.
- 자간은 0. 글꼴을 바꾸지 않는다(픽셀 글꼴과 매끈한 글꼴을 섞지 않는다).
- 한글 줄바꿈은 낱말 단위(공통 CSS).

## 장의 짜임 (계획안 본문)
모든 본문 장은 같은 순서다: **머리말(`.kicker`, 아래 점선) → 결론 한 문장 제목(`.title`) → 창 1~2개 → 출처(`.src`)**.
- 제목은 결론 문장이다. "현황"(×) → "참여 학교는 늘었지만, 지역 공간과 잇는 학교는 3곳 중 1곳뿐입니다"(○).
- 창 하나에 메시지 하나. 창 머리줄(`.c-no` · `h3`)에 그 창이 무엇인지 쓴다.

## 게임 창
- 먹 테(4px) + 남색 안 + 크림 안테(4px) + 모서리 한 도트 깎기. 공통 부품 CSS가 그린다.
- 머리줄: 왼쪽 단색 · 오른쪽 체크 무늬 디더(카드 · 막대 판).
- 창 안 구분선은 점선(4px 간격). 실선을 쓰지 않는다.
- 막대 · 간트는 칸으로 끊긴 체력 막대 모양이다.

## 진행 칸(.prog) — 이 계열의 얼굴
- 표지 · 목차 · 간지 · 마무리에만 쓴다. 칸 수 = 섹션 수(최대 5), 칸 아래 로마 숫자는 자동.
- 표지: 모두 빈 칸 / 목차: 다음 칸 `.next`(금색 테) / 간지: 지난 칸 `.done`(남색 채움) · 지금 칸 `.now`(금색 채움) / 마무리: 모두 `.done`.
- 본문 장에는 쓰지 않는다.

## 커서와 기호
- ▶ = 지금 고른 것(목차 지금 줄, 표지 머리말), ▼ = 계속(간지 설명 끝, 표지 대화창). 공통 CSS가 붙인다. 다른 기호를 더하지 않는다.

## 해야 할 것
1. 장마다 결론 한 문장 제목.
2. 정보는 창 안에, 창마다 머리줄.
3. 강조는 빨강(바탕) · 금색(창) 각각 한 곳, 같은 내용.
4. 글자 크기는 11의 배수.
5. 화면을 채운다. 창이 작게 몰리면 창을 키우거나 장을 합친다.

## 하지 말 것
1. 새 색, 그라데이션, 흐린 그림자, 둥근 모서리.
2. Galmuri11 말고 다른 글꼴, 11의 배수가 아닌 글자 크기.
3. 창 밖 바탕에 정보 상자 늘어놓기.
4. 장 번호 · 쪽 표시 · 점을 손으로 쓰기(엔진이 채운다).
5. 공통 CSS · 엔진을 HTML 안에 옮겨 쓰기, `@font-face` 새로 쓰기.
6. 인라인 `style`은 `--v` · `--from` · `--to`만.

## 새 부품을 만들 때
1. 먼저 `.grid` · `.split` · `.stack`과 기존 창으로 될지 본다.
2. 새 상자는 게임 창 규칙(먹 테 · 남색 · 크림 안테 · 모서리 깎기)을 그대로 쓴다.
3. 모든 길이는 4px(한 도트)의 배수, 글자는 11의 배수.
4. 강조는 `.is-key` 한 곳, 창 안이면 금색.

## 알려진 한계 (v1)
- 도트 그림(캐릭터 · 지도 · 아이템)은 키트에 없다. 근거 표지(#9~#12)처럼 그림이 필요하면 SVG로 4px 격자에 맞춰 그리되 16색 안에서.
- 막대는 가로뿐. 세로 막대 · 선 · 도넛 · 지도 부품은 없다.
- Galmuri11은 KS X 1001 한글 2,350자 범위(갤러리 글꼴 파일 기준)라 드문 글자는 대체 글꼴로 보인다.
- 밤 색(#9 표지 색) 바꿔 보기는 아직 키트에 없다(#90 장표에는 있음).
````

---

## 2. 글씨체

- 모든 글자(제목 · 본문 · 숫자) Galmuri11(400/700). 공통 CSS가 불러오므로 설치하지 않아도 됩니다(열 때 인터넷 필요).
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

**게임 창: 먹 테 + 크림 안테 + 모서리 깎기 + 디더 머리줄. 카드 · 타일 · 막대 판 · 간트 · 표가 모두 이 창**
- `.card` — 예: `<div class="card">`
- `.tile` — 예: `<div class="tile">`
- `.bars` — 예: `<div class="bars">`
- `.gantt` — 예: `<div class="gantt">`
- `.tbl` — 예: `<table class="tbl">`
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.a` — 예: `<p class="a">`
- `.toc-list` — 예: `<ol class="toc-list">`
- `.win-head`
- `.c-no` — 예: `<span class="c-no">`

**진행 칸: 칸 수 = 섹션 수. .done 지남(채움) · .now 지금(금색 테) · .next 다음(금색 테)**
- `.prog` — 예: `<div class="prog" aria-hidden="true">`
- `.done` — 예: `<i class="done">`
- `.now` — 예: `<i class="now">`
- `.next` — 예: `<i class="next">`

**표지**
- `.cover` — 예: `<section class="slide cover">`
- `.c-text` — 예: `<div class="c-text">`
- `.c-tag` — 예: `<span class="c-tag">`
- `.c-sub` — 예: `<p class="c-sub">`
- `.c-org` — 예: `<p class="c-org">`
- `.prog` — 예: `<div class="prog" aria-hidden="true">`

**목차: 남색 창 안 줄 목록, 지금 장은 금색 테 + ▶ 커서**
- `.toc-list` — 예: `<ol class="toc-list">`
- `.is-now` — 예: `<li class="is-now">`
- `.toc` — 예: `<section class="slide toc">`
- `.prog` — 예: `<div class="prog" aria-hidden="true">`

**간지: 큰 번호 + 섹션 이름 + 진행 칸**
- `.divider` — 예: `<section class="slide divider">`
- `.d-no` — 예: `<div class="d-no">`
- `.prog` — 예: `<div class="prog" aria-hidden="true">`

**마무리**
- `.close` — 예: `<section class="slide close">`
- `.prog` — 예: `<div class="prog" aria-hidden="true">`

**배치 격자**
- `.grid` — 예: `<div class="grid g2">`
- `.center` — 예: `<div class="grid g3 fill center">`
- `.g2` — 예: `<div class="grid g2">`
- `.g3` — 예: `<div class="grid g3 fill center">`
- `.g4`
- `.split` — 예: `<div class="split fill">`
- `.stack` — 예: `<div class="fill stack">`

**카드 묶음(창 하나 = 카드 하나)**
- `.card` — 예: `<div class="card">`
- `.c-no` — 예: `<span class="c-no">`
- `.c-foot` — 예: `<p class="c-foot">`
- `.is-key` — 예: `<div class="tile is-key">`

**수치 타일**
- `.tile` — 예: `<div class="tile">`
- `.is-key` — 예: `<div class="tile is-key">`

**막대: 칸으로 끊긴 체력 막대. style="--v:42" 는 최댓값 대비 %**
- `.bars` — 예: `<div class="bars">`
- `.bar` — 예: `<div class="bar" style="--v:69">`
- `.is-key` — 예: `<div class="tile is-key">`

**현안 → 해결: 왼쪽은 크림 쪽지, 오른쪽은 남색 창**
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

**표**
- `.tbl` — 예: `<table class="tbl">`
- `.n` — 예: `<td class="n">`
- `.is-key` — 예: `<div class="tile is-key">`

---

## 4. HTML 뼈대 (예시 덱 8장 — 부품 견본입니다. 장 구성은 따라 하지 말고, 공통 파일 두 줄은 그대로 두며, 장은 내용에 맞게 새로)

```html
<!DOCTYPE html>
<html lang="ko" data-kit="A">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>덱 키트 A · 픽셀 게임 — 예시 덱</title>
<!-- 이 계열의 공통 CSS(글꼴 · 색 · 부품). 이 줄은 지우거나 바꾸지 마세요 -->
<link rel="stylesheet" href="https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/A.css">
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
  <div class="prog" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
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
  <div class="prog" aria-hidden="true"><i class="next"></i><i></i><i></i><i></i><i></i></div>
  <span class="page-no"></span>
</section>

<!-- 3. 간지 -->
<section class="slide divider">
  <div class="d-no"><small>SECTION</small>01</div>
  <h2>현황</h2>
  <p>참여는 늘었지만 학교 밖과 이어지는 수업은 아직 적습니다.</p>
  <div class="prog" aria-hidden="true"><i class="now"></i><i></i><i></i><i></i><i></i></div>
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
  <div class="prog" aria-hidden="true"><i class="done"></i><i class="done"></i><i class="done"></i><i class="done"></i><i class="done"></i></div>
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

부품 모양 · 크기를 이해하는 데만 쓰세요(`https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/A.css`의 계열 부분).

```css
/* A 픽셀 게임 — 덱 키트 v1 (deck.css 다음에 불러옴)
   밝은 크림 바탕 위 남색 게임 창. 글자는 모두 Galmuri11(11의 배수 크기로 또렷하게).
   강조는 제목 한 낱말(빨강)과 창 안 금색 선택 한 곳 — 둘은 같은 내용을 가리킨다.
   근거 장표: #9 · #10 · #11 · #12(표지), #90(목차·간지 키트) */
:root{
  --ds-stage:#D8D0BC;
  --ds-bg:#F1EBDC; --ds-surface:#1D2B53; --ds-ink:#1D1B2E; --ds-sub:#5E5870; --ds-line:#CFC4A6;
  --ds-accent:#D23B52; --ds-hi:#FFCF4A;
  --ds-c1:#1D2B53; --ds-c2:#2F4C8C; --ds-c3:#5A82D0; --ds-c4:#A9C8F5; --ds-c5:#F7F2E4;
  --ds-radius:0px; --ds-shadow:none; --px:4px;
  --ds-font-title:"Galmuri11","DotGothic16","Malgun Gothic",monospace;
  --ds-font-body:"Galmuri11","DotGothic16","Malgun Gothic",monospace;
  --ds-font-num:"Galmuri11","DotGothic16","Malgun Gothic",monospace;
}
.slide{isolation:isolate;background:var(--ds-bg);color:var(--ds-ink);font:400 33px/1.5 var(--ds-font-body);-webkit-font-smoothing:none}

/* ── 공통: 머리말 · 결론 제목 · 쪽 번호 · 출처 ─────────────────── */
.s-body{position:absolute;inset:80px 120px 96px;display:flex;flex-direction:column;gap:36px}
.kicker{margin:0;padding-bottom:16px;font:700 22px/1 var(--ds-font-body);color:var(--ds-ink);
  background:repeating-linear-gradient(90deg,var(--ds-sub) 0 var(--px),transparent var(--px) calc(var(--px) * 2)) left bottom/100% var(--px) no-repeat}
.title{margin:0;max-width:1600px;font:700 55px/1.4 var(--ds-font-title);text-wrap:balance}
.title em{font-style:normal;color:var(--ds-accent)}
.lead{margin:-12px 0 0;max-width:1400px;font-size:33px;color:var(--ds-sub)}
.fill{flex:1;min-height:0}
.src{position:absolute;left:120px;bottom:40px;margin:0;font:400 22px/1 var(--ds-font-body);color:var(--ds-sub)}
.page-no{position:absolute;right:120px;bottom:40px;font:400 22px/1 var(--ds-font-num);color:var(--ds-sub)}

/* ── 게임 창: 먹 테 + 크림 안테 + 모서리 깎기 + 디더 머리줄. 카드 · 타일 · 막대 판 · 간트 · 표가 모두 이 창 ── */
.card,.tile,.bars,.gantt,.tbl,.fix .a,.toc-list{
  background:var(--ds-surface);color:var(--ds-c5);border:var(--px) solid var(--ds-ink);
  box-shadow:inset 0 0 0 var(--px) var(--ds-c1),inset 0 0 0 calc(var(--px) * 2) var(--ds-c5);
  clip-path:polygon(var(--px) 0,calc(100% - var(--px)) 0,100% var(--px),100% calc(100% - var(--px)),calc(100% - var(--px)) 100%,var(--px) 100%,0 calc(100% - var(--px)),0 var(--px))}
/* 창 머리줄: 왼쪽 단색 + 오른쪽 디더(체크 무늬) */
.win-head,.card .c-no,.bars h3{display:block;margin:0;padding:14px 24px;font:700 22px/1 var(--ds-font-body);color:var(--ds-c5);
  background:linear-gradient(90deg,var(--ds-c2) 58%,transparent 58%),repeating-conic-gradient(var(--ds-c2) 0 25%,var(--ds-c1) 0 50%) 0 0/calc(var(--px) * 2) calc(var(--px) * 2)}

/* ── 진행 칸: 칸 수 = 섹션 수. .done 지남(채움) · .now 지금(금색 테) · .next 다음(금색 테) ── */
.prog{display:flex;align-items:center;counter-reset:p}
.prog i{position:relative;width:64px;height:64px;border:var(--px) solid var(--ds-c1);background:var(--ds-c5);counter-increment:p}
.prog i + i{margin-left:56px}
.prog i + i::before{content:"";position:absolute;right:calc(100% + var(--px));top:50%;width:56px;height:var(--px);margin-top:calc(var(--px) / -2);background:var(--ds-c1)}
.prog i::after{content:counter(p,upper-roman);position:absolute;left:50%;top:calc(100% + 16px);transform:translateX(-50%);font:400 22px/1 var(--ds-font-num);color:var(--ds-sub)}
.prog i.done{background:var(--ds-c1)}
.prog i.now,.prog i.next{border-color:var(--ds-hi);outline:var(--px) solid var(--ds-c1);outline-offset:0}
.prog i.now{background:var(--ds-hi)}
.prog i.now::after{color:var(--ds-ink);font-weight:700}

/* ── 표지 ─────────────────────────────────────────── */
.cover .c-text{position:absolute;left:120px;top:150px;width:1500px;display:flex;flex-direction:column;gap:32px}
.cover .c-tag{font:700 22px/1 var(--ds-font-body);color:var(--ds-sub)}
.cover .c-tag::before{content:"▶ ";color:var(--ds-accent)}
.cover h1{margin:0;font:700 88px/1.3 var(--ds-font-title)}
.cover h1 em{font-style:normal;color:var(--ds-accent)}
.cover .c-sub{margin:0;font-size:33px;color:var(--ds-sub);max-width:1100px}
/* 기관 · 날짜 줄은 게임 대화창: 남색 창 + ▼(계속) */
.cover .c-org{position:absolute;left:120px;bottom:96px;width:1000px;display:flex;gap:44px;margin:0;padding:36px 44px;font:700 33px/1.4 var(--ds-font-body);
  background:var(--ds-surface);color:var(--ds-c5);border:var(--px) solid var(--ds-ink);box-shadow:inset 0 0 0 var(--px) var(--ds-c1),inset 0 0 0 calc(var(--px) * 2) var(--ds-c5)}
.cover .c-org::after{content:"▼";margin-left:auto;color:var(--ds-hi)}
.cover .prog{position:absolute;right:160px;bottom:150px}

/* ── 목차: 남색 창 안 줄 목록, 지금 장은 금색 테 + ▶ 커서 ────────────── */
.toc-list{list-style:none;margin:0;padding:20px 28px;width:1080px}
.toc-list li{position:relative;display:grid;grid-template-columns:88px 1fr 110px;align-items:center;height:104px;padding:0 24px;font:700 33px/1.2 var(--ds-font-title);
  background:repeating-linear-gradient(90deg,var(--ds-c2) 0 var(--px),transparent var(--px) calc(var(--px) * 2)) left bottom/100% var(--px) no-repeat}
.toc-list li:last-child{background:none}
.toc-list li b{font:700 33px/1 var(--ds-font-num);color:var(--ds-c4)}
.toc-list li span:last-child{justify-self:end;font:400 22px/1 var(--ds-font-num);color:var(--ds-c4)}
.toc-list li.is-now{color:var(--ds-hi);box-shadow:inset 0 0 0 var(--px) var(--ds-hi)}
.toc-list li.is-now b{color:var(--ds-hi)}
.toc-list li.is-now::before{content:"▶";position:absolute;left:-24px;color:var(--ds-c5);font-size:22px}
.toc .prog{position:absolute;right:110px;bottom:190px}

/* ── 간지: 큰 번호 + 섹션 이름 + 진행 칸 ─────────────────────── */
.divider .d-no{position:absolute;left:120px;top:170px;font:700 220px/1 var(--ds-font-num);color:var(--ds-c1)}
.divider .d-no small{display:block;margin-bottom:28px;font-size:22px;font-weight:700;color:var(--ds-sub)}
.divider h2{position:absolute;left:120px;top:540px;margin:0;font:700 77px/1.2 var(--ds-font-title)}
.divider p{position:absolute;left:120px;top:670px;margin:0;width:1100px;font-size:33px;color:var(--ds-sub)}
.divider p::after{content:" ▼";color:var(--ds-accent)}
.divider .prog{position:absolute;right:150px;bottom:180px}

/* ── 마무리 ────────────────────────────────────────── */
.close h2{position:absolute;left:120px;top:330px;margin:0;font:700 88px/1.3 var(--ds-font-title)}
.close p{position:absolute;left:120px;top:600px;margin:0;font-size:22px;color:var(--ds-sub)}
.close .prog{position:absolute;right:150px;top:450px}

/* ── 배치 격자 ─────────────────────────────────────── */
.grid{display:grid;gap:36px;align-items:stretch}
.grid.center{align-content:center}
.grid.g2{grid-template-columns:repeat(2,1fr)}.grid.g3{grid-template-columns:repeat(3,1fr)}.grid.g4{grid-template-columns:repeat(4,1fr)}
.split{display:grid;grid-template-columns:1.35fr 1fr;gap:44px;align-items:stretch}
.stack{display:flex;flex-direction:column;justify-content:center;gap:28px}

/* ── 카드 묶음(창 하나 = 카드 하나) ───────────────────────────── */
.card{padding:8px 8px 36px;display:flex;flex-direction:column;gap:18px;min-width:0;min-height:440px}
.card > :not(.c-no){margin-left:32px;margin-right:32px}
.card h3{margin-top:12px;margin-bottom:0;font:700 44px/1.3 var(--ds-font-title);color:var(--ds-c5)}
.card p{margin:0;font-size:33px;line-height:1.45;color:var(--ds-c5)}
.card .c-foot{margin-top:auto;padding-top:20px;font-size:22px;color:var(--ds-c4);
  background:repeating-linear-gradient(90deg,var(--ds-c2) 0 var(--px),transparent var(--px) calc(var(--px) * 2)) left top/100% var(--px) no-repeat}
.card .c-foot b{font:700 33px/1 var(--ds-font-num);color:var(--ds-c5)}
.card.is-key{border-color:var(--ds-hi)}.card.is-key .c-foot b{color:var(--ds-hi)}

/* ── 수치 타일 ─────────────────────────────────────── */
.tile{padding:32px 36px;display:flex;flex-direction:column;gap:14px;min-width:0}
.tile span{font-size:22px;color:var(--ds-c4)}
.tile b{font:700 88px/1 var(--ds-font-num);color:var(--ds-c5)}
.tile b small{margin-left:8px;font-size:33px;font-weight:400;color:var(--ds-c4)}
.tile p{margin:0;font-size:22px;color:var(--ds-c4)}
.tile.is-key{border-color:var(--ds-hi)}.tile.is-key b{color:var(--ds-hi)}

/* ── 막대: 칸으로 끊긴 체력 막대. style="--v:42" 는 최댓값 대비 % ───────── */
.bars{padding:8px 8px 40px;display:flex;flex-direction:column;justify-content:flex-start;gap:44px;min-width:0}
.bars h3{align-self:stretch}
.bar{display:grid;grid-template-columns:110px 1fr 110px;align-items:center;gap:20px;margin:0 32px;font-size:22px}
.bar::before{content:"";grid-column:2;grid-row:1;height:44px;width:calc(var(--v) * 1%);
  background:repeating-linear-gradient(90deg,var(--ds-c4) 0 20px,transparent 20px 24px)}
.bar span{grid-column:1;grid-row:1;color:var(--ds-c4)}
.bar b{grid-column:3;grid-row:1;justify-self:end;font:700 33px/1 var(--ds-font-num);color:var(--ds-c5)}
.bar.is-key::before{background:repeating-linear-gradient(90deg,var(--ds-hi) 0 20px,transparent 20px 24px)}.bar.is-key b{color:var(--ds-hi)}
.bars h3 + .bar{margin-top:36px}

/* ── 현안 → 해결: 왼쪽은 크림 쪽지, 오른쪽은 남색 창 ───────────────── */
.fix{display:grid;grid-template-columns:1fr 80px 1.25fr;gap:0;align-items:stretch}
.fix > p{margin:0;padding:30px 36px;font-size:33px;line-height:1.4}
.fix .q{background:#E6DDC6;color:var(--ds-ink);border:var(--px) dashed var(--ds-sub)}
.fix .a{color:var(--ds-c5)}
.fix .q b,.fix .a b{display:block;margin-bottom:10px;font:700 22px/1 var(--ds-font-body)}
.fix .q b{color:var(--ds-sub)}.fix .a b{color:var(--ds-c4)}
.fix i{position:relative}
.fix i::after{content:"▶";position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);text-align:center;font-size:33px;color:var(--ds-ink)}
.fix.is-key .a{border-color:var(--ds-hi)}.fix.is-key .a b{color:var(--ds-hi)}

/* ── 간트(월 1~12): style="--from:3;--to:6" ────────────────────── */
.gantt{padding:28px 32px;display:grid;grid-template-columns:240px repeat(12,1fr);row-gap:20px;align-items:center;min-width:0}
.gantt .g-h{font:400 22px/1 var(--ds-font-num);color:var(--ds-c4);text-align:center}
.gantt .g-h:first-child{text-align:left}
.gantt .g-name{grid-column:1;font-size:22px;line-height:1.3;color:var(--ds-c5)}
.gantt .g-bar{grid-column:calc(var(--from) + 1) / calc(var(--to) + 2);height:28px;background:repeating-linear-gradient(90deg,var(--ds-c3) 0 20px,transparent 20px 24px)}
.gantt .g-bar.is-key{background:repeating-linear-gradient(90deg,var(--ds-hi) 0 20px,transparent 20px 24px)}

/* ── 표 ────────────────────────────────────────────── */
.tbl{width:100%;border-collapse:separate;border-spacing:0;font-size:33px}
.tbl th{padding:22px 32px 18px;text-align:left;font:700 22px/1.2 var(--ds-font-body);color:var(--ds-c4)}
.tbl td{padding:18px 32px;background:repeating-linear-gradient(90deg,var(--ds-c2) 0 var(--px),transparent var(--px) calc(var(--px) * 2)) left top/100% var(--px) no-repeat}
.tbl td.n{text-align:right;font:700 33px/1 var(--ds-font-num)}
.tbl tr.is-key td{color:var(--ds-hi)}
.tbl tfoot td{background:var(--ds-c2);color:var(--ds-c5);font-weight:700}
```
