// God view: free orbit/pan camera over the island, hover + click buildings, info card, searchable building list, fly-to.
import * as THREE from "three";
import { B2T } from "./world.js";

const $ = id => document.getElementById(id);

export class GodView {
  constructor(world, camera, canvas, input, onGo) {
    this.world = world; this.camera = camera; this.canvas = canvas; this.input = input; this.onGo = onGo;
    this.active = false;
    this.target = new THREE.Vector3(0, 0, 0); this.yaw = 0.6; this.pitch = 0.95; this.dist = 320;
    this.fly = null; this.sel = null; this.hover = null;
    this.ray = new THREE.Raycaster(); this.mouse = new THREE.Vector2(); this.lastHover = 0;
    this.box = new THREE.Box3Helper(new THREE.Box3(), 0xffd34d); this.box.visible = false; world.scene.add(this.box);
    this.drag = null; this.touches = new Map();
    this.buildUI();
    const c = canvas;
    c.addEventListener("contextmenu", e => { if (this.active) e.preventDefault(); });
    c.addEventListener("mousedown", e => {
      if (!this.active) return;
      if (document.pointerLockElement) document.exitPointerLock();
      e.preventDefault();
      this.drag = { b: (e.button === 0 && (e.shiftKey || e.ctrlKey || e.altKey)) ? 2 : e.button, moved: 0 };
      this.canvas.style.cursor = this.drag.b === 0 ? "grabbing" : "move";
    });
    c.addEventListener("dblclick", e => {
      if (!this.active) return;
      const p = this.groundPoint(e.clientX, e.clientY);
      if (p) this.fly = { from: this.target.clone(), to: p, d0: this.dist, d1: Math.max(40, this.dist * 0.6), t: 0 };
    });
    addEventListener("mouseup", e => {
      if (!this.active || !this.drag) return;
      if (this.drag.moved < 5 && this.drag.b === 0) this.pick(e.clientX, e.clientY, true);
      this.drag = null; this.canvas.style.cursor = "grab";
    });
    addEventListener("mousemove", e => {
      if (!this.active) return;
      if (this.drag) {
        const dx = e.movementX || 0, dy = e.movementY || 0;
        this.drag.moved += Math.abs(dx) + Math.abs(dy);
        if (this.drag.b === 0) this.pan(-dx, -dy);
        else { this.yaw -= dx * 0.005; this.pitch = THREE.MathUtils.clamp(this.pitch + dy * 0.004, 0.2, 1.54); this.fly = null; }
      } else if (performance.now() - this.lastHover > 80) { this.lastHover = performance.now(); this.pick(e.clientX, e.clientY, false); }
    });
    c.addEventListener("wheel", e => {
      if (!this.active) return;
      // zoom towards the point under the cursor
      const before = this.dist, after = THREE.MathUtils.clamp(this.dist * (e.deltaY > 0 ? 1.12 : 0.89), 15, 1400);
      const p = this.groundPoint(e.clientX, e.clientY);
      if (p && after < before) this.target.lerp(p, 1 - after / before);
      this.dist = after; this.fly = null;
    }, { passive: true });
    // touch: 1 finger pan, 2 fingers pinch-zoom + twist, tap = pick
    c.addEventListener("touchstart", e => {
      if (!this.active) return;
      for (const t of e.changedTouches) this.touches.set(t.identifier, { x: t.clientX, y: t.clientY, x0: t.clientX, y0: t.clientY, t0: performance.now() });
      e.preventDefault();
    }, { passive: false });
    c.addEventListener("touchmove", e => {
      if (!this.active) return;
      const prev = new Map([...this.touches].map(([k, v]) => [k, { ...v }]));
      for (const t of e.changedTouches) { const s = this.touches.get(t.identifier); if (s) { s.x = t.clientX; s.y = t.clientY; } }
      const ids = [...this.touches.keys()];
      if (ids.length === 1) { const a = this.touches.get(ids[0]), p = prev.get(ids[0]); this.pan(-(a.x - p.x), -(a.y - p.y)); }
      else if (ids.length >= 2) {
        const a = this.touches.get(ids[0]), b = this.touches.get(ids[1]), pa = prev.get(ids[0]), pb = prev.get(ids[1]);
        const d1 = Math.hypot(pa.x - pb.x, pa.y - pb.y), d2 = Math.hypot(a.x - b.x, a.y - b.y);
        if (d1 > 0 && d2 > 0) this.dist = THREE.MathUtils.clamp(this.dist * d1 / d2, 15, 1400);
        const a1 = Math.atan2(pb.y - pa.y, pb.x - pa.x), a2 = Math.atan2(b.y - a.y, b.x - a.x);
        this.yaw += (a2 - a1);
        const my1 = (pa.y + pb.y) / 2, my2 = (a.y + b.y) / 2; this.pitch = THREE.MathUtils.clamp(this.pitch + (my2 - my1) * 0.004, 0.25, 1.52);
      }
      e.preventDefault();
    }, { passive: false });
    c.addEventListener("touchend", e => {
      if (!this.active) return;
      for (const t of e.changedTouches) {
        const s = this.touches.get(t.identifier);
        if (s && Math.hypot(s.x - s.x0, s.y - s.y0) < 10 && performance.now() - s.t0 < 350 && this.touches.size === 1) this.pick(t.clientX, t.clientY, true);
        this.touches.delete(t.identifier);
      }
    });
  }

  buildUI() {
    const wrap = document.createElement("div"); wrap.id = "god"; wrap.className = "hidden";
    wrap.innerHTML = `
      <div id="godbar">🌐 上帝視角 · <span class="desk">左鍵拖曳平移 · 右鍵(或Shift+左鍵)拖曳旋轉視角 · 滾輪縮放 · 雙擊飛到該處 · WASD/QE ·</span><span class="mob">單指平移 · 雙指縮放旋轉 ·</span> 點建築看資訊 · <b>G</b> 返回</div>
      <div id="godlist"><input id="godq" placeholder="搜尋 167 棟建築 / 風格…"><div id="goditems"></div></div>
      <div id="godcard" class="hidden">
        <div id="gc-name"></div><div id="gc-en"></div><div id="gc-style"></div><div id="gc-desc"></div><div id="gc-meta"></div>
        <div class="gc-btns"><button id="gc-walk">🚶 走過去</button><button id="gc-drive">🚗 開車過去</button><button id="gc-close">✕</button></div>
      </div>
      <div id="godtip" class="hidden"></div>`;
    document.body.appendChild(wrap);
    this.ui = wrap;
    $("godq").addEventListener("input", () => this.renderList());
    $("godq").addEventListener("keydown", e => e.stopPropagation());
    $("gc-close").onclick = () => this.select(null);
    $("gc-walk").onclick = () => this.sel && this.onGo(this.sel, "foot");
    $("gc-drive").onclick = () => this.sel && this.onGo(this.sel, "car");
    for (const ev of ["mousedown", "touchstart", "wheel"]) wrap.querySelectorAll("#godlist,#godcard").forEach(el => el.addEventListener(ev, e => e.stopPropagation(), { passive: true }));
  }
  renderList() {
    const q = ($("godq").value || "").trim().toLowerCase();
    const items = this.world.buildings.filter(b => !q || `${b.name_zh} ${b.name_en} ${b.style} ${b.style_zh} ${b.tier} ${b.id}`.toLowerCase().includes(q))
      .sort((a, b) => a.name_en.localeCompare(b.name_en));
    $("goditems").innerHTML = items.map(b => `<div class="gi" data-id="${b.id}"><b>${b.name_zh}</b> <span>${b.name_en}</span><i>${b.style_zh} · ${b.tier}</i></div>`).join("")
      || "<div class='gi'>沒有符合的建築</div>";
    for (const el of $("goditems").querySelectorAll(".gi[data-id]")) el.onclick = () => { const b = this.world.buildings.find(x => x.id === el.dataset.id); this.select(b, true); };
  }

  enter(from) {
    this.active = true; this.ui.classList.remove("hidden");
    if (document.pointerLockElement) document.exitPointerLock();
    this.target.copy(from); this.target.y = 0; this.dist = 140; this.pitch = 0.9; this.canvas.style.cursor = "grab";
    this.renderList();
  }
  exit() { this.active = false; this.ui.classList.add("hidden"); this.select(null); $("godtip").classList.add("hidden"); this.canvas.style.cursor = ""; this.drag = null; }

  pan(dx, dy) {
    const s = this.dist * 0.0018;
    const f = new THREE.Vector3(-Math.sin(this.yaw), 0, -Math.cos(this.yaw)), r = new THREE.Vector3(-f.z, 0, f.x);
    this.target.addScaledVector(r, dx * s).addScaledVector(f, -dy * s);
    this.fly = null;
  }

  groundPoint(cx, cy) {
    this.mouse.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1);
    this.ray.setFromCamera(this.mouse, this.camera);
    const p = new THREE.Vector3();
    return this.ray.ray.intersectPlane(new THREE.Plane(new THREE.Vector3(0, 1, 0), 0), p) ? p : null;
  }
  pickBuilding(cx, cy) {
    this.mouse.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1);
    this.ray.setFromCamera(this.mouse, this.camera);
    let best = null, bd = Infinity; const hit = new THREE.Vector3();
    for (const b of this.world.buildings) {
      if (!b.box) b.box = new THREE.Box3().setFromObject(b.shell);
      if (this.ray.ray.intersectBox(b.box, hit)) { const d = hit.distanceTo(this.ray.ray.origin); if (d < bd) { bd = d; best = b; } }
    }
    return best;
  }
  pick(cx, cy, click) {
    const b = this.pickBuilding(cx, cy);
    const tip = $("godtip");
    if (!click) {
      this.hover = b;
      if (b) { tip.textContent = `${b.name_zh}  ${b.name_en}`; tip.style.left = (cx + 14) + "px"; tip.style.top = (cy + 10) + "px"; tip.classList.remove("hidden"); }
      else tip.classList.add("hidden");
      this.canvas.style.cursor = b ? "pointer" : "grab";
      return;
    }
    this.select(b, false);
  }
  select(b, flyTo) {
    this.sel = b;
    if (!b) { $("godcard").classList.add("hidden"); this.box.visible = false; return; }
    if (!b.box) b.box = new THREE.Box3().setFromObject(b.shell);
    this.box.box.copy(b.box); this.box.visible = true;
    $("gc-name").textContent = b.name_zh; $("gc-en").textContent = b.name_en;
    $("gc-style").textContent = `${b.style_zh} · ${b.style} · ${b.tier}`;
    $("gc-desc").textContent = b.description || "";
    const s = b.size || [0, 0, 0];
    $("gc-meta").textContent = `id: ${b.id} · ${s[0].toFixed(0)}×${s[1].toFixed(0)} m · 高 ${s[2].toFixed(0)} m`;
    $("godcard").classList.remove("hidden");
    if (flyTo) {
      const c = b.box.getCenter(new THREE.Vector3()); c.y = 0;
      this.fly = { from: this.target.clone(), to: c, d0: this.dist, d1: Math.max(45, b.box.getSize(new THREE.Vector3()).length() * 2.2), t: 0 };
    }
  }

  update(dt) {
    const k = this.input;
    const sp = this.dist * 0.9 * dt * (k.key("ShiftLeft") ? 3 : 1);
    const f = new THREE.Vector3(-Math.sin(this.yaw), 0, -Math.cos(this.yaw)), r = new THREE.Vector3(-f.z, 0, f.x);
    if (k.key("KeyW") || k.key("ArrowUp")) this.target.addScaledVector(f, sp);
    if (k.key("KeyS") || k.key("ArrowDown")) this.target.addScaledVector(f, -sp);
    if (k.key("KeyD") || k.key("ArrowRight")) this.target.addScaledVector(r, sp);
    if (k.key("KeyA") || k.key("ArrowLeft")) this.target.addScaledVector(r, -sp);
    if (k.key("KeyQ")) this.yaw += dt * 1.4;
    if (k.key("KeyE")) this.yaw -= dt * 1.4;
    if (k.key("KeyZ")) this.dist = Math.min(1400, this.dist * (1 + dt * 1.5));
    if (k.key("KeyX")) this.dist = Math.max(15, this.dist * (1 - dt * 1.5));
    if (this.fly) {
      this.fly.t = Math.min(1, this.fly.t + dt * 1.6); const e = this.fly.t * this.fly.t * (3 - 2 * this.fly.t);
      this.target.lerpVectors(this.fly.from, this.fly.to, e); this.dist = THREE.MathUtils.lerp(this.fly.d0, this.fly.d1, e);
      if (this.fly.t >= 1) this.fly = null;
    }
    const isl = this.world.isl; this.target.x = THREE.MathUtils.clamp(this.target.x, -isl[0] * 1.2, 3400); this.target.z = THREE.MathUtils.clamp(this.target.z, -isl[1] * 1.3, isl[1] * 1.3);
    const off = new THREE.Vector3(Math.sin(this.yaw) * Math.cos(this.pitch), Math.sin(this.pitch), Math.cos(this.yaw) * Math.cos(this.pitch));
    this.camera.position.copy(this.target).addScaledVector(off, this.dist);
    this.camera.lookAt(this.target);
    this.camera.fov += (50 - this.camera.fov) * 0.1;
  }
}
