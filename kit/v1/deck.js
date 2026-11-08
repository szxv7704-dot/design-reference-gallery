/* 덱 키트 공용 엔진 v1 — 모든 계열이 같이 쓴다. 덱 HTML은 <section class="slide"> 만 쓰면 된다.
   - 1920 × 1080 무대를 창에 맞게 통째로 줄임(글자가 다시 흘러내리지 않음)
   - → · Space · PageDown · Enter = 다음, ← · PageUp = 이전, Home · End, F = 전체 화면, 화면 누르기 · 밀기
   - 장 수 · 점 · 쪽 표시(.page-no)는 장 개수로 자동(손으로 맞추지 않음), 주소 #3 = 3장
   - data-steps="n" 장: 안의 [data-step="1"…"n"] 를 누를 때마다 하나씩 보임
   - window.DECK = { go(장, 단계), next(), prev(), index, count } */
(function () {
  var stage = document.querySelector('.deck-stage'); if (!stage) return;
  var slides = [].slice.call(stage.children).filter(function (e) { return e.classList.contains('slide'); });
  var N = slides.length, cur = 0, step = 0;
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };
  function stepsOf(s) {
    var n = +s.getAttribute('data-steps') || 0;
    [].forEach.call(s.querySelectorAll('[data-step]'), function (e) { n = Math.max(n, +e.getAttribute('data-step') || 0); });
    return n;
  }
  // 발표 도구
  var ui = document.createElement('nav'); ui.className = 'deck-ui'; ui.setAttribute('aria-label', '장 넘기기');
  ui.innerHTML = '<button type="button" data-go="prev" aria-label="이전">←</button><span class="deck-dots" aria-hidden="true">' +
    slides.map(function () { return '<i></i>'; }).join('') + '</span><span class="deck-count" aria-live="polite"></span>' +
    '<button type="button" data-go="next" aria-label="다음">→</button>';
  document.body.appendChild(ui);
  var dots = ui.querySelectorAll('.deck-dots i'), count = ui.querySelector('.deck-count');
  slides.forEach(function (s, i) {
    s.setAttribute('role', 'group'); s.setAttribute('aria-roledescription', 'slide'); s.setAttribute('aria-label', (i + 1) + ' / ' + N);
    [].forEach.call(s.querySelectorAll('.page-no'), function (e) { e.textContent = pad(i + 1) + ' / ' + pad(N); });
  });
  function paint() {
    slides.forEach(function (s, i) { var on = i === cur; s.classList.toggle('is-on', on); s.setAttribute('aria-hidden', on ? 'false' : 'true'); if ('inert' in s) s.inert = !on; });
    [].forEach.call(slides[cur].querySelectorAll('[data-step]'), function (e) { e.classList.toggle('is-shown', +e.getAttribute('data-step') <= step); });
    [].forEach.call(dots, function (d, i) { d.classList.toggle('is-on', i === cur); });
    count.textContent = pad(cur + 1) + ' / ' + pad(N);
    if (history.replaceState) history.replaceState(null, '', '#' + (cur + 1));
    var fx = window.DECK_FX; if (fx && fx.enter) fx.enter(slides[cur], cur, step);
  }
  function go(n, k) { cur = Math.max(0, Math.min(N - 1, n)); step = Math.max(0, Math.min(stepsOf(slides[cur]), k || 0)); paint(); }
  function next() { if (step < stepsOf(slides[cur])) { step++; paint(); } else if (cur < N - 1) go(cur + 1, 0); }
  function prev() { if (step > 0) { step--; paint(); } else if (cur > 0) go(cur - 1, 99); }
  function fit() { var s = Math.min(innerWidth / 1920, innerHeight / 1080); stage.style.transform = 'translate(-50%,-50%) scale(' + s + ')'; }
  var busy = function (t) { return t && t.closest && t.closest('button,a,input,select,textarea,label,[data-no-advance]'); };
  document.addEventListener('keydown', function (e) {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    var k = e.key;
    if ((k === ' ' || k === 'Enter') && busy(e.target)) return;
    if (k === 'ArrowRight' || k === 'PageDown' || k === ' ' || k === 'Enter') { e.preventDefault(); next(); }
    else if (k === 'ArrowLeft' || k === 'PageUp') { e.preventDefault(); prev(); }
    else if (k === 'Home') go(0, 0); else if (k === 'End') go(N - 1, 99);
    else if (k === 'f' || k === 'F') { if (document.fullscreenElement) document.exitFullscreen(); else if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen(); }
  });
  stage.addEventListener('click', function (e) { if (!busy(e.target)) next(); });
  ui.addEventListener('click', function (e) { var b = e.target.closest('[data-go]'); if (b) (b.getAttribute('data-go') === 'next' ? next : prev)(); });
  var x0 = null;
  stage.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  stage.addEventListener('touchend', function (e) { if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null; if (Math.abs(dx) > 50) (dx < 0 ? next : prev)(); });
  var hideT = 0;   // 발표 도구는 마우스를 움직일 때만 잠깐 보인다
  addEventListener('mousemove', function () { document.body.classList.add('ui-on'); clearTimeout(hideT); hideT = setTimeout(function () { document.body.classList.remove('ui-on'); }, 1800); });
  addEventListener('resize', fit); fit();
  var h = parseInt((location.hash || '').slice(1), 10);
  go(h > 0 ? h - 1 : 0, 0);
  window.DECK = { go: go, next: next, prev: prev, get index() { return cur; }, get step() { return step; }, count: N };
})();
