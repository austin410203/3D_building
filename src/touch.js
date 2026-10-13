// Mobile touch controls: left virtual joystick (analog move / steer), right-side drag to look,
// context buttons (foot: RUN / JUMP / 上車, car: 油門 / 煞車 / 手煞車 / 換檔 / 下車) + small N / V / M / H buttons.
export const isTouch = () => /[?&]touch=1/.test(location.search) || ((("ontouchstart" in window) || navigator.maxTouchPoints > 0) && matchMedia("(pointer: coarse)").matches);

export class TouchControls {
  constructor(input) {
    this.input = input; this.mode = "foot"; this.runLatch = false;
    input.axis = { x: 0, y: 0, mag: 0, active: false };
    const root = this.root = document.createElement("div"); root.id = "touch"; root.className = "hidden";
    root.innerHTML = `
      <div id="tlook"></div>
      <div id="tstick"><div id="tknob"></div></div>
      <div id="tbtns-foot" class="tbtns">
        <button data-hold="Space" class="tb big">跳</button>
        <button data-toggle="run" class="tb">跑</button>
        <button data-tap="KeyF" class="tb accent" id="tbF">上車</button>
      </div>
      <div id="tbtns-car" class="hidden">
        <button data-tap="KeyQ" class="tb sm" style="grid-area:dn">檔−</button>
        <button data-tap="KeyE" class="tb sm" style="grid-area:up">檔+</button>
        <button data-hold="Space" class="tb sm" style="grid-area:hb">手煞</button>
        <button data-tap="KeyF" class="tb accent sm" style="grid-area:ex">下車</button>
        <button data-hold="KeyS" class="tb brake" style="grid-area:br">煞車</button>
        <button data-hold="KeyW" class="tb gas" style="grid-area:gas">油門</button>
      </div>
      <div id="tmisc">
        <button data-tap="KeyM" class="tb xs" id="tbM">自/手排</button>
        <button data-tap="KeyV" class="tb xs">視角</button>
        <button data-tap="KeyN" class="tb xs">日/夜</button>
        <button data-tap="KeyR" class="tb xs">重置車</button>
      </div>`;
    document.body.appendChild(root);
    this.stick = root.querySelector("#tstick"); this.knob = root.querySelector("#tknob");
    this.stickId = null; this.lookIds = new Map();
    // ---- joystick (floating: appears where the left thumb lands)
    const zoneL = e => e.clientX < innerWidth * 0.42 && e.clientY > innerHeight * 0.3;
    const onStart = e => {
      for (const t of e.changedTouches) {
        if (t.target.closest && t.target.closest(".tb")) continue;
        if (this.stickId === null && zoneL(t)) {
          this.stickId = t.identifier; this.ox = t.clientX; this.oy = t.clientY;
          this.stick.style.left = (t.clientX - 70) + "px"; this.stick.style.top = (t.clientY - 70) + "px"; this.stick.classList.add("on");
          this.setAxis(0, 0);
        } else {
          this.lookIds.set(t.identifier, [t.clientX, t.clientY]);
        }
      }
    };
    const onMove = e => {
      for (const t of e.changedTouches) {
        if (t.identifier === this.stickId) {
          let dx = t.clientX - this.ox, dy = t.clientY - this.oy; const L = Math.hypot(dx, dy), R = 60;
          if (L > R) { dx *= R / L; dy *= R / L; }
          this.knob.style.transform = `translate(${dx}px, ${dy}px)`;
          this.setAxis(dx / R, dy / R);
        } else if (this.lookIds.has(t.identifier)) {
          const [px, py] = this.lookIds.get(t.identifier);
          input.mdx += (t.clientX - px) * 1.8; input.mdy += (t.clientY - py) * 1.4;
          this.lookIds.set(t.identifier, [t.clientX, t.clientY]);
        }
      }
      e.preventDefault();
    };
    const onEnd = e => {
      for (const t of e.changedTouches) {
        if (t.identifier === this.stickId) {
          this.stickId = null; this.knob.style.transform = ""; this.stick.classList.remove("on"); this.setAxis(0, 0);
        }
        this.lookIds.delete(t.identifier);
      }
    };
    root.addEventListener("touchstart", onStart, { passive: false });
    root.addEventListener("touchmove", onMove, { passive: false });
    root.addEventListener("touchend", onEnd); root.addEventListener("touchcancel", onEnd);
    // ---- buttons
    for (const b of root.querySelectorAll(".tb")) {
      const hold = b.dataset.hold, tap = b.dataset.tap, tog = b.dataset.toggle;
      b.addEventListener("touchstart", e => {
        e.preventDefault(); e.stopPropagation(); b.classList.add("down");
        if (hold) { if (!input.down.has(hold)) input.just.add(hold); input.down.add(hold); }
        if (tap) { input.just.add(tap); }
        if (tog === "run") { this.runLatch = !this.runLatch; b.classList.toggle("latched", this.runLatch); this.applyRun(); }
      }, { passive: false });
      const up = e => { e.preventDefault(); b.classList.remove("down"); if (hold) input.down.delete(hold); };
      b.addEventListener("touchend", up); b.addEventListener("touchcancel", up);
    }
  }
  setAxis(x, y) {
    const a = this.input.axis; a.x = x; a.y = y; a.mag = Math.min(1, Math.hypot(x, y)); a.active = a.mag > 0.08;
    this.applyRun();
  }
  applyRun() {
    // pushing the stick to the rim also runs
    const run = this.runLatch || this.input.axis.mag > 0.92;
    if (run) this.input.down.add("TouchRun"); else this.input.down.delete("TouchRun");
  }
  show() { this.root.classList.remove("hidden"); }
  setMode(m) {
    this.mode = m;
    this.root.querySelector("#tbtns-foot").classList.toggle("hidden", m !== "foot");
    this.root.querySelector("#tbtns-car").classList.toggle("hidden", m === "foot");
  }
  setNearCar(near) { this.root.querySelector("#tbF").classList.toggle("dim", !near); }
}
