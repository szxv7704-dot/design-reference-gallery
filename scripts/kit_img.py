# 계열 키트의 얼굴 그림(kit/img/): 근거 키트 장표(#91 나이테 · #103 밤하늘 · #110 막새)의 캔버스 그림을 이미지 파일로 떠낸다.
# 그림을 새로 그리는 것이 아니라, 이미 만든 장표의 그림을 그대로 옮기는 일이다(제작 기준 4: 그림은 이미지로).
# 실행: node scripts/kit_img.js <임시 폴더>  →  python3 scripts/kit_img.py <임시 폴더>     (Playwright · Pillow · numpy)
import os, sys
import numpy as np
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C, O = sys.argv[1], os.path.join(ROOT, 'kit', 'img')
os.makedirs(O, exist_ok=True)
op = lambda n: Image.open(os.path.join(C, n))
def save(im, name, q=84, maxw=None):
    if maxw and im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(os.path.join(O, name), 'WEBP', quality=q, method=6); print(name, im.size, os.path.getsize(os.path.join(O, name)) // 1024, 'KB')
def paper_to_alpha(im, cut=0.05):
    """종이 바탕째 그려진 그림에서 바탕(네 귀퉁이 평균색)을 투명으로: 어떤 바탕 위에 올려도 가장자리가 안 보이게"""
    a = np.asarray(im.convert('RGB')).astype(np.float32) / 255
    P = np.concatenate([a[:12, :12].reshape(-1, 3), a[:12, -12:].reshape(-1, 3), a[-12:, :12].reshape(-1, 3), a[-12:, -12:].reshape(-1, 3)]).mean(0)
    al = np.clip(((P - a) / P).max(2), 0, 1); al = np.where(al < cut, 0, (al - cut) / (1 - cut))
    rgb = np.where(al[..., None] > 0, (a - (1 - al[..., None]) * P) / np.maximum(al[..., None], 1e-4), 0)
    return Image.fromarray((np.clip(np.dstack([rgb, al]), 0, 1) * 255).astype(np.uint8), 'RGBA')
def clean(im, th=22):
    """아주 옅은 알파(종이 결 잡음)를 지워 파일을 줄인다"""
    a = np.asarray(im).copy(); a[a[..., 3] < th] = 0; return Image.fromarray(a, 'RGBA')
# ── E 나무 단면(투명 바탕): 다 자란 단면 + 간지 상태 다섯(같은 틀, 겹이 자란다. 점선 = 다 자랐을 때 크기)
save(clean(op('91-init-2-ps91-cv-2316x1303.png').crop((1329, 217, 2231, 1187))), 'E-full.webp', q=80, maxw=680)
for k in range(1, 6): save(clean(op('91-s%d-1-ps91-cv-2316x1303.png' % k).crop((1301, 215, 2301, 1215))), 'E-s%d.webp' % k, q=80, maxw=680)
# ── G 밤하늘(바탕) + 별자리(투명 겹): 간지 상태 다섯 + 다 이어진 것
for tag, n in (('toc', '103-init-0'), ('divider', '103-init-2'), ('close', '103-init-4')):
    save(op(n + '-gk-sky-2356x1325.png').convert('RGB'), 'G-sky-%s.webp' % tag, q=86, maxw=1920)
for k in range(1, 6): save(op('103-s%d-3-gk-con-2356x1325.png' % k), 'G-con-s%d.webp' % k, q=92, maxw=1920)
save(op('103-init-5-gk-con-2356x1325.png'), 'G-con-all.webp', q=92, maxw=1920)
# ── H 막새(한지 바탕을 투명으로): 큰 막새 하나 · 처마 줄 상태 다섯 · 처마 끝
save(paper_to_alpha(op('110-init-2-plain-515x515.png')), 'H-big.webp', q=90)
for k in range(1, 6): save(paper_to_alpha(op('110-s%d-1-hk-cv-2356x1325.png' % k).crop((1260, 836, 2316, 1060))), 'H-s%d.webp' % k, q=88)
save(paper_to_alpha(op('110-init-3-hk-cv-2356x1325.png').crop((1200, 320, 2336, 800))), 'H-roof.webp', q=88)
