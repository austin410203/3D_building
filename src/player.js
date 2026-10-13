// On-foot controller: capsule vs. BVH (three-mesh-bvh shapecast), walk / run / jump, animation crossfades.
import * as THREE from "three";

const UP = new THREE.Vector3(0, 1, 0);
const tmpBox = new THREE.Box3(), tmpSeg = new THREE.Line3(), tv = new THREE.Vector3(), tv2 = new THREE.Vector3();

export class Player {
  constructor(scene, world, gltf) {
    this.world = world;
    this.obj = gltf.scene; this.obj.traverse(o => { if (o.isMesh) { o.castShadow = true; o.frustumCulled = false; } });
    scene.add(this.obj);
    this.mixer = new THREE.AnimationMixer(this.obj);
    this.actions = {};
    for (const clip of gltf.animations) this.actions[clip.name] = this.mixer.clipAction(clip);
    this.current = null; this.play("Idle");
    this.radius = 0.32; this.segment = new THREE.Line3(new THREE.Vector3(0, 0.32, 0), new THREE.Vector3(0, 1.45, 0));
    this.pos = new THREE.Vector3(); this.vel = new THREE.Vector3();
    this.onGround = false; this.yaw = 0; this.facing = 0;
    this.visible = true;
  }
  play(name, fade = 0.2) {
    const a = this.actions[name]; if (!a || this.current === a) return;
    a.reset().setEffectiveWeight(1).fadeIn(fade).play();
    if (this.current) this.current.fadeOut(fade);
    this.current = a;
  }
  setVisible(v) { this.visible = v; this.obj.visible = v; }
  teleport(p, yaw = 0) { this.pos.copy(p); this.vel.set(0, 0, 0); this.facing = yaw; }

  update(dt, input, camYaw) {
    // desired horizontal velocity relative to the camera
    const fwd = new THREE.Vector3(-Math.sin(camYaw), 0, -Math.cos(camYaw));
    const right = new THREE.Vector3(-fwd.z, 0, fwd.x);
    const wish = new THREE.Vector3();
    if (input.key("KeyW")) wish.add(fwd); if (input.key("KeyS")) wish.sub(fwd);
    if (input.key("KeyD")) wish.add(right); if (input.key("KeyA")) wish.sub(right);
    let scale = 1;
    if (input.axis && input.axis.active) {                      // touch joystick (analog)
      wish.set(0, 0, 0).addScaledVector(fwd, -input.axis.y).addScaledVector(right, input.axis.x);
      scale = Math.min(1, input.axis.mag * 1.25);
    }
    const moving = wish.lengthSq() > 0;
    const run = input.key("ShiftLeft") || input.key("ShiftRight") || input.key("TouchRun");
    const speed = (run ? 6.2 : 2.0) * (run ? 1 : Math.max(0.35, scale));
    if (moving) {
      wish.normalize();
      this.facing = Math.atan2(wish.x, wish.z);
    }
    const accel = this.onGround ? 14 : 3;
    const tx = wish.x * speed, tz = wish.z * speed;
    this.vel.x += (tx - this.vel.x) * Math.min(1, accel * dt);
    this.vel.z += (tz - this.vel.z) * Math.min(1, accel * dt);
    if (this.onGround && input.pressed("Space")) { this.vel.y = 5.2; this.onGround = false; }
    this.vel.y += -20 * dt;
    // integrate in sub-steps with capsule collision
    const steps = 4, h = dt / steps;
    for (let s = 0; s < steps; s++) this.step(h);
    if (this.pos.y < -20) this.pos.y = 5;
    // visuals
    this.obj.position.copy(this.pos);
    const cur = this.obj.rotation.y; let d = this.facing - cur; d = Math.atan2(Math.sin(d), Math.cos(d));
    this.obj.rotation.y = cur + d * Math.min(1, dt * 12);
    const hs = Math.hypot(this.vel.x, this.vel.z);
    if (!this.onGround) this.play("Jump", 0.15);
    else if (hs > 3.6) { this.play("Run"); this.current.timeScale = hs / 6.2; }
    else if (hs > 0.3) { this.play("Walk"); this.current.timeScale = Math.max(0.6, hs / 1.9); }
    else this.play("Idle", 0.3);
    this.mixer.update(dt);
  }

  step(h) {
    this.pos.addScaledVector(this.vel, h);
    const bvh = this.world.bvh;
    tmpSeg.copy(this.segment); tmpSeg.start.add(this.pos); tmpSeg.end.add(this.pos);
    tmpBox.makeEmpty(); tmpBox.expandByPoint(tmpSeg.start); tmpBox.expandByPoint(tmpSeg.end);
    tmpBox.min.addScalar(-this.radius); tmpBox.max.addScalar(this.radius);
    const r = this.radius;
    bvh.shapecast({
      intersectsBounds: box => box.intersectsBox(tmpBox),
      intersectsTriangle: tri => {
        const triPoint = tv, capPoint = tv2;
        const dist = tri.closestPointToSegment(tmpSeg, triPoint, capPoint);
        if (dist < r) {
          const depth = r - dist;
          const dir = capPoint.sub(triPoint).normalize();
          tmpSeg.start.addScaledVector(dir, depth); tmpSeg.end.addScaledVector(dir, depth);
        }
      },
    });
    const newPos = tv.copy(tmpSeg.start).sub(this.segment.start);
    const delta = newPos.clone().sub(this.pos);
    this.onGround = delta.y > Math.abs(h * this.vel.y * 0.25);
    const off = Math.max(0, delta.length() - 1e-5);
    delta.normalize().multiplyScalar(off);
    this.pos.add(delta);
    if (this.onGround) this.vel.y = 0;
    else if (off > 0) { delta.normalize(); this.vel.addScaledVector(delta, -delta.dot(this.vel)); }
  }
}
