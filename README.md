# 발표자료 디자인 레퍼런스 갤러리

한글 문서(계획안 · 연수 강의안 · 성과 보고)를 **16:9 발표 덱**으로 바꿀 때 **채팅 AI가 읽는 디자인 안내이자 재료**입니다. GitHub Pages로 공개됩니다.
쓰는 법: Claude · ChatGPT에 문서를 올리고 이 갤러리 주소(https://szxv7704-dot.github.io/design-reference-gallery/)를 주면, AI가 첫 화면의 안내를 읽고 덱 HTML을 만듭니다.
분류 틀은 [`docs/patterns.md`](docs/patterns.md), 기존 장표 판정은 [`docs/triage.md`](docs/triage.md), 만드는 규칙은 [`docs/criteria.md`](docs/criteria.md).
모든 기관명 · 사업 · 수치는 **가상 예시**이고, 사진은 AI로 만든 것입니다.

## 세 층

| 층 | 무엇 | 원본 |
|---|---|---|
| 기본 장표 | 내용의 모양 23가지(표지 · 항목 · 둘 비교 · 추이 · 화면 짚기 …). 한 장에 하나 | `data/patterns.json` · 부품 `kit/parts.css` + `kit/{계열}.css` |
| 흐름 | 기본 장표를 순서대로 엮은 것: 계획안 발표 · 성과 공유회 · 사업 설명회 · 연수 한 차시 | `data/flows.json` · 예시 덱 `src/flows/{plan,share,brief,lecture,lecture2,lecture3}.html` |
| 분위기 | 색 · 글꼴 · 상징 부품: A 픽셀 게임 · B 미니멀 스튜디오 · C 경쾌한 놀이 오브젝트 · D 인쇄·종이 에디토리얼 · E 자연 재질 · F 관측·중계 인포그래픽 · G 어두운 콘셉트 · H 전통 공예·문양 | `kit/{계열}.css` · `kit/{계열}.design.md` |

자료는 **재료**(AI가 그대로 조립하는 덱 키트 부품)와 **참고**(기존 레퍼런스 장표 — 변주 · 영감)로 나뉩니다.

## 구조

| 경로 | 내용 |
|---|---|
| `index.html` | 첫 화면. **`scripts/site.py`가 만든다(손으로 고치지 말 것).** 내용이 모두 HTML 안에 들어 있어 AI가 주소만으로 글로 읽는다. 순서: 쓰는 법 → 분위기 여덟 → AI가 지킬 것 → 흐름(자리 띠 + 예시 덱 장들) → 기본 장표 23(견본 그림 · 내용 조건 · 견본 코드 · 참고할 변주) → 뼈대 · 상징 부품 · 점검 → 참고 서랍(영감 · 인쇄물). 분위기를 고르면 견본 그림이 그 계열로 바뀐다(`?fam=A`) |
| `guide.md` | 첫 화면과 같은 내용의 AI용 안내(글). `scripts/kit.py`가 만든다. 주소를 못 읽는 AI에는 이 파일을 첨부 |
| `kit/` | 덱 키트: 공용 부품 · 계열 CSS · 예시 덱 여섯(`{계열}.html` 성과 공유회 · `-plan` 계획안 발표 · `-brief` 사업 설명회 · `-lecture` · `-lecture2` · `-lecture3` 연수 1 ~ 3차시) · 계열별 지시서 `{계열}.md` · 배포판 `v1/` |
| `data/patterns.json` · `data/flows.json` | 기본 장표 23 · 흐름 넷의 정의(안내문 · 첫 화면 · 판정표가 모두 이것을 읽는다) |
| `data/triage.json` · `docs/triage.md` | 기존 장표 판정(기본 후보 · 변주 · 영감 · 범위 밖): `python3 scripts/triage.py`. 판정은 스크립트 안 `BODY`와 규칙을 고친다 |
| `data/kit_slides.json` | 예시 덱의 장 목록(흐름 · 장 · 기본 장표): `scripts/kit.py`가 만든다 |
| `docs/criteria.md` | 제작 기준(대상 · 그림 규칙 · 피할 것 · 루틴에 붙일 규칙) |
| `refs/NN.html` · `thumbs/NN.jpg` · `data/rounds.json` | 레퍼런스 장표 원본 · 썸네일 · 목록(루틴이 갱신). 첫 화면에서는 '참고할 변주'와 참고 서랍에 나온다 |
| `assets/` | 코드 칸에서 불러오는 사진(20KB 넘는 내장 사진을 뺀 것) |
| `scripts/add-code.js` | 표지 장표만 떼어 낸 "HTML로 가져다 쓰기" 코드 칸을 페이지 끝에 붙임: `node scripts/add-code.js refs/NN.html` |
| `scripts/thumb.js` | 썸네일 생성: `node scripts/thumb.js refs/NN.html thumbs/NN.jpg` (Playwright 필요) |

다시 만드는 순서(키트 · 흐름 · 판정 · 화면):

```
python3 scripts/kit.py             # 여덟 계열 전부(몇 개만: kit.py F H): 배포 CSS · 예시 덱 48개 · 지시서 · guide.md · data/kit_slides.json
node scripts/kit_thumbs.js         # 예시 덱 썸네일
python3 scripts/triage.py          # 판정표
python3 scripts/site.py            # 첫 화면
node scripts/check.js kit A A-plan A-brief A-lecture A-lecture2 A-lecture3 …   # 넘침 · 글자 크기(덱 이름 = kit/ 의 파일 이름)
```

## 레퍼런스 장표의 옛 분류 (rounds.json 필드)

아래는 `data/rounds.json`에 남아 있는 필드의 뜻입니다. 첫 화면은 이 분류 대신 기본 장표(`pattern`)와 판정을 씁니다. 새 장표에는 `pattern`을 적습니다.


맨 위는 **무엇을 만드나**(`use`), 그 아래는 모든 장표에 공통인 필터, 마지막으로 용도별 전용 필터.

### 1. 역할 — `role` (모든 장표에 하나, 한 가지 기준: "이 장표는 어디에 쓰이나")
| 역할 | 판정 기준 | 예 |
|---|---|---|
| `표지` | 가장 큰 글자가 사업 이름. 덱의 첫 장, 분위기를 정한다 | #17, #58, #71 |
| `본문` | 섹션 머리말 + 결론 한 문장 제목 + 도식. 표지 뒤 한 장 | #20, #47~#57 |
| `목차·간지` | 목차·섹션 간지·마무리(계열 키트) | #46, #52, #62 |
| `발표 틀` | 한 장이 아니라 여러 화면을 넘기는 진행 방식(허브·스크롤·카드 넘김·탐험 지도) | #33, #34, #35, #75 |
| `인쇄·홍보물` | 화면 발표가 아닌 종이·게시용(포스터·리플렛·소식지·배너·티켓) | #63~#70 |

`type`(실험형·실무형·계열키트·인쇄물)은 만든 경로 기록으로만 남긴다. 갤러리는 `role`로 나눈다(없으면 type으로 추정). `use`는 role에서 나온다(인쇄·홍보물이면 "인쇄·홍보물", 나머지는 "발표 덱").

### 2. 공통 필터 (모든 장표에 적는다)
- `family` **분위기**: A 픽셀 게임 · B 미니멀 스튜디오 · C 경쾌한 놀이 오브젝트 · D 인쇄·종이 에디토리얼 · E 자연 재질 · F 관측·중계 인포그래픽 · G 어두운 콘셉트 · H 전통 공예·문양. 본문 요소는 `family` 대신 어울리는 분위기 목록 `families`.
- `motion` **움직임**: `정지` / `모션`(저절로 움직임) / `인터랙션`(눌러서·넘겨서 조작)
- `domain` **분야**: `학생·교육과정` / `돌봄·유아` / `특수교육` / `업무·행정` / `시설·안전` / `지역·문화`. 세부 주제는 `topic`(검색으로 찾는다).
- `series` **시리즈**(선택): 한 캠페인으로 묶이는 장표들의 이름(예: `업무도구 나눔`).

### 3. 전용 필터
- 본문(`role: 본문`)
  - `info_type`: 비전 체계도, 현안→해결방안, 배경·목적, 분류·유목화, 흐름·절차, 조직·체계, 일정, 핵심 수치, 비교·순위, 추이, 구성비, 표·목록, 지도·분포
  - `modules`: 장표 안 모듈 1~3개(셰브런 단계, 현안→해결 표, 위계도, 방사형, 순환, 깔때기, 매트릭스, 비교 VS, 카드 묶음, 수치 타일, 막대, 선, 도넛, 표, 타임라인, 간트, 지도)
  - `kind` **정형 유형**(새 장표는 이것을 적는다): 사업 개요 · 추진 체계 · 추진 경과 · 주요 추진 내용 · 핵심 성과 · 목표 대비 달성 · 전년 대비·비교 · 추이 · 구성비 · 참여 분포 · 우수 사례 · 참여자 목소리 · 만족도 · 전후 비교 · 시사점·과제 · 향후 계획 · 단계·절차 · 요약표 · 자주 묻는 질문. 없으면 `info_type`에서 옮겨 센다(docs/criteria.md 3). 갤러리 '무엇을 보여 주나'가 이것이다.
  - `section`: (옛 기준) 계획안 속 위치. 갤러리에서는 더 쓰지 않는다.
- 숨기기: `hidden: true` · `hide_reason` — 제작 기준에 걸린 장표. 파일은 남기고 목록에서만 뺀다.
  - `texture`: 평면 / 약한 입체 / 재질, `deck_ok`·`deck_note`: 덱에 넣으면 안 되는 요소와 그 이유
- 인쇄·홍보물
  - `print_kind`: `포스터` / `리플렛·소책자` / `소식지` / `배너` / `티켓·굿즈` (여러 개 가능)
  - `format`: 판형 설명(예: `A3 세로 포스터 + A4 3단 접지 리플렛`)

카드 표시: 움직임은 `■ 정지`·`▶ 모션`·`◉ 인터랙션` 꼬리표로 늘 보이고, `deck_ok: false`인 요소는 흐린 썸네일·점선 테두리와 `실패 사례 · 덱 제외` 꼬리표로 구분한다(배울 점은 `deck_note`).

분위기 필터: 자기 분위기(`family`)가 있는 장표는 그것으로, 중립 장표(본문)는 어울리는 분위기 목록(`families`)으로 걸린다. 칩 숫자는 지금 고른 역할 안에서 센다.

## 갱신 방식

claude.ai 루틴이 새 레퍼런스를 만들 때마다 `refs/`, `thumbs/`, `data/rounds.json`을 갱신해 `main`에 푸시합니다.
푸시되면 GitHub Pages가 자동으로 다시 배포합니다.

`data/rounds.json`의 각 항목에는 `v`(HTML·썸네일 내용의 md5 앞 8자리)가 있습니다. 갤러리는 링크와 썸네일 주소 뒤에 `?v=`를 붙여, 같은 번호를 재작업해도 브라우저 캐시 때문에 옛 버전이 보이지 않게 합니다.

새 회차를 `refs/`에 넣은 뒤에는 `node scripts/add-code.js refs/NN.html`로 코드 칸을 붙이고, `python3 scripts/ingest.py NN`으로 `src/` 추출 → 빌드 → 오프라인 검사 → `v` 재계산을 한 번에 합니다.

## 소스와 빌드 (인터넷 없이 도는 장표)

`refs/{번호}.html`은 **빌드 결과물**입니다. 직접 고치지 말고 `src/{번호}/`를 고친 뒤 빌드합니다.

| 위치 | 내용 |
|---|---|
| `src/{번호}/page.html` | 페이지 원본. 글꼴 · 큰 그림 · 외부 라이브러리 자리는 `/*@@FONTS@@*/` · `@@ASSET:이름@@` · `@@IMPORTMAP:three@@` 자리표시 |
| `src/{번호}/assets/` | 페이지에 들어가는 사진 · 조각 그림 원본 |
| `src/{번호}/build.json` | 쓰는 글꼴(가족 · 굵기) · 자산 목록 · 외부 라이브러리 |
| `fonts/*.woff2` | 글꼴 원본(OFL). 한글 2,350자 + 영문 · 문장부호 + 갤러리에 쓰인 글자 |
| `vendor/three/` | three.js r160(MIT) 사본 |

```
python3 scripts/build.py 109        # src/109 → refs/109.html  (all = 전부)
node scripts/check.js refs          # 바깥 연결을 막고 전 장표 검사 → check/report.json
python3 scripts/extract.py 110      # (옛 장표를 src/ 로 옮길 때만) refs → src
python3 scripts/ingest.py 111       # 새 회차: 추출 → 없는 글꼴 받기 → 빌드 → 검사 → v 재계산 (실패 시 종료 코드 1)
```

- `check.js`는 바깥 연결 · 콘솔 오류 · 글꼴 외에 **장표 규칙**도 봅니다(`data/rounds.json`의 `motion`·`role` 기준, 하나라도 걸리면 실패 → `ingest.py`도 실패).
  - `reduced_motion`: 모션·인터랙션 장표에 `prefers-reduced-motion` 처리가 없음
  - `infinite_under_reduce`: 움직임 줄이기를 켜도 무한 반복 애니메이션(안내 깜빡임 등)이 계속 돎
  - `print_css`: 인쇄·홍보물에 `@media print`가 없음
  - `slide_overflow` · `small_text`: 덱 키트 예시 덱의 장마다 내용이 1920 × 1080 밖으로 나가거나 글자가 22px 미만
  - `stage_ratio` · `stage_overflow`: 덱 장표(`.stage-frame` 안 무대)가 16:9가 아니거나 내용이 무대 밖으로 넘침
  - 움직임 줄이기는 장표 CSS(`#psNN-css`) 안에 `animation:none` · 전환 0.01초로 두고, 단계 연출을 스크립트로 돌리는 장표는 `go()`에서 그 단계의 끝 모습으로 바로 보낸다(코드 복사 칸에도 그대로 실림).
- 빌드는 페이지에 쓰인 글자만 잘라 글꼴을 박아 넣고, 그림 · 라이브러리도 파일 안에 넣습니다. 결과물에 바깥 주소가 없습니다(‘코드 복사’ 안의 글은 예외).
- 새 글꼴이 필요하면 `fonts/needed.json`에 적고 `scripts/fetch_fonts.py` → `scripts/pack_fonts.py`(원본 ttf는 저장소 밖).

## 공통 부품: 아이콘 세트

`icons/icons.html`(갤러리에서 열림) · `icons/icons.json` · 원본 페이지 `src/icons/`.

- 85개, 12묶음(사람 · 학교·교육 · 목표·성과 · 분석·자료 · 예산·재정 · 일정·시간 · 행정·문서 · 안전·복지 · 시설·환경 · 디지털 · 소통·홍보 · 체계·흐름).
- 규격: 24×24, 선 1.75, 둥근 끝, `currentColor`. 배지 4종(평행사변형·원·사각·선만)은 `--ds-*` 변수를 따른다.
- 원본 [Tabler Icons](https://tabler.io/icons) © Paweł Kuna, MIT(`icons/LICENSE-tabler.txt`). 선 굵기만 2→1.75로 조정.
- 루틴은 인덱스 DB `icons` 모음(`_set` = 규칙·CSS·SVG 틀, `g01`~`g12` = 묶음별 아이콘)에서 읽어 SVG를 페이지 안에 넣는다.
- 아이콘을 더할 때: `icons/icons.json`에 같은 규격으로 넣고 `src/icons/page.html`의 데이터도 바꾼 뒤 `python3 -c "import sys;sys.path.insert(0,'scripts');import build;build.build('icons','icons')"`로 다시 만든다. 인덱스 DB도 함께 고친다.

## 덱 키트 (재료)

A(픽셀 게임) · B(미니멀 스튜디오) · C(경쾌한 놀이 오브젝트) · D(인쇄·종이 에디토리얼) · E(자연 재질) · F(관측·중계 인포그래픽) · G(어두운 콘셉트) · H(전통 공예·문양) 여덟이 있고, 모음 화면은 `kit/index.html`입니다.
여덟 키트는 **같은 부품 이름**(기본 장표 23가지)을 쓰고, 계열마다 모양과 상징 부품만 다릅니다(A 진행 칸 `.prog` · B 모형대 매스 `.mass` · C 블록 탑 `.blocks` · D 판 번호 `.reg` · E 나이테 `.rings` · F 구간 띠 `.lane` · G 별 잇기 `.stars` · H 막새 줄 `.tiles`).
E ~ H는 근거 장표의 **색 · 글꼴 · 짜임**만 옮겼습니다(근거 장표의 캔버스 · SVG 그림은 제작 기준에 따라 옮기지 않음).
예시 덱의 원본은 계열 공용이고(`src/flows/`), 상징 부품 자리(`@@SIG:cover@@` · `@@SIG:toc:1@@` · `@@SIG:divider:3@@` · `@@SIG:close@@`)만 `scripts/kit.py`가 계열별로 채웁니다.

| 위치 | 내용 |
|---|---|
| `kit/deck.css` · `kit/deck.js` | 모든 계열 공용 바탕 · 엔진: 1920 × 1080 무대 통째 줄이기, ← → · Space · F, 장 수 · 점 · 쪽 표시 자동, `data-steps` 단계 공개, 인쇄 장당 1쪽(16:9), 움직임 줄이기 |
| `kit/parts.css` | 공용 정형 부품(계열 토큰을 따름). 성과 공유회: `.brief` · `.mile` · `.delta` · `.goal` · `.likert` · `.ba` · `.case`(사진 자리 `.ph`) · `.road`. 기본 장표: 한 문장 `.say` · 항목 `.points` · 용어 정의 `.define` · 인용 `.quote` · 체계 `.tree` · 추이 `.trend` · 구성비 `.share` · 화면 짚기 `.shot` · 질문 `.ask` · 할 일 `.todo` |
| `kit/{A~H}.css` | 계열 토큰(`--ds-*`)과 계열 부품(표지 · 목차 · 간지 · 마무리 · 상징 부품 · 카드 · 수치 타일 · 막대 · 현안→해결 · 간트 · 표) + 공용 부품 계열 조정 |
| `kit/{A~H}.design.md` | 계열 디자인 규칙(한글 기준, 손으로 씀) |
| `src/flows/{share,plan,brief,lecture,lecture2,lecture3}.html` | 예시 덱 원본(계열 공용). 흐름과 덱의 짝은 `data/flows.json`(`deck` · `more`). 장마다 `data-pattern` = 기본 장표 id, 장 앞 주석 `<!-- 3. 이름 -->` |
| `src/kit-{A~H}/build.json` | 계열이 쓰는 글꼴(가족 · 굵기) |
| `kit/{계열}.html` · `-plan` · `-brief` · `-lecture` · `-lecture2` · `-lecture3` · `kit/{계열}.md` · `kit/v1/` · `kit/thumbs/` · `guide.md` | **만든 것**: 인터넷 없이 도는 예시 덱 · 계열 지시서 · 배포용 CSS/엔진 · 썸네일 · AI용 안내 |
| `scripts/kit.py`의 `META` | 계열마다 다른 것(근거 장표 · 글꼴 역할 · 한 줄 소개 · 상징 부품 설명) |

```
python3 scripts/kit.py                           # 전부 다시 만들기(계열을 적으면 그 계열만)
node scripts/kit_thumbs.js                       # 예시 덱 썸네일 kit/thumbs/{계열}{-흐름}-{장}.jpg
python3 scripts/kit.py inline B 슬라이드.html      # AI가 만든 덱을 인터넷 없이 도는 파일 하나로
```

- 안내문(`guide.md` · 첫 화면 · 지시서)은 AI와의 계약입니다: 문서 읽기 → 흐름 → 문단마다 기본 장표 → 구성안 확인 → HTML. **문서에 없는 숫자 지어내기 금지**, **한 장에 기본 장표 하나**, **그림은 코드로 그리지 않고 이미지를 요청**, 결론 한 문장 제목, 강조색 한 곳, 높이 예산, 생략 없이 출력, 내보내기 전 점검 7개.
- 기본 장표를 더하거나 고칠 때: `data/patterns.json` → 부품 CSS(`kit/parts.css`) → 예시 덱 원본에 그 장 추가(`data-pattern`) → 위 명령으로 다시 만들기. 견본 코드는 예시 덱에서 그 기본 장표가 처음 나오는 장을 그대로 씁니다.
- 배포판은 `https://szxv7704-dot.github.io/design-reference-gallery/kit/v1/{계열}.css`를 불러오므로 `kit/v1/`은 GitHub Pages에 올라가야 동작합니다. 이미 나간 덱이 깨지지 않게 **있는 클래스의 모양은 바꾸지 않고 더하기만** 합니다. 모양을 바꿔야 하면 버전을 새로(`v2`) 만듭니다.

## 글꼴 라이선스

모든 글꼴은 SIL OFL 1.1입니다. 표는 `fonts/LICENSES.md`, 전문은 `fonts/OFL.txt`.
- 빌드는 줄인 글꼴에도 저작권 · 라이선스 이름표(0 · 13 · 14)를 남기고, 장표 글꼴 앞에 고지 주석을 붙입니다.
- 저작권 문구의 예약 이름(Saira)이 글꼴 이름에 있으면 수정본 이름에서 `DRG`로 바꿉니다(장표 CSS의 이름은 그대로). 도우미: `scripts/fontlic.py`.

## 공통 부품: 와우 포인트 24

`wow/wow.html`(갤러리에서 열림) · 원본 `src/wow/`. 발표 와우 기법 24가지를 여섯 묶음(드러내기·이동 / 대비·전환 / 숫자 체감 / 은유·세계관 / 감각·형식 / 소리가 보이는 모션)으로 모은 9장 덱. 장마다 기법이 실제로 움직이고(← → 넘기기 · R 다시 재생), 인쇄하면 끝 화면으로 한 장씩 나온다.

- 사진 9장(`src/wow/assets/wow-*.webp`)은 `page.html` 맨 위 `--img-A`~`--img-N` 변수로 연결한다(N = 불꽃 배경 밤바다).
- ⑥ 팡! 터뜨리기: 캔버스 입자 불꽃(로켓 → 국화·버들·은빛 불꽃 → 연기·빛 번짐), 글자 없음. ⑥ 타이포 조립: 글자를 가로획·세로획·고리 조각으로 나눠(긴 획은 반으로) 자기 칸 안에서 0.14~0.3초마다 90°·45°로 돌고 자리를 바꾸다 2~2.7초에 맞춘다. 두 카드 모두 '⤢ 크게 보기'로 화면 전체 재생, 인쇄하면 끝 장면 한 장.
- ⑥ 칙칙폭폭 지나가기: 입체 글자(Black Han Sans에 두께) '새로운 출발'의 음절 하나가 객차 한 량. 바퀴 없이 차대·연결고리만 달고 레일 위로 오른쪽에서 들어와 레일 이음매마다 앞 칸부터 덜컹이며 멈추고, 멈출 때 칸끼리 밀렸다 당겨짐. 배경은 이미지 없이 해 질 녘 그러데이션·지평선·레일.
- ⑥ 쿵! 내려앉기: 어두운 무대 위 조명, 그림자가 먼저 커지고 입체 글자 '기간 절반'이 떨어져 착지 → 화면 흔들림·눌렸다 펴짐·바닥 균열·먼지·파편 → 말머리 '그래서 결론은'. 의성어 글자는 쓰지 않음.
- 다시 만들기: `python3 -c "import sys;sys.path.insert(0,'scripts');import build;build.build('wow','wow')"`
