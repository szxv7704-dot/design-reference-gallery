// 와우 포인트 데모 통과 기준 검사(2026-11-28): 사람이 판단할 장면 모음과 기계로 재는 세 기준.
//  ① 폰 글자: 폰 가로 화면(844 × 390)에서 데모 안 글자가 모두 9px 이상(끝 화면 기준)
//  ② 화면 사용: 바탕색이 아닌 칸을 감싸는 사각형이 데모 상자의 60% 이상(가장 넓게 쓴 순간 기준)
//  ③ 빈 화면 없음: 0.4초 뒤부터 그 사각형이 3% 밑으로 떨어지는(단색만 남는) 순간이 없음
//  ④ 같은 요소가 끝까지 이어지는가 · ⑤ 끝 장면 한 장으로 메시지가 읽히는가 → 장면 모음(check/wow/{번호}.png)을 보고 사람이 판단
// 실행: node scripts/check_wow.js 32 33 34 38   (Playwright · Python Pillow)
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path'); const { execFileSync } = require('child_process');
const ROOT = path.resolve(__dirname, '..'), OUT = path.join(ROOT, 'check', 'wow');
(async () => {
  const nos = process.argv.slice(2); fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch(); const res = {};
  for (const no of nos) {
    // ① 폰 글자(끝 화면: 움직임 줄이기)
    const m = await b.newPage({ viewport: { width: 844, height: 390 }, deviceScaleFactor: 1 });
    await m.emulateMedia({ reducedMotion: 'reduce' });
    await m.goto('file://' + path.join(ROOT, 'wow', no + '.html#2')); await m.waitForTimeout(600);
    const small = await m.evaluate(() => { const d = document.querySelector('.slide.on .demo'); const k = d.getBoundingClientRect().width / d.offsetWidth; const out = [];
      d.querySelectorAll('*').forEach(e => { if (![...e.childNodes].some(t => t.nodeType === 3 && t.textContent.trim())) return; const cs = getComputedStyle(e); if (e.checkVisibility && !e.checkVisibility({ opacityProperty: true, visibilityProperty: true })) return;   // 부모가 투명해 안 보이는 글자는 빼고 센다
        const r = e.getBoundingClientRect(); if (!r.width) return; const sv = e.closest('svg'); const px = sv && sv.viewBox.baseVal && sv.viewBox.baseVal.width ? parseFloat(cs.fontSize) * sv.getBoundingClientRect().width / sv.viewBox.baseVal.width : parseFloat(cs.fontSize) * k;   // SVG 글자는 viewBox 단위
        out.push([e.textContent.trim().slice(0, 12), +px.toFixed(1)]); }); return out; });
    await m.close();
    // ②③ 큰 화면에서 실제 속도로 장면을 찍는다
    const p = await b.newPage({ viewport: { width: 1600, height: 956 } }); const dir = path.join(OUT, no); fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir);
    await p.goto('file://' + path.join(ROOT, 'wow', no + '.html#2')); await p.waitForTimeout(80);
    const box = await (await p.$('.slide.on .stagebox')).boundingBox(); const t0 = Date.now(); let k = 0; const ts = [];
    while (Date.now() - t0 < 8200) { ts.push(Date.now() - t0); await p.screenshot({ path: path.join(dir, String(k++).padStart(3, '0') + '.png'), clip: box }); }
    await p.close();
    const py = execFileSync('python3', ['-c', `
import glob, json, sys
from PIL import Image
fs = sorted(glob.glob(sys.argv[1] + '/*.png')); ts = json.loads(sys.argv[2])
def cover(f):
    # 화면 사용 = 바탕색이 아닌 칸들을 감싸는 사각형의 넓이 비율(단색 면이 넓은 디자인을 깎지 않게). 바탕 = 위 · 아래 줄에서 가장 많은 색
    im = Image.open(f).convert('RGB').resize((160, 90)); px = list(im.get_flattened_data()) if hasattr(im, "get_flattened_data") else list(im.getdata())
    edge = px[:160] + px[-160:]; bg = max(set(edge), key=edge.count)
    on = [i for i, c in enumerate(px) if sum(abs(a - b) for a, b in zip(c, bg)) > 40]
    if len(on) < 30: return 0.0
    xs = [i % 160 for i in on]; ys = [i // 160 for i in on]
    return (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) / (160 * 90)
cv = [cover(f) for f in fs]
low = [round(t / 1000, 2) for t, c in zip(ts, cv) if t > 400 and c < .03]
# 장면 모음: 0.33초 간격 24장
pick = [min(range(len(ts)), key=lambda i: abs(ts[i] - k * 333)) for k in range(24)]
w = 300; ims = [Image.open(fs[i]).convert('RGB').resize((w, 169)) for i in pick]
S = Image.new('RGB', (6 * (w + 6), 4 * 175), (110, 110, 110))
for n, im in enumerate(ims): S.paste(im, ((n % 6) * (w + 6), (n // 6) * 175))
S.save(sys.argv[3])
print(json.dumps({'max_cover': round(max(cv), 2), 'end_cover': round(cv[-1], 2), 'empty_at': low[:6]}))
`, dir, JSON.stringify(ts), path.join(OUT, no + '.png')]).toString();
    const r = JSON.parse(py); const minFont = small.length ? Math.min(...small.map(x => x[1])) : null;
    r.min_font_phone = minFont; r.small_texts = small.filter(x => x[1] < 9).slice(0, 6);
    r.pass = { phone_text: minFont === null || minFont >= 9, coverage: r.max_cover >= .6, no_empty: !r.empty_at.length };
    res[no] = r; fs.rmSync(dir, { recursive: true, force: true });
    console.log(no, JSON.stringify(r));
  }
  await b.close(); fs.writeFileSync(path.join(OUT, 'report.json'), JSON.stringify(res, null, 1));
})();
