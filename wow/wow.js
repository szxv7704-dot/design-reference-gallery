/* scripts/wow.py 가 wow/wow.html 에서 뽑아 만든 공용 움직임 엔진. 고치지 말 것 */

(() => {
  const stage = document.getElementById('stage'), slides = [...document.querySelectorAll('.slide')];
  let cur = 0;
  const fit = () => { const k = Math.min(innerWidth / 1600, (innerHeight - 56) / 900); window.__k = k; stage.style.transform = 'translate(-50%,-50%) scale(' + k + ')'; };
  addEventListener('resize', fit); fit();

  // 100칸
  const ug = document.getElementById('unitGrid');
  if (ug) for (let i = 0; i < 100; i++) { const c = document.createElement('i'); if (i < 41) { c.className = 'on'; c.style.setProperty('--i', i); } ug.appendChild(c); }

  // 자바스크립트로 움직이는 데모: run(엘리먼트, 끝 화면만?)
  const ease = t => 1 - Math.pow(1 - t, 3);
  const DEMOS = {
    count(el, end) {
      const v = el.querySelector('.cv'), bar = el.querySelector('.track i'), T = 2000, goal = 10000, tok = el._t = (el._t || 0) + 1;
      const set = p => { v.textContent = Math.round(goal * p).toLocaleString('ko-KR'); bar.style.width = p * 100 + '%'; el.classList.toggle('done', p >= 1); };
      if (end) return set(1);
      set(0); const t0 = performance.now() + 400;
      const step = now => { if (tok !== el._t) return; const p = Math.max(0, Math.min(1, (now - t0) / T)); set(ease(p)); if (p < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    },
    race(el, end) {
      const D = [['신도시선', '#C4471A', [6, 8, 11, 14, 16]], ['구도심선', '#5C636C', [15, 14, 13, 12, 11]], ['역전선', '#7E858D', [12, 12, 11.5, 11, 10]], ['산단선', '#E38A5B', [5, 7, 9.5, 12, 13.5]], ['외곽선', '#A7ACB2', [8, 8.5, 7, 6, 5]]];
      if (!el._rows) el._rows = D.map(([n, c]) => { const r = document.createElement('div'); r.className = 'row'; r.innerHTML = '<div class="bar" style="background:' + c + '">' + n + '</div><span class="v"></span>'; el.appendChild(r); return r; });
      const yr = el.querySelector('.yr'), tok = el._t = (el._t || 0) + 1;
      const show = y => {
        const vals = D.map(d => d[2][y]), order = vals.map((v, i) => i).sort((a, b) => vals[b] - vals[a]);
        order.forEach((i, rank) => { const r = el._rows[i]; r.style.transform = 'translateY(' + (rank * 118 + 90) + '%)'; const w = vals[i] / 16 * 100; r.querySelector('.bar').style.width = w + '%'; const s = r.querySelector('.v'); s.textContent = vals[i]; s.style.left = w + '%'; });
        yr.textContent = 2021 + y;
      };
      if (end) return show(4);
      show(0); let y = 0;
      const tick = () => { if (tok !== el._t || y >= 4) return; show(++y); setTimeout(tick, 900); };
      setTimeout(tick, 900);
    },
    morph(el, end) {
      const C = ['#7B4F9E', '#9572B3', '#AE93C6', '#C6B3D8', '#5E3D7C', '#DCD0E7'], L = ['학교 직접', '교육 사업', '시설', '인건비 외', '정책', '기타'];
      const S = [
        [0, 1, 2, 3, 4, 5].map(i => [6, 8 + i * 14, 88, 14, '#3A2B4A']),
        [[6, 8, 50, 52], [6, 60, 50, 32], [56, 8, 38, 30], [56, 38, 20, 30], [76, 38, 18, 30], [56, 68, 38, 24]].map((r, i) => [...r, C[i]]),
        [[6, 40, 34, 26], [40, 40, 18, 26], [58, 40, 13, 26], [71, 40, 10, 26], [81, 40, 8, 26], [89, 40, 5, 26]].map((r, i) => [...r, i ? '#C6B3D8' : '#E2571A'])
      ];
      const caps = ['① 총액 한 덩어리', '② 분야로 나눔', '③ 한 줄로 비교 · 학교 직접이 가장 크다'];
      if (!el._tiles) el._tiles = L.map(t => { const d = document.createElement('div'); d.className = 'tile'; d.innerHTML = '<span>' + t + '</span>'; el.appendChild(d); return d; });
      const cap = el.querySelector('.cap'), tot = el.querySelector('.tot'), tok = el._t = (el._t || 0) + 1;
      const set = s => {
        S[s].forEach(([x, y, w, h, c], i) => { const d = el._tiles[i]; Object.assign(d.style, { left: x + '%', top: y + '%', width: w + '%', height: h + '%', background: c }); d.querySelector('span').style.opacity = s === 0 || (s === 2 && i > 1) ? 0 : 1; d.style.color = s === 2 && i ? '#3A2B4A' : '#fff'; });
        cap.textContent = caps[s]; tot.style.opacity = s === 0 ? 1 : 0;
      };
      if (end) return set(2);
      set(0); let s = 0;
      const tick = () => { if (tok !== el._t || s >= 2) return; set(++s); setTimeout(tick, 1700); };
      setTimeout(tick, 1400);
    },
    ba(el) { /* 자동 훑기는 CSS. 끌면 직접 비교 */ },
    fw(el, end) { el._e = el._e || Fireworks(el); end ? el._e.final() : el._e.run(); },
    asm(el, end) { el._e = el._e || Assembly(el); end ? el._e.final() : el._e.run(); },
    train(el, end) { el._e = el._e || Train(el); end ? el._e.final() : el._e.run(); },
    thud(el, end) { el._e = el._e || Thud(el); end ? el._e.final() : el._e.run(); }
  };


  // ── 불꽃: 캔버스 입자(로켓 → 터짐 → 불티가 흘러내려 아래에서 글자로 모임) ──
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.fonts && document.fonts.load('900 40px "Gothic A1"');
  // [발사 시각(초), x, 터질 높이(y), 종류, 크기, 글자 만들기]
  const SHOW = [[0, .3, .3, 'peony', 1], [.2, .7, .27, 'blue', 1], [.5, .5, .17, 'big', 1],
    [.95, .14, .38, 'willow', 1], [1.05, .86, .36, 'willow', 1], [1.25, .36, .22, 'peony', .95], [1.35, .64, .23, 'peony', .95],
    [1.5, .22, .3, 'blue', .85], [1.6, .78, .29, 'peony', .85], [2.3, .5, .24, 'big', 1.15],
    [3.3, .17, .2, 'blue', .8], [3.6, .83, .19, 'peony', .8], [4.4, .32, .15, 'willow', .8], [4.7, .68, .16, 'blue', .8]];
  function Fireworks(root) {
    const fx = root.querySelector('canvas.fx'), sm = root.querySelector('canvas.sm'), gc = root.querySelector('canvas.gl');
    const g = fx.getContext('2d'), s = sm.getContext('2d'), gx = gc.getContext('2d'), TEXT = root.dataset.text || '목표 달성!';
    let W = 0, H = 0, u = 1, qf = 1, slow = 0, parts = [], rockets = [], puffs = [], flashes = [], tps = [], syl = {}, raf = 0, T = 0, last = 0, ev = [], textAt = 0, running = false;
    const rnd = (a, b) => a + Math.random() * (b - a);
    const col = { gold: () => [rnd(36, 44), rnd(35, 55), rnd(72, 82)], white: () => [rnd(30, 220), rnd(5, 15), rnd(90, 97)],
      blue: () => [rnd(205, 218), rnd(25, 45), rnd(78, 88)], pale: () => [rnd(38, 44), rnd(20, 35), rnd(84, 92)] };
    const size = () => {
      W = root.offsetWidth; H = root.offsetHeight; u = W / 1600;
      const R = Math.min(2, Math.max(1, (devicePixelRatio || 1) * (window.__k || 1)));
      [fx, sm].forEach(c => { c.width = Math.round(W * R); c.height = Math.round(H * R); });
      gc.width = Math.round(W * R / 3); gc.height = Math.round(H * R / 3);
      g.setTransform(R, 0, 0, R, 0, 0); s.setTransform(R, 0, 0, R, 0, 0); g.lineCap = 'round';
    };
    const burst = (x, y, type, k) => {
      const dens = (.3 + .7 * Math.min(1, u * 1.2)) * qf;
      const n = Math.round({ big: 720, peony: 460, blue: 400, willow: 380 }[type] * dens);
      const base = { big: 13.5, peony: 10.5, blue: 9.8, willow: 8 }[type] * u * k;
      for (let i = 0; i < n; i++) {
        const a = Math.random() * 6.2832, sp = base * (.18 + .82 * Math.sqrt(Math.random()));
        const kind = type === 'blue' ? (Math.random() < .45 ? 'blue' : 'white') : type === 'willow' ? (Math.random() < .6 ? 'gold' : 'pale') : (Math.random() < .55 ? 'white' : Math.random() < .6 ? 'pale' : 'gold');
        parts.push({ x, y, px: x, py: y, vx: Math.cos(a) * sp, vy: Math.sin(a) * sp, life: 1, decay: rnd(.006, .0105) * (type === 'willow' ? .55 : 1),
          drag: type === 'willow' ? .958 : .972, gr: (type === 'willow' ? .05 : .032) * u, c: col[kind](), w: rnd(1.3, 2.7) * Math.max(.45, u), gl: Math.random() < .45 });
      }
      flashes.push({ x, y, r: 80 * u * k, a: 1 });
      for (let i = 0; i < 5; i++) puffs.push({ x: x + rnd(-160, 160) * u * k, y: y + rnd(-80, 180) * u * k, r: rnd(70, 130) * u, gr: rnd(.3, .6) * u, a: rnd(.02, .04) });
    };
    const launch = (x, ty, type, k, text) => {
      const gR = .22 * u; rockets.push({ x, y: H, vx: rnd(-.25, .25) * u, vy: -Math.sqrt(2 * gR * (H - ty)), gR, type, k, text });
    };
    const frame = now => {
      const dt = Math.min(50, now - last) || 16.7, f = dt / 16.667; last = now; T += dt / 1000;
      if (dt > 30) { if (++slow > 15 && qf > .45) { qf *= .8; slow = 0; } } else slow = Math.max(0, slow - 1);
      while (ev.length && ev[0][0] <= T) { const e = ev.shift(); launch(e[1] * W, e[2] * H, e[3], e[4], e[5]); }
      // 연기: 매 장 새로 그림
      s.clearRect(0, 0, W, H);
      puffs = puffs.filter(p => (p.a -= .00035 * f) > 0);
      for (const p of puffs) {
        p.r += p.gr * f; p.y -= .08 * u * f;
        const gr = s.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r);
        gr.addColorStop(0, 'rgba(190,196,210,' + p.a + ')'); gr.addColorStop(1, 'rgba(190,196,210,0)');
        s.fillStyle = gr; s.fillRect(p.x - p.r, p.y - p.r, p.r * 2, p.r * 2);
      }
      // 불티: 앞 장을 조금씩 지워 꼬리를 남김
      g.globalCompositeOperation = 'destination-out'; g.fillStyle = 'rgba(0,0,0,' + Math.min(1, .11 * f) + ')'; g.fillRect(0, 0, W, H);
      g.globalCompositeOperation = 'lighter';
      rockets = rockets.filter(r => {
        const px = r.x, py = r.y; r.vy += r.gR * f; r.x += r.vx * f; r.y += r.vy * f;
        g.strokeStyle = 'rgba(245,240,228,.85)'; g.lineWidth = 2.2 * Math.max(.5, u); g.beginPath(); g.moveTo(px, py); g.lineTo(r.x, r.y); g.stroke();
        if (Math.random() < .7) parts.push({ x: r.x, y: r.y, px: r.x, py: r.y, vx: rnd(-.5, .5) * u, vy: rnd(.4, 1.6) * u, life: .55, decay: .03, drag: .95, gr: .02 * u, c: col.gold(), w: 1.1 * Math.max(.5, u), gl: false });
        if (r.vy > -1.2 * u) { burst(r.x, r.y, r.type, r.k); return false; }
        return true;
      });
      flashes = flashes.filter(fl => (fl.a -= .07 * f) > 0);
      for (const fl of flashes) {
        const gr = g.createRadialGradient(fl.x, fl.y, 0, fl.x, fl.y, fl.r);
        gr.addColorStop(0, 'rgba(250,248,242,' + .18 * fl.a + ')'); gr.addColorStop(1, 'rgba(250,248,242,0)');
        g.fillStyle = gr; g.fillRect(fl.x - fl.r, fl.y - fl.r, fl.r * 2, fl.r * 2);
      }
      parts = parts.filter(p => (p.life -= p.decay * f) > 0);
      for (const p of parts) {
        p.px = p.x; p.py = p.y; const dr = Math.pow(p.drag, f); p.vx *= dr; p.vy = p.vy * dr + p.gr * f; p.x += p.vx * f; p.y += p.vy * f;
        const L = p.life;
        g.strokeStyle = 'hsla(' + p.c[0] + ',' + p.c[1] + '%,' + (p.c[2] - (1 - L) * 12) + '%,' + Math.min(1, L * 1.6) + ')';
        g.lineWidth = p.w * (.35 + .65 * L); g.beginPath(); g.moveTo(p.px, p.py); g.lineTo(p.x, p.y); g.stroke();
        if (p.gl && L < .45 && Math.random() < .25) { const r = (1 + Math.random() * 1.6) * Math.max(.5, u); g.fillStyle = 'rgba(255,248,225,' + (.5 + Math.random() * .5) + ')'; g.fillRect(p.x - r / 2, p.y - r / 2, r, r); }
      }
      // 자모 불티: 조각 모양을 따라가며 떨어지고, 닿으면 반짝, 음절이 다 모이면 크게 반짝
      gx.clearRect(0, 0, gc.width, gc.height); gx.drawImage(fx, 0, 0, gc.width, gc.height);
      if (running) raf = requestAnimationFrame(frame);
    };
    const reset = () => { cancelAnimationFrame(raf); running = false; size(); g.clearRect(0, 0, W, H); s.clearRect(0, 0, W, H); gx.clearRect(0, 0, gc.width, gc.height); parts = []; rockets = []; puffs = []; flashes = []; T = 0; };
    return {
      run() { if (RM) return this.final(); reset(); ev = SHOW.map(e => e.slice()); running = true; last = performance.now(); raf = requestAnimationFrame(frame); },
      stop() { running = false; cancelAnimationFrame(raf); },
      // 인쇄·움직임 줄이기: 2.4초 시점까지 한꺼번에 계산해 터진 장면 한 장을 남김
      final() { reset(); ev = SHOW.map(e => e.slice()); let t = performance.now(); last = t; for (let i = 0; i < 145; i++) frame(t += 16.7); }
    };
  }

  // ── 낱획 나누기(공용): 글자 그림(M)을 가로획·세로획·고리 조각으로 ──
  const segment = (M, cw, ch, fs) => {
    const N = cw * ch;
    const nb4 = j => { const jx = j % cw; return [jx > 0 ? j - 1 : -1, jx < cw - 1 ? j + 1 : -1, j >= cw ? j - cw : -1, j + cw < N ? j + cw : -1]; };
    // 1) 점마다 가로로 이어진 길이·세로로 이어진 길이 → 가로획(1)·세로획(2)·꺾임·사선(3)
    const hr = new Uint16Array(N), vr = new Uint16Array(N);
    for (let y = 0; y < ch; y++) { let s0 = -1; for (let k = 0; k <= cw; k++) { const on = k < cw && M[y * cw + k]; if (on && s0 < 0) s0 = k; else if (!on && s0 >= 0) { for (let j = s0; j < k; j++) hr[y * cw + j] = k - s0; s0 = -1; } } }
    for (let k = 0; k < cw; k++) { let s0 = -1; for (let y = 0; y <= ch; y++) { const on = y < ch && M[y * cw + k]; if (on && s0 < 0) s0 = y; else if (!on && s0 >= 0) { for (let j = s0; j < y; j++) vr[j * cw + k] = y - s0; s0 = -1; } } }
    const cls = new Uint8Array(N);
    for (let i = 0; i < N; i++) if (M[i]) cls[i] = hr[i] > vr[i] * 1.25 ? 1 : vr[i] > hr[i] * 1.25 ? 2 : 3;
    const id = new Int32Array(N).fill(-1), comps = [];
    for (let i = 0; i < N; i++) if (M[i] && id[i] < 0) {
      const k = comps.length, q = [i], px = []; id[i] = k;
      while (q.length) { const j = q.pop(); px.push(j); for (const n of nb4(j)) if (n >= 0 && M[n] && id[n] < 0 && cls[n] === cls[i]) { id[n] = k; q.push(n); } }
      comps.push(px);
    }
    const merge = (from, to) => { if (from === to || !comps[from] || !comps[to]) return; comps[from].forEach(j => id[j] = to); comps[to] = comps[to].concat(comps[from]); comps[from] = null; };
    // 2) 너무 작은 조각(획이 만나는 모서리 등)은 가장 많이 맞닿은 획에 붙임
    const minP = fs * fs * .006;
    for (let pass = 0; pass < 3; pass++) comps.forEach((px, ci) => {
      if (!px || px.length >= minP) return; const cnt = {};
      px.forEach(j => nb4(j).forEach(n => { if (n >= 0 && M[n] && id[n] !== ci) cnt[id[n]] = (cnt[id[n]] || 0) + 1; }));
      let best = -1, bn = 0; for (const k in cnt) if (cnt[k] > bn) { bn = cnt[k]; best = +k; }
      if (best >= 0) merge(ci, best);
    });
    // 3) 고리(ㅇ, ㅎ의 동그라미): 구멍이 있고 곧은 줄이 짧은 잉크 덩어리는 획 하나로
    const ink = new Int32Array(N).fill(-1);
    for (let i = 0; i < N; i++) if (M[i] && ink[i] < 0) {
      const q = [i], px = []; ink[i] = i; let x0 = cw, y0 = ch, x1 = 0, y1 = 0, mh = 0, mv = 0;
      while (q.length) { const j = q.pop(); px.push(j); const jx = j % cw, jy = (j / cw) | 0; if (jx < x0) x0 = jx; if (jx > x1) x1 = jx; if (jy < y0) y0 = jy; if (jy > y1) y1 = jy; if (hr[j] > mh) mh = hr[j]; if (vr[j] > mv) mv = vr[j];
        for (const n of nb4(j)) if (n >= 0 && M[n] && ink[n] < 0) { ink[n] = i; q.push(n); } }
      const bw = x1 - x0 + 1, bh = y1 - y0 + 1;
      if (mh / bw > .78 || mv / bh > .78 || bw < fs * .2) continue;
      const seen = new Uint8Array(bw * bh), qq = [];
      for (let yy = 0; yy < bh; yy++) for (let xx = 0; xx < bw; xx++) if (xx === 0 || yy === 0 || xx === bw - 1 || yy === bh - 1) { const g0 = (y0 + yy) * cw + x0 + xx; if (ink[g0] !== i) { seen[yy * bw + xx] = 1; qq.push(yy * bw + xx); } }
      while (qq.length) { const l = qq.pop(), lx = l % bw, ly = (l / bw) | 0; for (const [ax, ay] of [[lx - 1, ly], [lx + 1, ly], [lx, ly - 1], [lx, ly + 1]]) { if (ax < 0 || ay < 0 || ax >= bw || ay >= bh) continue; const li = ay * bw + ax; if (!seen[li] && ink[(y0 + ay) * cw + x0 + ax] !== i) { seen[li] = 1; qq.push(li); } } }
      let hole = 0; for (let l = 0; l < bw * bh; l++) if (!seen[l] && ink[(y0 + ((l / bw) | 0)) * cw + x0 + l % bw] !== i) hole++;
      if (hole > fs * fs * .002) { const ids = [...new Set(px.map(j => id[j]))]; ids.slice(1).forEach(k => merge(k, ids[0])); }
    }
    return comps.filter(Boolean);
  };

  // ── 타이포 조립(타이포그래피 어셈블리): 글자를 획 조각으로 나눠, 자기 칸 안에서 탁탁 돌고 자리를 바꾸다 한순간 맞춘다 ──
  function Assembly(root) {
    const cv = root.querySelector('canvas'), g = cv.getContext('2d');
    const LINES = [{ t: '2027', k: .8, ls: .95 }, { t: '새로운 시작', k: 1, ls: .3 }], ROT = [0, 90, -90, 180, 45, -45, 135, -135].map(d => d * Math.PI / 180);
    const rnd = (a, b) => a + Math.random() * (b - a);
    let W = 0, H = 0, fs = 0, ps = [], raf = 0, t0 = 0, end = 0, running = false;
    const build = () => {
      W = root.offsetWidth; H = root.offsetHeight;
      const R = Math.min(2, Math.max(1, (devicePixelRatio || 1) * (window.__k || 1)));
      cv.width = Math.round(W * R); cv.height = Math.round(H * R); g.setTransform(R, 0, 0, R, 0, 0);
      fs = Math.round(W * (W < 800 ? .085 : .05));
      const cw = Math.ceil(W), ch = Math.ceil(H), c = document.createElement('canvas'), x = c.getContext('2d', { willReadFrequently: true });
      c.width = cw; c.height = ch; x.fillStyle = '#fff'; x.textBaseline = 'alphabetic';
      const lh = fs * 1.5, top = H / 2 - lh * LINES.length / 2;
      LINES.forEach((ln, li) => {
        const f = Math.round(fs * ln.k); x.font = '600 ' + f + 'px "Noto Sans KR"';
        const chars = [...ln.t], ws = chars.map(t => x.measureText(t).width), sp = f * ln.ls, fm = x.measureText('국');
        const base = top + lh * li + lh / 2 + ((fm.fontBoundingBoxAscent || f * .88) - (fm.fontBoundingBoxDescent || f * .22)) / 2;
        let cx = (W - ws.reduce((a, b) => a + b, 0) - sp * (chars.length - 1)) / 2;
        chars.forEach((t, i) => { x.fillText(t, cx, base); cx += ws[i] + sp; });
      });
      const d = x.getImageData(0, 0, cw, ch).data, M = new Uint8Array(cw * ch);
      for (let i = 0; i < M.length; i++) M[i] = d[i * 4 + 3] >= 128 ? 1 : 0;
      // 긴 획은 반으로 나눠 조각을 잘게(영상처럼 '무슨 글자지?')
      const comps = []; segment(M, cw, ch, fs).forEach(px => {
        let x0 = cw, y0 = ch, x1 = 0, y1 = 0; px.forEach(j => { const jx = j % cw, jy = (j / cw) | 0; if (jx < x0) x0 = jx; if (jx > x1) x1 = jx; if (jy < y0) y0 = jy; if (jy > y1) y1 = jy; });
        const w = x1 - x0 + 1, h = y1 - y0 + 1;
        if (w > h * 1.8 && w > fs * .5) { const m = (x0 + x1) / 2; comps.push(px.filter(j => j % cw < m), px.filter(j => j % cw >= m)); }
        else if (h > w * 1.8 && h > fs * .5) { const m = (y0 + y1) / 2; comps.push(px.filter(j => ((j / cw) | 0) < m), px.filter(j => ((j / cw) | 0) >= m)); }
        else comps.push(px);
      });
      ps = comps.filter(px => px.length > 3).map(px => {
        let x0 = cw, y0 = ch, x1 = 0, y1 = 0; px.forEach(j => { const jx = j % cw, jy = (j / cw) | 0; if (jx < x0) x0 = jx; if (jx > x1) x1 = jx; if (jy < y0) y0 = jy; if (jy > y1) y1 = jy; });
        const w = x1 - x0 + 3, h = y1 - y0 + 3, sp = document.createElement('canvas'); sp.width = w; sp.height = h;
        const sx = sp.getContext('2d'), im = sx.createImageData(w, h);
        px.forEach(j => { const k = ((((j / cw) | 0) - y0 + 1) * w + (j % cw) - x0 + 1) * 4; im.data[k] = 242; im.data[k + 1] = 239; im.data[k + 2] = 232; im.data[k + 3] = 255; });
        sx.putImageData(im, 0, 0);
        return { sp, w, h, hx: (x0 + x1) / 2, hy: (y0 + y1) / 2, nx: 0, dx: 0, dy: 0, r: 0, set: rnd(2, 2.7) };
      });
      end = Math.max(...ps.map(p => p.set)) + .2;
    };
    const draw = t => {
      g.clearRect(0, 0, W, H);
      for (const p of ps) {
        if (t < p.set) {
          if (t >= p.nx) { p.nx = t + rnd(.14, .3); p.dx = rnd(-1, 1) * fs * .3; p.dy = rnd(-1, 1) * fs * .24; p.r = ROT[(Math.random() * ROT.length) | 0]; }
          g.save(); g.translate(p.hx + p.dx, p.hy + p.dy); g.rotate(p.r); g.drawImage(p.sp, -p.w / 2, -p.h / 2); g.restore();
        } else g.drawImage(p.sp, p.hx - p.w / 2, p.hy - p.h / 2);
      }
    };
    const frame = now => { const t = (now - t0) / 1000; draw(t); if (running && t < end) raf = requestAnimationFrame(frame); else running = false; };
    const ready = cb => (document.fonts ? document.fonts.load('600 40px "Noto Sans KR"').then(cb, cb) : cb());
    return {
      run() { this.stop(); ready(() => { build(); if (RM) return draw(99); ps.forEach(p => p.nx = 0); running = true; t0 = performance.now(); raf = requestAnimationFrame(frame); }); },
      stop() { running = false; cancelAnimationFrame(raf); },
      final() { this.stop(); ready(() => { build(); draw(99); }); }
    };
  }


  // ── 캔버스 장면 공용: 크기 맞추기 · 재생 고리 · 글꼴 기다리기 ──
  const fitCanvas = (root, cv, g) => { const W = root.offsetWidth, H = root.offsetHeight, R = Math.min(2, Math.max(1, (devicePixelRatio || 1) * (window.__k || 1))); cv.width = Math.round(W * R); cv.height = Math.round(H * R); g.setTransform(R, 0, 0, R, 0, 0); return [W, H]; };
  const Loop = (build, draw, dur, fonts) => {
    let raf = 0, t0 = 0, running = false;
    const ready = cb => (document.fonts ? Promise.all(fonts.map(f => document.fonts.load(f))).then(cb, cb) : cb());
    const frame = now => { const t = (now - t0) / 1000; draw(t); if (running && t < dur) raf = requestAnimationFrame(frame); else running = false; };
    return {
      run() { this.stop(); ready(() => { build(); if (RM) return draw(99); running = true; t0 = performance.now(); raf = requestAnimationFrame(frame); }); },
      stop() { running = false; cancelAnimationFrame(raf); },
      final() { this.stop(); ready(() => { build(); draw(99); }); }
    };
  };
  // ── 입체 글자(공용): 아주 굵은 글자에 두께를 줘 덩어리처럼. 앞면은 위가 밝은 그러데이션, 옆면은 두 톤 ──
  const BHS = '"Black Han Sans"';
  const extrude = (text, f, front, side, depth) => {
    const font = '400 ' + f + 'px ' + BHS, mc = document.createElement('canvas').getContext('2d'); mc.font = font;
    const tm = mc.measureText(text), asc = Math.ceil(tm.actualBoundingBoxAscent || f * .8), desc = Math.ceil(tm.actualBoundingBoxDescent || f * .06);
    const D = Math.max(2, Math.round(f * depth)), ex = .62, ey = -.5, pad = 4;
    const cw = Math.ceil(tm.width) + pad * 2 + Math.ceil(D * ex), ch = asc + desc + pad * 2 + Math.ceil(D * -ey), ox = pad, oy = pad + Math.ceil(D * -ey) + asc;
    const tint = col => { const c = document.createElement('canvas'); c.width = cw; c.height = ch; const x = c.getContext('2d'); x.font = font; x.textBaseline = 'alphabetic'; x.fillStyle = col; x.fillText(text, ox, oy); return c; };
    const c = document.createElement('canvas'); c.width = cw; c.height = ch; const x = c.getContext('2d');
    const sA = tint(side[1]), sB = tint(side[0]);
    for (let i = D; i >= 1; i--) x.drawImage(i > D * .45 ? sA : sB, i * ex, i * ey);
    x.drawImage(tint('rgba(255,255,255,.5)'), 0, -1);
    const fc = tint('#000'), fx = fc.getContext('2d'); fx.globalCompositeOperation = 'source-in';
    const gr = fx.createLinearGradient(0, oy - asc, 0, oy + desc); gr.addColorStop(0, front[0]); gr.addColorStop(1, front[1]); fx.fillStyle = gr; fx.fillRect(0, 0, cw, ch);
    x.drawImage(fc, 0, 0);
    return { cv: c, w: cw, h: ch, ox, oy, adv: tm.width, asc, desc };
  };
  const IVORY = [['#FAF5EC', '#D8CDBC'], ['#8C7F6E', '#5A5045']];

  // ── 칙칙폭폭 지나가기: 음절 하나 = 객차 한 량. 바퀴 없는 입체 글자 열차가 오른쪽에서 들어와 덜컹이며 멈춤 ──
  function Train(root) {
    const cv = root.querySelector('canvas'), g = cv.getContext('2d'), TEXT = '새로운 출발';
    let W, H, f, u, railY, cars, len, endX, startX, bg, r, plate, chTop;
    const MOVE = 3.8, T0 = .25;
    const build = () => {
      [W, H] = fitCanvas(root, cv, g); u = W / 1600; f = Math.round(W * (W < 800 ? .15 : .118)); railY = H * .7;
      r = f * .088; plate = f * .085; chTop = railY - plate - f * .02;
      cars = []; let x = 0;
      [...TEXT].forEach(ch => { if (!ch.trim()) { x += f * .34; return; } const sp = extrude(ch, f, ...IVORY, .2); cars.push({ sp, x, w: sp.adv }); x += sp.adv + f * .17; });
      len = x - f * .17; endX = (W - len) / 2; startX = W + f * .8;
      // 배경: 해 질 녘 하늘 · 먼 지평선 · 레일과 침목(한 번만 그려 둠)
      bg = document.createElement('canvas'); bg.width = cv.width; bg.height = cv.height; const b = bg.getContext('2d'); b.setTransform(cv.width / W, 0, 0, cv.height / H, 0, 0);
      const hz = railY - f * .42, sky = b.createLinearGradient(0, 0, 0, hz);
      sky.addColorStop(0, '#0F1219'); sky.addColorStop(.62, '#231F24'); sky.addColorStop(.9, '#4A3830'); sky.addColorStop(1, '#6A4A36');
      b.fillStyle = sky; b.fillRect(0, 0, W, hz);
      b.fillStyle = '#16141A'; b.beginPath(); b.moveTo(0, hz);
      for (let k = 0; k <= 24; k++) { const xx = W * k / 24; b.lineTo(xx, hz - f * (.12 + .1 * Math.abs(Math.sin(k * 1.7)) + .06 * Math.sin(k * .6))); }
      b.lineTo(W, hz); b.closePath(); b.fill();
      const gd = b.createLinearGradient(0, hz, 0, H); gd.addColorStop(0, '#1D1A18'); gd.addColorStop(1, '#090808'); b.fillStyle = gd; b.fillRect(0, hz, W, H - hz);
      for (let xx = -f; xx < W + f; xx += f * .42) { b.fillStyle = '#2A2521'; b.fillRect(xx, railY + f * .03, f * .22, f * .05); }
      b.fillStyle = '#3B3631'; b.fillRect(0, railY - f * .015, W, f * .045);
      b.fillStyle = '#9A9085'; b.fillRect(0, railY - f * .015, W, Math.max(1, f * .008));
    };
    const pos = t => { const p = Math.max(0, Math.min(1, (t - T0) / MOVE)); return [endX + (startX - endX) * Math.pow(1 - p, 2.4), (p < 1 ? 2.4 * Math.pow(1 - p, 1.4) : 0)]; };
    const draw = t => {
      g.setTransform(cv.width / W, 0, 0, cv.height / H, 0, 0); g.drawImage(bg, 0, 0, W, H);
      const [X, sp] = pos(t), ds = t - T0 - MOVE, J = f * 1.05;
      // 그림자
      g.fillStyle = 'rgba(0,0,0,.45)'; g.beginPath(); g.ellipse(X + len / 2, railY + f * .05, len / 2 + f * .1, f * .06, 0, 0, 6.2832); g.fill();
      // 전조등 빛(맨 앞 칸 왼쪽)
      const hx = X - f * .04, hy = chTop - f * .12, cone = g.createLinearGradient(hx, 0, hx - f * 3, 0);
      cone.addColorStop(0, 'rgba(255,236,200,.28)'); cone.addColorStop(1, 'rgba(255,236,200,0)');
      g.fillStyle = cone; g.beginPath(); g.moveTo(hx, hy - f * .03); g.lineTo(hx - f * 3, hy - f * .5); g.lineTo(hx - f * 3, railY); g.lineTo(hx, hy + f * .05); g.closePath(); g.fill();
      cars.forEach((c, i) => {
        const slack = ds > 0 ? f * .07 * Math.exp(-ds * 3.5) * Math.sin(ds * 13 - i * .5) * (i / Math.max(1, cars.length - 1)) : 0;
        const cx = X + c.x + slack, b1x = cx + c.w * .2, b2x = cx + c.w * .8;
        const bump = bx => { const ph = ((bx % J) + J) % J; return Math.exp(-ph / (f * .05)); };
        const k1 = bump(b1x), k2 = bump(b2x), lift = -(k1 + k2) / 2 * f * .045 * sp, tilt = (k2 - k1) * .02 * sp;
        // 연결고리
        if (i < cars.length - 1) { const nx = X + cars[i + 1].x; g.fillStyle = '#2B2723'; g.fillRect(cx + c.w, chTop + plate * .35 + lift, nx - cx - c.w, plate * .3); }
        g.save(); g.translate(cx + c.w / 2, chTop + lift); g.rotate(tilt);
        // 속도가 빠를 때 뒤로 잔상
        if (sp > .2) for (let k = 3; k >= 1; k--) { g.globalAlpha = .1 * sp; g.drawImage(c.sp.cv, -c.w / 2 - c.sp.ox + k * f * .07 * sp, -c.sp.oy - c.sp.desc * .2); }
        g.globalAlpha = 1; g.drawImage(c.sp.cv, -c.w / 2 - c.sp.ox, -c.sp.oy - c.sp.desc * .2);
        // 차대
        g.fillStyle = '#26221F'; g.fillRect(-c.w / 2 - f * .03, 0, c.w + f * .06, plate);
        g.fillStyle = 'rgba(255,255,255,.2)'; g.fillRect(-c.w / 2 - f * .03, 0, c.w + f * .06, Math.max(1, plate * .16));
        g.restore();
        if (i === 0) { g.fillStyle = '#FFF4DC'; g.beginPath(); g.arc(hx, hy + lift, f * .035, 0, 6.2832); g.fill(); }
      });
    };
    return Loop(build, draw, T0 + MOVE + 1.6, ['400 40px ' + BHS]);
  }

  // ── 쿵! 내려앉기: 그림자가 먼저 커지고 → 무거운 입체 글자가 떨어져 쿵 → 흔들림·바닥 균열·먼지 → 결론만 남음 ──
  function Thud(root) {
    const cv = root.querySelector('canvas'), g = cv.getContext('2d');
    let W, H, f, u, gy, words, total, x0, bg, cracks, dust, chips, lastT, spawned, puff, beam;
    const TL = 1.05, FALL = .5;
    const rnd = (a, b) => a + Math.random() * (b - a);
    const build = () => {
      [W, H] = fitCanvas(root, cv, g); u = W / 1600; f = Math.round(W * (W < 800 ? .17 : .105)); gy = H * .7;
      words = [extrude('기간', f, ...IVORY, .22), extrude('절반', f, ['#F6B48C', '#D96A3E'], ['#8E4C31', '#5E3222'], .22)];
      const gap = f * .3; total = words[0].adv + gap + words[1].adv; x0 = (W - total) / 2; words[1].dx = words[0].adv + gap; words[0].dx = 0;
      bg = document.createElement('canvas'); bg.width = cv.width; bg.height = cv.height; const b = bg.getContext('2d'); b.setTransform(cv.width / W, 0, 0, cv.height / H, 0, 0);
      const wall = b.createLinearGradient(0, 0, 0, gy); wall.addColorStop(0, '#0B0B0E'); wall.addColorStop(1, '#1A1817'); b.fillStyle = wall; b.fillRect(0, 0, W, gy);
      const fl = b.createLinearGradient(0, gy, 0, H); fl.addColorStop(0, '#24211E'); fl.addColorStop(1, '#0A0909'); b.fillStyle = fl; b.fillRect(0, gy, W, H - gy);
      b.fillStyle = 'rgba(255,255,255,.05)'; b.fillRect(0, gy, W, 1);
      // 균열: 착지면에서 바깥으로 갈라지는 선
      cracks = []; const cx = W / 2;
      for (let i = 0; i < 9; i++) {
        let x = rnd(x0 + total * .05, x0 + total * .95), y = gy + 1, side = x < cx ? -1 : 1, head = side < 0 ? Math.PI - rnd(-.05, .3) : rnd(-.05, .3), pts = [[x, y]];
        const n = 6 + (Math.random() * 5 | 0);
        for (let k = 0; k < n; k++) { head += rnd(-.45, .45); head = side < 0 ? Math.min(Math.PI + .05, Math.max(Math.PI - .5, head)) : Math.max(-.05, Math.min(.5, head)); const L = f * rnd(.07, .17); x += Math.cos(head) * L; y += Math.abs(Math.sin(head)) * L * .55; pts.push([x, y]); }
        cracks.push({ pts, w: f * rnd(.014, .026) });
      }
      // 먼지 알갱이 그림(부드러운 점)
      puff = document.createElement('canvas'); puff.width = puff.height = 64; const pc = puff.getContext('2d'), pg = pc.createRadialGradient(32, 32, 0, 32, 32, 32);
      pg.addColorStop(0, 'rgba(200,190,176,1)'); pg.addColorStop(1, 'rgba(200,190,176,0)'); pc.fillStyle = pg; pc.fillRect(0, 0, 64, 64);
      beam = document.createElement('canvas'); beam.width = Math.ceil(W * .9); beam.height = Math.ceil(gy); const bc = beam.getContext('2d'), bw2 = beam.width / 2;
      bc.filter = 'blur(' + Math.round(f * .25) + 'px)'; const bgd = bc.createLinearGradient(0, 0, 0, gy); bgd.addColorStop(0, 'rgba(255,238,215,0)'); bgd.addColorStop(1, 'rgba(255,238,215,.075)');
      bc.fillStyle = bgd; bc.beginPath(); bc.moveTo(bw2 - f * .35, 0); bc.lineTo(bw2 + f * .35, 0); bc.lineTo(bw2 + total * .62, gy); bc.lineTo(bw2 - total * .62, gy); bc.closePath(); bc.fill();
      dust = []; chips = []; lastT = 0; spawned = false;
    };
    const spawn = () => {
      spawned = true; const cx = x0 + total / 2;
      for (let i = 0; i < 300; i++) { const x = rnd(x0 - f * .1, x0 + total + f * .1), dir = Math.sign(x - cx) || 1; dust.push({ x, y: gy - rnd(0, f * .15), vx: dir * rnd(2, 13) * u * (.4 + Math.abs(x - cx) / total), vy: -rnd(.3, 2.4) * u, r: rnd(12, 28) * u, a: rnd(.14, .28), life: rnd(1.8, 3), age: 0 }); }
      for (let i = 0; i < 26; i++) chips.push({ x: rnd(x0, x0 + total), y: gy - 2, vx: rnd(-6, 6) * u, vy: -rnd(3, 8) * u, s: rnd(2, 5) * u, rot: rnd(0, 6), vr: rnd(-.3, .3), bounced: 0 });
    };
    const draw = t => {
      const dt = Math.min(.05, Math.max(0, t - lastT)), fr = dt * 60; lastT = t;
      if (t >= TL && !spawned && t < TL + 3) spawn();
      const at = t - TL, shake = at > 0 && at < .55 ? f * .07 * Math.exp(-at * 8) : 0;
      g.setTransform(cv.width / W, 0, 0, cv.height / H, 0, 0);
      g.translate(rnd(-1, 1) * shake, rnd(-1, 1) * shake * .7);
      g.drawImage(bg, -f * .2, -f * .2, W + f * .4, H + f * .4);
      // 위에서 떨어지는 조명(착지 뒤 살짝 흔들림)
      const sway = at > 0 ? f * .3 * Math.sin(at * 2.6) * Math.exp(-at * .9) : 0, lx = W / 2 + sway;
      const spot = g.createRadialGradient(lx, gy + f * .2, 0, lx, gy + f * .2, total * .75); spot.addColorStop(0, 'rgba(255,238,215,.24)'); spot.addColorStop(1, 'rgba(255,238,215,0)');
      g.save(); g.translate(lx, gy + f * .2); g.scale(1, .32); g.translate(-lx, -(gy + f * .2)); g.fillStyle = spot; g.beginPath(); g.arc(lx, gy + f * .2, total * .75, 0, 6.2832); g.fill(); g.restore();
      g.drawImage(beam, lx - beam.width / 2, 0);
      // 균열
      if (at > 0) {
        const rev = Math.min(1, at / .22), fade = at > 1.5 ? .55 : 1;
        cracks.forEach(c => { const n = Math.max(1, Math.round((c.pts.length - 1) * rev)); g.strokeStyle = 'rgba(0,0,0,' + .8 * fade + ')'; g.lineWidth = c.w; g.lineJoin = 'round'; g.beginPath(); g.moveTo(c.pts[0][0], c.pts[0][1]); for (let k = 1; k <= n; k++) g.lineTo(c.pts[k][0], c.pts[k][1]); g.stroke();
          g.strokeStyle = 'rgba(255,240,220,' + .16 * fade + ')'; g.lineWidth = Math.max(.6, c.w * .4); g.beginPath(); g.moveTo(c.pts[0][0], c.pts[0][1] + c.w); for (let k = 1; k <= n; k++) g.lineTo(c.pts[k][0], c.pts[k][1] + c.w); g.stroke(); });
      }
      // 떨어지는 동안: 위치(가속) · 그림자는 점점 커지고 진해짐
      const p = Math.max(0, Math.min(1, (t - (TL - FALL)) / FALL)), yOff = t < TL ? -(H * .95) * (1 - p * p) : 0;
      const sh = t < TL - FALL ? .08 : t < TL ? .08 + .5 * p : .58, sw = t < TL ? .45 + .55 * p : 1;
      g.fillStyle = 'rgba(0,0,0,' + sh + ')'; g.beginPath(); g.ellipse(x0 + total / 2 + f * .08, gy + f * .04, total / 2 * sw + f * .1, f * .07 * sw, 0, 0, 6.2832); g.fill();
      if (t >= TL - FALL) {
        const s = at > 0 ? Math.exp(-at * 9) : 0, sy = 1 - .13 * s * Math.cos(at * 26), sx = 1 + .055 * s * Math.cos(at * 26);
        const drawWords = (dy, al) => { g.save(); g.globalAlpha = al; g.translate(x0 + total / 2, gy + dy); g.scale(sx, sy); words.forEach(w => g.drawImage(w.cv, -total / 2 + w.dx - w.ox, -w.oy - w.desc)); g.restore(); };
        if (t < TL) for (let k = 3; k >= 1; k--) drawWords(yOff - k * f * .16 * p, .1);
        drawWords(yOff, 1);
      }
      // 먼지 · 파편
      if (spawned && at < 3) {
        g.save(); dust.forEach(d => { d.age += dt; if (d.age > d.life) return; const k = Math.pow(.955, fr); d.vx *= k; d.vy = d.vy * k - .01 * u * fr; d.x += d.vx * fr; d.y += d.vy * fr; d.r += .35 * u * fr;
          g.globalAlpha = d.a * (1 - d.age / d.life); g.drawImage(puff, d.x - d.r, d.y - d.r, d.r * 2, d.r * 2); }); g.restore();
        chips.forEach(c => { if (c.bounced < 2) { c.vy += .35 * u * fr; c.x += c.vx * fr; c.y += c.vy * fr; c.rot += c.vr * fr; if (c.y > gy - c.s / 2 && c.vy > 0) { c.y = gy - c.s / 2; c.vy *= -.3; c.vx *= .5; c.bounced++; } }
          g.save(); g.translate(c.x, c.y); g.rotate(c.rot); g.fillStyle = '#3A342E'; g.fillRect(-c.s / 2, -c.s / 2, c.s, c.s); g.restore(); });
      }
      // 말머리: 쿵 다음에 조용히
      const la = Math.max(0, Math.min(1, (at - .65) / .5));
      if (la > 0) { g.save(); g.globalAlpha = la; g.fillStyle = '#B9B0A3'; g.font = '600 ' + Math.round(f * .16) + 'px "Noto Sans KR"'; g.textAlign = 'center'; try { g.letterSpacing = Math.round(f * .05) + 'px'; } catch (e) {} g.fillText('그래서 결론은', W / 2, gy - words[0].asc - f * .42); g.restore(); }
    };
    return Loop(build, draw, TL + 3.2, ['400 40px ' + BHS, '600 20px "Noto Sans KR"']);
  }

  // 비포/애프터 끌기
  document.querySelectorAll('.d-ba').forEach(el => {
    const move = e => { const r = el.getBoundingClientRect(); el.style.setProperty('--x', Math.max(0, Math.min(100, (e.clientX - r.left) / r.width * 100)) + '%'); };
    el.addEventListener('pointerdown', e => { el.classList.add('drag'); el.setPointerCapture(e.pointerId); move(e); });
    el.addEventListener('pointermove', e => { if (el.hasPointerCapture(e.pointerId)) move(e); });
  });

  const play = (s, end) => {
    s.classList.remove('play'); void s.offsetWidth; s.classList.add('play');
    s.querySelectorAll('.d-ba').forEach(el => { el.classList.remove('drag'); el.style.removeProperty('--x'); });
    s.querySelectorAll('[data-js]').forEach(el => DEMOS[el.dataset.js](el, end));
  };
  const count = document.getElementById('count');
  // 크게 보기(화면 전체 재생)
  const fv = document.getElementById('fullv') || document.createElement('div'), ENG = { pop: Fireworks, asm: Assembly, train: Train, thud: Thud }, TAG = { pop: '⑥ 팡! 터뜨리기 · 크게 보기', asm: '⑥ 타이포 조립 · 크게 보기', train: '⑥ 칙칙폭폭 지나가기 · 크게 보기', thud: '⑥ 쿵! 내려앉기 · 크게 보기' };
  let fvk = null; const fvEl = () => fv.querySelector('[data-kind=' + fvk + ']');
  const openFull = kind => {
    slides[cur].querySelectorAll('.demo [data-js]').forEach(e => e._e && e._e.stop());
    fvk = kind; fv.className = 'fullv open'; fv.querySelectorAll('[data-kind]').forEach(e => e.classList.toggle('on', e.dataset.kind === kind)); document.getElementById('fvtag').textContent = TAG[kind];
    const el = fvEl(); el._e = el._e || ENG[kind](el); el._e.run();
  };
  const closeFull = () => { if (!fv.classList.contains('open')) return; const el = fvEl(); el._e && el._e.stop(); fv.className = 'fullv'; };
  const replayFull = () => fvEl()._e.run();
  document.querySelectorAll('[data-open]').forEach(b => b.addEventListener('click', () => openFull(b.dataset.open)));
  (fv.querySelector('[data-fv=replay]') || {}).onclick = replayFull;
  (fv.querySelector('[data-fv=close]') || {}).onclick = closeFull;
  const go = i => {
    i = Math.max(0, Math.min(slides.length - 1, i));
    closeFull(); slides[cur].querySelectorAll('[data-js]').forEach(e => e._e && e._e.stop());
    slides[cur].classList.remove('on', 'play'); cur = i; slides[cur].classList.add('on'); play(slides[cur]);
    count.textContent = (cur + 1) + ' / ' + slides.length;
    history.replaceState(null, '', '#' + (cur + 1));
  };
  document.getElementById('prev').onclick = () => go(cur - 1);
  document.getElementById('next').onclick = () => go(cur + 1);
  document.getElementById('replay').onclick = () => fv.classList.contains('open') ? replayFull() : play(slides[cur]);
  document.querySelectorAll('[data-go]').forEach(a => a.addEventListener('click', () => go(+a.dataset.go - 1)));
  addEventListener('keydown', e => {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    const k = e.key;
    if (fv.classList.contains('open')) {
      if (k === 'Escape') closeFull(); else if (k === 'r' || k === 'R' || k === ' ') replayFull(); else return;
      e.preventDefault(); return;
    }
    if (k === 'ArrowRight' || k === 'PageDown' || k === ' ') { go(cur + 1); e.preventDefault(); }
    else if (k === 'ArrowLeft' || k === 'PageUp') { go(cur - 1); e.preventDefault(); }
    else if (k === 'Home') go(0); else if (k === 'End') go(slides.length - 1);
    else if (k === 'r' || k === 'R') play(slides[cur]);
  });
  // 인쇄: 모든 장을 끝 화면으로
  addEventListener('beforeprint', () => slides.forEach(s => { s.classList.add('play'); s.querySelectorAll('[data-js]').forEach(el => DEMOS[el.dataset.js](el, true)); }));
  addEventListener('afterprint', () => slides.forEach((s, i) => { if (i !== cur) s.classList.remove('play'); }));
  go((parseInt(location.hash.slice(1), 10) || 1) - 1);
})();
