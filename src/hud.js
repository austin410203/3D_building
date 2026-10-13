// HUD: analog tachometer + digital speed / gear, minimap, building name, prompts.
const $ = id => document.getElementById(id);

export class HUD {
  constructor(world) {
    this.world = world;
    this.g = $("gauge").getContext("2d"); this.mm = $("minimap").getContext("2d");
    this.lastB = null;
  }
  show() { $("hud").classList.remove("hidden"); }
  setDriving(on) { $("dash").classList.toggle("hidden", !on); }
  prompt(txt) { const p = $("prompt"); if (txt) { p.textContent = txt; p.style.display = "block"; } else p.style.display = "none"; }
  building(b) {
    if (b === this.lastB) return; this.lastB = b;
    $("bname").textContent = b ? `${b.name_zh}  ${b.name_en}` : "海港小鎮島 Harbor Town Island";
    $("bstyle").textContent = b ? `${b.style_zh} · ${b.style} · ${b.tier}` : `TownKit · ${this.world.buildings.length} 棟建築`;
  }
  car(car) {
    $("kmh").textContent = Math.round(car.kmh);
    $("gear").textContent = car.gearLabel; $("mode").textContent = car.auto ? "AUTO  [M]" : "MANUAL  Q/E";
    const x = this.g, W = 300, cx = 150, cy = 150, R = 132;
    x.clearRect(0, 0, W, W);
    x.beginPath(); x.arc(cx, cy, R + 8, 0, Math.PI * 2); x.fillStyle = "rgba(5,8,16,0.72)"; x.fill();
    const a0 = Math.PI * 0.75, a1 = Math.PI * 2.25, maxR = 9000;
    const ang = r => a0 + (a1 - a0) * Math.min(1, r / maxR);
    x.lineWidth = 10; x.strokeStyle = "#ffffff22"; x.beginPath(); x.arc(cx, cy, R - 6, a0, a1); x.stroke();
    x.strokeStyle = "#e33"; x.beginPath(); x.arc(cx, cy, R - 6, ang(7500), a1); x.stroke();
    x.strokeStyle = car.rpm > 7300 ? "#f44" : "#4df"; x.beginPath(); x.arc(cx, cy, R - 6, a0, ang(car.rpm)); x.stroke();
    x.fillStyle = "#fff"; x.font = "bold 15px sans-serif"; x.textAlign = "center"; x.textBaseline = "middle";
    for (let k = 0; k <= 9; k++) {
      const a = ang(k * 1000);
      x.save(); x.translate(cx + Math.cos(a) * (R - 30), cy + Math.sin(a) * (R - 30)); x.fillText(k, 0, 0); x.restore();
      x.strokeStyle = "#fff"; x.lineWidth = 3; x.beginPath();
      x.moveTo(cx + Math.cos(a) * (R - 14), cy + Math.sin(a) * (R - 14)); x.lineTo(cx + Math.cos(a) * R, cy + Math.sin(a) * R); x.stroke();
    }
    const a = ang(car.rpm);
    x.strokeStyle = "#f33"; x.lineWidth = 4; x.beginPath(); x.moveTo(cx, cy); x.lineTo(cx + Math.cos(a) * (R - 20), cy + Math.sin(a) * (R - 20)); x.stroke();
    x.fillStyle = "#ddd"; x.font = "11px sans-serif"; x.fillText("x1000 rpm", cx, cy + 60);
    if (car.shiftFlash > 0) { x.fillStyle = `rgba(80,255,255,${car.shiftFlash})`; x.font = "bold 18px sans-serif"; x.fillText("SHIFT", cx, cy - 75); }
    if (car.kmh >= 299) { x.fillStyle = "#fc3"; x.font = "bold 13px sans-serif"; x.fillText("LIMITER 300", cx, cy + 82); }
  }
  minimap(p, yaw, carPos) {
    const x = this.mm, W = x.canvas.width, S = W / 2, scale = W / (this.mapRange || 420);
    const toM = (wx, wz) => [S + (wx - p.x) * scale, S + (wz - p.z) * scale];
    x.clearRect(0, 0, W, W);
    x.save(); x.beginPath(); x.arc(S, S, S - 2, 0, Math.PI * 2); x.clip();
    x.fillStyle = "#1f4f6e"; x.fillRect(0, 0, W, W);
    // island + ring
    x.fillStyle = "#3d6b3a"; x.beginPath();
    const I = this.world.isl || [300, 240];
    for (let i = 0; i <= 64; i++) { const t = i / 64 * Math.PI * 2, c = Math.cos(t), s = Math.sin(t);
      const bx = I[0] * 0.95 * Math.sign(c) * Math.abs(c) ** 0.5, by = I[1] * 0.95 * Math.sign(s) * Math.abs(s) ** 0.5;
      const [mx, my] = toM(bx, -by); i ? x.lineTo(mx, my) : x.moveTo(mx, my); }
    x.fill();
    if (this.world.ring) { x.strokeStyle = "#999"; x.lineWidth = 3; x.beginPath(); this.world.ring.forEach((q, i) => { const [mx, my] = toM(q.x, q.z); i ? x.lineTo(mx, my) : x.moveTo(mx, my); }); x.closePath(); x.stroke(); }
    x.strokeStyle = "#888"; x.lineWidth = 3;
    for (const [ax, c, a1, a2] of [["x", 0, 240, 3200], ...(this.world.roads || [])]) {
      x.beginPath();
      const [m1x, m1y] = ax === "x" ? toM(a1, -c) : toM(c, -a1); const [m2x, m2y] = ax === "x" ? toM(a2, -c) : toM(c, -a2);
      x.moveTo(m1x, m1y); x.lineTo(m2x, m2y); x.stroke();
    }
    x.fillStyle = "#e8d8b0";
    for (const b of this.world.buildings) { const [mx, my] = toM(b.p.x, b.p.z); x.fillRect(mx - 2.5, my - 2.5, 5, 5); }
    if (carPos) { const [mx, my] = toM(carPos.x, carPos.z); x.fillStyle = "#f33"; x.beginPath(); x.arc(mx, my, 4, 0, Math.PI * 2); x.fill(); }
    x.restore();
    x.save(); x.translate(S, S); x.rotate(-yaw + Math.PI);
    x.fillStyle = "#fff"; x.beginPath(); x.moveTo(0, -8); x.lineTo(5, 6); x.lineTo(-5, 6); x.closePath(); x.fill(); x.restore();
  }
}
