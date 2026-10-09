# 발표자료 디자인 레퍼런스 갤러리

계획안 발표자료(PPT·HTML)를 위한 표지·도식 디자인 레퍼런스 모음입니다. GitHub Pages로 공개됩니다.
모든 기관명·계획안·수치는 **가상 예시**입니다.

## 구조

| 경로 | 내용 |
|---|---|
| `index.html` | 갤러리 첫 화면 (`data/rounds.json`을 읽어 카드 목록 표시) |
| `refs/NN.html` | 레퍼런스 원본 페이지 (NN = 회차 번호, 두 자리) |
| `thumbs/NN.jpg` | 표지 썸네일 (640px 폭) |
| `data/rounds.json` | 회차 목록 데이터 |
| `assets/` | 코드 칸에서 불러오는 사진(20KB 넘는 내장 사진을 뺀 것) |
| `scripts/add-code.js` | 표지 장표만 떼어 낸 "HTML로 가져다 쓰기" 코드 칸을 페이지 끝에 붙임: `node scripts/add-code.js refs/NN.html` (실무형처럼 원래 코드 칸이 있으면 건너뜀, 다시 실행하면 새로 만듦) |
| `scripts/thumb.js` | 썸네일 생성: `node scripts/thumb.js refs/NN.html thumbs/NN.jpg` (Playwright 필요) |

## 분류 체계

- **표지(실험형)**: 덱의 분위기를 정하는 첫 장. `family`에 계열 기호를 적는다.
  A 픽셀 게임 · B 미니멀 스튜디오 · C 경쾌한 놀이 오브젝트 · D 인쇄·종이 에디토리얼 · E 자연 재질 · F 관측·중계 인포그래픽 · G 어두운 콘셉트
- **요소(실무형)**: 표지 뒤에 오는 본문 장표.
  - `info_type`: 추이, 비교·순위, 구성비, 분류·유목화, 흐름·절차, 조직·체계, 일정, 핵심 수치, 지도·분포, 표·목록
  - `texture`: 평면 / 약한 입체 / 재질 (재질일수록 어울리는 계열이 좁다)
  - `families`: 어울리는 표지 계열 기호 목록
  - `deck_ok`, `deck_note`: 덱에 넣으면 안 되는 요소와 그 이유
  - `section`: 계획안 속 위치(보조 꼬리표)

갤러리에서 계열을 고르면 그 계열의 표지와 어울리는 요소(덱 제외 빼고)가 함께 나온다.

## 갱신 방식

claude.ai 루틴이 새 레퍼런스를 만들 때마다 `refs/`, `thumbs/`, `data/rounds.json`을 갱신해 `main`에 푸시합니다.
푸시되면 GitHub Pages가 자동으로 다시 배포합니다.

`data/rounds.json`의 각 항목에는 `v`(HTML·썸네일 내용의 sha1 앞 8자리)가 있습니다. 갤러리는 링크와 썸네일 주소 뒤에 `?v=`를 붙여, 같은 번호를 재작업해도 브라우저 캐시 때문에 옛 버전이 보이지 않게 합니다.

새 회차를 `refs/`에 넣은 뒤에는 `node scripts/add-code.js refs/NN.html`을 실행해 코드 칸을 붙이고, `v`를 다시 계산합니다.
