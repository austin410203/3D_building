# 日光艙屋 Solar Pod Home — off-grid sci-fi dwelling: copper-clad modules with rounded corners on a pipe frame,
# glazed lab-kitchen pod, upper sleeping module with balcony, tilting solar array. (ref: solar module house)
begin_building("pod_solar", "日光艙屋", "Solar Pod Home", "Sci-Fi Off-Grid Module", "科幻離網艙屋",
               "upscale", "house", ["sci-fi", "solarpunk", "post-apocalyptic", "anime", "realistic"],
               "Raised copper module house: pipe-frame base + deck, lower glazed kitchen/lab pod, interior stair to an upper "
               "sleeping module with wrap balcony, roof hatch, two large tilting solar panels, antenna mast, hydroponic planters.", 2, PLOT)

DZ = 0.9
L1, L2, L3 = DZ, DZ + 2.9, DZ + 5.7
ob("Plot", [(-9.0, -8.5, -0.4, 9.0, 7.5, 0.0)], ["Grass"], kind="terrain", walkable=True)
for i, (x, y, s) in enumerate(((-7.5, -6.5, 0.6), (6.8, -6.8, 0.8), (7.6, 5.0, 0.5), (-7.8, 4.8, 0.7))):
    mb = MB(); mb.sph(0, 0, 0.1, s, "Stone", sx=1.3, sz=0.6); furn("Rock", mb, x, y, 0, i * 40)
tree(-7.0, 1.0, 0, 0.9, "broad", seed=81); tree(7.2, -1.5, 0, 0.8, "broad", seed=82)
# pipe frame base + deck
for y in (-3.6, 3.6):
    pipe_run("BasePipe%s" % ("S" if y < 0 else "N"), [(-6.6, y, 0.42), (6.6, y, 0.42)], 0.36, "PanelCopper")
for x in (-6.6, 6.6):
    pipe_run("BasePipe%s" % ("W" if x < 0 else "E"), [(x, -3.6, 0.42), (x, 3.6, 0.42)], 0.3, "PanelCopper")
mb = MB()
for x in (-6.6, -2.2, 2.2, 6.6):
    for y in (-3.6, 3.6):
        mb.cyl(x, y, 0, 0.12, 0.5, "MetalDark", seg=16); mb.cyl(x, y, 0.75, DZ - 0.1, 0.12, "MetalDark", seg=12)
for x in (-5.5, -1.0, 3.5):
    mb.box(x - 0.6, -3.9, 0.15, x + 0.6, -3.3, 0.7, "PanelSteel")                # battery / tank boxes
mb.obj("BaseFrame", kind="structure")
slab("Deck", -6.8, -4.2, 6.8, 3.9, DZ, 0.2, top="PanelSteel", under="MetalDark", ft=0.04)
rail("DeckRailS1", -6.8, -4.2, 0.6, -4.2, DZ, 1.0, "bar"); rail("DeckRailS2", 1.8, -4.2, 6.8, -4.2, DZ, 1.0, "bar")
rail("DeckRailE", 6.8, -4.2, 6.8, 3.9, DZ, 1.0, "bar"); rail("DeckRailW", -6.8, -4.2, -6.8, 3.9, DZ, 1.0, "bar")
n = round(DZ / 0.18); L = (n - 1) * 0.28
stair("DeckStair", 1.2, -4.2 - L, 0.0, DZ, "+y", 1.1, 0.28, "PanelSteel", rails="both", rail_style="bar")

def rounded_corners(x1, y1, x2, y2, z1, z2, r=0.35, m="PanelCopper"):
    mb = MB()
    for (x, y) in ((x1, y1), (x2, y1), (x1, y2), (x2, y2)):
        mb.cyl(x, y, z1, z2, r, m, seg=20)
    mb.obj("Corners_%d" % int(z1 * 100), kind="trim")

# ---------------------------------------------------------------- lower pod: kitchen / lab
ring("Lo", -4.5, -3.0, 3.5, 3.0, L1, L2, "PanelCopper", "PanelSteel", 0.22, 0.03,
     {"S": [(-4.0, -0.2, L1 + 0.15, L2 - 0.25, "shop", "MetalDark"), (0.4, 1.4, L1, L1 + 2.3, "door_glass"), (1.8, 3.0, L1 + 0.9, L2 - 0.4, "win")],
      "W": [(-2.0, 2.0, L1 + 0.15, L2 - 0.25, "shop", "MetalDark")], "E": [(-1.0, 1.0, L1 + 0.9, L2 - 0.5, "win")]})
rounded_corners(-4.5, -3.0, 3.5, 3.0, L1, L2 + 0.1)
ob("Lo_Floor", [(-4.28, -2.78, L1, 3.28, 2.78, L1 + 0.01)], ["Parquet"], kind="floor", walkable=True)
kitchen_run(-1.6, 2.45, L1, 0, 3.4, "White", "MarbleBlack")
mb = MB(); mb.box(-1.0, -0.45, 0, 1.0, 0.45, 0.92, "PanelSteel"); mb.box(-1.1, -0.5, 0.92, 1.1, 0.5, 0.96, "Marble")
furn("Island", mb, -2.0, 0.2, L1, 0, "cook")
for x in (-2.6, -1.4):
    stool(x, -0.6, L1, 0, 0.75, "PlasticDark")
shelf_goods(-1.6, -2.55, L1, 180, 1.4, 1.8, 0.35)
for i in range(3):                                               # hydroponic racks
    mb = MB(); mb.box(-0.5, -0.2, 0, 0.5, 0.2, 1.9, "MetalDark")
    for j in range(4):
        mb.box(-0.48, -0.18, 0.2 + j * 0.45, 0.48, 0.18, 0.28 + j * 0.45, "White")
        mb.sph(0, 0, 0.35 + j * 0.45, 0.12, "PlantGreen", sx=3.6, sy=1.2, sz=0.8)
        mb.box(-0.46, -0.17, 0.6 + j * 0.45 - 0.03, 0.46, 0.17, 0.6 + j * 0.45, "NeonPurple")
    furn("Hydroponics", mb, -4.0, 0.6 + i * 1.05, L1, 90, "use")
console(1.6, 2.5, L1, 0, 1.8, 2, "Screen")
lamp("Lo_L1", -2.0, 0.2, L2 - 0.2, 60, (0.95, 0.95, 1.0), kind="pendant"); lamp("Lo_L2", 1.6, 0.0, L2 - 0.2, 45, (0.95, 0.95, 1.0))
ob("Lo_Strip", [(-4.26, -2.76, L2 - 0.26, 3.26, -2.72, L2 - 0.22)], ["LightCool"], kind="light_fixture")

# ---------------------------------------------------------------- upper module (bigger, cantilevered)
st = stair("Lo_Stair", 2.85, 2.6, L1, L2, "-y", 0.75, 0.26, "PanelSteel", rails="left", rail_style="bar") if False else None
st = stair("Lo_Stair", -4.05, -0.3, L1, L2, "+y", 0.7, 0.26, "PanelSteel", rails="right", rail_style="bar") if False else None
# stair along the east wall climbing +y
st = stair("Lo_Stair", 2.9, -2.6, L1, L2, "+y", 0.8, 0.26, "PanelSteel", rails="left", rail_style="bar")
slab("Up_Floor", -5.3, -3.3, 4.3, 3.3, L2, 0.25, holes=[(2.48, -2.62, 3.32, st[1] + 0.02)], top="CarpetGrey", under="PanelSteel")
ring("Up", -5.5, -3.5, 4.5, 3.5, L2, L3, "PanelCopper", "PlasterInt", 0.22, 0.03,
     {"S": [(-5.0, -1.0, L2 + 0.3, L3 - 0.3, "shop", "MetalDark"), (0.2, 1.2, L2, L2 + 2.2, "door_glass")],
      "W": [(-2.6, 2.6, L2 + 0.8, L3 - 0.3, "win3", "MetalDark")], "E": [(0.8, 2.4, L2 + 0.9, L3 - 0.4, "win")],
      "N": [(-3.6, -0.6, L2 + 1.0, L3 - 0.4, "win")]})
rounded_corners(-5.5, -3.5, 4.5, 3.5, L2 - 0.2, L3 + 0.3, 0.45)
rail("Up_HoleRail", 2.45, st[1] - 1.4, 2.45, st[1], L2, 1.0, "bar") if False else rail("Up_HoleRail", 2.45, -2.6, 2.45, st[1] - 0.05, L2, 1.0, "bar")
bed(-3.2, 1.9, L2, 0, 1.6, 2.0, "FabricWhite", "PanelSteel")
nightstand(-4.5, 2.95, L2, 0) if False else None
desk(0.0, 2.85, L2, 0, 1.6, 0.7, "PanelSteel"); sofa(-0.5, -2.75, L2, 0, 2.0, "FabricNavy") if False else armchair(-0.6, -0.8, L2, 200, "FabricNavy")
wardrobe(1.5, 2.95, L2, 0, 1.0, 2.1, 0.55, "PanelSteel") if False else None
plant(-4.9, -2.9, L2, 0, 1.0, "PanelDark", "palm")
lamp("Up_L1", -2.5, 0.0, L3 - 0.2, 55); lamp("Up_L2", 1.0, 1.0, L3 - 0.2, 40)
# balcony (south) on the lower pod roof + west deck
slab("UpBalc", -5.5, -4.6, 4.5, -3.53, L2, 0.25, top="PanelSteel", under="PanelCopper")
rail("UpBalcS", -5.5, -4.6, 4.5, -4.6, L2, 1.0, "glass"); rail("UpBalcW", -5.5, -4.6, -5.5, -3.53, L2, 1.0, "glass")
rail("UpBalcE", 4.5, -4.6, 4.5, -3.53, L2, 1.0, "glass")
umbrella_table(2.6, -4.05, L2, 0) if False else round_table(-2.5, -4.05, L2, 0, 0.35)
chair(-3.2, -4.05, L2, 270, "MetalDark"); chair(-1.8, -4.05, L2, 90, "MetalDark")
ob("UpLED", [(-5.52, -4.62, L2 - 0.26, 4.52, -4.58, L2 - 0.2)], ["LightCool"], kind="light_fixture")
# roof + solar array + mast
slab("Up_Roof", -5.5, -3.5, 4.5, 3.5, L3 + 0.25, 0.25, top="PanelDark", under="Ceiling")
mb = MB()
for k, x0 in enumerate((-5.0, -1.4)):
    mb.box(x0 + 1.4, -0.1, 0, x0 + 1.6, 0.1, 1.6, "MetalDark")
    mb.quad([(x0, -1.6, 0.6), (x0 + 3.2, -1.6, 0.6), (x0 + 3.2, 0.9, 3.4), (x0, 0.9, 3.4)], "Solar", 0.06)
    for i in range(1, 4):
        xx = x0 + i * 0.8
        mb.quad([(xx - 0.01, -1.6, 0.61), (xx + 0.01, -1.6, 0.61), (xx + 0.01, 0.9, 3.41), (xx - 0.01, 0.9, 3.41)], "Metal", 0.0)
s_ = mb.obj("SolarArray", 0, 0, L3 + 0.25, kind="trim"); s_["interact"] = "use"; s_["openable"] = "tilt"
mb = MB(); mb.cyl(0, 0, 0, 3.6, 0.06, "Metal", seg=10); mb.cyl(0, 0, 3.6, 4.4, 0.025, "Metal", seg=6)
mb.sph(0, 0, 4.45, 0.08, "NeonRed"); mb.cyl(0, 0, 2.0, 2.3, 0.35, "MetalDark", seg=16, r2=0.1)
mb.obj("Mast", 3.6, 2.6, L3 + 0.25, kind="trim")
mb = MB(); mb.cyl(0, 0, 0, 0.5, 0.5, "PanelSteel", seg=20); mb.cyl(0, 0, 0.5, 0.6, 0.45, "MetalDark", seg=20)
h_ = mb.obj("RoofHatch", 2.0, 0.0, L3 + 0.25, kind="door"); h_["openable"] = "hinge"; h_["interact"] = "open"
lamp("DeckL", 1.2, -4.0, L2 - 0.3, 30, (0.85, 0.95, 1.0), kind="point", fixture=False)
mb = MB(); mb.box(-0.2, -0.05, -0.3, 0.2, 0.05, 0.3, "PanelDark"); mb.cyl(0, -0.06, 0, 0, 0.12, "NeonCyan", seg=16, axis="y")
mb.obj("Badge", 4.55, 0.0, L2 + 1.6, 90, kind="sign") if False else None
planter(-3.5, -3.75, DZ, 0, 2.0, 0.5, 0.5, "PanelSteel"); barrel(5.6, 2.8, DZ, 0, "PanelCopper"); crate(5.7, -2.6, DZ, 15, 0.6, "PanelSteel")

label_building(L3 + 0.25 + 4.0, -4.9, (-0.2, -3.05, L1 + 1.5), 7.0)
spawn("deck_stair", 1.2, -4.2 - L - 1.0, 0, 0)
