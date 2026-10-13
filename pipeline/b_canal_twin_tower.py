# 運河雙子樓 Canal Twin Houses — two joined narrow towers (teal 5F + ochre 6F with hip roof) on a stone pier in the
# harbour, shops at the quay, lanterns, jetty with boats, boardwalk to the beach. (ref: isometric canal towers at dusk)
begin_building("canal_twin_tower", "運河雙子樓", "Canal Twin Houses", "Harbour Canal Townhouses", "港灣運河樓房",
               "standard", "mixed-use townhouses", ["realistic", "anime", "ghibli", "fantasy-port", "slice-of-life"],
               "Stone quay platform in the water with a teal 5-storey and an ochre 6-storey tower sharing one U-stair; "
               "G/F grocery + noodle bar, flats above, roof terrace, lanterns, jetty with two rowing boats, boardwalk to shore.", 6, PLOT)

QZ = 0.0
ob("Quay", [(-9.0, -9.0, -3.2, 9.0, 8.0, QZ)], ["Block"], kind="structure")
ob("QuayTop", [(-9.05, -9.05, QZ - 0.02, 9.05, 8.05, QZ + 0.02)], ["Cobble"], kind="floor", walkable=True)
ob("QuayCurb", [(-9.15, -9.15, QZ - 0.3, 9.15, -8.95, QZ + 0.12), (-9.15, 7.95, QZ - 0.3, 9.15, 8.15, QZ + 0.12),
                (-9.15, -8.95, QZ - 0.3, -8.95, 7.95, QZ + 0.12), (8.95, -8.95, QZ - 0.3, 9.15, 7.95, QZ + 0.12)], ["Stone"], kind="trim")
# boardwalk to shore (local -Y) + jetty (east)
ob("Boardwalk", [(-1.4, -28.0, QZ - 0.25, 1.4, -9.0, QZ - 0.02)], ["WoodLight"], kind="floor", walkable=True)
mb = MB()
for y in range(-27, -9, 3):
    for x in (-1.3, 1.3):
        mb.cyl(x, y, -2.6, QZ + 0.9, 0.12, "WoodDark", seg=10)
mb.obj("BoardwalkPiles", kind="structure")
rail("BWRailW", -1.4, -28.0, -1.4, -9.05, QZ - 0.02, 1.0, "wood"); rail("BWRailE", 1.4, -28.0, 1.4, -9.05, QZ - 0.02, 1.0, "wood")
ob("Jetty", [(9.0, -6.0, QZ - 0.6, 13.5, -4.2, QZ - 0.4)], ["WoodLight"], kind="floor", walkable=True)
n = 3; stair("JettySteps", 9.45, -5.1, QZ - 0.4, QZ, "-x", 1.6, 0.28, "WoodLight", rails="none")
mb = MB()
for x in (10.0, 11.5, 13.0):
    for y in (-6.1, -4.1):
        mb.cyl(x, y, -2.6, QZ - 0.2, 0.12, "WoodDark", seg=10)
mb.obj("JettyPiles", kind="structure")
boat(11.4, -7.6, -0.75, 90, 4.5, 1.4, "WoodLight"); boat(11.6, -2.5, -0.75, 95, 4.2, 1.3, "PaintTeal")

ZA = [QZ + 3.2 * i for i in range(6)]          # tower A: 5 floors, roof terrace at ZA[5]
ZB = [QZ + 3.2 * i for i in range(7)]          # tower B: 6 floors + hip roof
AX1, AX2, AY1, AY2 = -6.6, -0.5, -6.6, 0.6
BX1, BX2, BY1, BY2 = -0.5, 5.7, -3.4, 5.2
SX, SY = 4.05, 1.6
# ---------------------------------------------------------------- tower B (ochre, shared stair)
hole = None
for f in range(6):
    z0, z1 = ZB[f], ZB[f + 1]
    link = (-3.0, -2.1, z0 + (0.0 if f else 0.0), z0 + 2.15, "open") if f <= 5 else None
    ops = {"S": ([(0.0, 2.6, z0 + 0.3, z0 + 2.9, "shop", "WoodDark"), (2.9, 3.9, z0, z0 + 2.3, "door", "PaintRed")] if f == 0 else
                 [(0.4, 2.2, z0 + 0.9, z0 + 2.3, "win3", "WoodDark"), (3.0, 4.0, z0 + 1.0, z0 + 2.2, "win", "WoodDark")]),
           "E": [(-2.6, -1.2, z0 + 0.9, z0 + 2.3, "win", "WoodDark"), (0.2, 1.0, z0 + 0.9, z0 + 2.2, "win", "WoodDark")] if f else
                [(-2.4, -1.4, z0 + 1.0, z0 + 2.4, "win", "WoodDark")],
           "N": [(0.2, 2.2, z0 + 0.9, z0 + 2.3, "win", "WoodDark"), (3.2, 4.8, z0 + 1.6 + 0.8, z0 + 3.0, "win", "WoodDark")],
           "W": [link, (1.2, 2.6, z0 + 0.9, z0 + 2.3, "win", "WoodDark")]}
    ring("B%d" % (f + 1), BX1, BY1, BX2, BY2, z0, z1, "Plaster" if f else "Stone", "PlasterInt", 0.22, 0.03, ops)
    if f:
        slab("B%d_Floor" % (f + 1), BX1 + 0.22, BY1 + 0.22, BX2 - 0.22, BY2 - 0.22, z0, 0.22, holes=[hole], top="WoodFloor")
    else:
        slab("B1_Floor", BX1 + 0.22, BY1 + 0.22, BX2 - 0.22, BY2 - 0.22, z0 + 0.0, 0.2, top="StoneTile", under="Stone")
    if f < 5:
        hole, arrive = stair_u("B%d_Stair" % (f + 1), SX, SY, z0, z1, "+y", 0.95, 0.1, m="WoodLight", rail_style="wood")
    lamp("B%d_StairL" % (f + 1), SX, 3.6, z1 - 0.22, 25)
slab("B_Ceil", BX1 + 0.22, BY1 + 0.22, BX2 - 0.22, BY2 - 0.22, ZB[6], 0.22, top="WoodLight", under="Ceiling")
iwall("B_StairHallP", "y", BY1 + 0.22, BY2 - 0.22, 2.9, ZB[0], ZB[1] - 0.22, ops=[(-2.6, -1.6, ZB[0], ZB[0] + 2.1, "door")])
hip_roof("B_Roof", BX1, BY1, BX2, BY2, ZB[6], 34, 0.55, "SlateDark", curl=0.08, ornaments=False)
# tower A (teal) shares B's west wall
for f in range(5):
    z0, z1 = ZA[f], ZA[f + 1]
    ops = {"S": ([(-6.2, -3.4, z0 + 0.3, z0 + 2.9, "shop", "WoodDark"), (-3.1, -2.1, z0, z0 + 2.3, "door", "PaintRed"),
                  (-1.8, -0.8, z0 + 0.9, z0 + 2.6, "win", "WoodDark")] if f == 0 else
                 [(-6.0, -4.2, z0 + 0.9, z0 + 2.3, "win3", "WoodDark"), (-3.2, -2.2, z0, z0 + 2.3, "door_glass"), (-1.6, -0.9, z0 + 1.0, z0 + 2.2, "win", "WoodDark")]),
           "W": [(-5.6, -3.6, z0 + 0.9, z0 + 2.3, "win", "WoodDark"), (-1.6, -0.4, z0 + 1.0, z0 + 2.2, "win", "WoodDark")],
           "N": [(-5.8, -4.4, z0 + 0.9, z0 + 2.3, "win", "WoodDark")]}
    ring("A%d" % (f + 1), AX1, AY1, AX2, AY2, z0, z1, "PaintTeal" if f else "Stone", "PlasterInt", 0.22, 0.03, ops, sides="SNW")
    ob("A%d_WallE" % (f + 1), [(AX2 - 0.22, AY1, z0, AX2 + 0.03, BY1, z1)], ["PaintTeal" if f else "Stone"], kind="wall")
    if f:
        slab("A%d_Floor" % (f + 1), AX1 + 0.22, AY1 + 0.22, AX2, AY2 - 0.22, z0, 0.22, top="WoodFloor")
    else:
        slab("A1_Floor", AX1 + 0.22, AY1 + 0.22, AX2, AY2 - 0.22, z0, 0.2, top="StoneTile", under="Stone")
slab("A_Roof", AX1, AY1, AX2, AY2, ZA[5], 0.22, top="TileWhite", under="Ceiling")
rails_rect("A_RoofRail", AX1 + 0.05, AY1 + 0.05, AX2 - 0.05, AY2 - 0.05, ZA[5], "SW", style="bar")
rail("A_RoofRailN", AX1 + 0.05, AY2 - 0.05, AX2 - 0.05, AY2 - 0.05, ZA[5], 1.0, "bar")
rail("A_RoofRailE", AX2 - 0.05, AY1 + 0.05, AX2 - 0.05, BY1, ZA[5], 1.0, "bar")
# B's top-floor west door onto A's roof terrace
for f, z0 in enumerate(ZA[:5]):
    zc = ZA[f + 1] - 0.22
    if f == 0:
        shelf_goods(-5.9, -3.0, z0, 90, 2.4, 1.8, 0.4); shelf_goods(-3.6, -1.2, z0, 0, 2.6, 1.6, 0.6, double=True)
        shop_counter(-1.6, -4.6, z0, 90, 1.6, "WoodDark", "WoodLight"); drinks_fridge(-5.9, -0.2, z0, 90, 1.0, 2.0)
        lamp("A1_L", -3.6, -3.0, zc, 70, (1.0, 0.8, 0.55))
    else:
        room("studio", AX1 + 0.22, AY1 + 0.22, AX2 - 0.22, AY2 - 0.22, z0, zc - z0, "E", fab=["FabricRed", "FabricBlue", "FabricGreen", "FabricBeige"][f - 1])
for f, z0 in enumerate(ZB[:6]):
    zc = ZB[f + 1] - 0.22
    if f == 0:
        bar_counter(0.6, -0.6, z0, 0, 2.6, "WoodDark", "WoodLight")
        kitchen_run(1.2, 1.0 + 0.0, z0, 0, 2.6, "Metal", "Chrome", uppers=False) if False else kitchen_run(1.3, 4.65, z0, 0, 2.6, "Metal", "Chrome")
        cafe_set(1.2, -2.6, z0, 0, "WoodLight", "WoodDark")
        for i, x in enumerate((0.0, 1.4)):
            lamp("B1_Lantern%d" % i, x, -1.0, zc, 35, (1.0, 0.5, 0.2), kind="lantern", glow="Lantern")
    else:
        room("living", BX1 + 0.22, BY1 + 0.22, 2.84, 0.6, z0, zc - z0, "E", fab="FabricBeige")
        room("bedroom", BX1 + 0.22, 0.72, 2.84, BY2 - 0.22, z0, zc - z0, "E", fab=["FabricBlue", "FabricWhite", "FabricRed", "FabricNavy", "FabricGreen"][f - 1])
        iwall("B%d_P" % (f + 1), "x", BX1 + 0.22, 2.84, 0.66, z0, zc)
        iwall("B%d_HallP" % (f + 1), "y", BY1 + 0.22, BY2 - 0.22, 2.9, z0, zc, ops=[(-1.0, -0.1, z0, z0 + 2.1, "door"), (2.6, 3.5, z0, z0 + 2.1, "door")])

# ---------------------------------------------------------------- dressing: awnings, signs, lanterns, clutter
mb = MB()
mb.prism([(AY1 - 0.03, 2.75), (AY1 - 1.4, 2.4), (AY1 - 1.4, 2.5), (AY1 - 0.03, 2.95)], -6.5, -3.0, "AwningGreen", plane="yz")
mb.obj("AwningA", kind="trim")
mb = MB()
for i in range(8):
    mb.prism([(BY1 - 0.03, 2.75), (BY1 - 1.4, 2.4), (BY1 - 1.4, 2.5), (BY1 - 0.03, 2.95)], -0.3 + i * 0.36, -0.12 + i * 0.36,
             "AwningRed" if i % 2 == 0 else "AwningWhite", plane="yz")
mb.obj("AwningB", kind="trim")
sign_board("SignA", "百匯商店", -4.8, AY1 - 0.1, 3.1, 2.6, 0.38, 0, "WoodDark", "Lantern", 0.26)
sign_board("SignB", "港口麵館", 1.3, BY1 - 0.1, 3.1, 2.6, 0.38, 0, "PaintRed", "NeonYellow", 0.26)
neon_vertical("BladeB", "麵", BX2 + 0.15, -2.6, 4.8, 1.0, 90, "NeonOrange", size=0.5)
for i, (x, y, z) in enumerate(((-6.3, AY1 - 1.2, 2.8), (-3.2, AY1 - 1.2, 2.8), (0.2, BY1 - 1.2, 2.8), (4.6, BY1 - 1.2, 2.8),
                                (-0.4, AY1 - 0.4, 9.0), (5.2, BY1 - 0.4, 12.4), (-6.8, -2.0, 6.0))):
    lamp("Lantern%d" % i, x, y, z, 35, (1.0, 0.5, 0.2), kind="lantern", glow="Lantern")
for f in (1, 2, 3):
    ac_unit(AX1 - 0.2, -1.5, ZA[f] + 2.4, 270); ac_unit(BX2 + 0.2, 3.5, ZB[f + 1] + 2.4, 90)
for f in (2, 4):
    slab("A_Balc%d" % f, -6.2, AY1 - 1.0, -4.0, AY1 - 0.03, ZA[f], 0.15, top="WoodLight", under="WoodDark")
    rails_rect("A_BalcR%d" % f, -6.2, AY1 - 1.0, -4.0, AY1 - 0.03, ZA[f], "SWE", style="wood")
    plant(-5.6, AY1 - 0.55, ZA[f], 0, 0.7)
for i, (x, y) in enumerate(((-7.6, -7.6), (-7.8, 2.0), (7.5, 6.6), (7.6, -7.4))):
    plant(x, y, QZ, 0, 1.0, "Terracotta", ["bush", "tall", "palm", "bush"][i])
for i in range(4):
    crate(6.6 + (i % 2) * 0.7, -7.6 + (i // 2) * 0.7, QZ, 15 * i, 0.6)
barrel(7.8, -5.6, QZ, 0, "PlasticBlue"); bench(-4.0, -8.3, QZ, 180, 2.0, "WoodLight", "MetalDark")
water_tank(-2.4, -2.0, ZA[5], 0, 0.5, 1.0, "Chrome"); antenna(-6.0, 0.0, ZA[5], 2.8); dish(-3.5, -6.0, ZA[5], 180)
umbrella_table(-4.4, -3.4, ZA[5], 0, "AwningRed")
mb = MB()                                                        # mooring bollards + street lamp poles on the quay
for (x, y) in ((-8.5, -8.5), (8.5, -8.5), (8.5, 7.5), (-8.5, 7.5), (8.5, -1.0)):
    mb.cyl(x, y, QZ, QZ + 0.5, 0.15, "MetalDark", seg=12); mb.cyl(x, y, QZ + 0.5, QZ + 0.6, 0.2, "MetalDark", seg=12)
mb.obj("Bollards", kind="trim")
street_lamp(-8.2, -7.0, QZ, 180, 4.2, 200); street_lamp(8.2, 2.0, QZ, 270, 4.2, 200)
for i in range(4):
    cable("Line%d" % i, (AX1, AY1 + 0.3, 6.0 + i * 2.5), (BX2, BY1, 7.5 + i * 2.2), 0.7)

label_building(ZB[6] + 3.6 + 1.2, BY1 - 0.4, (-2.6, AY1 - 0.04, 2.55), 9.0)
spawn("boardwalk", 0.0, -26.0, QZ - 0.02, 0)
