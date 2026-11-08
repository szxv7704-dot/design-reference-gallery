# D 인쇄·종이 에디토리얼 — 성과 공유회 · 설명회 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **ChatGPT · Claude · Gemini 같은 채팅 AI**에게 통째로 주면, 이 디자인으로 사업 성과 공유회 · 사업 설명회 발표 덱을 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 D 계열 장표(#4 · #27 · #32 · #60 · #62)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일을 첨부**합니다(안 되면 내용을 끝까지 복사해 붙여 넣기).
2. 만들 발표를 말합니다. 예) "2026 ○○ 사업 성과 공유회, ○○교육청 ○○과. 핵심 성과는 아래 표(출처: ○○ 실적), 우수 사례 3개는 … 덱으로 만들어 줘. 결과는 .html 파일로." 사례 사진이 있으면 함께 올립니다.
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
4. 쓴 클래스가 모두 부품 사전(3) 또는 '추가 부품' 칸에 있는가? 인라인 style은 `--v` · `--t` · `--from` · `--to`뿐인가? 코드로 그린 그림(SVG · CSS 도형)이 없는가?
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

## 장의 짜임 (성과 공유회 · 설명회 본문)
모든 본문 장은 같은 순서다: **머리말(`.kicker`, 아래 이중 괘선) → 결론 한 문장 제목(`.title`, 명조) → 도식 1~2개 → 출처(`.src`)**.
- 제목은 결론 문장이다. "핵심 성과"(×) → "참여 학교 138교, 연계 수업 1,240회가 열렸습니다"(○).
- 머리말은 덱 목차와 같은 말을 쓴다. 성과 공유회: 01 사업 개요 · 02 추진 경과 · 03 핵심 성과 · 04 우수 사례 · 05 시사점 · 향후 계획.
- 카드 · 수치 타일은 **상자가 아니라 지면의 단**이다: 위에 이중 괘선, 그림자 · 테두리 없음.
- 막대 · 간트 · 표는 종이 위에 한 장 더 놓은 것처럼 흰 면 + 위 3px 먹선.

## 판 번호(.reg) — 이 계열의 얼굴
- 표지: 큰 명조 연도(남색) + 맞춤 표지(⊕).
- 목차: 12단 눈금(제목 아래) + 맞춤 표지. 목록은 오른쪽 8단, 왼쪽 4단은 비워 둔다.
- 간지: **재단 표시(`.crop`)와 주홍 판 어긋남(번호에 4~6px)은 덱 전체에서 간지에만.**
- 마무리: 맞춤 표지만. 문의는 겹 테두리 공지란.
- 본문 장에는 쓰지 않는다.

## 성과 공유회 부품(공용 parts.css)
사업 개요 `.brief` · 추진 경과 `.mile` · 증감 `.delta` · 목표 대비 달성 `.goal` · 만족도 `.likert` · 전후 비교 `.ba` · 우수 사례 `.case`(사진 `.ph` + 목소리) · 향후 계획 `.road`. 모양은 이 계열의 토큰을 따른다.
- **그림을 코드로 그리지 않는다.** 사물 · 인물 · 풍경 · 캐릭터가 필요하면 사용자에게 이미지를 요청하고, 사진은 `.ph` 자리에 넣는다(docs/criteria.md 4).

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
6. 인라인 `style`은 `--v` · `--t` · `--from` · `--to`만.
7. 사물 · 인물 · 풍경을 SVG · CSS로 그리기(이미지를 요청한다).

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
- `.fill` — 예: `<div class="brief fill">`
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
- `.grid` — 예: `<div class="grid g4 fill center">`
- `.center` — 예: `<div class="grid g4 fill center">`
- `.g2`
- `.g3`
- `.g4` — 예: `<div class="grid g4 fill center">`
- `.split`
- `.stack` — 예: `<div class="fill stack">`

**카드 묶음: 상자 대신 지면의 단(이중 괘선 머리)**
- `.card`
- `.c-no`
- `.c-foot`
- `.is-key` — 예: `<div class="is-key">`

**수치 타일: 큰 명조 숫자**
- `.tile` — 예: `<div class="tile is-key">`
- `.is-key` — 예: `<div class="is-key">`

**막대(가로, 남색 한 판): style="--v:42" 는 최댓값 대비 %**
- `.bars`
- `.bar`
- `.is-key` — 예: `<div class="is-key">`

**현안 → 해결**
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

**표: 신문 표(위 굵은 선 · 가는 줄 · 합계 위 이중 괘선)**
- `.tbl`
- `.n`
- `.is-key` — 예: `<div class="is-key">`
- `.brief` — 예: `<div class="brief fill">`
- `.goal` — 예: `<div class="goal fill">`
- `.likert` — 예: `<div class="likert fill">`
- `.case` — 예: `<div class="case fill">`
- `.ba` — 예: `<div class="ba">`
- `.mile` — 예: `<ol class="mile fill">`
- `.road` — 예: `<div class="road fill">`

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
<html lang="ko" data-kit="D">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>덱 키트 D · 인쇄·종이 에디토리얼 — 성과 공유회 예시 덱</title>
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
    <span class="c-tag">2026 성과 공유회 · 가상 예시</span>
    <h1>학교 문화예술교육<br><em>지역 연계</em> 사업 성과</h1>
    <p class="c-sub">1년 동안 학교 밖 교실 46곳에서 일어난 일</p>
  </div>
  <div class="reg" aria-hidden="true"><b>2026</b></div>
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
  <div class="reg" aria-hidden="true"><b>01</b></div>
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
  <div class="reg is-off" aria-hidden="true"><b>03</b><i class="crop"></i></div>
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

/* 성과 공유회 부품(parts.css) 계열 조정: 상자 대신 지면의 단(이중 괘선), 판은 위 3px 먹선 */
.brief > div{background:var(--rule2);box-shadow:none;padding:32px 0 0;min-height:380px}
.brief b{font-weight:900;letter-spacing:-.02em}
.goal,.likert,.case > div{border-top:3px solid var(--ds-ink)}
.ba > div{box-shadow:none;border:1px solid var(--ds-line)}
.ba > div.is-key{border-color:var(--ds-accent)}
.mile li::after{height:1px;top:95px;background:var(--ds-ink)}
.mile li::before{width:20px;height:20px;margin:8px 0 18px;border-width:2px;border-color:var(--ds-ink)}
.mile li.is-key::before{border-color:var(--ds-accent)}
.road h3{background:var(--ds-c1)}
.road li::before{width:8px;height:8px}
.case blockquote{border-left-width:2px}
```
