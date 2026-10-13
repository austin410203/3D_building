# 極光貨櫃研究站 Aurora Container Research Station — stacked ISO containers on steel stilts around a glazed
# stair tower; bunk room, lab, mess, comms room, balcony walkway with canopy; snow-loaded roofs. (ref: arctic container base)
begin_building("station_arctic", "極光貨櫃研究站", "Aurora Container Research Station", "Polar Container Outpost", "極地貨櫃前哨站",
               "utility", "research station", ["realistic", "survival", "sci-fi", "thriller", "post-apocalyptic"],
               "Four containers (blue 20ft bunks, yellow 40ft lab, grey 20ft mess, grey 40ft comms/lounge) on stilts around a "
               "glass stair tower; twin front stairs, upper balcony walkway + slanted canopy, antenna mast, dish, fuel drums.", 2, PLOT)

LZ = 1.6                     # lower container base
UZ = LZ + 2.59               # upper container base
ob("Plot", [(-13.0, -9.0, -0.6, 15.5, 6.5, 0.0)], ["Snow"], kind="terrain", walkable=True)
mb = MB()                                                        # steel stilts + beams
for x in (-9.2, -6.3, -3.3, 0.5, 3.6, 6.6, 9.6, 12.5):
    for y in (-2.45, -1.0, 1.0):
        mb.bc(x, y, -0.3, 0.2, 0.2, LZ + 0.3, "MetalDark")
for y in (-1.0, 1.0):
    mb.box(-9.5, y - 0.12, LZ - 0.3, 12.8, y + 0.12, LZ, "MetalDark")
mb.obj("Stilts", kind="structure")
# front walkway deck (grating) + twin stairs
slab("Walkway", -9.4, -2.7, 12.73, -1.24, LZ, 0.12, top="PanelSteel", under="MetalDark", ft=0.03)
rail("WalkRailS1", -9.4, -2.7, -6.1, -2.7, LZ, 1.0, "bar"); rail("WalkRailS2", -4.9, -2.7, 5.3, -2.7, LZ, 1.0, "bar")
rail("WalkRailS3", 6.7, -2.7, 12.73, -2.7, LZ, 1.0, "bar")
rail("WalkRailW", -9.4, -2.7, -9.4, -1.24, LZ, 1.0, "bar"); rail("WalkRailE", 12.73, -2.7, 12.73, -1.24, LZ, 1.0, "bar")
n = round(LZ / 0.18); L = (n - 1) * 0.28
stair("StairL", -5.5, -2.7 - L, 0.0, LZ, "+y", 1.2, 0.28, "PanelSteel", rails="both", rail_style="bar")
stair("StairR", 6.0, -2.7 - L, 0.0, LZ, "+y", 1.2, 0.28, "PanelSteel", rails="both", rail_style="bar")

# ---------------------------------------------------------------- glass stair tower
TX1, TX2, TY1, TY2 = -3.2, 0.4, -1.8, 3.0
TT = 0.1
ring("Tower", TX1, TY1, TX2, TY2, LZ, UZ + 2.8, "PanelSteel", "PanelSteel", TT, 0.0,
     {"S": [(-3.0, -2.2, LZ + 0.1, UZ + 2.6, "shop", "MetalDark"), (-2.0, -1.0, LZ + 0.12, LZ + 2.2, "door_metal"),
            (-0.8, 0.2, LZ + 0.1, UZ + 2.6, "shop", "MetalDark")],
      "W": [(-1.1, -0.3, LZ + 0.12, LZ + 2.2, "open"), (-1.1, -0.3, UZ + 0.12, UZ + 2.2, "open"), (0.3, 2.6, LZ + 0.2, UZ + 2.6, "shop", "MetalDark")],
      "E": [(-1.1, -0.3, LZ + 0.12, LZ + 2.2, "open"), (-1.1, -0.3, UZ + 0.12, UZ + 2.2, "open"), (0.3, 2.6, LZ + 0.2, UZ + 2.6, "shop", "MetalDark")],
      "N": [(-2.9, 0.1, LZ + 0.2, UZ + 2.6, "shop", "MetalDark")]})
slab("Tower_Floor", TX1 + TT, TY1 + TT, TX2 - TT, TY2 - TT, LZ + 0.12, 0.15, top="PanelSteel", under="MetalDark")
hole, arr = stair_u("TowerStair", (TX1 + TX2) / 2, -0.2, LZ + 0.12, UZ + 0.12, "+y", 1.25, 0.08, m="PanelSteel", rail_style="bar")
slab("Tower_Up", TX1 + TT, TY1 + TT, TX2 - TT, TY2 - TT, UZ + 0.12, 0.15, holes=[hole], top="PanelSteel", under="MetalDark")
slab("Tower_Roof", TX1, TY1, TX2, TY2, UZ + 2.95, 0.15, top="Snow", under="PanelSteel")
for z in (LZ + 2.4, UZ + 2.4):
    lamp("TowerL%d" % int(z), -1.4, 0.0, z, 60, (1.0, 0.85, 0.6))
ob("Bridges", [(-3.34, -1.1, LZ + 0.12, -3.2, -0.3, LZ + 0.14), (0.4, -1.1, LZ + 0.12, 0.54, -0.3, LZ + 0.14),
               (-3.34, -1.1, UZ + 0.12, -3.2, -0.3, UZ + 0.14), (0.4, -1.1, UZ + 0.12, 0.54, -0.3, UZ + 0.14)],
   ["PanelSteel"], kind="floor", walkable=True)

# ---------------------------------------------------------------- lower containers
container("Bunks", -9.4, -1.22, LZ, "x", 6.06, "ContBlue", "WoodLight",
          {"S": [(-8.4, -6.8, LZ + 0.9, LZ + 2.0, "win"), (-6.0, -5.0, LZ + 0.12, LZ + 2.2, "door_metal"), (-4.4, -3.4, LZ + 0.9, LZ + 2.0, "win")],
           "E": [(-1.1, -0.3, LZ + 0.12, LZ + 2.2, "open")]}, doors_end="W")
for i, x in enumerate((-8.3, -7.2)):
    mb = MB()
    for zz in (0.25, 1.35):
        mb.box(-0.45, -1.0, zz, 0.45, 1.0, zz + 0.12, "MetalDark"); mb.box(-0.43, -0.98, zz + 0.12, 0.43, 0.98, zz + 0.3, "Mattress")
        mb.box(-0.43, -0.98, zz + 0.3, 0.43, 0.3, zz + 0.38, ["FabricRed", "FabricNavy"][i])
    for (sx, sy) in ((-0.45, -1.0), (0.4, -1.0), (-0.45, 0.95), (0.4, 0.95)):
        mb.box(sx, sy, 0, sx + 0.05, sy + 0.05, 2.0, "MetalDark")
    furn("BunkBed", mb, x, 0.0, LZ + 0.12, 0, "sleep")
for i in range(3):
    mb = MB(); mb.box(-0.25, -0.25, 0, 0.25, 0.25, 1.9, "Metal"); mb.box(-0.23, -0.26, 0.1, 0.23, -0.25, 1.8, "MetalDark")
    furn("Locker", mb, -5.6 + i * 0.52, 0.85, LZ + 0.12, 0, "open")
lamp("BunksL", -6.0, 0.0, LZ + 2.5, 40)
container("Lab", 0.54, -1.22, LZ, "x", 12.19, "ContYellow", "White",
          {"S": [(1.0, 2.6, LZ + 0.9, LZ + 2.0, "win"), (4.6, 5.6, LZ + 0.12, LZ + 2.2, "door_metal"), (7.6, 9.6, LZ + 0.9, LZ + 2.0, "win")],
           "W": [(-1.1, -0.3, LZ + 0.12, LZ + 2.2, "open")], "N": [(9.8, 11.6, LZ + 1.0, LZ + 2.0, "win")]},
          floor="TileWhite", doors_end="E")
for i, x in enumerate((2.0, 7.8)):
    mb = MB(); mb.box(-1.2, -0.35, 0, 1.2, 0.35, 0.9, "White"); mb.box(-1.25, -0.4, 0.9, 1.25, 0.4, 0.94, "MarbleBlack")
    for j in range(4):
        mb.cyl(-0.9 + j * 0.5, 0, 0.94, 1.15, 0.05, ["Glass", "GlassBlue", "NeonGreen", "Glass"][j], seg=10)
    mb.box(-1.2, 0.3, 0.94, 1.2, 0.35, 1.6, "MetalDark"); mb.box(-1.2, 0.25, 1.5, 1.2, 0.35, 1.55, "LightCool")
    furn("LabBench", mb, x, 0.75, LZ + 0.12, 0, "work")
console(10.6, 0.7, LZ + 0.12, 0, 2.2, 2, "ScreenGreen"); server_rack(11.95, -0.55, LZ + 0.12, 270)
fridge(5.1, 0.82, LZ + 0.12, 0, 0.75, 1.85, "White"); office_chair(10.6, -0.2, LZ + 0.12, 0)
for i, x in enumerate((2.5, 6.0, 9.8)):
    lamp("LabL%d" % i, x, 0.0, LZ + 2.5, 50, (0.9, 0.95, 1.0))

# ---------------------------------------------------------------- upper containers
container("Mess", -9.4, -1.22, UZ, "x", 6.06, "ContGrey", "WoodLight",
          {"S": [(-8.6, -6.2, UZ + 0.8, UZ + 2.1, "win3"), (-5.0, -3.5, UZ + 0.8, UZ + 2.1, "win")],
           "E": [(-1.1, -0.3, UZ + 0.12, UZ + 2.2, "open")], "W": [(-0.8, 0.8, UZ + 0.9, UZ + 2.0, "win")]}, roof=True)
kitchen_run(-6.9, 0.84, UZ + 0.12, 0, 3.6, "White", "Chrome", uppers=True)
table(-6.0, -0.4, UZ + 0.12, 0, 2.2, 0.75, 0.75, "WoodLight", "MetalDark")
for x in (-6.7, -5.3):
    chair(x, -0.95, UZ + 0.12, 180, "MetalDark")
lamp("MessL", -6.0, -0.3, UZ + 2.5, 45, kind="pendant")
container("Comms", 0.54, -1.22, UZ, "x", 12.19, "ContGrey", "PlasterInt",
          {"S": [(0.8, 3.4, UZ + 0.5, UZ + 2.2, "shop", "MetalDark"), (4.0, 5.0, UZ + 0.12, UZ + 2.2, "door_glass"),
                 (6.0, 11.4, UZ + 0.5, UZ + 2.2, "shop", "MetalDark")],
           "W": [(-1.1, -0.3, UZ + 0.12, UZ + 2.2, "open")], "E": [(-0.6, 0.6, UZ + 0.9, UZ + 2.0, "win")]}, floor="CarpetGrey")
console(9.5, 0.75, UZ + 0.12, 0, 3.4, 4, "Screen"); office_chair(9.0, -0.15, UZ + 0.12, 0); office_chair(10.2, -0.15, UZ + 0.12, 0)
sofa(2.4, 0.7, UZ + 0.12, 0, 2.2, "FabricRed"); coffee_table(2.4, -0.25, UZ + 0.12, 0, 1.0, 0.5)
bookshelf(6.5, 1.0, UZ + 0.12, 0, 1.6, 2.2, 0.3)
for i, x in enumerate((2.4, 6.0, 9.8)):
    lamp("CommsL%d" % i, x, 0.0, UZ + 2.5, 45)
# upper balcony walkway + slanted canopy (ref)
slab("UpWalk", 0.54, -2.6, 12.73, -1.25, UZ, 0.12, top="PanelSteel", under="MetalDark", ft=0.03)
rail("UpWalkS", 0.54, -2.6, 12.73, -2.6, UZ, 1.0, "bar"); rail("UpWalkE", 12.73, -2.6, 12.73, -1.25, UZ, 1.0, "bar")
mb = MB()
mb.quad([(5.0, -3.4, UZ + 3.6), (12.6, -3.4, UZ + 3.6), (12.6, 1.4, UZ + 2.75), (5.0, 1.4, UZ + 2.75)], "PanelSteel", 0.1)
mb.quad([(5.0, -3.4, UZ + 3.62), (12.6, -3.4, UZ + 3.62), (12.6, 1.4, UZ + 2.77), (5.0, 1.4, UZ + 2.77)], "Snow", 0.0)
for x in (5.3, 12.3):
    mb.box(x - 0.06, -3.3, UZ, x + 0.06, -3.18, UZ + 3.55, "MetalDark")
mb.obj("Canopy", kind="structure")
for nm, (x1, x2) in (("SnowA", (-9.4, -3.34)), ("SnowB", (0.54, 12.73))):
    ob(nm, [(x1 - 0.05, -1.27, UZ + 2.67, x2 + 0.05, 1.27, UZ + 2.82)], ["Snow"], kind="trim")
ob("SnowWalk", [(-9.0, -1.22, UZ, -2.94, 1.22, UZ + 0.04)], ["Snow"], kind="trim") if False else None

# ---------------------------------------------------------------- dressing
pipe_run("Chimney1", [(-4.0, 0.6, UZ + 2.67), (-4.0, 0.6, UZ + 4.2)], 0.14, "MetalDark")
pipe_run("Chimney2", [(11.5, 0.6, UZ + 2.67), (11.5, 0.6, UZ + 4.6)], 0.18, "MetalDark")
mb = MB(); mb.cyl(0, 0, 0, 9.0, 0.08, "Metal", seg=10); mb.cyl(0, 0, 9.0, 10.5, 0.03, "Metal", seg=6); mb.sph(0, 0, 10.55, 0.1, "NeonRed")
for k in range(3):
    a = k * 2 * math.pi / 3
    pipe_run("Guy%d" % k, [(14.5, 3.5, 8.5), (14.5 + math.cos(a) * 4, 3.5 + math.sin(a) * 4, 0.0)], 0.01, "Black", kind="cable")
mb.obj("Mast", 14.5, 3.5, 0, kind="trim")
dish(13.6, -3.0, 0.0, 200)
for i in range(5):
    barrel(-11.5 + (i % 3) * 0.65, -4.0 - (i // 3) * 0.65, 0, 0, ["PlasticRed", "PlasticYellow", "PlasticBlue"][i % 3])
for i in range(3):
    crate(9.0 + i * 0.75, -5.2, 0, 10 * i, 0.7, "WoodLight")
mb = MB()                                                        # snowmobile
mb.box(-0.5, -1.2, 0.15, 0.5, 1.0, 0.6, "PlasticYellow"); mb.box(-0.35, 0.0, 0.6, 0.35, 0.9, 0.8, "LeatherBlack")
mb.box(-0.45, -1.4, 0.05, -0.35, 0.2, 0.1, "Metal"); mb.box(0.35, -1.4, 0.05, 0.45, 0.2, 0.1, "Metal"); mb.box(-0.4, -0.6, 0.6, 0.4, -0.55, 1.0, "GlassDark")
furn("Snowmobile", mb, 0.0, -6.5, 0, 20, "use")
for i, (x, y, z) in enumerate(((-5.5, -2.75, LZ + 2.4), (6.0, -2.75, LZ + 2.4), (-1.4, -1.85, UZ + 2.6), (12.5, -2.7, UZ + 2.4))):
    mb = MB(); mb.box(-0.25, -0.15, -0.15, 0.25, 0.05, 0.15, "MetalDark"); mb.box(-0.22, -0.16, -0.12, 0.22, -0.15, 0.12, "LightWarm")
    mb.obj("Flood%d" % i, x, y, z, kind="light_fixture")
    lamp("FloodL%d" % i, x, y - 0.4, z - 0.2, 120, (1.0, 0.85, 0.6), kind="point", fixture=False)
sign_board("StationSign", "AURORA STATION 極光站", 6.2, -1.32, LZ + 2.25, 3.2, 0.36, 0, "Black", "PlasticYellow", 0.22)
for i in range(6):
    tree(-12.0 + i * 0.6, 5.5 + (i % 2) * 0.8, 0, 0.7, "pine", seed=300 + i) if i % 2 == 0 else None

label_building(UZ + 2.95 + 3.0, -2.9, (-0.5, -1.86, LZ + 1.4), 9.0)
spawn("stairs_left", -5.5, -2.7 - L - 1.2, 0, 0)
