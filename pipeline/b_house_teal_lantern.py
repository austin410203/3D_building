# 青瓦燈籠茶屋 Teal Lantern Teahouse — Ghibli-like teal clapboard house raised on a deck + old tree trunk.
# Walkable: front stair -> deck -> G/F tea room -> stair -> 2F bedroom/study -> stair -> roof terrace.
begin_building("house_teal_lantern", "青瓦燈籠茶屋", "Teal Lantern Teahouse", "Ghibli Seaside Stilt House", "吉卜力海邊高腳屋",
               "standard", "house+shop", ["anime", "ghibli", "cozy", "fantasy", "realistic"],
               "Teal clapboard 2-storey teahouse on a raised timber deck around an old tree trunk; red-framed bay windows, "
               "paper lanterns, roof terrace with antennas.", 2, PLOT)

DZ = 2.4                     # deck level
G1, G2 = DZ, DZ + 3.0        # ground-floor storey
U1, U2 = G2, G2 + 2.8        # upper storey
T = 0.18

ob("Plot", [(-7.0, -10.5, -0.4, 7.5, 6.0, 0.0)], ["Cobble"], kind="floor", walkable=True)
# ---------------------------------------------------------------- deck + supports + tree
slab("Deck", -5.2, -5.6, 5.2, 4.2, DZ, 0.28, top="WoodLight", under="WoodDark", ft=0.05)
mb = MB()
for x in (-5.0, -1.7, 1.7, 5.0):
    for y in (-5.4, -0.6, 4.0):
        mb.bc(x, y, 0, 0.26, 0.26, DZ - 0.28, "WoodDark")
        mb.bc(x, y, 0, 0.4, 0.4, 0.25, "Stone")
for y in (-5.4, -0.6, 4.0):
    mb.box(-5.2, y - 0.12, DZ - 0.55, 5.2, y + 0.12, DZ - 0.28, "WoodDark")
for x in (-5.0, 5.0):
    mb.box(x - 0.12, -5.6, DZ - 0.5, x + 0.12, 4.2, DZ - 0.28, "WoodDark")
for x in (-5.0, 5.0):                                                   # diagonal braces
    mb.prism([(-5.3, 0.2), (-4.9, 0.2), (-0.8, DZ - 0.55), (-1.2, DZ - 0.55)], x - 0.06, x + 0.06, "WoodDark", plane="yz")
mb.obj("DeckFrame", kind="structure")
mb = MB()                                                               # old tree trunk the deck is built around
mb.cyl(0.6, 0.6, -0.3, 1.2, 1.25, "Bark", seg=14, r2=0.95)
mb.cyl(0.6, 0.6, 1.2, DZ - 0.28, 0.95, "Bark", seg=14, r2=0.85)
for a in range(6):
    t = a * math.pi / 3 + 0.3
    mb.sph(0.6 + math.cos(t) * 1.4, 0.6 + math.sin(t) * 1.4, 0.0, 0.55, "Bark", sx=1.8, sy=0.7, sz=0.6)
mb.obj("TreeTrunk", kind="structure")
pipe_run("Branch1", [(1.2, 1.0, DZ - 0.6), (3.4, 2.6, DZ + 0.8), (5.6, 3.6, DZ + 3.5)], 0.32, "Bark")
pipe_run("Branch2", [(0.2, 0.4, DZ - 0.6), (-2.6, 2.6, DZ - 0.4), (-6.0, 3.4, DZ + 1.2)], 0.24, "Bark")
tree(6.2, 4.6, DZ + 1.6, 1.6, "broad", seed=11)
tree(-6.6, 3.8, DZ - 0.2, 1.1, "broad", seed=12)

# front stair (13 risers) + deck railing with gap
n = round(DZ / 0.18); L = (n - 1) * 0.28
stair("MainStair", 0.0, -5.6 - L, 0.0, DZ, "+y", 1.6, 0.28, "WoodLight", rails="both", rail_style="wood")
rail("DeckRailS1", -5.2, -5.6, -0.85, -5.6, DZ, 1.0, "wood"); rail("DeckRailS2", 0.85, -5.6, 5.2, -5.6, DZ, 1.0, "wood")
rail("DeckRailW", -5.2, -5.6, -5.2, 4.2, DZ, 1.0, "wood"); rail("DeckRailE", 5.2, -5.6, 5.2, 4.2, DZ, 1.0, "wood")
rail("DeckRailN", -5.2, 4.2, 5.2, 4.2, DZ, 1.0, "wood")

# ---------------------------------------------------------------- ground floor: tea room
R = "PaintRed"
ring("GF", -3.6, -3.0, 3.6, 3.2, G1, G2, "SidingTeal", "WoodLight", T, 0.03,
     {"S": [(-3.0, -1.3, G1 + 0.9, G1 + 2.3, "win3", R), (-0.5, 0.5, G1, G1 + 2.2, "door", R), (1.1, 3.0, G1 + 0.75, G1 + 2.3, "open")],
      "W": [(-1.5, 0.8, G1 + 0.9, G1 + 2.3, "win", R)],
      "E": [(-2.6, -1.3, G1 + 0.9, G1 + 2.3, "win", R)],
      "N": [(2.0, 3.0, G1 + 1.6, G1 + 2.4, "win", R)]})
bay_window("GF_Bay", "S", 1.1, 3.0, G1 + 0.75, G1 + 2.3, -3.03, 0.55)
ob("GF_FloorBoards", [(-3.42, -2.82, G1, 3.42, 3.02, G1 + 0.01)], ["WoodFloor"], kind="floor", walkable=True)
st_end = stair("GF_Stair", -3.3, 2.52, G1, G2, "+x", 0.9, 0.28, "WoodLight", rails="right", rail_style="wood")
shop_counter(2.65, 0.3, G1, 270, 2.0, "WoodDark", "WoodLight")
bookshelf(3.2, 0.3, G1, 270, 1.8, 2.2, 0.35, "WoodDark")
cafe_set(-2.2, -1.4, G1, 0, "WoodLight", "WoodDark"); cafe_set(-2.2, 0.9, G1, 0, "WoodLight", "WoodDark")
plant(-3.1, -2.5, G1, 0, 0.9, kind="tall")
rug(-1.3, -0.3, G1, 0, 2.6, 2.2, "CarpetRed")
for i, (x, y) in enumerate(((-2.2, -1.4), (-2.2, 0.9), (1.2, 0.3))):
    lamp("GF_Lantern%d" % i, x, y, G2 - 0.22, 40, (1.0, 0.55, 0.25), kind="lantern", glow="Lantern")

# ---------------------------------------------------------------- upper floor (overhangs 0.4 m)
slab("UF_Floor", -3.82, -3.22, 3.82, 3.42, U1, 0.22, holes=[(-3.35, 2.0, st_end[0], 3.05)], top="WoodFloor", under="WoodLight")
ring("UF", -4.0, -3.4, 4.0, 3.6, U1, U2, "SidingTeal", "PlasterInt", T, 0.03,
     {"S": [(-3.4, -1.2, U1 + 0.7, U1 + 2.2, "open"), (-0.6, 0.6, U1 + 0.9, U1 + 2.2, "win", R), (1.4, 3.4, U1 + 0.7, U1 + 2.2, "open")],
      "W": [(-1.0, 1.0, U1 + 0.9, U1 + 2.2, "win", R)],
      "E": [(1.6, 3.0, U1 + 0.9, U1 + 2.2, "win", R)],
      "N": [(-3.4, -2.2, U1 + 1.2, U1 + 2.2, "win", R)]})
bay_window("UF_BayL", "S", -3.4, -1.2, U1 + 0.7, U1 + 2.2, -3.43, 0.6)
bay_window("UF_BayR", "S", 1.4, 3.4, U1 + 0.7, U1 + 2.2, -3.43, 0.6)
ob("UF_Soffit", [(-4.03, -3.43, U1 - 0.3, 4.03, -3.0, U1 - 0.22), (-4.03, 3.2, U1 - 0.3, 4.03, 3.63, U1 - 0.22),
                 (-4.03, -3.0, U1 - 0.3, -3.6, 3.2, U1 - 0.22), (3.6, -3.0, U1 - 0.3, 4.03, 3.2, U1 - 0.22)], ["WoodDark"], kind="trim")
mb = MB()                                                               # brackets under the overhang
for x in (-3.8, -1.3, 1.3, 3.8):
    mb.prism([(-3.0, U1 - 1.0), (-3.0, U1 - 0.3), (-3.4, U1 - 0.3)], x - 0.05, x + 0.05, "WoodDark", plane="yz")
mb.obj("UF_Brackets", kind="trim")
iwall("UF_P1", "y", -3.22, 1.9, -0.2, U1, U2 - 0.22, ops=[(0.7, 1.6, U1, U1 + 2.1, "door")])
iwall("UF_P2", "x", -3.82, -0.2, 1.95, U1, U2 - 0.22)
rail("UF_VoidRail", -0.14, 1.98, st_end[0], 1.98, U1, 1.0, "wood")
room("bedroom", -3.82, -3.22, -0.26, 1.89, U1, 2.58, "E", fab="FabricWhite")
rs_end = stair("UF_Stair", 3.32, -3.0, U1, U2, "+y", 0.9, 0.28, "WoodLight", rails="left", rail_style="wood")
desk(0.9, -2.85, U1, 180, 1.4, 0.65)
bookshelf(0.6, 3.22, U1, 0, 1.2, 2.2)
armchair(1.8, 0.8, U1, 220, "FabricBeige")
floor_lamp(2.4, 1.5, U1)
lamp("UF_StudyLight", 1.4, -0.5, U2 - 0.22, 60)

# ---------------------------------------------------------------- roof terrace
slab("Roof", -4.0, -3.4, 4.0, 3.6, U2 + 0.2, 0.2, holes=[(2.85, -3.0, 3.8, rs_end[1])], top="WoodLight", under="WoodDark")
ob("Eaves", [(-4.25, -3.65, U2 - 0.05, 4.25, 3.85, U2 + 0.02)], ["TinRust"], kind="trim")
rails_rect("RoofRail", -3.95, -3.35, 3.95, 3.55, U2 + 0.2, "SNWE", style="wood")
rail("HatchRailW", 2.82, -3.0, 2.82, rs_end[1] - 0.05, U2 + 0.2, 1.0, "wood")
rail("HatchRailS", 2.82, -3.03, 3.8, -3.03, U2 + 0.2, 1.0, "wood")
antenna(-3.2, 2.8, U2 + 0.2, 3.6); antenna(-1.5, 3.0, U2 + 0.2, 2.6)
dish(1.0, 3.0, U2 + 0.2, 160)
water_tank(-2.8, -1.5, U2 + 0.2, 0, 0.55, 1.0, "PaintTeal")
bench(0.0, -2.9, U2 + 0.2, 180, 1.6)
for i in range(3):
    plant(-1.0 + i * 1.2, 2.9, U2 + 0.2, 0, 0.8, kind="bush")

# ---------------------------------------------------------------- dressing: window sheds, lanterns, plants, sign
ob("ShedS", [(-3.2, -3.75, G1 + 2.45, -1.1, -3.03, G1 + 2.52)], ["TinRust"], kind="trim")
ob("ShedW", [(-4.3, -1.7, G1 + 2.45, -3.63, 1.0, G1 + 2.52)], ["TinRust"], kind="trim")
sign_board("Sign", "青瓦茶屋", 0.0, -3.13, G1 + 2.55, 1.7, 0.42, 0, "WoodDark", "Lantern", 0.28, frame="PaintRed")
for i, (x, y, z) in enumerate(((-5.0, -5.4, DZ + 2.4), (5.0, -5.4, DZ + 2.4), (-4.2, -3.6, U1 + 2.3), (4.2, -3.6, U1 + 2.3),
                                (-0.95, -3.4, G1 + 2.5), (0.95, -3.4, G1 + 2.5))):
    mb = MB(); mb.box(-0.03, -0.03, -2.4 if i < 2 else 0, 0.03, 0.03, 0.25, "WoodDark") if i < 2 else None
    mb.box(-0.02, -0.4, 0.2, 0.02, 0.02, 0.25, "WoodDark"); mb.obj("LanternArm%d" % i, x, y, z, kind="trim")
    lamp("Lantern%d" % i, x, y - 0.38, z + 0.2, 30, (1.0, 0.5, 0.2), kind="lantern", glow="Lantern")
for i, (x, y) in enumerate(((-4.6, -4.9), (-3.9, -4.9), (3.7, -4.9), (4.6, -4.4), (4.6, 3.6), (-4.6, 3.6))):
    plant(x, y, DZ, 0, R_.uniform(0.7, 1.1) if False else 0.75 + 0.1 * (i % 3), kind=["bush", "tall", "bush"][i % 3])
planter(-2.6, -5.35, DZ, 0, 1.6, 0.35, 0.4, "WoodDark"); planter(2.6, -5.35, DZ, 0, 1.6, 0.35, 0.4, "WoodDark")
bench(-3.2, 3.85, DZ, 0, 1.6)
cable("Wire1", (-4.0, 3.5, U2 + 2.5), (-12.0, 9.0, 6.0), 1.0)
cable("Wire2", (4.0, 3.5, U2 + 1.0), (12.0, 8.0, 6.0), 1.2)

label_building(U2 + 0.2 + 3.6, -3.6, (1.0, -3.06, G1 + 1.5), 7.0)
spawn("stair_foot", 0.0, -5.6 - L - 1.2, 0, 0)
