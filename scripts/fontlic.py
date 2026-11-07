# 글꼴 라이선스(SIL OFL 1.1) 도우미 — pack_fonts.py · build.py 가 함께 쓴다.
#  - 조건 2: 사본마다 저작권 고지와 라이선스를 함께 → 줄인 글꼴에도 이름표 0(저작권) · 13(라이선스) · 14(주소)를 남긴다
#  - 조건 3: 수정본(글자를 줄인 것 포함)은 예약 이름(Reserved Font Name)을 글꼴 이름으로 쓰지 못한다
#           → 저작권 문구에 적힌 예약 이름이 글꼴 이름에 들어 있으면 'DRG'로 바꾼다(CSS 에서 부르는 이름은 그대로)
# 실행: python3 scripts/fontlic.py          → fonts/LICENSES.md 다시 만들기
#       python3 scripts/fontlic.py --fix    → fonts/*.woff2 의 예약 이름도 바꾼 뒤 LICENSES.md 만들기
import glob, os, re, sys
from fontTools.ttLib import TTFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEEP_NAME_IDS = [0, 1, 2, 3, 4, 5, 6, 13, 14, 16, 17]
RENAME_IDS = (1, 3, 4, 6, 16, 17, 18, 21, 22, 25)
SUB = 'DRG'   # design-reference-gallery

def name(f, i):
    return (f['name'].getDebugName(i) or '').strip()

def reserved(f):
    txt = name(f, 0) + ' ' + name(f, 13)
    out = []
    for m in re.finditer(r'reserved\s+font\s+names?\s*((?:["\'‘“][^"\'’”]+["\'’”]\s*(?:,|and)?\s*)+)', txt, re.I):
        out += re.findall(r'["\'‘“]([^"\'’”]+)["\'’”]', m.group(1))
    return out

def clean(f):
    """예약 이름이 글꼴 이름에 들어 있으면 바꾼다. 바꾼 (예약 이름, 새 이름) 목록을 돌려준다."""
    done = []
    for rfn in reserved(f):
        for rec in f['name'].names:
            if rec.nameID in RENAME_IDS:
                s = rec.toUnicode()
                if rfn in s:
                    rec.string = s.replace(rfn, SUB)
                    done.append((rfn, rec.toUnicode()))
    return done

def notice(fam, f):
    """사람이 읽는 고지 한 줄: 가족 이름 — 저작권"""
    c = re.sub(r'\s+', ' ', name(f, 0)).replace('*/', '* /')
    return '%s — %s' % (fam, c)

def write_index():
    rows = {}
    for p in sorted(glob.glob(os.path.join(ROOT, 'fonts', '*.woff2'))):
        key, w = os.path.basename(p)[:-6].rsplit('-', 1)
        f = TTFont(p)
        r = rows.setdefault(key, {'w': [], 'c': name(f, 0), 'lic': name(f, 13), 'url': name(f, 14), 'n': name(f, 1), 'rfn': reserved(f)})
        r['w'].append(w)
    L = ['# 글꼴 라이선스', '',
         '이 저장소의 `fonts/*.woff2`와, 빌드가 장표(`refs/*.html`)에 잘라 넣은 글꼴은 모두 **SIL Open Font License 1.1** 글꼴의 수정본(글자를 줄인 것)입니다. 라이선스 전문은 [`OFL.txt`](OFL.txt)에 있습니다.', '',
         '- 원본은 `scripts/fetch_fonts.py`가 [google/fonts](https://github.com/google/fonts)의 `ofl/` 디렉터리에서 받습니다(원본 ttf는 저장소 밖).',
         '- 줄인 글꼴에도 이름표 0(저작권) · 13(라이선스) · 14(라이선스 주소)를 남기고, 장표 HTML의 글꼴 앞에는 사람이 읽는 고지 주석을 붙입니다(OFL 조건 2).',
         '- 저작권 문구에 **예약 이름**(Reserved Font Name)이 있고 그것이 글꼴 이름에 들어 있으면, 수정본의 글꼴 이름에서 `%s`로 바꿉니다(OFL 조건 3). 장표 CSS에서 부르는 이름은 그대로입니다.' % SUB,
         '- 나눔 글꼴 일부는 파일 안 라이선스 칸에 `NHN Corporation`만 적혀 있지만, google/fonts에서 `OFL.txt`와 함께 OFL로 배포되는 파일입니다.',
         '- 이 표는 `python3 scripts/fontlic.py`로 파일 안 정보를 읽어 만듭니다. 손으로 고치지 마세요.', '',
         '| 글꼴(파일 이름) | 굵기 | 저작권 (파일 안 표기) | 예약 이름 | 파일 안 라이선스 표기 |', '|---|---|---|---|---|']
    for k, r in rows.items():
        lic = 'SIL OFL 1.1' if 'Open Font License' in r['lic'] or 'OpenFontLicense' in r['url'] else (r['lic'] or '—') + ' → OFL (google/fonts `ofl/`)'
        L.append('| %s | %s | %s | %s | %s |' % (k, ' · '.join(sorted(r['w'])), r['c'].replace('|', '/'), ', '.join(r['rfn']) or '—', lic))
    open(os.path.join(ROOT, 'fonts', 'LICENSES.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    return rows

if __name__ == '__main__':
    if '--fix' in sys.argv:
        for p in sorted(glob.glob(os.path.join(ROOT, 'fonts', '*.woff2'))):
            f = TTFont(p); d = clean(f)
            if d: f.flavor = 'woff2'; f.save(p); print('예약 이름 바꿈', os.path.basename(p), sorted({x[1] for x in d})[:3])
    rows = write_index()
    print('LICENSES.md', len(rows), '가족')
