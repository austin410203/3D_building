# 貨櫃森林咖啡館 Container Grove Café — timber + glass café, black container kitchen, planted terrace,
# yellow 40ft container lounge under a timber canopy (ref: architectural container café sketch).
begin_building("cafe_container", "貨櫃森林咖啡館", "Container Grove Café", "Industrial Container Modern", "工業貨櫃現代",
               "upscale", "café / commercial", ["realistic", "modern", "slice-of-life", "anime"],
               "Raised concrete podium, timber post-and-beam café with full glazing, 20ft black container kitchen, "
               "outdoor stair to a planted terrace, 40ft yellow container lounge with sliding glass wall, timber canopy roof.", 2, PLOT)

PZ = 0.6                 # podium level
TZ = 4.0                 # terrace level
ob("Plot", [(-10.0, -8.5, -0.4, 9.5, 6.0, 0.0)], ["StoneTile"], kind="floor", walkable=True)
ob("Podium", [(-9.0, -5.5, -0.2, 7.0, 4.0, PZ - 0.02)], ["Concrete"], kind="structure")
ob("PodiumDeck", [(-9.0, -5.5, PZ - 0.02, 7.0, 4.0, PZ)], ["WoodLight"], kind="floor", walkable=True)
n = 3; L = (n - 1) * 0.28
stair("FrontSteps", -4.3, -5.5 - L, 0.0, PZ, "+y", 3.2, 0.28, "WoodLight", rails="left", rail_style="bar")
planter(-1.4, -6.0, 0, 0, 2.2, 0.6, 0.6, "Concrete"); planter(-7.3, -6.0, 0, 0, 2.6, 0.6, 0.6, "Concrete")
rail("PodiumRailS", -2.65, -5.5, 7.0, -5.5, PZ, 1.0, "bar"); rail("PodiumRailE", 7.0, -5.5, 7.0, 4.0, PZ, 1.0, "bar")

# ---------------------------------------------------------------- G/F café (timber + glass)
W_ = "WoodLight"
ring("Cafe", -6.0, -3.6, 4.0, 3.0, PZ, TZ, "WoodLight", "PlasterInt", 0.2, 0.03,
     {"S": [(-5.8, -2.2, PZ + 0.1, TZ - 0.4, "shop", W_), (-1.9, -0.6, PZ, PZ + 2.4, "door_glass"), (-0.3, 3.8, PZ + 0.1, TZ - 0.4, "shop", W_)],
      "E": [(-3.4, 2.8, PZ + 0.1, TZ - 0.4, "shop", W_)],
      "W": [(-2.2, -1.2, PZ, PZ + 2.1, "open")],
      "N": [(-4.5, -2.5, PZ + 1.2, PZ + 2.4, "win", W_), (1.0, 3.0, PZ + 1.2, PZ + 2.4, "win", W_)]})
ob("CafeFloor", [(-5.8, -3.4, PZ, 3.8, 2.8, PZ + 0.01)], ["Parquet"], kind="floor", walkable=True)
shop_counter(1.8, 1.6, PZ, 0, 3.0, "WoodDark", "MarbleBlack")
mb = MB()                                                        # espresso machine + grinder + cake display
mb.box(-0.4, -0.25, 0, 0.4, 0.25, 0.45, "Chrome"); mb.box(-0.38, -0.27, 0.32, 0.38, -0.25, 0.4, "Black")
mb.cyl(-0.2, -0.3, 0.12, 0.2, 0.04, "Black", seg=10); mb.cyl(0.2, -0.3, 0.12, 0.2, 0.04, "Black", seg=10)
mb.cyl(0.65, 0, 0, 0.35, 0.08, "MetalDark", seg=12); mb.cyl(0.65, 0, 0.35, 0.55, 0.1, "GlassDark", seg=12, r2=0.06)
mb.box(-1.4, -0.25, 0, -0.7, 0.25, 0.4, "Glass"); mb.box(-1.35, -0.2, 0.05, -0.75, 0.2, 0.12, "BookC")
furn("EspressoBar", mb, 1.8, 1.75, PZ + 1.05, 180, "cook")
bookshelf(1.8, 2.62, PZ, 0, 3.0, 2.6, 0.3, "WoodDark", books=True)
for x, y in ((-4.6, -2.3), (-2.6, -2.3), (-4.6, -0.2), (1.0, -2.4), (2.9, -2.4), (2.9, -0.4)):
    cafe_set(x, y, PZ, 0, "Marble", "WoodLight")
sofa(-4.0, 2.25, PZ, 0, 2.6, "FabricBeige")
coffee_table(-4.0, 1.2, PZ, 0, 1.4, 0.6)
plant(-5.5, -3.1, PZ, 0, 1.3, kind="tall"); plant(3.5, -3.1, PZ, 0, 1.2, kind="palm"); plant(-0.5, 2.5, PZ, 0, 1.0)
for i, (x, y) in enumerate(((-4.6, -2.3), (-2.6, -2.3), (-4.6, -0.2), (1.0, -2.4), (2.9, -2.4), (2.9, -0.4), (1.8, 1.3))):
    lamp("CafePendant%d" % i, x, y, TZ - 0.25, 35, kind="pendant")
lamp("CafeSofa", -4.0, 1.6, TZ - 0.25, 50)

# ---------------------------------------------------------------- black 20ft kitchen container (west)
container("Kitchen", -8.44, -3.0, PZ, "y", 6.06, "ContBlack", "TileWhite",
          {"W": [(-1.5, 0.5, PZ + 1.2, PZ + 2.1, "win")], "N": [(-7.9, -6.9, PZ + 0.12, PZ + 2.2, "door_metal")]},
          sides="SNW", floor="TileWhite", doors_end="S")
kitchen_run(-8.06, 0.2, PZ + 0.12, 90, 3.0, "Metal", "Chrome")
fridge(-8.03, 2.35, PZ + 0.12, 90); shelf_goods(-6.5, -2.55, PZ + 0.12, 180, 1.4, 1.8, 0.4)
lamp("KitchenLight", -7.2, 0.0, PZ + 2.5, 50, (0.9, 0.95, 1.0))

# ---------------------------------------------------------------- outdoor stair to the terrace (east side, climbs -y)
stair("TerraceStair", 5.3, 2.8, PZ, TZ, "-y", 1.1, 0.28, "WoodLight", rails="both", rail_style="bar")
nT = round((TZ - PZ) / 0.18); Lt = (nT - 1) * 0.28
slab("Terrace", -6.0, -4.6, 6.4, 3.0, TZ, 0.35, holes=[(4.7, 2.8 - Lt - 0.02, 5.9, 2.95)], top="WoodLight", under="WoodDark", ft=0.05)
mb = MB()                                                        # timber posts + beams carrying the terrace
for x in (-5.9, -2.0, 2.0, 6.25):
    mb.bc(x, -4.45, PZ, 0.24, 0.24, TZ - 0.35 - PZ, "WoodLight")
for y in (-1.2, 2.85):
    mb.bc(6.25, y, PZ, 0.24, 0.24, TZ - 0.35 - PZ, "WoodLight")
mb.box(-6.0, -4.58, TZ - 0.6, 6.4, -4.32, TZ - 0.35, "WoodLight"); mb.box(6.13, -4.6, TZ - 0.6, 6.37, 3.0, TZ - 0.35, "WoodLight")
mb.obj("TerraceFrame", kind="structure")
rail("TerRailS", -6.0, -4.6, 6.4, -4.6, TZ, 1.05, "cable"); rail("TerRailW", -6.0, -4.6, -6.0, 0.5, TZ, 1.05, "cable")
rail("TerRailE", 6.4, -4.6, 6.4, 3.0, TZ, 1.05, "cable"); rail("TerRailHole", 4.65, 2.8 - Lt, 4.65, 2.95, TZ, 1.05, "cable")
for i in range(5):                                               # planter boxes with trailing plants (ref)
    planter(-4.8 + i * 2.4, -4.35, TZ, 0, 2.0, 0.45, 0.45, "White", trailing=True)
for x in (-3.5, 0.0):
    umbrella_table(x, -2.4, TZ, 0, "AwningWhite")
bench(3.2, -1.2, TZ, 270, 1.6)

# ---------------------------------------------------------------- yellow 40ft lounge container + canopy
container("Lounge", -7.69, 0.56, TZ, "x", 12.19, "ContYellow", "WoodLight",
          {"S": [(-5.6, -0.4, TZ + 0.2, TZ + 2.35, "shop", "Frame"), (-0.2, 0.8, TZ + 0.12, TZ + 2.3, "door_glass"),
                 (1.0, 4.2, TZ + 0.2, TZ + 2.35, "shop", "Frame")],
           "E": [(1.0, 2.6, TZ + 0.8, TZ + 2.2, "win")], "N": [(-4.0, -1.0, TZ + 1.0, TZ + 2.2, "win")]},
          floor="Parquet", doors_end="W")
ob("LoungeOverhangSupport", [(-7.6, 0.6, PZ + 2.59, -6.0, 3.0, TZ - 0.02)], ["MetalDark"], kind="structure") if False else None
sofa(-4.4, 2.5, TZ + 0.12, 0, 2.4, "FabricNavy"); coffee_table(-4.4, 1.55, TZ + 0.12, 0)
sofa(2.6, 2.5, TZ + 0.12, 0, 2.2, "FabricBeige"); coffee_table(2.6, 1.55, TZ + 0.12, 0)
bar_counter(-1.2, 2.55, TZ + 0.12, 180, 1.8, "WoodDark", "WoodLight", stools=False)
bookshelf(-6.8, 1.8, TZ + 0.12, 90, 1.6, 2.2, 0.3)
for i, x in enumerate((-4.4, -1.2, 2.6)):
    lamp("LoungeLight%d" % i, x, 1.8, TZ + 2.55, 45, kind="ceiling")
mb = MB()                                                        # timber canopy roof (ref)
mb.box(-8.3, -1.4, TZ + 3.05, 5.4, 3.5, TZ + 3.25, "WoodLight")
mb.box(-8.35, -1.45, TZ + 3.25, 5.45, 3.55, TZ + 3.45, "Black")
for i in range(18):
    x = -8.1 + i * 0.75
    mb.box(x, -1.4, TZ + 2.92, x + 0.08, 3.5, TZ + 3.05, "WoodDark")
for x in (-6.5, -0.8, 4.9):
    mb.bc(x, -1.2, TZ, 0.18, 0.18, 3.05, "Black")
mb.box(-8.3, -1.32, TZ + 2.75, 5.4, -1.08, TZ + 3.05, "Black")
mb.obj("Canopy", kind="structure")
for i, x in enumerate((-4.5, 0.0, 3.6)):
    lamp("CanopyDown%d" % i, x, -0.6, TZ + 3.0, 25, kind="point", fixture=False)

# ---------------------------------------------------------------- sign + greenery
t = text("SignBig", "CONTAINER CAFÉ  貨櫃咖啡", -1.4, -1.37, TZ + 2.9, 0.26, "PlasticYellow", extrude=0.01)
sign_board("SignBlade", "咖啡 COFFEE", -6.3, -3.75, PZ + 2.9, 2.2, 0.42, 0, "WoodDark", "NeonYellow", 0.26)
tree(8.6, 1.6, 0, 2.0, "broad", seed=21); tree(-10.0, 3.6, 0, 1.4, "broad", seed=22)
plant(6.3, -5.0, PZ, 0, 1.0, kind="tall"); plant(-8.6, -5.0, PZ, 0, 1.0, kind="palm")

label_building(TZ + 3.45 + 0.4, -4.9, (-2.35, -3.66, PZ + 1.6), 8.0)
spawn("front_steps", -4.3, -5.5 - L - 1.0, 0, 0)
