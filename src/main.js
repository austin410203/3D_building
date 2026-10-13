import * as THREE from "three";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";
import { World, loader, B2T } from "./world.js";
import { Player } from "./player.js";
import { Car } from "./car.js";
import { CarAudio } from "./audio.js";
import { HUD } from "./hud.js";
import { TouchControls, isTouch } from "./touch.js";
import { GodView } from "./god.js";
const MOBILE = isTouch();

const $ = id => document.getElementById(id);
// ---------------------------------------------------------------- renderer / scene
const canvas = $("c");
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: "high-performance" });
renderer.setPixelRatio(Math.min(devicePixelRatio, MOBILE ? 1.0 : 1.5));
renderer.setSize(innerWidth, innerHeight);
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 0.75;
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(62, innerWidth / innerHeight, 0.1, 9000);
const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
const bloom = new UnrealBloomPass(new THREE.Vector2(innerWidth, innerHeight), 0.45, 0.35, 0.92); bloom.enabled = false;
composer.addPass(bloom); composer.addPass(new OutputPass());
addEventListener("resize", () => {
  camera.aspect = innerWidth / innerHeight; camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight); composer.setSize(innerWidth, innerHeight);
});

// ---------------------------------------------------------------- input
const input = {
  down: new Set(), just: new Set(), mdx: 0, mdy: 0, wheel: 0,
  key(c) { return this.down.has(c); }, pressed(c) { return this.just.has(c); },
  endFrame() { this.just.clear(); this.mdx = this.mdy = this.wheel = 0; },
};
addEventListener("keydown", e => { if (!input.down.has(e.code)) input.just.add(e.code); input.down.add(e.code); if (["Space", "ArrowUp", "ArrowDown"].includes(e.code)) e.preventDefault(); });
addEventListener("keyup", e => input.down.delete(e.code));
addEventListener("blur", () => input.down.clear());
addEventListener("mousemove", e => { if (document.pointerLockElement === canvas) { input.mdx += e.movementX; input.mdy += e.movementY; } });
addEventListener("wheel", e => { input.wheel += Math.sign(e.deltaY); }, { passive: true });
canvas.addEventListener("click", () => { if (!MOBILE && started && document.pointerLockElement !== canvas) lockPointer(); });
const touch = MOBILE ? new TouchControls(input) : null;
function lockPointer() { try { const r = canvas.requestPointerLock(); if (r && r.catch) r.catch(() => {}); } catch (e) {} }
if (MOBILE) {
  document.body.classList.add("mobile");
  document.querySelector("#loading .keys").innerHTML = "<b>手機操作</b> 左下搖桿 移動/轉向（推到底=跑步）· 右半邊拖曳 轉視角<br>"
    + "步行：跳 / 跑 / 上車　開車：油門 / 煞車 / 手煞 / 檔± / 下車<br>建議橫向全螢幕遊玩";
}

// ---------------------------------------------------------------- world + actors
const world = new World(scene, renderer, (f, label) => {
  $("loadbar").style.width = (f * 100).toFixed(1) + "%"; $("loadtxt").textContent = `載入 ${Math.round(f * 100)}%  ${label || ""}`;
});
const hud = new HUD(world);
const audio = new CarAudio();
let player, car, started = false, mode = "foot", god = null, preGod = "foot";
let camYaw = Math.PI, camPitch = 0.25, camDist = 4.2, firstPerson = false;
const camPos = new THREE.Vector3(), camLook = new THREE.Vector3();

async function boot() {
  const [hero, carG] = await Promise.all([loader.loadAsync("models/hero.glb"), loader.loadAsync("models/car.glb")]);
  await world.load();
  player = new Player(scene, world, hero);
  car = new Car(scene, world, carG);
  car.onShift = up => audio.blip(up);
  god = new GodView(world, camera, canvas, input, goFromGod);
  // spawn: by the central crossroads, car parked on the main avenue facing east (toward the causeway)
  const sp = world.groundAt(12, 9, 50); player.teleport(new THREE.Vector3(12, sp ? sp.point.y : 0.2, 9), Math.PI / 2);
  car.place(new THREE.Vector3(16, 0, 2.2), Math.PI / 2);
  camPos.set(6, 4, 12);
  $("start").disabled = false; $("start").textContent = "開始遊玩  ▶";
  $("loadtxt").textContent = "可以開始了！其餘建築會在背景持續載入（滑鼠會被鎖定，Esc 釋放）";
}
$("start").addEventListener("click", () => {
  started = true; $("loading").classList.add("hidden"); hud.show(); hud.building(null); godBtn.classList.remove("hidden");
  if (MOBILE) godBtn.textContent = "\u{1F310} 上帝";
  audio.start();
  if (MOBILE) {
    touch.show(); touch.setMode("foot");
    world.sun.shadow.mapSize.set(1024, 1024);
    const el = document.documentElement;
    (el.requestFullscreen ? el.requestFullscreen() : Promise.resolve()).then(() => screen.orientation && screen.orientation.lock && screen.orientation.lock("landscape").catch(() => {})).catch(() => {});
  } else lockPointer();
});
boot().catch(e => { console.error(e); $("loadtxt").textContent = "載入失敗：" + e.message; });

// ---------------------------------------------------------------- game loop
const clock = new THREE.Clock(); let fpsAcc = 0, fpsN = 0, shadows = true;
function enterCar() {
  mode = "car"; hud.setDriving(true); if (touch) touch.setMode("car");
  player.obj.removeFromParent(); car.obj.add(player.obj);
  const s = car.seat ? car.seat.position : new THREE.Vector3(0.38, 0.44, -0.25);
  player.obj.position.set(s.x, s.y - 0.98, s.z); player.obj.rotation.set(0, 0, 0);
  player.play("Drive", 0.1); camYaw = car.yaw + Math.PI;
}
function exitCar() {
  mode = "foot"; hud.setDriving(false); if (touch) touch.setMode("foot");
  car.obj.remove(player.obj); scene.add(player.obj);
  const f = car.fwd, left = new THREE.Vector3(f.z, 0, -f.x);
  const p = car.pos.clone().addScaledVector(left, 1.8); p.y += 0.5;
  player.teleport(p, car.yaw); car.throttle = 0;
}
// ---------------------------------------------------------------- god view
const godBtn = document.createElement("button"); godBtn.id = "godbtn"; godBtn.textContent = "\u{1F310} 上帝視角 (G)"; godBtn.className = "hidden";
document.body.appendChild(godBtn);
godBtn.addEventListener("click", e => { e.stopPropagation(); toggleGod(); });
godBtn.addEventListener("touchstart", e => { e.stopPropagation(); }, { passive: true });
function toggleGod() {
  if (!god || !started) return;
  if (mode !== "god") {
    preGod = mode; mode = "god"; world.godLabels = true;
    god.enter(preGod === "car" ? car.pos : player.pos);
    hud.setDriving(false); hud.mapRange = 900; if (touch) touch.root.classList.add("hidden");
    godBtn.textContent = MOBILE ? "返回" : "返回遊戲 (G)";
  } else {
    god.exit(); mode = preGod; world.godLabels = false; hud.mapRange = 420;
    if (mode === "car") hud.setDriving(true);
    if (touch) { touch.root.classList.remove("hidden"); touch.setMode(mode); }
    godBtn.textContent = MOBILE ? "\u{1F310} 上帝" : "\u{1F310} 上帝視角 (G)";
    if (!MOBILE) lockPointer();
  }
}
function goFromGod(b, how) {
  // front of the building = its spawn point (Blender local coords) rotated + translated; else 3 m in front of the facade
  const rz = b.rotz || 0, sp = (b.spawns && b.spawns[0]) ? b.spawns[0].local : [0, -((b.size && b.size[1]) || 10) / 2 - 3, 0];
  const lx = sp[0], ly = sp[1];
  const wx = b.pos[0] + lx * Math.cos(rz) - ly * Math.sin(rz), wy = b.pos[1] + lx * Math.sin(rz) + ly * Math.cos(rz);
  const p = B2T(wx, wy, 0); const g = world.groundAt(p.x, p.z, 60); p.y = g ? g.point.y + 0.05 : 0.2;
  // outward facade direction: Blender local -Y rotated by rz, converted to three (x, -y)
  const dir = new THREE.Vector3(Math.sin(rz), 0, Math.cos(rz)); const yawOut = Math.atan2(dir.x, dir.z);
  toggleGod();
  if (how === "car") {
    const cp = p.clone().addScaledVector(dir, 4); const gg = world.groundAt(cp.x, cp.z, 60); cp.y = gg ? gg.point.y : p.y;
    car.place(cp, yawOut + Math.PI / 2);
    if (mode === "foot") { player.teleport(cp.clone(), 0); enterCar(); }
  } else {
    if (mode === "car") exitCar();
    player.teleport(p, yawOut + Math.PI); camYaw = yawOut;
  }
}
function loop() {
  requestAnimationFrame(loop);
  const dt = Math.min(0.05, clock.getDelta());
  if (!player) { renderer.render(scene, camera); return; }
  if (started) {
    // global keys
    if (input.pressed("KeyN")) { world.setNight(!world.night); bloom.enabled = world.night; }
    if (input.pressed("KeyG")) toggleGod();
    if (input.pressed("KeyV")) firstPerson = !firstPerson;
    if (input.pressed("KeyH")) $("help").classList.toggle("hidden");
    if (input.pressed("KeyP")) { shadows = !shadows; world.sun.castShadow = shadows; }
    camYaw -= input.mdx * 0.0025; camPitch = THREE.MathUtils.clamp(camPitch + input.mdy * 0.002, -0.6, 1.2);
    camDist = THREE.MathUtils.clamp(camDist + input.wheel * 0.6, 1.8, 14);
    const nearCar = player.pos.distanceTo(car.pos) < 3.2;
    if (mode === "god") {
      god.update(dt); player.mixer.update(dt); hud.prompt(null);
    } else if (mode === "foot") {
      player.update(dt, input, camYaw);
      car.update(dt, input, false);
      if (touch) touch.setNearCar(nearCar);
      if (nearCar) { hud.prompt(MOBILE ? "點「上車」" : "按 F 上車"); if (input.pressed("KeyF")) enterCar(); } else hud.prompt(null);
    } else {
      car.update(dt, input, true);
      player.mixer.update(dt);
      hud.prompt(null);
      if (input.pressed("KeyF") && car.kmh < 15) exitCar();
      if (input.pressed("KeyR")) { const g = world.groundAt(car.pos.x, car.pos.z, car.pos.y + 20); car.place(new THREE.Vector3(car.pos.x, g ? g.point.y : car.pos.y + 1, car.pos.z), car.yaw); }
      hud.car(car);
    }
    audio.update(car, mode === "car");
  }
  // ---- camera
  if (mode === "god") {
    // camera placed by god.update
  } else if (mode === "foot") {
    const head = player.pos.clone(); head.y += 1.55;
    if (firstPerson) {
      camera.position.copy(head);
      camera.rotation.set(-camPitch * 0.8, camYaw, 0, "YXZ"); player.obj.visible = false;
    } else {
      player.obj.visible = true;
      const off = new THREE.Vector3(Math.sin(camYaw) * Math.cos(camPitch), Math.sin(camPitch), Math.cos(camYaw) * Math.cos(camPitch));
      let d = camDist;
      const hit = world.bvh.raycastFirst(new THREE.Ray(head, off), THREE.DoubleSide, 0, camDist);
      if (hit) d = Math.max(0.6, hit.distance - 0.25);
      camera.position.copy(head).addScaledVector(off, d);
      camera.lookAt(head);
    }
    camera.fov += (62 - camera.fov) * 0.1;
  } else {
    const f = car.fwd;
    if (firstPerson) {
      const s = new THREE.Vector3(0.38, 1.12, -0.05).applyQuaternion(car.obj.quaternion).add(car.pos);
      camera.position.copy(s); camera.quaternion.copy(car.obj.quaternion).multiply(new THREE.Quaternion().setFromEuler(new THREE.Euler(-0.05, Math.PI, 0)));
      camera.rotateY(-input.mdx * 0); player.obj.visible = false;
    } else {
      player.obj.visible = true;
      const spd = car.kmh;
      const back = 6.2 + spd / 300 * 2.5, up = 2.1 + spd / 300 * 0.4;
      // allow mouse orbit around the car; it springs back behind when idle
      camYaw += (car.yaw + Math.PI - camYaw) * (input.mdx === 0 ? Math.min(1, dt * 2.5) : 0);
      const target = car.pos.clone().add(new THREE.Vector3(Math.sin(camYaw) * back, up, Math.cos(camYaw) * back));
      camPos.lerp(target, Math.min(1, dt * 7));
      camera.position.copy(camPos);
      camLook.copy(car.pos).addScaledVector(f, 2.5); camLook.y += 0.9;
      camera.lookAt(camLook);
    }
    camera.fov += ((62 + Math.min(1, car.kmh / 300) * 22) - camera.fov) * 0.08;
  }
  camera.updateProjectionMatrix();
  const actor = mode === "god" ? god.target : (mode === "foot" ? player.pos : car.pos);
  world.update(dt, mode === "foot" ? player.pos : null, camera.position);
  world.followSun(actor);
  if (started) {
    hud.building(world.nearestBuilding(actor));
    const yaw = mode === "god" ? god.yaw + Math.PI : (mode === "foot" ? player.obj.rotation.y : car.yaw);
    hud.minimap(actor, yaw, mode === "foot" ? car.pos : null);
  }
  input.endFrame();
  if (bloom.enabled) composer.render(); else renderer.render(scene, camera);
  fpsAcc += dt; fpsN++;
  if (fpsAcc > 0.5) { $("fps").textContent = `${Math.round(fpsN / fpsAcc)} fps · ${renderer.info.render.calls} draws · ${(renderer.info.render.triangles / 1e6).toFixed(2)}M tris`; fpsAcc = 0; fpsN = 0; }
}
loop();
window.game = { get world() { return world; }, get car() { return car; }, get player() { return player; }, input, setMode: m => (m === "car" ? enterCar() : exitCar()) };
