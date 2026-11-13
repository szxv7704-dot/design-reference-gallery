# A 픽셀 게임 — 발표 덱 지시서 (채팅 AI용)

> 이 파일을 **Claude · ChatGPT 같은 채팅 AI**에게 자기 문서와 함께 주면, 문서 내용을 이 디자인의 16:9 발표 덱으로 만들어 주도록 쓴 지시서입니다.
> 디자인 레퍼런스 갤러리(https://szxv7704-dot.github.io/design-reference-gallery/)의 A 계열 장표(#9 · #10 · #11 · #12 · #90)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.

## 사용법 (사람이 읽는 안내)

1. 채팅 AI 대화창에 **이 파일과 발표할 문서**(한글 · PDF · 붙여 넣은 글)를 넣습니다.
2. 어떤 자리인지 말합니다. 예) "이 계획안으로 10분짜리 발표 덱을 만들어 줘. 결과는 .html 파일로."
3. AI가 먼저 **장별 구성안**을 보여 줍니다. 고칠 곳을 말하거나 "좋아, 만들어 줘".
4. 받은 `.html`을 내려받아 더블클릭합니다. → · Space로 넘기고, F는 전체 화면, 인쇄하면 장마다 한 쪽(16:9) PDF가 됩니다.
5. 고칠 곳은 "3장 제목을 ○○로"처럼 말합니다. 코드가 끊기면 "끊긴 곳부터 이어서".

알아 둘 점
- 열 때 **인터넷이 필요**합니다(공통 CSS · 엔진 · 글꼴을 `szxv7704-dot.github.io`에서 불러옴). 인터넷이 막힌 곳에서 발표하려면 저장소에서 `python3 scripts/kit.py inline A 슬라이드.html`을 실행해 모든 것이 파일 안에 든 판을 만드세요.
- 수치는 AI가 지어내지 않도록 적어 두었지만, **받은 덱의 숫자를 원문과 꼭 대조**하세요.
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

사용자가 준 **문서**(한글 계획안 · 연수 강의안 · 성과 보고 등)의 내용으로 **16:9 발표 덱 HTML 파일 하나**를 만듭니다.
이 안내의 **기본 장표(3)** · **흐름(4)** · **견본 코드(8)**를 재료로 씁니다. 색 · 글꼴 · 부품 모양은 뼈대(6)의 두 줄이 인터넷에서 불러오므로, **당신이 쓰는 것은 `<section class="slide">`들뿐**입니다.

## 1. 진행 순서

1. **문서를 읽습니다.** 문서가 없으면 달라고 합니다. 발표 자리(계획안 발표 · 성과 공유회 · 설명회 · 연수)와 발표 시간을 모르면 짧게 묻습니다.
2. **흐름을 고릅니다(4).** 문서 종류에 맞는 흐름의 자리 순서를 따르되, 문서에 없는 자리는 뺍니다.
3. **문단마다 기본 장표를 고릅니다(3).** 한 장에 기본 장표 하나. 내용 조건을 넘치면 장을 나눕니다.
4. 분위기 계열은 **A 픽셀 게임**입니다.
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

**계획안 발표** — 계획안 문서의 내용을 발표로 옮길 때 · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/A-plan.html

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

**성과 공유회** — 한 해 사업의 결과를 알릴 때 · 예시 덱 https://szxv7704-dot.github.io/design-reference-gallery/kit/A.html

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

## 5. 분위기 계열: A 픽셀 게임

크림 바탕 위 남색 게임 창, 픽셀 글꼴. 강조는 빨강 낱말 하나와 창 안 금색 한 곳. 어울리는 자리: 학생 · 체험 행사, 가벼운 연수. 자세한 규칙은 아래 '디자인 규칙'.

## 6. HTML 뼈대

```html
<!DOCTYPE html>
<html lang="ko" data-kit="A">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>발표 제목</title>
<!-- 이 계열의 공통 CSS(글꼴 · 색 · 부품). 주소를 바꾸지 마세요 -->
<link rel="stylesheet" href="https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/A.css">
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

이 계열은 진행 칸(`.prog`)을 씁니다. 칸 수 = 섹션 수, 목차는 다음 칸 `.next`, 간지는 지난 칸 `.done` · 지금 칸 `.now`, 맺음은 모두 `.done`.

## 8. 기본 장표별 견본 코드

문구는 모두 가상 예시입니다. **구조와 클래스만 가져오고 문구는 하나도 남기지 않습니다.**

### 표지 · `cover`

- 이런 내용일 때: 문서 제목 · 기관 · 날짜
- 내용 조건: 제목 2줄 이하, 부제 1줄. 넘치면: 부제를 뺀다
- 부품: `.cover`

```html
<section data-pattern="cover" class="slide cover">
  <div class="c-text">
    <span class="c-tag">2027 추진 계획 · 가상 예시</span>
    <h1>학교 문화예술교육<br><em>지역 연계</em> 추진 계획</h1>
    <p class="c-sub">시 지역에서 군 지역으로, 138교에서 200교로</p>
  </div>
  <div class="prog" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
  <p class="c-org"><span>○○교육청 교육과정과</span><span>2027. 2. 10.</span></p>
</section>
```

### 목차 · `toc`

- 이런 내용일 때: 문서의 큰 번호(Ⅰ · Ⅱ · Ⅲ), 차시 순서
- 내용 조건: 3~5줄. 넘치면: 큰 묶음으로 합친다
- 부품: `.toc` + `.toc-list`

```html
<section data-pattern="toc" class="slide toc">
  <div class="s-body">
    <p class="kicker">CONTENTS</p>
    <h2 class="title">차례</h2>
    <ol class="toc-list">
      <li class="is-now"><b>01</b><span>추진 배경</span><span>03</span></li>
      <li><b>02</b><span>목표 · 추진 체계</span><span>04</span></li>
      <li><b>03</b><span>세부 추진 과제</span><span>06</span></li>
      <li><b>04</b><span>일정 · 예산</span><span>08</span></li>
      <li><b>05</b><span>기대 효과</span><span>11</span></li>
    </ol>
  </div>
  <div class="prog" aria-hidden="true"><i class="next"></i><i></i><i></i><i></i><i></i></div>
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
  <div class="prog" aria-hidden="true"><i class="done"></i><i class="done"></i><i class="now"></i><i></i><i></i></div>
  <span class="page-no"></span>
</section>
```

### 맺음 · `closing`

- 이런 내용일 때: 문의처 · 담당 · 다음 차시 예고
- 내용 조건: 두 줄 문장 + 연락처 한 줄. 넘치면: —
- 부품: `.close`

```html
<section data-pattern="closing" class="slide close">
  <h2>어느 학교에서든<br>30분 안에</h2>
  <p>문의 · ○○교육청 교육과정과 문화예술교육 담당</p>
  <div class="prog" aria-hidden="true"><i class="done"></i><i class="done"></i><i class="done"></i><i class="done"></i><i class="done"></i></div>
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
    <p class="kicker">05 기대 효과</p>
    <h2 class="title">가장 먼저 달라지는 것은 <em>군 지역 학교의 이동 시간</em>입니다</h2>
    <ol class="points fill">
      <li class="is-key"><b>이동 시간 절반</b><p>군 지역 학교 평균 62분 → 30분 안</p></li>
      <li><b>참여 학교 200교</b><p>138교에서 62교 늘림, 그중 40교가 군 지역</p></li>
      <li><b>학교 행정 한 번으로</b><p>버스 · 보험 · 인솔을 학교가 따로 계약하지 않음</p></li>
    </ol>
  </div>
  <p class="src">자료: ○○교육청 운영 실적 · 2027 계획(가상 예시)</p>
  <span class="page-no"></span>
</section>
```

### 용어 정의 · `define`

- 이런 내용일 때: "○○란", 용어 풀이, 개념 설명
- 내용 조건: 용어 1개 + 뜻 한 문장 + 예 1~2개. 넘치면: 용어마다 한 장
- 부품: `.define`

### 인용 · `quote`

- 이런 내용일 때: 참여자 말 · 설문 서술 답 · 법령 조문
- 내용 조건: 1~3개, 각 60자 이하, 말한 사람. 넘치면: 가장 강한 것 하나만
- 부품: `.quote`

### 순서·단계 · `steps`

- 이런 내용일 때: 절차 · 신청 방법 · 따라 하기 · 단계별 추진 · 향후 계획
- 내용 조건: 3~4단계, 단계마다 이름 + 할 일 3줄 이하. 넘치면: 5단계부터 두 장
- 부품: `.road`

```html
<section data-pattern="steps" class="slide">
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
```

### 둘 비교 · `compare`

- 이런 내용일 때: 문제점 ↔ 개선 방안, 문단 ↔ 고른 장표, 기존안 ↔ 새 안
- 내용 조건: 2~3줄, 줄마다 왼쪽 · 오른쪽 한 짝. 넘치면: 4줄부터 두 장
- 부품: `.fix` (+ `.stack`) — 누를 때마다 한 줄씩 보이려면 data-step

```html
<section data-pattern="compare" class="slide" data-steps="3">
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
    <p class="kicker">03 세부 추진 과제</p>
    <h2 class="title">여섯 과제 중 <em>이동 지원</em> 둘은 상반기에 끝냅니다</h2>
    <div class="grid g3 fill center">
      <div class="card is-key"><span class="c-no">묶음 1 · 이동</span><h3>찾아가는 교실</h3><p>예술 공간 버스 운영<br>군 지역 거점 지정</p><p class="c-foot">기한 <b>6월</b></p></div>
      <div class="card"><span class="c-no">묶음 2 · 수업</span><h3>함께 짜는 수업</h3><p>공동 설계 연수<br>학년별 수업 모델 개발</p><p class="c-foot">기한 <b>10월</b></p></div>
      <div class="card"><span class="c-no">묶음 3 · 행정</span><h3>한 번에 하는 행정</h3><p>이동 · 보험 일괄 계약<br>신청 서류 줄이기</p><p class="c-foot">기한 <b>3월</b></p></div>
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
    <p class="kicker">01 추진 배경</p>
    <h2 class="title">참여 학교는 4년 새 <em>여섯 배</em>로 늘었습니다</h2>
    <div class="trend fill">
      <div style="--v:17"><b>23<small>교</small></b><i></i><span>2023</span></div>
      <div style="--v:30"><b>41<small>교</small></b><i></i><span>2024</span></div>
      <div style="--v:54"><b>74<small>교</small></b><i></i><span>2025</span></div>
      <div class="is-key" style="--v:100"><b>138<small>교</small></b><i></i><span>2026</span></div>
    </div>
  </div>
  <p class="src">자료: ○○교육청 운영 실적(가상 예시)</p>
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
    <p class="kicker">04 일정 · 예산</p>
    <h2 class="title">계약을 3월에 끝내야 <em>4월 버스 운행</em>이 시작됩니다</h2>
    <div class="gantt fill">
      <span class="g-h">과제</span><span class="g-h">1</span><span class="g-h">2</span><span class="g-h">3</span><span class="g-h">4</span><span class="g-h">5</span><span class="g-h">6</span><span class="g-h">7</span><span class="g-h">8</span><span class="g-h">9</span><span class="g-h">10</span><span class="g-h">11</span><span class="g-h">12</span>
      <span class="g-name">일괄 계약</span><span class="g-bar" style="--from:1;--to:3"></span>
      <span class="g-name">버스 운행</span><span class="g-bar is-key" style="--from:4;--to:12"></span>
      <span class="g-name">거점 지정</span><span class="g-bar" style="--from:3;--to:6"></span>
      <span class="g-name">설계 연수</span><span class="g-bar" style="--from:2;--to:10"></span>
      <span class="g-name">수업 모델</span><span class="g-bar" style="--from:5;--to:10"></span>
    </div>
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

### 질문 · `ask`

- 이런 내용일 때: 여는 질문 · 토의 주제 · 퀴즈 · 자주 묻는 질문
- 내용 조건: 질문 1개 + 보기 4개 이하(ol) 또는 답 1개(.a-a). 넘치면: 질문마다 한 장
- 부품: `.ask` — 퀴즈 답은 .a-a 에 data-step="1" 을 붙여 가렸다 연다. 이 장은 .title 없이

### 할 일 · `todo`

- 이런 내용일 때: 실습 안내 · 과제 · 제출 서류 · 신청 기한
- 내용 조건: 할 일 한 문장 + 조건 칸 2~3개(시간 · 결과물 · 도움). 넘치면: 할 일마다 한 장
- 부품: `.todo` — 이 장은 .title 없이

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

## 디자인 규칙 (`A` design.md)

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

- 글꼴: 모든 글자(제목 · 본문 · 숫자) Galmuri11(400/700). 공통 CSS가 불러오므로 설치하지 않아도 됩니다.
- 글꼴은 변수로만 지정합니다: `var(--ds-font-title)` · `var(--ds-font-body)` · `var(--ds-font-num)`(숫자 · 영문에만).

---

## 부품 사전 (이 계열 CSS에 정의된 클래스 전부)

"예"는 예시 덱에서 그 클래스를 처음 쓴 태그입니다. 공용: `.slide`(장 하나) · `data-steps="n"`(장) + `data-step="k"`(안의 요소, 누를 때마다 하나씩) · `.page-no`(빈 칸, 엔진이 채움).

**공통: 머리말 · 결론 제목 · 쪽 번호 · 출처**
- `.s-body` — 예: `<div class="s-body">`
- `.kicker` — 예: `<p class="kicker">`
- `.title` — 예: `<h2 class="title">`
- `.lead`
- `.fill` — 예: `<div class="trend fill">`
- `.src` — 예: `<p class="src">`
- `.page-no` — 예: `<span class="page-no">`

**게임 창: 먹 테 + 크림 안테 + 모서리 깎기 + 디더 머리줄. 카드 · 타일 · 막대 판 · 간트 · 표가 모두 이 창**
- `.card` — 예: `<div class="card is-key">`
- `.tile` — 예: `<div class="tile is-key">`
- `.bars`
- `.gantt` — 예: `<div class="gantt fill">`
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
- `.cover` — 예: `<section data-pattern="cover" class="slide cover">`
- `.c-text` — 예: `<div class="c-text">`
- `.c-tag` — 예: `<span class="c-tag">`
- `.c-sub` — 예: `<p class="c-sub">`
- `.c-org` — 예: `<p class="c-org">`
- `.prog` — 예: `<div class="prog" aria-hidden="true">`

**목차: 남색 창 안 줄 목록, 지금 장은 금색 테 + ▶ 커서**
- `.toc-list` — 예: `<ol class="toc-list">`
- `.is-now` — 예: `<li class="is-now">`
- `.toc` — 예: `<section data-pattern="toc" class="slide toc">`
- `.prog` — 예: `<div class="prog" aria-hidden="true">`

**간지: 큰 번호 + 섹션 이름 + 진행 칸**
- `.divider` — 예: `<section data-pattern="divider" class="slide divider">`
- `.d-no` — 예: `<div class="d-no">`
- `.prog` — 예: `<div class="prog" aria-hidden="true">`

**마무리**
- `.close` — 예: `<section data-pattern="closing" class="slide close">`
- `.prog` — 예: `<div class="prog" aria-hidden="true">`

**배치 격자**
- `.grid` — 예: `<div class="grid g3 fill center">`
- `.center` — 예: `<div class="grid g3 fill center">`
- `.g2`
- `.g3` — 예: `<div class="grid g3 fill center">`
- `.g4` — 예: `<div class="grid g4 fill center">`
- `.split`
- `.stack` — 예: `<div class="fill stack">`

**카드 묶음(창 하나 = 카드 하나)**
- `.card` — 예: `<div class="card is-key">`
- `.c-no` — 예: `<span class="c-no">`
- `.c-foot` — 예: `<p class="c-foot">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**수치 타일**
- `.tile` — 예: `<div class="tile is-key">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**막대: 칸으로 끊긴 체력 막대. style="--v:42" 는 최댓값 대비 %**
- `.bars`
- `.bar`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**현안 → 해결: 왼쪽은 크림 쪽지, 오른쪽은 남색 창**
- `.fix` — 예: `<div class="fix" data-step="1">`
- `.q` — 예: `<p class="q">`
- `.a` — 예: `<p class="a">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**간트(월 1~12): style="--from:3;--to:6"**
- `.gantt` — 예: `<div class="gantt fill">`
- `.g-h` — 예: `<span class="g-h">`
- `.g-name` — 예: `<span class="g-name">`
- `.g-bar` — 예: `<span class="g-bar" style="--from:1;--to:3">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**표**
- `.tbl` — 예: `<table class="tbl">`
- `.n` — 예: `<td class="n">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`
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
- `.quote`
- `.tree` — 예: `<div class="tree fill" style="--n:3">`
- `.trend` — 예: `<div class="trend fill">`
- `.share` — 예: `<div class="share fill">`
- `.ask`
- `.todo`
- `.say` — 예: `<div class="say fill">`
- `.define`
- `.t-mid` — 예: `<div class="t-mid is-key">`
- `.t-top` — 예: `<div class="t-top">`
- `.a-q`
- `.t-do`
- `.a-a`
- `.shot`
- `.shot-img`
- `.sh-bar` — 예: `<div class="sh-bar">`

**사업 개요: 목적 · 대상 · 기간 · 규모 네 칸**
- `.brief` — 예: `<div class="brief fill">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**추진 경과: 가로 시간선 위 이정표. 날짜는 <time>**
- `.mile` — 예: `<ol class="mile fill">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**증감 표시: 수치 타일 안 <span class="delta">▲ 38교</span> (줄면 .down)**
- `.delta` — 예: `<span class="delta">`
- `.down`

**목표 대비 달성: 실적 막대 + 목표선. style="--v:92;--t:80"(최댓값 대비 %)**
- `.goal` — 예: `<div class="goal fill">`
- `.g-row` — 예: `<div class="g-row" style="--v:88.5;--t:76.9">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`
- `.g-key` — 예: `<p class="g-key">`
- `.v` — 예: `<i class="v">`
- `.t` — 예: `<i class="t">`

**만족도: 문항마다 다섯 단계 100% 막대. <i style="--v:%"> 다섯 개(매우 불만 → 매우 만족)**
- `.likert` — 예: `<div class="likert fill">`
- `.lk` — 예: `<div class="lk is-key">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`
- `.lk-key` — 예: `<p class="lk-key">`

**전후 비교: 사업 전 → 사업 후, 짝마다 한 줄**
- `.ba` — 예: `<div class="ba">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`
- `.ba-head` — 예: `<p class="ba-head">`

**우수 사례: 사진 자리 + 학교 · 한 줄 성과 + 참여자 목소리**
- `.case` — 예: `<div class="case fill">`
- `.ph` — 예: `<div class="ph" data-need="사진 자리 · 4:3 · 공방에서 도자기를 빚는 초등학생">`
- `.c-body` — 예: `<div class="c-body">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**향후 계획: 단계 머리(화살 띠) + 단계별 할 일**
- `.road` — 예: `<div class="road fill">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**한 문장: 장 가운데 큰 문장 하나 + 받치는 말 한 줄(.title 없이 .kicker 아래에)**
- `.say` — 예: `<div class="say fill">`

**항목: 번호 + 이름 + 설명. 3~5줄(5줄이면 설명은 한 줄)**
- `.points` — 예: `<ol class="points fill">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**용어 정의: 왼쪽 용어, 오른쪽 뜻 한 문장 + 예 한두 개**
- `.define`

**인용: 말 1~3개. 말한 사람은 figcaption**
- `.quote`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**체계: 맨 위 하나(.t-top) → 가운데 갈래(.t-mid) → 갈래마다 할 일 목록(ul). 갈래 수는 style="--n:3"**
- `.tree` — 예: `<div class="tree fill" style="--n:3">`
- `.t-top` — 예: `<div class="t-top">`
- `.t-mid` — 예: `<div class="t-mid is-key">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**추이: 시점마다 세로 막대. style="--v:62"(가장 큰 값 = 100). 3~8시점**
- `.trend` — 예: `<div class="trend fill">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**구성비: 100% 막대 하나(.sh-bar, <i style="--v:%"> 합 100) + 조각 설명(ul, 같은 순서)**
- `.share` — 예: `<div class="share fill">`
- `.sh-bar` — 예: `<div class="sh-bar">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**화면 짚기: 화면 캡처 자리(.shot-img 안 .ph) + 번호 표시(<b style="--x:%;--y:%">) + 번호별 설명(ol)**
- `.shot`
- `.shot-img`
- `.ph` — 예: `<div class="ph" data-need="사진 자리 · 4:3 · 공방에서 도자기를 빚는 초등학생">`
- `.is-key` — 예: `<div class="is-key" style="--v:100">`

**질문: 큰 질문(.a-q) + 보기(ol, 4개까지) 또는 답(.a-a). 답은 data-step 으로 가렸다 연다**
- `.ask`
- `.a-q`
- `.a-a`

**할 일: 지금 할 일 한 문장(.t-do) + 시간 · 결과물 · 도움 받을 곳 같은 조건 칸(dl)**
- `.todo`
- `.t-do`

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

부품 모양 · 크기가 궁금하면 `https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/A.css`를 봅니다(HTML에 옮겨 쓰지 마세요).
