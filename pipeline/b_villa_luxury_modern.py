# 白崖現代豪宅 White Cliff Modern Villa — luxury modernist villa: concrete living pavilion, cantilevered plaster
# bedroom volume, garage with roof terrace, infinity pool + deck. (tier: luxury)
begin_building("villa_luxury_modern", "白崖現代豪宅", "White Cliff Modern Villa", "Luxury Modernist Villa", "奢華現代主義別墅",
               "luxury", "villa", ["realistic", "modern", "thriller", "life-sim", "anime"],
               "Glass-walled concrete living pavilion (living/dining/kitchen island), floating stair, cantilevered upper "
               "volume with master suite + ensuite, 2nd bedroom, study, garage with car, roof terrace, infinity pool & deck.", 2, PLOT)

G1, G2, U2 = 0.0, 3.6, 6.8
POOL = (-14.1, -8.1, -10.7, 4.8)
slab("Plot", -15.0, -11.5, 13.0, 9.5, 0.0, 0.4, holes=[(-15.0, -9.0, -8.0, 7.5)], top="Grass", under="Grass")
ob("Drive", [(4.4, -11.5, 0.0, 9.8, -1.0, 0.03)], ["StoneTile"], kind="floor", walkable=True)
ob("Walk", [(0.6, -11.5, 0.0, 3.0, -3.0, 0.03)], ["StoneTile"], kind="floor", walkable=True)
ob("FrontWall", [(-15.0, -11.5, 0.0, 0.4, -11.2, 0.9), (3.2, -11.5, 0.0, 4.2, -11.2, 0.9), (10.0, -11.5, 0.0, 13.0, -11.2, 0.9)],
   ["Concrete"], kind="wall")

# ---------------------------------------------------------------- living pavilion (A)
GL = "FrameWhite"
ring("A", -8.0, -3.0, 4.0, 6.0, G1, G2, "Concrete", "PlasterInt", 0.25, 0.0,
     {"S": [(-7.7, 0.6, 0.05, G2 - 0.35, "shop", "Frame"), (1.0, 2.6, 0, 2.6, "door_double", "WoodDark"), (2.9, 3.7, 0.05, G2 - 0.35, "shop", "Frame")],
      "W": [(-2.7, 5.7, 0.05, G2 - 0.35, "shop", "Frame")],
      "N": [(-7.6, -4.4, 1.0, 2.6, "win", "Frame")],
      "E": [(-2.7, -0.8, 0.9, 2.6, "win", "Frame")]})
slab("A_Floor", -7.75, -2.75, 3.75, 5.75, G1, 0.2, top="Marble", under="Concrete")
st = stair("A_Stair", -4.6, 5.3, G1, G2, "+x", 0.9, 0.28, "WoodLight", rails="right", rail_style="glass")
sofa(-5.0, -0.2, G1, 0, 3.0, "FabricWhite"); sofa(-7.0, 1.6, G1, 90, 2.2, "FabricWhite")
coffee_table(-5.0, 1.4, G1, 0, 1.4, 0.8, "MarbleBlack"); rug(-5.2, 1.4, G1, 0, 4.2, 3.2, "CarpetGrey")
tv(-5.0, 3.6, G1, 180, 2.0) if False else None
mb = MB()                                                       # fireplace / TV wall
mb.box(-1.8, -0.25, 0, 1.8, 0.25, 3.2, "MarbleBlack"); mb.box(-0.9, -0.26, 0.3, 0.9, -0.24, 0.8, "NeonOrange")
mb.box(-1.0, -0.27, 1.4, 1.0, -0.25, 2.5, "Black"); mb.box(-0.96, -0.28, 1.44, 0.96, -0.27, 2.46, "Screen")
furn("MediaWall", mb, -5.0, 3.5, G1, 180, "use")
dining_set(-0.6, 1.0, G1, 90, 2.2, 1.0, "WoodDark") if False else None
table(0.8, -0.8, G1, 0, 2.4, 1.0, 0.75, "WoodDark", "MetalDark")
for i, x in enumerate((-0.1, 0.8, 1.7)):
    chair(x, -1.5, G1, 180, "LeatherBlack"); chair(x, -0.1, G1, 0, "LeatherBlack")
kitchen_run(1.5, 3.95, G1, 0, 3.2, "White", "Marble", uppers=False) if False else kitchen_run(2.0, 5.42, G1, 0, 3.4, "White", "Marble", uppers=True)
mb = MB(); mb.box(-1.4, -0.5, 0, 1.4, 0.5, 0.9, "WoodDark"); mb.box(-1.5, -0.55, 0.9, 1.5, 0.55, 0.95, "Marble")
furn("KitchenIsland", mb, 2.0, 3.0, G1, 0, "cook")
for x in (1.2, 2.0, 2.8):
    stool(x, 2.25, G1, 0, 0.75)
fridge(3.4, 1.2, G1, 270, 0.9, 2.0)
plant(-7.5, -2.4, G1, 0, 1.5, "Concrete", "palm"); plant(3.4, -2.4, G1, 0, 1.2, "Concrete", "tall")
for i, (x, y) in enumerate(((-5, 0.5), (-2, 0.5), (0.8, -0.8), (2.0, 3.0))):
    lamp("A_L%d" % i, x, y, G2 - 0.2, 70, kind="pendant" if i >= 2 else "ceiling")

# ---------------------------------------------------------------- garage (B) + roof terrace
ring("B", 4.0, -1.0, 10.0, 6.0, G1, G2 - 0.4, "Concrete", "Concrete", 0.25, 0.0,
     {"S": [(4.8, 9.2, 0, 2.6, "roller")], "W": [(1.5, 2.4, 0, 2.1, "door")]})
mb = MB()                                                       # timber slat garage door (closed)
for i in range(14):
    mb.box(4.82, -1.05, 0.05 + i * 0.185, 9.18, -0.98, 0.2 + i * 0.185, "WoodLight")
mb.obj("GarageDoor", kind="door")["openable"] = "slide"
car(7.0, 2.6, G1, 0, "PlasticDark")
shelf_goods(9.4, 3.5, G1, 270, 2.4, 2.0, 0.5); lamp("B_L", 7.0, 2.5, G2 - 0.6, 60, (0.9, 0.95, 1.0))
slab("B_Roof", 4.0, -1.0, 10.0, 6.0, G2 - 0.2, 0.25, top="WoodLight", under="Concrete", ft=0.05)
slab("A_RoofE", 2.0, -3.0, 4.0, 6.0, G2 + 0.0, 0.25, top="WoodLight", under="Ceiling", ft=0.05)
rail("TerrRailS", 2.0, -3.0, 4.0, -3.0, G2, 1.05, "glass"); rail("TerrRailS2", 4.0, -1.0, 10.0, -1.0, G2 - 0.2, 1.25, "glass")
rail("TerrRailE", 10.0, -1.0, 10.0, 6.0, G2 - 0.2, 1.25, "glass"); rail("TerrRailN", 2.0, 6.0, 10.0, 6.0, G2 - 0.2, 1.25, "glass")
rail("TerrRailW", 4.0, -3.0, 4.0, -1.0, G2, 1.05, "glass")
sofa(7.0, 5.3, G2 - 0.2, 0, 2.8, "FabricBeige"); coffee_table(7.0, 4.0, G2 - 0.2, 0, 1.4, 0.7, "WoodLight")
umbrella_table(7.2, 1.0, G2 - 0.2, 0, "AwningWhite"); plant(9.4, -0.5, G2 - 0.2, 0, 1.2, "Concrete", "palm")

# ---------------------------------------------------------------- upper volume (C), cantilevered west + south
slab("C_Floor", -9.8, -4.3, 1.8, 5.8, G2, 0.3, holes=[(-4.62, 4.83, st[0] + 0.02, 5.77)], top="Parquet", under="PlasterInt")
ring("C", -10.0, -4.5, 2.0, 6.0, G2, U2, "Plaster", "PlasterInt", 0.25, 0.03,
     {"S": [(-9.6, -4.6, G2 + 0.1, U2 - 0.4, "shop", "Frame"), (-3.6, 1.4, G2 + 0.8, U2 - 0.4, "shop", "Frame")],
      "W": [(-4.0, 4.0, G2 + 0.1, U2 - 0.4, "shop", "Frame")],
      "E": [(3.9, 4.8, G2, G2 + 2.3, "door_glass"), (-3.5, -1.0, G2 + 0.9, U2 - 0.4, "win", "Frame")],
      "N": [(-8.0, -5.5, G2 + 1.4, U2 - 0.6, "win", "Frame")]})
ob("C_Soffit", [(-10.0, -4.5, G2 - 0.32, -8.0, 6.0, G2 - 0.28), (-8.0, -4.5, G2 - 0.32, 2.0, -3.0, G2 - 0.28)], ["WoodLight"], kind="trim")
zc = U2 - 0.3; h = zc - G2
# corridor along north + rooms
iwall("C_Corr", "x", -9.75, 1.75, 3.8, G2, zc, ops=[(-6.0, -5.1, G2, G2 + 2.1, "door"), (-1.0, -0.1, G2, G2 + 2.1, "door")])
iwall("C_P1", "y", -4.25, 3.8, -4.0, G2, zc)
iwall("C_Bath", "x", -9.75, -7.06, 0.4, G2, zc)
iwall("C_BathE", "y", 0.46, 3.74, -7.0, G2, zc, ops=[(1.0, 1.9, G2, G2 + 2.1, "door")])
iwall("C_Study", "y", 3.86, 5.75, -5.0, G2, zc, ops=[(4.3, 5.2, G2, G2 + 2.1, "door")])
# master (SW)
bed(-6.8, -2.2, G2, 90, 1.9, 2.1, "FabricWhite", "WoodDark") if False else bed(-6.8, -0.4, G2, 180, 1.9, 2.1, "FabricWhite", "WoodDark")
nightstand(-8.05, 0.4, G2, 180); nightstand(-5.55, 0.4, G2, 180)
armchair(-8.7, -3.2, G2, 45, "LeatherBlack"); floor_lamp(-9.3, -2.3, G2); rug(-6.8, -1.2, G2, 0, 3.0, 2.4, "CarpetGrey")
lamp("C_MasterL", -6.8, -1.5, zc, 60)
# ensuite (W/N of master)
bathtub(-8.6, 3.2, G2, 0, 1.8, 0.8); toilet(-9.45, 1.2, G2, 90); vanity(-8.2, 0.73, G2, 180, 1.0)
lamp("C_BathL", -8.4, 2.1, zc, 35, (0.95, 0.97, 1.0))
ob("C_BathFl", [(-9.75, 0.46, G2, -7.06, 3.74, G2 + 0.008)], ["MarbleBlack"], kind="floor", walkable=True)
wardrobe(-4.4, 2.2, G2, 270, 1.2, 2.2, 0.6, "WoodDark")
# bedroom 2 (SE)
room("bedroom", -3.94, -4.25, 1.75, 3.74, G2, h, "N", fab="FabricBlue")
# study (NW of corridor)
desk(-6.0, 5.35, G2, 0, 1.6, 0.7, "WoodDark"); bookshelf(-9.45, 4.8, G2, 90, 1.6, 2.4, 0.35)
lamp("C_StudyL", -7.0, 4.8, zc, 40); lamp("C_CorrL", -1.0, 4.8, zc, 30)
# roof of C with solar + fascia
slab("C_Roof", -10.0, -4.5, 2.0, 6.0, U2 + 0.25, 0.3, top="Concrete", under="Ceiling")
ob("C_Fascia", [(-10.1, -4.6, U2 - 0.05, 2.1, -4.45, U2 + 0.35), (-10.1, 5.95, U2 - 0.05, 2.1, 6.1, U2 + 0.35),
                (-10.1, -4.45, U2 - 0.05, -9.95, 5.95, U2 + 0.35), (1.95, -4.45, U2 - 0.05, 2.1, 5.95, U2 + 0.35)], ["White"], kind="trim")
mb = MB()
for i in range(4):
    for j in range(3):
        mb.quad([(-9 + i * 2.4, -3.0 + j * 2.6, 0.2), (-7 + i * 2.4, -3.0 + j * 2.6, 0.2), (-7 + i * 2.4, -1.0 + j * 2.6, 0.7),
                 (-9 + i * 2.4, -1.0 + j * 2.6, 0.7)], "Solar", 0.04)
mb.obj("SolarPanels", 0, 0, U2 + 0.25, kind="trim")

# ---------------------------------------------------------------- pool + deck (west)
slab("Deck", -15.0, -9.0, -8.0, 7.5, 0.06, 0.46, holes=[POOL], top="WoodLight", under="Concrete", ft=0.06)
ob("PoolShell", [(-14.2, -8.2, -1.5, -10.6, 4.8, 0.07)], ["TileBlue"], kind="structure") if False else None
mb = MB()
mb.box(-14.3, -8.3, -1.5, -10.5, -8.1, 0.08, "TileBlue"); mb.box(-14.3, 4.8, -1.5, -10.5, 5.0, 0.08, "TileBlue")
mb.box(-14.3, -8.1, -1.5, -14.1, 4.8, 0.08, "TileBlue"); mb.box(-10.7, -8.1, -1.5, -10.5, 4.8, 0.08, "TileBlue")
mb.box(-14.1, -8.1, -1.5, -10.7, 4.8, -1.4, "TileBlue")
mb.box(-14.1, -8.1, -0.08, -10.7, 4.8, -0.05, "PoolWater")
mb.box(-14.12, -8.12, -0.6, -14.1, 4.78, -0.55, "NeonCyan")
mb.obj("Pool", kind="water")
for i in range(3):
    mb = MB(); mb.box(-0.35, -1.0, 0.25, 0.35, 0.6, 0.35, "White"); mb.prism([(0.4, 0.35), (0.6, 0.35), (1.0, 0.95), (0.85, 0.95)], -0.35, 0.35, "White", plane="yz")
    mb.box(-0.3, -0.95, 0.35, 0.3, 0.95, 0.42, "FabricWhite"); mb.bc(0, -0.9, 0, 0.6, 0.05, 0.25, "Chrome"); mb.bc(0, 0.5, 0, 0.6, 0.05, 0.25, "Chrome")
    furn("Lounger", mb, -9.2, -6.5 + i * 1.3, 0.06, 90, "sit")
umbrella_table(-12.4, 6.3, 0.06, 0, "AwningWhite")
for i, (x, y) in enumerate(((-14.4, -10.5), (11.8, -10.5), (-14.4, 8.8), (11.8, 8.8), (12.0, 0.0))):
    tree(x, y, 0, 1.0, "palm", seed=60 + i)
for i, x in enumerate((-12.0, -8.0, -4.0, 0.0)):
    mb = MB(); mb.cyl(0, 0, 0, 0.6, 0.06, "MetalDark", seg=10); mb.cyl(0, 0, 0.6, 0.66, 0.08, "LightWarm", seg=10)
    furn("Bollard", mb, x, -10.0, 0, 0); lamp("BollardL%d" % i, x, -10.0, 0.7, 10, kind="point", fixture=False)
planter(-4.0, -4.2, 0, 0, 5.0, 0.8, 0.5, "Concrete"); planter(7.0, -2.0, 0, 0, 3.6, 0.7, 0.45, "Concrete")
sign_board("HouseNo", "白崖 No.8", 2.0, -11.25, 0.55, 1.0, 0.28, 0, "MarbleBlack", "Brass", 0.16)
lamp("EntryDown", 1.8, -3.3, G2 - 0.4, 40, kind="point", fixture=False)

label_building(U2 + 0.6 + 2.0, -4.8, (0.75, -3.04, 1.55), 9.0)
spawn("front_gate", 1.8, -12.5, 0, 0)
