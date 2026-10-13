# 夜巷住商公寓 Night-Alley Mixed-Use Apartment — 5 storeys: ramen shop + 3 flats + rooftop studio.
# Refs: night city cut-away apartment towers. Walkable: shared U-stair core (E side), every floor + roof terrace.
begin_building("apt_urban_5f", "夜巷住商公寓", "Night Alley Mixed-Use Apartment", "Urban Asian Mixed-Use", "都市亞洲住商",
               "standard", "apartment", ["realistic", "anime", "slice-of-life", "cyberpunk-lite"],
               "5F walk-up: G/F ramen shop with counter seating, 2F-4F one-bedroom flats with balcony, 5F loft studio, "
               "roof terrace with water tank. Shared U-stair core.", 5, PLOT)

X1, X2, Y1, Y2, T = -5.0, 5.0, -4.5, 4.5, 0.2
xi1, xi2, yi1, yi2 = X1 + T, X2 - T, Y1 + T, Y2 - T
Z = [0.0, 3.6, 6.8, 10.0, 13.2, 16.4]
ST = 0.22
HX = 2.55                       # hall partition centre
SX, SY = 3.7, 0.4               # stair front-edge centre

ob("Plot", [(-6.6, -7.2, -0.4, 6.6, 6.2, 0.0)], ["StoneTile"], kind="floor", walkable=True)
slab("F1_Floor", xi1, yi1, xi2, yi2, 0.0, 0.2, top="StoneTile", under="Concrete")

hole = None
for f in range(5):
    z0, z1 = Z[f], Z[f + 1]; H = z1 - z0
    lw = z0 + H / 2 + 0.8          # landing window
    if f == 0:
        ops = {"S": [(-4.6, -0.6, 0.35, 3.1, "shop"), (-0.4, 0.6, 0, 2.4, "door_glass"), (0.8, 2.3, 0.35, 3.1, "shop"),
                     (3.2, 4.2, 0, 2.4, "door_glass")],
               "N": [(-3.8, -1.6, 2.35, 3.05, "win"), (-0.8, 0.1, 0, 2.1, "door_metal"), (3.3, 4.3, lw, lw + 0.7, "win")],
               "W": [(-3.0, -1.0, 1.0, 2.9, "win")]}
        ext = "BrickDark"
    elif f < 4:
        ops = {"S": [(-4.4, -2.6, z0 + 0.9, z0 + 2.4, "grille" if f == 1 else "win"), (-1.9, -0.9, z0, z0 + 2.4, "door_glass"),
                     (-0.4, 1.8, z0 + 0.9, z0 + 2.4, "win3"), (3.0, 4.4, z0 + 1.0, z0 + 2.2, "win")],
               "N": [(-4.0, -1.6, z0 + 1.2, z0 + 2.3, "win"), (0.3, 1.2, z0 + 1.5, z0 + 2.2, "win"), (3.3, 4.3, lw, lw + 0.7, "win")],
               "W": [(0.9, 1.6, z0 + 1.0, z0 + 2.2, "win")]}
        ext = "MosaicBeige"
    else:
        ops = {"S": [(-4.4, -0.4, z0 + 0.4, z0 + 2.6, "win3"), (0.4, 1.4, z0, z0 + 2.4, "door_glass"), (3.0, 4.4, z0 + 1.0, z0 + 2.2, "win")],
               "N": [(-4.2, -0.4, z0 + 0.9, z0 + 2.5, "win3"), (3.3, 4.3, lw, lw + 0.7, "win")],
               "W": [(-2.0, 2.0, z0 + 0.9, z0 + 2.4, "win3")]}
        ext = "MosaicBeige"
    ring("F%d" % (f + 1), X1, Y1, X2, Y2, z0, z1, ext, "PlasterInt", T, 0.03, ops)
    if f > 0:
        slab("F%d_Floor" % (f + 1), xi1, yi1, xi2, yi2, z0, ST, holes=[hole], top="WoodFloor")
    hole, arrive = stair_u("F%d_Stair" % (f + 1), SX, SY, z0, z1, "+y", 1.0, 0.1, m="Concrete", solid=False)
    # hall partition (flats have a door into the hall)
    hops = [] if f == 0 else [(-2.0, -1.1, z0, z0 + 2.1, "door")]
    iwall("F%d_HallWall" % (f + 1), "y", yi1, yi2, HX, z0, z1 - ST, ops=hops)
    ob("F%d_HallFloor" % (f + 1), [(HX + 0.06, yi1, z0, xi2, SY, z0 + 0.008)], ["TileWhite"], kind="floor", walkable=True)
    lamp("F%d_HallLight" % (f + 1), 3.7, -2.0, z1 - ST, 40, (1.0, 0.85, 0.65))
    lamp("F%d_LandingLight" % (f + 1), 4.6, 3.7, z0 + H / 2 + 1.6, 25, (1.0, 0.85, 0.65), kind="wall")

# roof slab with the last stair hole + exterior floor bands
slab("Roof", xi1, yi1, xi2, yi2, Z[5], ST, holes=[hole], top="Concrete", under="Ceiling")
for f in range(1, 6):
    z = Z[f]
    ob("Band%d" % f, [(X1 - 0.09, Y1 - 0.09, z - 0.14, X2 + 0.09, Y1 - 0.03, z + 0.1),
                      (X1 - 0.09, Y2 + 0.03, z - 0.14, X2 + 0.09, Y2 + 0.09, z + 0.1),
                      (X1 - 0.09, Y1 - 0.03, z - 0.14, X1 - 0.03, Y2 + 0.03, z + 0.1),
                      (X2 + 0.03, Y1 - 0.03, z - 0.14, X2 + 0.09, Y2 + 0.03, z + 0.1)], ["Concrete"], kind="trim")

# ---------------------------------------------------------------- G/F ramen shop
z0 = 0.0
iwall("F1_RR_A", "x", 0.9, HX - 0.06, 2.6, 0, Z[1] - ST, ops=[(1.45, 2.2, 0, 2.1, "door")])
iwall("F1_RR_B", "y", 2.66, yi2, 0.9, 0, Z[1] - ST)
toilet(1.3, 3.95, 0, 0); vanity(2.05, 4.04, 0, 0, 0.6)
ob("F1_RRFloor", [(0.96, 2.66, 0, HX - 0.06, yi2, 0.008)], ["TileBlue"], kind="floor", walkable=True)
lamp("F1_RRLight", 1.7, 3.45, Z[1] - ST, 25)
kitchen_run(-2.6, 3.97, 0, 0, 3.0, m="Metal", top="Chrome", uppers=True)
fridge(-4.42, 3.95, 0, 0)
bar_counter(-1.6, 1.4, 0, 0, 5.2, m="WoodDark", top="WoodLight")
cafe_set(-3.6, -3.0, 0, 0); cafe_set(-1.7, -3.0, 0, 0)
shelf_goods(-4.55, -0.6, 0, 90, 1.4, 1.6, 0.35)
for i, x in enumerate((-3.6, -1.6, 0.4)):
    lamp("F1_Pendant%d" % i, x, 1.4, Z[1] - ST, 45, kind="pendant")
lamp("F1_Ceil", -2.6, -2.8, Z[1] - ST, 80)
picture(-4.79, -2.2, 1.9, 90, 1.2, 0.8, "Paper")                  # menu board
# hall mailboxes
mb = MB()
mb.box(-0.6, -0.12, 0, 0.6, 0.12, 0.9, "Metal")
for i in range(4):
    for j in range(2):
        mb.box(-0.55 + i * 0.28, -0.125, 0.1 + j * 0.4, -0.31 + i * 0.28, -0.12, 0.42 + j * 0.4, "MetalDark")
furn("Mailboxes", mb, 4.68, -2.6, 1.0, 90, "use")

# ---------------------------------------------------------------- 2F-4F flats
for f in (1, 2, 3):
    z0 = Z[f]; zc = Z[f + 1] - ST
    iwall("F%d_P1" % (f + 1), "x", xi1, HX - 0.06, 0.6, z0, zc, ops=[(-1.5, -0.6, z0, z0 + 2.1, "door"), (1.5, 2.3, z0, z0 + 2.1, "door")])
    iwall("F%d_P2" % (f + 1), "y", 0.66, yi2, -0.54, z0, zc)
    ob("F%d_BathFloor" % (f + 1), [(-0.48, 0.66, z0, HX - 0.06, yi2, z0 + 0.008)], ["TileWhite"], kind="floor", walkable=True)
    # kitchen + dining
    kitchen_run(-4.49, -1.6, z0, 90, 2.6)
    fridge(-4.43, 0.1, z0, 90)
    dining_set(-2.7, -1.7, z0, 0, 1.2, 0.75, "WoodLight")
    # living
    sofa(0.3, 0.07, z0, 0, 2.1, ["FabricGreen", "FabricNavy", "FabricRed"][f - 1])
    coffee_table(0.3, -1.4, z0, 0)
    rug(0.3, -1.5, z0, 0, 2.4, 1.6, ["CarpetRed", "CarpetGrey", "CarpetRed"][f - 1])
    tv(0.5, -4.0, z0, 180, 1.3)
    plant(2.15, -3.9, z0, 0, 1.0, kind="tall")
    lamp("F%d_LivingLight" % (f + 1), 0.0, -2.0, zc, 90)
    lamp("F%d_KitchenLight" % (f + 1), -3.2, -1.7, zc, 60, kind="pendant")
    room("bedroom", xi1, 0.66, -0.6, yi2, z0, zc - z0, "S", fab=["FabricBlue", "FabricBeige", "FabricWhite"][f - 1])
    room("bath", -0.48, 0.66, HX - 0.06, yi2, z0, zc - z0, "S")
    # balcony
    slab("F%d_Balcony" % (f + 1), -2.6, Y1 - 1.25, 0.0, Y1 - 0.03, z0, 0.18, top="StoneTile", under="Concrete")
    rails_rect("F%d_BalRail" % (f + 1), -2.6, Y1 - 1.25, 0.0, Y1 - 0.03, z0, "SWE", style="bar")
    ac_unit(-0.45, Y1 - 0.25, z0 + 0.04, 180)
    plant(-2.3, Y1 - 0.95, z0, 0, 0.8)
    ac_unit(X1 - 0.2, -3.0, z0 + 2.4, 270)

# ---------------------------------------------------------------- 5F loft studio
z0 = Z[4]; zc = Z[5] - ST
room("studio", xi1, yi1, HX - 0.06, yi2, z0, zc - z0, "E", fab="FabricRed")
bookshelf(0.8, 4.12, z0, 0, 1.2, 2.2)
desk(-1.6, -3.9, z0, 180, 1.4, 0.7)
sofa(1.4, -1.0, z0, 270, 1.9, "FabricBeige")
plant(-4.4, 3.9, z0, 0, 1.2, kind="palm")
mb = MB()                                                         # easel with canvas
mb.box(-0.03, -0.3, 0, 0.03, -0.26, 1.7, "WoodLight"); mb.box(-0.4, 0.15, 0, -0.36, 0.19, 1.6, "WoodLight")
mb.box(0.36, 0.15, 0, 0.4, 0.19, 1.6, "WoodLight"); mb.box(-0.45, -0.22, 0.75, 0.45, -0.18, 1.45, "PaintTeal")
furn("Easel", mb, -3.5, -2.0, z0, 30, "use")
lamp("F5_Light1", -2.5, -1.5, zc, 90); lamp("F5_Light2", -0.5, 2.0, zc, 70)
slab("F5_Balcony", -0.4, Y1 - 1.55, 2.4, Y1 - 0.03, z0, 0.18, top="WoodLight", under="Concrete")
rails_rect("F5_BalRail", -0.4, Y1 - 1.55, 2.4, Y1 - 0.03, z0, "SWE", style="glass")
umbrella_table(1.0, Y1 - 0.85, z0, 0) if False else round_table(1.0, Y1 - 0.8, z0, 0, 0.3)
chair(0.3, Y1 - 0.8, z0, 270, "MetalDark"); chair(1.7, Y1 - 0.8, z0, 90, "MetalDark")

# ---------------------------------------------------------------- roof terrace + stair penthouse
zr = Z[5]
ob("Parapet", [(X1, Y1, zr, X2, Y1 + 0.2, zr + 1.0), (X1, Y1 + 0.2, zr, X1 + 0.2, Y2, zr + 1.0),
               (X1 + 0.2, Y2 - 0.2, zr, 2.4, Y2, zr + 1.0), (X2 - 0.2, Y1 + 0.2, zr, X2, -1.6, zr + 1.0)],
   ["Concrete"], kind="wall")
ob("ParapetCap", [(X1 - 0.04, Y1 - 0.04, zr + 1.0, X2 + 0.04, Y1 + 0.24, zr + 1.06),
                  (X1 - 0.04, Y1 + 0.24, zr + 1.0, X1 + 0.24, Y2 + 0.04, zr + 1.06),
                  (X1 + 0.24, Y2 - 0.24, zr + 1.0, 2.4, Y2 + 0.04, zr + 1.06)], ["Stone"], kind="trim")
ring("PH", 2.4, -1.6, X2, Y2, zr, zr + 2.7, "Concrete", "PlasterInt", 0.2, 0.0,
     {"S": [(3.5, 4.5, zr, zr + 2.2, "door_metal")], "W": [(1.0, 2.2, zr + 1.2, zr + 2.0, "win")]})
slab("PH_Roof", 2.4, -1.6, X2, Y2, zr + 2.9, 0.2, top="Concrete", under="Ceiling", walk=True)
lamp("PH_Light", 3.7, 1.5, zr + 2.7, 30)
lamp("PH_DoorLight", 4.0, -1.75, zr + 2.4, 30, kind="wall")
water_tank(3.7, 2.6, zr + 2.9, 0, 0.7, 1.2)
antenna(2.9, 0.2, zr + 2.9, 3.2)
dish(4.5, -0.8, zr + 2.9, 200)
for i, (x, y) in enumerate(((-4.2, 3.0), (-4.2, 1.6), (-2.0, 3.8))):
    ac_unit(x, y, zr, 90 if i < 2 else 0)
pipe_run("RoofPipe", [(-3.6, 2.2, zr + 0.3), (-1.2, 2.2, zr + 0.3), (-1.2, 2.2, zr + 1.4), (2.4, 2.2, zr + 1.4)], 0.06, "Rust")
pipe_run("DownPipe", [(X2 + 0.1, Y1 + 0.3, 0.2), (X2 + 0.1, Y1 + 0.3, zr + 0.9)], 0.06, "MetalDark")
for i in range(3):
    plant(-3.8 + i * 1.3, -3.9, zr, 0, 1.0 + 0.2 * i, kind=["bush", "tall", "palm"][i])
bench(-1.0, -3.95, zr, 180, 1.6)
# clothesline
mb = MB()
for x in (-4.2, -0.8):
    mb.cyl(x, 0.6, 0, 1.9, 0.025, "Metal", seg=8)
mb.box(-4.2, 0.595, 1.85, -0.8, 0.605, 1.86, "Black")
for i, c in enumerate(("FabricWhite", "FabricBlue", "FabricRed", "FabricWhite")):
    mb.box(-3.9 + i * 0.75, 0.59, 1.15 + (i % 2) * 0.2, -3.4 + i * 0.75, 0.61, 1.85, c)
furn("Clothesline", mb, 0, 0, zr, 0)
# string lights over terrace
for i in range(6):
    lamp("Fairy%d" % i, -4.4 + i * 1.3, -2.2 + (i % 2) * 0.3, zr + 2.3, 6, (1.0, 0.7, 0.4), kind="point", fixture=False)
    mb = MB(); mb.sph(0, 0, 0, 0.05, "LightWarm"); mb.obj("FairyBulb%d" % i, -4.4 + i * 1.3, -2.2 + (i % 2) * 0.3, zr + 2.3, kind="light_fixture")
cable("FairyCable", (-4.8, -2.2, zr + 2.5), (2.4, -2.0, zr + 2.6), 0.25)

# ---------------------------------------------------------------- facade dressing
ys = Y1 - 0.03
mb = MB()                                                         # awning
mb.prism([(ys, 2.75), (ys - 1.3, 2.45), (ys - 1.3, 2.62), (ys, 3.05)], -4.7, 2.4, "AwningRed", plane="yz")
for i in range(9):
    x = -4.6 + i * 0.85
    mb.box(x, ys - 1.32, 2.3, x + 0.42, ys - 1.28, 2.47, "AwningWhite")
mb.obj("Awning", kind="trim")
sign_board("ShopSign", "拉麵 · 夜巷   RAMEN", -1.15, ys - 0.1, 3.33, 7.0, 0.46, 0, "WoodDark", "NeonYellow", 0.3)
sign_board("HallSign", "住戶入口", 3.7, ys - 0.06, 2.75, 1.2, 0.3, 0, "Black", "LabelGlow", 0.18)
neon_vertical("Blade", "拉麵屋", -4.6, ys - 0.75, 5.6, 2.6, 90, "NeonRed", size=0.4)
for i, x in enumerate((-4.3, 2.0)):
    lamp("Lantern%d" % i, x, ys - 1.0, 2.45, 35, (1.0, 0.45, 0.2), kind="lantern", glow="Lantern")
vending(5.7, -3.5, 0, 270)
trash_bin(5.6, -1.9, 0, 270)
plant(-5.6, -5.5, 0, 0, 1.0, kind="bush")
cable("Cable1", (X1 - 0.05, Y1 + 0.5, 9.5), (X1 - 4.5, -10.0, 7.0), 0.8)

label_building(Z[5] + 2.9 + 0.2, Y1 - 0.4, (2.85, Y1 - 0.03, 1.55), 8.0)
spawn("front_door", 3.7, Y1 - 1.6, 0, 0)
spawn("shop_door", 0.1, Y1 - 1.6, 0, 0)
