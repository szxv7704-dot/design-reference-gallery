// 첫 화면 '무엇을 하려고 하나요?' 미리보기 그림: 따로 있는 페이지(와우 포인트 · 아이콘 세트)를 찍어 thumbs/hub-*.jpg 로
// (레퍼런스 장표 미리보기는 rounds.json 의 썸네일을, 덱 키트는 kit/thumbs/ 를 그대로 쓴다)
// 실행: node scripts/hub_thumbs.js   (Playwright · Python Pillow 필요) — 와우 포인트 · 아이콘 세트를 고친 뒤 다시 실행
const { chromium } = require('playwright'); const path = require('path'); const { execFileSync } = require('child_process');
const ROOT = path.resolve(__dirname, '..');
const SHOTS = [
  ['wow/wow.html', 'hub-wow-1', null], ['wow/wow.html', 'hub-wow-2', 'ArrowRight'], ['wow/wow.html', 'hub-wow-3', 'ArrowRight'],
  ['icons/icons.html', 'hub-icons-1', null], ['icons/icons.html', 'hub-icons-2', 'scroll'],
];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.route('**/*', r => /^(file|data|blob):/.test(r.request().url()) ? r.continue() : r.abort());
  let cur = '';
  for (const [file, name, act] of SHOTS) {
    if (file !== cur) { await p.goto('file://' + path.join(ROOT, file)); await p.waitForTimeout(1500); cur = file; }
    if (act === 'ArrowRight') { await p.keyboard.press('ArrowRight'); await p.waitForTimeout(1600); }
    if (act === 'scroll') { await p.evaluate(() => scrollTo(0, 900)); await p.waitForTimeout(400); }
    await p.screenshot({ path: path.join(ROOT, 'thumbs', name + '.png') });
  }
  await b.close();
  execFileSync('python3', ['-c', `
import glob, os
from PIL import Image
for p in glob.glob(os.path.join(${JSON.stringify(path.join(ROOT, 'thumbs'))}, 'hub-*.png')):
    Image.open(p).convert('RGB').resize((640, 360), Image.LANCZOS).save(p[:-4] + '.jpg', quality=82); os.remove(p)
`]);
  console.log('thumbs/hub-*.jpg', SHOTS.length);
})();
