// 표지별 덱 검사: data/decks.json 의 모든 장(light/NN.html?slide=…)을 열어
//  ① 16:9 무대를 찾았는가(못 찾으면 페이지가 통째로 뜬다) ② 무대 밖으로 나간 요소 ③ 글자가 자기 칸에서 잘린 요소 ④ 스크립트 오류 를 본다.
// 실행: node scripts/check_decks.js [표지 번호 …]   (없으면 전부. 5~15분)  → 문제가 있으면 종료 코드 1
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path'); const http = require('http');
const ROOT = path.resolve(__dirname, '..');
const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.json': 'application/json', '.css': 'text/css', '.woff2': 'font/woff2', '.jpg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp', '.svg': 'image/svg+xml' };
(async () => {
  const srv = http.createServer((q, s) => { const f = path.join(ROOT, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { s.writeHead(404); s.end(); } else { s.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream' }); s.end(d); } }); });
  await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port + '/';
  const decks = JSON.parse(fs.readFileSync(path.join(ROOT, 'data', 'decks.json'), 'utf8')); const want = process.argv.slice(2);
  const urls = [...new Set(Object.entries(decks).filter(([k]) => !want.length || want.includes(k)).flatMap(([, d]) => d.slides.map(s => s.file)))];
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } }); await p.emulateMedia({ reducedMotion: 'reduce' }); const bad = [];
  for (const u of urls) {
    const errs = []; p.removeAllListeners('pageerror'); p.on('pageerror', e => errs.push(String(e.message).slice(0, 80)));
    await p.goto(base + u); await p.waitForTimeout(1600);
    const r = await p.evaluate(() => {
      const fit = Math.min(innerWidth, innerHeight * 16 / 9);
      const E = [...document.querySelectorAll('body *')].find(e => { const r = e.getBoundingClientRect(); return Math.abs(r.width - fit) < 3 && Math.abs(r.width / r.height - 16 / 9) < 0.06; });
      if (!E) return { stage: false };
      const R = E.getBoundingClientRect(); let out = 0, clip = 0; const ex = [];
      E.querySelectorAll('*').forEach(e => { const r = e.getBoundingClientRect(), cs = getComputedStyle(e); if (!r.width || !r.height || cs.visibility === 'hidden' || cs.opacity === '0') return;
        if (r.right > R.right + 3 || r.bottom > R.bottom + 3 || r.left < R.left - 3 || r.top < R.top - 3) { out++; if (ex.length < 2) ex.push('밖 ' + e.tagName + '.' + String(e.className.baseVal ?? e.className).split(' ')[0]); }
        if ([...e.childNodes].some(t => t.nodeType === 3 && t.textContent.trim()) && cs.overflow !== 'visible' && e.scrollWidth > e.clientWidth + 2) { clip++; if (ex.length < 2) ex.push('잘림 ' + e.textContent.trim().slice(0, 14)); } });
      return { stage: true, out, clip, ex };
    });
    if (!r.stage || r.out || r.clip || errs.length) bad.push(u + (r.stage ? ` 밖 ${r.out} 잘림 ${r.clip} ${r.ex.join(' | ')}` : ' 무대를 못 찾음') + (errs.length ? ' 오류 ' + errs[0] : ''));
  }
  await b.close(); srv.close();
  console.log('검사', urls.length, '장 · 문제', bad.length); bad.forEach(x => console.log('  ' + x)); process.exitCode = bad.length ? 1 : 0;
})();
