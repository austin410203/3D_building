// World: island env + 67 buildings (progressive), collision BVH, extra roads (ring + causeway), doors, labels, sky/day-night.
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";
import { Sky } from "three/addons/objects/Sky.js";
import * as BGU from "three/addons/utils/BufferGeometryUtils.js";
import { MeshBVH, acceleratedRaycast } from "three-mesh-bvh";

THREE.Mesh.prototype.raycast = acceleratedRaycast;
const draco = new DRACOLoader().setDecoderPath("https://www.gstatic.com/draco/versioned/decoders/1.5.7/");
export const loader = new GLTFLoader().setDRACOLoader(draco);
const B2T = (x, y, z) => new THREE.Vector3(x, z, -y);          // Blender (Z-up) -> three (Y-up)

// island ring road + 3 km causeway (Blender coords, metres) — must match TownKit/scripts/world.py
let ISL = [300, 240];
const RING_D = 0.815, ROAD_Z = 0.17;
function superellipse(t, d) {
  const c = Math.cos(t), s = Math.sin(t);
  return [ISL[0] * d * Math.sign(c) * Math.abs(c) ** 0.5, ISL[1] * d * Math.sign(s) * Math.abs(s) ** 0.5];
}

export class World {
  constructor(scene, renderer, onProgress) {
    this.scene = scene; this.renderer = renderer; this.onProgress = onProgress;
    this.buildings = []; this.doors = []; this.labels = []; this.colliderMeshes = [];
    this.night = false; this.glassMats = new Set(); this.emissiveMats = new Set();
    this.root = new THREE.Group(); scene.add(this.root);
  }

  async load() {
    const t0 = performance.now();
    this.manifest = await (await fetch("models/manifest.json?v=" + Date.now(), { cache: "no-store" })).json();
    const V = this.manifest.build || "";
    this.v = V ? "?v=" + V : "";
    if (this.manifest.isl) ISL = this.manifest.isl;
    this.isl = ISL; this.roads = this.manifest.roads || [];
    this.setupSky();
    this.setupSea();
    const prog = { done: 0, total: 3 + this.manifest.buildings.length };
    const tick = (label) => { prog.done++; this.onProgress(prog.done / prog.total, label); };
    const [env, col] = await Promise.all([
      loader.loadAsync("models/" + this.manifest.env.shell + this.v).then(g => { tick("地形"); return g; }),
      loader.loadAsync("models/collider.glb" + this.v).then(g => { tick("碰撞"); return g; }),
    ]);
    this.prepVisual(env.scene); this.root.add(env.scene);
    const roads = this.buildExtraRoads();
    this.buildCollider(col.scene, roads);
    tick("道路");
    // buildings: nearest first, 6 parallel
    const spawn = new THREE.Vector3(0, 0, 0);
    const list = this.manifest.buildings.map(b => ({ ...b, p: B2T(...b.pos) })).sort((a, b) => a.p.distanceTo(spawn) - b.p.distanceTo(spawn));
    let i = 0;
    const worker = async () => {
      while (i < list.length) {
        const b = list[i++];
        try {
          const g = await loader.loadAsync("models/" + b.shell + this.v);
          this.prepVisual(g.scene); this.root.add(g.scene);
          const rec = { ...b, shell: g.scene, interior: null, interiorUrl: b.interior, loadingInt: false };
          this.registerDoors(g.scene, rec);
          this.addLabel(rec);
          this.buildings.push(rec);
        } catch (e) { console.warn("building failed", b.id, e); }
        tick(b.name_zh);
      }
    };
    // play can start once the nearest buildings are in; the rest keep streaming in the background
    this.allLoaded = Promise.all([worker(), worker(), worker(), worker(), worker(), worker()]).then(() => {
      console.log("world loaded in", ((performance.now() - t0) / 1000).toFixed(1), "s"); this.onProgress(1, "全部建築已載入");
      setTimeout(() => this.batchStatic(), 50);
    });
    await new Promise(res => { const iv = setInterval(() => { if (this.buildings.length >= 12 || i >= list.length) { clearInterval(iv); res(); } }, 100); });
  }

  // Merge every static building mesh by material + 250 m grid cell -> a few hundred draw calls instead of thousands.
  // Doors (D_* nodes, animated), interiors (loaded later) and label sprites stay separate.
  batchStatic() {
    const t0 = performance.now(), CELL = 250, groups = new Map();
    const c = new THREE.Vector3();
    for (const b of this.buildings) {
      b.shell.updateMatrixWorld(true);
      b.box = new THREE.Box3().setFromObject(b.shell);
      const take = [];
      b.shell.traverse(o => {
        if (!o.isMesh || Array.isArray(o.material)) return;
        for (let p = o; p && p !== b.shell; p = p.parent) if (p.name && p.name.startsWith("D_")) return;
        take.push(o);
      });
      for (const o of take) {
        const src = o.geometry;
        if (!src.attributes.position) continue;
        if (!src.boundingSphere) src.computeBoundingSphere();
        c.copy(src.boundingSphere.center).applyMatrix4(o.matrixWorld);
        const key = o.material.uuid + "|" + Math.floor(c.x / CELL) + "|" + Math.floor(c.z / CELL);
        const g = new THREE.BufferGeometry();
        g.setAttribute("position", src.attributes.position.clone());
        g.setAttribute("normal", src.attributes.normal ? src.attributes.normal.clone() : null);
        if (!src.attributes.normal) { g.deleteAttribute("normal"); g.computeVertexNormals(); }
        const n = src.attributes.position.count;
        g.setAttribute("uv", src.attributes.uv ? src.attributes.uv.clone() : new THREE.BufferAttribute(new Float32Array(n * 2), 2));
        if (src.index) g.setIndex(src.index.clone()); else { const ix = new Uint32Array(n); for (let i = 0; i < n; i++) ix[i] = i; g.setIndex(new THREE.BufferAttribute(ix, 1)); }
        g.applyMatrix4(o.matrixWorld);
        let grp = groups.get(key); if (!grp) groups.set(key, grp = { mat: o.material, geos: [] });
        grp.geos.push(g);
        o.removeFromParent(); src.dispose();
      }
    }
    let n = 0;
    for (const { mat, geos } of groups.values()) {
      const merged = BGU.mergeGeometries(geos, false);
      for (const g of geos) g.dispose();
      if (!merged) continue;
      merged.computeBoundingSphere();
      const m = new THREE.Mesh(merged, mat);
      m.castShadow = !this.glassMats.has(mat); m.receiveShadow = true; m.matrixAutoUpdate = false;
      this.root.add(m); n++;
    }
    console.log("batched static buildings into", n, "meshes in", ((performance.now() - t0) / 1000).toFixed(1), "s");
    this.batched = true;
  }

  prepVisual(root) {
    root.traverse(o => {
      if (!o.isMesh) return;
      o.castShadow = true; o.receiveShadow = true;
      const mats = Array.isArray(o.material) ? o.material : [o.material];
      for (const m of mats) {
        if (!m) continue;
        if (m.map) { m.map.anisotropy = 8; }
        if (/glass/i.test(m.name) && !/frost/i.test(m.name)) { this.glassMats.add(m); o.castShadow = false; }
        if (m.emissive && (m.emissive.r + m.emissive.g + m.emissive.b) > 0.05) { this.emissiveMats.add(m); m.userData.baseEI = m.emissiveIntensity; }
        if (m.transparent) { m.depthWrite = false; }
      }
    });
  }

  // ------------------------------------------------------------- collision
  buildCollider(colScene, extra) {
    const geos = [];
    colScene.updateMatrixWorld(true);
    colScene.traverse(o => {
      if (!o.isMesh) return;
      const g = o.geometry.clone(); g.applyMatrix4(o.matrixWorld);
      for (const k of Object.keys(g.attributes)) if (k !== "position") g.deleteAttribute(k);
      geos.push(g.index ? g.toNonIndexed() : g);
    });
    for (const g of extra) { const c = g.clone(); for (const k of Object.keys(c.attributes)) if (k !== "position") c.deleteAttribute(k); geos.push(c.index ? c.toNonIndexed() : c); }
    const merged = BGU.mergeGeometries(geos, false);
    merged.boundsTree = new MeshBVH(merged, { maxLeafTris: 10 });
    this.collider = new THREE.Mesh(merged, new THREE.MeshBasicMaterial({ wireframe: true, visible: false }));
    this.scene.add(this.collider);
    this.bvh = merged.boundsTree;
  }

  groundAt(x, z, fromY = 60, maxD = 200) {
    const ray = new THREE.Ray(new THREE.Vector3(x, fromY, z), new THREE.Vector3(0, -1, 0));
    const hit = this.bvh.raycastFirst(ray, THREE.DoubleSide, 0, maxD);
    return hit ? hit : null;
  }

  // ------------------------------------------------------------- ring road + causeway
  buildExtraRoads() {
    const asphalt = new THREE.MeshStandardMaterial({ color: 0x2b2d31, roughness: 0.9 });
    const tex = new THREE.TextureLoader().load("models/textures/asphalt_col.webp", t => { t.wrapS = t.wrapT = THREE.RepeatWrapping; t.colorSpace = THREE.SRGBColorSpace; asphalt.color.set(0xffffff); asphalt.needsUpdate = true; });
    asphalt.map = tex;
    const white = new THREE.MeshStandardMaterial({ color: 0xf2f2ee, roughness: 0.6 });
    const yellow = new THREE.MeshStandardMaterial({ color: 0xf2c230, roughness: 0.6 });
    const rail = new THREE.MeshStandardMaterial({ color: 0xb9bec4, roughness: 0.35, metalness: 0.8 });
    const conc = new THREE.MeshStandardMaterial({ color: 0x8d8f8c, roughness: 0.9 });
    const colGeos = [];
    // polyline -> ribbon helper (points in three coords on XZ, y given)
    const ribbon = (pts, w, y, mat, closed, uvScale = 8, addCol = true, thick = 0) => {
      const pos = [], uv = [], idx = []; let acc = 0;
      const n = pts.length;
      for (let i = 0; i < n; i++) {
        const p = pts[i], q = pts[(i + 1) % n], o = pts[(i - 1 + n) % n];
        const a = closed || (i > 0 && i < n - 1) ? q.clone().sub(o) : (i === 0 ? q.clone().sub(p) : p.clone().sub(o));
        a.y = 0; a.normalize();
        const nrm = new THREE.Vector3(-a.z, 0, a.x).multiplyScalar(w / 2);
        if (i > 0) acc += p.distanceTo(pts[i - 1]);
        pos.push(p.x + nrm.x, y, p.z + nrm.z, p.x - nrm.x, y, p.z - nrm.z);
        uv.push(0, acc / uvScale, w / uvScale, acc / uvScale);
      }
      const m = closed ? n : n - 1;
      for (let i = 0; i < m; i++) {
        const a = i * 2, b = ((i + 1) % n) * 2;
        idx.push(a, a + 1, b, a + 1, b + 1, b);
      }
      const g = new THREE.BufferGeometry();
      g.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3));
      g.setAttribute("uv", new THREE.Float32BufferAttribute(uv, 2));
      g.setIndex(idx); g.computeVertexNormals();
      const mesh = new THREE.Mesh(g, mat); mesh.receiveShadow = true; this.root.add(mesh);
      if (addCol) colGeos.push(g);
      return g;
    };
    const offset = (pts, d, closed) => pts.map((p, i) => {
      const n = pts.length, q = pts[(i + 1) % n], o = pts[(i - 1 + n) % n];
      const a = (closed || (i > 0 && i < n - 1) ? q.clone().sub(o) : (i === 0 ? q.clone().sub(p) : p.clone().sub(o)));
      a.y = 0; a.normalize();
      return new THREE.Vector3(p.x - a.z * d, p.y, p.z + a.x * d);
    });
    const dashes = (pts, closed, mat, y, len = 3, gap = 6, w = 0.15) => {
      // dashed centre line as many small quads (one geometry)
      const segs = []; let carry = 0;
      const n = closed ? pts.length : pts.length - 1;
      for (let i = 0; i < n; i++) {
        const a = pts[i], b = pts[(i + 1) % pts.length], L = a.distanceTo(b);
        let t = carry;
        while (t < L) { segs.push([a.clone().lerp(b, t / L), a.clone().lerp(b, Math.min(L, t + len) / L)]); t += len + gap; }
        carry = t - L;
      }
      const pos = [];
      for (const [p, q] of segs) {
        const d = q.clone().sub(p).normalize(); const nn = new THREE.Vector3(-d.z, 0, d.x).multiplyScalar(w / 2);
        pos.push(p.x + nn.x, y, p.z + nn.z, p.x - nn.x, y, p.z - nn.z, q.x + nn.x, y, q.z + nn.z,
                 p.x - nn.x, y, p.z - nn.z, q.x - nn.x, y, q.z - nn.z, q.x + nn.x, y, q.z + nn.z);
      }
      const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3)); g.computeVertexNormals();
      this.root.add(new THREE.Mesh(g, mat));
    };
    const Y = ROAD_Z;
    // --- ring road
    const ring = [];
    for (let i = 0; i < 360; i++) { const [x, y] = superellipse(i / 360 * Math.PI * 2, RING_D); ring.push(B2T(x, y, Y)); }
    ribbon(ring, 12, Y, asphalt, true);
    dashes(ring, true, yellow, Y + 0.012, 4, 4);
    for (const s of [-1, 1]) { const e = offset(ring, s * 5.7, true); dashes(e, true, white, Y + 0.012, 1000, 0.01, 0.15); }
    this.ring = ring;
    // --- connectors: extend every avenue end that stops short of the ring road (Blender coords)
    const rx = y => ISL[0] * RING_D * Math.max(0, 1 - (Math.abs(y) / (ISL[1] * RING_D)) ** 4) ** 0.25;
    const ry = x => ISL[1] * RING_D * Math.max(0, 1 - (Math.abs(x) / (ISL[0] * RING_D)) ** 4) ** 0.25;
    for (const [ax, c, a1, a2] of this.roads) {
      for (const e of [a1, a2]) {
        const lim = ax === "x" ? rx(c) : ry(c), sgn = Math.sign(e);
        if (Math.abs(e) < lim - 1 && Math.abs(e) > 30) {
          const a = ax === "x" ? [e, c] : [c, e], b = ax === "x" ? [sgn * (lim + 1), c] : [c, sgn * (lim + 1)];
          ribbon([B2T(a[0], a[1], Y), B2T(b[0], b[1], Y)], 8, Y - 0.005, asphalt, false);
        }
      }
    }
    // --- causeway: from the ring's east point 3 km out to sea + turnaround loop
    const x0 = ISL[0] * RING_D - 2, x1 = 3200;
    const cw = [];
    for (let x = x0; x <= x1; x += 25) cw.push(B2T(x, 0, Y));
    ribbon(cw, 16, Y, asphalt, false, 8);
    dashes(cw, false, white, Y + 0.012, 6, 9, 0.18);
    for (const s of [-1, 1]) dashes(offset(cw, s * 7.6, false), false, white, Y + 0.012, 1000, 0.01, 0.2);
    // deck + piers + guard rails (rails are collidable)
    const deck = new THREE.Mesh(new THREE.BoxGeometry(x1 - 215, 0.8, 18), conc); deck.position.copy(B2T((x1 + 215) / 2, 0, Y - 0.45)); this.root.add(deck);
    const pierG = new THREE.CylinderGeometry(0.9, 1.1, 8, 10); const piers = new THREE.InstancedMesh(pierG, conc, Math.ceil((x1 - 220) / 40));
    for (let k = 0, x = 220; x < x1; x += 40, k++) piers.setMatrixAt(k, new THREE.Matrix4().makeTranslation(...B2T(x, 0, -4.2).toArray()));
    this.root.add(piers);
    for (const s of [-1, 1]) {
      const g = new THREE.BoxGeometry(x1 - x0 - 30, 0.9, 0.25); const m = new THREE.Mesh(g, rail);
      m.position.copy(B2T((x0 + 30 + x1) / 2, s * 8.2, Y + 0.45)); m.castShadow = true; this.root.add(m);
      const cg = g.clone(); cg.translate(m.position.x, m.position.y, m.position.z); colGeos.push(cg);
    }
    // turnaround loop at the far end
    const loop = [];
    for (let i = 0; i <= 72; i++) { const a = Math.PI / 2 - i / 72 * Math.PI * 2; loop.push(B2T(x1 + 70 + Math.cos(a + Math.PI) * 70 + 70 - 70, Math.sin(a) * 70 * 0 + 0, Y)); }
    const loop2 = [];
    for (let i = 0; i < 96; i++) { const a = i / 96 * Math.PI * 2; loop2.push(B2T(x1 + 80 + Math.cos(a) * 80, Math.sin(a) * 80, Y)); }
    ribbon(loop2, 16, Y, asphalt, true);
    const pad = new THREE.Mesh(new THREE.CylinderGeometry(92, 92, 0.8, 64), conc); pad.position.copy(B2T(x1 + 80, 0, Y - 0.45)); this.root.add(pad);
    const padTop = new THREE.CylinderGeometry(88, 88, 0.02, 64); padTop.translate(...B2T(x1 + 80, 0, Y - 0.02).toArray()); colGeos.push(padTop);
    this.root.add(new THREE.Mesh(padTop, new THREE.MeshStandardMaterial({ color: 0x3a6b3a, roughness: 1 })));
    // overhead gantry signs every 500 m
    for (let x = 500; x < x1; x += 500) this.gantry(B2T(x, 0, Y), `${(x / 1000).toFixed(1)} km`);
    return colGeos;
  }

  gantry(p, txt) {
    const g = new THREE.Group(); g.position.copy(p);
    const mat = new THREE.MeshStandardMaterial({ color: 0x777b80, metalness: 0.7, roughness: 0.4 });
    for (const s of [-1, 1]) { const post = new THREE.Mesh(new THREE.BoxGeometry(0.3, 7, 0.3), mat); post.position.set(0, 3.5, s * 8.6); g.add(post); }
    const beam = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.4, 17.6), mat); beam.position.set(0, 7, 0); g.add(beam);
    const sign = new THREE.Mesh(new THREE.PlaneGeometry(6, 1.6), new THREE.MeshBasicMaterial({ map: this.textTex(["CAUSEWAY  海上快速道路", txt], 768, 200, "#1f6b3a"), side: THREE.DoubleSide }));
    sign.position.set(-0.25, 6.2, 0); sign.rotation.y = -Math.PI / 2; g.add(sign);
    this.root.add(g);
  }

  // ------------------------------------------------------------- doors (auto open when the player is near)
  registerDoors(root, rec) {
    root.updateMatrixWorld(true);
    root.traverse(o => {
      const u = o.userData || {};
      if (!u.openable || !o.name.startsWith("D_")) return;
      const box = new THREE.Box3().setFromObject(o); const c = box.getCenter(new THREE.Vector3());
      let off = null;
      if (u.open_offset) { const v = typeof u.open_offset === "string" ? JSON.parse(u.open_offset) : u.open_offset; off = B2T(v[0], v[1], v[2]); }
      this.doors.push({ o, type: u.openable, center: c, rot0: o.rotation.y, pos0: o.position.clone(),
                        ang: THREE.MathUtils.degToRad(u.open_angle || 85), off, t: 0 });
    });
  }

  updateDoors(dt, actorPos) {
    for (const d of this.doors) {
      const near = actorPos && d.center.distanceToSquared(actorPos) < 2.6 * 2.6;
      const target = near ? 1 : 0;
      if (d.t === target) continue;
      d.t = THREE.MathUtils.clamp(d.t + (target ? 1 : -1) * dt * 2.2, 0, 1);
      const e = d.t * d.t * (3 - 2 * d.t);
      if (d.type === "hinge") d.o.rotation.y = d.rot0 + d.ang * e;
      else if (d.off) d.o.position.copy(d.pos0).addScaledVector(d.off, e);
    }
  }

  // ------------------------------------------------------------- name labels (canvas sprites, cheap)
  textTex(lines, w = 1024, h = 256, bg = "rgba(8,10,20,0.82)") {
    const c = document.createElement("canvas"); c.width = w; c.height = h; const x = c.getContext("2d");
    x.fillStyle = bg; x.fillRect(0, 0, w, h);
    x.strokeStyle = "#5ff"; x.lineWidth = 6; x.strokeRect(3, 3, w - 6, h - 6);
    x.fillStyle = "#fff"; x.textAlign = "center"; x.textBaseline = "middle";
    x.font = `bold ${Math.round(h * 0.34)}px "Microsoft JhengHei","Noto Sans TC",sans-serif`; x.fillText(lines[0], w / 2, h * 0.36);
    if (lines[1]) { x.fillStyle = "#9ff"; x.font = `${Math.round(h * 0.2)}px "Microsoft JhengHei","Noto Sans TC",sans-serif`; x.fillText(lines[1], w / 2, h * 0.74); }
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return t;
  }
  addLabel(rec) {
    const tex = this.textTex([`${rec.name_zh}  ${rec.name_en}`, `${rec.style_zh} · ${rec.style}  |  ${rec.tier}`]);
    const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: tex, depthWrite: false, transparent: true }));
    const h = (rec.size && rec.size[2]) || 10;
    sp.position.copy(B2T(rec.pos[0], rec.pos[1], rec.pos[2] + h + 3));
    sp.scale.set(12, 3, 1); sp.renderOrder = 5;
    this.root.add(sp); rec.label = sp; this.labels.push(sp);
  }

  // ------------------------------------------------------------- per-frame: interiors, labels
  update(dt, actorPos, camPos) {
    this.updateDoors(dt, actorPos);
    // doors are separate (animated) draw calls: only show the ones near the camera
    this._doorTick = (this._doorTick || 0) + 1;
    if (this._doorTick % 15 === 0) for (const d of this.doors) d.o.visible = d.center.distanceToSquared(camPos) < 85 * 85;
    for (const b of this.buildings) {
      const d = b.p.distanceTo(camPos);
      if (b.label) {
        b.label.visible = this.godLabels ? true : d < 260;
        const s = this.godLabels ? THREE.MathUtils.clamp(d / 110, 0.5, 4) : THREE.MathUtils.clamp(d / 40, 0.6, 3);
        if (this.godLabels) b.label.visible = d < 520;
        b.label.scale.set(12 * s, 3 * s, 1);
      }
      const want = d < 70 && !this.godLabels;
      if (want && !b.interior && b.interiorUrl && !b.loadingInt) {
        b.loadingInt = true;
        loader.loadAsync("models/" + b.interiorUrl + this.v).then(g => { this.prepVisual(g.scene); this.root.add(g.scene); b.interior = g.scene; })
          .catch(e => console.warn(e));
      }
      if (b.interior) b.interior.visible = d < 90;
    }
  }

  nearestBuilding(p) {
    let best = null, bd = 1e9;
    for (const b of this.buildings) {
      const s = b.size || [10, 10, 10];
      const r = Math.max(s[0], s[1]) * 0.5 + 2;
      const d = Math.hypot(b.p.x - p.x, b.p.z - p.z);
      if (d < r && d < bd) { bd = d; best = b; }
    }
    return best;
  }

  // ------------------------------------------------------------- sky / sea / lights / day-night
  setupSky() {
    const s = this.scene;
    this.sky = new Sky(); this.sky.scale.setScalar(45000); s.add(this.sky);
    const u = this.sky.material.uniforms;
    u.turbidity.value = 6; u.rayleigh.value = 1.6; u.mieCoefficient.value = 0.004; u.mieDirectionalG.value = 0.85;
    this.sun = new THREE.DirectionalLight(0xfff1dc, 3.2); this.sun.castShadow = true;
    this.sun.shadow.mapSize.set(2048, 2048); const c = this.sun.shadow.camera; c.left = c.bottom = -70; c.right = c.top = 70; c.near = 1; c.far = 400;
    this.sun.shadow.bias = -0.0004; this.sun.shadow.normalBias = 0.04;
    s.add(this.sun); s.add(this.sun.target);
    this.hemi = new THREE.HemisphereLight(0xcfe3ff, 0x5d5446, 1.1); s.add(this.hemi);
    s.fog = new THREE.Fog(0xa9c4dc, 300, 2600);
    this.stars = this.makeStars(); s.add(this.stars);
    this.setNight(false);
  }
  makeStars() {
    const n = 2500, p = new Float32Array(n * 3);
    for (let i = 0; i < n; i++) { const th = Math.random() * Math.PI * 2, ph = Math.acos(Math.random() * 0.9 + 0.1); p.set([Math.cos(th) * Math.sin(ph) * 4000, Math.cos(ph) * 4000, Math.sin(th) * Math.sin(ph) * 4000], i * 3); }
    const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.BufferAttribute(p, 3));
    return new THREE.Points(g, new THREE.PointsMaterial({ color: 0xffffff, size: 2, sizeAttenuation: false, fog: false }));
  }
  setupSea() {
    const c = document.createElement("canvas"); c.width = c.height = 256; const x = c.getContext("2d"); const img = x.createImageData(256, 256);
    for (let i = 0; i < 256 * 256; i++) { const v = 128 + (Math.random() - 0.5) * 40; img.data.set([v, v, 255, 255], i * 4); }
    x.putImageData(img, 0, 0);
    const nt = new THREE.CanvasTexture(c); nt.wrapS = nt.wrapT = THREE.RepeatWrapping; nt.repeat.set(400, 400);
    this.seaMat = new THREE.MeshPhysicalMaterial({ color: 0x1c4e6e, roughness: 0.12, metalness: 0.0, normalMap: nt, normalScale: new THREE.Vector2(0.15, 0.15), clearcoat: 0.6 });
    const sea = new THREE.Mesh(new THREE.PlaneGeometry(16000, 16000), this.seaMat);
    sea.rotation.x = -Math.PI / 2; sea.position.y = -0.62; sea.receiveShadow = true; this.scene.add(sea); this.sea = sea;
  }
  setNight(on) {
    this.night = on;
    const u = this.sky.material.uniforms;
    const elev = on ? -6 : 38, az = 210;
    const sp = new THREE.Vector3().setFromSphericalCoords(1, THREE.MathUtils.degToRad(90 - elev), THREE.MathUtils.degToRad(az));
    u.sunPosition.value.copy(sp);
    this.sunDir = on ? new THREE.Vector3(0.4, 0.8, 0.3).normalize() : sp.clone();
    this.sun.intensity = on ? 0.25 : 3.2; this.sun.color.set(on ? 0x8fa8ff : 0xfff1dc);
    this.hemi.intensity = on ? 0.18 : 1.1;
    this.scene.fog.color.set(on ? 0x0a1022 : 0xa9c4dc);
    this.stars.visible = on; this.sky.visible = !on;
    this.scene.background = on ? new THREE.Color(0x060a18) : null;
    this.renderer.toneMappingExposure = on ? 0.9 : 0.75;
    for (const m of this.emissiveMats) m.emissiveIntensity = (m.userData.baseEI || 1) * (on ? 1.1 : 0.5);
    for (const m of this.glassMats) { m.emissive = m.emissive || new THREE.Color(); m.emissive.set(on ? 0xffb066 : 0x000000); m.emissiveIntensity = on ? 0.35 : 0; }
    if (this.seaMat) this.seaMat.color.set(on ? 0x081a28 : 0x1c4e6e);
  }
  followSun(p) {
    this.sun.position.copy(p).addScaledVector(this.sunDir, 160); this.sun.target.position.copy(p);
    if (this.sea) this.sea.material.normalMap.offset.x += 0.00002;
  }
}
export { B2T };
