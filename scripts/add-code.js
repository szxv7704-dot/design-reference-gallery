// 레퍼런스 페이지에 "HTML로 가져다 쓰기"(표지 장표만 떼어 낸 복사용 코드) 칸을 붙인다.
// 사용: node scripts/add-code.js refs/NN.html [refs/MM.html ...]   (Playwright 필요)
// - 이미 코드 칸이 있는 페이지(실무형, data-dr-code)는 건너뛴다.
// - 표지 = 폭 600px 이상, 16:9 비율인 첫 요소. 스크립트를 끈 상태의 원본 마크업에서 떼어 낸다.
// - 표지 안 요소에 실제로 쓰이는 CSS 규칙만 모으고, 조상 요소의 클래스·글꼴은 빈 껍데기로 다시 감싼다.
// - 20KB 넘는 data: 이미지는 assets/NN-k.확장자 로 빼고 공개 주소로 바꾼다(캔버스가 픽셀을 읽는 페이지는 그대로 둔다).
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { chromium } = require('playwright');

const SITE = 'https://szxv7704-dot.github.io/design-reference-gallery/';
const RAW = 'https://raw.githubusercontent.com/szxv7704-dot/design-reference-gallery/main/';
const ASSET_BASE = process.env.ASSET_BASE || SITE + 'assets/';
const ROOT = path.resolve(__dirname, '..');

function extract([touched, slideOid]) {
  // ── 브라우저 안에서 실행 (스크립트 꺼진 원본 DOM) ──
  const all = [...document.body.querySelectorAll('*')];
  // 표지는 스크립트를 켠 실행에서 찾은 것(캔버스 크기를 스크립트가 정하는 페이지 때문). 없으면 여기서 찾는다
  const slide = (slideOid && document.querySelector(`[data-oid="${slideOid}"]`)) ||
    all.find(e => { const r = e.getBoundingClientRect(); return r.width >= 600 && Math.abs(r.width / r.height - 16 / 9) < 0.05; });
  if (!slide) return { error: '16:9 표지를 찾지 못함' };
  let root = slide;
  while (root.parentElement && root.parentElement !== document.body && root.parentElement.children.length === 1) root = root.parentElement;

  const scripts = [...document.querySelectorAll('script')].filter(s => !s.src && !s.type?.includes('json'));
  const scriptText = scripts.map(s => s.textContent).join('\n');
  const extScripts = [...document.querySelectorAll('script[src]')].map(s => s.outerHTML);

  // 스크립트가 실제로 찾아 쓴 표지 밖 요소(다시 보기 버튼, 상태 표시 등). touched = 스크립트 켠 실행에서 기록한 data-oid
  const extras = [];
  for (const oid of touched) {
    let el = document.querySelector(`[data-oid="${oid}"]`);
    if (el && /^(TBODY|THEAD|TFOOT|TR|TD|TH|CAPTION|COLGROUP|COL)$/.test(el.tagName)) el = el.closest('table') || el;   // 표 조각은 표째로
    if (el && el.namespaceURI === 'http://www.w3.org/2000/svg' && el.tagName.toLowerCase() !== 'svg') el = el.closest('svg') || el; // SVG 조각은 svg째로
    if (!el || root.contains(el) || el.contains(root) || el === document.body || el === document.documentElement) continue;
    if (el.closest('script,style,head,.drc')) continue;
    if (extras.some(x => x.contains(el))) continue;
    for (let i = extras.length - 1; i >= 0; i--) if (el.contains(extras[i])) extras.splice(i, 1);
    extras.push(el);
  }
  extras.sort((a, b) => a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1);

  // 조상 사슬(body 바로 아래 ~ root의 부모)을 빈 껍데기로
  const chain = []; for (let a = root.parentElement; a && a !== document.body; a = a.parentElement) chain.unshift(a);
  const nodes = [root, ...root.querySelectorAll('*'), ...extras.flatMap(e => [e, ...e.querySelectorAll('*')]), ...chain];
  const classes = new Set(), ids = new Set();
  for (const n of nodes) { n.classList.forEach(c => classes.add(c)); if (n.id) ids.add(n.id); }

  const pseudo = /::?(before|after|placeholder|marker|selection|first-letter|first-line|backdrop|hover|focus|focus-visible|focus-within|active|visited|disabled|checked|target|root)\b(\([^)]*\))?/g;
  function keepSelector(sel) {
    if (/^\s*(html|body)(\s*,\s*(html|body))*\s*$/.test(sel)) return false;           // 페이지 바탕은 버린다
    if (/:root\b/.test(sel) && !/[.#]/.test(sel.replace(/:root/g, ''))) return true;   // 변수
    return sel.split(',').some(part => {
      const p = part.trim();
      const toks = [...p.matchAll(/([.#])(-?[_a-zA-Z][\w-]*)/g)];
      if (toks.length) return toks.every(([, t, name]) => t === '.' ? (classes.has(name) || scriptText.includes(name)) : (ids.has(name) || scriptText.includes(name)));
      if (/^\*/.test(p) || p === '*') return true;
      const clean = p.replace(pseudo, '').trim() || '*';
      try { return nodes.some(n => n.matches(clean)); } catch (e) { return true; }
    });
  }
  function rulesOf(list, depth) {
    const out = [];
    for (const r of list) {
      if (r instanceof CSSStyleRule) { if (keepSelector(r.selectorText)) out.push(r.cssText); }
      else if (r.cssRules && !(r instanceof CSSKeyframesRule)) {      // @media @container @supports @layer
        const inner = rulesOf(r.cssRules, depth + 1);
        if (inner.length) out.push(r.cssText.slice(0, r.cssText.indexOf('{')).trim() + ' {\n  ' + inner.join('\n  ') + '\n}');
      } else out.push(r.cssText);                                    // @keyframes @font-face @property @import
    }
    return out;
  }
  const css = [];
  for (const sh of document.styleSheets) { let rs; try { rs = sh.cssRules; } catch (e) { continue; } if (sh.ownerNode?.tagName === 'STYLE') css.push(...rulesOf(rs, 0)); }
  const links = [...document.querySelectorAll('link[rel="stylesheet"]')].map(l => l.outerHTML);

  // 글꼴·글자색은 body에서 물려받으므로 바깥 껍데기에 옮겨 적는다
  const bs = getComputedStyle(document.body);
  const inherit = `font-family:${bs.fontFamily};font-size:${bs.fontSize};line-height:${bs.lineHeight};color:${bs.color}`;
  const open = [], close = [];
  chain.forEach((a, i) => {
    const t = a.tagName.toLowerCase();
    const attrs = [a.className && typeof a.className === 'string' ? `class="${a.className}"` : '', a.id ? `id="${a.id}"` : '',
      i === 0 ? `style="${inherit.replace(/"/g, "'")}${a.getAttribute('style') ? ';' + a.getAttribute('style').replace(/"/g, "'") : ''}"` : (a.getAttribute('style') ? `style="${a.getAttribute('style').replace(/"/g, "'")}"` : '')].filter(Boolean).join(' ');
    open.push(`<${t}${attrs ? ' ' + attrs : ''}>`); close.unshift(`</${t}>`);
  });
  let body = root.outerHTML + (extras.length ? '\n' + extras.map(e => e.outerHTML).join('\n') : '');
  if (!chain.length) body = `<div style="${inherit.replace(/"/g, "'")}">\n${body}\n</div>`;
  else body = open.join('') + '\n' + body + '\n' + close.join('');
  const readsPixels = /getImageData|toDataURL/.test(scriptText);
  const title = document.title;
  return { css, links, extScripts, body, scripts: scripts.map(s => s.textContent.trim()), readsPixels, title,
           extras: extras.map(e => e.tagName + (e.id ? '#' + e.id : '') + '(' + e.querySelectorAll('*').length + ')') };
}

function externalize(text, nn, readsPixels, assets) {
  if (readsPixels) return text;
  return text.replace(/data:image\/(jpeg|jpg|png|webp|gif);base64,([A-Za-z0-9+/=]+)/g, (m, ext, b64) => {
    if (b64.length < 20000) return m;
    const buf = Buffer.from(b64, 'base64');
    const name = `${nn}-${crypto.createHash('sha1').update(buf).digest('hex').slice(0, 8)}.${ext === 'jpeg' ? 'jpg' : ext}`;
    assets.set(name, buf);
    return ASSET_BASE + name;
  });
}

function buildSnippet(x, nn, assets) {
  const css = externalize(x.css.join('\n'), nn, x.readsPixels, assets);
  const body = externalize(x.body, nn, x.readsPixels, assets);
  return [
    `<!-- ${x.title.replace(/--/g, '—')} · 표지 장표 코드 (가상 예시) -->`,
    `<meta charset="utf-8">`,
    `<meta name="viewport" content="width=device-width,initial-scale=1">`,
    ...x.links, ...x.extScripts,
    `<style>\n${css}\n</style>`,
    '', body, '',
    ...x.scripts.map(s => `<script>\n${s}\n</script>`)
  ].join('\n');
}

const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function section(snippet, nn, hasAssets) {
  return `
<section class="drc" data-dr-code aria-labelledby="drc-h">
<style>
.drc{max-width:1120px;margin:56px auto 64px;padding:28px;background:#FFFFFF;border:1px solid #E1E5EA;border-radius:16px;box-shadow:0 12px 32px -20px rgba(0,0,0,.35);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:28px;align-items:start;
  font-family:"IBM Plex Sans KR","Noto Sans KR","Malgun Gothic","Apple SD Gothic Neo",sans-serif;color:#1C2430;text-align:left}
.drc *{box-sizing:border-box}
.drc h2{grid-column:1/-1;margin:0;font-size:26px;font-weight:800;letter-spacing:-.02em;color:#1C2430;font-family:inherit}
.drc-note{background:#F6F7F9;border:1px solid #E1E5EA;border-radius:12px;padding:18px 20px;font-size:15px;line-height:1.7;color:#3D4654}
.drc-note p{margin:0 0 10px}.drc-note ol{margin:0;padding-left:1.3em}.drc-note li{margin:4px 0}
.drc-note code{font-family:"IBM Plex Mono",Consolas,monospace;font-size:.9em;background:#E9ECF1;padding:1px 5px;border-radius:4px;color:#1C2430}
.drc-note a{color:#2563A8}
.drc-box{position:relative;background:#14262E;border-radius:12px;min-width:0}
.drc-box pre{margin:0;padding:18px 18px 18px;max-height:520px;overflow:auto;font:12.5px/1.65 "IBM Plex Mono",Consolas,monospace;color:#E4ECEA;tab-size:2;white-space:pre}
.drc-copy{position:absolute;top:10px;right:14px;z-index:1;font:700 14px "IBM Plex Sans KR","Malgun Gothic",sans-serif;padding:8px 16px;border-radius:999px;border:0;background:#E4F1EE;color:#14262E;cursor:pointer}
.drc-copy:focus-visible{outline:3px solid #7FC4B8;outline-offset:2px}
@media (max-width:760px){.drc{grid-template-columns:1fr;padding:18px;margin:40px 12px 48px}}
</style>
<h2 id="drc-h">HTML로 가져다 쓰기</h2>
<div class="drc-note">
  <p>아래 코드는 위 표지 장표의 스타일·마크업·스크립트만 떼어 합친 것입니다. 빈 HTML 파일에 붙여 넣으면 그대로 동작합니다. 폰트 링크도 들어 있습니다(인터넷이 안 되는 곳에서는 대체 폰트로 표시됩니다).</p>
  <ol>
    <li>제목·기관명·날짜 같은 글자는 코드 안에서 바로 고치면 됩니다.</li>
    <li>색은 <code>:root</code> 또는 맨 바깥 요소의 CSS 변수(<code>--</code>로 시작)를 먼저 바꿔 보세요.</li>
    ${hasAssets ? '<li>사진은 갤러리 주소에서 불러옵니다. 내 사진으로 바꾸려면 <code>src</code>·<code>url()</code> 주소만 교체하세요.</li>' : ''}
    <li>AI 채팅에서 쓸 때는 링크 대신 이 코드를 붙여 넣고 "이 표지를 ○○ 계획 주제로 바꿔 줘"처럼 요청하세요. 링크로 주려면 원본 파일 주소를 쓰세요: <a href="${RAW}refs/${nn}.html" target="_blank" rel="noopener">refs/${nn}.html 원본</a></li>
  </ol>
</div>
<div class="drc-box">
  <button class="drc-copy" type="button">코드 복사</button>
  <pre><code>${esc(snippet)}</code></pre>
</div>
<script>
(function(){
  var sec=document.currentScript.closest('.drc'), b=sec.querySelector('.drc-copy'), c=sec.querySelector('code');
  b.addEventListener('click',function(){
    var done=function(){b.textContent='복사됨';setTimeout(function(){b.textContent='코드 복사'},1600)};
    var pick=function(){var r=document.createRange();r.selectNodeContents(c);var s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='선택됨 · Ctrl+C'};
    try{navigator.clipboard.writeText(c.textContent).then(done,pick)}catch(e){pick()}
  });
})();
</script>
</section>
`;
}

// 원본 HTML의 모든 시작 태그에 data-oid 번호를 붙인다(script·style 안은 건드리지 않음)
function tag(html) {
  let n = 0;
  return html.split(/(<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>|<!--[\s\S]*?-->)/i).map((part, i) =>
    i % 2 ? part : part.replace(/<([a-zA-Z][\w-]*)(?=[\s>\/])/g, (m, t) => /^(html|head|body|meta|link|title|br|wbr)$/i.test(t) ? m : `${m} data-oid="${n++}"`)).join('');
}
// 스크립트를 켠 실행에서 DOM 조회 함수가 돌려준 요소의 data-oid를 모은다
const SPY = `(() => {
  const seen = new Set(); window.__oids = seen;
  const rec = r => { if (!r) return r; const add = e => { const o = e && e.getAttribute && e.getAttribute('data-oid'); if (o) seen.add(o); };
    if (r.length !== undefined && typeof r !== 'string') for (const e of r) add(e); else add(r); return r; };
  const wrap = (proto, names) => names.forEach(k => { const f = proto[k]; if (f) proto[k] = function () { return rec(f.apply(this, arguments)); }; });
  wrap(Document.prototype, ['getElementById', 'querySelector', 'querySelectorAll', 'getElementsByClassName', 'getElementsByTagName', 'getElementsByName']);
  wrap(Element.prototype, ['querySelector', 'querySelectorAll', 'getElementsByClassName', 'getElementsByTagName', 'closest']);
  wrap(DocumentFragment.prototype, ['querySelector', 'querySelectorAll', 'getElementById']);
})();`;

(async () => {
  const files = process.argv.slice(2);
  if (!files.length) { console.error('사용: node scripts/add-code.js refs/NN.html ...'); process.exit(1); }
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 1280, height: 900 } });
  const live = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  await live.addInitScript(SPY);
  for (const f of files) {
    const file = path.resolve(f), nn = path.basename(file, '.html');
    let html = fs.readFileSync(file, 'utf8').replace(/\n<section class="drc" data-dr-code[\s\S]*?<\/section>\n/, '');   // 이전에 붙인 칸은 새로 만든다
    if (/id="copyBtn"|코드 복사/.test(html)) { console.log(nn, '건너뜀(원래 코드 칸 있음)'); continue; }
    const tmp = path.join(path.dirname(file), '.tag-' + path.basename(file));
    fs.writeFileSync(tmp, tag(html));
    const lp = await live.newPage();
    await lp.goto('file://' + tmp); await lp.waitForTimeout(8000);
    const touched = await lp.evaluate(() => [...window.__oids]);
    const slideOid = await lp.evaluate(() => {
      const s = [...document.body.querySelectorAll('*')].find(e => { const r = e.getBoundingClientRect(); return r.width >= 600 && Math.abs(r.width / r.height - 16 / 9) < 0.05; });
      let e = s; while (e && !e.hasAttribute('data-oid')) e = e.parentElement; return e ? e.getAttribute('data-oid') : null; });
    await lp.close();
    const page = await ctx.newPage();
    await page.goto('file://' + tmp); await page.waitForTimeout(300);
    const x = await page.evaluate(extract, [touched, slideOid]); await page.close();
    fs.unlinkSync(tmp);
    if (!x.error) { x.body = x.body.replace(/ data-oid="\d+"/g, ''); }
    if (x.error) { console.log(nn, '실패:', x.error); continue; }
    const assets = new Map();
    const snippet = buildSnippet(x, nn, assets);
    if (process.env.SNIPPET_OUT) fs.writeFileSync(path.join(process.env.SNIPPET_OUT, nn + '.html'), snippet);
    for (const [name, buf] of assets) { fs.mkdirSync(path.join(ROOT, 'assets'), { recursive: true }); fs.writeFileSync(path.join(ROOT, 'assets', name), buf); }
    const sec = section(snippet, nn, assets.size > 0);
    html = /<\/body>/i.test(html) ? html.replace(/<\/body>(?![\s\S]*<\/body>)/i, sec + '</body>') : html + sec;
    if (!process.env.DRY) fs.writeFileSync(file, html);
    console.log(nn, `코드 ${Math.round(snippet.length / 1024)}KB`, assets.size ? `사진 ${assets.size}장 분리` : '', x.readsPixels ? '(캔버스 픽셀 읽기: 사진 내장 유지)' : '', x.extras.length ? '추가 요소: ' + x.extras.join(', ') : '');
  }
  await browser.close();
})();
