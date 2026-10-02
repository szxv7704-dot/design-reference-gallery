// 사용법: node scripts/thumb.js refs/27.html thumbs/27.jpg
// 페이지 맨 위의 16:9 표지(가로 600px 이상, 비율 약 1.78)를 찾아 640px 폭 JPG 썸네일로 저장한다.
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 0.5 });
  await page.goto('file://' + path.resolve(src));
  await page.waitForTimeout(3500); // 웹폰트·등장 애니메이션 대기
  const box = await page.evaluate(() => {
    for (const el of document.querySelectorAll('body *')) {
      const r = el.getBoundingClientRect();
      if (r.width >= 600 && Math.abs(r.width / r.height - 16 / 9) < 0.06) {
        return { x: r.x, y: r.y + scrollY, width: r.width, height: r.height };
      }
    }
    return null;
  });
  const clip = box || { x: 0, y: 0, width: 1280, height: 720 };
  await page.screenshot({ path: out, type: 'jpeg', quality: 78, clip });
  await browser.close();
})();
