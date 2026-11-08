# B 미니멀 스튜디오 — 성과 공유회 · 설명회 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **ChatGPT · Claude · Gemini 같은 채팅 AI**에게 통째로 주면, 이 디자인으로 사업 성과 공유회 · 사업 설명회 발표 덱을 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 B 계열 장표(#19 · #26 · #28 · #37 · #46 · #116)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일을 첨부**합니다(안 되면 내용을 끝까지 복사해 붙여 넣기).
2. 만들 발표를 말합니다. 예) "2026 ○○ 사업 성과 공유회, ○○교육청 ○○과. 핵심 성과는 아래 표(출처: ○○ 실적), 우수 사례 3개는 … 덱으로 만들어 줘. 결과는 .html 파일로." 사례 사진이 있으면 함께 올립니다.
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
- 표지 · 목차 · 간지 · 마무리에는 이 계열의 상징 부품인 모형대 매스(`.mass`)를 씁니다. 목차 · 간지의 `.lit` 층 = 지금 섹션(아래층이 1섹션).
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
- `.fill` — 예: `<div class="brief fill">`
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
- `.grid` — 예: `<div class="grid g4 fill center">`
- `.center` — 예: `<div class="grid g4 fill center">`
- `.g2`
- `.g3`
- `.g4` — 예: `<div class="grid g4 fill center">`
- `.split`

**카드 묶음**
- `.card`
- `.c-foot`
- `.c-no`
- `.is-key` — 예: `<div class="is-key">`

**수치 타일**
- `.tile` — 예: `<div class="tile is-key">`
- `.is-key` — 예: `<div class="is-key">`

**막대(가로): style="--v:42" 는 최댓값 대비 %**
- `.bars`
- `.bar`
- `.is-key` — 예: `<div class="is-key">`

**현안 → 해결 표**
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.stack` — 예: `<div class="fill stack">`
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
<html lang="ko" data-kit="B">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>덱 키트 B · 미니멀 스튜디오 — 성과 공유회 예시 덱</title>
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
    <span class="c-tag">2026 성과 공유회 · 가상 예시</span>
    <h1>학교 문화예술교육<br><em>지역 연계</em> 사업 성과</h1>
    <p class="c-sub">1년 동안 학교 밖 교실 46곳에서 일어난 일</p>
  </div>
  <div class="mass" aria-hidden="true"><i></i><i></i><i class="lit"></i><i></i><i></i></div>
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
  <div class="mass" aria-hidden="true"><i class="lit"></i><i></i><i></i><i></i><i></i></div>
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
  <div class="mass" aria-hidden="true"><i></i><i></i><i class="lit"></i><i></i><i></i></div>
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
