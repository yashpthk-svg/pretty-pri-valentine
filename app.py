from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">

<style>
:root{
  --pink1:#ffd1df;
  --pink2:#ffe6ef;
  --light-red:#ff5a86;
}

/* ---------- SCENE 0 OVERLAY ---------- */
.blackScreen{
  position:fixed;
  inset:0;
  background:#000;
  display:none;              /* shown via JS */
  place-items:center;
  z-index:9999;
}
.blackScreen.on{ display:grid; }
.blackText{
  text-align:center;
}
.blackText h1{
  font-size:48px;
  color:var(--light-red);
  margin:0;
  font-family:'Pacifico', cursive;
}
.blackText p{
  font-family:system-ui,Arial;
  font-size:14px;
  opacity:.7;
  margin-top:14px;
  color:#fff;
}

/* ---------- EXISTING STYLES ---------- */
body{
  margin:0;
  min-height:100vh;
  overflow:hidden;
  font-family:'Pacifico', cursive;
  background: radial-gradient(1200px 700px at 30% 20%, var(--pink2), var(--pink1));
}

/* BACKGROUND PHOTOS LAYER */
.bg{
  position:fixed;
  inset:0;
  pointer-events:none;
  opacity:1;
  z-index:0;
}

/* Polaroid base */
.pol{
  position:absolute;
  width:150px;
  background:#fff;
  padding:10px 10px 18px;
  border-radius:7px;
  box-shadow:0 16px 30px rgba(0,0,0,.35);
  opacity:0;
  transform: translateY(140px) rotate(var(--r));
}

/* montage enter */
.pol.enter{
  animation: rollIn 900ms cubic-bezier(.2,.9,.2,1) forwards;
  animation-delay: var(--delay);
}

/* drift after enter */
.pol.drift{
  opacity:.96;
  animation: drift 12s ease-in-out infinite;
  animation-delay: 0s;
}

.pol img{ width:100%; border-radius:5px; }

@keyframes rollIn{
  0%   { opacity:0; transform: translateY(160px) rotate(var(--r)); }
  70%  { opacity:.96; transform: translateY(-10px) rotate(var(--r)); }
  100% { opacity:.96; transform: translateY(0px) rotate(var(--r)); }
}

@keyframes drift{
  0%   { transform:translate(0,0) rotate(var(--r)); }
  50%  { transform:translate(var(--dx),var(--dy)) rotate(var(--r)); }
  100% { transform:translate(0,0) rotate(var(--r)); }
}

/* MAIN */
.wrap{
  min-height:100vh;
  display:grid;
  place-items:center;
  padding:20px;
  position:relative;
  z-index:2;
}

.card{
  width:min(900px,96vw);
  background:rgba(255,255,255,.35);
  border-radius:20px;
  padding:28px 24px;
  text-align:center;
  box-shadow:0 30px 80px rgba(0,0,0,.25);
}

.main{
  font-size:30px;
  line-height:1.4;
  color:var(--light-red);
  min-height:120px;
}

.textBackdrop{
  background: rgba(255, 245, 248, 0.65);
  backdrop-filter: blur(6px);
  border-radius: 16px;
  padding: 18px 20px;
}

.line{
  opacity:0;
  transform:translateY(12px);
  transition:opacity 1s ease, transform 1s ease;
  margin:10px 0;
}
.line.show{
  opacity:1;
  transform:translateY(0);
}

.small{
  font-family:system-ui,Arial;
  font-size:15px;
  opacity:.75;
  margin-bottom:14px;
}

/* Counters block */
.counterWrap{
  margin: 14px auto 8px;
  width: min(720px, 92vw);
  display: none;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
}

.pill{
  font-family:system-ui,Arial;
  font-size:15px;
  background: rgba(255,255,255,.45);
  border:1px solid rgba(255,255,255,.6);
  border-radius: 999px;
  padding: 10px 14px;
  box-shadow: 0 8px 18px rgba(0,0,0,.15);
  color: rgba(0,0,0,.75);
}
.pill b{
  color:#111;
  font-weight: 700;
}
.subnote{
  font-family:system-ui,Arial;
  font-size:13px;
  opacity:.75;
  margin-top:6px;
}

/* CHOICES ARENA */
.choices{
  position:relative;
  width:min(720px,92vw);
  height:180px;
  margin:24px auto 0;
  display:none;
}

/* Scene 1 layout (runaway) */
.choices.scene1 #opt1{
  position:absolute;
  left:16px;
  top:50%;
  transform:translateY(-50%);
  width:min(340px,44vw);
}
.choices.scene1 #opt2{
  position:absolute;
  left:60%;
  top:55%;
  width:min(240px,36vw);
  z-index:10;
}

/* Final layout (no gimmicks) */
.choices.final{
  height:auto;
  display:flex;
  gap:16px;
  justify-content:center;
  flex-wrap:wrap;
}
.choices.final #opt1,
.choices.final #opt2{
  position:static !important;
  transform:none !important;
  width:min(240px, 42vw);
}

.btn{
  font-family:system-ui,Arial;
  padding:14px 18px;
  border-radius:14px;
  border:1px solid rgba(255,255,255,.6);
  background:rgba(255,255,255,.45);
  cursor:pointer;
  color:#444;
  font-size:16px;
  box-shadow:0 10px 25px rgba(0,0,0,.2);
}

/* HINT */
.hint{
  font-family:system-ui,Arial;
  font-size:14px;
  opacity:.6;
  margin-top:16px;
}

/* MODAL */
.modal{
  position:fixed;
  inset:0;
  display:none;
  place-items:center;
  background:rgba(0,0,0,.5);
  z-index:5;
  padding:18px;
}
.modal.on{ display:grid; }

.modalCard{
  background:rgba(255,255,255,.92);
  padding:28px;
  border-radius:20px;
  width:min(680px,92vw);
  text-align:center;
}
.modalCard p{
  font-size:28px;
  color:var(--light-red);
  white-space: pre-line;
}
</style>
</head>

<body>

<!-- SCENE 0 -->
<div class="blackScreen" id="scene0">
  <div class="blackText">
    <h1>Hi Bubuuu!</h1>
    <p>Tap to advance</p>
  </div>
</div>

<div class="bg" id="bg"></div>

<div class="wrap" id="tap">
  <div class="card">
    <div class="small" id="small"></div>

    <div class="counterWrap" id="counterWrap">
      <div class="pill">Times I’ve hurt you: <b id="hurtNum">0</b></div>
      <div class="pill">
        Times I’ve loved you: <b id="loveNum">0</b>
        <div class="subnote" id="loveSub" style="display:none;">
          maybe not in the way you want but in all the ways I can love, and more.
        </div>
      </div>
    </div>

    <div class="main textBackdrop" id="main"></div>

    <div class="choices scene1" id="choices">
      <button class="btn" id="opt1"></button>
      <button class="btn" id="opt2"></button>
    </div>

    <div class="hint" id="hint">Tap to advance</div>
  </div>
</div>

<div class="modal" id="modal">
  <div class="modalCard">
    <p id="modalMsg"></p>
  </div>
</div>

<script>
/* ---------- PHOTOS (ONLY ENTER IN SCENE 3) ---------- */
const bg = document.getElementById('bg');
const photos = [...Array(10)].map((_,i)=>`/static/ph${i+1}.jpeg`);
let photosBuilt = false;

function buildPhotosHidden(){
  if(photosBuilt) return;
  photosBuilt = true;
  bg.innerHTML = "";

  const anchors=[
    {x:10,y:10},{x:28,y:14},{x:46,y:10},{x:64,y:14},{x:82,y:10},
    {x:14,y:44},{x:32,y:48},{x:50,y:44},{x:68,y:48},{x:46,y:74},
  ];

  photos.forEach((src,i)=>{
    const d=document.createElement('div');
    d.className='pol';

    const a=anchors[i] || {x:10+(i%5)*18,y:12+Math.floor(i/5)*32};
    d.style.left=a.x+'%';
    d.style.top=a.y+'%';

    d.style.setProperty('--dx',(Math.random()*18-9)+'px');
    d.style.setProperty('--dy',(Math.random()*18-9)+'px');
    d.style.setProperty('--r',(Math.random()*16-8)+'deg');
    d.style.setProperty('--delay', (i * 90) + "ms");

    const img=document.createElement('img');
    img.src=src;
    d.appendChild(img);
    bg.appendChild(d);
  });
}

function rollInMontage(){
  buildPhotosHidden();
  const all = [...document.querySelectorAll('.pol')];
  all.forEach(el=>{
    el.classList.remove('drift');
    el.classList.add('enter');
  });

  setTimeout(()=>{
    all.forEach(el=>{
      el.classList.remove('enter');
      el.classList.add('drift');
    });
  }, 1300);
}

/* ---------- UI ---------- */
const main=document.getElementById('main');
const small=document.getElementById('small');
const choices=document.getElementById('choices');
const hint=document.getElementById('hint');

const counterWrap=document.getElementById('counterWrap');
const hurtNum=document.getElementById('hurtNum');
const loveNum=document.getElementById('loveNum');
const loveSub=document.getElementById('loveSub');

function clearMain(){ main.innerHTML=''; }
function addLine(t){
  const d=document.createElement('div');
  d.className='line';
  d.textContent=t;
  main.appendChild(d);
  requestAnimationFrame(()=>d.classList.add('show'));
}
async function lines(arr, delay=1500){
  clearMain();
  for(const l of arr){
    addLine(l);
    await new Promise(r=>setTimeout(r,delay));
  }
}

/* ---------- COUNTERS ---------- */
function animateCounter(el, from, to, ms, finalText){
  const start = performance.now();
  function step(t){
    const p = Math.min((t-start)/ms, 1);
    const v = Math.floor(from + (to-from) * p);
    el.textContent = v.toLocaleString();
    if(p < 1) requestAnimationFrame(step);
    else el.textContent = finalText;
  }
  requestAnimationFrame(step);
}

/* ---------- MODAL ---------- */
const modal=document.getElementById('modal');
const modalMsg=document.getElementById('modalMsg');
function showMsg(t){
  modalMsg.textContent=t;
  modal.classList.add('on');
}
modal.onclick=()=>modal.classList.remove('on');

/* ---------- RUNAWAY (SCENE 1 ONLY) ---------- */
const opt1=document.getElementById('opt1');
const opt2=document.getElementById('opt2');

function runAwayFar(){
  const box=choices.getBoundingClientRect();
  const r1=opt1.getBoundingClientRect();

  const maxX=box.width-opt2.offsetWidth-12;
  const maxY=box.height-opt2.offsetHeight-12;

  const minDist = 240;

  let tries=0;
  while(tries++ < 160){
    const x=12+Math.random()*maxX;
    const y=12+Math.random()*maxY;

    const vx = box.left + x;
    const vy = box.top + y;

    const dx = vx - r1.left;
    const dy = vy - r1.top;

    if(Math.hypot(dx,dy) > minDist){
      opt2.style.left=x+'px';
      opt2.style.top=y+'px';
      return;
    }
  }
  opt2.style.left=(box.width*0.65)+'px';
  opt2.style.top=(box.height*0.20)+'px';
}

function enableRunaway(on){
  if(on){
    choices.classList.remove('final');
    choices.classList.add('scene1');

    opt2.style.position="absolute";
    opt2.style.transform="none";
    runAwayFar();

    opt2.onmouseenter=runAwayFar;
    opt2.onmousedown=e=>{e.preventDefault();runAwayFar();};
    opt2.ontouchstart=e=>{e.preventDefault();runAwayFar();};
    opt2.onclick=e=>{e.preventDefault();runAwayFar();};
  }else{
    opt2.onmouseenter=null;
    opt2.onmousedown=null;
    opt2.ontouchstart=null;
    opt2.onclick=null;
  }
}

/* ---------- SCENES ---------- */
let scene = 0;
const scene0 = document.getElementById("scene0");

function hideChoices(){ choices.style.display='none'; }
function hideCounters(){ counterWrap.style.display='none'; }
function showCounters(){ counterWrap.style.display='flex'; }

function showChoices(mode){
  choices.style.display='block';
  if(mode === "final"){
    choices.classList.remove('scene1');
    choices.classList.add('final');
    enableRunaway(false);
  }else{
    choices.classList.remove('final');
    choices.classList.add('scene1');
    enableRunaway(true);
  }
}

function scene0Run(){
  scene = 0;
  scene0.classList.add("on");
  hint.textContent = "Tap to advance";
}

async function scene1Run(){
  scene = 1;
  // IMPORTANT: not changing anything inside scene 1 behavior
  small.textContent='';
  hideCounters();
  hideChoices();
  hint.textContent="Tap to advance";

  await lines([
    "I’m sorry and I know there’s nothing I can do about what I’ve wronged, but a man should try everything in his power to love a boss baby like you."
  ], 1400);

  opt1.textContent="Let’s see what Yashi has to say";
  opt2.textContent="Not interested";
  showChoices("scene1");
}

async function scene2Run(){
  scene = 2;
  hideChoices();
  small.textContent="Haha I bet you didn’t even try to click on the other option, if you did, at least here I’m not giving you an option.";
  hint.textContent="Tap to advance";

  showCounters();
  loveSub.style.display="none";
  hurtNum.textContent="0";
  loveNum.textContent="0";

  animateCounter(hurtNum, 0, 950000, 2800, "Million+");
  setTimeout(()=> animateCounter(loveNum, 0, 950000000, 3400, "Billion+"), 1200);
  setTimeout(()=> { loveSub.style.display="block"; }, 1200 + 3400 + 250);

  await lines([
    "Here’s me trying a new way, a nerdy way. 😉"
  ], 1800);

  // no photos in scene 2
}

async function scene3Run(){
  scene = 3;
  hideChoices();
  hideCounters();
  small.textContent='';
  hint.textContent="Tap to advance";

  await lines([
    "We have come a long way, here’s a very short glimpse of our highs",
    "From priority waste, to my priority, to me being waste; you have always stood there patiently, loving me, tolerating me.",
    "I thank every god there is and there was that I am lucky enough to have you."
  ], 1600);

  // photos roll-in after scene 3 text
  rollInMontage();
}

async function scene4Run(){
  scene = 4;
  hideChoices();
  hideCounters();
  small.textContent='';
  hint.textContent="Tap to advance";

  await lines([
    "I have asked you a million of questions, my personal ChatGPT.",
    "But, I should have asked this a year ago, or for the matter of fact every morning that I wake up."
  ], 1600);
}

async function scene5Run(){
  scene = 5;
  hideCounters();
  small.textContent='';
  hint.textContent="Tap buttons";

  await lines([
    "My Parekh, will you be my valentine and give me a chance to love you the way I do?"
  ], 1500);

  opt1.textContent="Yes 💖";
  opt2.textContent="No 💔";
  showChoices("final");

  const existing = document.getElementById("noWrap");
  if(!existing){
    const noWrap = document.createElement("div");
    noWrap.id="noWrap";
    noWrap.style.display="flex";
    noWrap.style.flexDirection="column";
    noWrap.style.alignItems="center";

    const note = document.createElement("div");
    note.textContent="No gimmicks";
    note.style.fontFamily="system-ui, Arial";
    note.style.fontSize="12px";
    note.style.fontWeight="700";
    note.style.opacity="0.8";
    note.style.marginTop="6px";
    note.style.textAlign="center";

    choices.innerHTML="";
    choices.appendChild(opt1);
    noWrap.appendChild(opt2);
    noWrap.appendChild(note);
    choices.appendChild(noWrap);
  }

  opt1.onclick = ()=>{ if(scene===5) showMsg("🥹 I love you from Nagar to Ghatkopar and back."); };
  opt2.onclick = ()=>{ if(scene===5) showMsg(
    "I will keep trying, keep loving you. (Till death do us apart)\n" +
    "If this made a smile at any moment, just drop a “.” And I’ll understand."
  );};
}

async function scene6Run(){
  scene = 6;
  hideChoices();
  hideCounters();
  small.textContent='';
  hint.textContent="";

  await lines([
    "The End",
    "Thank you baby"
  ], 1600);
}

/* ---------- BUTTON EVENTS ---------- */
opt1.onclick = ()=>{ if(scene===1) scene2Run(); };
opt2.onclick = (e)=>{ if(scene===1){ e.preventDefault(); runAwayFar(); } };

/* ---------- SCENE 0 CLICK (THIS FIXES YOUR ISSUE) ---------- */
scene0.addEventListener("click", ()=>{
  if(scene !== 0) return;
  scene0.classList.remove("on");
  scene1Run();
});
scene0.addEventListener("touchstart", ()=>{
  if(scene !== 0) return;
  scene0.classList.remove("on");
  scene1Run();
}, {passive:true});

/* ---------- TAP TO ADVANCE (NO AUTO TIMERS) ---------- */
document.getElementById('tap').onclick = (e)=>{
  if(e.target.tagName === "BUTTON") return;
  if(modal.classList.contains("on")) return;

  if(scene === 2) scene3Run();
  else if(scene === 3) scene4Run();
  else if(scene === 4) scene5Run();
  else if(scene === 5) scene6Run();   // tap anywhere (not buttons) goes to The End
};

/* ---------- START ---------- */
scene0Run();
</script>
</body>
</html>
"""

if __name__=="__main__":
    app.run(port=5050, debug=True)
