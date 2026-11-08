# A 픽셀 게임 — 성과 공유회 · 설명회 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **ChatGPT · Claude · Gemini 같은 채팅 AI**에게 통째로 주면, 이 디자인으로 사업 성과 공유회 · 사업 설명회 발표 덱을 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 A 계열 장표(#9 · #10 · #11 · #12 · #90)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일을 첨부**합니다(안 되면 내용을 끝까지 복사해 붙여 넣기).
2. 만들 발표를 말합니다. 예) "2026 ○○ 사업 성과 공유회, ○○교육청 ○○과. 핵심 성과는 아래 표(출처: ○○ 실적), 우수 사례 3개는 … 덱으로 만들어 줘. 결과는 .html 파일로." 사례 사진이 있으면 함께 올립니다.
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

당신은 **사업 성과 공유회 · 사업 설명회** 발표 덱 제작 도우미입니다. 사용자가 준 사업 내용과 성과로, 아래 **디자인 규칙(1)** · **부품 사전(3)** · **HTML 뼈대(4)**를 지켜 **브라우저에서 바로 열리는 덱 HTML 파일 하나**를 만듭니다.
공통 CSS(글꼴 · 색 · 부품 모양)와 동작 엔진은 뼈대의 `<link>` · `<script src>` 두 줄이 불러옵니다. **당신이 쓰는 것은 `<section class="slide">`들과, 꼭 필요할 때만 '추가 부품' CSS뿐입니다.**

### 진행 순서
1. 사용자가 아직 말하지 않았다면 짧게 묻습니다: 성과 공유회인지 설명회인지, 사업 이름 · 기관(부서) · 날짜, 섹션별 핵심 내용, **쓸 수치와 그 출처**, 우수 사례(학교 · 한 줄 성과 · 인용), 사례 사진이 있는지, 원하는 장 수(없으면 내용에 맞게).
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
10. 인라인 `style`은 막대 값(`style="--v:42"`, 가장 큰 값 = 100) · 목표선(`--t`) · 간트 기간(`style="--from:3;--to:6"`, 1~12월)에만 씁니다. 만족도 막대는 `<i style="--v:%">` 다섯 개(합 100).
11. **그림을 코드로 그리지 않습니다.** SVG · CSS · 캔버스로 사물 · 인물 · 풍경 · 캐릭터를 그리지 마세요. 그림이 필요하면 만들지 말고 **사용자에게 이미지를 요청**합니다(무엇 · 쓰는 자리 · 비율 · 배경). 사진은 `.ph` 자리에 사용자가 준 이미지를 `<img>`로 넣고, 아직 없으면 `<div class="ph" data-need="사진 자리 · 4:3 · 무슨 장면"></div>`로 자리만 둡니다. 막대 · 표 같은 데이터 도식은 부품 CSS로 만듭니다.

### 구성은 내용이 정합니다
- 뼈대(4)의 13장은 **부품 견본**입니다. 장 순서 · 장 수 · 문장을 따라 하지 마세요. 예시 문구는 하나도 남기지 않습니다.
- **성과 공유회** 흐름: 사업 개요(`.brief`) → 추진 경과(`.mile`) → 핵심 성과(`.tile` + `.delta`) · 목표 대비 달성(`.goal`) · 만족도(`.likert`) · 전후 비교(`.ba`) → 우수 사례 · 참여자 목소리(`.case`) → 시사점(`.fix`) → 향후 계획(`.road`). **사업 설명회** 흐름: 사업 개요 → 지원 내용(`.tbl`) → 신청 자격 · 절차 → 주요 일정(`.mile`) → 유의사항 → 문의. 내용이 없는 자리는 빼고 목차도 그에 맞춥니다.
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
4. 쓴 클래스가 모두 부품 사전(3) 또는 '추가 부품' 칸에 있는가? 인라인 style은 `--v` · `--t` · `--from` · `--to`뿐인가? 코드로 그린 그림(SVG · CSS 도형)이 없는가?
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
밝은 크림 바탕 위에 남색 게임 창이 뜬다. 16비트 RPG의 대화창 · 메뉴 · 진행 칸으로 사업의 1년을 읽게 한다.
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

## 장의 짜임 (성과 공유회 · 설명회 본문)
모든 본문 장은 같은 순서다: **머리말(`.kicker`, 아래 점선) → 결론 한 문장 제목(`.title`) → 창 1~2개 → 출처(`.src`)**.
- 제목은 결론 문장이다. "핵심 성과"(×) → "참여 학교 138교, 연계 수업 1,240회가 열렸습니다"(○).
- 머리말은 덱 목차와 같은 말을 쓴다. 성과 공유회: 01 사업 개요 · 02 추진 경과 · 03 핵심 성과 · 04 우수 사례 · 05 시사점 · 향후 계획.
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

## 성과 공유회 부품(공용 parts.css)
사업 개요 `.brief` · 추진 경과 `.mile` · 증감 `.delta` · 목표 대비 달성 `.goal` · 만족도 `.likert` · 전후 비교 `.ba` · 우수 사례 `.case`(사진 `.ph` + 목소리) · 향후 계획 `.road`. 모양은 이 계열의 토큰을 따른다.
- **그림을 코드로 그리지 않는다.** 사물 · 인물 · 풍경 · 캐릭터가 필요하면 사용자에게 이미지를 요청하고, 사진은 `.ph` 자리에 넣는다(docs/criteria.md 4).

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
6. 인라인 `style`은 `--v` · `--t` · `--from` · `--to`만.
7. 사물 · 인물 · 풍경을 SVG · CSS로 그리기(이미지를 요청한다).

## 새 부품을 만들 때
1. 먼저 `.grid` · `.split` · `.stack`과 기존 창으로 될지 본다.
2. 새 상자는 게임 창 규칙(먹 테 · 남색 · 크림 안테 · 모서리 깎기)을 그대로 쓴다.
3. 모든 길이는 4px(한 도트)의 배수, 글자는 11의 배수.
4. 강조는 `.is-key` 한 곳, 창 안이면 금색.

## 알려진 한계 (v1)
- 도트 그림(캐릭터 · 지도 · 아이템)은 키트에 없고 코드로 그리지 않는다. 필요하면 16색 도트 이미지를 사용자에게 요청한다.
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
- `.fill` — 예: `<div class="brief fill">`
- `.src` — 예: `<p class="src">`
- `.page-no` — 예: `<span class="page-no">`

**게임 창: 먹 테 + 크림 안테 + 모서리 깎기 + 디더 머리줄. 카드 · 타일 · 막대 판 · 간트 · 표가 모두 이 창**
- `.card`
- `.tile` — 예: `<div class="tile is-key">`
- `.bars`
- `.gantt`
- `.tbl`
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.a` — 예: `<p class="a">`
- `.toc-list` — 예: `<ol class="toc-list">`
- `.win-head`
- `.c-no`

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
- `.grid` — 예: `<div class="grid g4 fill center">`
- `.center` — 예: `<div class="grid g4 fill center">`
- `.g2`
- `.g3`
- `.g4` — 예: `<div class="grid g4 fill center">`
- `.split`
- `.stack` — 예: `<div class="fill stack">`

**카드 묶음(창 하나 = 카드 하나)**
- `.card`
- `.c-no`
- `.c-foot`
- `.is-key` — 예: `<div class="is-key">`

**수치 타일**
- `.tile` — 예: `<div class="tile is-key">`
- `.is-key` — 예: `<div class="is-key">`

**막대: 칸으로 끊긴 체력 막대. style="--v:42" 는 최댓값 대비 %**
- `.bars`
- `.bar`
- `.is-key` — 예: `<div class="is-key">`

**현안 → 해결: 왼쪽은 크림 쪽지, 오른쪽은 남색 창**
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.q` — 예: `<p class="q">`
- `.a` — 예: `<p class="a">`
- `.is-key` — 예: `<div class="is-key">`

**간트(월 1~12): style="--from:3;--to:6"**
- `.gantt`
- `.g-h`
- `.g-name`
- `.g-bar`
- `.is-key` — 예: `<div class="is-key">`

**표**
- `.tbl`
- `.n`
- `.is-key` — 예: `<div class="is-key">`
- `.brief` — 예: `<div class="brief fill">`
- `.goal` — 예: `<div class="goal fill">`
- `.likert` — 예: `<div class="likert fill">`
- `.ba` — 예: `<div class="ba">`
- `.case` — 예: `<div class="case fill">`
- `.g-row` — 예: `<div class="g-row" style="--v:88.5;--t:76.9">`
- `.lk` — 예: `<div class="lk is-key">`
- `.lk-key` — 예: `<p class="lk-key">`
- `.mile` — 예: `<ol class="mile fill">`
- `.road` — 예: `<div class="road fill">`
- `.ph` — 예: `<div class="ph" data-need="사진 자리 · 4:3 · 공방에서 도자기를 빚는 초등학생">`

**사업 개요: 목적 · 대상 · 기간 · 규모 네 칸**
- `.brief` — 예: `<div class="brief fill">`
- `.is-key` — 예: `<div class="is-key">`

**추진 경과: 가로 시간선 위 이정표. 날짜는 <time>**
- `.mile` — 예: `<ol class="mile fill">`
- `.is-key` — 예: `<div class="is-key">`

**증감 표시: 수치 타일 안 <span class="delta">▲ 38교</span> (줄면 .down)**
- `.delta` — 예: `<span class="delta">`
- `.down`

**목표 대비 달성: 실적 막대 + 목표선. style="--v:92;--t:80"(최댓값 대비 %)**
- `.goal` — 예: `<div class="goal fill">`
- `.g-row` — 예: `<div class="g-row" style="--v:88.5;--t:76.9">`
- `.is-key` — 예: `<div class="is-key">`
- `.g-key` — 예: `<p class="g-key">`
- `.v` — 예: `<i class="v">`
- `.t` — 예: `<i class="t">`

**만족도: 문항마다 다섯 단계 100% 막대. <i style="--v:%"> 다섯 개(매우 불만 → 매우 만족)**
- `.likert` — 예: `<div class="likert fill">`
- `.lk` — 예: `<div class="lk is-key">`
- `.is-key` — 예: `<div class="is-key">`
- `.lk-key` — 예: `<p class="lk-key">`

**전후 비교: 사업 전 → 사업 후, 짝마다 한 줄**
- `.ba` — 예: `<div class="ba">`
- `.is-key` — 예: `<div class="is-key">`
- `.ba-head` — 예: `<p class="ba-head">`

**우수 사례: 사진 자리 + 학교 · 한 줄 성과 + 참여자 목소리**
- `.case` — 예: `<div class="case fill">`
- `.ph` — 예: `<div class="ph" data-need="사진 자리 · 4:3 · 공방에서 도자기를 빚는 초등학생">`
- `.c-body` — 예: `<div class="c-body">`
- `.is-key` — 예: `<div class="is-key">`

**향후 계획: 단계 머리(화살 띠) + 단계별 할 일**
- `.road` — 예: `<div class="road fill">`
- `.is-key` — 예: `<div class="is-key">`

---

## 4. HTML 뼈대 (예시 덱 13장 — 부품 견본입니다. 장 구성은 따라 하지 말고, 공통 파일 두 줄은 그대로 두며, 장은 내용에 맞게 새로)

```html
<!DOCTYPE html>
<html lang="ko" data-kit="A">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>덱 키트 A · 픽셀 게임 — 성과 공유회 예시 덱</title>
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
    <span class="c-tag">2026 성과 공유회 · 가상 예시</span>
    <h1>학교 문화예술교육<br><em>지역 연계</em> 사업 성과</h1>
    <p class="c-sub">1년 동안 학교 밖 교실 46곳에서 일어난 일</p>
  </div>
  <div class="prog" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
  <p class="c-org"><span>○○교육청 교육과정과</span><span>2026. 12. 18.</span></p>
</section>

<!-- 2. 목차 -->
<section class="slide toc">
  <div class="s-body">
    <p class="kicker">CONTENTS</p>
    <h2 class="title">차례</h2>
    <ol class="toc-list">
      <li class="is-now"><b>01</b><span>사업 개요</span><span>03</span></li>
      <li><b>02</b><span>추진 경과</span><span>04</span></li>
      <li><b>03</b><span>핵심 성과</span><span>05</span></li>
      <li><b>04</b><span>우수 사례</span><span>10</span></li>
      <li><b>05</b><span>시사점 · 향후 계획</span><span>11</span></li>
    </ol>
  </div>
  <div class="prog" aria-hidden="true"><i class="next"></i><i></i><i></i><i></i><i></i></div>
  <span class="page-no"></span>
</section>

<!-- 3. 사업 개요 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">01 사업 개요</p>
    <h2 class="title">학교 수업을 <em>지역 예술 공간</em>과 이어 10개월을 운영했습니다</h2>
    <div class="brief fill">
      <div class="is-key"><span>목적</span><b>학교 밖 예술 공간을 교실로</b><p>교과 수업과 이어지는 체험</p></div>
      <div><span>대상</span><b>초 · 중학교 138교</b><p>희망 학교 공모(목표 120교)</p></div>
      <div><span>기간</span><b>2026. 3. ~ 12.</b><p>1 · 2학기 10개월</p></div>
      <div><span>규모</span><b>9억 5천만 원</b><p>교육청 · 지자체 7 : 3</p></div>
    </div>
  </div>
  <p class="src">가상 예시</p>
  <span class="page-no"></span>
</section>

<!-- 4. 추진 경과 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">02 추진 경과</p>
    <h2 class="title">봄에 판을 깔고, <em>2학기</em>에 연계 수업이 본격화됐습니다</h2>
    <ol class="mile fill">
      <li><time>2026. 3.</time><b>공간 협약</b><p>공연장 · 전시관 · 공방 46곳</p></li>
      <li><time>4.</time><b>공동 설계 연수</b><p>예술가 · 교사 6시간</p></li>
      <li><time>5.</time><b>연계 수업 시작</b><p>1학기 62교</p></li>
      <li class="is-key"><time>9.</time><b>2학기 확대</b><p>138교로 늘어남</p></li>
      <li><time>12.</time><b>성과 공유회</b><p>사례 발표 · 내년 계획</p></li>
    </ol>
  </div>
  <span class="page-no"></span>
</section>

<!-- 5. 간지 -->
<section class="slide divider">
  <div class="d-no"><small>SECTION</small>03</div>
  <h2>핵심 성과</h2>
  <p>목표보다 많이 열렸고, 한 곳은 아직 모자랍니다.</p>
  <div class="prog" aria-hidden="true"><i class="done"></i><i class="done"></i><i class="now"></i><i></i><i></i></div>
  <span class="page-no"></span>
</section>

<!-- 6. 핵심 성과: 수치 타일 + 증감 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">03 핵심 성과</p>
    <h2 class="title">참여 학교 <em>138교</em>, 연계 수업 1,240회가 열렸습니다</h2>
    <div class="grid g4 fill center">
      <div class="tile is-key"><span>참여 학교</span><b>138<small>교</small></b><span class="delta">▲ 64교</span><p>2025 시범 대비</p></div>
      <div class="tile"><span>연계 수업</span><b>1,240<small>회</small></b><span class="delta">▲ 702회</span><p>2025 시범 대비</p></div>
      <div class="tile"><span>참여 학생</span><b>2.1<small>만 명</small></b><span class="delta">▲ 1.2만 명</span><p>2025 시범 대비</p></div>
      <div class="tile"><span>예술 공간</span><b>46<small>곳</small></b><span class="delta">▲ 19곳</span><p>2025 시범 대비</p></div>
    </div>
  </div>
  <p class="src">자료: ○○교육청 운영 실적(가상 예시)</p>
  <span class="page-no"></span>
</section>

<!-- 7. 목표 대비 달성 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">03 핵심 성과</p>
    <h2 class="title">네 지표 중 셋은 목표를 넘었고, <em>예술 공간</em>은 92%입니다</h2>
    <div class="goal fill">
      <div class="g-row" style="--v:88.5;--t:76.9"><span>참여 학교</span><i></i><b>115%<small>138 / 120교</small></b></div>
      <div class="g-row" style="--v:95.4;--t:76.9"><span>연계 수업</span><i></i><b>124%<small>1,240 / 1,000회</small></b></div>
      <div class="g-row" style="--v:80.8;--t:76.9"><span>참여 학생</span><i></i><b>105%<small>2.1 / 2만 명</small></b></div>
      <div class="g-row is-key" style="--v:70.8;--t:76.9"><span>예술 공간</span><i></i><b>92%<small>46 / 50곳</small></b></div>
      <p class="g-key"><span><i class="v"></i>달성률</span><span><i class="t"></i>목표(100%)</span></p>
    </div>
  </div>
  <p class="src">자료: ○○교육청 운영 실적(가상 예시)</p>
  <span class="page-no"></span>
</section>

<!-- 8. 만족도 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">03 핵심 성과</p>
    <h2 class="title">학생 <em>10명 중 9명</em>이 다시 하고 싶다고 답했습니다</h2>
    <div class="likert fill">
      <div class="lk is-key"><span>다시 참여하고 싶다</span><div><i style="--v:2"></i><i style="--v:3"></i><i style="--v:6"></i><i style="--v:27"></i><i style="--v:62"></i></div><b>4.5<small> / 5</small></b></div>
      <div class="lk"><span>예술가 선생님과 함께해 좋았다</span><div><i style="--v:1"></i><i style="--v:2"></i><i style="--v:8"></i><i style="--v:30"></i><i style="--v:59"></i></div><b>4.4<small> / 5</small></b></div>
      <div class="lk"><span>교과 내용이 더 잘 이해됐다</span><div><i style="--v:3"></i><i style="--v:6"></i><i style="--v:15"></i><i style="--v:38"></i><i style="--v:38"></i></div><b>4.0<small> / 5</small></b></div>
      <div class="lk"><span>이동 · 안전이 걱정되지 않았다</span><div><i style="--v:4"></i><i style="--v:9"></i><i style="--v:21"></i><i style="--v:36"></i><i style="--v:30"></i></div><b>3.8<small> / 5</small></b></div>
      <p class="lk-key"><span><i></i>전혀 아니다</span><span><i></i>아니다</span><span><i></i>보통</span><span><i></i>그렇다</span><span><i></i>매우 그렇다</span></p>
    </div>
  </div>
  <p class="src">학생 설문 1,860명(가상 예시)</p>
  <span class="page-no"></span>
</section>

<!-- 9. 전후 비교 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">03 핵심 성과</p>
    <h2 class="title">참여 뒤, <em>학교 밖 수업을 계획한 학교</em>가 두 배로 늘었습니다</h2>
    <div class="fill stack">
      <p class="ba-head"><span>사업 전(2025)</span><span>사업 후(2026)</span></p>
      <div class="ba">
        <div><span>학교 밖 수업을 계획한 학교</span><p>참여교 중</p><b>31<small>%</small></b></div><i aria-hidden="true"></i><div class="is-key"><span>학교 밖 수업을 계획한 학교</span><p>참여교 중</p><b>64<small>%</small></b></div>
        <div><span>교사 1명당 연계 수업</span><p>한 해</p><b>1.4<small>회</small></b></div><i aria-hidden="true"></i><div><span>교사 1명당 연계 수업</span><p>한 해</p><b>3.2<small>회</small></b></div>
        <div><span>예술가와 수업해 본 교사</span><p>참여교 교사 중</p><b>18<small>%</small></b></div><i aria-hidden="true"></i><div><span>예술가와 수업해 본 교사</span><p>참여교 교사 중</p><b>47<small>%</small></b></div>
      </div>
    </div>
  </div>
  <p class="src">교사 설문 412명(가상 예시)</p>
  <span class="page-no"></span>
</section>

<!-- 10. 우수 사례 + 참여자 목소리 -->
<section class="slide">
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

<!-- 11. 시사점: 현안 → 해결(누를 때마다 한 줄) -->
<section class="slide" data-steps="3">
  <div class="s-body">
    <p class="kicker">05 시사점 · 향후 계획</p>
    <h2 class="title">막힌 곳은 <em>이동 · 안전</em>이었고, 내년엔 묶어서 지원합니다</h2>
    <div class="fill stack">
      <div class="fix" data-step="1"><p class="q"><b>막힌 곳 1</b>예술 공간이 시 지역에 몰려 군 지역 학교는 이동이 깁니다</p><i aria-hidden="true"></i><p class="a"><b>고칠 방법 1</b>군 지역에 찾아오는 예술 공간 버스 2대</p></div>
      <div class="fix is-key" data-step="2"><p class="q"><b>막힌 곳 2</b>학교마다 버스 · 보험을 따로 준비해야 했습니다</p><i aria-hidden="true"></i><p class="a"><b>고칠 방법 2</b>이동 · 보험 · 인솔 보조를 교육청이 한꺼번에 계약</p></div>
      <div class="fix" data-step="3"><p class="q"><b>막힌 곳 3</b>예술가 · 교사 설계 시간이 학기 초에 몰렸습니다</p><i aria-hidden="true"></i><p class="a"><b>고칠 방법 3</b>공동 설계 연수를 학기마다 두 번으로 나눔</p></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>

<!-- 12. 향후 계획 -->
<section class="slide">
  <div class="s-body">
    <p class="kicker">05 시사점 · 향후 계획</p>
    <h2 class="title">2027년엔 <em>군 지역</em>부터 넓혀 200교로 갑니다</h2>
    <div class="road fill">
      <div class="is-key"><h3><small>2027 상반기</small>군 지역 넓히기</h3><ul><li>찾아오는 예술 공간 버스 2대</li><li>군 지역 학교 우선 선정</li><li>이동 · 보험 일괄 계약</li></ul></div>
      <div><h3><small>2027 하반기</small>200교로 확대</h3><ul><li>예술 공간 60곳 협약</li><li>학기별 공동 설계 연수</li><li>연계 수업 2,000회</li></ul></div>
      <div><h3><small>2028</small>교육과정에 넣기</h3><ul><li>학년별 연계 수업 모델</li><li>교육과정 편성 안내</li><li>성과 지표 정례 조사</li></ul></div>
    </div>
  </div>
  <span class="page-no"></span>
</section>

<!-- 13. 마무리 -->
<section class="slide close">
  <h2>학교 밖도<br>교실이었습니다</h2>
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

/* 성과 공유회 부품(parts.css) 계열 조정: 정보는 남색 창 안, 창 안 강조는 금색, 글자는 11의 배수 */
:root{--ds-on:#F7F2E4;--ds-on-sub:#A9C8F5;--ds-key:#FFCF4A;--ds-track:#2F3E6B;
  --ds-fs-body:33px;--ds-fs-label:22px;--ds-fs-sub:22px;--ds-fs-h:44px;--ds-fs-num:88px;--ds-fs-num-s:44px}
.brief > div,.goal,.likert,.ba > div,.case > div{border:var(--px) solid var(--ds-ink);box-shadow:inset 0 0 0 var(--px) var(--ds-c1),inset 0 0 0 calc(var(--px) * 2) var(--ds-c5);
  clip-path:polygon(var(--px) 0,calc(100% - var(--px)) 0,100% var(--px),100% calc(100% - var(--px)),calc(100% - var(--px)) 100%,var(--px) 100%,0 calc(100% - var(--px)),0 var(--px))}
.brief > div.is-key,.case > div.is-key,.ba > div.is-key{border-color:var(--ds-hi)}
.g-row > i::before{background:repeating-linear-gradient(90deg,var(--ds-c3) 0 20px,transparent 20px 24px)}
.g-row.is-key > i::before{background:repeating-linear-gradient(90deg,var(--ds-hi) 0 20px,transparent 20px 24px)}
.lk > div i:nth-child(1),.lk-key i:nth-of-type(1){background:#2F3E6B}.lk > div i:nth-child(2),.lk-key i:nth-of-type(2){background:#3B5A9E}
.lk > div i:nth-child(3),.lk-key i:nth-of-type(3){background:#5A82D0}.lk > div i:nth-child(4),.lk-key i:nth-of-type(4){background:#A9C8F5}
.lk > div i:nth-child(5),.lk-key i:nth-of-type(5){background:#F7F2E4}
.case blockquote{border-left-style:dashed}
.mile li::before{border-radius:0}.mile li.is-key::before{background:var(--ds-accent);border-color:var(--ds-accent)}
.road h3{background:var(--ds-c1);clip-path:polygon(0 0,calc(100% - 28px) 0,100% 50%,calc(100% - 28px) 100%,0 100%,20px 50%)}
.road > div:first-child h3{clip-path:polygon(0 0,calc(100% - 28px) 0,100% 50%,calc(100% - 28px) 100%,0 100%)}
.road li::before{border-radius:0}
.ph:empty::after{border-style:dashed;border-width:var(--px)}
```
