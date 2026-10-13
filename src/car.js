// Sports car: engine torque curve, 6-speed gearbox (auto / manual), clutch launch, shift time, 300 km/h limiter,
// aero drag, kinematic steering with handbrake drift, 4-point ground following, capsule wall collisions.
import * as THREE from "three";

export const GEARS = [3.4, 2.36, 1.79, 1.38, 1.1, 0.88];
const FD = 3.42, WR = 0.345, EFF = 0.9, MASS = 1450, WB = 2.72, TRACK = 0.83;
const IDLE = 900, REDLINE = 8000, LIMIT_KMH = 300;
const TQ = [[0, 300], [1000, 360], [2500, 480], [4000, 600], [5500, 660], [6500, 620], [7300, 560], [8000, 470], [8600, 300]];
function torque(rpm) {
  for (let i = 1; i < TQ.length; i++) if (rpm <= TQ[i][0]) {
    const [r0, t0] = TQ[i - 1], [r1, t1] = TQ[i]; return t0 + (t1 - t0) * (rpm - r0) / (r1 - r0);
  }
  return 0;
}
const tmpBox = new THREE.Box3(), seg = new THREE.Line3(), pA = new THREE.Vector3(), pB = new THREE.Vector3();

export class Car {
  constructor(scene, world, gltf) {
    this.world = world; this.obj = gltf.scene; scene.add(this.obj);
    this.obj.traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; } });
    const f = n => this.obj.getObjectByName(n);
    this.wheels = ["Wheel_FL", "Wheel_FR", "Wheel_RL", "Wheel_RR"].map(f);
    this.pivots = [f("FrontPivot_L"), f("FrontPivot_R")];
    this.steeringWheel = f("SteeringWheel"); this.swRot0 = this.steeringWheel ? this.steeringWheel.quaternion.clone() : null;
    this.seat = f("Seat_Driver");
    this.brakeMats = []; this.obj.traverse(o => { if (o.isMesh) for (const m of [].concat(o.material)) if (m && m.name === "CarBrake") { this.brakeMats.push(m); } });
    this.lights = [];
    for (const sx of [-0.62, 0.62]) {
      const l = new THREE.SpotLight(0xf4f7ff, 0, 90, 0.45, 0.5, 1.2); l.position.set(sx, 0.6, 2.2);
      const t = new THREE.Object3D(); t.position.set(sx * 1.4, -0.4, 30); this.obj.add(l, t); l.target = t; this.lights.push(l);
    }
    this.pos = new THREE.Vector3(); this.yaw = 0; this.vLong = 0; this.vLat = 0; this.vy = 0;
    this.rpm = IDLE; this.gear = 1; this.shiftT = 0; this.shiftTo = 1; this.auto = true; this.steer = 0;
    this.throttle = 0; this.brake = 0; this.slip = 0; this.pitch = 0; this.roll = 0; this.airborne = false;
    this.wheelSpin = 0; this.lastShift = 0; this.shiftFlash = 0;
  }
  place(p, yaw) { this.pos.copy(p); this.yaw = yaw; this.vLong = this.vLat = this.vy = 0; this.gear = 1; this.rpm = IDLE; this.settle(); }
  get kmh() { return Math.abs(this.vLong) * 3.6; }
  get fwd() { return new THREE.Vector3(Math.sin(this.yaw), 0, Math.cos(this.yaw)); }
  get gearLabel() { return this.gear < 0 ? "R" : (this.shiftT > 0 ? "·" : String(this.gear)); }

  shift(to) {
    if (to === this.gear || to < 1 || to > GEARS.length || this.shiftT > 0) return;
    this.shiftTo = to; this.shiftT = to > this.gear ? 0.22 : 0.16; this.shiftFlash = 1;
    if (this.onShift) this.onShift(to > this.gear);
  }

  update(dt, input, driving) {
    this.simT = (this.simT || 0) + dt;
    const thr = driving && (input.key("KeyW") || input.key("ArrowUp")) ? 1 : 0;
    const brk = driving && (input.key("KeyS") || input.key("ArrowDown")) ? 1 : 0;
    const hb = driving && input.key("Space");
    let st = 0;
    if (driving) { if (input.key("KeyA") || input.key("ArrowLeft")) st += 1; if (input.key("KeyD") || input.key("ArrowRight")) st -= 1; }
    if (driving && input.axis && input.axis.active) st = -Math.sign(input.axis.x) * Math.min(1, Math.abs(input.axis.x) * 1.15) ** 1.4;   // analog touch steering
    if (driving && input.pressed("KeyM")) this.auto = !this.auto;
    if (driving && !this.auto) { if (input.pressed("KeyE")) this.shift(this.gear + 1); if (input.pressed("KeyQ")) this.shift(this.gear - 1); }

    // ---- gear selection: reverse / drive
    let throttle = thr, braking = 0;
    if (this.gear > 0) {
      if (brk && this.vLong > 0.6) braking = 1;
      else if (brk && this.vLong <= 0.6) { this.gear = -1; this.rpm = IDLE; }
    } else {
      if (thr && this.vLong > -0.6) { this.gear = 1; } else if (thr) braking = 1;
      throttle = brk ? 1 : 0;
    }
    if (this.kmh >= LIMIT_KMH && this.gear > 0) throttle = 0;                     // electronic limiter
    this.throttle += (throttle - this.throttle) * Math.min(1, dt * 8); this.brake = braking;

    // ---- engine / gearbox
    const ratio = this.gear < 0 ? 3.2 : GEARS[(this.shiftT > 0 ? this.shiftTo : this.gear) - 1];
    const wheelRpm = Math.abs(this.vLong) / (2 * Math.PI * WR) * 60;
    let target = wheelRpm * ratio * FD;
    if (this.shiftT > 0) {
      this.shiftT -= dt;
      this.rpm += (target - this.rpm) * Math.min(1, dt * 14);
      if (this.shiftT <= 0) { this.gear = this.shiftTo; this.shiftT = 0; }
    } else {
      if ((this.gear === 1 || this.gear < 0) && target < 2200) target = Math.max(target, IDLE + this.throttle * 2600);   // clutch slip launch
      target = Math.max(IDLE, target);
      this.rpm += (target - this.rpm) * Math.min(1, dt * 10);
    }
    let drive = 0;
    if (this.shiftT <= 0) {
      let tq = torque(this.rpm) * this.throttle;
      if (this.rpm >= REDLINE) { tq = 0; this.rpm = REDLINE - 150 * Math.random(); }   // rev limiter bounce
      drive = tq * ratio * FD * EFF / WR * (this.gear < 0 ? -1 : 1);
      if (this.throttle < 0.05 && this.gear > 0 && this.vLong > 1) drive -= 900 * this.rpm / REDLINE;                 // engine braking
      drive = THREE.MathUtils.clamp(drive, -10500, 10500);                                                       // traction limit
    }
    if (this.gear < 0 && this.vLong < -8.5) drive = Math.max(drive, 0);
    // auto box
    this.shiftFlash = Math.max(0, this.shiftFlash - dt * 3);
    if (this.auto && this.gear > 0 && this.shiftT <= 0 && !this.airborne) {
      const now = this.simT;
      if (this.rpm > 7350 && this.throttle > 0.3 && this.gear < GEARS.length && now - this.lastShift > 0.4) { this.shift(this.gear + 1); this.lastShift = now; }
      else if (this.gear > 1 && (this.rpm < 2900 || (braking && this.rpm < 4200)) && now - this.lastShift > 0.5) {
        const down = wheelRpm * GEARS[this.gear - 2] * FD;
        if (down < 7200) { this.shift(this.gear - 1); this.lastShift = now; }
      }
    }
    // ---- longitudinal
    const v = this.vLong, sgn = Math.sign(v);
    const drag = 0.5 * 1.225 * 0.72 * v * v * sgn + (Math.abs(v) > 0.05 ? 0.012 * MASS * 9.81 * sgn : 0);
    let brakeF = 0;
    if (braking) brakeF = 13500 * sgn;
    if (hb) brakeF += 4500 * sgn;
    if (!this.airborne) {
      let a = (drive - drag - brakeF) / MASS;
      const nv = this.vLong + a * dt;
      this.vLong = (braking || hb) && Math.sign(nv) !== Math.sign(this.vLong) && this.vLong !== 0 ? 0 : nv;
      if (!thr && !brk && Math.abs(this.vLong) < 0.15) this.vLong = 0;
    }
    // ---- steering (speed-sensitive) + lateral grip / drift
    const spd = Math.abs(this.vLong);
    const maxSteer = THREE.MathUtils.lerp(0.62, 0.06, THREE.MathUtils.clamp(spd / 75, 0, 1) ** 0.6);
    this.steer += (st * maxSteer - this.steer) * Math.min(1, dt * (st ? 5 : 8));
    if (!this.airborne) {
      let yawRate = this.vLong * Math.tan(this.steer) / WB;
      if (hb && spd > 8) yawRate *= 1.6;
      this.yaw += yawRate * dt;
      const grip = hb ? 1.0 : (spd > 40 ? 7 : 10);
      // a share of the old momentum stays sideways when gripping is low -> drift
      this.vLat += (-yawRate * this.vLong * (hb ? 0.18 : 0.02)) * dt;
      this.vLat *= Math.exp(-grip * dt);
    }
    this.slip = Math.min(1, Math.abs(this.vLat) / 6 + (hb && spd > 5 ? 0.5 : 0) + (this.throttle > 0.8 && this.gear === 1 && spd < 12 ? 0.35 : 0));
    // ---- integrate with collision sub-steps
    const f = this.fwd, r = new THREE.Vector3(-f.z, 0, f.x);
    const vel = f.clone().multiplyScalar(this.vLong).addScaledVector(r, this.vLat);
    const n = Math.max(1, Math.ceil(vel.length() * dt / 0.35));
    for (let i = 0; i < n; i++) {
      this.pos.addScaledVector(vel, dt / n);
      if (this.collide(vel)) { const ff = this.fwd, rr = new THREE.Vector3(-ff.z, 0, ff.x); this.vLong = vel.dot(ff); this.vLat = vel.dot(rr); }
    }
    this.settle(dt);
    // ---- visuals
    this.wheelSpin += this.vLong / WR * dt;
    for (const w of this.wheels) if (w) w.rotation.x = this.wheelSpin;
    for (const p of this.pivots) if (p) p.rotation.y = this.steer;
    if (this.steeringWheel) { this.steeringWheel.quaternion.copy(this.swRot0).multiply(new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0, 1, 0), this.steer * 6)); }
    for (const m of this.brakeMats) m.emissiveIntensity = (braking || hb) ? 8 : (this.world.night ? 2.5 : 1.0);
    for (const l of this.lights) l.intensity = this.world.night ? 400 : 0;
  }

  collide(vel) {
    const bvh = this.world.bvh; const f = this.fwd; const r = new THREE.Vector3(-f.z, 0, f.x);
    let hit = false;
    for (const off of [-0.38, 0, 0.38]) {
      seg.start.copy(this.pos).addScaledVector(f, -1.55).addScaledVector(r, off); seg.start.y += 0.85;
      seg.end.copy(this.pos).addScaledVector(f, 1.6).addScaledVector(r, off); seg.end.y += 0.85;
      const rad = 0.56;
      tmpBox.makeEmpty(); tmpBox.expandByPoint(seg.start); tmpBox.expandByPoint(seg.end); tmpBox.min.addScalar(-rad); tmpBox.max.addScalar(rad);
      const push = new THREE.Vector3();
      bvh.shapecast({
        intersectsBounds: b => b.intersectsBox(tmpBox),
        intersectsTriangle: tri => {
          const d = tri.closestPointToSegment(seg, pA, pB);
          if (d < rad) {
            const dir = pB.clone().sub(pA); dir.y = 0;
            if (dir.lengthSq() < 1e-8) return;
            dir.normalize(); push.addScaledVector(dir, rad - d);
            seg.start.addScaledVector(dir, rad - d); seg.end.addScaledVector(dir, rad - d);
          }
        },
      });
      if (push.lengthSq() > 1e-8) {
        this.pos.add(push); hit = true;
        const nrm = push.clone().normalize(); const vn = vel.dot(nrm);
        if (vn < 0) { vel.addScaledVector(nrm, -1.3 * vn); vel.multiplyScalar(0.85); if (this.onCrash && -vn > 6) this.onCrash(-vn); }
      }
    }
    return hit;
  }

  settle(dt = 0) {
    // sample ground under the four wheels
    const f = this.fwd, r = new THREE.Vector3(-f.z, 0, f.x);
    const hs = [];
    for (const [a, b] of [[WB / 2, TRACK], [WB / 2, -TRACK], [-WB / 2, TRACK], [-WB / 2, -TRACK]]) {
      const p = this.pos.clone().addScaledVector(f, a).addScaledVector(r, b);
      const hit = this.world.groundAt(p.x, p.z, this.pos.y + 1.4, 30);
      hs.push(hit ? hit.point.y : -1e3);
    }
    const valid = hs.filter(h => h > -999);
    const g = valid.length ? valid.reduce((s, h) => s + h, 0) / valid.length : -1e3;
    if (this.pos.y > g + 0.08 && dt) { this.airborne = true; this.vy -= 9.81 * dt; this.pos.y += this.vy * dt; if (this.pos.y < g) { this.pos.y = g; this.vy = 0; this.airborne = false; } }
    else { this.pos.y = g > -999 ? g : this.pos.y; this.vy = 0; this.airborne = false; }
    if (valid.length >= 2 && !this.airborne) { this.safe = this.safe || {}; this.safe.p = this.pos.clone(); this.safe.yaw = this.yaw; }
    if (this.pos.y < -2.5 && this.safe) {                       // fell into the sea / off the map -> back to last safe spot
      this.place(this.safe.p.clone().addScaledVector(this.fwd, -8), this.safe.yaw); if (this.onReset) this.onReset(); return;
    }
    if (valid.length === 4) {
      const front = (hs[0] + hs[1]) / 2, back = (hs[2] + hs[3]) / 2, left = (hs[0] + hs[2]) / 2, right = (hs[1] + hs[3]) / 2;
      const tp = Math.atan2(back - front, WB), tr = Math.atan2(left - right, TRACK * 2);
      this.pitch += (tp - this.pitch) * 0.3; this.roll += (tr - this.roll) * 0.3;
    }
    // body roll from cornering + squat
    const lat = THREE.MathUtils.clamp(this.vLong * Math.tan(this.steer) / WB * this.vLong * 0.004, -0.06, 0.06);
    const pitchDyn = THREE.MathUtils.clamp(-this.throttle * 0.012 + this.brake * 0.03, -0.03, 0.04);
    this.obj.position.copy(this.pos);
    this.obj.rotation.set(0, 0, 0);
    this.obj.quaternion.setFromEuler(new THREE.Euler(this.pitch + pitchDyn, this.yaw, this.roll + lat, "YXZ"));
  }
}
