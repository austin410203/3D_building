# 朝陽社區公寓 Sunrise Walk-up Apartments — typical East-Asian 6F walk-up: G/F arcade (騎樓) with shops,
# 2 flats per floor around a central U-stair, iron window grilles, balconies with laundry, rooftop tin addition.
begin_building("apt_block_6f", "朝陽社區公寓", "Sunrise Walk-up Apartments", "Taiwanese Walk-up Apartment", "台式公寓",
               "standard", "apartment block", ["realistic", "slice-of-life", "anime", "urban-survival"],
               "6-storey mosaic-tile walk-up: arcade with convenience store + breakfast shop, 10 one-bedroom flats "
               "(2 per floor), central U-stair, grilled windows, balconies with laundry, rooftop iron-sheet addition with water tanks.", 6, PLOT)

X1, X2, Y1, Y2 = -8.0, 8.0, -6.0, 6.0
T = 0.2
Z = [0.0, 3.6, 6.6, 9.6, 12.6, 15.6, 18.6]
YF = -3.0                                   # G/F shop front (arcade 3 m deep)
SX, SY = 0.0, 2.2
ob("Plot", [(-9.5, -7.6, -0.4, 9.5, 7.5, 0.0)], ["StoneTile"], kind="floor", walkable=True)
ob("Arcade", [(X1, Y1, 0.0, X2, YF, 0.02)], ["TileWhite"], kind="floor", walkable=True)
slab("F1_Floor", X1 + T, YF + T, X2 - T, Y2 - T, 0.0, 0.2, top="TileWhite", under="Concrete")

# ---------------------------------------------------------------- shells
hole = None
for f in range(6):
    z0, z1 = Z[f], Z[f + 1]
    if f == 0:
        ops = {"S": [(-7.6, -2.6, 0.3, 3.0, "shop"), (-2.4, -1.5, 0, 2.4, "door_glass"), (-0.6, 0.6, 0, 2.4, "door_metal"),
                     (1.5, 2.4, 0, 2.4, "door_glass"), (2.6, 7.6, 0, 2.9, "roller")],
               "N": [(-6.5, -4.5, 2.0, 2.9, "win"), (4.5, 6.5, 2.0, 2.9, "win")]}
        ring("F1", X1, YF, X2, Y2, z0, z1, "StoneTile", "PlasterInt", T, 0.03, ops)
    else:
        wv = []
        for sx in (-1, 1):
            a = sorted((sx * 7.4, sx * 5.0)); b = sorted((sx * 4.2, sx * 3.2)); c = sorted((sx * 2.6, sx * 1.6))
            wv += [(a[0], a[1], z0 + 0.9, z0 + 2.2, "grille"), (b[0], b[1], z0, z0 + 2.3, "door_glass")]
        wv.append((-0.7, 0.7, z0 + 1.0, z0 + 2.2, "win"))
        ops = {"S": wv,
               "N": [(-7.2, -5.0, z0 + 1.0, z0 + 2.2, "grille"), (5.0, 7.2, z0 + 1.0, z0 + 2.2, "grille"),
                     (-0.6, 0.6, z0 + 1.5 + 0.6, z0 + 2.7, "win")],
               "W": [(-0.7, 0.5, z0 + 1.0, z0 + 2.2, "grille"), (2.0, 2.9, z0 + 1.5, z0 + 2.2, "win"), (4.0, 5.4, z0 + 1.0, z0 + 2.2, "grille")],
               "E": [(-0.7, 0.5, z0 + 1.0, z0 + 2.2, "grille"), (2.0, 2.9, z0 + 1.5, z0 + 2.2, "win"), (4.0, 5.4, z0 + 1.0, z0 + 2.2, "grille")]}
        ring("F%d" % (f + 1), X1, Y1, X2, Y2, z0, z1, "MosaicPink", "PlasterInt", T, 0.03, ops)
        slab("F%d_Floor" % (f + 1), X1 + T, Y1 + T, X2 - T, Y2 - T, z0, 0.22, holes=[hole], top="TileWhite")
    hole, arrive = stair_u("F%d_Stair" % (f + 1), SX, SY, z0, z1, "+y", 1.0, 0.1, m="Concrete", rail_style="bar")
    zc = z1 - 0.22
    # hall walls (x = +-1.3) with flat doors
    for sx in (-1, 1):
        ops_ = [] if f == 0 else [(-2.4, -1.5, z0, z0 + 2.1, "door")]
        iwall("F%d_Hall%s" % (f + 1, "W" if sx < 0 else "E"), "y", (YF if f == 0 else Y1) + T, Y2 - T, sx * 1.3, z0, zc, ops=ops_)
    ob("F%d_HallFloor" % (f + 1), [(-1.24, (YF if f == 0 else Y1) + T, z0, 1.24, SY, z0 + 0.008)], ["StoneTile"], kind="floor", walkable=True)
    lamp("F%d_HallL" % (f + 1), 0.0, -0.5, zc, 30, (1.0, 0.9, 0.75))
slab("Roof", X1 + T, Y1 + T, X2 - T, Y2 - T, Z[6], 0.22, holes=[hole], top="Concrete")
for f in range(1, 7):                                            # floor bands
    z = Z[f]
    ob("Band%d" % f, [(X1 - 0.08, Y1 - 0.08, z - 0.12, X2 + 0.08, Y1 - 0.03, z + 0.08)], ["Concrete"], kind="trim")
mb = MB()                                                        # arcade columns
for x in (-7.75, -4.6, -1.45, 1.45, 4.6, 7.75):
    mb.box(x - 0.25, Y1, 0, x + 0.25, Y1 + 0.5, Z[1], "StoneTile")
mb.obj("ArcadeColumns", kind="structure")

# ---------------------------------------------------------------- G/F shops
# west: convenience store
for i in range(3):
    shelf_goods(-6.2 + i * 1.6, 1.4, 0, 90, 2.6, 1.6, 0.8, double=True)
for i in range(3):
    drinks_fridge(-7.2 + i * 1.3, 5.4, 0, 0)
shop_counter(-3.0, -2.0, 0, 90, 1.8, "White", "Marble")
lamp("ShopA_L1", -4.5, 0.0, Z[1] - 0.22, 80, (0.9, 0.95, 1.0)); lamp("ShopA_L2", -4.5, 3.5, Z[1] - 0.22, 80, (0.9, 0.95, 1.0))
# east: breakfast shop
kitchen_run(4.8, 5.45, 0, 0, 3.6, "Metal", "Chrome", uppers=False)
shop_counter(4.2, -2.0, 0, 0, 2.6, "Metal", "Chrome")
for (x, y) in ((3.0, 0.5), (5.6, 0.5), (3.0, 2.8), (5.6, 2.8)):
    dining_set(x, y, 0, 0, 1.0, 0.6, "PlasticRed") if False else table(x, y, 0, 0, 1.0, 0.6, 0.72, "White", "Chrome")
    for dy in (-0.55, 0.55):
        stool(x - 0.25, y + dy, 0, 0, 0.45, "PlasticRed"); stool(x + 0.25, y + dy, 0, 0, 0.45, "PlasticRed")
lamp("ShopB_L1", 4.5, 0.5, Z[1] - 0.22, 70); lamp("ShopB_L2", 4.5, 3.5, Z[1] - 0.22, 70)
mb = MB()
mb.box(-0.6, -0.12, 0, 0.6, 0.12, 1.0, "Metal")
for i in range(5):
    for j in range(2):
        mb.box(-0.56 + i * 0.23, -0.125, 0.2 + j * 0.4, -0.36 + i * 0.23, -0.12, 0.55 + j * 0.4, "MetalDark")
furn("Mailboxes", mb, 0.0, YF + 0.35, 0.6, 0, "use")
for i, x in enumerate((-6.8, -6.0, -5.2, 5.2, 6.0, 6.8, -3.8, 3.8)):
    scooter(x, -4.7, 0, 0, ["PlasticRed", "White", "PlasticBlue", "PlasticDark"][i % 4])
sign_board("SignA", "便利商店  24H", -4.5, Y1 - 0.12, Z[1] - 0.35, 5.2, 0.55, 0, "White", "PlasticGreen", 0.34, frame="PlasticYellow")
sign_board("SignB", "朝陽早餐店", 4.6, Y1 - 0.12, Z[1] - 0.35, 5.2, 0.55, 0, "PlasticYellow", "PlasticRed", 0.34)
neon_vertical("BladeA", "朝陽公寓", X1 - 0.05, Y1 - 0.4, 8.5, 3.0, 90, "NeonCyan", size=0.42)

# ---------------------------------------------------------------- flats (mirrored west / east)
def flat(sx, f):
    z0 = Z[f]; zc = Z[f + 1] - 0.22; h = zc - z0
    def X(a, b):
        return tuple(sorted((sx * a, sx * b)))
    side_in = "E" if sx < 0 else "W"          # side facing the hall
    # partitions: living front (y<-1.0), kitchen | bath | bedroom along the outer side, corridor by the hall
    iwall("F%d_%s_PA" % (f + 1, sx), "x", *X(7.8, 1.36), -1.0, z0, zc, ops=[(*X(2.0, 3.1), z0, z0 + 2.1, "open")])
    iwall("F%d_%s_PB" % (f + 1, sx), "y", -0.94, Y2 - T, sx * 2.66, z0, zc,
          ops=[(-0.4, 0.8, z0, z0 + 2.1, "open"), (2.1, 2.9, z0, z0 + 2.1, "door"), (4.0, 4.9, z0, z0 + 2.1, "door")])
    iwall("F%d_%s_PC" % (f + 1, sx), "x", *X(7.8, 2.72), 1.6, z0, zc)
    iwall("F%d_%s_PD" % (f + 1, sx), "x", *X(7.8, 2.72), 3.3, z0, zc)
    xa, xb = X(7.8, 1.36)
    xk = X(7.8, 2.72)
    room("living", xa, Y1 + T, xb, -1.06, z0, h, "N", fab=RNG.choice(["FabricBlue", "FabricGreen", "FabricBeige"]))
    room("kitchen", xk[0], -0.94, xk[1], 1.54, z0, h, side_in)
    room("bath", xk[0], 1.66, xk[1], 3.24, z0, h, side_in)
    room("bedroom", xk[0], 3.36, xk[1], Y2 - T, z0, h, side_in)
    ob("F%d_%s_BathFl" % (f + 1, sx), [(xk[0], 1.66, z0, xk[1], 3.24, z0 + 0.008)], ["TileBlue"], kind="floor", walkable=True)
    cabinet_low(sx * 2.0, 5.5, z0, 0, 1.0, 1.9, 0.5, "WoodLight")          # corridor closet
    lamp("F%d_%s_CorL" % (f + 1, sx), sx * 2.0, 2.0, zc, 25)
    # front balcony with laundry + AC
    bx = X(7.5, 2.0)
    slab("F%d_%s_Balc" % (f + 1, sx), bx[0], Y1 - 1.2, bx[1], Y1 - 0.03, z0, 0.16, top="TileWhite", under="Concrete")
    rails_rect("F%d_%s_BalR" % (f + 1, sx), bx[0], Y1 - 1.2, bx[1], Y1 - 0.03, z0, "SWE", style="bar", h=1.1)
    laundry((bx[0] + bx[1]) / 2, Y1 - 0.6, z0, 4.4)
    ac_unit(sx * 6.4, Y1 - 0.25, z0 + 0.04, 180)
    plant(sx * 2.4, Y1 - 0.9, z0, 0, 0.7)
    ac_unit(sx * (X2 + 0.18) , 3.5, z0 + 2.3, 90 if sx > 0 else 270)

for f in range(1, 6):
    for sx in (-1, 1):
        flat(sx, f)

# ---------------------------------------------------------------- roof: tin addition + tanks
zr = Z[6]
ob("Parapet", [(X1, Y1, zr, X2, Y1 + 0.2, zr + 1.1), (X1, Y1 + 0.2, zr, X1 + 0.2, Y2, zr + 1.1),
               (X2 - 0.2, Y1 + 0.2, zr, X2, Y2, zr + 1.1), (X1 + 0.2, Y2 - 0.2, zr, -3.5, Y2, zr + 1.1),
               (4.5, Y2 - 0.2, zr, X2 - 0.2, Y2, zr + 1.1)], ["MosaicPink"], kind="wall")
ring("Shack", -3.5, -0.4, 4.5, Y2, zr, zr + 2.6, "TinRust", "PlasterInt", 0.12, 0.0,
     {"S": [(-1.2, -0.2, zr, zr + 2.1, "door_metal"), (1.5, 3.5, zr + 1.0, zr + 2.0, "grille")],
      "E": [(1.5, 3.5, zr + 1.0, zr + 2.0, "win")]})
gable_roof("ShackRoof", -3.5, -0.4, 4.5, Y2, zr + 2.6, 12, 0.35, "TinRust", "MetalDark", along="x", cap="Metal")
iwall("ShackP", "x", 1.3, 4.38, 2.0, zr, zr + 2.5, ops=[(1.5, 2.4, zr, zr + 2.1, "door")])
bed(3.1, 4.6, zr, 0, 1.4, 2.0, "FabricRed", "MetalDark"); desk(2.9, 0.4, zr, 180, 1.2, 0.6)
lamp("ShackL1", 0.0, 1.0, zr + 2.45, 30); lamp("ShackL2", 3.0, 3.9, zr + 2.45, 30)
for i, x in enumerate((-6.6, -5.0)):
    water_tank(x, 4.6, zr, 0, 0.55, 1.4, "Chrome")
for i in range(6):
    mb = MB(); mb.box(-0.4, -0.25, 0, 0.4, 0.25, 0.35, "White"); mb.sph(0, 0, 0.42, 0.25, "PlantGreen", sx=1.4, sz=0.6)
    furn("FoamPlanter", mb, -7.0 + i * 0.95 if i < 3 else 5.2 + (i - 3) * 0.95, -5.2, zr, 0)
dish(6.6, 2.0, zr, 220); antenna(-6.8, 1.5, zr, 3.0)
laundry(-5.5, -1.0, zr, 3.0, 90)

label_building(zr + 2.6 + 3.0, Y1 - 0.4, (-0.95, YF - 0.03, 1.6), 9.0)
spawn("arcade", 0.0, Y1 - 1.5, 0, 0)
