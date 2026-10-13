# 霓虹窄塔 Neon Sliver Tower — cyberpunk narrow 5-storey tower with stacked uses (ref: grimy neon block).
# Walkable: U-stair core on the east side, all floors + roof hut.
begin_building("tower_cyber_narrow", "霓虹窄塔", "Neon Sliver Tower", "Cyberpunk Vertical Block", "賽博龐克窄樓",
               "budget", "mixed-use tower", ["cyberpunk", "sci-fi", "neo-noir", "realistic"],
               "6x7 m five-storey neon tower: G/F DVD & gadget shop, 2F hacker den with servers, 3F capsule hostel, "
               "4F neon bar, 5F loft, roof hut with antennas. Grimy steel cladding, fans, pipes, vertical neon signs.", 5, PLOT)

X1, X2, Y1, Y2, T = -3.2, 3.2, -3.5, 3.5, 0.2
xi1, xi2, yi1, yi2 = X1 + T, X2 - T, Y1 + T, Y2 - T
Z = [0.0, 3.4, 6.4, 9.4, 12.4, 15.4]
SX, SY = 1.95, 0.0
ob("Plot", [(-4.6, -5.4, -0.4, 4.6, 4.6, 0.0)], ["Concrete"], kind="floor", walkable=True)
slab("F1_Floor", xi1, yi1, xi2, yi2, 0.0, 0.2, top="TileWhite", under="Concrete")

hole = None
for f in range(5):
    z0, z1 = Z[f], Z[f + 1]
    if f == 0:
        ops = {"S": [(-2.9, -0.9, 0.4, 2.9, "shop"), (-0.7, 0.3, 0, 2.3, "door_glass"), (0.6, 2.9, 0, 2.7, "roller")],
               "W": [(-2.0, -0.6, 1.2, 2.6, "grille")]}
        ext = "PanelDark"
    else:
        ops = {"S": [(-2.6, -0.6, z0 + 0.9, z0 + 2.3, ["win", "grille", "win3", "win"][f - 1]),
                     (0.5, 2.6, z0 + 0.9, z0 + 2.3, "grille" if f % 2 else "win")],
               "W": [(-1.0, 1.0, z0 + 1.0, z0 + 2.2, "win" if f != 2 else "grille")],
               "N": [(-2.4, -1.0, z0 + 1.2, z0 + 2.1, "win")]}
        ext = "GrimeTeal" if f % 2 else "GrimeBlue"
    ring("F%d" % (f + 1), X1, Y1, X2, Y2, z0, z1, ext, "PlasterInt" if f != 3 else "BrickDark", T, 0.03, ops)
    if f > 0:
        slab("F%d_Floor" % (f + 1), xi1, yi1, xi2, yi2, z0, 0.22, holes=[hole],
             top=["TileWhite", "CarpetGrey", "WoodFloor", "Parquet", "WoodFloor"][f])
    hole, arrive = stair_u("F%d_Stair" % (f + 1), SX, SY, z0, z1, "+y", 1.0, 0.1, m="MetalDark", rail_style="bar")
    lamp("F%d_StairLight" % (f + 1), SX, 2.0, z1 - 0.22, 25, (0.7, 0.9, 1.0))
slab("Roof", xi1, yi1, xi2, yi2, Z[5], 0.22, holes=[hole], top="Concrete")

# ---------------------------------------------------------------- G/F gadget & DVD shop
shop_counter(1.9, -1.6, 0, 180, 1.8, "PanelDark", "MetalDark")
shelf_goods(-2.75, -0.6, 0, 90, 2.4, 2.0, 0.4); shelf_goods(-1.0, 1.4, 0, 0, 2.6, 1.6, 0.6, double=True)
arcade(-2.45, 2.6, 0, 90, "PlasticDark", "NeonCyan")
vending(4.1, -2.4, 0, 270, "NeonRed")
lamp("F1_L1", -1.4, -1.5, Z[1] - 0.22, 50, (0.8, 0.9, 1.0)); lamp("F1_L2", 1.6, -1.9, Z[1] - 0.22, 40, (1.0, 0.4, 0.8))
# ---------------------------------------------------------------- 2F hacker den
z0 = Z[1]
console(-1.2, 2.75, z0, 0, 2.6, 3, "ScreenGreen"); office_chair(-1.2, 1.85, z0, 0)
server_rack(-2.65, 0.3, z0, 90); server_rack(-2.65, -0.8, z0, 90)
bed(-1.6, -2.3, z0, 90, 1.0, 1.95, "FabricNavy", "MetalDark")
lamp("F2_L", -1.0, 0.0, Z[2] - 0.22, 35, (0.4, 1.0, 0.6))
# ---------------------------------------------------------------- 3F capsule hostel
z0 = Z[2]
for k, y in enumerate((-2.0, 0.2)):
    for lvl in range(2):
        mb = MB(); zz = lvl * 1.15
        mb.box(-1.0, -1.05, zz, 1.0, 1.05, zz + 1.1, "White")
        mb.box(-0.98, -1.0, zz + 0.12, 0.98, 1.0, zz + 0.3, "Mattress")
        mb.box(-0.9, -0.95, zz + 0.3, 0.9, -0.5, zz + 0.4, "FabricWhite")
        mb.box(-1.02, 0.6, zz + 0.1, 1.02, 1.07, zz + 0.95, "LightSoft") if False else None
        mb.box(0.98, -0.9, zz + 0.15, 1.01, 0.9, zz + 1.0, "Black")                      # open face
        mb.box(0.985, -0.85, zz + 0.95, 1.0, -0.6, zz + 1.02, "LED")
        mb.box(-0.98, -1.0, zz + 0.95, 0.95, 1.0, zz + 0.98, "LightWarm")
        o = furn("Capsule", mb, -2.0, y, z0, 0, "sleep")
    mb = MB(); mb.box(-0.15, -0.9, 1.1, 0.15, 0.9, 1.14, "MetalDark")
    for i in range(6):
        mb.box(-0.02, -0.9 + i * 0.36, 0, 0.02, -0.86 + i * 0.36, 2.3, "Chrome") if False else None
for i in range(4):
    mb = MB(); mb.box(-0.25, -0.25, 0, 0.25, 0.25, 1.9, "Metal")
    for j in range(3):
        mb.box(-0.23, -0.26, 0.05 + j * 0.62, 0.23, -0.25, 0.6 + j * 0.62, "MetalDark")
    furn("Locker", mb, -0.4 + i * 0.52, -3.0, z0, 0, "open")
lamp("F3_L", -0.5, -0.5, Z[3] - 0.22, 40)
# ---------------------------------------------------------------- 4F neon bar
z0 = Z[3]
bar_counter(-1.2, 1.3, z0, 0, 2.8, "MarbleBlack", "Marble")
bookshelf(-1.2, 2.95, z0, 0, 2.6, 2.0, 0.3, "MetalDark", books=False)
for i in range(10):
    mb = MB(); mb.cyl(0, 0, 0, 0.3, 0.04, ["GlassBlue", "Glass", "NeonGreen", "GlassDark"][i % 4], seg=8)
    furn("Bottle", mb, -2.35 + i * 0.25, 2.95, z0 + 1.15, 0)
arcade(-2.5, -2.6, z0, 90, "PlasticRed", "NeonYellow"); claw_machine(1.7, -2.5, z0, 180)
ob("F4_NeonStrip", [(xi1 + 0.02, yi2 - 0.05, Z[4] - 0.4, 0.8, yi2 - 0.02, Z[4] - 0.36)], ["NeonPink"], kind="light_fixture")
lamp("F4_L1", -1.2, 0.6, Z[4] - 0.22, 40, (1.0, 0.3, 0.8), kind="pendant"); lamp("F4_L2", 1.0, -1.6, Z[4] - 0.22, 30, (0.3, 0.8, 1.0))
# ---------------------------------------------------------------- 5F loft
z0 = Z[4]
bed(-1.8, 2.2, z0, 0, 1.4, 2.0, "FabricRed", "MetalDark")
sofa(-2.5, -1.4, z0, 90, 1.8, "FabricNavy"); tv(0.4, -1.4, z0, 270, 1.2) if False else tv(-0.4, -3.0, z0, 180, 1.2)
kitchen_run(1.7, -3.0, z0, 180, 2.4, "MetalDark", "MarbleBlack", uppers=False) if False else desk(1.6, -2.7, z0, 180, 1.4, 0.7)
lamp("F5_L", -1.0, 0.0, Z[5] - 0.22, 50, (1.0, 0.7, 0.5))

# ---------------------------------------------------------------- roof hut + clutter
zr = Z[5]
ring("Hut", 0.7, -1.8, X2, Y2, zr, zr + 2.6, "PanelSteel", "PanelSteel", 0.15, 0.0,
     {"W": [(-1.6, -0.7, zr, zr + 2.2, "door_metal")]})
slab("HutRoof", 0.7, -1.8, X2, Y2, zr + 2.75, 0.15, top="PanelDark", under="PanelSteel")
rail("HutVoidRail", 0.85, -0.03, 1.95, -0.03, zr, 1.0, "bar")
lamp("HutLight", 1.9, -1.0, zr + 2.6, 25, (0.7, 0.9, 1.0))
rails_rect("RoofRail", X1 + 0.05, Y1 + 0.05, X2 - 0.05, Y2 - 0.05, zr, "SW", style="bar")
rail("RoofRailN", X1 + 0.05, Y2 - 0.05, 0.7, Y2 - 0.05, zr, 1.0, "bar"); rail("RoofRailE", X2 - 0.05, Y1 + 0.05, X2 - 0.05, -1.8, zr, 1.0, "bar")
antenna(2.6, 2.6, zr + 2.75, 4.0); antenna(-2.6, 2.8, zr, 3.0)
dish(1.6, 0.4, zr + 2.75, 200); water_tank(-1.8, 1.2, zr, 0, 0.6, 1.4, "Rust")
mb = MB()
for i in range(3):
    mb.cyl(-2.4 + i * 0.6, -2.6, 0, 1.2 + i * 0.3, 0.12, "MetalDark", seg=12)
mb.obj("Vents", 0, 0, zr, kind="trim")

# ---------------------------------------------------------------- facade clutter
ys = Y1 - 0.03
def fan_box(name, x, y, z, w=1.6, h=1.3, d=0.5, rot=0, m="PanelSteel"):
    mb = MB()
    mb.box(-w / 2, -d, -h / 2, w / 2, 0, h / 2, m)
    r = min(w, h) * 0.38
    mb.cyl(0, -d - 0.01, 0, 0, r + 0.04, "MetalDark", seg=28, axis="y")
    for k in range(6):
        mb.box(-r, -d - 0.03, -0.015 + (k - 2.5) * r / 3, r, -d - 0.01, 0.015 + (k - 2.5) * r / 3, "Black")
    return mb.obj(name, x, y, z, rot, kind="trim")
fan_box("FanA", -1.8, ys, 8.0, 1.8, 1.5, 0.45)
fan_box("FanB", 1.6, ys, 14.0, 1.4, 1.2, 0.4)
fan_box("FanW", X1 - 0.03, 1.8, 11.0, 1.4, 1.2, 0.5, 270)
for f in (1, 2, 3, 4):
    ac_unit(-1.0 if f % 2 else 1.6, ys - 0.15, Z[f] + 0.2, 180)
neon_vertical("BladePink", "電腦酒場夜市", 2.75, ys - 0.12, 9.6, 6.0, 0, "NeonPink", "Black", 0.45)
sign_board("SignDVD", "DVD · 電器", -1.6, ys - 0.12, 3.05, 2.6, 0.5, 0, "Black", "NeonOrange", 0.3, frame="NeonOrange")
sign_board("SignBar", "BAR 酒", -1.6, ys - 0.12, 12.1, 1.7, 0.45, 0, "Black", "NeonRed", 0.3, frame="NeonRed")
sign_board("SignOpen", "OPEN 24H", 0.6, ys - 0.06, 2.85, 1.2, 0.3, 0, "Black", "NeonCyan", 0.18)
mb = MB(); mb.cyl(0, 0, -0.35, 0.35, 0.36, "Black", seg=28, axis="y"); mb.cyl(0, -0.03, -0.32, 0.32, 0.32, "NeonPink", seg=28, axis="y")
mb.box(-0.02, 0.0, 0.35, 0.02, 0.6, 0.4, "MetalDark"); mb.obj("RoundSign", X2 + 0.7, -1.2, 6.2, 90, kind="sign")
pipe_run("PipeA", [(X1 - 0.12, Y1 + 0.4, 0.3), (X1 - 0.12, Y1 + 0.4, 14.2), (X1 - 0.12, 1.0, 14.2), (X1 - 0.12, 1.0, zr + 1.0)], 0.07, "Brass")
pipe_run("PipeB", [(X2 + 0.1, Y1 + 0.25, 0.3), (X2 + 0.1, Y1 + 0.25, 7.0), (X2 + 0.1, 0.5, 7.0), (X2 + 0.1, 0.5, zr + 0.5)], 0.06, "Rust")
pipe_run("PipeC", [(-0.2, ys - 0.12, 3.4), (-0.2, ys - 0.12, 6.0), (0.3, ys - 0.12, 6.4), (0.3, ys - 0.12, 15.0)], 0.045, "Brass")
mb = MB()                                                       # grilled balcony cage on 2F/3F west
for z in (Z[1], Z[2]):
    mb.box(X1 - 0.8, -1.4, z - 0.12, X1 - 0.03, 1.2, z, "MetalDark")
    for i in range(14):
        y = -1.4 + i * 0.2
        mb.box(X1 - 0.8, y - 0.01, z, X1 - 0.78, y + 0.01, z + 1.0, "MetalDark")
    mb.box(X1 - 0.82, -1.42, z + 1.0, X1 - 0.03, 1.22, z + 1.04, "MetalDark")
mb.obj("WestCage", kind="railing")
for i in range(6):
    cable("Cable%d" % i, (X1 + 0.3 + i * 1.1, ys - 0.1, 5.0 + i * 1.7), (X1 - 6 + i * 3.0, ys - 8.0, 6.5), 0.9 + 0.2 * i)
lamp("StreetGlow", 0.0, ys - 1.5, 3.2, 60, (1.0, 0.3, 0.8), kind="point", fixture=False)
crate(-3.8, -4.3, 0, 10); crate(-3.7, -4.3, 0.6, 30, 0.5); barrel(3.9, 2.8, 0, 0, "PlasticBlue"); trash_bin(-3.9, -2.2, 0, 90)

label_building(zr + 2.75 + 4.0, Y1 - 0.4, (-0.95, ys, 1.6), 6.0)
spawn("front", -0.2, Y1 - 1.6, 0, 0)
