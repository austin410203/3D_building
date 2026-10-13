# 霓光電路別墅 Neon Circuit Villa — near-future luxury villa: charcoal panels traced with glowing circuit lines,
# walled courtyard with tree + holo table, glowing stairs, roof terraces (ref: isometric neon-line villa).
import random as _r
begin_building("villa_neon_circuit", "霓光電路別墅", "Neon Circuit Villa", "Near-Future Tech Villa", "近未來科技別墅",
               "luxury", "villa", ["cyberpunk", "sci-fi", "near-future", "realistic", "anime"],
               "Charcoal composite villa with cyan circuit-trace lighting: gated courtyard, glowing steps, G/F lounge + kitchen + "
               "game room, 2F suite with balcony, west wing with roof terrace reached by an outside stair.", 2, PLOT)

rr = _r.Random(5)
PZ = 0.45
G1, G2, U2 = PZ, PZ + 3.4, PZ + 6.6
ob("Plot", [(-12.0, -12.0, -0.4, 12.0, 11.0, 0.0)], ["Concrete"], kind="floor", walkable=True)
ob("Plinth", [(-11.0, -9.0, -0.2, 11.0, 10.0, PZ)], ["StoneTile"], kind="floor", walkable=True)
ob("Road", [(-1.4, -12.0, 0.0, 1.4, -9.0, 0.02)], ["PanelDark"], kind="floor", walkable=True)
ob("RoadGlow", [(-1.45, -12.0, 0.02, -1.38, -9.0, 0.03), (1.38, -12.0, 0.02, 1.45, -9.0, 0.03)], ["NeonCyan"], kind="light_fixture")

TR = []
def traces(face, sgn, axis, a1, a2, z1, z2, n=6, glow="NeonCyan"):
    """random orthogonal glowing PCB traces on a wall face (axis: along which the face runs)"""
    for i in range(n):
        a = rr.uniform(a1 + 0.3, a2 - 0.3); z = z1 + 0.05
        pts = [(a, z)]
        for k in range(rr.randint(2, 4)):
            z = min(z2 - 0.2, z + rr.uniform(0.4, 1.4)); pts.append((a, z))
            a = max(a1 + 0.1, min(a2 - 0.1, a + rr.choice((-1, 1)) * rr.uniform(0.3, 1.5))); pts.append((a, z))
        for (p, q), (p2, q2) in zip(pts, pts[1:]):
            lo_a, hi_a = sorted((p, p2)); lo_z, hi_z = sorted((q, q2))
            d1, d2 = sorted((face, face + sgn * 0.015))
            if axis == "x":
                TR.append((lo_a - 0.015, d1, lo_z - 0.015, hi_a + 0.015, d2, hi_z + 0.015))
            else:
                TR.append((d1, lo_a - 0.015, lo_z - 0.015, d2, hi_a + 0.015, hi_z + 0.015))
        p, q = pts[-1]
        d1, d2 = sorted((face, face + sgn * 0.02))
        TR.append((p - 0.06, d1, q - 0.06, p + 0.06, d2, q + 0.06) if axis == "x" else (d1, p - 0.06, q - 0.06, d2, p + 0.06, q + 0.06))

# ---------------------------------------------------------------- perimeter wall + gate + courtyard
W_ = "PanelDark"
ob("Perimeter", [(-11.0, -9.0, PZ, -1.6, -8.7, PZ + 1.8), (1.6, -9.0, PZ, 11.0, -8.7, PZ + 1.8),
                 (-11.0, -8.7, PZ, -10.7, 10.0, PZ + 1.8), (10.7, -8.7, PZ, 11.0, 10.0, PZ + 1.8)], [W_], kind="wall")
traces(-9.03, -1, "x", -11.0, -1.6, PZ, PZ + 1.8, 5); traces(-9.03, -1, "x", 1.6, 11.0, PZ, PZ + 1.8, 5)
mb = MB()                                                       # sliding slatted gate
for i in range(12):
    mb.box(-1.55 + i * 0.26, -0.03, 0.0, -1.4 + i * 0.26, 0.03, 1.7, "Wood" + "Dark")
mb.box(-1.6, -0.04, 1.7, 1.6, 0.04, 1.78, "NeonCyan")
g = mb.obj("Gate", 0, -8.85, PZ, kind="door"); g["openable"] = "slide"; g["open_offset"] = json.dumps([3.2, 0, 0]); g["interact"] = "open"
n = 3; L = (n - 1) * 0.28
stair("GateSteps", 0.0, -9.0 - L - 0.05, 0.0, PZ, "+y", 3.0, 0.28, "PanelDark", rails="none", solid=True)
ob("StepGlow", [(-1.5, -9.0 - L - 0.06 + i * 0.28, 0.15 * (i + 1) - 0.02, 1.5, -9.0 - L - 0.04 + i * 0.28, 0.15 * (i + 1)) for i in range(n - 1)],
   ["NeonCyan"], kind="light_fixture")
mb = MB()                                                       # holo table + ring
mb.cyl(0, 0, 0, 0.75, 0.5, "PanelDark", seg=24); mb.cyl(0, 0, 0.75, 0.8, 0.9, "GlassDark", seg=32)
mb.cyl(0, 0, 0.8, 0.82, 0.88, "NeonCyan", seg=32, r2=0.86); mb.cyl(0, 0, 0.0, 0.02, 2.0, "NeonCyan", seg=48)
mb.cyl(0, 0, 0.02, 0.03, 1.94, "PanelDark", seg=48)
furn("HoloTable", mb, 1.5, -4.5, PZ, 0, "use")
for k in range(4):
    a = k * math.pi / 2 + math.pi / 4
    stool(1.5 + math.cos(a) * 1.2, -4.5 + math.sin(a) * 1.2, PZ, 0, 0.46, "PlasticDark")
tree(-3.2, -5.6, PZ, 0.9, "broad", seed=71)
mb = MB(); mb.cyl(0, 0, 0, 0.35, 1.0, "PanelDark", seg=24); mb.cyl(0, 0, 0.35, 0.37, 0.98, "Soil", seg=24); mb.cyl(0, 0, 0.3, 0.33, 1.02, "NeonCyan", seg=24)
furn("TreeRing", mb, -3.2, -5.6, PZ, 0)
for (x, y) in ((-9.8, -7.8), (9.8, -7.8), (-6.0, -7.9), (6.0, -7.9), (9.8, -2.0)):
    plant(x, y, PZ, 0, 0.9, "PanelDark", "tall")
bench(6.5, -7.9, PZ, 0, 2.0, "WoodDark", "PanelDark")
for i, x in enumerate((-6, -1.5, 3.5)):
    lamp("CourtL%d" % i, x, -6.0, PZ + 2.6, 30, (0.4, 0.9, 1.0), kind="point", fixture=False)

# ---------------------------------------------------------------- main house (east)
ring("M", -3.0, -2.0, 9.0, 8.0, G1, G2, W_, "PlasterInt", 0.25, 0.03,
     {"S": [(-2.6, 0.4, G1 + 0.8, G2 - 0.6, "win3"), (1.0, 2.2, G1, G1 + 2.4, "door_glass"), (3.0, 8.4, G1 + 0.1, G2 - 0.5, "shop")],
      "E": [(0.0, 3.0, G1 + 0.9, G2 - 0.6, "win"), (5.0, 7.0, G1 + 0.9, G2 - 0.6, "win")],
      "N": [(4.0, 7.0, G1 + 1.2, G2 - 0.6, "win")], "W": [(4.5, 6.5, G1, G1 + 2.2, "door_glass")]})
slab("M_Floor", -2.75, -1.75, 8.75, 7.75, G1, 0.2, top="MarbleBlack", under="Concrete")
st = stair("M_Stair", -2.25, 0.2, G1, G2, "+y", 0.9, 0.28, "PanelDark", rails="right", rail_style="glass")
ob("M_StairGlow", [(-2.72, 0.2, G1 + 0.02, -2.96, st[1], G1 + 0.05)], ["NeonCyan"], kind="light_fixture")
iwall("M_P1", "x", -1.7, 8.75, 3.2, G1, G2 - 0.22, ops=[(-1.2, 0.0, G1, G1 + 2.1, "open"), (5.5, 6.4, G1, G1 + 2.1, "door")])
sofa(4.5, 2.6, G1, 0, 3.2, "LeatherBlack"); sofa(7.9, 0.8, G1, 270, 2.2, "LeatherBlack")
coffee_table(4.5, 1.0, G1, 0, 1.6, 0.8, "GlassDark"); rug(5.2, 1.0, G1, 0, 4.4, 3.0, "CarpetGrey")
tv(4.5, -1.6, G1, 180, 2.4, cab=True)
kitchen_run(1.0, 7.42, G1, 0, 3.6, "PanelDark", "Marble")
mb = MB(); mb.box(-1.2, -0.45, 0, 1.2, 0.45, 0.9, "PanelDark"); mb.box(-1.3, -0.5, 0.9, 1.3, 0.5, 0.95, "Marble")
mb.box(-1.2, -0.46, 0.1, 1.2, -0.45, 0.13, "NeonCyan"); furn("Island", mb, 1.0, 5.5, G1, 0, "cook")
fridge(-1.7, 7.4, G1, 0, 0.9, 2.0)
for i in range(3):
    arcade(6.0 + i * 0.85, 7.3, G1, 0, "PlasticDark", ["NeonCyan", "NeonPink", "NeonPurple"][i])
armchair(7.0, 4.6, G1, 0, "FabricNavy")
for i, (x, y) in enumerate(((4.5, 1.0), (1.0, 5.5), (7.0, 5.6), (0.0, 1.2))):
    lamp("M_L%d" % i, x, y, G2 - 0.22, 60, (0.95, 0.9, 1.0), kind="pendant" if i == 1 else "ceiling")
ob("M_CoveGlow", [(-2.7, -1.7, G2 - 0.3, 8.7, -1.66, G2 - 0.26)], ["NeonCyan"], kind="light_fixture")

# 2F
slab("U_Floor", -2.75, -1.75, 8.75, 7.75, G2, 0.22, holes=[(-2.72, 0.15, -1.78, st[1] + 0.02)], top="Parquet", under="Ceiling")
ring("U", -1.0, 0.0, 9.0, 8.0, G2, U2, W_, "PlasterInt", 0.25, 0.03,
     {"S": [(-0.6, 2.0, G2 + 0.9, U2 - 0.6, "win3"), (3.0, 4.2, G2, G2 + 2.4, "door_glass"), (5.0, 8.5, G2 + 0.9, U2 - 0.6, "win3")],
      "E": [(2.0, 6.0, G2 + 0.9, U2 - 0.6, "win3")], "W": [(4.5, 5.5, G2, G2 + 2.3, "door_glass")],
      "N": [(1.0, 3.0, G2 + 1.2, U2 - 0.6, "win")]})
rail("U_HoleE", -1.74, 0.15, -1.74, st[1] - 0.05, G2, 1.0, "glass"); rail("U_HoleS", -2.72, 0.13, -1.74, 0.13, G2, 1.0, "glass")
rail("U_WEdge", -3.0, -2.0, -3.0, 8.0, G2, 1.0, "glass"); rail("U_NEdge", -3.0, 8.0, -1.0, 8.0, G2, 1.0, "glass")
rail("U_Front", -3.0, -2.0, 9.0, -2.0, G2, 1.0, "glass"); rail("U_E", 9.0, -2.0, 9.0, 0.0, G2, 1.0, "glass")

iwall("U_P1", "y", 0.25, 7.75, 4.6, G2, U2 - 0.22, ops=[(0.6, 1.5, G2, G2 + 2.1, "door")])
iwall("U_P2", "x", 4.66, 8.75, 4.2, G2, U2 - 0.22, ops=[(5.0, 5.9, G2, G2 + 2.1, "door")])
bed(7.68, 2.2, G2, 270, 1.9, 2.1, "FabricNavy", "PanelDark")
nightstand(7.8, 0.6, G2, 90) if False else None
room("bath", 4.66, 4.26, 8.75, 7.75, G2, U2 - 0.22 - G2, "S")
desk(1.0, 7.3, G2, 0, 1.8, 0.75, "PanelDark"); bookshelf(-0.7, 5.0, G2, 90, 1.6, 2.4); sofa(1.4, 1.0, G2, 0, 2.2, "FabricNavy") if False else armchair(1.5, 1.2, G2, 200, "FabricNavy")
lamp("U_L1", 1.8, 3.5, U2 - 0.22, 55, (0.9, 0.9, 1.0)); lamp("U_L2", 6.8, 2.0, U2 - 0.22, 50)
slab("U_Roof", -1.0, 0.0, 9.0, 8.0, U2 + 0.2, 0.25, top=W_, under="Ceiling")
ob("U_RoofCap", [(-1.1, -0.1, U2 + 0.2, 9.1, 0.05, U2 + 0.28), (-1.1, 7.95, U2 + 0.2, 9.1, 8.1, U2 + 0.28),
                 (-1.1, 0.05, U2 + 0.2, -0.95, 7.95, U2 + 0.28), (8.95, 0.05, U2 + 0.2, 9.1, 7.95, U2 + 0.28)], ["NeonCyan"], kind="light_fixture")
mb = MB()                                                       # perforated screen panel on the 2F front (ref)
for i in range(10):
    for j in range(9):
        mb.box(5.05 + i * 0.35, -0.12, G2 + 0.3 + j * 0.35, 5.08 + i * 0.35, -0.08, G2 + 0.6 + j * 0.35, "NeonCyan" if (i + j) % 4 == 0 else "Metal")
mb.obj("ScreenPanel", kind="trim") if False else None
lamp("U_BalcL", 3.6, -1.4, U2 - 0.4, 25, (0.4, 0.9, 1.0), kind="point", fixture=False)

# ---------------------------------------------------------------- west wing + roof terrace
ring("Wg", -10.4, 1.5, -3.0, 9.6, G1, G2, W_, "PlasterInt", 0.25, 0.03,
     {"S": [(-9.6, -6.6, G1 + 0.8, G2 - 0.6, "win"), (-5.6, -4.4, G1, G1 + 2.3, "door_glass")],
      "W": [(3.0, 8.0, G1 + 0.8, G2 - 0.6, "win3")]}, sides="SNW")
ob("WgECap", [(-3.25, 8.0, G1, -3.0, 9.6, G2)], [W_], kind="wall")
slab("Wg_Floor", -10.15, 1.75, -3.25, 9.35, G1, 0.2, top="Parquet", under="Concrete")
bed(-8.2, 7.6, G1, 0, 1.6, 2.0, "FabricWhite", "PanelDark"); desk(-9.6, 4.0, G1, 90, 1.4, 0.7, "PanelDark")
plant(-4.0, 2.2, G1, 0, 1.0, "PanelDark", "tall"); lamp("Wg_L", -7.0, 5.5, G2 - 0.22, 55)
slab("Wg_Roof", -10.4, 1.5, -3.0, 9.6, G2, 0.25, top="WoodDark", under="Ceiling")
rail("WgRailS", -9.45, 1.5, -3.05, 1.5, G2, 1.0, "glass"); rail("WgRailW", -10.4, 1.5, -10.4, 9.6, G2, 1.0, "glass")
rail("WgRailN", -10.4, 9.6, -3.05, 9.6, G2, 1.0, "glass")
umbrella_table(-7.0, 4.5, G2, 0, "AwningWhite"); sofa(-7.0, 8.9, G2, 0, 2.6, "FabricWhite")
plant(-9.8, 2.1, G2, 0, 1.0, "PanelDark", "tall"); plant(-9.8, 8.9, G2, 0, 1.0, "PanelDark")
o = stair("WgStair", -9.6, -2.5, G1, G2, "+y", 1.0, 0.28, W_, rails="right", rail_style="glass") if False else None
# outside stair from courtyard to the wing terrace (glowing steps), along the wing's east face
es = stair("WgStair", -2.0, 9.6 - 0.15, G1, G2, "-y", 1.0, 0.28, W_, rails="left", rail_style="glass") if False else None
es = stair("WgStair", -10.0, 1.5 - (round((G2 - G1) / 0.18) - 1) * 0.28, G1, G2, "+y", 1.0, 0.28, W_, rails="right", rail_style="glass")
ob("WgStairGlow", [(-10.52, -4.2, G1 + 0.02, -10.5, es[1], G1 + 0.05)], ["NeonCyan"], kind="light_fixture") if False else None
ob("Wg_RoofOpen", [(-10.4, 1.48, G2 - 0.01, -9.5, 1.52, G2)], ["Concrete"], kind="trim")

# glowing circuit traces on facades
traces(-2.03, -1, "x", -3.0, 9.0, G1, G2, 10)
traces(-0.03, -1, "x", -1.0, 9.0, G2, U2, 7)
traces(9.03, 1, "y", -2.0, 8.0, G1, U2, 9)
traces(1.47, -1, "x", -10.4, -3.0, G1, G2, 6)
traces(-10.43, -1, "y", 1.5, 9.6, G1, G2, 6)
mb = MB()
for b in TR:
    mb.box(*b, "NeonCyan")
mb.obj("CircuitTraces", kind="light_fixture")
for i, (x, y, z) in enumerate(((3.0, -2.6, G2 - 0.4), (-6.5, 1.0, G2 - 0.6), (9.6, 3.0, U2 - 0.8))):
    lamp("TraceGlow%d" % i, x, y, z, 40, (0.3, 0.9, 1.0), kind="point", fixture=False)

label_building(U2 + 0.3 + 2.4, -2.6, (2.6, -2.05, G1 + 1.6), 9.0)
spawn("gate", 0.0, -11.5, 0, 0)
