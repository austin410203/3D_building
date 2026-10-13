# TownKit v2: parametric building generator + extra furniture + bespoke-shape helpers.
# exec'd after lib_core / lib_town / lib_furn in the same namespace.
import math, json, random
from mathutils import Vector, Matrix

# ============================================================== extra furniture
def pew(x, y, z=0, rot=0, w=2.4, m="WoodDark"):
    mb = MB()
    mb.box(-w / 2, -0.22, 0.42, w / 2, 0.22, 0.47, m); mb.box(-w / 2, 0.18, 0.47, w / 2, 0.24, 0.95, m)
    for sx in (-w / 2, w / 2 - 0.05):
        mb.box(sx, -0.25, 0, sx + 0.05, 0.25, 0.95, m)
    o = furn("Pew", mb, x, y, z, rot, "sit"); o["use_points"] = json.dumps([[u, 0, 0.47] for u in (-w / 3, 0, w / 3)])
    return o

def exam_bed(x, y, z=0, rot=0):
    mb = MB()
    mb.box(-0.35, -0.95, 0, 0.35, 0.95, 0.65, "Chrome") if False else None
    for sx in (-0.3, 0.3):
        for sy in (-0.85, 0.85):
            mb.cyl(sx, sy, 0, 0.65, 0.025, "Chrome", seg=8)
    mb.box(-0.38, -1.0, 0.65, 0.38, 1.0, 0.78, "LeatherBlack"); mb.box(-0.38, 0.55, 0.78, 0.38, 1.0, 0.95, "LeatherBlack")
    mb.box(-0.4, -1.05, 0.78, 0.4, -0.9, 0.8, "Paper")
    return furn("ExamBed", mb, x, y, z, rot, "sleep")

def hospital_bed(x, y, z=0, rot=0):
    mb = MB()
    for sx in (-0.42, 0.42):
        for sy in (-0.95, 0.95):
            mb.cyl(sx, sy, 0.05, 0.5, 0.025, "Chrome", seg=8); mb.cyl(sx, sy, 0, 0.08, 0.05, "Rubber", seg=8)
    mb.box(-0.45, -1.0, 0.5, 0.45, 1.0, 0.68, "Mattress"); mb.box(-0.45, 0.95, 0.5, 0.45, 1.05, 1.1, "White")
    mb.box(-0.47, -0.4, 0.68, -0.44, 0.6, 0.9, "Chrome"); mb.box(0.44, -0.4, 0.68, 0.47, 0.6, 0.9, "Chrome")
    mb.box(-0.43, -0.98, 0.68, 0.43, 0.3, 0.72, "FabricBlue")
    mb.cyl(0.7, 0.9, 0, 1.9, 0.015, "Chrome", seg=6); mb.box(0.62, 0.86, 1.6, 0.78, 0.9, 1.85, "GlassFrost")
    return furn("HospitalBed", mb, x, y, z, rot, "sleep")

def treadmill(x, y, z=0, rot=0):
    mb = MB()
    mb.box(-0.4, -0.9, 0, 0.4, 0.9, 0.22, "PlasticDark"); mb.box(-0.32, -0.85, 0.22, 0.32, 0.85, 0.24, "Rubber")
    for sx in (-0.38, 0.38):
        mb.box(sx - 0.03, 0.75, 0.2, sx + 0.03, 0.85, 1.3, "MetalDark")
    mb.box(-0.4, 0.6, 1.2, 0.4, 0.9, 1.35, "PlasticDark"); mb.box(-0.2, 0.62, 1.3, 0.2, 0.7, 1.45, "Screen")
    return furn("Treadmill", mb, x, y, z, rot, "use")

def weight_bench(x, y, z=0, rot=0):
    mb = MB()
    mb.box(-0.15, -0.6, 0.4, 0.15, 0.6, 0.48, "LeatherBlack"); mb.box(-0.05, -0.5, 0, 0.05, 0.5, 0.4, "MetalDark")
    for sx in (-0.55, 0.55):
        mb.box(sx - 0.03, 0.4, 0, sx + 0.03, 0.5, 1.2, "MetalDark")
    mb.cyl(-0.9, 0.45, 1.1, 1.1, 0.012, "Chrome", seg=8, axis="x") if False else mb.box(-0.9, 0.43, 1.08, 0.9, 0.47, 1.12, "Chrome")
    for sx in (-0.75, 0.75):
        mb.cyl(sx, 0.45, 1.1, 1.1, 0.2, "Black", seg=16, axis="x") if False else mb.box(sx - 0.03, 0.3, 0.95, sx + 0.03, 0.6, 1.25, "Black")
    return furn("WeightBench", mb, x, y, z, rot, "use")

def school_desk(x, y, z=0, rot=0, chair_=True):
    mb = MB()
    mb.box(-0.35, -0.25, 0.7, 0.35, 0.25, 0.73, "WoodLight")
    for sx in (-0.32, 0.32):
        mb.box(sx - 0.02, -0.22, 0, sx + 0.02, 0.22, 0.7, "MetalDark")
    mb.box(-0.32, -0.2, 0.55, 0.32, 0.22, 0.57, "MetalDark")
    o = furn("SchoolDesk", mb, x, y, z, rot, "work")
    if chair_:
        ca = math.radians(rot)
        chair(x + 0.5 * math.sin(ca), y - 0.5 * math.cos(ca), z, rot + 180, "WoodLight", "PlasticBlue", 0.44)
    return o

def whiteboard(x, y, z, rot=0, w=2.4):
    mb = MB(); mb.box(-w / 2, 0, 0, w / 2, 0.03, 1.2, "FrameAlu"); mb.box(-w / 2 + 0.04, -0.005, 0.04, w / 2 - 0.04, 0, 1.16, "White")
    mb.box(-w / 2, -0.08, -0.03, w / 2, 0.03, 0.0, "FrameAlu")
    return furn("Whiteboard", mb, x, y, z, rot, "use")

def workbench(x, y, z=0, rot=0, w=2.0):
    mb = MB()
    mb.box(-w / 2, -0.35, 0.85, w / 2, 0.35, 0.92, "WoodLight")
    for sx in (-w / 2 + 0.05, w / 2 - 0.1):
        for sy in (-0.3, 0.25):
            mb.box(sx, sy, 0, sx + 0.06, sy + 0.06, 0.85, "MetalDark")
    mb.box(-w / 2, -0.32, 0.25, w / 2, 0.32, 0.28, "WoodLight")
    mb.box(-w / 2, 0.3, 0.92, w / 2, 0.35, 1.8, "WoodDark")
    for i in range(6):
        mb.box(-w / 2 + 0.2 + i * 0.3, 0.27, 1.2 + (i % 2) * 0.2, -w / 2 + 0.24 + i * 0.3, 0.3, 1.5 + (i % 2) * 0.2, RNG.choice(["MetalDark", "PlasticRed", "Chrome"]))
    mb.box(0.2, -0.2, 0.92, 0.6, 0.1, 1.1, "PlasticRed")
    return furn("Workbench", mb, x, y, z, rot, "work")

def oven(x, y, z=0, rot=0, w=1.4):
    mb = MB()
    mb.box(-w / 2, -0.45, 0, w / 2, 0.45, 1.7, "Metal")
    for q in (0.35, 0.95):
        mb.box(-w / 2 + 0.1, -0.46, q, w / 2 - 0.1, -0.45, q + 0.45, "GlassDark"); mb.box(-w / 2 + 0.1, -0.47, q + 0.38, w / 2 - 0.1, -0.46, q + 0.42, "NeonOrange")
    return furn("Oven", mb, x, y, z, rot, "cook")

def bread_display(x, y, z=0, rot=0, w=2.0):
    mb = MB()
    mb.box(-w / 2, -0.3, 0, w / 2, 0.3, 0.9, "WoodLight"); mb.box(-w / 2, -0.3, 0.9, w / 2, 0.3, 1.35, "Glass")
    for i in range(int(w / 0.18)):
        mb.sph(-w / 2 + 0.12 + i * 0.18, RNG.uniform(-0.15, 0.15), 0.98, 0.07, RNG.choice(["BookC", "Terracotta", "WoodLight"]), sx=1.4)
    return furn("BreadDisplay", mb, x, y, z, rot, "shop")

def bunk(x, y, z=0, rot=0, fab="FabricNavy"):
    mb = MB()
    for zz in (0.25, 1.35):
        mb.box(-0.45, -1.0, zz, 0.45, 1.0, zz + 0.12, "MetalDark"); mb.box(-0.43, -0.98, zz + 0.12, 0.43, 0.98, zz + 0.3, "Mattress")
        mb.box(-0.43, -0.98, zz + 0.3, 0.43, 0.3, zz + 0.38, fab)
    for (sx, sy) in ((-0.45, -1.0), (0.4, -1.0), (-0.45, 0.95), (0.4, 0.95)):
        mb.box(sx, sy, 0, sx + 0.05, sy + 0.05, 2.0, "MetalDark")
    return furn("BunkBed", mb, x, y, z, rot, "sleep")

def piano(x, y, z=0, rot=0):
    mb = MB()
    mb.box(-0.75, -0.1, 0, 0.75, 0.3, 1.25, "Black"); mb.box(-0.75, -0.35, 0.7, 0.75, -0.1, 0.78, "Black")
    mb.box(-0.7, -0.33, 0.78, 0.7, -0.12, 0.8, "White")
    mb.box(-0.4, -0.85, 0.45, 0.4, -0.55, 0.5, "Black")
    return furn("Piano", mb, x, y, z, rot, "play")

def fireplace(x, y, z=0, rot=0, m="Brick"):
    mb = MB()
    mb.box(-0.9, -0.3, 0, 0.9, 0.3, 1.2, m); mb.box(-1.0, -0.38, 1.2, 1.0, 0.3, 1.3, "WoodDark")
    mb.box(-0.5, -0.31, 0.1, 0.5, 0.1, 0.75, "Black"); mb.box(-0.35, -0.2, 0.12, 0.35, 0.0, 0.35, "NeonOrange")
    return furn("Fireplace", mb, x, y, z, rot, "use")

def rope_posts(x, y, z=0, rot=0, w=3.0):
    mb = MB()
    for i in range(4):
        u = -w / 2 + w * i / 3
        mb.cyl(u, 0, 0, 0.03, 0.15, "Brass", seg=12); mb.cyl(u, 0, 0.03, 0.95, 0.025, "Brass", seg=8)
    mb.box(-w / 2, -0.015, 0.85, w / 2, 0.015, 0.88, "FabricRed")
    return furn("RopePosts", mb, x, y, z, rot)

def gas_pump(x, y, z=0, rot=0):
    mb = MB(); mb.box(-0.4, -0.25, 0, 0.4, 0.25, 1.8, "White"); mb.box(-0.42, -0.27, 1.5, 0.42, 0.27, 1.9, "PlasticRed")
    mb.box(-0.25, -0.26, 1.0, 0.25, -0.25, 1.4, "Screen"); mb.box(0.4, -0.05, 0.5, 0.5, 0.05, 1.3, "Rubber")
    return furn("GasPump", mb, x, y, z, rot, "use")

def telescope(x, y, z=0, rot=0):
    mb = MB(); mb.cyl(0, 0, 0, 1.0, 0.25, "White", seg=16, r2=0.15)
    o = mb.obj("TelescopeBase_%d" % CUR.n, x, y, z, rot, kind="furniture")
    mb = MB(); mb.cyl(0, 0, 0, 2.6, 0.25, "White", seg=20, r2=0.22); mb.cyl(0, 0, 2.6, 2.7, 0.27, "Black", seg=20)
    t = mb.obj("TelescopeTube_%d" % CUR.n, x, y, z + 1.0, kind="furniture"); t.rotation_euler = (math.radians(-40), 0, math.radians(rot))
    t["interact"] = "use"
    return o

# ============================================================== room fills (canonical frame: door on the -v wall)
def fillroom(kind, x1, y1, x2, y2, z, h=2.8, door="S", light=True, var=0):
    if x2 - x1 < 1.4 or y2 - y1 < 1.4:
        return
    P, ra, W, D = _frame(x1, y1, x2, y2, door)
    def put(fn, u, v, r=0, *a, **k):
        if not (0 < u < W and 0 < v < D):
            return None
        px, py = P(u, v)
        return fn(px, py, z, (r + ra) % 360, *a, **k)
    lp = 1.0
    if kind in ("living", "bedroom", "kitchen", "bath", "studio", "office", "meeting", "storage"):
        room(kind, x1, y1, x2, y2, z, h, door, light)
        return
    if kind == "shop":
        rows = max(1, int((D - 2.4) / 1.6))
        for r_ in range(rows):
            for i in range(max(1, int((W - 1.2) / 2.0))):
                put(shelf_goods, 1.1 + i * 2.0, 2.2 + r_ * 1.6, 0, 1.8, 1.5, 0.6, double=True)
        put(shop_counter, W - 1.0, 1.2, 270, 1.6, "WoodDark", "Marble")
        put(drinks_fridge, 0.4, D - 0.6, 90, 1.0, 2.0) if D > 3 else None
    elif kind == "market":
        rows = max(1, int((D - 2.6) / 1.7))
        for r_ in range(rows):
            for i in range(max(1, int((W - 1.0) / 2.2))):
                put(shelf_goods, 1.2 + i * 2.2, 2.6 + r_ * 1.7, 0, 2.0, 1.6, 0.7, double=True)
        for i in range(max(1, int((W - 1) / 1.3))):
            put(drinks_fridge, 0.8 + i * 1.3, D - 0.4, 0, 1.2, 2.0)
        for i in range(2):
            put(shop_counter, 1.2 + i * 1.8, 0.9, 0, 1.2, "White", "PlasticDark")
    elif kind == "cafe":
        put(shop_counter, W / 2, D - 0.9, 0, min(3.0, W - 1), "WoodDark", "Marble")
        for i in range(max(1, int((W - 0.8) / 1.6))):
            for j in range(max(1, int((D - 2.6) / 1.6))):
                put(cafe_set, 0.9 + i * 1.6, 1.0 + j * 1.6, 0)
        put(plant, 0.4, D - 0.4, 0, 1.0, kind="tall")
    elif kind == "restaurant":
        for i in range(max(1, int((W - 0.6) / 2.2))):
            for j in range(max(1, int((D - 1.4) / 2.2))):
                put(dining_set, 1.2 + i * 2.2, 1.4 + j * 2.2, 0, 1.2, 0.8, "WoodDark")
    elif kind == "bar":
        put(bar_counter, W / 2, D - 1.2, 180, min(4.0, W - 1.2), "WoodDark", "WoodLight")
        put(bookshelf, W / 2, D - 0.2, 0, min(3.6, W - 1.2), 2.0, 0.3, "WoodDark", books=False)
        for i in range(max(1, int((W - 1) / 1.8))):
            put(round_table, 1.0 + i * 1.8, 1.0, 0, 0.35, 1.05, "WoodDark")
            put(stool, 0.6 + i * 1.8, 1.0, 0, 0.75); put(stool, 1.4 + i * 1.8, 1.0, 0, 0.75)
    elif kind == "lobby":
        put(reception, W / 2, D - 1.2, 180, min(3.2, W - 1.6))
        put(sofa, 0.6, D / 2, 90, min(2.4, D - 1.2), "LeatherBlack"); put(coffee_table, 1.6, D / 2, 90, 1.0, 0.5, "MarbleBlack")
        put(plant, 0.4, 0.5, 0, 1.3, kind="palm"); put(plant, W - 0.4, 0.5, 0, 1.3, kind="palm")
    elif kind == "office_open":
        room("office", x1, y1, x2, y2, z, h, door, light); return
    elif kind == "classroom":
        put(whiteboard, W / 2, D - 0.05, 0, min(3.2, W - 1), "z") if False else None
        px, py = P(W / 2, D - 0.04); whiteboard(px, py, z + 0.9, (0 + ra) % 360, min(3.2, W - 1))
        put(desk, W / 2, D - 1.2, 180, 1.2, 0.6, "WoodDark", pc=False, chair_=False)
        for i in range(max(1, int((W - 0.8) / 1.1))):
            for j in range(max(1, int((D - 2.6) / 1.1))):
                put(school_desk, 0.8 + i * 1.1, D - 2.3 - j * 1.1, 0)
    elif kind == "library":
        for i in range(max(1, int((W - 0.6) / 1.5))):
            put(bookshelf, 0.9 + i * 1.5, D - 0.2, 0, 1.4, 2.2)
        for j in range(max(0, int((D - 3.0) / 1.8))):
            put(bookshelf, W / 2 + 0.8, 2.0 + j * 1.8, 0, min(3.0, W / 2 - 0.5), 1.6, 0.5)
        put(table, W / 4, 1.4, 0, 1.6, 0.8, 0.75, "WoodDark"); put(chair, W / 4 - 0.4, 0.8, 180); put(chair, W / 4 + 0.4, 0.8, 180)
    elif kind == "gym":
        for i in range(max(1, int((W - 0.6) / 1.2))):
            put(treadmill, 0.8 + i * 1.2, D - 1.1, 0)
        for i in range(max(1, int((W - 1) / 2.0))):
            put(weight_bench, 1.2 + i * 2.0, 1.4, 0)
        put(rug, W / 2, D / 2 - 0.2, 0, max(1.0, W - 1.5), 1.2, "PlasticBlue")
    elif kind == "clinic":
        put(exam_bed, 0.6, D - 1.2, 0); put(desk, W - 0.6, D / 2, 270, 1.2, 0.6, pc=True)
        put(cabinet_low, 1.6, D - 0.25, 0, 1.2, 1.0, 0.4, "White"); put(chair, W - 1.6, D / 2, 90)
    elif kind == "ward":
        for i in range(max(1, int((W - 0.4) / 1.4))):
            put(hospital_bed, 0.8 + i * 1.4, D - 1.15, 0)
    elif kind == "hotel":
        bw = 1.6 if W >= 3.0 else 1.0
        put(bed, W / 2, D - 1.05, 0, bw, 2.0, RNG.choice(["FabricWhite", "FabricBeige", "FabricBlue"]))
        put(nightstand, W / 2 - bw / 2 - 0.28, D - 0.25, 0) if W > bw + 0.7 else None
        put(desk, W - 0.4, 1.6, 270, 1.0, 0.5, pc=False) if W > 2.6 and D > 3.2 else None
        put(armchair, 0.6, 1.3, 45) if W > 2.8 else None
    elif kind == "dorm":
        for i in range(max(1, int((W - 0.2) / 1.1))):
            put(bunk, 0.6 + i * 1.1, D - 1.05, 0)
    elif kind == "workshop":
        put(workbench, W / 2, D - 0.4, 0, min(3.0, W - 1.0))
        put(shelf_goods, 0.3, D / 2, 90, min(2.0, D - 1.2), 2.0, 0.5)
        put(crate, W - 0.7, 1.2, 10); put(barrel, W - 0.6, 2.2, 0, "Rust")
    elif kind == "garage":
        put(car, W / 2, D / 2, 0, RNG.choice(["PlasticRed", "PlasticBlue", "White", "PlasticDark"]))
        put(workbench, W / 2, D - 0.4, 0, min(2.4, W - 1.0)) if D > 6 else None
    elif kind == "chapel":
        for j in range(max(1, int((D - 3.0) / 1.0))):
            for sx in (-1, 1):
                put(pew, W / 2 + sx * (W / 4 + 0.3), 1.2 + j * 1.0, 0, max(1.2, W / 2 - 1.2))
        mb = MB(); mb.box(-0.8, -0.4, 0, 0.8, 0.4, 1.0, "Marble"); mb.box(-0.9, -0.45, 1.0, 0.9, 0.45, 1.05, "FabricWhite")
        mb.box(-0.03, 0.2, 1.05, 0.03, 0.26, 1.7, "Brass"); mb.box(-0.2, 0.2, 1.45, 0.2, 0.26, 1.5, "Brass")
        px, py = P(W / 2, D - 0.8); furn("Altar", mb, px, py, z, ra, "use")
    elif kind == "bank":
        put(shop_counter, W / 2, D - 1.3, 180, min(5.0, W - 1.0), "MarbleBlack", "Marble", register=True)
        put(rope_posts, W / 2, D - 2.5, 0, min(3.0, W - 2))
        put(sofa, 0.6, 1.4, 90, 1.8, "LeatherBlack"); put(plant, W - 0.4, 0.5, 0, 1.4, kind="palm")
    elif kind == "laundry":
        for i in range(max(1, int((W - 0.2) / 0.7))):
            put(washer, 0.45 + i * 0.7, D - 0.35, 0)
        put(bench, W / 2, 1.0, 180, min(2.0, W - 1))
    elif kind == "arcade":
        for i in range(max(1, int((W - 0.4) / 0.85))):
            put(arcade, 0.5 + i * 0.85, D - 0.45, 0, RNG.choice(["PlasticBlue", "PlasticRed", "PlasticDark"]),
                RNG.choice(["NeonPink", "NeonCyan", "NeonYellow", "NeonPurple"]))
        put(claw_machine, 0.6, 1.2, 0); put(vending, W - 0.6, 1.2, 270, "NeonBlue")
    elif kind == "bakery":
        put(bread_display, W / 2, 1.6, 0, min(2.6, W - 1.2)); put(oven, 0.9, D - 0.5, 0, 1.4)
        put(shelf_goods, W - 1.2, D - 0.3, 0, 1.6, 1.8, 0.4)
        put(cafe_set, W - 1.0, 0.8, 0) if W > 4 else None
    elif kind == "server":
        for i in range(max(1, int((W - 0.4) / 0.8))):
            put(server_rack, 0.5 + i * 0.8, D - 0.6, 0)
        put(console, W / 2, 1.0, 180, min(2.0, W - 0.8), 2)
    elif kind == "lounge":
        put(sofa, W / 2, D - 0.5, 0, min(2.6, W - 1.0), RNG.choice(["FabricNavy", "LeatherBlack", "FabricBeige"]))
        put(coffee_table, W / 2, D - 1.6, 0); put(armchair, 0.7, 1.0, 45); put(rug, W / 2, D - 1.6, 0, min(3, W - 1), 2.0)
        put(tv, W / 2, 0.25, 180, 1.4) if D > 4 else None
    elif kind == "dining":
        put(dining_set, W / 2, D / 2, 0, min(2.0, W - 1.6), 0.9, "WoodDark")
        put(cabinet_low, W / 2, D - 0.25, 0, min(2.0, W - 1), 0.85, 0.45, "WoodDark")
    elif kind == "forge":
        mb = MB(); mb.box(-0.8, -0.6, 0, 0.8, 0.6, 1.1, "BrickDark"); mb.box(-0.5, -0.61, 0.3, 0.5, -0.4, 0.8, "NeonOrange")
        mb.box(-0.3, -0.3, 1.1, 0.3, 0.3, 2.4, "BrickDark"); px, py = P(1.0, D - 0.7); furn("Furnace", mb, px, py, z, ra, "use")
        mb = MB(); mb.box(-0.15, -0.15, 0, 0.15, 0.15, 0.55, "WoodDark"); mb.box(-0.35, -0.12, 0.55, 0.35, 0.12, 0.75, "MetalDark")
        mb.cyl(0.35, 0, 0.62, 0.68, 0.1, "MetalDark", seg=8, r2=0.02); px, py = P(W / 2, D / 2); furn("Anvil", mb, px, py, z, ra, "use")
        put(workbench, W - 1.2, D - 0.4, 0, min(2.0, W - 1.6)); put(barrel, 0.5, 1.2, 0, "WoodLight")
        lamp("ForgeGlow", *P(1.0, D - 1.2), z + 1.0, 60, (1.0, 0.45, 0.15), kind="point", fixture=False)
    elif kind == "farm":
        for i in range(max(1, int((W - 0.4) / 1.2))):
            for j in range(max(1, int((D - 1.6) / 1.4))):
                mb = MB(); mb.box(-0.5, -0.25, 0, 0.5, 0.25, 2.0, "MetalDark")
                for k in range(4):
                    zz = 0.25 + k * 0.45
                    mb.box(-0.48, -0.23, zz, 0.48, 0.23, zz + 0.06, "White"); mb.sph(0, 0, zz + 0.14, 0.12, "PlantGreen", sx=3.6, sy=1.4, sz=0.7)
                    mb.box(-0.46, -0.21, zz + 0.38, 0.46, 0.21, zz + 0.4, "NeonPurple")
                px, py = P(0.8 + i * 1.2, D - 0.5 - j * 1.4); furn("FarmRack", mb, px, py, z, ra, "use")
    elif kind == "aquarium":
        for i in range(max(1, int((W - 0.4) / 2.2))):
            mb = MB(); mb.box(-1.0, -0.4, 0, 1.0, 0.4, 0.7, "PanelDark"); mb.box(-1.0, -0.4, 0.7, 1.0, 0.4, 2.2, "GlassBlue")
            mb.box(-0.95, -0.35, 0.72, 0.95, 0.35, 2.0, "PoolWater")
            for k in range(5):
                mb.sph(RNG.uniform(-0.8, 0.8), RNG.uniform(-0.2, 0.2), RNG.uniform(1.0, 1.9), 0.06, RNG.choice(["PlasticYellow", "PlasticRed", "NeonCyan"]), sx=2.0)
            px, py = P(1.2 + i * 2.2, D - 0.5); furn("FishTank", mb, px, py, z, ra, "use")
        lamp("AquaGlow", *P(W / 2, D - 1.0), z + 2.4, 50, (0.3, 0.7, 1.0), kind="point", fixture=False)
        put(bench, W / 2, 1.5, 180, min(2.4, W - 1))
    elif kind == "onsen":
        mb = MB(); mb.box(-1.4, -1.0, 0, 1.4, 1.0, 0.5, "Stone"); mb.box(-1.25, -0.85, 0.3, 1.25, 0.85, 0.46, "PoolWater")
        px, py = P(W / 2, D / 2 + 0.3); furn("HotSpring", mb, px, py, z, ra, "wash")
        put(bench, 1.2, 0.8, 180, 1.6, "WoodLight", "WoodDark")
    elif kind == "none":
        pass
    if light and kind != "none":
        cx, cy = P(W / 2, D / 2)
        lamp("FillL_%s" % kind, cx, cy, z + h, 60 if W * D < 14 else 110, kind="ceiling")

# ============================================================== transform block (rotated sub-assemblies)
def xblock(M, fn, *a, **k):
    """run fn() while recording new objects, then pre-multiply their world matrix by M"""
    before = set(o.name for o in CUR.col.objects) | set(o.name for o in CUR.lab.objects)
    res = fn(*a, **k)
    for coll_ in (CUR.col, CUR.lab):
        for o in list(coll_.objects):
            if o.name not in before and (o.parent is None or o.parent == CUR.root):
                o.matrix_basis = M @ o.matrix_basis      # root is identity during build
    return res

def place_at(x, y, z=0, rot=0):
    return Matrix.Translation((x, y, z)) @ Matrix.Rotation(math.radians(rot), 4, "Z")

# ============================================================== polygon (round) towers + spiral stairs
def _poly(r, n, phase=0.0):
    return [Vector((math.cos(phase + 2 * math.pi * i / n) * r, math.sin(phase + 2 * math.pi * i / n) * r, 0)) for i in range(n)]

def poly_wall(name, cx, cy, r, n, z1, z2, ext, intm="PlasterInt", t=0.3, ops=None, phase=None):
    """n-gon tower wall. ops = {segment_index: [(u1, u2, zb, zt, kind[, frame]), ...]} with u measured from the segment centre."""
    phase = math.pi / n if phase is None else phase
    pts = _poly(r, n, phase)
    ops = ops or {}
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        L = (b - a).length + t * math.tan(math.pi / n) * 2 + 0.02
        mid = (a + b) / 2
        ang = math.atan2((b - a).y, (b - a).x)
        M = Matrix.Translation((cx + mid.x, cy + mid.y, 0)) @ Matrix.Rotation(ang, 4, "Z")
        o = [(p[0], p[1], p[2], p[3]) for p in ops.get(i, [])]
        def build(i=i, o=o, L=L):
            # local frame: wall runs along x, outer face at y=0 facing -y?  CCW polygon -> outward is -y of (b-a) left normal
            w = wall(_nm("%s_Seg%d" % (name, i)), "x", -L / 2, L / 2, 0.0, t, z1, z2, intm, CUR.col, o)
            adopt(w, "wall")
            if ext != intm:
                w2 = wall(_nm("%s_Clad%d" % (name, i)), "x", -L / 2, L / 2, -0.03, 0.0, z1, z2, ext, CUR.col, o)
                adopt(w2, "wall")
            for j, p in enumerate(ops.get(i, [])):
                kind = p[4] if len(p) > 4 else "win"
                fill("%s_%d_%d" % (name, i, j), "S", -0.03, t, p[0], p[1], p[2], p[3], kind,
                     frame=p[5] if len(p) > 5 else "Frame")
        xblock(M, build)
    return pts


def disc_floor(name, cx, cy, r, n, z, t=0.2, hole_r=0.0, top="WoodFloor", under="Ceiling", phase=None, seg=None):
    """n-gon floor slab with an optional round hole (for spiral stairs)"""
    phase = math.pi / n if phase is None else phase
    seg = seg or max(n * 3, 24)
    bm = bmesh.new()
    def outer(a):
        # point on the polygon at angle a
        k = n
        best = None
        for i in range(k):
            p = Vector((math.cos(phase + 2 * math.pi * i / k), math.sin(phase + 2 * math.pi * i / k), 0)) * r
            q = Vector((math.cos(phase + 2 * math.pi * (i + 1) / k), math.sin(phase + 2 * math.pi * (i + 1) / k), 0)) * r
            d = Vector((math.cos(a), math.sin(a), 0))
            # ray-segment intersection
            e = q - p; den = d.x * e.y - d.y * e.x
            if abs(den) < 1e-9: continue
            s_ = (p.x * e.y - p.y * e.x) / den; u = (p.x * d.y - p.y * d.x) / den
            if s_ > 0 and -1e-6 <= u <= 1 + 1e-6:
                best = d * s_
        return best
    angs = [2 * math.pi * i / seg for i in range(seg)]
    O = [outer(a) for a in angs]
    if hole_r > 0:
        I = [Vector((math.cos(a) * hole_r, math.sin(a) * hole_r, 0)) for a in angs]
    for zz, mi_ in ((z, 0), (z - t, 1)):
        if hole_r > 0:
            vo = [bm.verts.new((cx + p.x, cy + p.y, zz)) for p in O]; vi = [bm.verts.new((cx + p.x, cy + p.y, zz)) for p in I]
            for i in range(seg):
                j = (i + 1) % seg
                f = bm.faces.new((vo[i], vo[j], vi[j], vi[i])); f.material_index = mi_
        else:
            f = bm.faces.new([bm.verts.new((cx + p.x, cy + p.y, zz)) for p in O]); f.material_index = mi_
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(_nm(name)); bm.to_mesh(me); bm.free()
    me.materials.append(M[top]); me.materials.append(M[under])
    o = bpy.data.objects.new(_nm(name), me); CUR.col.objects.link(o); adopt(o, "floor", walkable=True)
    return o

def spiral_stair(name, cx, cy, z0, z1, r_out=1.3, r_in=0.18, a0=0.0, turn=1.0, m="Stone", post="Stone", rail_=True):
    """one `turn` revolution from z0 to z1 starting at angle a0 (deg). Returns end angle (deg)."""
    n = max(8, round((z1 - z0) / 0.19)); rz = (z1 - z0) / n
    da = 2 * math.pi * turn / n
    mb = MB()
    for i in range(1, n):
        a1 = math.radians(a0) + (i - 1) * da; a2 = a1 + da * 1.05
        top = z0 + i * rz
        pts = [(math.cos(a1) * r_in, math.sin(a1) * r_in), (math.cos(a1) * r_out, math.sin(a1) * r_out),
               (math.cos(a2) * r_out, math.sin(a2) * r_out), (math.cos(a2) * r_in, math.sin(a2) * r_in)]
        vs_t = [mb.bm.verts.new((cx + p[0], cy + p[1], top)) for p in pts]
        vs_b = [mb.bm.verts.new((cx + p[0], cy + p[1], top - 0.07)) for p in pts]
        mb.bm.faces.new(vs_t); mb.bm.faces.new(list(reversed(vs_b)))
        for k in range(4):
            q = (k + 1) % 4
            mb.bm.faces.new((vs_t[k], vs_b[k], vs_b[q], vs_t[q]))
        mb._tag(vs_t + vs_b, m)
    mb.cyl(cx, cy, z0, z1, r_in, post, seg=12)
    o = mb.obj(name, kind="stair", walkable=True)
    o["risers"] = n; o["riser"] = rz
    if rail_:
        pts = []
        for i in range(n + 1):
            a = math.radians(a0) + i * da
            pts.append((cx + math.cos(a) * (r_out - 0.05), cy + math.sin(a) * (r_out - 0.05), z0 + i * rz + 0.95))
        pipe_run(name + "_Rail", pts, 0.025, "MetalDark", kind="railing")
    return a0 + math.degrees(2 * math.pi * turn)

def dome(name, cx, cy, z, r, m="PaintTeal", sz=1.0, seg=32):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=seg // 2, radius=r)
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if v.co.z < -1e-4], context="VERTS")
    bmesh.ops.scale(bm, vec=(1, 1, sz), verts=bm.verts)
    bmesh.ops.translate(bm, vec=(cx, cy, z), verts=bm.verts)
    for f in bm.faces: f.smooth = True
    me = bpy.data.meshes.new(_nm(name)); bm.to_mesh(me); bm.free(); me.materials.append(M[m])
    o = bpy.data.objects.new(_nm(name), me); CUR.col.objects.link(o); adopt(o, "roof")
    return o

def crenellate(name, pts, z, h=0.7, w=0.5, t=0.4, m="Stone"):
    """merlons along a closed polyline (list of Vector, local coords)"""
    mb = MB()
    for i in range(len(pts)):
        a, b = pts[i], pts[(i + 1) % len(pts)]
        L = (b - a).length; k = max(1, int(L / (w * 2)))
        d = (b - a).normalized()
        for j in range(k):
            c = a + d * (L * (j + 0.5) / k)
            ang = math.degrees(math.atan2(d.y, d.x))
            sub = MB(); sub.box(-w / 2, -t / 2, 0, w / 2, t / 2, h, m)
            o = sub.obj("%s_%d_%d" % (name, i, j), c.x, c.y, z, ang, kind="trim")
    return None

# ============================================================== parametric standard building
ROOF_KINDS = ("flat", "terrace", "gable", "gable_y", "hip", "shed", "mansard", "dome", "sawtooth", "none", "skirt")
SHOPLIKE = ("shop", "market", "cafe", "restaurant", "bar", "bakery", "arcade", "laundry", "bank", "lobby", "showroom")

def _spans(a, b, rooms):
    tot = sum(r[1] for r in rooms) or 1
    out = []; x = a
    for i, (k, w) in enumerate(rooms):
        nx = b if i == len(rooms) - 1 else x + (b - a) * w / tot
        out.append((k, x, nx)); x = nx
    return out

def _n1(hh):
    n = max(4, 2 * round(hh / 0.36)); return n // 2

def std(S):
    """Parametric walkable building. Footprint centred at origin, front = -Y. See TownKit docs for keys."""
    g = S.get
    W, D = S["W"], S["D"]; n = g("floors", 2); h0 = g("h0", 3.4); h = g("h", 3.2); T = g("T", 0.22)
    P = g("plinth", 0.0)
    Z = [P, P + h0] + [P + h0 + h * i for i in range(1, n)]
    x1, x2, y1, y2 = -W / 2, W / 2, -D / 2, D / 2
    xi1, xi2, yi1, yi2 = x1 + T, x2 - T, y1 + T, y2 - T
    ext0, ext = g("ext0", g("ext", "Plaster")), g("ext", "Plaster")
    extf = g("ext_f")                     # optional per-floor list
    intm = g("int", "PlasterInt")
    wk, fr = g("win", "win"), g("frame", "Frame")
    bay = g("bay", 2.6); ww = g("win_w", 1.4); sill = g("sill", 0.9); head = g("head", 2.3)
    fm, bm_, sm = g("front", 3.0), g("back", 2.0), g("side", 2.5)
    ctx = dict(Z=Z, W=W, D=D, x1=x1, x2=x2, y1=y1, y2=y2, T=T, wins=[])
    # plot + plinth + steps
    pm = g("plot_m", "StoneTile")
    ob("Plot", [(x1 - sm, y1 - fm, -0.4, x2 + sm, y2 + bm_, 0.0)], [pm], kind="floor" if pm != "Grass" else "terrain", walkable=True)
    if P > 0:
        ob("Plinth", [(x1 - 0.3, y1 - 0.3, -0.2, x2 + 0.3, y2 + 0.3, P - 0.02)], [g("plinth_m", "Stone")], kind="structure")
    multi = n > 1
    # stair core geometry
    if multi:
        sw, gap = g("stair_w", 1.0), 0.1
        cw = 2 * sw + gap
        scx = xi2 - 0.05 - cw / 2
        xc = xi2 - cw - 0.16
        dmax = max(((_n1(hh) - 1) * 0.28 + sw + 0.05) for hh in (h0, h))
        SY = yi2 - dmax - 0.05
        yC1 = SY - 1.6
        if yC1 - yi1 < 2.6:
            raise ValueError("%s: depth %.1f too small for stair core" % (CUR.bid, D))
    else:
        xc, SY, yC1 = xi2, yi2, yi2
    ctx.update(xc=xc, SY=SY, yC1=yC1)
    door_x = g("door_x", (xi1 + (xc if multi else xi2)) / 2)
    door_w = g("door_w", 1.0)
    door_k = g("door_k", "door_glass" if g("ground", "shop") in SHOPLIKE else "door")
    hole = None
    for f in range(n):
        z0, z1 = Z[f], Z[f + 1]; zc = z1 - 0.22; hh = z1 - z0
        prog = (g("prog") or {}).get(f)
        if f == 0:
            front = prog[0] if prog else g("g_front", [(g("ground", "shop"), 1)])
            back = prog[1] if prog else g("g_back", [("storage", 1), ("bath", 0.6)])
        else:
            front = prog[0] if prog else g("u_front", [("living", 2), ("kitchen", 1)])
            back = prog[1] if prog else g("u_back", [("bedroom", 1.4), ("bath", 0.8)])
        if not multi:
            back = []
        fs = _spans(xi1, xi2, front)
        bs = _spans(xi1, xc - 0.06, back) if back else []
        ops = {"S": [], "N": [], "W": [], "E": []}
        # ---- south facade
        balc = f > 0 and g("balcony", "none") != "none" and (g("balcony") == "front" or (g("balcony") == "alt" and f % 2 == 1))
        for (k, a, b) in fs:
            w_ = b - a
            if f == 0 and k in SHOPLIKE:
                segs = [(a + 0.3, b - 0.3)]
                if a < door_x < b:
                    segs = [(a + 0.3, door_x - door_w / 2 - 0.2), (door_x + door_w / 2 + 0.2, b - 0.3)]
                for (p, q) in segs:
                    if q - p > 0.8:
                        ops["S"].append((p, q, z0 + 0.3, z0 + min(hh - 0.5, 3.0), g("shop_k", "shop"), g("shop_frame", "Frame")))
                continue
            kk = max(1, int(w_ / bay))
            for i in range(kk):
                c = a + w_ * (i + 0.5) / kk; hw = min(ww, w_ / kk - 0.5) / 2
                if hw < 0.3: continue
                if f == 0 and abs(c - door_x) < door_w / 2 + hw + 0.3: continue
                if balc and i == kk // 2:
                    ops["S"].append((c - 0.5, c + 0.5, z0, z0 + 2.3, "door_glass"))
                else:
                    ops["S"].append((c - hw, c + hw, z0 + sill, z0 + min(head, hh - 0.45), wk, fr))
                    ctx["wins"].append(("S", c, z0 + sill, z0 + min(head, hh - 0.45), hw))
            if balc and w_ > 2.4:
                slab("F%d_Balc_%d" % (f + 1, int(a * 10)), a + 0.25, y1 - 1.25, b - 0.25, y1 - 0.03, z0, 0.16,
                     top=g("balc_floor", "StoneTile"), under="Concrete")
                rails_rect("F%d_BalR_%d" % (f + 1, int(a * 10)), a + 0.25, y1 - 1.25, b - 0.25, y1 - 0.03, z0, "SWE",
                           style=g("balc_rail", "bar"))
                if g("balc_plants", True):
                    plant(a + 0.6, y1 - 0.8, z0, 0, 0.7)
        if f == 0 and g("s_ops0") is not None:
            ops["S"] = [tuple(o_[:4]) + tuple(o_[4:]) for o_ in g("s_ops0")]
        if f == 0:
            if door_k != "none":
                ops["S"].append((door_x - door_w / 2, door_x + door_w / 2, z0, z0 + g("door_h", 2.4), door_k, g("door_m", "Frame")))
                CUR.main_door = (door_x, y1, z0)
        # ---- north facade (back rooms + stair landing window)
        for (k, a, b) in bs:
            w_ = b - a; kk = max(1, int(w_ / bay))
            for i in range(kk):
                c = a + w_ * (i + 0.5) / kk; hw = min(ww * 0.8, w_ / kk - 0.5) / 2
                if hw < 0.3: continue
                zb_ = z0 + (1.5 if k == "bath" else sill)
                ops["N"].append((c - hw, c + hw, zb_, z0 + min(head, hh - 0.45), wk, fr))
        if not multi and f == 0:
            for (k, a, b) in fs:
                c = (a + b) / 2
                if b - a > 1.6:
                    ops["N"].append((c - 0.6, c + 0.6, z0 + 1.0, z0 + min(head, hh - 0.45), wk, fr))
        if multi:
            lw = z0 + hh / 2 + 0.8
            if lw + 0.7 < z1 - 0.1:
                ops["N"].append((scx - 0.5, scx + 0.5, lw, lw + 0.7, "win", fr))
        # ---- west / east facades
        for sd, spans_ in (("W", [(yi1, yC1), (SY, yi2)] if multi else [(yi1, yi2)]), ("E", [(yi1, yC1)] if multi else [(yi1, yi2)])):
            for (a, b) in spans_:
                w_ = b - a
                if w_ < 1.4 or g("side_windows", True) is False: continue
                kk = max(1, int(w_ / (bay * 1.2)))
                for i in range(kk):
                    c = a + w_ * (i + 0.5) / kk; hw = min(ww * 0.8, w_ / kk - 0.6) / 2
                    if hw < 0.3: continue
                    if f == 0 and g("ground") in SHOPLIKE and sd == "E" and False: continue
                    ops[sd].append((c - hw, c + hw, z0 + sill, z0 + min(head, hh - 0.45), wk, fr))
        if multi and f == 0 and g("side_door", True):
            ops["E"].append((yC1 + 0.3, SY - 0.3, z0, z0 + 2.2, "door", g("door_m", "Frame")))
        e = (extf[f] if extf else (ext0 if f == 0 else ext))
        ring("F%d" % (f + 1), x1, y1, x2, y2, z0, z1, e, intm, T, 0.03 if e != intm else 0.0, ops)
        # ---- floors / stairs
        topm = g("floor0", "StoneTile") if f == 0 else g("floor", "WoodFloor")
        if f == 0:
            slab("F1_Floor", xi1, yi1, xi2, yi2, z0, 0.2, top=topm, under="Concrete")
        else:
            slab("F%d_Floor" % (f + 1), xi1, yi1, xi2, yi2, z0, 0.22, holes=[hole] if hole else [], top=topm)
        roof_access = g("roof", "flat") == "terrace"
        if multi and (f < n - 1 or roof_access):
            hole, _ = stair_u("F%d_Stair" % (f + 1), scx, SY, z0, z1, "+y", sw, gap, m=g("stair_m", "Concrete"), rail_style=g("stair_rail", "bar"))
        else:
            hole = None if f == n - 1 else hole
        # ---- partitions
        if multi:
            dops = []
            for (k, a, b) in fs:
                if b - a > 1.3:
                    c = (a + b) / 2 if not (f == 0 and k in SHOPLIKE) else b - 0.8
                    dops.append((c - 0.45, c + 0.45, z0, z0 + 2.1, "door"))
            iwall("F%d_CorrS" % (f + 1), "x", xi1, xi2, yC1, z0, zc, ops=dops)
            bops = [((a + b) / 2 - 0.45, (a + b) / 2 + 0.45, z0, z0 + 2.1, "door") for (k, a, b) in bs if b - a > 1.3]
            iwall("F%d_CorrN" % (f + 1), "x", xi1, xc - 0.06, SY, z0, zc, ops=bops)
            iwall("F%d_Core" % (f + 1), "y", SY + 0.06, yi2, xc, z0, zc)
            ob("F%d_CorrFloor" % (f + 1), [(xi1, yC1 + 0.06, z0, xi2, SY - 0.06, z0 + 0.008)], [g("corr_floor", "TileWhite")], kind="floor", walkable=True)
            lamp("F%d_CorrL" % (f + 1), (xi1 + xi2) / 2, (yC1 + SY) / 2, zc, 30)
        for (k, a, b) in fs[1:]:
            iwall("F%d_FP_%d" % (f + 1, int(a * 10)), "y", yi1, yC1 - 0.06, a, z0, zc)
        for (k, a, b) in bs[1:]:
            iwall("F%d_BP_%d" % (f + 1, int(a * 10)), "y", SY + 0.06, yi2, a, z0, zc)
        # ---- fill rooms
        for (k, a, b) in fs:
            fillroom(k, a + 0.07, yi1, b - 0.07, (yC1 - 0.06) if multi else yi2, z0, zc - z0, "N" if multi else "S")
        for (k, a, b) in bs:
            fillroom(k, a + 0.07, SY + 0.06, b - 0.07, yi2, z0, zc - z0, "S")
            if k == "bath":
                ob("F%d_BathFl_%d" % (f + 1, int(a * 10)), [(a + 0.07, SY + 0.06, z0, b - 0.07, yi2, z0 + 0.008)], ["TileWhite"], kind="floor", walkable=True)
        ctx.setdefault("rooms", []).append((f, fs, bs))
    # ---- roof
    zr = Z[n]
    rk = g("roof", "flat"); rm = g("roof_m", "Concrete"); ov = g("over", 0.5)
    ctx["roof_z"] = zr
    if rk != "none":
        slab("RoofSlab", xi1, yi1, xi2, yi2, zr, 0.22, holes=[hole] if (rk == "terrace" and hole) else [],
             top="Concrete" if rk in ("flat", "terrace", "dome", "sawtooth") else "WoodLight", under="Ceiling")
    top = zr
    if rk in ("flat", "terrace"):
        ph = g("parapet", 1.0 if rk == "terrace" else 0.6)
        pmat = g("parapet_m", ext)
        ob("Parapet", [(x1, y1, zr, x2, y1 + 0.2, zr + ph), (x1, y2 - 0.2, zr, x2, y2, zr + ph), (x1, y1 + 0.2, zr, x1 + 0.2, y2 - 0.2, zr + ph),
                       (x2 - 0.2, y1 + 0.2, zr, x2, y2 - 0.2, zr + ph)], [pmat], kind="wall")
        ob("ParapetCap", [(x1 - 0.05, y1 - 0.05, zr + ph, x2 + 0.05, y1 + 0.25, zr + ph + 0.06), (x1 - 0.05, y2 - 0.25, zr + ph, x2 + 0.05, y2 + 0.05, zr + ph + 0.06),
                          (x1 - 0.05, y1 + 0.25, zr + ph, x1 + 0.25, y2 - 0.25, zr + ph + 0.06), (x2 - 0.25, y1 + 0.25, zr + ph, x2 + 0.05, y2 - 0.25, zr + ph + 0.06)],
           [g("cap_m", "Stone")], kind="trim")
        top = zr + ph
        if rk == "terrace" and multi:
            ring("PH", xc - 0.06, yC1 - 0.06, x2, y2, zr, zr + 2.7, g("ph_m", "Concrete"), "PlasterInt", 0.2, 0.0,
                 {"W": [(yC1 + 0.3, SY - 0.3, zr, zr + 2.2, "door_metal")]})
            slab("PH_Roof", xc - 0.06, yC1 - 0.06, x2, y2, zr + 2.9, 0.2, top="Concrete")
            lamp("PH_L", scx, (yC1 + SY) / 2, zr + 2.7, 25)
            umbrella_table((xi1 + xc) / 2, (yi1 + yC1) / 2, zr, 0, g("umbrella", "AwningWhite")) if xc - xi1 > 3.5 else None
            for i in range(3):
                plant(xi1 + 0.6 + i * 1.0, yi2 - 0.5, zr, 0, 0.9, kind=["bush", "tall", "palm"][i])
            top = zr + 2.9
    elif rk in ("gable", "gable_y"):
        _, top = gable_roof("Roof", x1, y1, x2, y2, zr, g("pitch", 35), ov, rm, g("eave_m", "WoodDark"),
                            along="x" if rk == "gable" else "y", gable_m=g("gable_m", ext), cap=g("cap", "RoofRed"))
    elif rk == "hip":
        _, top = hip_roof("Roof", x1, y1, x2, y2, zr, g("pitch", 30), ov, rm, g("eave_m", "WoodDark"), curl=g("curl", 0.0),
                          ornaments=g("ornaments", False))
    elif rk == "skirt":
        _, top = hip_roof("Roof", x1, y1, x2, y2, zr, g("pitch", 30), ov, rm, g("eave_m", "WoodDark"), curl=g("curl", 0.3))
    elif rk == "shed":
        rise = W * math.tan(math.radians(g("pitch", 12))) if g("shed_axis", "y") == "x" else D * math.tan(math.radians(g("pitch", 12)))
        mb = MB()
        mb.quad([(x1 - ov, y1 - ov, zr + rise), (x2 + ov, y1 - ov, zr + rise), (x2 + ov, y2 + ov, zr), (x1 - ov, y2 + ov, zr)], rm, 0.15)
        for xx in (x1, x2 - 0.2):
            mb.prism([(y1, zr), (y2, zr), (y1, zr + rise)], xx, xx + 0.2, ext, plane="yz")
        mb.box(x1, y1, zr, x2, y1 + 0.2, zr + rise, ext)
        mb.obj("Roof", kind="roof"); top = zr + rise
    elif rk == "mansard":
        mh = g("mansard_h", 2.4); ins = g("mansard_in", 1.0)
        hip_roof("Mansard", x1, y1, x2, y2, zr, 70, 0.15, rm, "WoodDark", curl=0.0, cap=None,
                 inner=(x1 + ins, y1 + ins, x2 - ins, y2 - ins, zr + mh))
        ob("MansardTop", [(x1 + ins - 0.05, y1 + ins - 0.05, zr + mh - 0.05, x2 - ins + 0.05, y2 - ins + 0.05, zr + mh + 0.1)], ["MetalDark"], kind="roof")
        nd = max(1, int((W - 2) / 2.6))
        for i in range(nd):                                  # dormers on the front slope
            dx = x1 + 1.3 + (W - 2.6) * (i + 0.5) / nd
            mb = MB()
            mb.box(dx - 0.55, y1 + 0.25, zr + 0.4, dx + 0.55, y1 + 0.9, zr + 1.7, g("dormer_m", "Plaster"))
            mb.box(dx - 0.35, y1 + 0.22, zr + 0.6, dx + 0.35, y1 + 0.26, zr + 1.5, "Glass")
            mb.prism([(dx - 0.7, zr + 1.7), (dx + 0.7, zr + 1.7), (dx, zr + 2.15)], y1 + 0.15, y1 + 1.0, rm, plane="xz")
            mb.obj("Dormer%d" % i, kind="trim")
        top = zr + mh + 0.1
    elif rk == "dome":
        r = min(W, D) / 2 * g("dome_k", 0.7)
        mb = MB(); mb.cyl(0, 0, zr, zr + 1.0, r + 0.1, ext, seg=32); mb.obj("Drum", kind="roof")
        dome("Dome", 0, 0, zr + 1.0, r, rm, g("dome_sz", 1.0))
        top = zr + 1.0 + r * g("dome_sz", 1.0)
        mb = MB(); mb.cyl(0, 0, top - 0.05, top + 0.6, 0.12, "Brass", seg=10, r2=0.02); mb.sph(0, 0, top + 0.2, 0.15, "Brass"); mb.obj("DomeFinial", kind="trim")
    elif rk == "gambrel":                       # barn roof: steep lower + shallow upper slopes, ridge along x
        hw = D / 2 + ov; kz1, kz2 = 2.0, 3.2; ki = hw * 0.45
        mb = MB()
        for sg in (-1, 1):
            mb.quad([(x1 - ov, sg * hw, zr), (x2 + ov, sg * hw, zr), (x2 + ov, sg * ki, zr + kz1), (x1 - ov, sg * ki, zr + kz1)], rm, 0.12)
            mb.quad([(x1 - ov, sg * ki, zr + kz1), (x2 + ov, sg * ki, zr + kz1), (x2 + ov, 0, zr + kz2), (x1 - ov, 0, zr + kz2)], rm, 0.12)
        for xx in (x1, x2 - 0.2):
            mb.prism([(-D / 2, zr), (D / 2, zr), (D / 2 * 0.45, zr + kz1 - 0.05), (0, zr + kz2 - 0.1), (-D / 2 * 0.45, zr + kz1 - 0.05)], xx, xx + 0.2, g("gable_m", ext), plane="yz")
        mb.obj("Roof", kind="roof"); top = zr + kz2
    elif rk == "sawtooth":
        k = max(2, int(W / 4.0)); sw_ = W / k
        mb = MB()
        for i in range(k):
            xa = x1 + i * sw_
            mb.prism([(y1 - 0.1, zr), (y2 + 0.1, zr), (y2 + 0.1, zr + 0.0)], xa, xa + 0.01, rm, plane="yz") if False else None
            mb.quad([(xa, y1 - 0.2, zr), (xa + sw_, y1 - 0.2, zr + 1.8), (xa + sw_, y2 + 0.2, zr + 1.8), (xa, y2 + 0.2, zr)], rm, 0.12)
            mb.box(xa + sw_ - 0.06, y1 - 0.2, zr, xa + sw_, y2 + 0.2, zr + 1.8, "GlassDark")
        mb.obj("Sawtooth", kind="roof"); top = zr + 1.8
    ctx["top"] = top
    # ---- trims / decor
    dec = set(g("decor", []))
    if "bands" in dec:
        for zz in Z[1:-1]:
            ob("Band_%d" % int(zz * 10), [(x1 - 0.08, y1 - 0.08, zz - 0.12, x2 + 0.08, y1 - 0.02, zz + 0.06)], [g("band_m", "Stone")], kind="trim")
    if "cornice" in dec:
        cm_ = g("band_m", "Stone")
        ob("Cornice", [(x1 - 0.25, y1 - 0.25, zr - 0.35, x2 + 0.25, y1 + 0.1, zr - 0.05), (x1 - 0.18, y1 - 0.18, zr - 0.5, x2 + 0.18, y1, zr - 0.35),
                       (x1 - 0.25, y1, zr - 0.35, x1 + 0.1, y2 + 0.25, zr - 0.05), (x2 - 0.1, y1, zr - 0.35, x2 + 0.25, y2 + 0.25, zr - 0.05)], [cm_], kind="trim")
    if "pilasters" in dec:
        mb = MB()
        for (k, a, b) in ctx["rooms"][0][1]:
            for xx in (a, b):
                mb.box(xx - 0.22, y1 - 0.12, P, xx + 0.22, y1, zr - 0.3, g("band_m", "Stone"))
        mb.obj("Pilasters", kind="trim")
    if "quoins" in dec:
        mb = MB()
        zz = P
        while zz < zr - 0.3:
            for (cx_, cy_) in ((x1, y1), (x2, y1), (x1, y2), (x2, y2)):
                sx = 1 if cx_ < 0 else -1; sy = 1 if cy_ < 0 else -1
                L1 = 0.5 if int(zz / 0.32) % 2 else 0.3
                mb.box(min(cx_ - sx * 0.05, cx_ + sx * L1), min(cy_ - sy * 0.05, cy_ + sy * 0.3), zz,
                       max(cx_ - sx * 0.05, cx_ + sx * L1), max(cy_ - sy * 0.05, cy_ + sy * 0.3), zz + 0.28, g("band_m", "Stone"))
            zz += 0.32
        mb.obj("Quoins", kind="trim")
    if "shutters" in dec:
        mb = MB()
        for (sd, c, zb_, zt_, hw) in ctx["wins"]:
            for sx in (-1, 1):
                xa = c + sx * (hw + 0.05); xb = c + sx * (hw + 0.05 + hw * 0.9)
                mb.box(min(xa, xb), y1 - 0.08, zb_, max(xa, xb), y1 - 0.04, zt_, g("shutter_m", "PaintTeal"))
                for q in range(int((zt_ - zb_) / 0.12)):
                    zq = zb_ + 0.06 + q * 0.12
                    mb.box(min(xa, xb) + 0.03, y1 - 0.1, zq, max(xa, xb) - 0.03, y1 - 0.08, zq + 0.02, g("shutter_m", "PaintTeal"))
        mb.obj("Shutters", kind="trim")
    if "boxes" in dec:                       # window flower boxes
        mb = MB()
        for (sd, c, zb_, zt_, hw) in ctx["wins"]:
            if zb_ < P + 1.5: continue
            mb.box(c - hw, y1 - 0.32, zb_ - 0.25, c + hw, y1 - 0.05, zb_ - 0.05, "Terracotta")
            for i in range(int(hw * 4)):
                mb.sph(c - hw + 0.12 + i * 0.25, y1 - 0.18, zb_ - 0.02, 0.12, RNG.choice(["PlantGreen", "FabricRed", "PlasticYellow"]))
        mb.obj("FlowerBoxes", kind="trim")
    if "chimney" in dec:
        cxp = x1 + W * 0.25
        mb = MB(); mb.box(cxp - 0.35, 0.2, zr - 0.2, cxp + 0.35, 0.9, top + 0.9, g("chimney_m", "Brick"))
        mb.box(cxp - 0.42, 0.13, top + 0.9, cxp + 0.42, 0.97, top + 1.0, "Stone"); mb.obj("Chimney", kind="trim")
    if "ac" in dec:
        for i, zz in enumerate(Z[1:-1] if n > 1 else [Z[0] + 2.4]):
            ac_unit(x1 - 0.2, (y1 + yC1) / 2 if multi else 0.0, zz - 0.8, 270)
    if "pipes" in dec:
        pipe_run("DownPipe", [(x2 + 0.1, y1 + 0.3, 0.1), (x2 + 0.1, y1 + 0.3, zr + 0.4)], 0.06, g("pipe_m", "MetalDark"))
    if "tank" in dec and rk in ("flat", "terrace"):
        water_tank(x1 + 1.2, y2 - 1.2, zr, 0, 0.55, 1.2, "Chrome")
    if "solar" in dec and rk in ("flat", "terrace", "shed"):
        mb = MB()
        for i in range(max(1, int((W - 2) / 1.8))):
            mb.quad([(x1 + 1 + i * 1.8, y1 + 1.0, 0.3), (x1 + 2.6 + i * 1.8, y1 + 1.0, 0.3), (x1 + 2.6 + i * 1.8, y1 + 2.6, 0.9), (x1 + 1 + i * 1.8, y1 + 2.6, 0.9)], "Solar", 0.04)
        mb.obj("Solar", 0, 0, zr if rk != "shed" else top + 0.1, kind="trim")
    if "antenna" in dec:
        antenna(x1 + 1.0, y2 - 0.8, top, 2.6)
    if "plants" in dec:
        for (px_, py_) in ((x1 - 0.6, y1 - 0.8), (x2 + 0.6, y1 - 0.8)):
            plant(px_, py_, 0, 0, 1.0, "Terracotta", "bush")
    if "lanterns" in dec:
        for i, xx in enumerate((x1 + 0.6, x2 - 0.6)):
            lamp("FrontLantern%d" % i, xx, y1 - 0.5, P + 2.6, 30, (1.0, 0.5, 0.2), kind="lantern", glow="Lantern")
    if "walllamps" in dec:
        for i, dx in enumerate((-door_w / 2 - 0.35, door_w / 2 + 0.35)):
            lamp("DoorLamp%d" % i, door_x + dx, y1 - 0.12, P + 2.1, 25, kind="wall")
    if "trees" in dec:
        tree(x1 - sm + 1.0, y2 + bm_ - 1.0, 0, 0.9, "broad", seed=sum(map(ord, CUR.bid)))
        tree(x2 + sm - 1.0, y2 + bm_ - 1.0, 0, 1.0, "broad", seed=sum(map(ord, CUR.bid)) + 1)
    # ---- front: awning / porch / steps / signs
    if g("awning"):
        am = g("awning"); a1_, a2_ = g("awning_span", (x1 + 0.2, (xc if multi else x2) - 0.2))
        mb = MB()
        zt_ = Z[0] + min(h0 - 0.4, 3.0)
        mb.prism([(y1 - 0.03, zt_), (y1 - 1.3, zt_ - 0.4), (y1 - 1.3, zt_ - 0.25), (y1 - 0.03, zt_ + 0.2)], a1_, a2_, am, plane="yz")
        if g("awning_stripes"):
            for i in range(int((a2_ - a1_) / 0.6)):
                mb.prism([(y1 - 0.02, zt_), (y1 - 1.31, zt_ - 0.4), (y1 - 1.31, zt_ - 0.25), (y1 - 0.02, zt_ + 0.2)],
                         a1_ + i * 0.6, a1_ + i * 0.6 + 0.3, g("awning_stripes"), plane="yz")
        mb.obj("Awning", kind="trim")
    if g("porch"):
        pw = g("porch_w", door_w + 2.0); pd_ = g("porch_d", 1.8); ph_ = Z[0] + g("porch_h", 2.7)
        mb = MB()
        for sx in (-1, 1):
            mb.cyl(door_x + sx * (pw / 2 - 0.15), y1 - pd_ + 0.15, P, ph_, 0.1, g("porch_col", "White"), seg=12)
        mb.box(door_x - pw / 2, y1 - pd_, ph_, door_x + pw / 2, y1, ph_ + 0.15, g("porch_col", "White"))
        mb.obj("PorchFrame", kind="structure")
        gable_roof("PorchRoof", door_x - pw / 2, y1 - pd_, door_x + pw / 2, y1 - 0.02, ph_ + 0.15, 30, 0.2, g("porch_roof", rm if rk != "flat" else "RoofTile"),
                   "WoodDark", along="y", gable_m=None, cap=None)
        if P > 0:
            ob("PorchDeck", [(door_x - pw / 2, y1 - pd_, 0.0, door_x + pw / 2, y1, P)], [g("porch_floor", "WoodLight")], kind="floor", walkable=True)
    if P > 0:
        nP = max(1, round(P / 0.17)); LP = (nP - 1) * 0.29
        y0 = y1 - (g("porch_d", 1.8) if g("porch") else 0.0)
        if nP >= 2:
            stair("FrontSteps", door_x, y0 - LP - 0.0, 0.0, P, "+y", max(1.4, door_w + 0.6), 0.29, g("plinth_m", "Stone"), rails="none", solid=True)
            if not g("porch"):
                ob("Landing", [(door_x - door_w / 2 - 0.4, y1 - 0.35, 0.0, door_x + door_w / 2 + 0.4, y1, P)], [g("plinth_m", "Stone")], kind="floor", walkable=True)
                stair("FrontSteps2", door_x, y1 - 0.35 - LP, 0.0, P, "+y", max(1.4, door_w + 0.6), 0.29, g("plinth_m", "Stone"), rails="none", solid=True) if False else None
    if g("sign"):
        st_ = g("sign"); sw__ = st_[3] if len(st_) > 3 else min(W - 1.0, len(st_[0]) * 0.36 + 1.0)
        zs = Z[0] + min(h0 - 0.4, 3.0) + (0.55 if g("awning") else 0.3)
        zs = min(zs, Z[1] - 0.3) if multi else zs
        sign_board("Sign", st_[0], g("sign_x", door_x if not g("ground") in SHOPLIKE else (x1 + (xc if multi else x2)) / 2), y1 - 0.1, zs,
                   sw__, 0.48, 0, st_[1], st_[2], 0.3)
    if g("blade"):
        bt = g("blade")
        neon_vertical("Blade", bt[0], x1 + 0.3, y1 - 0.7, Z[0] + h0 + 1.2 if n > 1 else Z[0] + 2.0, 2.4, 90, bt[1], size=0.38)
    return ctx

def finish_std(ctx, extra_label_h=2.0):
    d = getattr(CUR, "main_door", (0, ctx["y1"], 0))
    label_building(ctx["top"] + extra_label_h, ctx["y1"] - 0.5, (d[0] + 0.95, d[1] - 0.04, d[2] + 1.5), max(6.0, ctx["W"] * 0.6))
    spawn("front", d[0], ctx["y1"] - 2.5, 0, 0)

def B(meta, spec, extra=None):
    """one-call building: meta = (id, zh, en, style, style_zh, tier, category, game_styles, desc)"""
    bid, zh, en, st, stz, tier, cat, gs, desc = meta
    begin_building(bid, zh, en, st, stz, tier, cat, gs, desc, spec.get("floors", 2), PLOT)
    CUR.spec = spec
    CUR.main_door = None
    ctx = std(spec)
    if extra:
        extra(ctx)
    if CUR.main_door is None:
        CUR.main_door = (0.0, ctx["y1"], 0.0)
    finish_std(ctx)

# ============================================================== registry for the v2 districts
REG = {}
def reg(meta, spec, extra=None):
    W, D = spec["W"], spec["D"]
    fm, bm_, sm = spec.get("front", 3.0), spec.get("back", 2.0), spec.get("side", 2.5)
    REG[meta[0]] = dict(fn=lambda: B(meta, spec, extra), pw=W + 2 * sm, front=D / 2 + fm, back=D / 2 + bm_, meta=meta)

def regx(meta, fn, pw, front, back):
    """bespoke builder: fn() must call begin_building(...PLOT) itself (use BX(meta) helper)"""
    REG[meta[0]] = dict(fn=fn, pw=pw, front=front, back=back, meta=meta)

def BX(meta, floors):
    bid, zh, en, st, stz, tier, cat, gs, desc = meta
    begin_building(bid, zh, en, st, stz, tier, cat, gs, desc, floors, PLOT)
    CUR.main_door = None


def halftimber(ctx, z1, z2, m="WoodDark", step=1.6):
    """timber framing strips on all four facades between z1..z2 (Tudor / medieval look)"""
    x1, x2, y1, y2 = ctx["x1"], ctx["x2"], ctx["y1"], ctx["y2"]
    mb = MB(); o_ = 0.035
    for (ya, yb) in ((y1 - o_ - 0.03, y1 - o_), (y2 + o_, y2 + o_ + 0.03)):
        for zz in (z1 + 0.02, (z1 + z2) / 2, z2 - 0.14):
            mb.box(x1 - o_, ya, zz, x2 + o_, yb, zz + 0.12, m)
        k = max(2, int((x2 - x1) / step))
        for i in range(k + 1):
            xx = x1 + (x2 - x1) * i / k
            mb.box(xx - 0.06, ya, z1, xx + 0.06, yb, z2, m)
            if i < k and i % 2 == 0:
                # diagonal brace in the lower half
                xb = x1 + (x2 - x1) * (i + 1) / k
                mb.quad([(xx, ya, z1 + 0.1), (xx + 0.12, ya, z1 + 0.1), (xb, ya, (z1 + z2) / 2), (xb - 0.12, ya, (z1 + z2) / 2)], m, 0) if False else None
    for (xa, xb) in ((x1 - o_ - 0.03, x1 - o_), (x2 + o_, x2 + o_ + 0.03)):
        for zz in (z1 + 0.02, (z1 + z2) / 2, z2 - 0.14):
            mb.box(xa, y1 - o_, zz, xb, y2 + o_, zz + 0.12, m)
        k = max(2, int((y2 - y1) / step))
        for i in range(k + 1):
            yy = y1 + (y2 - y1) * i / k
            mb.box(xa, yy - 0.06, z1, xb, yy + 0.06, z2, m)
    return mb.obj("HalfTimber_%d" % int(z1 * 10), kind="trim")


# ============================================================== v3 helpers
def false_front(ctx, m="WoodLight", h=2.2, sign=None, glow="NeonYellow"):
    """western saloon false-front parapet"""
    x1, x2, y1, zr = ctx["x1"], ctx["x2"], ctx["y1"], ctx["roof_z"]
    mb = MB(); mb.box(x1, y1 - 0.15, zr - 0.1, x2, y1, zr + h, m)
    mb.box(x1 - 0.1, y1 - 0.3, zr + h, x2 + 0.1, y1 + 0.05, zr + h + 0.15, "WoodDark"); mb.obj("FalseFront", kind="wall")
    ctx["top"] = max(ctx["top"], zr + h + 0.2)
    if sign:
        sign_board("FrontSign", sign, 0.0, y1 - 0.2, zr + h * 0.55, min(ctx["W"] - 1.0, len(sign) * 0.4 + 1.0), 0.7, 0, "WoodDark", glow, 0.42)

def round_door(x, y, z, r=1.1, m="PaintTeal", frame="WoodLight"):
    mb = MB(); mb.cyl(0, 0, -r - 0.1, r + 0.1, r + 0.12, frame, seg=24, axis="y") if False else None
    mb = MB(); mb.cyl(0, -0.06, 0, 0.0, r + 0.12, frame, seg=28, axis="y"); mb.cyl(0, -0.1, 0, 0, r, m, seg=28, axis="y")
    mb.sph(0, -0.16, 0, 0.08, "Brass")
    return mb.obj("RoundDoor_%d" % int(x * 10), x, y, z + r, kind="trim")

def skirt_ring(ctx, z, over=1.0, m="SlateDark", curl=0.4, inset=0.6):
    """extra pagoda-style roof skirt around the building at height z (castle / pagoda tiers)"""
    x1, x2, y1, y2 = ctx["x1"], ctx["x2"], ctx["y1"], ctx["y2"]
    hip_roof("Skirt_%d" % int(z * 10), x1, y1, x2, y2, z, 24, over, m, "PaintRed", curl=curl, cap=None,
             inner=(x1 + 0.0, y1 + 0.0, x2 - 0.0, y2 - 0.0, z + 0.8))
