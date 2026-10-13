# Build the TownKit island (or a subset) headless:
#   blender -b --factory-startup -P build.py -- [--only apt_urban_5f,cafe_container] [--out file.blend] [--day] [--nolabels]
import bpy, os, sys, json, time
SD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(SD, ".."))
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def arg(k, d=None):
    return argv[argv.index(k) + 1] if k in argv else d
ONLY = arg("--only"); ONLY = set(ONLY.split(",")) if ONLY else None
OUT = arg("--out", os.path.join(ROOT, "TownKit.blend"))
NIGHT = "--day" not in argv
ENV = "--noenv" not in argv

# (module file, plot location (x, y, z), rotation deg). Rotation 0 = front faces -Y (south), 180 = faces +Y.
LAYOUT = [
    ("b_apt_urban_5f.py",       (-26.0, 14.3, 0.15), 0),
    ("b_house_teal_lantern.py", (-55.0, -18.5, 0.15), 180),
    ("b_tower_cyber_narrow.py", (44.0, 12.5, 0.15), 0),
    ("b_cafe_container.py",     (85.0, 15.6, 0.15), 0),
    ("b_house_eastasian_tile.py", (-82.0, -17.5, 0.15), 180),
    ("b_apt_block_6f.py",       (-50.0, 14.6, 0.15), 0),
    ("b_office_glass_tower.py", (20.0, 20.5, 0.15), 0),
    ("b_villa_luxury_modern.py", (-82.0, 19.0, 0.15), 0),
    ("b_villa_neon_circuit.py", (26.0, -20.5, 0.15), 180),
    ("b_shop_neon_corner.py",   (62.5, 14.6, 0.15), 0),
    ("b_pod_solar.py",          (56.0, -17.0, 0.15), 180),
    ("b_station_arctic.py",     (-2.0, 86.0, 7.0), 0),
    ("b_canal_twin_tower.py",   (237.0, -190.0, 0.15), 180),
    ("b_temple_pagoda.py",      (-28.0, -27.0, 0.15), 180),
]

def ns():
    g = {"LIB": os.path.join(SD, "lib_core.py"), "__name__": "__tk__", "ROOT": ROOT, "SD": SD}
    for f in ("lib_core.py", "lib_town.py", "lib_furn.py", "world.py", "lib_gen.py"):
        exec(compile(open(os.path.join(SD, f), encoding="utf8").read(), f, "exec"), g)
    g["tk_materials"]()
    return g

def clear():
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    for c in list(bpy.data.collections):
        bpy.data.collections.remove(c)

t0 = time.time()
clear()
g = ns()
g["LABELS_ON"] = "--nolabels" not in argv
g["setup_render"](NIGHT)
if ENV:
    g["build_island"]()
    g["end_building"]((0, 0, 0), 0, bevel_kinds=("furniture",))
for f, loc, rot in LAYOUT:
    bid = f[2:-3]
    if ONLY and bid not in ONLY and "v1" not in ONLY:
        continue
    t1 = time.time()
    g2 = dict(g); g2["PLOT"] = (loc, rot)      # private namespace: building vars can't clobber the libs
    exec(compile(open(os.path.join(SD, f), encoding="utf8").read(), f, "exec"), g2)
    g["end_building"](loc, rot)
    print("   built %s in %.1fs" % (bid, time.time() - t1))
# ---------------------------------------------------------------- v2 districts (auto-placed along avenues)
DISTRICTS = ["d1_world.py", "d2_civic.py", "d3_commerce.py", "d4_modern.py", "d5_fantasy.py",
             "d6_asia.py", "d7_west.py", "d8_future.py", "d9_legend.py"]
from mathutils import Vector
def world_rect(root):
    pts = []
    for o in g["_all_children"](root):
        if o.type == "MESH" and o.get("kind") not in ("label", "cable", "collider"):
            pts += [o.matrix_world @ Vector(c) for c in o.bound_box]
    return (min(p.x for p in pts), min(p.y for p in pts), max(p.x for p in pts), max(p.y for p in pts))
occ = [world_rect(o) for o in bpy.data.objects if o.name.startswith("BLD_") and o.type == "EMPTY"]
for (ax, c, a1, a2) in g["ROADS"]:
    occ.append((a1, c - 7.2, a2, c + 7.2) if ax == "x" else (c - 7.2, a1, c + 7.2, a2))
def free(r):
    for q in occ:
        if r[0] < q[2] - 0.01 and r[2] > q[0] + 0.01 and r[1] < q[3] - 0.01 and r[3] > q[1] + 0.01:
            return False
    H = g["HILL"]; hi = g["h_island"]
    for px in (r[0], (r[0] + r[2]) / 2, r[2]):
        for py in (r[1], (r[1] + r[3]) / 2, r[3]):
            if abs(hi(px, py)) > 0.02:
                return False
    cx, cy = max(r[0], min(H[0], r[2])), max(r[1], min(H[1], r[3]))
    return ((cx - H[0]) ** 2 + (cy - H[1]) ** 2) ** 0.5 > H[3] + 2
ROWS = []      # (avenue y, side) ; side +1 = north of the avenue (faces south, rot 0)
for (ax, c, a1, a2) in g["ROADS"]:
    if ax == "x":
        ROWS += [(c, 1, a1, a2), (c, -1, a1, a2)]
for fn in DISTRICTS:
    p_ = os.path.join(SD, fn)
    if os.path.exists(p_):
        exec(compile(open(p_, encoding="utf8").read(), fn, "exec"), g)
placed = {}
for bid, R_ in g["REG"].items():
    if ONLY and bid not in ONLY and "v2" not in ONLY:
        continue
    pos = None
    for (cy, side, a1, a2) in ROWS:
        x = a1 + R_["pw"] / 2 + 1
        while x < a2 - R_["pw"] / 2 - 1 and pos is None:
            if side > 0:
                Y = cy + 7.3 + R_["front"]; rect = (x - R_["pw"] / 2, cy + 7.3, x + R_["pw"] / 2, Y + R_["back"])
            else:
                Y = cy - 7.3 - R_["front"]; rect = (x - R_["pw"] / 2, Y - R_["back"], x + R_["pw"] / 2, cy - 7.3)
            if free(rect):
                pos = ((x, Y, 0.15), 0 if side > 0 else 180, rect)
            x += 2.0
        if pos: break
    if pos is None:
        print("!! no plot for", bid); continue
    occ.append(pos[2])
    t1 = time.time()
    g["PLOT"] = (pos[0], pos[1])
    try:
        R_["fn"]()
        g["end_building"](pos[0], pos[1])
        print("   built %s at %s rot %d in %.1fs" % (bid, tuple(round(v, 1) for v in pos[0]), pos[1], time.time() - t1))
    except Exception as e:
        import traceback; traceback.print_exc(); print("!! FAILED", bid, e)
g["set_lights_mode"](NIGHT)
bpy.context.scene["tk_roads"] = json.dumps(g["ROADS"]); bpy.context.scene["tk_isl"] = json.dumps(g["ISL"])
with open(os.path.join(ROOT, "export", "catalog_build.json"), "w", encoding="utf8") as fp:
    json.dump(g["BUILDINGS"], fp, ensure_ascii=False, indent=1)
bpy.ops.wm.save_as_mainfile(filepath=OUT)
print("saved", OUT, "in %.1fs" % (time.time() - t0))
