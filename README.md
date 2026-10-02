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
| `scripts/thumb.js` | 썸네일 생성: `node scripts/thumb.js refs/NN.html thumbs/NN.jpg` (Playwright 필요) |

## 갱신 방식

claude.ai 루틴이 새 레퍼런스를 만들 때마다 `refs/`, `thumbs/`, `data/rounds.json`을 갱신해 `main`에 푸시합니다.
푸시되면 GitHub Pages가 자동으로 다시 배포합니다.
