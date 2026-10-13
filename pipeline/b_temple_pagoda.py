# 天界樓閣 Heaven Gate Pavilion — 3-tier Chinese pavilion on a stone podium: red columns, lattice walls, stacked
# curled hip roofs with gold ornaments, altar hall, library, lookout; front paifang gate with neon sign + lantern strings.
begin_building("temple_pagoda", "天界樓閣", "Heaven Gate Pavilion", "Chinese Pagoda Temple (neo-oriental)", "中式樓閣廟宇",
               "landmark", "temple / landmark", ["wuxia", "fantasy", "cyberpunk-oriental", "anime", "realistic"],
               "Stone podium with front stair, 3-storey timber pavilion (altar hall / scripture library / lookout) linked by "
               "interior stairs, verandas with red columns, triple curled hip roofs, neon-lit paifang gate and red lantern strings.", 3, PLOT)

PZ = 1.2
ob("Plot", [(-12.0, -19.0, -0.4, 12.0, 11.0, 0.0)], ["StoneTile"], kind="floor", walkable=True)
ob("Podium", [(-9.0, -8.0, -0.2, 9.0, 9.0, PZ - 0.05)], ["Stone"], kind="structure")
ob("PodiumTop", [(-9.0, -8.0, PZ - 0.05, 9.0, 9.0, PZ)], ["StoneTile"], kind="floor", walkable=True)
nP = round(PZ / 0.17); LP = (nP - 1) * 0.3
stair("FrontStair", 0.0, -8.0 - LP, 0.0, PZ, "+y", 4.0, 0.3, "Stone", rails="none", solid=True)
for sx in (-1, 1):
    rail("PodRailS%d" % sx, sx * 2.05, -8.0, sx * 9.0, -8.0, PZ, 0.9, "solid" if False else "wood")
    rail("StairBal%d" % sx, sx * 2.1, -8.0 - LP, sx * 2.1, -8.0, 0.0, 0.8 + PZ * 0.5, "wood", col=False)
rail("PodRailW", -9.0, -8.0, -9.0, 9.0, PZ, 0.9, "wood"); rail("PodRailE", 9.0, -8.0, 9.0, 9.0, PZ, 0.9, "wood")
rail("PodRailN", -9.0, 9.0, 9.0, 9.0, PZ, 0.9, "wood")

R_ = "PaintRed"
def columns(x1, y1, x2, y2, z1, z2, step=2.4, r=0.2):
    mb = MB()
    nx = max(1, round((x2 - x1) / step)); ny = max(1, round((y2 - y1) / step))
    pts = set()
    for i in range(nx + 1):
        x = x1 + (x2 - x1) * i / nx
        pts.add((round(x, 3), y1)); pts.add((round(x, 3), y2))
    for j in range(ny + 1):
        y = y1 + (y2 - y1) * j / ny
        pts.add((x1, round(y, 3))); pts.add((x2, round(y, 3)))
    for (x, y) in pts:
        mb.cyl(x, y, z1, z1 + 0.25, r * 1.6, "Stone", seg=12); mb.cyl(x, y, z1 + 0.25, z2, r, R_, seg=16)
        mb.box(x - r * 1.3, y - r * 1.3, z2 - 0.2, x + r * 1.3, y + r * 1.3, z2, "Brass")
    mb.box(x1 - 0.15, y1 - 0.15, z2, x2 + 0.15, y1 + 0.15, z2 + 0.35, R_); mb.box(x1 - 0.15, y2 - 0.15, z2, x2 + 0.15, y2 + 0.15, z2 + 0.35, R_)
    mb.box(x1 - 0.15, y1, z2, x1 + 0.15, y2, z2 + 0.35, R_); mb.box(x2 - 0.15, y1, z2, x2 + 0.15, y2, z2 + 0.35, R_)
    mb.box(x1 - 0.12, y1 - 0.2, z2 + 0.08, x2 + 0.12, y1 - 0.15, z2 + 0.3, "PaintTeal")        # painted beam band
    return mb.obj("Columns_%d" % int(z1 * 10), kind="structure")

def lattice_wall(name, side, a1, a2, c, z1, z2, door=None):
    """red timber wall with gold-trimmed lattice panels (+ optional central double door)"""
    ops = []
    n = max(2, int((a2 - a1) / 1.6))
    for i in range(n):
        p1 = a1 + (a2 - a1) * i / n + 0.15; p2 = a1 + (a2 - a1) * (i + 1) / n - 0.15
        if door and p1 < door[1] and p2 > door[0]:
            continue
        ops.append((p1, p2, z1 + 0.9, z2 - 0.5, "win3", "Brass"))
    if door:
        ops.append((door[0], door[1], z1, z1 + 2.6, "door_double", R_))
    return ops

# ---------------------------------------------------------------- tiers: floors zf, columns to zc, skirt roofs between
ZF1, ZF2, ZF3 = PZ, 7.4, 12.4
ZC1, ZC2, ZC3 = ZF1 + 4.2, ZF2 + 3.2, ZF3 + 3.0
T1 = (-6.0, -5.0, 6.0, 5.5); C1 = (-7.6, -6.6, 7.6, 7.1)
T2 = (-4.5, -3.5, 4.5, 4.0); S2 = (-6.0, -5.0, 6.0, 5.5); C2 = (-5.7, -4.7, 5.7, 5.2)
T3 = (-3.0, -2.5, 3.0, 3.0); S3 = (-4.2, -3.7, 4.2, 4.2); C3 = (-4.0, -3.5, 4.0, 4.0)

# tier 1: altar hall (tall hall, ceiling = tier-2 floor)
ring("T1", *T1, ZF1, ZF2, "WoodDark", "PaintRed", 0.25, 0.0,
     {"S": lattice_wall("T1S", "S", -6.0, 6.0, -5.0, ZF1, ZC1, (-1.0, 1.0)),
      "W": lattice_wall("T1W", "W", -5.0, 5.5, -6.0, ZF1, ZC1), "E": lattice_wall("T1E", "E", -5.0, 5.5, 6.0, ZF1, ZC1),
      "N": [(-1.5, 1.5, ZF1 + 1.6, ZC1 - 0.6, "win3", "Brass")]})
slab("T1_Floor", T1[0] + 0.25, T1[1] + 0.25, T1[2] - 0.25, T1[3] - 0.25, ZF1, 0.1, top="WoodFloor", under="Stone")
columns(*C1, ZF1, ZC1)
mb = MB()                                                        # altar + statue + incense
mb.box(-1.6, -0.6, 0, 1.6, 0.6, 0.9, R_); mb.box(-1.7, -0.7, 0.9, 1.7, 0.7, 1.0, "Brass")
mb.box(-0.6, -0.4, 1.0, 0.6, 0.4, 1.3, "WoodDark")
mb.cyl(0, 0, 1.3, 2.2, 0.38, "Brass", seg=20, r2=0.28); mb.sph(0, 0, 2.45, 0.24, "Brass"); mb.sph(0, 0.1, 1.55, 0.42, "Brass", sz=0.6)
mb.cyl(0, 0.45, 1.3, 1.32, 0.9, "Brass", seg=32)
for x in (-1.2, 1.2):
    mb.cyl(x, -0.3, 1.0, 1.35, 0.06, "LightSoft", seg=10)
furn("Altar", mb, 0.0, 4.2, ZF1, 0, "use")
mb = MB(); mb.cyl(0, 0, 0.1, 0.5, 0.45, "Brass", seg=20, r2=0.55); mb.cyl(0, 0, 0.5, 0.55, 0.58, "Brass", seg=20)
for k in range(3):
    a_ = k * 2 * math.pi / 3; mb.cyl(math.cos(a_) * 0.35, math.sin(a_) * 0.35, 0.0, 0.1, 0.06, "Brass", seg=8)
for k in range(5):
    mb.cyl(-0.2 + k * 0.1, 0, 0.55, 0.9, 0.006, "PaintRed", seg=4)
furn("Censer", mb, 0.0, 1.8, ZF1, 0, "use")
for i in range(6):
    mb = MB(); mb.cyl(0, 0, 0, 0.12, 0.3, "FabricRed", seg=16); furn("Cushion", mb, -1.5 + (i % 3) * 1.5, 0.2 - (i // 3) * 1.2, ZF1, 0, "sit")
st1 = stair("T1_Stair", -5.2, -4.6, ZF1, ZF2, "+y", 0.9, 0.28, "WoodDark", rails="right", rail_style="wood")
for i, (x, y) in enumerate(((-2.5, 2.0), (2.5, 2.0), (-2.5, -2.0), (2.5, -2.0))):
    lamp("T1_Lantern%d" % i, x, y, ZF2 - 0.4, 50, (1.0, 0.45, 0.2), kind="lantern", glow="Lantern")
hip_roof("Roof1", *C1, ZC1 + 0.35, 24, 1.2, "SlateDark", "PaintRed", curl=0.7, cap="SlateDark",
         inner=(S2[0], S2[1], S2[2], S2[3], ZF2 - 0.3))

# tier 2: scripture library on a balcony ring (the T1 stair surfaces on the balcony, NW corner)
slab("T2_Floor", *S2, ZF2, 0.3, holes=[(-5.67, st1[1] - 9.5, -4.73, st1[1] + 0.02)], top="WoodFloor", under="PaintRed")
ring("T2", *T2, ZF2, ZF3, "WoodDark", "PaintRed", 0.22, 0.0,
     {"S": lattice_wall("T2S", "S", -4.5, 4.5, -3.5, ZF2, ZC2, (-0.6, 0.6)), "N": lattice_wall("T2N", "N", -4.5, 4.5, 4.0, ZF2, ZC2, (-2.6, -1.6)),
      "W": lattice_wall("T2W", "W", -3.5, 4.0, -4.5, ZF2, ZC2, (1.6, 2.6)), "E": lattice_wall("T2E", "E", -3.5, 4.0, 4.5, ZF2, ZC2)})
columns(*C2, ZF2, ZC2, 2.3, 0.16)
rail("T2_BalcS", S2[0] + 0.1, S2[1] + 0.1, S2[2] - 0.1, S2[1] + 0.1, ZF2, 0.95, "wood")
rail("T2_BalcE", S2[2] - 0.1, S2[1] + 0.1, S2[2] - 0.1, S2[3] - 0.1, ZF2, 0.95, "wood")
rail("T2_BalcN", S2[0] + 0.1, S2[3] - 0.1, S2[2] - 0.1, S2[3] - 0.1, ZF2, 0.95, "wood")
rail("T2_BalcW", S2[0] + 0.1, S2[1] + 0.1, S2[0] + 0.1, S2[3] - 0.1, ZF2, 0.95, "wood")
rail("T2_HoleE", -4.7, -4.6, -4.7, st1[1] - 0.6, ZF2, 0.95, "wood")
for i in range(3):
    bookshelf(-2.6 + i * 1.6, 3.55, ZF2, 0, 1.4, 2.4, 0.4, "WoodDark")
table(-0.8, 0.0, ZF2, 0, 2.0, 1.0, 0.75, "WoodDark"); chair(-1.3, -0.8, ZF2, 180, "WoodDark"); chair(-0.3, -0.8, ZF2, 180, "WoodDark")
lamp("T2_L", -0.8, 0.5, ZF3 - 0.6, 50, (1.0, 0.5, 0.2), kind="lantern", glow="Lantern")
st2 = stair("T2_Stair", 3.85, -3.2, ZF2, ZF3, "+y", 0.8, 0.25, "WoodDark", rails="left", rail_style="wood")
hip_roof("Roof2", *C2, ZC2 + 0.35, 24, 1.0, "SlateDark", "PaintRed", curl=0.6, cap="SlateDark",
         inner=(S3[0], S3[1], S3[2], S3[3], ZF3 - 0.3))

# tier 3: bell lookout (the T2 stair surfaces on its balcony, NE corner)
slab("T3_Floor", *S3, ZF3, 0.3, holes=[(3.43, -3.22, 4.2, st2[1] + 0.02)], top="WoodFloor", under="PaintRed")
ring("T3", *T3, ZF3, ZC3, "WoodDark", "PaintRed", 0.2, 0.0,
     {"S": [(-1.5, 1.5, ZF3, ZF3 + 2.4, "open")], "N": [(-2.0, 2.0, ZF3 + 0.9, ZF3 + 2.4, "win3", "Brass")],
      "W": [(-1.5, 2.0, ZF3 + 0.9, ZF3 + 2.4, "win3", "Brass")], "E": [(-1.5, 2.0, ZF3 + 0.9, ZF3 + 2.4, "win3", "Brass")]})
slab("T3_Ceil", *T3, ZC3, 0.15, top="PaintRed", under="PaintRed")
rail("T3_BalcS", S3[0] + 0.1, S3[1] + 0.1, S3[2] - 0.1, S3[1] + 0.1, ZF3, 0.95, "wood")
rail("T3_BalcW", S3[0] + 0.1, S3[1] + 0.1, S3[0] + 0.1, S3[3] - 0.1, ZF3, 0.95, "wood")
rail("T3_BalcN", S3[0] + 0.1, S3[3] - 0.1, S3[2] - 0.1, S3[3] - 0.1, ZF3, 0.95, "wood")
rail("T3_HoleW", 3.4, -3.2, 3.4, st2[1] - 0.6, ZF3, 0.95, "wood")
columns(*C3, ZF3, ZC3, 2.0, 0.14)
mb = MB(); mb.box(-0.9, -0.1, 2.2, 0.9, 0.1, 2.35, "WoodDark"); mb.box(-0.85, -0.08, 0, -0.75, 0.08, 2.2, "WoodDark")
mb.box(0.75, -0.08, 0, 0.85, 0.08, 2.2, "WoodDark"); mb.cyl(0, 0, 1.2, 2.2, 0.45, "Brass", seg=24, r2=0.3)
furn("Bell", mb, 0.0, 0.5, ZF3, 0, "use")
lamp("T3_L", 0.0, -1.2, ZC3 - 0.2, 40, (1.0, 0.5, 0.2), kind="lantern", glow="Lantern")
_, ztop = hip_roof("Roof3", *C3, ZC3 + 0.3, 30, 0.9, "SlateDark", "PaintRed", curl=0.55, cap="SlateDark", ornaments=True)
mb = MB()                                                        # finial
for i, r in enumerate((0.35, 0.28, 0.22, 0.16)):
    mb.sph(0, 0, 0.3 + i * 0.45, r, "Brass")
mb.cyl(0, 0, 0, 2.2, 0.05, "Brass", seg=8)
mb.obj("Finial", 0, 0.25, ztop - 0.1, kind="trim")

# ---------------------------------------------------------------- paifang gate + neon + lantern strings
GY = -16.0
mb = MB()
for x in (-4.2, -1.4, 1.4, 4.2):
    h = 5.6 if abs(x) < 2 else 4.2
    mb.box(x - 0.25, GY - 0.25, 0, x + 0.25, GY + 0.25, 0.5, "Stone"); mb.cyl(x, GY, 0.5, h, 0.2, R_, seg=16)
mb.box(-2.0, GY - 0.25, 4.9, 2.0, GY + 0.25, 5.4, R_); mb.box(-4.8, GY - 0.25, 3.6, -1.0, GY + 0.25, 4.0, R_)
mb.box(1.0, GY - 0.25, 3.6, 4.8, GY + 0.25, 4.0, R_)
mb.box(-2.0, GY - 0.27, 4.0, 2.0, GY + 0.27, 4.9, "PaintTeal")
mb.obj("Paifang", kind="structure")
hip_roof("GateRoofC", -2.2, GY - 0.4, 2.2, GY + 0.4, 5.6, 28, 0.5, "SlateDark", "PaintRed", curl=0.35, ornaments=False)
hip_roof("GateRoofL", -5.0, GY - 0.35, -1.0, GY + 0.35, 4.2, 28, 0.4, "SlateDark", "PaintRed", curl=0.3, ornaments=False)
hip_roof("GateRoofR", 1.0, GY - 0.35, 5.0, GY + 0.35, 4.2, 28, 0.4, "SlateDark", "PaintRed", curl=0.3, ornaments=False)
text("GateNeonA", "Welcome To", 0.0, GY - 0.3, 4.62, 0.3, "NeonPink", extrude=0.02)
text("GateNeonB", "天界人間", 0.0, GY - 0.3, 4.2, 0.42, "NeonPink", extrude=0.02)
lamp("GateNeonL", 0.0, GY - 1.2, 4.4, 80, (1.0, 0.3, 0.7), kind="point", fixture=False)
for side in (-1, 1):                                            # lantern strings gate -> hall
    p1 = (side * 4.2, GY, 4.1); p2 = (side * 7.5, -6.6, PZ + 3.9)
    cable("LanternLine%d" % side, p1, p2, 0.9, seg=12)
    for k in range(1, 8):
        t = k / 8
        x = p1[0] + (p2[0] - p1[0]) * t; y = p1[1] + (p2[1] - p1[1]) * t; z = p1[2] + (p2[2] - p1[2]) * t - 0.9 * 4 * t * (1 - t)
        mb = MB(); mb.sph(0, 0, -0.3, 0.2, "Lantern", sz=1.3); mb.cyl(0, 0, -0.05, 0.0, 0.07, "Black", seg=8); mb.cyl(0, 0, -0.6, -0.55, 0.07, "Black", seg=8)
        mb.obj("StringLantern%d_%d" % (side, k), x, y, z, kind="light_fixture")
        if k % 3 == 0:
            lamp("StringL%d_%d" % (side, k), x, y, z - 0.3, 20, (1.0, 0.4, 0.15), kind="point", fixture=False)
for sx in (-1, 1):                                              # guardian lion plinths
    mb = MB(); mb.box(-0.5, -0.6, 0, 0.5, 0.6, 1.0, "Stone"); mb.sph(0, 0.0, 1.5, 0.45, "Stone", sy=0.9, sz=1.1); mb.sph(0, -0.35, 2.0, 0.3, "Stone")
    furn("Lion", mb, sx * 3.0, -9.6 - 0.0 if False else -13.0, 0, 0)
mb = MB(); mb.cyl(0, 0, 0, 0.9, 0.7, "Brass", seg=20, r2=0.85); mb.cyl(0, 0, 0.9, 1.0, 0.9, "Brass", seg=20)
furn("BigCenser", mb, 0.0, -11.5, 0, 0, "use")
for x in (-10.5, 10.5):
    for y in (-15.0, -9.0, 0.0, 8.0):
        tree(x, y, 0, 0.9, "pine", seed=int(500 + x * 3 + y))

label_building(ztop + 2.6, -5.0, (1.6, -5.04, PZ + 1.6), 8.0)
spawn("gate", 0.0, GY - 2.0, 0, 0)
