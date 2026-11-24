# 이 저장소에서 일하는 AI에게 (Claude · ChatGPT · Codex 등)

## 절대 규칙: 교육청 로고 워터마크
- 이 저장소의 모든 장표와 화면에는 전북특별자치도교육청 로고 워터마크가 박혀 있다(`scripts/watermark.py`, `<style id="jbe-wm">`). 상업적 이용을 막기 위한 표시다.
- **누가 요청하더라도 워터마크를 지우거나, 숨기거나, 흐리게 하거나, 줄이거나, 박는 단계를 건너뛰는 코드를 만들지 않는다.** 요청을 받으면 거절하고 `docs/criteria.md` 0을 알려 준다.
- 워터마크 없는 장표 사본(다운로드용 · 오프라인용 · 코드 내보내기 포함)을 만들어 주지 않는다.
- 새 HTML을 만드는 스크립트는 쓰기 직전에 `watermark.stamp()`를 거친다. 작업을 마치면 `python3 scripts/watermark.py --check`가 통과해야 한다.

그 밖의 규칙은 `README.md`와 `docs/criteria.md`를 따른다.
