// 인터넷 없이 검사: refs/ 의 장표(또는 지정한 폴더)를 바깥 연결을 모두 막은 채 열어
//  ① 바깥 요청 시도(주소) ② 콘솔 오류 ③ 쓰인 글꼴이 실제로 불러와졌는지 ④ 첫 화면 스크린샷 을 기록한다.
// 실행: node scripts/check.js [폴더=refs] [번호...]  → check/report.json, check/shots/{번호}.png
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const ROOT = path.resolve(__dirname, '..');
(async () => {
  const args = process.argv.slice(2), dir = path.resolve(args[0] || path.join(ROOT, 'refs'));
  let nos = args.slice(1); if (!nos.length) nos = fs.readdirSync(dir).filter(f => /^\d+\.html$/.test(f)).map(f => f.slice(0, -5)).sort((a, b) => a - b);
  const out = path.join(ROOT, 'check'); fs.mkdirSync(path.join(out, 'shots'), { recursive: true });
  const b = await chromium.launch(); const report = {};
  for (const no of nos) {
    const p = await b.newPage({ viewport: { width: 1280, height: 900 } }); const ext = new Set(), errs = [];
    p.on('pageerror', e => errs.push(String(e.message).slice(0, 160)));
    p.on('console', m => { if (m.type() === 'error' && !/net::ERR_/.test(m.text())) errs.push(m.text().slice(0, 160)); });
    await p.route('**/*', r => { const u = r.request().url(); if (u.startsWith('file:') || u.startsWith('data:') || u.startsWith('blob:')) return r.continue(); ext.add(u.split('?')[0].slice(0, 90)); r.abort(); });
    try { await p.goto('file://' + path.join(dir, no + '.html'), { timeout: 60000 }); await p.waitForTimeout(1500); } catch (e) { errs.push('load: ' + e.message.slice(0, 120)); }
    const fonts = await p.evaluate(async () => { await document.fonts.ready; const s = {}; document.fonts.forEach(f => { s[f.family.replace(/"/g, '') + ' ' + f.weight] = f.status; }); return s; }).catch(() => ({}));
    const bad = Object.entries(fonts).filter(([, v]) => v === 'error').map(([k]) => k);
    await p.screenshot({ path: path.join(out, 'shots', no + '.png') }).catch(() => {});
    report[no] = { external: [...ext], errors: errs, font_errors: bad, ok: !ext.size && !errs.length && !bad.length };
    await p.close();
  }
  await b.close();
  fs.writeFileSync(path.join(out, 'report.json'), JSON.stringify(report, null, 1));
  const bad = Object.entries(report).filter(([, r]) => !r.ok);
  console.log('검사', Object.keys(report).length, '통과', Object.keys(report).length - bad.length, '문제', bad.length);
  bad.forEach(([n, r]) => console.log(' #' + n, r.external.length ? '바깥 ' + r.external.length + ' ' + r.external.slice(0, 2).join(' ') : '', r.errors.length ? '오류 ' + r.errors.slice(0, 2).join(' | ') : '', r.font_errors.length ? '글꼴 ' + r.font_errors.join(',') : ''));
})();
