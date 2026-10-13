# 藍調轉角雜貨 Blue Corner Bodega — 2-storey corner shop: open G/F with corner columns and raised shutters,
# cluttered shop (records/games + snack bar), blue upper flat with LED-lit balcony, rooftop palms. (ref: blue diorama shop)
begin_building("shop_neon_corner", "藍調轉角雜貨", "Blue Corner Bodega", "Neon Corner Shop Diorama", "霓虹轉角店",
               "budget", "shop + flat", ["cyberpunk", "anime", "slice-of-life", "diorama", "realistic"],
               "Corner shop with open frontage (raised roller shutters) on two streets: record & game corner, snack counter, "
               "shelves, arcade. Upper blue flat with wrap balcony and LED under-glow, rooftop garden with palms.", 2, PLOT)

X1, X2, Y1, Y2 = -5.5, 5.0, -4.5, 4.5
G1, G2, U2 = 0.0, 3.4, 6.4
ob("Plot", [(-8.0, -7.5, -0.4, 7.5, 6.5, 0.0)], ["Cobble"], kind="floor", walkable=True)
slab("GF_Floor", X1 + 0.2, Y1 + 0.2, X2 - 0.2, Y2 - 0.2, G1, 0.2, top="StoneTile", under="Concrete")
ring("GF", X1, Y1, X2, Y2, G1, G2, "GrimeBlue", "BrickDark", 0.25, 0.03,
     {"S": [(-5.0, -0.4, 0.0, 2.9, "roller"), (0.2, 4.5, 0.0, 2.9, "roller")],
      "E": [(-4.0, 0.0, 0.0, 2.9, "roller"), (1.0, 2.0, 0.0, 2.2, "door_metal")],
      "W": [(-3.5, -1.0, 1.0, 2.5, "grille")]})
mb = MB()                                                        # corner column + raised shutters (rolled)
mb.box(X2 - 0.5, Y1 - 0.1, 0, X2 + 0.1, Y1 + 0.5, G2, "PanelDark")
mb.obj("CornerPier", kind="structure")
# stair to the flat (back wall, climbs +x)
st = stair("GF_Stair", -4.9, 3.75, G1, G2, "+x", 0.9, 0.28, "MetalDark", rails="right", rail_style="bar")
iwall("GF_StairWall", "x", X1 + 0.25, st[0] + 0.3, 3.2, G1, G2 - 0.22, t=0.1, m="BrickDark")
# left: pink-lit record / game corner
for i in range(2):
    shelf_goods(-4.95, -1.6 + i * 2.0, G1, 90, 1.8, 2.0, 0.4)
mb = MB()                                                        # record bins
for i in range(3):
    mb.box(-0.4 + i * 0.0, -0.3, 0, 0.4, 0.3, 0.8, "WoodDark")
for j in range(12):
    mb.box(-0.36 + j * 0.06, -0.25, 0.8, -0.33 + j * 0.06, 0.25, 1.1, RNG.choice(["BookA", "BookB", "BookC", "Black", "PlasticYellow"]))
furn("RecordBin", mb, -2.6, -1.4, G1, 0, "shop"); furn("RecordBin", mb if False else MB(), -2.6, 0.2, G1, 0) if False else None
mb = MB(); mb.box(-0.4, -0.3, 0, 0.4, 0.3, 0.8, "WoodDark")
for j in range(12):
    mb.box(-0.36 + j * 0.06, -0.25, 0.8, -0.33 + j * 0.06, 0.25, 1.1, RNG.choice(["BookA", "BookB", "BookC", "Black", "PlasticYellow"]))
furn("RecordBin", mb, -2.6, 0.2, G1, 0, "shop")
arcade(-1.2, 2.5, G1, 180, "PlasticBlue", "NeonPink")
lamp("GF_Pink", -3.2, -0.4, G2 - 0.22, 70, (1.0, 0.25, 0.6))
ob("GF_PinkStrip", [(X1 + 0.27, -3.9, G2 - 0.5, X1 + 0.3, 2.9, G2 - 0.46)], ["NeonPink"], kind="light_fixture")
# right: snack counter + goods
shop_counter(2.4, 0.6, G1, 180, 2.6, "PanelDark", "Marble")
mb = MB(); mb.box(-1.3, -0.2, 0, 1.3, 0.2, 0.5, "Glass"); mb.box(-1.25, -0.15, 0.02, 1.25, 0.15, 0.12, "BookC")
furn("Display", mb, 2.4, 0.75, G1 + 1.05, 0)
bookshelf(2.4, 2.95, G1, 0, 2.6, 2.2, 0.35, "MetalDark", books=False)
for i in range(8):
    mb = MB(); mb.cyl(0, 0, 0, 0.25, 0.05, RNG.choice(["PlasticRed", "PlasticGreen", "GlassBlue", "PlasticYellow"]), seg=8)
    furn("Jar", mb, 1.4 + i * 0.28, 2.95, G1 + 1.2, 0)
drinks_fridge(4.25, -2.6, G1, 270, 1.0, 2.0)
for x in (0.6, 1.4):
    stool(x, -0.1, G1, 0, 0.75, "PlasticRed")
crate(0.8, -3.6, G1, 10, 0.5, "PlasticBlue"); crate(1.4, -3.7, G1, 0, 0.5, "PlasticGreen")
for i, (x, y) in enumerate(((2.4, -1.0), (2.4, 1.6))):
    lamp("GF_Warm%d" % i, x, y, G2 - 0.22, 55, (1.0, 0.75, 0.45), kind="pendant")

# ---------------------------------------------------------------- upper flat
slab("UF_Floor", X1 + 0.2, Y1 + 0.2, X2 - 0.2, Y2 - 0.2, G2, 0.25, holes=[(-4.92, 3.28, st[0] + 0.02, 4.28)], top="WoodFloor", under="BrickDark")
ring("UF", X1, Y1, X2, Y2, G2, U2, "GrimeBlue", "PlasterInt", 0.25, 0.03,
     {"S": [(-4.6, -2.6, G2 + 0.9, G2 + 2.3, "win"), (-1.6, -0.6, G2, G2 + 2.3, "door_glass"), (1.0, 4.2, G2 + 0.9, G2 + 2.3, "win3")],
      "E": [(-3.0, -0.4, G2 + 0.9, G2 + 2.3, "win"), (1.0, 2.6, G2 + 0.9, G2 + 2.3, "win")],
      "W": [(-1.0, 1.0, G2, G2 + 2.3, "door_glass")], "N": [(1.0, 2.6, G2 + 1.2, G2 + 2.3, "win")]})
rail("UF_StairRail", -4.92, 3.24, st[0], 3.24, G2, 1.0, "bar")
iwall("UF_P1", "y", Y1 + 0.25, 3.0, 0.4, G2, U2 - 0.22, ops=[(-0.6, 0.3, G2, G2 + 2.1, "door")])
room("living", X1 + 0.25, Y1 + 0.25, 0.34, 3.0, G2, 2.75, "N", fab="FabricNavy")
bed(2.7, -2.9, G2, 180, 1.4, 2.0, "FabricRed", "MetalDark")
desk(4.1, 1.4, G2, 270, 1.2, 0.6); plant(0.9, 2.6, G2, 0, 0.8, kind="tall")
lamp("UF_L1", -2.6, -0.5, U2 - 0.22, 55); lamp("UF_L2", 2.6, -0.5, U2 - 0.22, 50, (0.5, 0.6, 1.0))
# wrap balcony (south + west) with LED under-glow
slab("Balc", X1 - 1.3, Y1 - 1.3, 1.0, Y1 - 0.03, G2, 0.2, top="TileWhite", under="PanelDark")
slab("BalcW", X1 - 1.3, Y1 - 0.03, X1 - 0.03, 2.5, G2, 0.2, top="TileWhite", under="PanelDark")
ob("BalcLED", [(X1 - 1.32, Y1 - 1.34, G2 - 0.22, 1.0, Y1 - 1.3, G2 - 0.17), (X1 - 1.34, Y1 - 1.3, G2 - 0.22, X1 - 1.3, 2.5, G2 - 0.17)],
   ["NeonBlue"], kind="light_fixture")
rail("BalcS", X1 - 1.3, Y1 - 1.3, 1.0, Y1 - 1.3, G2, 1.0, "bar"); rail("BalcWr", X1 - 1.3, Y1 - 1.3, X1 - 1.3, 2.5, G2, 1.0, "bar")
rail("BalcN", X1 - 1.3, 2.5, X1 - 0.03, 2.5, G2, 1.0, "bar"); rail("BalcE", 1.0, Y1 - 1.3, 1.0, Y1 - 0.03, G2, 1.0, "bar")
for i, (x, y) in enumerate(((-6.4, -5.3), (-3.0, -5.3), (-6.4, 1.6))):
    plant(x, y, G2, 0, 0.9, "PanelDark", ["palm", "bush", "tall"][i])
ac_unit(-1.0, Y1 - 0.4, G2 + 0.02, 180); bench(-6.3, -1.4, G2, 270, 1.4, "WoodDark")
ob("UF_LEDs", [(X1 - 0.06, Y1 - 0.06, G2 - 0.08, X2 + 0.06, Y1 - 0.03, G2 - 0.03), (X2 + 0.03, Y1 - 0.06, G2 - 0.08, X2 + 0.06, Y2, G2 - 0.03)],
   ["NeonBlue"], kind="light_fixture")

# ---------------------------------------------------------------- roof garden
slab("Roof", X1, Y1, X2, Y2, U2 + 0.25, 0.25, top="Concrete", under="Ceiling")
ob("RoofParapet", [(X1, Y1, U2 + 0.25, X2, Y1 + 0.2, U2 + 0.85), (X1, Y2 - 0.2, U2 + 0.25, X2, Y2, U2 + 0.85),
                   (X1, Y1 + 0.2, U2 + 0.25, X1 + 0.2, Y2 - 0.2, U2 + 0.85), (X2 - 0.2, Y1 + 0.2, U2 + 0.25, X2, Y2 - 0.2, U2 + 0.85)],
   ["GrimeBlue"], kind="wall")
for i, (x, y) in enumerate(((-3.8, 2.6), (3.2, 2.8), (3.6, -3.0))):
    tree(x, y, U2 + 0.25, 0.55, "palm", seed=90 + i)
    mb = MB(); mb.cyl(0, 0, 0, 0.6, 0.6, "Concrete", seg=16); furn("PalmPot", mb, x, y, U2 + 0.25, 0)
water_tank(-3.6, -2.6, U2 + 0.25, 0, 0.55, 1.1, "PaintTeal"); antenna(0.0, 3.6, U2 + 0.25, 2.6)
ac_unit(0.8, -3.9, U2 + 0.25, 0); ac_unit(2.0, -3.9, U2 + 0.25, 0)
rs = stair("UF_RoofStair", 4.2, 3.9, G2, U2 + 0.25, "-y", 0.8, 0.26, "MetalDark", rails="left") if False else None
mb = MB()
for sx in (-0.25, 0.25):
    mb.box(sx - 0.03, -0.03, 0, sx + 0.03, 0.03, U2 + 1.4, "MetalDark")
for i in range(int((U2 + 1.2) / 0.3)):
    mb.box(-0.25, -0.015, 0.25 + i * 0.3, 0.25, 0.015, 0.28 + i * 0.3, "Metal")
lad = mb.obj("RoofLadder", 3.6, Y2 + 0.18, 0, 0, kind="ladder"); lad["interact"] = "climb"; lad["top_z"] = U2 + 0.25

# ---------------------------------------------------------------- street dressing
street_lamp(X2 + 1.8, Y1 - 1.8, 0, 225, 4.6, 200)
sign_board("SignS", "藍調雜貨 BODEGA", -0.2, Y1 - 0.14, G2 - 0.25, 6.0, 0.42, 0, "Black", "NeonCyan", 0.28)
neon_vertical("BladeE", "唱片遊戲", X2 + 0.2, -3.6, G2 + 1.6, 2.4, 90, "NeonPink", size=0.36)
for i in range(3):
    crate(-6.6 + i * 0.1, -4.6 + i * 0.6, 0, 20 * i, 0.45, ["PlasticBlue", "WoodLight", "PlasticRed"][i])
trash_bin(5.9, 2.8, 0, 270, "PlasticBlue"); vending(-6.6, 2.6, 0, 90, "NeonBlue")
cable("Wire1", (X2, Y1, U2), (X2 + 1.8, Y1 - 1.8, 4.6), 0.4)

label_building(U2 + 0.85 + 2.4, Y1 - 0.4, (X2 - 0.2, Y1 - 0.1, 1.55), 7.0)
spawn("corner", X2 + 1.5, Y1 - 1.5, 0, 45)
