// 인터넷 없이 검사: refs/ 의 장표(또는 지정한 폴더)를 바깥 연결을 모두 막은 채 열어
//  ① 바깥 요청 시도(주소) ② 콘솔 오류 ③ 쓰인 글꼴이 실제로 불러와졌는지 ④ 첫 화면 스크린샷 을 기록한다.
//  ⑤ 장표 규칙(data/rounds.json 의 motion · role 을 보고 판정, 하나라도 걸리면 실패)
//     - reduced_motion: 움직임(모션·인터랙션) 장표인데 prefers-reduced-motion 처리가 없음
//     - infinite_under_reduce: 움직임 줄이기를 켜도 무한 반복 애니메이션이 계속 돎(안내 깜빡임 등)
//     - print_css: 인쇄·홍보물인데 @media print 가 없음
//     - stage_ratio · stage_overflow: 덱 장표(.stage-frame 안 무대)가 16:9가 아니거나 내용이 무대 밖으로 넘침
// 실행: node scripts/check.js [폴더=refs] [번호...]  → check/report.json, check/shots/{번호}.png
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const META = {}; try { JSON.parse(fs.readFileSync(path.join(ROOT, 'data', 'rounds.json'), 'utf8')).forEach(r => { META[Number(r.no)] = r; }); } catch (e) {}
const DECK = new Set(['표지', '본문', '목차·간지', '발표 틀']);
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
    const rules = [], m = META[Number(no)], src = fs.readFileSync(path.join(dir, no + '.html'), 'utf8');
    if (m) {
      if (m.role === '인쇄·홍보물' && !/@media\s+print/.test(src)) rules.push('print_css');
      if (DECK.has(m.role)) {
        const st = await p.evaluate(() => { const r = document.querySelector('.stage-frame > *'); if (!r) return null; const c = r.getBoundingClientRect();
          return { ar: c.width / c.height, ow: r.scrollWidth - r.clientWidth, oh: r.scrollHeight - r.clientHeight }; }).catch(() => null);
        if (st && Math.abs(st.ar - 16 / 9) > 0.01) rules.push('stage_ratio ' + st.ar.toFixed(3));
        if (st && (st.ow > 1 || st.oh > 1)) rules.push('stage_overflow ' + st.ow + '×' + st.oh);
      }
      if (m.motion && m.motion !== '정지') {
        if (!/prefers-reduced-motion/.test(src)) rules.push('reduced_motion');
        await p.emulateMedia({ reducedMotion: 'reduce' }); await p.waitForTimeout(300);
        const inf = await p.evaluate(() => document.getAnimations().filter(a => a.playState === 'running' && a.effect && a.effect.getComputedTiming().iterations === Infinity)
          .map(a => a.animationName || 'script')).catch(() => []);
        if (inf.length) rules.push('infinite_under_reduce ' + [...new Set(inf)].slice(0, 3).join(','));
      }
    }
    report[no] = { external: [...ext], errors: errs, font_errors: bad, rules, ok: !ext.size && !errs.length && !bad.length && !rules.length };
    await p.close();
  }
  await b.close();
  fs.writeFileSync(path.join(out, 'report.json'), JSON.stringify(report, null, 1));
  const bad = Object.entries(report).filter(([, r]) => !r.ok);
  console.log('검사', Object.keys(report).length, '통과', Object.keys(report).length - bad.length, '문제', bad.length);
  process.exitCode = bad.length ? 1 : 0;
  bad.forEach(([n, r]) => console.log(' #' + n, r.external.length ? '바깥 ' + r.external.length + ' ' + r.external.slice(0, 2).join(' ') : '', r.errors.length ? '오류 ' + r.errors.slice(0, 2).join(' | ') : '', r.font_errors.length ? '글꼴 ' + r.font_errors.join(',') : '', r.rules.length ? '규칙 ' + r.rules.join(' | ') : ''));
})();
