# F 관측·중계 인포그래픽 — 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **Claude · ChatGPT 같은 채팅 AI**에게 자기 문서와 함께 주면, 문서 내용을 이 디자인의 16:9 발표 덱으로 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 F 계열 장표(#20 · #25 · #31 · #52 · #71)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일과 발표할 문서**(한글 · PDF · 붙여 넣은 글)를 넣습니다.
2. 어떤 자리인지 말합니다. 예) "이 계획안으로 10분짜리 발표 덱을 만들어 줘. 결과는 .html 파일로."
3. AI가 먼저 **장별 구성안**을 보여 줍니다. 고칠 곳을 말하거나 "좋아, 만들어 줘".
4. 받은 `.html`을 내려받아 더블클릭합니다. → · Space로 넘기고, F는 전체 화면, 인쇄하면 장마다 한 쪽(16:9) PDF가 됩니다.
5. 고칠 곳은 "3장 제목을 ○○로"처럼 말합니다. 코드가 끊기면 "끊긴 곳부터 이어서".

알아 둘 점
- 열 때 **인터넷이 필요**합니다(공통 CSS · 엔진 · 글꼴을 `szxv7704-dot.github.io`에서 불러옴). 인터넷이 막힌 곳에서 발표하려면 저장소에서 `python3 scripts/kit.py inline F 슬라이드.html`을 실행해 모든 것이 파일 안에 든 판을 만드세요.
- 수치는 AI가 지어내지 않도록 적어 두었지만, **받은 덱의 숫자를 원문과 꼭 대조**하세요.
- 개인정보(학생 이름 · 사진 등)는 AI에게 넣지 마세요.

## 라이선스

- 글꼴: 모두 SIL Open Font License 1.1(전문 https://szxv7704-dot.github.io/design-reference-gallery/fonts/OFL.txt). 이 계열이 쓰는 글꼴의 저작권 고지:

| 글꼴 | 굵기 | 저작권 | 예약 이름 | 라이선스 |
|---|---|---|---|---|
| GothicA1 | 300 · 400 · 500 · 600 · 700 · 800 · 900 | (C) Copyright HanYang I&C Co.,Ltd. All rights reserved. | — | SIL OFL 1.1 |
| SairaSemiCondensed | 500 · 600 · 700 | Copyright 2016 The Saira Project Authors (omnibus.type@gmail.com), with reserved font name "Saira". | Saira | SIL OFL 1.1 |

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
4. 분위기 계열은 **F 관측·중계 인포그래픽**입니다.
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

**고르는 순서** — 한 문단이 둘 이상에 맞으면 위에서부터 먼저 맞는 것:

1. 숫자가 주인공이면 수 묶음(하나면 큰 숫자, 시간 축이 있으면 추이, 합이 100%면 구성비, 나머지는 막대 비교).
2. 날짜가 주인공이면 일정.
3. 두 쪽이 맞서면 둘 비교, 같은 것이 달라졌으면 전→후.
4. 차례가 있으면 순서·단계, 위아래가 있으면 체계, 갈래만 있으면 묶음·분류.
5. 칸이 3열 이상 필요하면 표.
6. 어디에도 안 맞으면 항목. 항목이 한 개면 한 문장.

## 4. 흐름 (문서 종류에 맞는 자리 순서)

자리 이름은 머리말(`.kicker`)과 목차에 씁니다. 장 수는 내용이 정하고, 문서에 없는 자리는 뺍니다.

**10장 세트 예시** — 세트의 열 가지 역할을 한 장씩(가상 주제: 생성형 AI 업무 활용 연수) · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/F-set.html

| 자리 | 기본 장표 |
| --- | --- |
| 표지 | 표지 |
| 전체 흐름 | 목차 |
| 핵심 개념 · 정의 | 용어 정의 |
| 비교 | 둘 비교 |
| 순서 · 절차 | 순서·단계 |
| 사례 · 화면 | 화면 짚기 |
| 실습 · 행동 안내 | 할 일 |
| 핵심 수치 · 근거 | 큰 숫자 |
| 요약 | 항목 |
| 마무리 | 맺음 |

**다른 주제 시험** — 다른 내용에도 쓰이는지 보는 본문 다섯 장(가상 주제: 학교 독서 활동 소개) · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/F-set2.html

| 자리 | 기본 장표 |
| --- | --- |
| 프로그램 묶음 | 묶음·분류 |
| 추이 | 추이 |
| 인용 | 인용 |
| 일정 | 일정 |
| 질문 | 질문 |

**계획안 발표** — 계획안 문서의 내용을 발표로 옮길 때 · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/F-plan.html

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

**성과 공유회** — 한 해 사업의 결과를 알릴 때 · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/F.html

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

## 5. 분위기 계열: F 관측·중계 인포그래픽

맑은 청백 바탕에 남색 기록판, 좁은 숫자 글꼴. 빨강 강조 한 곳. 어울리는 자리: 실적 · 통계가 많은 성과 보고, 체육 · 진로 행사. 자세한 규칙은 아래 '디자인 규칙'.

## 6. HTML 뼈대

```html
<!DOCTYPE html>
<html lang="ko" data-kit="F">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>발표 제목</title>
<!-- 이 계열의 공통 CSS(글꼴 · 색 · 부품). 주소를 바꾸지 마세요 -->
<link rel="stylesheet" href="https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/F.css">
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

이 계열은 구간 띠(`.lane`)를 씁니다. 칸 수 = 섹션 수, 지난 구간 `.done` · 지금 구간 `.now` · 남은 구간 `.ghost`.

## 8. 기본 장표별 견본 코드

문구는 모두 가상 예시입니다. **구조와 클래스만 가져오고 문구는 하나도 남기지 않습니다.**

### 표지 · `cover`

- 이런 내용일 때: 문서 제목 · 기관 · 날짜
- 내용 조건: 제목 2줄 이하, 부제 1줄. 넘치면: 부제를 뺀다
- 부품: `.cover`

```html
<section data-pattern="cover" class="slide cover">
  <div class="c-text">
    <span class="c-tag">교직원 연수 · 가상 예시</span>
    <h1>생성형 AI,<br><em>업무에 쓰는</em> 첫걸음</h1>
    <p class="c-sub">요청 한 줄을 바꾸면 결과가 달라집니다</p>
  </div>
  <div class="lane" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
  <p class="c-org"><span>○○교육청 교육연수원</span><span>2027. 3. 12.</span></p>
</section>
```

### 목차 · `toc`

- 이런 내용일 때: 문서의 큰 번호(Ⅰ · Ⅱ · Ⅲ), 차시 순서
- 내용 조건: 3~5줄. 넘치면: 큰 묶음으로 합친다
- 부품: `.toc` + `.toc-list`

```html
<section data-pattern="toc" class="slide toc">
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
  <div class="lane" aria-hidden="true"><i class="now"></i><i></i><i></i><i></i><i></i></div>
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
  <div class="lane" aria-hidden="true"><i class="done"></i><i class="done"></i><i class="now"></i><i class="ghost"></i><i class="ghost"></i></div>
  <span class="page-no"></span>
</section>
```

### 맺음 · `closing`

- 이런 내용일 때: 문의처 · 담당 · 다음 차시 예고
- 내용 조건: 두 줄 문장 + 연락처 한 줄. 넘치면: —
- 부품: `.close`

```html
<section data-pattern="closing" class="slide close">
  <h2>오늘 쓴 요청문을<br>내일 업무에</h2>
  <p>문의 · ○○교육청 교육연수원 연수 담당</p>
  <div class="lane" aria-hidden="true"><i class="done"></i><i class="done"></i><i class="done"></i><i class="done"></i><i class="done"></i></div>
  <span class="page-no"></span>
</section>
```

### 한 문장 · `statement`

- 이런 내용일 때: 목적 · 비전 · 결론처럼 한 문장이 전부인 곳
- 내용 조건: 40자 이하 한 문장 + 받치는 말 1줄. 넘치면: 받치는 말을 다음 장으로
- 부품: `.say` — 이 장만 .title 없이 .kicker 아래에 둔다

```html
<section data-pattern="statement" class="slide">
  <div class="s-body">
    <p class="kicker">02 목표 · 추진 체계</p>
    <div class="say fill">
      <p>2027년, <em>어느 학교에서든</em><br>30분 안에 닿는 학교 밖 교실</p>
      <small>군 지역 학교의 평균 이동 시간 62분을 30분 안으로 줄입니다.</small>
    </div>
  </div>
  <p class="src">자료: ○○교육청 운영 실적(가상 예시)</p>
  <span class="page-no"></span>
</section>
```

### 항목 · `points`

- 이런 내용일 때: 개조식(□ · ○ · -) 항목 3~5개, 학습 목표, 기대 효과
- 내용 조건: 3~5개, 이름 + 설명 1~2줄(5개면 1줄). 넘치면: 6개부터 두 장, 또는 묶음·분류로
- 부품: `.points` — 네 칸으로 한눈에 보일 때는 .brief(목적 · 대상 · 기간 · 규모)

```html
<section data-pattern="points" class="slide">
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

### 용어 정의 · `define`

- 이런 내용일 때: "○○란", 용어 풀이, 개념 설명
- 내용 조건: 용어 1개 + 뜻 한 문장 + 예 1~2개. 넘치면: 용어마다 한 장
- 부품: `.define`

```html
<section data-pattern="define" class="slide">
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

### 인용 · `quote`

- 이런 내용일 때: 참여자 말 · 설문 서술 답 · 법령 조문
- 내용 조건: 1~3개, 각 60자 이하, 말한 사람. 넘치면: 가장 강한 것 하나만
- 부품: `.quote`

```html
<section data-pattern="quote" class="slide">
  <div class="s-body">
    <p class="kicker">독서 활동 소개 · 읽은 사람들의 말</p>
    <h2 class="title">가장 많이 나온 말은 <em>"같이 읽으니 끝까지 읽었다"</em>였습니다</h2>
    <div class="quote fill">
      <figure class="is-key"><blockquote>혼자였으면 덮었을 책을 친구들과 이야기하려고 끝까지 읽었어요.</blockquote><figcaption>5학년 학생</figcaption></figure>
      <figure><blockquote>아침 10분이 쌓이니 수업 시작이 차분해졌습니다.</blockquote><figcaption>3학년 담임 교사</figcaption></figure>
      <figure><blockquote>집에서도 아이가 먼저 책 이야기를 꺼냅니다.</blockquote><figcaption>2학년 학부모</figcaption></figure>
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

```html
<section data-pattern="steps" class="slide">
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

### 둘 비교 · `compare`

- 이런 내용일 때: 문제점 ↔ 개선 방안, 문단 ↔ 고른 장표, 기존안 ↔ 새 안
- 내용 조건: 2~3줄, 줄마다 왼쪽 · 오른쪽 한 짝. 넘치면: 4줄부터 두 장
- 부품: `.fix` (+ `.stack`) — 누를 때마다 한 줄씩 보이려면 data-step

```html
<section data-pattern="compare" class="slide" data-steps="2">
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

### 전→후 · `before-after`

- 이런 내용일 때: 현행 → 개선, 사업 전 → 사업 후(숫자가 있는 짝)
- 내용 조건: 2~3짝, 같은 기준 · 같은 단위. 넘치면: 가장 큰 변화 3짝만
- 부품: `.ba` (+ `.ba-head`)

```html
<section data-pattern="before-after" class="slide">
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
```

### 묶음·분류 · `groups`

- 이런 내용일 때: 과제 · 프로그램을 갈래로 나눈 것
- 내용 조건: 2~4묶음, 묶음마다 3줄 이하. 넘치면: 묶음마다 한 장
- 부품: `.card` + `.grid.g2/.g3/.g4`

```html
<section data-pattern="groups" class="slide">
  <div class="s-body">
    <p class="kicker">독서 활동 소개 · 무엇을 하나</p>
    <h2 class="title">올해 독서 활동은 <em>세 갈래</em>로 엽니다</h2>
    <div class="grid g3 fill center">
      <div class="card is-key"><span class="c-no">매일</span><h3>아침 10분 읽기</h3><p>1교시 전, 고른 책을<br>소리 없이 읽는다</p><p class="c-foot">전 학년 <b>18학급</b></p></div>
      <div class="card"><span class="c-no">달마다</span><h3>책 대화</h3><p>같은 책을 읽고<br>모둠으로 이야기한다</p><p class="c-foot">학년별 <b>월 1회</b></p></div>
      <div class="card"><span class="c-no">학기마다</span><h3>작가와 만남</h3><p>읽은 책의 작가를<br>도서관으로 초대한다</p><p class="c-foot">연 <b>2회</b></p></div>
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

```html
<section data-pattern="numbers" class="slide">
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

### 막대 비교 · `bars`

- 이런 내용일 때: 항목 간 크기 비교 · 순위 · 목표 대비 실적
- 내용 조건: 3~5줄, 한 가지 단위. 넘치면: 위 4개 + 나머지 합
- 부품: `.goal` + `.g-row` — 목표선이 없으면 .bars + .bar

```html
<section data-pattern="bars" class="slide">
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

```html
<section data-pattern="table" class="slide">
  <div class="s-body">
    <p class="kicker">04 일정 · 예산</p>
    <h2 class="title">총 12억 원 가운데 <em>이동 지원</em>에 5.4억 원을 씁니다</h2>
    <div class="fill stack">
      <table class="tbl">
        <thead><tr><th>묶음</th><th>주요 내용</th><th>2026</th><th>2027</th></tr></thead>
        <tbody>
          <tr class="is-key"><td>이동</td><td>버스 2대 · 거점 6곳</td><td class="n">1.8억</td><td class="n">5.4억</td></tr>
          <tr><td>수업</td><td>설계 연수 · 수업 모델</td><td class="n">3.1억</td><td class="n">3.6억</td></tr>
          <tr><td>행정</td><td>일괄 계약 · 보험</td><td class="n">1.9억</td><td class="n">3.0억</td></tr>
        </tbody>
        <tfoot><tr><td>합계</td><td></td><td class="n">6.8억</td><td class="n">12.0억</td></tr></tfoot>
      </table>
    </div>
  </div>
  <p class="src">자료: ○○교육청 2027 예산안(가상 예시)</p>
  <span class="page-no"></span>
</section>
```

### 일정 · `timeline`

- 이런 내용일 때: 추진 일정 · 연혁 · 과정 지도
- 내용 조건: 이정표 3~5개(.mile) 또는 줄 3~5개 × 12달(.gantt). 넘치면: 분기 · 학기로 묶는다
- 부품: `.mile` — 달 단위 기간이 겹치면 .gantt

```html
<section data-pattern="timeline" class="slide">
  <div class="s-body">
    <p class="kicker">독서 활동 소개 · 한 해 일정</p>
    <h2 class="title">가장 큰 행사는 <em>10월 책 잔치</em>입니다</h2>
    <ol class="mile fill">
      <li><time>3월</time><b>아침 읽기 시작</b><p>학급 문고 채우기</p></li>
      <li><time>5월</time><b>작가와 만남 1</b><p>그림책 작가</p></li>
      <li><time>7월</time><b>방학 책 꾸러미</b><p>세 권씩 빌려 가기</p></li>
      <li class="is-key"><time>10월</time><b>책 잔치</b><p>전시 · 낭독 · 나눔 장터</p></li>
      <li><time>12월</time><b>한 해 돌아보기</b><p>읽은 책 지도 만들기</p></li>
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

```html
<section data-pattern="screen" class="slide">
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

```html
<section data-pattern="ask" class="slide">
  <div class="s-body">
    <p class="kicker">독서 활동 소개 · 함께 정할 것</p>
    <div class="ask fill">
      <p class="a-q">우리 학급에서 가장 먼저 시작할 수 있는 것은 무엇일까요?</p>
      <ol>
        <li>아침 10분 읽기</li>
        <li>달마다 책 대화</li>
        <li>학급 문고 바꿔 읽기</li>
        <li>읽은 책 한 줄 남기기</li>
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

```html
<section data-pattern="todo" class="slide">
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

## 디자인 규칙 (`F` design.md)

````markdown
---
kit: F
name: 관측·중계 인포그래픽
version: v1
stage: 1920x1080
colors:
  bg: "#F3F5F8"   # 무대 바탕(맑은 낮 청백)
  surface: "#FFFFFF"   # 기록판 면
  ink: "#12203A"   # 제목 · 본문(남색 먹)
  sub: "#55627A"   # 보조 글자
  accent: "#DC3B2D"   # 빨강 — 한 장에 한 곳만
  c1: "#172B52"   # 남색 기록판 머리
  c3: "#4C7FC6"   # 띠 · 간트 막대
  c4: "#9DB9E3"   # 막대(보통 값)
fonts:
  title: "Gothic A1 800"   # 표지 96 · 간지 88 · 마무리 80 · 장 제목 56 · 카드 제목 44
  body: "Gothic A1 500/700"   # 본문 28 · 보조 22~26
  num: "Saira Semi Condensed 600/700"   # 수치 88 · 쪽 번호 22 (숫자 · 영문에만)
space:
  side: 120px
  top: 84px
  bottom: 96px
  gap: 32px
radius: 0px
---

## 분위기
경기 중계 화면의 기록판. 맑은 청백 바탕에 남색 판이 놓이고, 숫자는 좁은 숫자 글꼴로 또렷하다. 빨강은 **지금 봐야 할 한 줄**에만.
- 강조색(`accent`)은 **한 장에 한 곳**: 제목의 핵심 낱말 하나(`<em>`) 또는 부품 하나(`.is-key`). 둘 다 쓰면 같은 내용을 가리켜야 한다.
- 면은 각지게(모서리 0), 가는 테두리 한 줄. 카드 · 타일은 남색 굵은 변을 한쪽에 둔다.
- 숫자 · 날짜 · 번호는 Saira Semi Condensed. 한글에는 쓰지 않는다.
- 머리말 띠 아래에는 눈금자 무늬가 있다(공통 CSS가 그림). 눈금을 다른 곳에 더 그리지 않는다.
- 트랙 · 경기장 · 지도 같은 **그림을 코드로 그리지 않는다.**
- 근거 장표: 표지 · 본문 #20 · #25 · #31 · #71, 목차 · 간지 키트 #52.
- 어울리는 자리: 실적 · 통계가 많은 성과 보고, 체육 · 진로 행사.

## 색의 역할
| 이름 | 쓰는 곳 | 쓰지 않는 곳 |
|---|---|---|
| bg | 모든 장의 바탕 | 카드 면 |
| surface | 카드 · 수치 타일 · 막대 판 · 표 · 간트 판 | 바탕 |
| ink | 제목 · 본문 · 굵은 선 | 넓은 면 채우기 |
| sub | 머리말 · 라벨 · 단위 · 출처 · 쪽 번호 | 결론 문장 |
| accent | 한 장에 한 곳(핵심 낱말 · 수치 · 막대 · 줄 · 카드, 지금 섹션) | 배경 · 장식 · 두 곳 이상 |
| c1 ~ c5 | 띠 · 막대 · 구성비 조각의 농담(c1 진함 → c5 옅음) | 글자 강조 |

새 색을 만들지 않는다. 빨강 · 초록으로 좋고 나쁨을 나타내지 않는다(강조는 accent 하나).

## 글자
- 제목은 Gothic A1 800, 본문은 Gothic A1 500/700, 숫자는 Saira Semi Condensed 600/700. 글꼴은 변수(`--ds-font-title` · `--ds-font-body` · `--ds-font-num`)로만 부른다.
- 한글에 넓은 자간을 쓰지 않는다. 자간은 0에서 -0.02em 사이.
- 크기: 읽는 글 28px 이상, 보조 글(라벨 · 단위 · 출처) 22px 이상. 부품 CSS가 이미 지키므로 크기를 줄이지 않는다.

## 장의 짜임
모든 본문 장은 같은 순서다: **머리말(`.kicker`) → 결론 한 문장 제목(`.title`) → 기본 장표 부품 하나 → 출처(`.src`, 수치가 있으면 반드시)**.
한 문장 · 질문 · 할 일 장만 제목 없이 머리말 아래에 부품을 둔다.

## 구간 띠(.lane)
가로 띠를 섹션 수만큼 나눈 것(최대 5). `.done` 지난 구간(남색) · `.now` 지금 구간(빨강) · `.ghost` 남은 구간(옅음).
- **표지 · 목차 · 간지 · 맺음에만** 쓴다. 본문 장에는 쓰지 않는다.
- 크기 · 위치는 부품 CSS 그대로. 돌리거나 기울이지 않는다.

## 하지 말 것
1. 새 색 · 그라데이션 · 그림 파일 만들기.
2. 본문 장에 상징 부품 넣기.
3. 장 번호 · 쪽 표시 · 점을 손으로 쓰기(엔진이 채운다).
4. 공통 CSS · 엔진을 HTML 안에 옮겨 쓰기, `@font-face` 새로 쓰기.
5. 사물 · 인물 · 풍경을 SVG · CSS로 그리기(이미지를 요청한다).
6. 한 장에 기본 장표를 둘 이상 넣기.

## 알려진 한계 (v1)
- 이 계열의 근거 장표는 사진 · 캔버스 그림에 기댄 표지가 많다. 키트는 그 **색 · 글꼴 · 짜임**만 옮겼고 그림은 옮기지 않았다.
- 표지에 쓸 사진 자리는 아직 없다(표지는 글자와 상징 부품으로만 만든다).
````

- 글꼴: 제목 Gothic A1(500/700/800) · 본문 Gothic A1(500/700/800) · 숫자 Saira Semi Condensed(600/700). 공통 CSS가 불러오므로 설치하지 않아도 됩니다.
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

**구간 띠: 칸 수 = 섹션 수. .done 지난 구간(남색) · .now 지금 구간(빨강) · .ghost 남은 구간(옅음)**
- `.lane` — 예: `<div class="lane" aria-hidden="true">`
- `.done` — 예: `<i class="done">`
- `.now` — 예: `<i class="now">`
- `.ghost` — 예: `<i class="ghost">`

**표지**
- `.cover` — 예: `<section data-pattern="cover" class="slide cover">`
- `.c-text` — 예: `<div class="c-text">`
- `.c-tag` — 예: `<span class="c-tag">`
- `.c-sub` — 예: `<p class="c-sub">`
- `.c-org` — 예: `<p class="c-org">`
- `.lane` — 예: `<div class="lane" aria-hidden="true">`

**목차: 줄 높이 112px, 지금 장 한 줄만 강조색**
- `.toc-list` — 예: `<ol class="toc-list">`
- `.is-now` — 예: `<li class="is-now">`
- `.toc` — 예: `<section data-pattern="toc" class="slide toc">`
- `.lane` — 예: `<div class="lane" aria-hidden="true">`

**간지: 큰 번호 + 섹션 이름 + 상징 부품**
- `.divider` — 예: `<section data-pattern="divider" class="slide divider">`
- `.d-no` — 예: `<div class="d-no">`
- `.lane` — 예: `<div class="lane" aria-hidden="true">`

**마무리**
- `.close` — 예: `<section data-pattern="closing" class="slide close">`
- `.lane` — 예: `<div class="lane" aria-hidden="true">`

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
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**수치 타일**
- `.tile` — 예: `<div class="tile is-key">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**막대(가로): style="--v:42" 는 최댓값 대비 %**
- `.bars`
- `.bar`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**현안 → 해결 표**
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.stack` — 예: `<div class="fill stack">`
- `.q` — 예: `<p class="q">`
- `.a` — 예: `<p class="a">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**간트(월 1~12): style="--from:3;--to:6"**
- `.gantt` — 예: `<div class="gantt fill">`
- `.g-h` — 예: `<span class="g-h">`
- `.g-name` — 예: `<span class="g-name">`
- `.g-bar` — 예: `<span class="g-bar" style="--from:1;--to:3">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**표**
- `.tbl` — 예: `<table class="tbl">`
- `.n` — 예: `<td class="n">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`
- `.tile` — 예: `<div class="tile is-key">`
- `.road` — 예: `<div class="road fill">`
- `.tree` — 예: `<div class="tree fill" style="--n:3">`

**사업 개요: 목적 · 대상 · 기간 · 규모 네 칸**
- `.brief` — 예: `<div class="brief fill">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**추진 경과: 가로 시간선 위 이정표. 날짜는 <time>**
- `.mile` — 예: `<ol class="mile fill">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**증감 표시: 수치 타일 안 <span class="delta">▲ 38교</span> (줄면 .down)**
- `.delta` — 예: `<span class="delta">`
- `.down`

**목표 대비 달성: 실적 막대 + 목표선. style="--v:92;--t:80"(최댓값 대비 %)**
- `.goal` — 예: `<div class="goal fill">`
- `.g-row` — 예: `<div class="g-row" style="--v:88.5;--t:76.9">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`
- `.g-key` — 예: `<p class="g-key">`
- `.v` — 예: `<i class="v">`
- `.t` — 예: `<i class="t">`

**만족도: 문항마다 다섯 단계 100% 막대. <i style="--v:%"> 다섯 개(매우 불만 → 매우 만족)**
- `.likert` — 예: `<div class="likert fill">`
- `.lk` — 예: `<div class="lk is-key">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`
- `.lk-key` — 예: `<p class="lk-key">`

**전후 비교: 사업 전 → 사업 후, 짝마다 한 줄**
- `.ba` — 예: `<div class="ba">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`
- `.ba-head` — 예: `<p class="ba-head">`

**우수 사례: 사진 자리 + 학교 · 한 줄 성과 + 참여자 목소리**
- `.case` — 예: `<div class="case fill">`
- `.ph` — 예: `<div class="ph">`
- `.c-body` — 예: `<div class="c-body">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**향후 계획: 단계 머리(화살 띠) + 단계별 할 일**
- `.road` — 예: `<div class="road fill">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**한 문장: 장 가운데 큰 문장 하나 + 받치는 말 한 줄(.title 없이 .kicker 아래에)**
- `.say` — 예: `<div class="say fill">`

**항목: 번호 + 이름 + 설명. 3~5줄(5줄이면 설명은 한 줄)**
- `.points` — 예: `<ol class="points fill">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**용어 정의: 왼쪽 용어, 오른쪽 뜻 한 문장 + 예 한두 개**
- `.define` — 예: `<dl class="define fill">`

**인용: 말 1~3개. 말한 사람은 figcaption**
- `.quote` — 예: `<div class="quote fill">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**체계: 맨 위 하나(.t-top) → 가운데 갈래(.t-mid) → 갈래마다 할 일 목록(ul). 갈래 수는 style="--n:3"**
- `.tree` — 예: `<div class="tree fill" style="--n:3">`
- `.t-top` — 예: `<div class="t-top">`
- `.t-mid` — 예: `<div class="t-mid is-key">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**추이: 시점마다 세로 막대. style="--v:62"(가장 큰 값 = 100). 3~8시점**
- `.trend` — 예: `<div class="trend fill">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**구성비: 100% 막대 하나(.sh-bar, <i style="--v:%"> 합 100) + 조각 설명(ul, 같은 순서)**
- `.share` — 예: `<div class="share fill">`
- `.sh-bar` — 예: `<div class="sh-bar">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**화면 짚기: 화면 캡처 자리(.shot-img 안 .ph) + 번호 표시(<b style="--x:%;--y:%">) + 번호별 설명(ol)**
- `.shot` — 예: `<div class="shot fill">`
- `.shot-img` — 예: `<div class="shot-img">`
- `.ph` — 예: `<div class="ph">`
- `.is-key` — 예: `<div class="fix is-key" data-step="2">`

**질문: 큰 질문(.a-q) + 보기(ol, 4개까지) 또는 답(.a-a). 답은 data-step 으로 가렸다 연다**
- `.ask` — 예: `<div class="ask fill">`
- `.a-q` — 예: `<p class="a-q">`
- `.a-a`

**할 일: 지금 할 일 한 문장(.t-do) + 시간 · 결과물 · 도움 받을 곳 같은 조건 칸(dl)**
- `.todo` — 예: `<div class="todo fill">`
- `.t-do` — 예: `<p class="t-do">`

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

부품 모양 · 크기가 궁금하면 `https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/F.css`를 봅니다(HTML에 옮겨 쓰지 마세요).
