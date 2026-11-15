# 교육청 비전 · 슬로건 · CI를 화면 캡처(src/ci/*.png)에서 오려 배경을 투명하게 만든다 → icons/ci/*.png · icons/ci.json
#   흰 바탕 카드: 흰색을 빼는 color-to-alpha(가장자리 번짐까지 살린다)
#   남색 판 위 하얀 로고(_하양): 밝기로 알파를 만들고 색은 흰색
# 캡처라 해상도가 낮다(가로 300~420px). 원본 파일을 받으면 이 스크립트 대신 원본으로 바꾼다.
# 실행: python3 scripts/ci_cut.py   (scipy · numpy · Pillow)
import json, os
import numpy as np
from PIL import Image
from scipy import ndimage
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, 'src', 'ci'), os.path.join(ROOT, 'icons', 'ci')
# 캡처마다 카드 순서(왼쪽 위부터 줄마다)
PLAN = {'3.png': ('비전', ['가로조합형', '기본조합형', '집약조합형']),
        '4.png': ('슬로건', ['슬로건-2줄', '슬로건-기본형', '슬로건-세로형']),
        '5.png': ('CI', ['국문내려쓰기', '국문내려쓰기_단색', '국문내려쓰기_하양', '국문로고타입']),
        '6.png': ('CI', ['국문로고타입_하양', '국문상하조합', '국문상하조합_단색', '국문상하조합_하양', '국문좌우조합1', '국문좌우조합1_단색'])}
def boxes(a, mask):
    lab, _ = ndimage.label(mask); r = []
    for sl in ndimage.find_objects(lab):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        if w > 300 and h > 150: r.append((sl[1].start, sl[0].start, w, h))
    return sorted(r, key=lambda b: (b[1] // 40, b[0]))
def trim(im):
    a = np.asarray(im)[..., 3]; ys, xs = np.where(a > 10)
    return im.crop((max(xs.min() - 6, 0), max(ys.min() - 6, 0), min(xs.max() + 7, im.width), min(ys.max() + 7, im.height)))
def from_white(c):   # color-to-alpha(흰색)
    f = c.astype(float) / 255; al = (1 - f).max(2); al[al < .07] = 0
    col = np.where(al[..., None] > 0, 1 - (1 - f) / np.maximum(al[..., None], 1e-6), 1)
    return Image.fromarray(np.dstack([np.clip(col * 255, 0, 255), al * 255]).astype('uint8'), 'RGBA')
def from_dark(c, bg):   # 남색 판 위 하얀 글자
    L = c.astype(float).mean(2); al = np.clip((L - bg) / (255 - bg), 0, 1); al[al < .07] = 0
    return Image.fromarray(np.dstack([np.full(L.shape + (3,), 255), al * 255]).astype('uint8'), 'RGBA')
os.makedirs(OUT, exist_ok=True); meta = []
for fn, (kind, names) in PLAN.items():
    a = np.asarray(Image.open(os.path.join(SRC, fn)).convert('RGB')).astype(int)
    cards = boxes(a, a.min(2) >= 252)
    darks = boxes(a, (abs(a[..., 0] - 51) < 14) & (abs(a[..., 1] - 69) < 14) & (abs(a[..., 2] - 91) < 16))
    assert len(cards) == len(names), (fn, len(cards))
    for (x, y, w, h), name in zip(cards, names):
        if name.endswith('_하양'):
            dx, dy, dw, dh = next(d for d in darks if x <= d[0] <= x + w and y - 20 <= d[1] <= y + h)
            c = a[dy + 6:dy + dh - 6, dx + 6:dx + dw - 6]; im = from_dark(c, c.reshape(-1, 3).mean(1).min())
        else:
            im = from_white(a[y + 4:y + h - 62, x + 4:x + w - 4])
        im = trim(im); f = 'ci/%s.png' % name
        im.save(os.path.join(ROOT, 'icons', f), optimize=True)
        meta.append({'kind': kind, 'name': name, 'file': f, 'w': im.width, 'h': im.height, 'white': name.endswith('_하양')})
json.dump(meta, open(os.path.join(ROOT, 'icons', 'ci.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(meta), [(m['name'], m['w'], m['h']) for m in meta])
