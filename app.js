const CONTACT_EMAIL = "katzdoll@gmail.com"; // contact address used by every envelope icon
(()=>{
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const root=document.documentElement,mq=matchMedia('(prefers-color-scheme: dark)');
const DL='https://github.com/RyanAnthonyGibo/siliconplay.app/releases/latest/download/SiliconPlay.dmg'; // #DOWNLOAD_URL
const C={
 readme:{t:'readme.md',w:520,h:470,cls:'mono',html:`<span class="h"># SiliconPlay</span>
Android emulator for macOS. Play Android games on
your Mac with Apple silicon.

<span class="h">## Why it's fast</span>
- Android 16 runs natively on the ARM cores
  (Apple Hypervisor framework). No x86 translation.
- Vulkan is drawn by Metal.
- Shaders compiled in safe math mode, so foliage
  renders correctly.

<span class="h">## Features</span>
- Keyboard + gamepad overlay (WASD, J, 1–6)
- Ready-made layouts you can rearrange
- No kexts. No background services. No bundled apps.

<span class="h">## Measured</span> <span class="k">(MacBook Pro, M3 Max)</span>
- up to 60 fps in a demanding 3D game
- render resolution up to 2560×1440
- 7–43 ms key-to-game input latency

<span class="h">## Requirements</span>
- Mac with Apple silicon (M1 or later)
- macOS 14 or later

<span class="h">## Free</span>
SiliconPlay is free. Optionally support the project
→ open Donate.app

<a href="${DL}">Download SiliconPlay for Mac</a>`},
 controls:{t:'Controls.png',w:400,h:360,html:`<div class="keysbig"><kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd></div><p style="text-align:center">Move with <b>WASD</b>. Attack with <b>J</b>. Skills on <b>1–6</b>.</p><div class="krow"><kbd>J</kbd><kbd>1</kbd><kbd>2</kbd><kbd>3</kbd><kbd>4</kbd><kbd>5</kbd><kbd>6</kbd></div><p style="text-align:center;color:var(--mut);margin-top:12px">Remap keys or use a gamepad from the overlay.</p>`},
 donate:{t:'Donate.app',w:360,h:330,html:`<h3 style="font-size:20px">Free. Optionally support the project.</h3><p style="color:var(--mut);margin-top:6px">Supporters get an ad-free app. The ad never covers your game.</p><div class="tiers"><a class="main" href="https://www.paypal.com/webapps/billing/plans/subscribe?plan_id=P-2GR38954JS846013SNLPWRTY" target="_blank" rel="noopener"><b>$2/month</b><span>No ads</span></a><a href="https://www.paypal.com/webapps/billing/plans/subscribe?plan_id=P-1L50440531901720SNLPWR5Q" target="_blank" rel="noopener"><b>$5/month</b><span>No ads + early builds</span></a><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=siliconplay.app@gmail.com&amp;item_name=SiliconPlay&amp;currency_code=USD&amp;no_recurring=1" target="_blank" rel="noopener"><b>One time</b><span>Any amount</span></a></div>`},
 faq:{t:'FAQ.txt',w:470,h:340,cls:'mono',html:`<span class="h">Q: Which Macs does it work on?</span>
A: Mac computers with Apple silicon (M1, M2, M3, M4, M5,
   and newer) running macOS 14 or later. Intel Macs: no.

<span class="h">Q: Is my game account safe?</span>
A: SiliconPlay includes optional root and does not
   modify games. Follow each game's terms of service.

<span class="h">Q: Is the source code available?</span>
A: No. Licenses for third-party components are
   included with the app.

<span class="h">Q: Is it free?</span>
A: Yes. SiliconPlay is free. Supporting the project
   is optional.`},
 licenses:{t:'LICENSES.txt',w:480,h:420,cls:'mono',html:`Open-source notices
===================

SiliconPlay includes third-party components.
Full notices are on the website and are also
bundled inside the app.

<span class="h">Android Emulator / Android SDK</span>
Apache License 2.0, and the Android SDK terms.

<span class="h">QEMU</span>
Included as part of the emulator.
GNU GPL version 2.

→ <a href="licenses.html">Licenses &amp; open-source notices</a>

<a href="privacy.html">Privacy</a> · <a href="mailto:${CONTACT_EMAIL}">Contact</a>`},
 terminal:{t:'Terminal — zsh',w:540,h:300,cls:'term',html:`<span class="p">~ %</span> siliconplay --version
SiliconPlay 1.0
  guest      Android 16 (arm64)
  hypervisor Apple Hypervisor.framework
  graphics   Vulkan → Metal (safe math)
  requires   Apple silicon M1+, macOS 14+

<span class="p">~ %</span> siliconplay bench <span class="d"># MacBook Pro, M3 Max</span>
  fps        60
  resolution 2560×1440
  input      7–43 ms key-to-game

<span class="p">~ %</span> <span class="cursor"></span>`},
 installer:{t:'Install SiliconPlay',w:440,h:260,html:`<div class="inst"><img src="assets/icon-tile.png" alt="SiliconPlay app icon"><div><h3 style="font-size:18px">SiliconPlay</h3><p style="color:var(--mut)">Android emulator for macOS<br>Apple silicon · macOS 14+</p></div></div><div class="prog"><i></i></div><a class="btnp" href="${DL}">Download for Mac</a><a class="btng" href="#" data-open="donate">Donate</a>`},
 projects:{t:'More from Ryan',w:480,h:340,html:`<p class="pj-h">Other projects</p><div class="pj">
<a href="https://github.com/RyanAnthonyGibo" target="_blank" rel="noopener"><span class="pg pg-gh"><svg viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M8 7 3 12l5 5 1.4-1.4L5.8 12l3.6-3.6zm8 0-1.4 1.4 3.6 3.6-3.6 3.6L16 17l5-5z"/></svg></span><span><b>GitHub</b><small>My profile and public work</small></span><i>↗</i></a>
<a href="https://www.alequeria.com.br" target="_blank" rel="noopener"><span class="pg pg-lq"><svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M12 20 3.5 9.5A11 11 0 0 1 20.5 9.5z" opacity=".9"/><path d="M12 20V7M12 20 7 8.2M12 20l5-11.8" stroke="#fff" stroke-width="1" opacity=".7"/></svg></span><span><b>a Lequeria</b><small>Handmade bamboo hand fans for the electronic music crowd</small></span><i>↗</i></a>
<a href="https://www.cvtingressos.com.br" target="_blank" rel="noopener"><span class="pg pg-cvt"><svg viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M3 7h18v3a2 2 0 0 0 0 4v3H3v-3a2 2 0 0 0 0-4z"/><path d="M15 7v10" stroke="#fff" stroke-dasharray="2 2"/></svg></span><span><b>CVT Ingressos</b><small>Ticket marketplace: buy, sell, trade and donate tickets</small></span><i>↗</i></a>
<a href="https://instagram.com/fcknstar" target="_blank" rel="noopener"><span class="pg pg-ig"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="5"/><circle cx="12" cy="12" r="3.6"/><circle cx="16.8" cy="7.2" r=".6" fill="currentColor"/></svg></span><span><b>Instagram</b><small>@fcknstar · personal</small></span><i>↗</i></a>
</div>`},
 trash:{t:'Trash',w:360,h:220,html:`<p style="color:var(--mut);text-align:center;margin-top:40px">Trash is empty.<br>No bundled software here either.</p>`},
 mac:{t:'SiliconPlay',html:`<div style="text-align:center"><img src="assets/icon-tile.png" alt="SiliconPlay app icon" width="110" style="margin:10px auto"><h3 style="font-size:22px;margin-top:8px">SiliconPlay is for Mac.</h3><p style="color:var(--mut);margin-top:6px">It runs Android games on Mac computers with Apple silicon. Send yourself the link and download it on your Mac.</p><button class="btnp" data-copy>Copy Link</button><a class="btng" href="${DL}">Download</a><p class="copied" style="color:var(--mut);margin-top:10px" aria-live="polite"></p></div>`}
};

/* theme */
function toggleTheme(e){e&&e.preventDefault();const c=root.dataset.theme||(mq.matches?'dark':'light'),n=c==='dark'?'light':'dark';root.dataset.theme=n;try{localStorage.setItem('sp-theme',n)}catch(_){}closeMenus()}
/* copy */
function copyLink(e){e&&e.preventDefault();const u=location.href.split('#')[0];(navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(()=>say('Link copied.'),()=>say(u));closeMenus()}
function say(m){$$('.copied').forEach(p=>p.textContent=m)}
document.addEventListener('click',e=>{
 const t=e.target.closest('[data-theme-toggle]');if(t)return toggleTheme(e);
 const c=e.target.closest('[data-copy]');if(c)return copyLink(e);
 const o=e.target.closest('[data-open]');if(o){e.preventDefault();closeMenus();openWin(o.dataset.open)}
});
/* clock */
const fmt=new Intl.DateTimeFormat(undefined,{weekday:'short',hour:'numeric',minute:'2-digit'}),pf=new Intl.DateTimeFormat(undefined,{hour:'numeric',minute:'2-digit'});
function tick(){const d=new Date();$('#clock').textContent=fmt.format(d);$('#pclock').textContent=pf.format(d).replace(/\s?[AP]M/i,'')}
tick();setInterval(tick,15000);
/* menus */
function closeMenus(){$$('.menu').forEach(m=>{m.classList.remove('open');m.firstElementChild.setAttribute('aria-expanded','false')})}
$$('.menu>button').forEach(b=>{
 b.addEventListener('click',e=>{e.stopPropagation();const m=b.parentElement,was=m.classList.contains('open');closeMenus();if(!was){m.classList.add('open');b.setAttribute('aria-expanded','true');const f=$('a',m);f&&f.focus()}});
 b.addEventListener('mouseenter',()=>{if($('.menu.open')&&!b.parentElement.classList.contains('open'))b.click()});
});
document.addEventListener('click',e=>{if(!e.target.closest('.menu'))closeMenus()});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeMenus();closeSheet()}});
/* windows */
let z=10,n=0;const wins=$('#wins'),open={};
function openWin(id){
 if(!C[id])return;if(open[id]){open[id].classList.remove('min');front(open[id]);return}
 const d=C[id],w=document.createElement('section');w.className='win';w.dataset.id=id;w.setAttribute('role','dialog');w.setAttribute('aria-label',d.t);
 const W=innerWidth,H=innerHeight,ww=Math.min(d.w||420,W-40),hh=Math.min(d.h||300,H-150);
 w.style.width=ww+'px';w.style.height=hh+'px';
 w.style.left=Math.max(12,Math.round((W-ww)/2-160+(n%5)*70))+'px';w.style.top=Math.max(36,Math.round((H-hh)/2-70+(n%5)*40))+'px';n++;
 w.innerHTML=`<div class="tb"><div class="lights"><button class="c" aria-label="Close"></button><button class="m" aria-label="Minimize"></button><button class="z" aria-label="Zoom"></button></div><h2>${d.t}</h2></div><div class="body ${d.cls||''}" tabindex="0">${d.html}</div>`;
 wins.appendChild(w);open[id]=w;front(w);mark();
 $('.c',w).onclick=()=>{w.remove();delete open[id];mark()};
 $('.m',w).onclick=()=>{w.classList.add('min');mark()};
 $('.z',w).onclick=()=>w.classList.toggle('zoomed');
 w.addEventListener('pointerdown',()=>front(w));
 drag(w,$('.tb',w));
 if(id==='installer')requestAnimationFrame(()=>{const p=$('.prog i',w);p&&(p.style.width='100%')});
 $('.c',w).focus({preventScroll:true});
}
function front(w){w.style.zIndex=++z}
function mark(){$$('.dock .dk').forEach(b=>b.classList.toggle('open',!!open[b.dataset.win]))}
function drag(w,h){h.addEventListener('pointerdown',e=>{if(e.target.closest('.lights'))return;if(w.classList.contains('zoomed'))return;
 const sx=e.clientX-w.offsetLeft,sy=e.clientY-w.offsetTop;h.setPointerCapture(e.pointerId);
 const mv=ev=>{w.style.left=Math.min(innerWidth-80,Math.max(-w.offsetWidth+80,ev.clientX-sx))+'px';w.style.top=Math.min(innerHeight-60,Math.max(26,ev.clientY-sy))+'px'};
 const up=()=>{h.removeEventListener('pointermove',mv);h.removeEventListener('pointerup',up)};
 h.addEventListener('pointermove',mv);h.addEventListener('pointerup',up)})}
/* desktop icons: single = select, double / Enter = open */
document.addEventListener('click',e=>{const i=e.target.closest('.dicon');$$('.dicon.sel').forEach(x=>x!==i&&x.classList.remove('sel'));if(i){i.classList.add('sel');i.setAttribute('aria-selected','true')}});
document.addEventListener('dblclick',e=>{const i=e.target.closest('.dicon');if(i)openWin(i.dataset.win)});
document.addEventListener('keydown',e=>{const i=e.target.closest&&e.target.closest('.dicon');if(i&&(e.key==='Enter'||e.key===' ')){e.preventDefault();openWin(i.dataset.win)}});
/* dock */
$$('.dock [data-win]').forEach(b=>b.addEventListener('click',e=>{if(b.classList.contains('bubble')||b.classList.contains('sp')){e.preventDefault();$('.bubble').classList.add('gone')}openWin(b.dataset.win)}));
/* phone sheets */
const sheet=$('#sheet');let last=null;
function openSheet(id){const d=C[id];if(!d)return;last=document.activeElement;$('#sheet-t').textContent=id==='mac'?'SiliconPlay':d.t.replace(/\.(md|txt|png|app)$/,'').replace(' — zsh','').replace(/^./,c=>c.toUpperCase());const b=$('.sbody',sheet);b.className='sbody '+(d.cls||'');b.innerHTML=d.html;sheet.hidden=false;$('.sclose',sheet).focus()}
function closeSheet(){if(sheet.hidden)return;sheet.hidden=true;last&&last.focus()}
$$('#phone [data-sheet]').forEach(b=>b.addEventListener('click',()=>openSheet(b.dataset.sheet)));
$('.sclose').onclick=closeSheet;
let sy0=null;sheet.addEventListener('touchstart',e=>{if($('.sbody',sheet).scrollTop<=0)sy0=e.touches[0].clientY},{passive:true});
sheet.addEventListener('touchend',e=>{if(sy0!==null&&e.changedTouches[0].clientY-sy0>90)closeSheet();sy0=null});
/* intro */
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;let attnT=null,attnOn=!RM;
function bounce(el,n,h){if(!el||RM)return;const k=[];const d=520;for(let i=0;i<n;i++){const hh=h*Math.pow(.8,i);k.push({transform:'translateY(0)',offset:i/n,easing:'cubic-bezier(.2,.7,.35,1)'},{transform:`translateY(${-hh}px)`,offset:(i+.5)/n,easing:'cubic-bezier(.6,0,.85,.4)'})}k.push({transform:'translateY(0)',offset:1});return el.animate(k,{duration:d*n})}
function attention(){const ic=$('.dock .sp');if(!attnOn||!ic)return;bounce(ic,3,26);attnT=setInterval(()=>attnOn&&bounce(ic,1,16),12000);bounce($('#phone .grid .app[data-sheet=mac] img'),1,8)}
function stopAttn(){attnOn=false;clearInterval(attnT)}
document.addEventListener('click',e=>{if(e.target.closest('.dock .sp,.bubble'))stopAttn()},true);
const intro=$('#intro');const end=()=>{intro.classList.add('done');setTimeout(()=>{intro.remove();attention()},600)};
if(matchMedia('(prefers-reduced-motion: reduce)').matches||sessionStorage.getItem('sp-intro')){intro.remove();setTimeout(attention,300)}else{sessionStorage.setItem('sp-intro','1');intro.onclick=end;setTimeout(end,1500)}
window.SP={attention,stopAttn,openWin,openSheet};
})();
document.querySelectorAll('[data-mail]').forEach(a=>a.href='mailto:'+CONTACT_EMAIL);
