// 덱 키트 장표 썸네일: kit/{계열}.html 의 모든 장을 찍어 kit/thumbs/{계열}-{장}.jpg(640 × 360)로
// 키트 모음 화면(kit/index.html) · 첫 화면 목적 타일 · 갤러리의 키트 장표 카드가 쓴다.
// 실행: node scripts/kit_thumbs.js [A B C D]   (Playwright · Python Pillow 필요) — 예시 덱을 고친 뒤 다시 실행
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs'); const { execFileSync } = require('child_process');
const ROOT = path.resolve(__dirname, '..'), OUT = path.join(ROOT, 'kit', 'thumbs');
(async () => {
  const fams = process.argv.slice(2).length ? process.argv.slice(2) : ['A', 'B', 'C', 'D'];
  fs.mkdirSync(OUT, { recursive: true });
  fs.readdirSync(OUT).filter(f => fams.includes(f.split('-')[0])).forEach(f => fs.unlinkSync(path.join(OUT, f)));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const F of fams) {
    await p.goto('file://' + path.join(ROOT, 'kit', F + '.html')); await p.waitForTimeout(600);
    const n = await p.evaluate(() => DECK.count);
    for (let i = 0; i < n; i++) { await p.evaluate(i => DECK.go(i, 99), i); await p.waitForTimeout(450); await p.screenshot({ path: path.join(OUT, `${F}-${i + 1}.png`) }); }
  }
  await b.close();
  execFileSync('python3', ['-c', `
import glob, os
from PIL import Image
for p in glob.glob(os.path.join(${JSON.stringify(OUT)}, '*.png')):
    Image.open(p).convert('RGB').resize((640, 360), Image.LANCZOS).save(p[:-4] + '.jpg', quality=80); os.remove(p)
`]);
  console.log('kit/thumbs', fams.join(' '));
})();
