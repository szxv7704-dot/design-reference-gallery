// 강의 · 영상 · 업무도구 세 페이지 공용. <body data-page="deck | video | tool">이 어느 데이터를 읽을지 정한다
(() => {
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
// 데이터에 적는 경로는 저장소 뿌리 기준(lectures/files/...) → 이 페이지 기준으로. 바깥 주소는 그대로
const href = p => /^(https?:)?\/\//.test(p) ? p : '../' + String(p).replace(/^\.?\//, '');
const svg = d => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${d}</svg>`;
const ICON = {
  deck: svg('<path d="M3 4h18"/><path d="M4 4v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-10"/><path d="M12 16v4"/><path d="M9 20h6"/><path d="M8 12l3 -3l2 2l3 -3"/>'),
  video: svg('<path d="M15 10l4.55 -2.28a1 1 0 0 1 1.45 .9v6.76a1 1 0 0 1 -1.45 .9l-4.55 -2.28v-4z"/><path d="M3 8a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v8a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2z"/>'),
  tool: svg('<path d="M7 10h3v-3l-3.5 -3.5a6 6 0 0 1 8 8l6 6a2 2 0 0 1 -3 3l-6 -6a6 6 0 0 1 -8 -8l3.5 3.5"/>'),
  chat: svg('<path d="M21 14l-3 -3h-7a1 1 0 0 1 -1 -1v-6a1 1 0 0 1 1 -1h9a1 1 0 0 1 1 1v10"/><path d="M14 15v2a1 1 0 0 1 -1 1h-7l-3 3v-10a1 1 0 0 1 1 -1h2"/>'),
  out: svg('<path d="M12 6h-6a2 2 0 0 0 -2 2v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-6"/><path d="M11 13l9 -9"/><path d="M15 4h5v5"/>'),
  down: svg('<path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2"/><path d="M7 11l5 5l5 -5"/><path d="M12 4v12"/>'),
  play: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4v16l13 -8z"/></svg>'
};
const PAGE = {
  deck: {data: 'lectures.json', unit: '강의', empty: '아직 올린 강의안이 없습니다.<br>강의안이 올라오면 여기에 보입니다.'},
  video: {data: 'videos.json', unit: '영상', empty: '아직 올린 강의 영상이 없습니다.<br>영상이 올라오면 여기에 보입니다.'},
  tool: {data: 'tools.json', unit: '도구', empty: '아직 올린 업무도구가 없습니다.<br>도구와 예제파일이 올라오면 여기에 보입니다.'}
};
const page = document.body.dataset.page, P = PAGE[page];

// 날짜는 'YYYY-MM-DD'를 그대로 읽는다(new Date('2026-11-24')는 UTC로 읽혀 하루 밀릴 수 있다)
const DOW = '일월화수목금토';
const ymd = s => { const [y, m, d] = String(s).split('-').map(Number); return new Date(y, m - 1, d); };
const fmt = s => { const t = ymd(s); return `${t.getFullYear()}. ${t.getMonth() + 1}. ${t.getDate()}.(${DOW[t.getDay()]})`; };
const today = (() => { const n = new Date(); return new Date(n.getFullYear(), n.getMonth(), n.getDate()); })();
// 예정 · 오늘 · 완료는 적지 않고 날짜로 정한다
const stateOf = x => { if (!x.date) return ''; const t = ymd(x.date); return t > today ? 'soon' : +t === +today ? 'today' : 'done'; };
const BADGE = {soon: '예정', today: '오늘', done: '완료'};

const when = x => x.date ? `<div class="when"><time datetime="${esc(x.date)}">${esc(fmt(x.date))}</time>${page === 'deck' ? `<span class="badge ${stateOf(x)}">${BADGE[stateOf(x)]}</span>` : ''}</div>` : '';
const meta = xs => (xs = xs.filter(Boolean)).length ? `<ul class="meta">${xs.map(x => `<li>${esc(x)}</li>`).join('')}</ul>` : '';
const tags = x => (x.tags || []).length ? `<div class="tags">${x.tags.map(t => `<span>${esc(t)}</span>`).join('')}</div>` : '';
const files = x => (x.files || []).map(f => `<a class="btn ghost" href="${esc(href(f.href))}" download>${ICON.down} ${esc(f.name)}${f.kind ? ` <small>${esc(f.kind)}</small>` : ''}</a>`);

const CARD = {
  deck(x){
    const s = stateOf(x), a = [];
    if (x.deck) a.push(`<a class="btn" href="${esc(href(x.deck))}" target="_blank" rel="noopener">강의안 열기 ${ICON.out}</a>`);
    if (x.video) a.push(`<a class="btn ghost" href="videos.html#${esc(x.video)}">${ICON.video} 강의 영상</a>`);
    a.push(...files(x));
    if (!a.length) a.push(`<span class="btn ghost" aria-disabled="true">${s === 'done' || !s ? '자료 정리 중' : '강의 후 올라옵니다'}</span>`);
    return `<li class="item${s === 'done' ? ' done' : ''}" id="${esc(x.id || '')}"><span class="ico">${ICON.deck}</span><div>${when(x)}<h3>${esc(x.title)}</h3>
      ${x.desc ? `<p>${esc(x.desc)}</p>` : ''}${meta([x.time, x.place, x.audience])}${tags(x)}<div class="acts">${a.join('')}</div></div></li>`;
  },
  video(x){
    const yt = ytId(x.youtube || x.url || ''), thumb = x.thumb ? href(x.thumb) : yt ? `https://i.ytimg.com/vi/${yt}/hqdefault.jpg` : '';
    const playable = yt || x.src;
    const screen = playable ? `<button type="button" class="screen" data-yt="${esc(yt || '')}" data-src="${esc(x.src ? href(x.src) : '')}" aria-label="${esc(x.title)} 재생">
        ${thumb ? `<img src="${esc(thumb)}" alt="" loading="lazy">` : ''}<span class="play">${ICON.play}</span>${x.duration ? `<span class="dur">${esc(x.duration)}</span>` : ''}</button>` : '';
    const a = [];
    if (!playable && x.url) a.push(`<a class="btn" href="${esc(x.url)}" target="_blank" rel="noopener">영상 보기 ${ICON.out}</a>`);
    if (x.lecture) a.push(`<a class="btn ghost" href="index.html#${esc(x.lecture)}">${ICON.deck} 강의안</a>`);
    a.push(...files(x));
    return `<li class="item vid" id="${esc(x.id || '')}">${screen}<div class="body">${when(x)}<h3>${esc(x.title)}</h3>
      ${x.desc ? `<p>${esc(x.desc)}</p>` : ''}${meta([!playable && x.duration, x.speaker])}${tags(x)}${a.length ? `<div class="acts">${a.join('')}</div>` : ''}</div></li>`;
  },
  tool(x){
    const a = [];
    if (x.href) a.push(`<a class="btn" href="${esc(href(x.href))}" target="_blank" rel="noopener">${esc(x.open || '도구 열기')} ${ICON.out}</a>`);
    a.push(...files(x));
    if (!a.length) a.push('<span class="btn ghost" aria-disabled="true">준비 중</span>');
    return `<li class="item" id="${esc(x.id || '')}"><span class="ico">${ICON.tool}</span><div>${x.version || x.date ? `<div class="when">${esc([x.version, x.date && fmt(x.date) + ' 갱신'].filter(Boolean).join(' · '))}</div>` : ''}<h3>${esc(x.title)}</h3>
      ${x.desc ? `<p>${esc(x.desc)}</p>` : ''}${meta([x.how])}${tags(x)}<div class="acts">${a.join('')}</div></div></li>`;
  }
};
// 유튜브 주소 모양 여럿(watch?v= · youtu.be/ · shorts/ · embed/ · 아이디만)에서 아이디만
function ytId(u){
  if (/^[\w-]{11}$/.test(u)) return u;
  const m = String(u).match(/(?:youtu\.be\/|[?&]v=|\/(?:shorts|embed|live)\/)([\w-]{11})/);
  return m ? m[1] : '';
}

let data = null, pick = '';
function render(){
  const items = data.items;
  let rows = items;
  if (page === 'deck') {
    const soon = items.filter(x => stateOf(x) && stateOf(x) !== 'done').sort((a, b) => ymd(a.date) - ymd(b.date));   // 가까운 강의부터
    const rest = items.filter(x => !soon.includes(x)).sort((a, b) => (b.date ? ymd(b.date) : 0) - (a.date ? ymd(a.date) : 0));   // 지난 강의는 최근부터
    const n = {'': items.length, soon: soon.length, done: rest.length};
    document.querySelectorAll('#seg button').forEach(b => { b.querySelector('em').textContent = n[b.dataset.s]; b.setAttribute('aria-pressed', b.dataset.s === pick); });
    $('#seg').hidden = !soon.length || !rest.length;
    rows = pick === 'soon' ? soon : pick === 'done' ? rest : soon.concat(rest);
  } else if (items.some(x => x.date)) {
    rows = items.slice().sort((a, b) => (b.date ? ymd(b.date) : 0) - (a.date ? ymd(a.date) : 0));   // 최근부터
  }
  const c = data.chat;
  const chat = c && page === 'deck' && pick !== 'done' ? `<li class="chat"><span class="ico">${ICON.chat}</span><div><b>${esc(c.title || '강의 소통방')}</b>${c.desc ? `<p>${esc(c.desc)}</p>` : ''}</div>
    ${c.url ? `<a class="btn" href="${esc(c.url)}" target="_blank" rel="noopener">들어가기 ${ICON.out}</a>` : '<span class="btn" aria-disabled="true">준비 중</span>'}</li>` : '';
  $('#list').className = page === 'video' && rows.length ? 'list vids' : 'list';
  $('#list').innerHTML = chat + (rows.length ? rows.map(CARD[page]).join('') : `<li class="empty"><span class="ico">${ICON[page]}</span>${P.empty}</li>`);
}

// 영상: 누를 때만 재생기를 넣는다(처음부터 넣으면 목록이 무겁고, 유튜브가 미리 쿠키를 심는다)
document.addEventListener('click', e => {
  const s = e.target.closest('.screen'); if (!s || s.querySelector('iframe,video')) return;
  if (s.dataset.yt) s.insertAdjacentHTML('beforeend', `<iframe src="https://www.youtube-nocookie.com/embed/${esc(s.dataset.yt)}?autoplay=1&rel=0" title="${esc(s.getAttribute('aria-label'))}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>`);
  else if (s.dataset.src) { s.insertAdjacentHTML('beforeend', `<video src="${esc(s.dataset.src)}" controls autoplay playsinline></video>`); }
  s.style.cursor = 'default';
});
$('#seg')?.addEventListener('click', e => { const b = e.target.closest('button'); if (!b) return; pick = b.dataset.s; render(); });

fetch('../data/' + P.data, {cache: 'no-cache'}).then(r => r.json()).then(d => {
  data = d; d.items = d.items || [];
  const n = d.items.length;
  $('#total').textContent = n ? n + '개' : '';
  if (page === 'deck' && n) {
    const k = d.items.filter(x => stateOf(x) === 'done').length, s = d.items.filter(x => stateOf(x) && stateOf(x) !== 'done').length;
    $('#summary').textContent = `강의 ${n}개` + (k ? ` · 완료 ${k}` : '') + (s ? ` · 예정 ${s}` : '');
  }
  if (d.updated) $('#stamp').textContent = ' · ' + fmt(d.updated).replace(/\(.\)$/, '') + ' 기준';
  render();
  if (location.hash) document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView();
}).catch(() => { $('#list').innerHTML = `<li class="empty">목록을 불러오지 못했습니다.</li>`; });
})();
