# 青瓦庭院宅 Slate-Roof Courtyard House — East-Asian 2-storey timber/plaster house, blue slate hip roofs with
# upturned eaves, covered balcony reached by an outside stair, garden. (ref: isometric east-asian house)
begin_building("house_eastasian_tile", "青瓦庭院宅", "Slate-Roof Garden House", "East Asian Traditional", "東亞傳統瓦屋",
               "upscale", "house", ["realistic", "anime", "wuxia-modern", "cozy", "rpg-village"],
               "Stone plinth, dark timber G/F with living/kitchen/bath, half-timbered plaster upper floor with tatami room "
               "and bedroom, blue slate hip roofs with upturned corners, covered balcony + outside stair, garden with lantern.", 2, PLOT)

PZ = 0.6
G1, G2 = PZ, PZ + 3.0
U1, U2 = G2, G2 + 2.8
ob("Plot", [(-8.5, -8.5, -0.4, 8.5, 8.5, 0.0)], ["Grass"], kind="terrain", walkable=True)
ob("Path", [(-2.6, -8.5, 0.0, -0.8, -4.3, 0.03)], ["StoneTile"], kind="floor", walkable=True)
ob("Plinth", [(-4.75, -3.75, -0.2, 3.75, 3.75, PZ - 0.02)], ["Stone"], kind="structure")
nP = 3; LP = (nP - 1) * 0.28
stair("PorchSteps", -1.7, -3.75 - LP - 0.6, 0.0, PZ, "+y", 1.8, 0.28, "Stone", rails="none", solid=True)
ob("Porch", [(-2.8, -4.35, 0.0, -0.6, -3.75, PZ)], ["Stone"], kind="floor", walkable=True)

# ---------------------------------------------------------------- ground floor
WD = "WoodDark"
ring("GF", -4.5, -3.5, 3.5, 3.5, G1, G2, "WoodDark", "PlasterInt", 0.2, 0.03,
     {"S": [(-4.0, -2.6, G1 + 0.9, G1 + 2.3, "win", WD), (-2.2, -1.2, G1, G1 + 2.2, "door", "WoodLight"),
            (0.3, 2.8, G1 + 0.9, G1 + 2.3, "win3", WD)],
      "E": [(-2.6, -0.6, G1 + 0.9, G1 + 2.3, "win", WD), (1.2, 2.4, G1 + 1.3, G1 + 2.2, "win", WD)],
      "W": [(1.0, 2.6, G1 + 0.9, G1 + 2.2, "win", WD)],
      "N": [(-1.5, -0.3, G1 + 1.3, G1 + 2.2, "win", WD), (1.5, 2.6, G1 + 1.5, G1 + 2.2, "win", WD)]})
slab("GF_Floor", -4.3, -3.3, 3.3, 3.3, G1, 0.2, top="WoodFloor", under="Stone")
iwall("GF_P1", "y", -3.3, 3.3, -0.5, G1, G2 - 0.22, ops=[(-2.6, -1.6, G1, G1 + 2.1, "door")])
iwall("GF_P2", "x", -0.44, 3.3, 0.9, G1, G2 - 0.22, ops=[(0.4, 1.3, G1, G1 + 2.1, "door")])
# west: entry + living, stair along W wall
st = stair("GF_Stair", -3.85, -2.0, G1, G2, "+y", 0.9, 0.28, "WoodLight", rails="right", rail_style="wood")
sofa(-1.25, 0.6, G1, 270, 2.0, "FabricBeige"); coffee_table(-2.2, 0.6, G1, 90)
rug(-2.1, 0.6, G1, 90, 2.2, 1.4, "CarpetRed"); cabinet_low(-1.1, -2.7, G1, 270, 1.2) if False else None
tv(-3.2, 3.05, G1, 0, 1.2) if False else bookshelf(-2.0, 3.1, G1, 0, 1.4, 2.0)
plant(-1.0, -3.0, G1, 0, 0.9, kind="tall")
lamp("GF_LivingL", -2.0, 0.0, G2 - 0.22, 70, kind="pendant")
# east-south: kitchen/dining
kitchen_run(1.4, -3.0, G1, 180, 3.0, "WoodLight", "Marble", uppers=False)
dining_set(1.5, -1.1, G1, 0, 1.4, 0.8, "WoodDark")
lamp("GF_DiningL", 1.5, -1.1, G2 - 0.22, 50, kind="pendant")
fridge(3.0, 0.4, G1, 270)
# east-north: bath
room("bath", -0.44, 0.96, 3.3, 3.3, G1, 2.78, "S")
ob("GF_BathFloor", [(-0.44, 0.96, G1, 3.3, 3.3, G1 + 0.008)], ["TileWhite"], kind="floor", walkable=True)

# ---------------------------------------------------------------- upper floor (west block) + balcony (east)
slab("UF_Floor", -4.3, -3.3, 1.0, 3.3, U1, 0.22, holes=[(-4.3, -2.0, -3.38, st[1] + 0.02)], top="Tatami", under="Ceiling")
ring("UF", -4.5, -3.5, 1.2, 3.5, U1, U2, "Plaster", "PlasterInt", 0.2, 0.03,
     {"S": [(-3.8, -2.6, U1 + 0.9, U1 + 2.1, "win", WD), (-1.6, 0.4, U1 + 0.9, U1 + 2.1, "win3", WD)],
      "E": [(-1.4, -0.4, U1, U1 + 2.1, "slide"), (1.2, 2.6, U1 + 0.9, U1 + 2.1, "win", WD)],
      "W": [(0.4, 1.8, U1 + 0.9, U1 + 2.1, "win", WD)],
      "N": [(-1.8, 0.2, U1 + 0.9, U1 + 2.1, "win", WD)]})
iwall("UF_P1", "y", -3.3, 3.3, -2.4, U1, U2 - 0.22, ops=[(-2.0, -1.1, U1, U1 + 2.1, "door"), (1.2, 2.1, U1, U1 + 2.1, "door")])
iwall("UF_P2", "x", -2.34, 1.0, 0.06, U1, U2 - 0.22)
rail("UF_VoidRail", -3.32, -2.0, -3.32, st[1], U1, 1.0, "wood")
ob("UF_HallFloor", [(-4.3, -3.3, U1, -2.46, 3.3, U1 + 0.008)], ["WoodFloor"], kind="floor", walkable=True)
# tatami room (south)
mb = MB(); mb.box(-0.6, -0.4, 0, 0.6, 0.4, 0.32, "WoodDark"); mb.box(-0.62, -0.42, 0.32, 0.62, 0.42, 0.35, "WoodDark")
furn("LowTable", mb, -0.7, -1.6, U1, 0, "use")
for (x, y) in ((-0.7, -2.35), (-0.7, -0.85)):
    mb = MB(); mb.box(-0.3, -0.3, 0, 0.3, 0.3, 0.08, "FabricRed"); o = furn("Zabuton", mb, x, y, U1, 0, "sit")
cabinet_low(-1.9, -2.8, U1, 90, 1.2, 0.8) if False else cabinet_low(0.5, -3.05, U1, 0, 1.0, 0.6, 0.4, "WoodDark")
plant(-2.0, -3.0, U1, 0, 0.6)
lamp("UF_TatamiL", -0.7, -1.6, U2 - 0.22, 45, kind="lantern", glow="LightSoft")
# bedroom (north)
bed(-0.7, 2.25, U1, 0, 1.6, 2.0, "FabricWhite", "WoodDark")
nightstand(0.4, 3.0, U1, 0); cabinet_low(0.75, 1.0, U1, 270, 1.2, 0.8, 0.45, "WoodDark")
lamp("UF_BedL", -0.7, 1.6, U2 - 0.22, 45)
lamp("UF_HallL", -3.3, 0.0, U2 - 0.22, 30)
# half-timbering on the plaster storey
mb = MB(); o_ = 0.035
for (xa, xb, ya, yb) in ((-4.5 - o_, 1.2 + o_, -3.5 - o_ - 0.03, -3.5 - o_), (-4.5 - o_, 1.2 + o_, 3.5 + o_, 3.5 + o_ + 0.03)):
    for zz in (U1 + 0.02, U1 + 0.85, U2 - 0.12):
        mb.box(xa, ya, zz, xb, yb, zz + 0.1, WD)
    for xx in (-4.5, -3.0, -2.2, -1.75, 0.55, 1.1):
        mb.box(xx - 0.05, ya, U1, xx + 0.05, yb, U2, WD)
for (xa, xb) in ((-4.5 - o_ - 0.03, -4.5 - o_), (1.2 + o_, 1.2 + o_ + 0.03)):
    for zz in (U1 + 0.02, U1 + 0.85, U2 - 0.12):
        mb.box(xa, -3.5 - o_, zz, xb, 3.5 + o_, zz + 0.1, WD)
    for yy in (-3.45, -1.5, 0.3, 2.0, 3.45):
        mb.box(xa, yy - 0.05, U1, xb, yy + 0.05, U2, WD)
mb.obj("UF_HalfTimber", kind="trim")

# balcony over the east G/F, reached by the outside stair
slab("Balcony", 1.2, -3.5, 4.9, 3.5, U1, 0.25, holes=[(3.75, -3.5, 4.9, 1.05)], top="WoodLight", under="WoodDark", ft=0.05)
ext = stair("OutStair", 4.3, -4.25, 0.0, U1, "+y", 1.0, 0.28, "WoodLight", rails="right", rail_style="wood")
rail("BalRailS", 1.2, -3.5, 3.7, -3.5, U1, 1.0, "wood"); rail("BalRailN", 1.2, 3.5, 4.9, 3.5, U1, 1.0, "wood")
rail("BalRailE", 4.9, 1.05, 4.9, 3.5, U1, 1.0, "wood"); rail("BalRailHole", 3.72, -3.5, 3.72, 1.05, U1, 1.0, "wood")
mb = MB()
for (x, y) in ((4.8, 3.4), (4.8, 1.1), (1.35, -3.4), (3.65, -3.4), (4.8, -3.4)):
    mb.bc(x, y, 0 if x > 3.6 else U1, 0.18, 0.18, (U2 - 0.1) - (0 if x > 3.6 else U1), WD)
mb.obj("BalPosts", kind="structure")
bench(2.4, 3.15, U1, 0, 1.6, "WoodLight", "WoodDark"); plant(1.6, -3.1, U1, 0, 0.8); plant(3.3, 3.0, U1, 0, 0.9, kind="tall")
mb = MB(); mb.box(-0.3, -0.3, 0, 0.3, 0.3, 0.06, "WoodLight"); mb.box(-0.3, -0.3, 0.38, 0.3, 0.3, 0.42, "WoodLight")
furn("Tea", mb, 2.4, 1.8, U1, 0)

# ---------------------------------------------------------------- roofs
hip_roof("RoofMain", -4.5, -3.5, 1.2, 3.5, U2, 32, 0.75, "SlateBlue", curl=0.35)
hip_roof("RoofBalc", 1.2, -3.5, 4.9, 3.5, U2 - 0.15, 26, 0.6, "SlateBlue", curl=0.3)
mb = MB()                                                       # G/F pent roof skirt (front + west)
for (a, b) in (((-4.95, -3.95), (1.2, -3.5)),):
    pass
mb.quad([(-5.2, -4.45, G2 - 0.25), (1.2, -4.45, G2 - 0.25), (1.2, -3.53, G2 + 0.3), (-5.2, -3.53, G2 + 0.3)], "SlateBlue", 0.12)
mb.quad([(-5.45, -4.45, G2 - 0.25), (-5.45, 4.2, G2 - 0.25), (-4.53, 4.2, G2 + 0.3), (-4.53, -3.53, G2 + 0.3)], "SlateBlue", 0.12)
mb.obj("SkirtRoof", kind="roof")
pipe_run("SkirtCap", [(-5.45, -4.45, G2 - 0.2), (1.2, -4.45, G2 - 0.2)], 0.05, "SlateDark")
mb = MB()                                                       # brackets under the skirt
for x in (-4.6, -2.8, -0.6, 1.0):
    mb.prism([(-3.53, G2 - 0.9), (-3.53, G2 - 0.2), (-4.2, G2 - 0.2)], x - 0.05, x + 0.05, WD, plane="yz")
mb.obj("SkirtBrackets", kind="trim")

# ---------------------------------------------------------------- garden
lamp("EntryLampL", -2.45, -3.62, G1 + 2.0, 25, kind="wall"); lamp("EntryLampR", -0.95, -3.62, G1 + 2.0, 25, kind="wall")
sign_board("Nameplate", "青瓦居", -1.7, -3.6, G1 + 2.45, 0.9, 0.3, 0, "WoodDark", "LabelGlow", 0.18)
mb = MB()                                                       # stone lantern (toro)
mb.box(-0.25, -0.25, 0, 0.25, 0.25, 0.15, "Stone"); mb.cyl(0, 0, 0.15, 0.75, 0.08, "Stone", seg=8)
mb.box(-0.22, -0.22, 0.75, 0.22, 0.22, 0.82, "Stone"); mb.box(-0.16, -0.16, 0.82, 0.16, 0.16, 1.1, "LightSoft")
mb.cyl(0, 0, 1.1, 1.32, 0.34, "Stone", seg=4, r2=0.04)
furn("StoneLantern", mb, -4.6, -6.0, 0, 45)
lamp("StoneLanternL", -4.6, -6.0, 1.0, 15, kind="point", fixture=False)
for i, (x, y, s) in enumerate(((-7.0, -6.5, 1.0), (6.8, -6.2, 1.2), (-7.2, 5.8, 1.3), (6.6, 6.4, 0.9), (6.9, 0.0, 1.1))):
    tree(x, y, 0, s, "broad", seed=40 + i)
for i in range(10):
    plant(-6.5 + (i % 5) * 0.9, -7.6 + (i // 5) * 0.8 if i < 5 else 7.6, 0, 0, 0.7, "Terracotta" if i % 2 else "Concrete")
for (x, y) in ((-5.8, -2.0), (-5.8, 0.0), (-5.8, 2.0), (2.0, -5.6), (3.5, -6.2)):
    mb = MB(); mb.sph(0, 0, 0.3, 0.55, RNG.choice(["PlantGreen", "PlantDark"]), sz=0.7); furn("Shrub", mb, x, y, 0, 0)
crate(5.8, -4.6, 0, 20, 0.5); barrel(6.2, -3.8, 0, 0, "Terracotta")
mb = MB(); mb.box(-0.35, -0.12, 0, 0.35, 0.12, 0.9, "Stone"); mb.box(-0.3, -0.13, 0.55, 0.3, -0.12, 0.8, "MetalDark")
furn("Mailbox", mb, -3.3, -8.0, 0, 0, "use")

label_building(U2 + 3.0, -4.6, (-2.55, -3.56, G1 + 1.5), 7.0)
spawn("garden_gate", -1.7, -8.4, 0, 0)
