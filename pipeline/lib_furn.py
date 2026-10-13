# TownKit furniture + props. Every builder makes one object in a local frame
# (origin = bottom centre, FRONT faces -Y, back toward +Y), then places it at (x, y, z) rotated rot degrees.
# Custom props: kind=furniture, interact=sit|sleep|open|use|cook|wash|shop|play|work, seats/use points.
import random, math

RNG = random.Random(7)

def _seat_pts(o, pts):
    o["use_points"] = json.dumps([[round(a, 2) for a in p] for p in pts])

# ---------------------------------------------------------------- seating / beds
def bed(x, y, z=0, rot=0, w=1.6, l=2.05, fab="FabricBlue", frame="WoodLight"):
    mb = MB(); hw = w / 2; hl = l / 2
    mb.box(-hw, -hl, 0.1, hw, hl, 0.32, frame)                          # base
    for sx in (-hw + 0.04, hw - 0.04):
        for sy in (-hl + 0.04, hl - 0.04):
            mb.bc(sx, sy, 0, 0.06, 0.06, 0.12, frame)
    mb.box(-hw, hl - 0.06, 0.1, hw, hl, 1.0, frame)                     # headboard
    mb.box(-hw + 0.03, -hl + 0.03, 0.32, hw - 0.03, hl - 0.06, 0.52, "Mattress")
    mb.box(-hw + 0.02, -hl + 0.02, 0.44, hw - 0.02, hl * 0.35, 0.56, fab)  # duvet
    mb.box(-hw + 0.02, -hl + 0.02, 0.2, hw - 0.02, -hl + 0.04, 0.56, fab)  # duvet overhang
    np_ = 2 if w > 1.2 else 1
    for i in range(np_):
        cx = -hw + w * (i + 0.5) / np_
        mb.sph(cx, hl - 0.3, 0.6, 0.25, "FabricWhite", sx=(w / np_ - 0.15) / 0.5, sy=0.6, sz=0.28)
    o = furn("Bed", mb, x, y, z, rot, "sleep")
    _seat_pts(o, [(0, 0, 0.55)])
    return o

def sofa(x, y, z=0, rot=0, w=2.1, fab="FabricGreen", d=0.9, legs="WoodDark"):
    mb = MB(); hw = w / 2; hd = d / 2
    mb.box(-hw, -hd, 0.1, hw, hd, 0.42, fab)
    mb.box(-hw, hd - 0.2, 0.42, hw, hd, 0.85, fab)                       # back
    mb.box(-hw, -hd, 0.42, -hw + 0.18, hd, 0.65, fab); mb.box(hw - 0.18, -hd, 0.42, hw, hd, 0.65, fab)
    n = max(1, round((w - 0.36) / 0.7))
    cw = (w - 0.36) / n
    for i in range(n):
        cx = -hw + 0.18 + cw * (i + 0.5)
        mb.box(cx - cw / 2 + 0.01, -hd + 0.02, 0.42, cx + cw / 2 - 0.01, hd - 0.2, 0.52, fab)
        mb.box(cx - cw / 2 + 0.02, hd - 0.32, 0.52, cx + cw / 2 - 0.02, hd - 0.2, 0.82, fab)
    for sx in (-hw + 0.06, hw - 0.06):
        for sy in (-hd + 0.06, hd - 0.06):
            mb.cyl(sx, sy, 0, 0.1, 0.025, legs, seg=8)
    mb.sph(-hw + 0.45, hd - 0.4, 0.68, 0.18, "FabricRed", sy=0.5)
    o = furn("Sofa", mb, x, y, z, rot, "sit")
    _seat_pts(o, [(-hw + 0.18 + cw * (i + 0.5), -0.05, 0.47) for i in range(n)])
    return o

def armchair(x, y, z=0, rot=0, fab="FabricBeige"):
    return sofa(x, y, z, rot, 0.95, fab, 0.85)

def chair(x, y, z=0, rot=0, m="WoodLight", seat=None, h=0.46):
    mb = MB()
    for sx in (-0.2, 0.2):
        for sy in (-0.2, 0.2):
            mb.bc(sx, sy, 0, 0.035, 0.035, h, m)
    mb.box(-0.22, -0.22, h, 0.22, 0.22, h + 0.04, seat or m)
    mb.bc(-0.2, 0.2, h, 0.035, 0.035, 0.45, m); mb.bc(0.2, 0.2, h, 0.035, 0.035, 0.45, m)
    mb.box(-0.22, 0.18, h + 0.22, 0.22, 0.22, h + 0.42, m)
    o = furn("Chair", mb, x, y, z, rot, "sit"); _seat_pts(o, [(0, 0, h + 0.04)])
    return o

def office_chair(x, y, z=0, rot=0, m="PlasticDark"):
    mb = MB()
    for a in range(5):
        t = a * 2 * math.pi / 5
        mb.box(-0.02, 0, 0.04, 0.02, 0.3, 0.08, "MetalDark")
    o = None
    mb.cyl(0, 0, 0.06, 0.42, 0.03, "Chrome", seg=10)
    mb.box(-0.25, -0.24, 0.42, 0.25, 0.24, 0.5, m)
    mb.box(-0.23, 0.2, 0.55, 0.23, 0.26, 1.05, m)
    mb.box(-0.02, 0.2, 0.45, 0.02, 0.24, 0.6, "MetalDark")
    for sx in (-0.26, 0.26):
        mb.box(sx - 0.02, -0.15, 0.62, sx + 0.02, 0.12, 0.66, m); mb.box(sx - 0.015, -0.02, 0.5, sx + 0.015, 0.02, 0.63, "MetalDark")
    for a in range(5):
        t = a * 2 * math.pi / 5
        mb.cyl(math.cos(t) * 0.3, math.sin(t) * 0.3, 0, 0.05, 0.025, "Rubber", seg=8)
    o = furn("OfficeChair", mb, x, y, z, rot, "sit"); _seat_pts(o, [(0, 0, 0.5)])
    return o

def stool(x, y, z=0, rot=0, h=0.75, top="LeatherBlack"):
    mb = MB()
    mb.cyl(0, 0, 0, 0.03, 0.2, "Chrome", seg=16); mb.cyl(0, 0, 0.03, h - 0.05, 0.025, "Chrome", seg=8)
    mb.cyl(0, 0, h * 0.35, h * 0.35 + 0.02, 0.15, "Chrome", seg=16, r2=0.15)
    mb.cyl(0, 0, h - 0.05, h, 0.18, top, seg=20)
    o = furn("Stool", mb, x, y, z, rot, "sit"); _seat_pts(o, [(0, 0, h)])
    return o

def bench(x, y, z=0, rot=0, w=1.8, m="WoodLight", legs="MetalDark"):
    mb = MB()
    for i in range(4):
        mb.box(-w / 2, -0.22 + i * 0.11, 0.42, w / 2, -0.13 + i * 0.11, 0.45, m)
    for i in range(3):
        mb.box(-w / 2, 0.2, 0.55 + i * 0.12, w / 2, 0.23, 0.63 + i * 0.12, m)
    for sx in (-w / 2 + 0.15, w / 2 - 0.15):
        mb.box(sx - 0.03, -0.22, 0, sx + 0.03, 0.2, 0.42, legs); mb.box(sx - 0.03, 0.18, 0.42, sx + 0.03, 0.24, 0.9, legs)
    o = furn("Bench", mb, x, y, z, rot, "sit"); _seat_pts(o, [(-w / 4, 0, 0.45), (w / 4, 0, 0.45)])
    return o

# ---------------------------------------------------------------- tables
def table(x, y, z=0, rot=0, w=1.4, d=0.8, h=0.75, m="WoodLight", legs=None):
    mb = MB()
    mb.box(-w / 2, -d / 2, h - 0.04, w / 2, d / 2, h, m)
    mb.box(-w / 2 + 0.04, -d / 2 + 0.04, h - 0.12, w / 2 - 0.04, d / 2 - 0.04, h - 0.04, m)
    for sx in (-w / 2 + 0.06, w / 2 - 0.06):
        for sy in (-d / 2 + 0.06, d / 2 - 0.06):
            mb.bc(sx, sy, 0, 0.05, 0.05, h - 0.04, legs or m)
    return furn("Table", mb, x, y, z, rot, "use")

def round_table(x, y, z=0, rot=0, r=0.4, h=0.74, m="Marble"):
    mb = MB()
    mb.cyl(0, 0, h - 0.03, h, r, m, seg=28); mb.cyl(0, 0, 0.03, h - 0.03, 0.035, "MetalDark", seg=10)
    mb.cyl(0, 0, 0, 0.03, 0.25, "MetalDark", seg=20)
    return furn("RoundTable", mb, x, y, z, rot, "use")

def dining_set(x, y, z=0, rot=0, w=1.4, d=0.8, m="WoodLight", n=4):
    t = table(x, y, z, rot, w, d, 0.75, m)
    ca = math.radians(rot)
    def P(u, v):
        return x + u * math.cos(ca) - v * math.sin(ca), y + u * math.sin(ca) + v * math.cos(ca)
    us = [-w / 4, w / 4] if n >= 4 else [0]
    for u in us:
        cx, cy = P(u, -d / 2 - 0.15); chair(cx, cy, z, rot + 180, m)
        cx, cy = P(u, d / 2 + 0.15); chair(cx, cy, z, rot, m)
    return t

def coffee_table(x, y, z=0, rot=0, w=1.1, d=0.6, m="WoodDark"):
    mb = MB()
    mb.box(-w / 2, -d / 2, 0.36, w / 2, d / 2, 0.42, m); mb.box(-w / 2 + 0.05, -d / 2 + 0.05, 0.08, w / 2 - 0.05, d / 2 - 0.05, 0.1, m)
    for sx in (-w / 2 + 0.04, w / 2 - 0.04):
        for sy in (-d / 2 + 0.04, d / 2 - 0.04):
            mb.bc(sx, sy, 0, 0.04, 0.04, 0.36, m)
    mb.box(-0.15, -0.1, 0.42, 0.1, 0.1, 0.46, "BookA"); mb.cyl(0.3, 0.05, 0.42, 0.52, 0.04, "Ceramic", seg=12)
    return furn("CoffeeTable", mb, x, y, z, rot, "use")

def desk(x, y, z=0, rot=0, w=1.4, d=0.7, m="WoodLight", pc=True, chair_=True):
    mb = MB()
    mb.box(-w / 2, -d / 2, 0.72, w / 2, d / 2, 0.75, m)
    mb.box(-w / 2, -d / 2 + 0.02, 0, -w / 2 + 0.03, d / 2, 0.72, m); mb.box(w / 2 - 0.03, -d / 2 + 0.02, 0, w / 2, d / 2, 0.72, m)
    mb.box(w / 2 - 0.45, -d / 2 + 0.03, 0.05, w / 2 - 0.03, d / 2, 0.72, m)          # drawer pedestal
    for q in (0.3, 0.52):
        mb.box(w / 2 - 0.43, -d / 2 + 0.02, q - 0.005, w / 2 - 0.05, -d / 2 + 0.03, q + 0.005, "MetalDark")
    if pc:
        mb.box(-0.3, d / 2 - 0.2, 0.75, 0.3, d / 2 - 0.16, 1.1, "PlasticDark")
        mb.box(-0.28, d / 2 - 0.205, 0.77, 0.28, d / 2 - 0.2, 1.08, "Screen")
        mb.box(-0.04, d / 2 - 0.16, 0.75, 0.04, d / 2 - 0.1, 0.9, "PlasticDark")
        mb.box(-0.22, -0.05, 0.75, 0.22, 0.1, 0.77, "PlasticDark")
        mb.cyl(-w / 2 + 0.2, d / 2 - 0.15, 0.75, 1.05, 0.012, "MetalDark", seg=8)
        mb.cyl(-w / 2 + 0.2, d / 2 - 0.15, 1.0, 1.1, 0.08, "MetalDark", seg=12, r2=0.03)
    o = furn("Desk", mb, x, y, z, rot, "work")
    if chair_:
        ca = math.radians(rot)
        office_chair(x - (-d / 2 - 0.35) * math.sin(ca), y + (-d / 2 - 0.35) * math.cos(ca), z, rot + 180)
    return o

# ---------------------------------------------------------------- storage
def bookshelf(x, y, z=0, rot=0, w=1.0, h=2.0, d=0.35, m="WoodDark", books=True):
    mb = MB(); t = 0.025
    mb.box(-w / 2, -d / 2, 0, -w / 2 + t, d / 2, h, m); mb.box(w / 2 - t, -d / 2, 0, w / 2, d / 2, h, m)
    mb.box(-w / 2, d / 2 - 0.01, 0, w / 2, d / 2, h, m)
    nsh = max(2, int(h / 0.38))
    for i in range(nsh + 1):
        zz = min(h - t, 0.05 + i * (h - 0.05) / nsh)
        mb.box(-w / 2, -d / 2, zz, w / 2, d / 2, zz + t, m)
        if books and i < nsh:
            u = -w / 2 + t + 0.01
            while u < w / 2 - t - 0.06:
                bw = RNG.uniform(0.025, 0.05); bh = RNG.uniform(0.2, 0.3)
                if RNG.random() < 0.12:
                    u += bw * 2; continue
                mb.box(u, -d / 2 + 0.04, zz + t, u + bw, d / 2 - 0.03, zz + t + bh, RNG.choice(["BookA", "BookB", "BookC", "BookD", "Paper"]))
                u += bw + 0.002
    return furn("Bookshelf", mb, x, y, z, rot, "use")

def wardrobe(x, y, z=0, rot=0, w=1.2, h=2.1, d=0.6, m="WoodLight"):
    mb = MB()
    mb.box(-w / 2, -d / 2 + 0.03, 0, w / 2, d / 2, h, m)
    mb.box(-w / 2 + 0.02, -d / 2 + 0.02, 0, w / 2 - 0.02, -d / 2 + 0.03, 0.08, "WoodDark")
    o = furn("Wardrobe", mb, x, y, z, rot, "open")
    for k, sgn in ((0, -1), (1, 1)):
        lw = w / 2 - 0.01
        lm = MB()
        lm.box(0, -0.022, 0, -sgn * lw, 0, h - 0.1, m)
        lm.box(-sgn * (lw - 0.06), -0.05, h * 0.45, -sgn * (lw - 0.04), -0.022, h * 0.6, "Brass")
        lf = lm.obj("Wardrobe_%02d_Door%d" % (CUR.n, k), kind="door")
        lf.parent = o; lf.location = (sgn * (w / 2 - 0.005), -d / 2 + 0.03, 0.08)
        lf["openable"] = "hinge"; lf["open_angle"] = -sgn * 100.0; lf["closed_rot_z"] = 0.0
    return o

def cabinet_low(x, y, z=0, rot=0, w=1.6, h=0.55, d=0.45, m="WoodLight"):
    mb = MB()
    mb.box(-w / 2, -d / 2, 0.08, w / 2, d / 2, h, m)
    n = max(2, round(w / 0.5))
    for i in range(n):
        u = -w / 2 + w * (i + 0.5) / n
        mb.box(u - 0.08, -d / 2 - 0.02, h - 0.12, u + 0.08, -d / 2, h - 0.1, "MetalDark")
        mb.box(-w / 2 + w * i / n + 0.004, -d / 2 - 0.005, 0.1, -w / 2 + w * (i + 1) / n - 0.004, -d / 2, h - 0.02, m)
    for sx in (-w / 2 + 0.05, w / 2 - 0.05):
        mb.bc(sx, 0, 0, 0.04, d - 0.1, 0.08, "MetalDark")
    return furn("Cabinet", mb, x, y, z, rot, "open")

def nightstand(x, y, z=0, rot=0, m="WoodLight"):
    mb = MB()
    mb.box(-0.22, -0.2, 0.05, 0.22, 0.2, 0.55, m)
    mb.box(-0.06, -0.215, 0.42, 0.06, -0.2, 0.44, "Brass")
    mb.cyl(0.08, 0.05, 0.55, 0.85, 0.012, "Brass", seg=8); mb.cyl(0.08, 0.05, 0.78, 0.95, 0.14, "LightSoft", seg=16, r2=0.09)
    return furn("Nightstand", mb, x, y, z, rot, "open")

# ---------------------------------------------------------------- kitchen / bath
def kitchen_run(x, y, z=0, rot=0, w=3.0, m="White", top="MarbleBlack", uppers=True, hood=True):
    """counter run along a back wall: sink at -1/4, cooktop at +1/4"""
    mb = MB(); d = 0.62
    mb.box(-w / 2, -d / 2 + 0.05, 0.1, w / 2, d / 2, 0.87, m)
    mb.box(-w / 2, -d / 2 + 0.08, 0, w / 2, d / 2, 0.1, "Black")
    mb.box(-w / 2 - 0.01, -d / 2, 0.87, w / 2 + 0.01, d / 2, 0.91, top)
    n = max(2, round(w / 0.6))
    for i in range(n):
        u1 = -w / 2 + w * i / n + 0.003; u2 = -w / 2 + w * (i + 1) / n - 0.003
        mb.box(u1, -d / 2 + 0.03, 0.12, u2, -d / 2 + 0.05, 0.85, m)
        mb.box((u1 + u2) / 2 - 0.1, -d / 2 + 0.01, 0.78, (u1 + u2) / 2 + 0.1, -d / 2 + 0.03, 0.8, "Chrome")
    sx = -w / 4
    mb.box(sx - 0.3, -0.2, 0.75, sx + 0.3, 0.18, 0.912, "Chrome")
    mb.box(sx - 0.27, -0.17, 0.76, sx + 0.27, 0.15, 0.915, "MetalDark")
    mb.cyl(sx, 0.24, 0.91, 1.2, 0.015, "Chrome", seg=10); mb.box(sx - 0.015, 0.05, 1.17, sx + 0.015, 0.25, 1.2, "Chrome")
    cx = w / 4
    mb.box(cx - 0.3, -0.25, 0.91, cx + 0.3, 0.25, 0.925, "Black")
    for a, b_ in ((-0.14, -0.12), (0.14, -0.12), (-0.14, 0.12), (0.14, 0.12)):
        mb.cyl(cx + a, b_, 0.925, 0.93, 0.09, "MetalDark", seg=16)
    mb.cyl(cx + 0.14, -0.12, 0.93, 1.03, 0.11, "Chrome", seg=16)            # pot
    mb.box(-w / 2 + 0.1, d / 2 - 0.02, 0.91, w / 2 - 0.1, d / 2, 1.5, "TileWhite")  # backsplash
    if uppers:
        mb.box(-w / 2, d / 2 - 0.35, 1.5, w / 2, d / 2, 2.2, m)
        for i in range(n):
            u1 = -w / 2 + w * i / n + 0.003; u2 = -w / 2 + w * (i + 1) / n - 0.003
            mb.box(u1, d / 2 - 0.37, 1.52, u2, d / 2 - 0.35, 2.18, m)
    if hood:
        mb.box(cx - 0.35, d / 2 - 0.5, 1.45, cx + 0.35, d / 2 - 0.02, 1.55, "Chrome")
    o = furn("Kitchen", mb, x, y, z, rot, "cook")
    _seat_pts(o, [(sx, -0.6, 0), (cx, -0.6, 0)])
    return o

def fridge(x, y, z=0, rot=0, w=0.75, h=1.85, m="Chrome"):
    mb = MB(); d = 0.7
    mb.box(-w / 2, -d / 2 + 0.04, 0, w / 2, d / 2, h, m)
    o = furn("Fridge", mb, x, y, z, rot, "open")
    for k, (q1, q2) in enumerate(((0.02, h * 0.62), (h * 0.63, h - 0.01))):
        lm = MB()
        lm.box(0, -0.04, q1, w - 0.01, 0, q2, m)
        lm.box(w - 0.1, -0.08, q1 + 0.1, w - 0.08, -0.04, q2 - 0.1, "MetalDark")
        lf = lm.obj("Fridge_%02d_Door%d" % (CUR.n, k), kind="door")
        lf.parent = o; lf.location = (-w / 2 + 0.005, -d / 2 + 0.04, 0)
        lf["openable"] = "hinge"; lf["open_angle"] = -100.0; lf["closed_rot_z"] = 0.0
    return o

def toilet(x, y, z=0, rot=0):
    mb = MB()
    mb.cyl(0, -0.05, 0, 0.38, 0.17, "Ceramic", seg=24, r2=0.2)
    mb.cyl(0, -0.08, 0.38, 0.42, 0.21, "White", seg=24)
    mb.box(-0.2, 0.15, 0.38, 0.2, 0.33, 0.8, "Ceramic")
    mb.box(-0.21, 0.14, 0.8, 0.21, 0.34, 0.83, "Ceramic")
    o = furn("Toilet", mb, x, y, z, rot, "sit"); _seat_pts(o, [(0, -0.05, 0.42)])
    return o

def vanity(x, y, z=0, rot=0, w=0.8):
    mb = MB()
    mb.box(-w / 2, -0.25, 0.1, w / 2, 0.25, 0.82, "WoodLight")
    mb.box(-w / 2 - 0.01, -0.26, 0.82, w / 2 + 0.01, 0.25, 0.86, "Marble")
    mb.cyl(0, -0.02, 0.8, 0.865, 0.18, "Ceramic", seg=24)
    mb.cyl(0, 0.17, 0.86, 1.05, 0.012, "Chrome", seg=8); mb.box(-0.012, 0.05, 1.02, 0.012, 0.18, 1.05, "Chrome")
    mb.box(-w / 2 + 0.05, 0.22, 1.1, w / 2 - 0.05, 0.25, 1.9, "Chrome")             # mirror
    mb.box(-w / 2 + 0.05, 0.18, 1.92, w / 2 - 0.05, 0.25, 1.97, "LightCool")
    return furn("Vanity", mb, x, y, z, rot, "wash")

def bathtub(x, y, z=0, rot=0, w=1.7, d=0.75):
    mb = MB()
    mb.box(-w / 2, -d / 2, 0, w / 2, d / 2, 0.55, "Ceramic")
    mb.box(-w / 2 + 0.08, -d / 2 + 0.08, 0.3, w / 2 - 0.08, d / 2 - 0.08, 0.5, "PoolWater")
    mb.cyl(w / 2 - 0.15, d / 2 - 0.05, 0.55, 0.7, 0.02, "Chrome", seg=8)
    o = furn("Bathtub", mb, x, y, z, rot, "wash")
    return o

def shower(x, y, z=0, rot=0, w=0.9, d=0.9):
    mb = MB()
    mb.box(-w / 2, -d / 2, 0, w / 2, d / 2, 0.06, "TileWhite")
    mb.box(-w / 2, -d / 2, 0.06, w / 2, -d / 2 + 0.01, 2.0, "GlassFrost")
    mb.box(-w / 2, -d / 2, 0.06, -w / 2 + 0.01, d / 2, 2.0, "GlassFrost")
    mb.cyl(0, d / 2 - 0.05, 0.9, 2.05, 0.012, "Chrome", seg=8); mb.cyl(0, d / 2 - 0.2, 2.0, 2.03, 0.1, "Chrome", seg=16)
    mb.box(-0.01, d / 2 - 0.2, 2.03, 0.01, d / 2 - 0.04, 2.05, "Chrome")
    return furn("Shower", mb, x, y, z, rot, "wash")

def washer(x, y, z=0, rot=0):
    mb = MB()
    mb.box(-0.3, -0.3, 0, 0.3, 0.3, 0.85, "White")
    mb.cyl(0, -0.3, 0.42, 0.42, 0.2, "Chrome", seg=24, axis="y")
    mb.box(-0.25, -0.31, 0.72, 0.25, -0.3, 0.8, "PlasticDark")
    return furn("Washer", mb, x, y, z, rot, "use")

# ---------------------------------------------------------------- living / decor
def tv(x, y, z=0, rot=0, w=1.6, cab=True):
    mb = MB()
    if cab:
        mb.box(-w / 2 - 0.1, -0.22, 0.05, w / 2 + 0.1, 0.22, 0.5, "WoodDark")
        mb.box(-w / 2, -0.22, 0.02, w / 2, 0.2, 0.05, "Black")
    h = w * 0.5625
    mb.box(-w / 2, 0.02, 0.85, w / 2, 0.06, 0.85 + h, "Black")
    mb.box(-w / 2 + 0.02, 0.015, 0.87, w / 2 - 0.02, 0.02, 0.83 + h, "Screen")
    mb.box(-0.15, 0.0, 0.5, 0.15, 0.1, 0.52, "Black"); mb.box(-0.03, 0.03, 0.5, 0.03, 0.06, 0.86, "Black")
    return furn("TV", mb, x, y, z, rot, "use")

def rug(x, y, z=0, rot=0, w=2.4, d=1.7, m="CarpetRed"):
    mb = MB(); mb.box(-w / 2, -d / 2, 0, w / 2, d / 2, 0.012, m)
    return furn("Rug", mb, x, y, z, rot)

def plant(x, y, z=0, rot=0, s=1.0, pot="Terracotta", kind="bush"):
    mb = MB()
    mb.cyl(0, 0, 0, 0.35 * s, 0.17 * s, pot, seg=16, r2=0.21 * s)
    mb.cyl(0, 0, 0.33 * s, 0.34 * s, 0.19 * s, "Soil", seg=16)
    if kind == "palm":
        mb.cyl(0, 0, 0.3 * s, 1.3 * s, 0.025 * s, "Bark", seg=6)
        for a in range(7):
            t = a * 2 * math.pi / 7
            mb.sph(math.cos(t) * 0.3 * s, math.sin(t) * 0.3 * s, 1.25 * s, 0.32 * s, "PlantGreen", sx=1.4, sy=0.35, sz=0.12)
    elif kind == "tall":
        for i in range(5):
            mb.sph(RNG.uniform(-0.1, 0.1) * s, RNG.uniform(-0.1, 0.1) * s, (0.6 + i * 0.22) * s, 0.2 * s,
                   RNG.choice(["PlantGreen", "PlantDark"]), sz=1.3)
    else:
        for i in range(6):
            mb.sph(RNG.uniform(-0.12, 0.12) * s, RNG.uniform(-0.12, 0.12) * s, RNG.uniform(0.45, 0.65) * s, RNG.uniform(0.15, 0.22) * s,
                   RNG.choice(["PlantGreen", "PlantDark"]))
    return furn("Plant", mb, x, y, z, rot)

def floor_lamp(x, y, z=0, rot=0):
    mb = MB()
    mb.cyl(0, 0, 0, 0.03, 0.15, "MetalDark", seg=16); mb.cyl(0, 0, 0.03, 1.5, 0.012, "MetalDark", seg=8)
    mb.cyl(0, 0, 1.4, 1.7, 0.2, "LightSoft", seg=20, r2=0.13)
    return furn("FloorLamp", mb, x, y, z, rot, "use")

def picture(x, y, z, rot=0, w=0.7, h=0.5, m="PaintTeal"):
    mb = MB()
    mb.box(-w / 2, 0, -h / 2, w / 2, 0.03, h / 2, "WoodDark"); mb.box(-w / 2 + 0.04, -0.005, -h / 2 + 0.04, w / 2 - 0.04, 0, h / 2 - 0.04, m)
    return furn("Picture", mb, x, y, z, rot)

def curtain(x, y, z, rot=0, w=1.4, h=2.2, m="FabricBeige"):
    mb = MB()
    mb.cyl(-w / 2 - 0.1, 0, h, h + 0.03, 0.015, "Brass", seg=8, axis="x") if False else None
    mb.box(-w / 2 - 0.15, -0.02, h - 0.02, w / 2 + 0.15, 0.02, h + 0.01, "Brass")
    for sx in (-1, 1):
        for i in range(4):
            u = sx * (w / 2 + 0.05 - i * 0.07)
            mb.box(u - 0.04, -0.06 + (i % 2) * 0.04, 0.05, u + 0.04, -0.02 + (i % 2) * 0.04, h - 0.03, m)
    return furn("Curtain", mb, x, y, z, rot)

# ---------------------------------------------------------------- commercial
def shop_counter(x, y, z=0, rot=0, w=2.0, m="WoodDark", top="Marble", register=True):
    mb = MB()
    mb.box(-w / 2, -0.3, 0, w / 2, 0.3, 1.0, m); mb.box(-w / 2 - 0.02, -0.33, 1.0, w / 2 + 0.02, 0.32, 1.05, top)
    if register:
        mb.box(0.2, -0.1, 1.05, 0.55, 0.2, 1.15, "PlasticDark"); mb.box(0.25, 0.12, 1.15, 0.5, 0.15, 1.35, "PlasticDark")
        mb.box(0.27, 0.115, 1.17, 0.48, 0.12, 1.33, "ScreenGreen")
    return furn("Counter", mb, x, y, z, rot, "shop")

def shelf_goods(x, y, z=0, rot=0, w=1.8, h=1.8, d=0.45, double=False):
    mb = MB()
    mb.box(-w / 2, -0.02, 0, w / 2, 0.02, h, "White") if double else mb.box(-w / 2, d / 2 - 0.03, 0, w / 2, d / 2, h, "White")
    for sx in (-w / 2, w / 2 - 0.03):
        mb.box(sx, -d / 2, 0, sx + 0.03, d / 2, h, "White")
    cols = ["PlasticRed", "PlasticBlue", "PlasticYellow", "PlasticGreen", "White", "BookA", "BookC", "Paper"]
    for i in range(5):
        zz = 0.1 + i * (h - 0.2) / 4.5
        mb.box(-w / 2, -d / 2, zz, w / 2, d / 2, zz + 0.02, "MetalDark")
        u = -w / 2 + 0.05
        while u < w / 2 - 0.12:
            pw = RNG.uniform(0.07, 0.14); ph = RNG.uniform(0.12, 0.28); c = RNG.choice(cols)
            for sy in ((-d / 2 + 0.03, -0.03), (0.03, d / 2 - 0.03)) if double else ((-d / 2 + 0.03, d / 2 - 0.05),):
                if RNG.random() < 0.9:
                    if RNG.random() < 0.3:
                        mb.cyl(u + pw / 2, (sy[0] + sy[1]) / 2, zz + 0.02, zz + 0.02 + ph, pw / 2.2, c, seg=10)
                    else:
                        mb.box(u, sy[0], zz + 0.02, u + pw, sy[1], zz + 0.02 + ph, c)
            u += pw + 0.015
    return furn("ShelfGoods", mb, x, y, z, rot, "shop")

def drinks_fridge(x, y, z=0, rot=0, w=1.2, h=2.0):
    mb = MB(); d = 0.7
    mb.box(-w / 2, -d / 2, 0, w / 2, d / 2, h, "White")
    mb.box(-w / 2 + 0.05, -d / 2 - 0.01, 0.15, w / 2 - 0.05, -d / 2 + 0.02, h - 0.1, "Glass")
    mb.box(-w / 2 + 0.06, -d / 2 + 0.03, 0.15, w / 2 - 0.06, -d / 2 + 0.05, h - 0.1, "LightCool")
    for i in range(5):
        zz = 0.2 + i * 0.36
        u = -w / 2 + 0.1
        while u < w / 2 - 0.1:
            mb.cyl(u, -d / 2 + 0.15, zz, zz + 0.22, 0.035, RNG.choice(["PlasticRed", "PlasticBlue", "PlasticGreen", "PlasticYellow"]), seg=8)
            u += 0.09
    mb.box(-w / 2, -d / 2, h - 0.25, w / 2, -d / 2 - 0.02, h, "NeonCyan")
    return furn("DrinksFridge", mb, x, y, z, rot, "open")

def vending(x, y, z=0, rot=0, glow="NeonRed"):
    mb = MB()
    mb.box(-0.5, -0.4, 0, 0.5, 0.4, 1.85, "PlasticRed" if glow == "NeonRed" else "PlasticBlue")
    mb.box(-0.45, -0.41, 0.75, 0.2, -0.39, 1.75, "LightCool")
    for i in range(4):
        for j in range(5):
            mb.cyl(-0.4 + j * 0.13, -0.38, 0.8 + i * 0.24, 0.98 + i * 0.24, 0.03, RNG.choice(["PlasticRed", "PlasticBlue", "PlasticYellow", "White"]), seg=8)
    mb.box(0.25, -0.42, 1.0, 0.45, -0.4, 1.5, "PlasticDark"); mb.box(-0.45, -0.42, 0.15, 0.2, -0.4, 0.4, "Black")
    return furn("Vending", mb, x, y, z, rot, "use")

def arcade(x, y, z=0, rot=0, body="PlasticBlue", glow="NeonPink"):
    mb = MB()
    mb.box(-0.35, -0.2, 0, 0.35, 0.45, 1.75, body)
    mb.prism([(-0.4, 0.95), (-0.4, 1.05), (-0.05, 1.1), (-0.05, 0.95)], -0.35, 0.35, "PlasticDark", plane="yz")
    mb.box(-0.3, -0.22, 1.12, 0.3, -0.18, 1.6, "Black")
    mb.box(-0.27, -0.225, 1.15, 0.27, -0.22, 1.57, "Screen")
    mb.box(-0.35, -0.25, 1.65, 0.35, 0.45, 1.9, glow)
    mb.cyl(-0.15, -0.3, 1.05, 1.13, 0.012, "Chrome", seg=6); mb.sph(-0.15, -0.3, 1.14, 0.025, "PlasticRed")
    for i in range(3):
        mb.cyl(0.05 + i * 0.08, -0.25, 1.05, 1.07, 0.022, RNG.choice(["PlasticRed", "PlasticYellow", "PlasticGreen"]), seg=10)
    return furn("Arcade", mb, x, y, z, rot, "play")

def claw_machine(x, y, z=0, rot=0):
    mb = MB()
    mb.box(-0.45, -0.45, 0, 0.45, 0.45, 0.85, "PlasticRed")
    mb.box(-0.45, -0.45, 0.85, 0.45, 0.45, 1.7, "Glass")
    for i in range(10):
        mb.sph(RNG.uniform(-0.35, 0.35), RNG.uniform(-0.35, 0.35), 0.92, 0.07, RNG.choice(["PlasticYellow", "PlasticBlue", "FabricRed", "FabricWhite"]))
    mb.box(-0.47, -0.47, 1.7, 0.47, 0.47, 1.95, "NeonYellow")
    return furn("ClawMachine", mb, x, y, z, rot, "play")

def bar_counter(x, y, z=0, rot=0, w=3.0, m="WoodDark", top="WoodLight", stools=True):
    mb = MB()
    mb.box(-w / 2, -0.3, 0, w / 2, 0.3, 1.05, m)
    mb.box(-w / 2 - 0.02, -0.4, 1.05, w / 2 + 0.02, 0.32, 1.1, top)
    mb.box(-w / 2, -0.33, 0.15, w / 2, -0.3, 0.2, "Brass")
    o = furn("BarCounter", mb, x, y, z, rot, "shop")
    if stools:
        ca = math.radians(rot)
        n = max(1, int(w / 0.6))
        for i in range(n):
            u = -w / 2 + w * (i + 0.5) / n
            stool(x + u * math.cos(ca) + 0.65 * math.sin(ca), y + u * math.sin(ca) - 0.65 * math.cos(ca), z, rot, 0.75)
    return o

def cafe_set(x, y, z=0, rot=0, m="Marble", chair_m="WoodLight"):
    round_table(x, y, z, rot, 0.38, 0.74, m)
    ca = math.radians(rot)
    for k in (-1, 1):
        chair(x + k * 0.6 * math.cos(ca), y + k * 0.6 * math.sin(ca), z, rot + (90 if k < 0 else 270), chair_m)

def umbrella_table(x, y, z=0, rot=0, cloth="AwningWhite"):
    round_table(x, y, z, rot, 0.45, 0.74, "WoodLight")
    mb = MB()
    mb.cyl(0, 0, 0.74, 2.4, 0.02, "WoodLight", seg=8)
    mb.cyl(0, 0, 2.0, 2.45, 1.2, cloth, seg=8, r2=0.05)
    furn("Umbrella", mb, x, y, z, rot)
    for k in range(3):
        a = ca = math.radians(rot + k * 120)
        chair(x + math.cos(a) * 0.75, y + math.sin(a) * 0.75, z, rot + k * 120 + 90, "WoodLight")

# ---------------------------------------------------------------- office / tech
def server_rack(x, y, z=0, rot=0):
    mb = MB()
    mb.box(-0.3, -0.5, 0, 0.3, 0.5, 2.0, "MetalDark")
    mb.box(-0.27, -0.51, 0.05, 0.27, -0.5, 1.95, "Black")
    for i in range(16):
        zz = 0.1 + i * 0.115
        mb.box(-0.25, -0.515, zz, 0.25, -0.505, zz + 0.09, "PanelDark")
        for j in range(RNG.randint(1, 4)):
            mb.box(-0.22 + j * 0.03, -0.52, zz + 0.03, -0.21 + j * 0.03, -0.515, zz + 0.04, RNG.choice(["LED", "NeonCyan", "NeonOrange"]))
    return furn("ServerRack", mb, x, y, z, rot, "use")

def console(x, y, z=0, rot=0, w=2.0, screens=3, glow="Screen"):
    mb = MB()
    mb.box(-w / 2, -0.4, 0, w / 2, 0.35, 0.72, "PanelSteel")
    mb.prism([(-0.45, 0.72), (-0.45, 0.78), (0.35, 0.9), (0.35, 0.72)], -w / 2, w / 2, "PanelDark", plane="yz")
    for i in range(int(w / 0.2)):
        u = -w / 2 + 0.1 + i * 0.2
        mb.cyl(u, -0.2, 0.8, 0.83, 0.025, RNG.choice(["NeonRed", "NeonGreen", "NeonYellow", "PlasticDark"]), seg=8)
    for i in range(screens):
        u = -w / 2 + w * (i + 0.5) / screens
        mb.box(u - w / screens / 2 + 0.05, 0.2, 0.95, u + w / screens / 2 - 0.05, 0.28, 1.6, "Black")
        mb.box(u - w / screens / 2 + 0.08, 0.195, 0.98, u + w / screens / 2 - 0.08, 0.2, 1.57, glow)
    return furn("Console", mb, x, y, z, rot, "work")

def reception(x, y, z=0, rot=0, w=3.0, m="MarbleBlack", top="Marble"):
    mb = MB()
    mb.box(-w / 2, -0.35, 0, w / 2, 0.35, 1.1, m)
    mb.box(-w / 2 - 0.05, -0.45, 1.1, w / 2 + 0.05, 0.1, 1.15, top)
    mb.box(-w / 2, 0.35, 0, w / 2, 0.75, 0.75, "WoodDark")
    mb.box(-w / 2 + 0.05, -0.36, 0.2, w / 2 - 0.05, -0.35, 0.25, "LightWarm")
    o = furn("Reception", mb, x, y, z, rot, "shop")
    return o

def meeting_table(x, y, z=0, rot=0, w=3.2, d=1.2):
    table(x, y, z, rot, w, d, 0.75, "WoodDark", "Chrome")
    ca = math.radians(rot)
    n = max(2, int(w / 0.8))
    for i in range(n):
        u = -w / 2 + w * (i + 0.5) / n
        for v, r2 in ((-d / 2 - 0.35, 180), (d / 2 + 0.35, 0)):
            office_chair(x + u * math.cos(ca) - v * math.sin(ca), y + u * math.sin(ca) + v * math.cos(ca), z, rot + r2)

# ---------------------------------------------------------------- exterior props
def ac_unit(x, y, z, rot=0):
    mb = MB()
    mb.box(-0.4, -0.15, 0, 0.4, 0.15, 0.55, "White")
    mb.cyl(0.08, -0.15, 0.27, 0.27, 0.2, "MetalDark", seg=20, axis="y")
    for i in range(7):
        mb.box(-0.12 + i * 0.0, -0.16, 0.08 + i * 0.06, 0.28, -0.155, 0.09 + i * 0.06, "Metal")
    mb.box(-0.42, -0.2, -0.04, 0.42, 0.2, 0.0, "MetalDark")
    return furn("ACUnit", mb, x, y, z, rot)

def water_tank(x, y, z, rot=0, r=0.6, h=1.3, m="Chrome"):
    mb = MB()
    for sx in (-r * 0.6, r * 0.6):
        for sy in (-r * 0.6, r * 0.6):
            mb.bc(sx, sy, 0, 0.06, 0.06, 0.5, "MetalDark")
    mb.cyl(0, 0, 0.5, 0.5 + h, r, m, seg=24); mb.cyl(0, 0, 0.5 + h, 0.6 + h, r * 0.9, m, seg=24, r2=0.15)
    return furn("WaterTank", mb, x, y, z, rot)

def dish(x, y, z, rot=0):
    mb = MB()
    mb.cyl(0, 0, 0, 0.6, 0.03, "Metal", seg=8)
    mb.cyl(0, -0.1, 0.45, 0.65, 0.35, "White", seg=20, r2=0.05, axis="z")
    o = furn("Dish", mb, x, y, z, rot)
    return o

def antenna(x, y, z, h=3.0):
    mb = MB()
    mb.cyl(0, 0, 0, h, 0.025, "Metal", seg=8)
    for i in range(4):
        zz = h * (0.55 + i * 0.12)
        w = 0.9 - i * 0.15
        mb.box(-w / 2, -0.01, zz, w / 2, 0.01, zz + 0.02, "Metal")
        for j in range(5):
            u = -w / 2 + w * j / 4
            mb.box(u - 0.008, -0.2, zz, u + 0.008, 0.2, zz + 0.015, "Metal")
    return furn("Antenna", mb, x, y, z, 0)

def pipe_run(name, pts, r=0.05, m="Rust", kind="trim"):
    """polyline of straight pipes with elbows (points in local building coords)"""
    for i in range(len(pts) - 1):
        a, b = Vector(pts[i]), Vector(pts[i + 1])
        mb = MB(); mb.cyl(0, 0, 0, (b - a).length, r, m, seg=12)
        mb.sph(0, 0, 0, r * 1.25, m)
        o = mb.obj("%s_%d" % (name, i), kind=kind)
        q = Vector((0, 0, 1)).rotation_difference((b - a).normalized())
        o.matrix_world = Matrix.Translation(a) @ q.to_matrix().to_4x4()

def cable(name, p1, p2, sag=0.6, r=0.012, seg=10):
    pts = []
    for i in range(seg + 1):
        t = i / seg
        p = Vector(p1).lerp(Vector(p2), t); p.z -= sag * 4 * t * (1 - t)
        pts.append(p)
    pipe_run(name, pts, r, "Black", kind="cable")

def trash_bin(x, y, z=0, rot=0, m="PlasticGreen"):
    mb = MB(); mb.box(-0.3, -0.35, 0.05, 0.3, 0.35, 1.0, m); mb.box(-0.32, -0.37, 1.0, 0.32, 0.37, 1.06, m)
    for sx in (-0.25, 0.25):
        mb.cyl(sx, -0.3, 0, 0.1, 0.05, "Rubber", seg=10, axis="z")
    return furn("TrashBin", mb, x, y, z, rot, "use")

def crate(x, y, z=0, rot=0, s=0.6, m="WoodLight"):
    mb = MB(); mb.box(-s / 2, -s / 2, 0, s / 2, s / 2, s, m)
    for e in (0.02,):
        mb.box(-s / 2 - e, -s / 2 - e, 0, s / 2 + e, s / 2 + e, 0.06, "WoodDark"); mb.box(-s / 2 - e, -s / 2 - e, s - 0.06, s / 2 + e, s / 2 + e, s, "WoodDark")
    return furn("Crate", mb, x, y, z, rot)

def barrel(x, y, z=0, rot=0, m="PlasticBlue"):
    mb = MB(); mb.cyl(0, 0, 0, 0.9, 0.29, m, seg=20)
    for q in (0.2, 0.7):
        mb.cyl(0, 0, q, q + 0.04, 0.3, "MetalDark", seg=20)
    return furn("Barrel", mb, x, y, z, rot)

def planter(x, y, z=0, rot=0, w=1.2, d=0.4, h=0.45, m="Concrete", trailing=True):
    mb = MB()
    mb.box(-w / 2, -d / 2, 0, w / 2, d / 2, h, m)
    mb.box(-w / 2 + 0.04, -d / 2 + 0.04, h - 0.06, w / 2 - 0.04, d / 2 - 0.04, h - 0.02, "Soil")
    n = max(2, int(w / 0.25))
    for i in range(n):
        u = -w / 2 + w * (i + 0.5) / n
        mb.sph(u, RNG.uniform(-0.05, 0.05), h + 0.08, RNG.uniform(0.13, 0.18), RNG.choice(["PlantGreen", "PlantDark"]))
        if trailing and RNG.random() < 0.7:
            mb.box(u - 0.06, -d / 2 - 0.03, h - RNG.uniform(0.3, 0.7), u + 0.06, -d / 2 - 0.0, h + 0.02, "PlantGreen")
    return furn("Planter", mb, x, y, z, rot)

def tree(x, y, z=0, s=1.0, kind="broad", seed=0):
    rr = random.Random(seed)
    mb = MB()
    if kind == "palm":
        h = 6 * s; segs = 6; lean = rr.uniform(-0.8, 0.8)
        p = Vector((0, 0, 0))
        for i in range(segs):
            q = Vector((lean * ((i + 1) / segs) ** 2, 0, h * (i + 1) / segs))
            d = q - p
            mb.cyl(p.x, p.y, p.z, p.z + d.length, 0.16 * s * (1 - i * 0.08), "Bark", seg=8)
            p = q
        for a in range(9):
            t = a * 2 * math.pi / 9
            for k in range(3):
                r_ = 0.5 + k * 0.6
                mb.sph(p.x + math.cos(t) * r_ * s, p.y + math.sin(t) * r_ * s, p.z - k * k * 0.15 * s, 0.4 * s, "PlantGreen", sx=1.4, sy=0.5, sz=0.15)
        o = mb.obj("Tree_%d" % seed, x, y, z, rr.uniform(0, 360), kind="vegetation")
        return o
    if kind == "pine":
        mb.cyl(0, 0, 0, 1.2 * s, 0.15 * s, "Bark", seg=8)
        for i in range(4):
            mb.cyl(0, 0, (1.0 + i * 1.1) * s, (2.6 + i * 1.1) * s, (1.7 - i * 0.35) * s, RNG.choice(["PlantDark", "PlantGreen"]), seg=10, r2=0.05)
        return mb.obj("Tree_%d" % seed, x, y, z, 0, kind="vegetation")
    h = rr.uniform(2.2, 3.0) * s
    mb.cyl(0, 0, 0, h, 0.14 * s, "Bark", seg=10, r2=0.09 * s)
    for i in range(3):
        a = rr.uniform(0, 6.28)
        mb.cyl(0, 0, h * 0.7, h * 0.7 + 0.9 * s, 0.05 * s, "Bark", seg=6)
    for i in range(9):
        mb.sph(rr.uniform(-1, 1) * s, rr.uniform(-1, 1) * s, h + rr.uniform(0, 1.6) * s, rr.uniform(0.8, 1.2) * s,
               rr.choice(["Leaf", "PlantGreen", "Leaf"]), sub=2)
    return mb.obj("Tree_%d" % seed, x, y, z, 0, kind="vegetation")

def street_lamp(x, y, z=0, rot=0, h=5.0, power=400):
    mb = MB()
    mb.cyl(0, 0, 0, 0.4, 0.12, "MetalDark", seg=12); mb.cyl(0, 0, 0.4, h, 0.06, "MetalDark", seg=10, r2=0.045)
    mb.box(-0.03, -1.0, h - 0.05, 0.03, 0.0, h, "MetalDark")
    mb.box(-0.15, -1.25, h - 0.15, 0.15, -0.85, h - 0.02, "MetalDark"); mb.box(-0.13, -1.23, h - 0.17, 0.13, -0.87, h - 0.15, "LightWarm")
    o = furn("StreetLamp", mb, x, y, z, rot)
    ca = math.radians(rot)
    lamp("StreetLampL_%02d" % CUR.n, x + 1.05 * math.sin(ca), y - 1.05 * math.cos(ca), z + h - 0.3, power, (1.0, 0.75, 0.45), "point", fixture=False)
    return o

def boat(x, y, z=0, rot=0, l=4.5, w=1.4, m="WoodLight"):
    mb = MB()
    pts = [(-w / 2, 0.35), (-w / 2 + 0.25, 0), (w / 2 - 0.25, 0), (w / 2, 0.35), (w / 2 + 0.05, 0.55), (-w / 2 - 0.05, 0.55)]
    mb.prism(pts, -l / 2 + 0.6, l / 2 - 0.6, m, plane="xz")
    mb.prism([(-0.1, 0.1), (0.1, 0.1), (w / 2 + 0.05, 0.55), (-w / 2 - 0.05, 0.55)], l / 2 - 0.6, l / 2, m, plane="xz")
    mb.prism([(-0.1, 0.1), (0.1, 0.1), (w / 2 + 0.05, 0.55), (-w / 2 - 0.05, 0.55)], -l / 2 + 0.6, -l / 2, m, plane="xz")
    mb.box(-w / 2 + 0.1, -l / 2 + 0.7, 0.2, w / 2 - 0.1, l / 2 - 0.7, 0.24, "WoodDark")
    for v in (-0.6, 0.6):
        mb.box(-w / 2 + 0.05, v - 0.12, 0.35, w / 2 - 0.05, v + 0.12, 0.4, "WoodDark")
    mb.box(-w / 2 - 0.06, -l / 2 + 0.6, 0.5, w / 2 + 0.06, l / 2 - 0.6, 0.56, "PaintRed")
    o = furn("Boat", mb, x, y, z, rot, "use")
    return o

def car(x, y, z=0, rot=0, body="PlasticRed"):
    mb = MB()
    mb.box(-0.85, -2.1, 0.3, 0.85, 2.1, 0.85, body)
    mb.prism([(-1.2, 0.85), (1.0, 0.85), (0.6, 1.4), (-0.8, 1.4)], -0.78, 0.78, body, plane="yz")
    mb.prism([(-1.15, 0.87), (0.95, 0.87), (0.58, 1.37), (-0.78, 1.37)], -0.8, 0.8, "GlassDark", plane="yz")
    for sx in (-0.82, 0.82):
        for sy in (-1.35, 1.35):
            mb.cyl(sx - (0.1 if sx < 0 else -0.1), sy, 0.33, 0.33, 0.33, "Rubber", seg=16, axis="x")
    for sx in (-0.6, 0.6):
        mb.box(sx - 0.15, -2.12, 0.6, sx + 0.15, -2.1, 0.7, "LightCool"); mb.box(sx - 0.15, 2.1, 0.6, sx + 0.15, 2.12, 0.7, "NeonRed")
    o = furn("Car", mb, x, y, z, rot, "use")
    return o

# ---------------------------------------------------------------- room presets
def _frame(x1, y1, x2, y2, door):
    if door == "S": return (lambda u, v: (x1 + u, y1 + v)), 0, x2 - x1, y2 - y1
    if door == "N": return (lambda u, v: (x2 - u, y2 - v)), 180, x2 - x1, y2 - y1
    if door == "W": return (lambda u, v: (x1 + v, y2 - u)), 270, y2 - y1, x2 - x1
    return (lambda u, v: (x2 - v, y1 + u)), 90, y2 - y1, x2 - x1

def room(kind, x1, y1, x2, y2, z, h=2.8, door="S", light=True, var=0, fab=None):
    """Furnish a rectangle (inner wall faces). Door wall = `door`; the band within 1 m of it stays clear."""
    P, ra, W, D = _frame(x1, y1, x2, y2, door)
    def put(fn, u, v, r=0, *a, **k):
        px, py = P(u, v)
        return fn(px, py, z, (r + ra) % 360, *a, **k)
    fab = fab or RNG.choice(["FabricBlue", "FabricGreen", "FabricRed", "FabricNavy", "FabricBeige"])
    if kind == "bedroom":
        bw = 1.6 if W >= 3.2 else 1.0
        put(bed, W / 2, D - 1.05, 0, bw, 2.05, fab)
        if W >= bw + 1.0:
            put(nightstand, W / 2 - bw / 2 - 0.3, D - 0.25, 0); put(nightstand, W / 2 + bw / 2 + 0.3, D - 0.25, 0)
        if D >= 3.4:
            put(wardrobe, 0.32, D - 2.3 if D > 4 else 1.7, 90, 1.2)
        if W >= 3.0 and D >= 3.2:
            put(desk, W - 0.38, 1.6, 270, 1.2, 0.6)
        put(rug, W / 2, D - 2.3, 0, min(2.0, W - 0.6), 1.2, "CarpetGrey")
    elif kind == "living":
        put(sofa, 0.5, D / 2 + 0.2, 90, min(2.2, D - 1.6), fab)
        put(coffee_table, 1.6, D / 2 + 0.2, 90)
        put(tv, W - 0.3, D / 2 + 0.2, 270, 1.4)
        put(rug, 1.7, D / 2 + 0.2, 90, min(2.4, D - 1.4), 1.8)
        put(plant, 0.35, D - 0.35, 0, 1.0, kind="tall")
        if W > 3.2:
            put(bookshelf, W / 2, D - 0.2, 0, 1.0, 2.0)
            put(floor_lamp, W / 2 - 0.9, D - 0.3, 0)
    elif kind == "kitchen":
        kw = min(W - 1.0, 3.0)
        put(kitchen_run, kw / 2 + 0.05, D - 0.33, 0, kw)
        put(fridge, kw + 0.5, D - 0.37, 0)
        if D >= 3.0:
            put(dining_set, W / 2, max(1.6, D / 2 - 0.3), 0, 1.2, 0.75)
    elif kind == "bath":
        put(toilet, 0.4, D - 0.4, 0)
        put(vanity, 1.2 if W > 1.8 else 0.4, D - 0.27 if W > 1.8 else 1.3, 0 if W > 1.8 else 90)
        if W > 2.2:
            put(shower, W - 0.47, D - 0.47, 0)
        put(washer, W - 0.35, 1.1 if D > 2 else 0.35, 270) if W > 2.0 and D > 2.4 else None
    elif kind == "studio":
        put(bed, 0.55, D - 1.05, 0, 1.0, 2.0, fab)
        put(kitchen_run, W - 0.33, D - 1.4, 270, min(2.2, D - 1.2), uppers=True, hood=False)
        put(table, W / 2 + 0.2, D / 2 - 0.3, 0, 0.8, 0.6); put(chair, W / 2 + 0.2, D / 2 - 0.85, 180)
        put(wardrobe, 1.6, D - 0.32, 0, 0.9) if W > 3.0 else None
        put(rug, W / 2, D / 2, 0, 1.6, 1.0, "CarpetRed")
    elif kind == "office":
        n = max(1, int((W - 0.6) / 1.6))
        rows = max(1, int((D - 1.4) / 1.8))
        for r_ in range(rows):
            for i in range(n):
                put(desk, 0.9 + i * 1.6, D - 0.5 - r_ * 1.8, 0, 1.4, 0.7)
        put(plant, W - 0.4, 1.2, 0, 1.1, kind="tall")
    elif kind == "meeting":
        put(meeting_table, W / 2, D / 2 + 0.2, 0, min(3.2, W - 1.8), 1.1)
        put(tv, W / 2, D - 0.15, 0, 1.8, cab=False)
    elif kind == "storage":
        for i in range(int((W - 0.4) / 1.0)):
            put(shelf_goods, 0.7 + i * 1.0, D - 0.3, 0, 0.9, 2.0)
        put(crate, W - 0.6, 1.4, 15); put(crate, W - 0.6, 1.4, 0) if False else None
    if light:
        cx, cy = P(W / 2, D / 2)
        lamp("RoomLight", cx, cy, z + h, 60 if W * D < 12 else 110, kind="ceiling")

def scooter(x, y, z=0, rot=0, body="PlasticRed"):
    """parked moped, front toward -Y"""
    mb = MB()
    for v in (-0.62, 0.62):
        mb.cyl(-0.05, v, 0.27, 0.37, 0.27, "Rubber", seg=18, axis="x")
    mb.box(-0.16, -0.3, 0.3, 0.16, 0.65, 0.62, body)
    mb.box(-0.15, 0.05, 0.62, 0.15, 0.62, 0.75, "LeatherBlack")
    mb.box(-0.12, -0.55, 0.28, 0.12, -0.3, 1.0, body)
    mb.box(-0.3, -0.62, 1.0, 0.3, -0.56, 1.04, "MetalDark")
    mb.box(-0.06, -0.66, 0.85, 0.06, -0.62, 0.95, "LightCool")
    mb.box(-0.18, 0.62, 0.55, 0.18, 0.75, 0.62, "MetalDark")
    return furn("Scooter", mb, x, y, z, rot, "use")

def laundry(x, y, z, w=2.0, rot=0):
    mb = MB()
    mb.box(-w / 2, -0.01, 1.95, w / 2, 0.01, 1.98, "Metal")
    for i in range(int(w / 0.35)):
        c = RNG.choice(["FabricWhite", "FabricBlue", "FabricRed", "FabricBeige", "FabricGreen"])
        u = -w / 2 + 0.1 + i * 0.35
        mb.box(u, -0.01, 1.95 - RNG.uniform(0.4, 0.8), u + 0.28, 0.01, 1.95, c)
    return furn("Laundry", mb, x, y, z, rot)
