// 근거 키트 장표(#91 · #103 · #110)의 캔버스를 그대로 PNG 로 떠낸다(2배 해상도). 간지는 섹션 단추 Ⅰ~Ⅴ 를 눌러 다섯 상태를 뜬다.
// 실행: node scripts/kit_img.js <임시 폴더>   → 이어서 python3 scripts/kit_img.py <임시 폴더> 가 잘라서 kit/img/ 에 넣는다
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const OUT=process.argv[2];
(async()=>{const b=await chromium.launch();
for(const n of [91,103,110]){
  const p=await b.newPage({viewport:{width:1280,height:900},deviceScaleFactor:2});
  await p.emulateMedia({reducedMotion:'reduce'});
  await p.goto('file://'+require('path').resolve(__dirname,'..')+'/refs/'+n+'.html');await p.waitForTimeout(5000);
  const save=async(tag)=>{const list=await p.evaluate(()=>[...document.querySelectorAll('canvas')].map(c=>({k:c.className||'plain',w:c.width,h:c.height,d:c.toDataURL('image/png')})));
    list.forEach((c,i)=>fs.writeFileSync(path.join(OUT,`${n}-${tag}-${i}-${c.k}-${c.w}x${c.h}.png`),Buffer.from(c.d.split(',')[1],'base64')));return list.length};
  console.log(n,'canvases',await save('init'));
  const btns=await p.evaluate(()=>[...document.querySelectorAll('button')].map(x=>x.textContent.trim()));console.log(n,btns.join('|'));
  for(const [i,t] of ['I','II','III','IV','V'].entries()){
    const ok=await p.evaluate(t=>{const R={I:['I','Ⅰ'],II:['II','Ⅱ'],III:['III','Ⅲ'],IV:['IV','Ⅳ'],V:['V','Ⅴ']}[t];const x=[...document.querySelectorAll('button')].find(x=>R.includes(x.textContent.trim())||R.some(r=>x.textContent.trim().startsWith(r+' ')));if(x){x.click();return x.textContent.trim()}return null},t);
    await p.waitForTimeout(2500); if(ok) await save('s'+(i+1)); else console.log('no button',t);
  }
  await p.close();
}
await b.close()})()
