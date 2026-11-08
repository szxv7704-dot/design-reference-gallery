# 덱 키트 만들기: kit/deck.css · kit/deck.js · kit/{계열}.css · kit/{계열}.design.md · src/kit-{계열}/ 에서
#   kit/v1/{계열}.css  배포용 묶음(글꼴 @font-face + 공용 바탕 + 계열 부품) — 채팅 AI가 만든 덱이 불러옴
#   kit/v1/deck.js     공용 엔진
#   kit/{계열}.md      채팅 AI용 지시서(사람 안내 · 계약 · 디자인 규칙 · 부품 사전 · 뼈대 · 엔진 사용법)
#   kit/{계열}.html    인터넷 없이 도는 예시 덱(글꼴 · CSS · 엔진을 파일 안에)
# 실행: python3 scripts/kit.py B
#       python3 scripts/kit.py inline B 슬라이드.html [결과.html]   ← AI가 만든 덱을 인터넷 없이 도는 파일 하나로
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import build
BASE = 'https://szxv7704-dot.github.io/design-reference-gallery/'
K = os.path.join(ROOT, 'kit')
NAMES = {'A': '픽셀 게임', 'B': '미니멀 스튜디오', 'C': '경쾌한 놀이 오브젝트', 'D': '인쇄·종이 에디토리얼', 'E': '자연 재질', 'F': '관측·중계 인포그래픽', 'G': '어두운 콘셉트', 'H': '전통 공예·문양'}
# 계열마다 다른 것: 근거 장표 · 글꼴 역할 · 상징 부품(표지 · 목차 · 간지 · 마무리에 쓰는 이 계열의 얼굴)
META = {
 'A': {'refs': '#9 · #10 · #11 · #12 · #90', 'roles': ('Galmuri11', 'Galmuri11', 'Galmuri11'),
       'sig': '진행 칸(`.prog`)을 씁니다. 칸 수 = 섹션 수, 목차는 다음 칸 `.next`, 간지는 지난 칸 `.done` · 지금 칸 `.now`, 마무리는 모두 `.done`.'},
 'B': {'refs': '#19 · #26 · #28 · #37 · #46 · #116', 'roles': ('Gothic A1', 'IBM Plex Sans KR', 'IBM Plex Mono'),
       'sig': '모형대 매스(`.mass`)를 씁니다. 목차 · 간지의 `.lit` 층 = 지금 섹션(아래층이 1섹션).'},
 'C': {'refs': '#7 · #24 · #29 · #39 · #82', 'roles': ('Black Han Sans', 'IBM Plex Sans KR', 'Fredoka'),
       'sig': '블록 탑(`.blocks`)을 씁니다. 블록 수 = 섹션 수(아래가 1섹션), 간지는 지금 층까지만 놓고 남은 층은 `.ghost`, 마무리는 `.flag`.'},
 'D': {'refs': '#4 · #27 · #32 · #60 · #62', 'roles': ('Noto Serif KR', 'IBM Plex Sans KR', 'Noto Serif KR'),
       'sig': '판 번호(`.reg`)를 씁니다. 큰 명조 숫자 하나에 주홍 판이 4px 어긋나는 곳은 덱 전체에서 간지뿐, 재단 표시(`.crop`)도 간지에만.'},
}
rd = lambda *p: open(os.path.join(*p), encoding='utf-8').read()
def wr(p, s): os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w', encoding='utf-8').write(s)
def fonts_of(fam): return json.load(open(os.path.join(ROOT, 'src', 'kit-' + fam, 'build.json')))['fonts']
LINK = lambda fam: '<link rel="stylesheet" href="%skit/v1/%s.css">' % (BASE, fam)
SCRIPT = '<script src="%skit/v1/deck.js"></script>' % BASE

def hosted(fam):
    faces = ''.join('@font-face{font-family:"%s";font-weight:%s;font-display:swap;src:url("../../fonts/%s-%s.woff2") format("woff2")}\n' % (f, w, f.replace(' ', ''), w) for f, w in fonts_of(fam))
    head = '/* %s %s — 덱 키트 v1 배포용 묶음(scripts/kit.py 가 만듦, 고치지 말 것)\n   글꼴: SIL Open Font License 1.1, 저작권 고지는 %sfonts/LICENSES.md */\n' % (fam, NAMES[fam], BASE)
    wr(os.path.join(K, 'v1', fam + '.css'), head + faces + rd(K, 'deck.css') + '\n' + rd(K, 'parts.css') + '\n' + rd(K, fam + '.css'))
    wr(os.path.join(K, 'v1', 'deck.js'), rd(K, 'deck.js'))

def skeleton(fam):
    s = rd(ROOT, 'src', 'kit-' + fam, 'page.html')
    s = s.replace('<style>\n/*@@FONTS@@*/\n/*@@KIT:%s@@*/\n</style>' % fam,
                  '<!-- 이 계열의 공통 CSS(글꼴 · 색 · 부품). 이 줄은 지우거나 바꾸지 마세요 -->\n' + LINK(fam) +
                  '\n<style>\n/* === 추가 부품: 새 클래스가 꼭 필요할 때만 이 줄 아래에(토큰 변수만 사용) === */\n</style>')
    s = s.replace('<script>\n/*@@KITJS@@*/\n</script>', '<!-- 동작 엔진. 이 줄은 지우거나 바꾸지 마세요 -->\n' + SCRIPT)
    assert LINK(fam) in s and SCRIPT in s, '뼈대 자리표시를 못 찾음'
    return s

def parts(fam, sample):
    """계열 CSS의 '── 이름 ──' 묶음마다 클래스 목록과, 예시 덱에서 그 클래스를 처음 쓴 태그"""
    css = rd(K, fam + '.css') + '\n' + rd(K, 'parts.css'); out = []   # 계열 부품 + 공용 성과 공유회 부품
    for m in re.finditer(r'/\* ── (.+?) ─+.*?\*/\n(.*?)(?=/\* ── |\Z)', css, re.S):
        title, body = m.group(1).strip(), re.sub(r'/\*.*?\*/', '', m.group(2), flags=re.S)
        sel = ' '.join(re.findall(r'([^{}]+)\{', body))
        cls = []
        for c in re.findall(r'\.([a-z][a-z0-9-]*)', sel):
            if c not in cls: cls.append(c)
        rows = []
        for c in cls:
            ex = re.search(r'<[a-z0-9]+[^>]*class="(?:[^"]* )?%s(?: [^"]*)?"[^>]*>' % re.escape(c), sample)
            rows.append('- `.%s`' % c + (' — 예: `%s`' % (ex.group(0)[:140] + ('…' if len(ex.group(0)) > 140 else '')) if ex else ''))
        out.append('**%s**\n%s' % (title, '\n'.join(rows)))
    return '\n\n'.join(out)

CONTRACT = '''## 0. 당신(AI)의 일

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
- 표지 · 목차 · 간지 · 마무리에는 이 계열의 상징 부품인 @@SIG@@
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
'''

def md(fam):
    sample = rd(ROOT, 'src', 'kit-' + fam, 'page.html')
    lic = rd(ROOT, 'fonts', 'LICENSES.md')
    fl = [l for l in lic.splitlines() if l.startswith('| ') and any(l.startswith('| %s ' % f.replace(' ', '')) for f, _ in fonts_of(fam))]
    eng = re.match(r'/\*(.*?)\*/', rd(K, 'deck.js'), re.S).group(1).strip()
    parts_txt = parts(fam, sample)
    L = ['# %s %s — 성과 공유회 · 설명회 발표 덱 지시서 (채팅 AI용)' % (fam, NAMES[fam]), '',
         '> 이 파일을 **ChatGPT · Claude · Gemini 같은 채팅 AI**에게 통째로 주면, 이 디자인으로 사업 성과 공유회 · 사업 설명회 발표 덱을 만들어 주도록 쓴 지시서입니다.',
         '> 디자인 레퍼런스 갤러리(%s)의 %s 계열 장표(%s)에서 뽑은 규칙입니다. 모든 예시 내용은 가상입니다.' % (BASE, fam, META[fam]['refs']), '',
         '## 사용법 (사람이 읽는 안내)', '',
         '1. 채팅 AI 대화창에 **이 파일을 첨부**합니다(안 되면 내용을 끝까지 복사해 붙여 넣기).',
         '2. 만들 발표를 말합니다. 예) "2026 ○○ 사업 성과 공유회, ○○교육청 ○○과. 핵심 성과는 아래 표(출처: ○○ 실적), 우수 사례 3개는 … 덱으로 만들어 줘. 결과는 .html 파일로." 사례 사진이 있으면 함께 올립니다.',
         '3. AI가 먼저 **장별 구성안**(머리말 · 결론 제목 · 부품 · 수치와 출처)을 보여 줍니다. 고칠 곳을 말하거나 "좋아, 만들어 줘".',
         '4. 받은 `슬라이드.html`을 내려받아 더블클릭합니다. → · Space로 넘기고, F는 전체 화면, 인쇄하면 장마다 한 쪽(16:9) PDF가 됩니다.',
         '5. 고칠 곳은 "3장 제목을 ○○로"처럼 말합니다. 코드가 끊기면 "끊긴 곳부터 이어서".', '',
         '알아 둘 점',
         '- 열 때 **인터넷이 필요**합니다(공통 CSS · 엔진 · 글꼴을 `szxv7704-dot.github.io`에서 불러옴). 업무망처럼 인터넷이 막힌 곳에서 발표하려면 저장소에서 `python3 scripts/kit.py inline %s 슬라이드.html`을 실행해 모든 것이 파일 안에 든 판을 만드세요.' % fam,
         '- AI 화면 안의 미리보기에서는 색 · 모양이 안 나올 수 있습니다. 내려받아 브라우저(크롬 · 엣지)로 열면 정상입니다.',
         '- 수치는 AI가 지어내지 않도록 계약에 적어 두었지만, **받은 덱의 숫자를 원자료와 꼭 대조**하세요.',
         '- 개인정보(학생 이름 · 사진 등)는 AI에게 넣지 마세요.', '',
         '## 라이선스', '',
         '- 글꼴: 모두 SIL Open Font License 1.1(전문 %sfonts/OFL.txt). 이 계열이 쓰는 글꼴의 저작권 고지:' % BASE, '',
         '| 글꼴 | 굵기 | 저작권 | 예약 이름 | 라이선스 |', '|---|---|---|---|---|', *fl, '',
         '- 공통 CSS · 엔진 · 이 지시서: 디자인 레퍼런스 갤러리 저장소의 일부(가상 예시 자료).', '',
         '---', '', '# ▼▼▼ 여기부터 AI에게 주는 지시서 ▼▼▼', '',
         '(위의 "사용법"과 "라이선스"는 사람을 위한 안내입니다. AI는 아래를 따르세요.)', '',
         CONTRACT.replace('@@SIG@@', META[fam]['sig']), '---', '',
         '## 1. 디자인 규칙 (`%s` design.md)' % fam, '', '````markdown', rd(K, fam + '.design.md').strip(), '````', '', '---', '',
         '## 2. 글씨체', '',
         ('- 모든 글자(제목 · 본문 · 숫자) %s' if len(set(META[fam]['roles'])) == 1 else '- 제목 %s · 본문 %s · 숫자 %s') % tuple(
             '%s(%s)' % (n, '/'.join(w for f, w in fonts_of(fam) if f == n)) for n in (META[fam]['roles'][:1] if len(set(META[fam]['roles'])) == 1 else META[fam]['roles'])) + '. 공통 CSS가 불러오므로 설치하지 않아도 됩니다(열 때 인터넷 필요).',
         '- 글꼴은 변수로만 지정합니다: `var(--ds-font-title)` · `var(--ds-font-body)` · `var(--ds-font-num)`(숫자 · 영문에만).', '', '---', '',
         '## 3. 부품 사전 (이 계열 CSS에 정의된 클래스)', '',
         '이 목록에 있는 클래스만 씁니다. "예"는 뼈대(4)에서 그 클래스를 처음 쓴 태그입니다. 공용 클래스: `.slide`(장 하나) · `data-steps="n"`(장) + `data-step="k"`(안의 요소, 누를 때마다 하나씩) · `.page-no`(빈 칸, 엔진이 채움).', '',
         parts_txt, '', '---', '',
         '## 4. HTML 뼈대 (예시 덱 13장 — 부품 견본입니다. 장 구성은 따라 하지 말고, 공통 파일 두 줄은 그대로 두며, 장은 내용에 맞게 새로)', '',
         '```html', skeleton(fam).strip(), '```', '', '---', '',
         '## 5. 참고: 엔진 사용법과 계열 CSS (뼈대가 이미 불러옴 — HTML에 옮겨 쓰지 마세요)', '',
         '```text', eng, '```', '',
         '부품 모양 · 크기를 이해하는 데만 쓰세요(`%skit/v1/%s.css`의 계열 부분).' % (BASE, fam), '',
         '```css', rd(K, fam + '.css').strip(), '```', '']
    wr(os.path.join(K, fam + '.md'), '\n'.join(L))

# 갤러리 목록에 넣는 키트 장표: 정형 유형마다 한 장, 계열을 돌려 가며(같은 내용 · 다른 분위기). data/kit_slides.json
KIT_SLIDES = [
  ('B', 3, '사업 개요', '목적 · 대상 · 기간 · 규모 네 칸', '네 칸 중 핵심 한 칸만 강조색 — 사업을 한 장으로 소개'),
  ('D', 4, '추진 경과', '가로 시간선 위 이정표 다섯', '이정표 하나만 강조해 "언제 커졌나"를 짚는다'),
  ('C', 6, '핵심 성과', '큰 숫자 넷 + 전년 대비 증감', '숫자 아래 ▲ 증감과 비교 기준을 한 줄로'),
  ('A', 7, '목표 대비 달성', '달성률 막대 + 목표선', '모자란 지표를 숨기지 않고 강조해 다음 해 과제로 잇는다'),
  ('B', 8, '만족도', '문항별 다섯 단계 100% 막대', '가장 높은 문항 하나를 제목 숫자로 뽑는다'),
  ('D', 9, '전후 비교', '사업 전 → 사업 후 세 짝', '가장 크게 바뀐 짝 하나만 강조'),
  ('C', 10, '우수 사례', '사진 자리 + 학교 · 한 줄 성과 + 인용', '사진은 이미지로 받아 넣고(코드로 그리지 않음), 목소리를 붙인다'),
  ('A', 10, '참여자 목소리', '사례 카드 속 인용 세 개', '학생 · 교사 목소리를 성과 숫자 옆에 둔다'),
  ('B', 12, '향후 계획', '단계 머리 띠 + 단계별 할 일', '다음 해 첫 단계만 강조'),
]
def write_slides():
    import hashlib
    out = []
    for fam, n, kind, title, take in KIT_SLIDES:
        th = 'kit/thumbs/%s-%d.jpg' % (fam, n)
        v = hashlib.md5(open(os.path.join(ROOT, th), 'rb').read()).hexdigest()[:8] if os.path.exists(os.path.join(ROOT, th)) else ''
        out.append({'kit': fam, 'slide': n, 'no': '%s%d' % (fam, n), 'title': title, 'kind': kind, 'role': '본문', 'family': fam,
                    'motion': '정지', 'file': 'kit/%s.html' % fam, 'hash': str(n), 'thumb': th, 'v': v,
                    'takeaway': take, 'topic': '덱 키트 %s %s · 성과 공유회 예시 덱 %d장' % (fam, NAMES[fam], n)})
    wr(os.path.join(ROOT, 'data', 'kit_slides.json'), json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    return len(out)

def inline(fam, src, out):
    s = open(src, encoding='utf-8').read()
    if LINK(fam) not in s or SCRIPT not in s: raise SystemExit('공통 파일 두 줄(<link> · <script src>)을 찾지 못했습니다: ' + src)
    s = s.replace(LINK(fam), '<style>\n/*@@FONTS@@*/\n' + build.kit_css(fam) + '\n</style>').replace(SCRIPT, '<script>\n' + rd(K, 'deck.js') + '\n</script>')
    text = re.sub(r'<script>.*?</script>', '', s, flags=re.S)
    notes = {}; faces = ''.join(build.face(f, w, text, notes) for f, w in fonts_of(fam))
    faces = '/* 글꼴: SIL Open Font License 1.1 (https://openfontlicense.org)\n   ' + '\n   '.join(notes.values()) + ' */\n' + faces
    open(out, 'w', encoding='utf-8').write(s.replace('/*@@FONTS@@*/', faces, 1))
    print('인터넷 없이 도는 파일:', out, os.path.getsize(out) // 1024, 'KB')

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['inline']:
        fam, src = a[1], a[2]; inline(fam, src, a[3] if len(a) > 3 else re.sub(r'\.html?$', '', src) + '-오프라인.html')
    else:
        print('data/kit_slides.json', write_slides())
        for fam in a or ['B']:
            hosted(fam); md(fam); n = build.build('kit-' + fam, K, fam)
            print(fam, 'v1/%s.css' % fam, '%s.md' % fam, os.path.getsize(os.path.join(K, fam + '.md')) // 1024, 'KB', '%s.html' % fam, n // 1024, 'KB')
