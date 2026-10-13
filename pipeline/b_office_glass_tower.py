# 海港金融中心 Harbor Finance Tower — 10-storey glass curtain-wall office tower with a concrete core
# (U-stair + 2 elevators), double-height lobby, fitted office floors, vacant shell floors, executive top floor, roof helipad.
begin_building("office_glass_tower", "海港金融中心", "Harbor Finance Tower", "Modern Glass High-rise", "現代玻璃帷幕大樓",
               "luxury", "office high-rise", ["realistic", "modern", "corporate", "thriller", "cyberpunk"],
               "20x20 m, 10 floors: marble lobby + reception, 2 elevator shafts (car objects with level data) + fire stair, "
               "open-plan offices / meeting / pantry / server room, 5 vacant shell floors for custom fit-out, "
               "executive suite, roof with helipad and plant.", 10, PLOT)

X1, X2, Y1, Y2, T = -10.0, 10.0, -10.0, 10.0, 0.25
xi1, xi2, yi1, yi2 = X1 + T, X2 - T, Y1 + T, Y2 - T
Z = [0.0, 4.5] + [4.5 + 3.6 * i for i in range(1, 10)]          # 11 values: G + 9 floors + roof
NF = len(Z) - 1
CX1, CX2, CY1, CY2 = -4.0, 4.0, 0.0, 5.0                          # core
SX, SY = -2.8, 0.5
SHAFT = (-1.55, 2.5, 2.8, CY2 - 0.06)
ob("Plot", [(-13.0, -13.5, -0.4, 13.0, 12.0, 0.0)], ["StoneTile"], kind="floor", walkable=True)
ob("Forecourt", [(-6.0, -13.5, 0.0, 6.0, Y1, 0.02)], ["Marble"], kind="floor", walkable=True)
slab("F1_Floor", xi1, yi1, xi2, yi2, 0.0, 0.2, top="Marble", under="Concrete")

FIN = MB()
hole = None
levels = []
for f in range(NF):
    z0, z1 = Z[f], Z[f + 1]
    levels.append(round(z0, 3))
    top = z1 - 0.6
    if f == 0:
        ops = {"S": [(-9.6, -2.2, 0.15, top, "shop"), (-2.0, -0.05, 0, 2.6, "door_glass"), (0.05, 2.0, 0, 2.6, "door_glass"),
                     (2.2, 9.6, 0.15, top, "shop")],
               "E": [(-9.6, 9.6, 0.15, top, "shop")], "W": [(-9.6, 9.6, 0.15, top, "shop")],
               "N": [(-9.6, -4.4, 0.15, top, "shop"), (5.0, 6.2, 0, 2.4, "door_glass"), (7.6, 9.6, 0.15, top, "shop")]}
        ext = "MarbleBlack"
    else:
        ops = {s: [(-9.7, 9.7, z0 + 0.12, top, "shop")] for s in "SNWE"}
        ext = "PanelSteel"
    ring("F%d" % (f + 1), X1, Y1, X2, Y2, z0, z1, ext, "PlasterInt", T, 0.04, ops)
    if f > 0:
        slab("F%d_Floor" % (f + 1), xi1, yi1, xi2, yi2, z0, 0.3, holes=[hole, SHAFT],
             top="CarpetGrey" if f not in (5, 6, 7, 8) else "Concrete")
    hole, arrive = stair_u("F%d_Stair" % (f + 1), SX, SY, z0, z1, "+y", 1.0, 0.1, m="Concrete", rail_style="bar")
    zc = z1 - 0.3
    # core walls
    iwall("F%d_CoreS" % (f + 1), "x", CX1, CX2, CY1, z0, zc, t=0.25, m="Concrete",
          ops=[(-2.9, -1.9, z0, z0 + 2.1, "door_metal"), (-1.2, 3.6, z0, z0 + 2.6, "open")])
    iwall("F%d_CoreN" % (f + 1), "x", CX1, CX2, CY2, z0, zc, t=0.25, m="Concrete")
    iwall("F%d_CoreW" % (f + 1), "y", CY1 + 0.12, CY2 - 0.12, CX1, z0, zc, t=0.25, m="Concrete")
    iwall("F%d_CoreE" % (f + 1), "y", CY1 + 0.12, CY2 - 0.12, CX2, z0, zc, t=0.25, m="Concrete")
    iwall("F%d_StairWall" % (f + 1), "y", CY1 + 0.12, CY2 - 0.12, -1.66, z0, zc, t=0.15, m="Concrete")
    # elevator front wall with two door openings + sliding door pairs
    iwall("F%d_LiftFront" % (f + 1), "x", -1.58, CX2 - 0.12, SHAFT[1], z0, zc, t=0.15, m="Marble",
          ops=[(-1.0, 0.0, z0, z0 + 2.2, "open"), (1.2, 2.2, z0, z0 + 2.2, "open")])
    iwall("F%d_LiftMid" % (f + 1), "y", SHAFT[1] + 0.08, CY2 - 0.12, 0.6, z0, zc, t=0.12, m="Concrete")
    for k, (a1, a2) in enumerate(((-1.0, 0.0), (1.2, 2.2))):
        for j, sgn in enumerate((-1, 1)):
            mb = MB(); mb.box(0, -0.03, 0, 0.5, 0.03, 2.2, "Chrome")
            d = mb.obj("F%d_Lift%d_Door%d" % (f + 1, k, j), a1 + j * 0.5, SHAFT[1] - 0.1, z0, kind="door")
            d["openable"] = "slide"; d["open_offset"] = json.dumps([sgn * 0.48, 0, 0]); d["interact"] = "elevator_call"
        mb = MB(); mb.box(-0.06, -0.02, 0, 0.06, 0.0, 0.14, "MetalDark"); mb.box(-0.03, -0.03, 0.04, 0.03, -0.02, 0.1, "LED")
        o = mb.obj("F%d_Lift%d_Button" % (f + 1, k), a2 + 0.2, SHAFT[1] - 0.13, z0 + 1.1, kind="trim")
        o["interact"] = "elevator_call"; o["elevator"] = k; o["level"] = f
    lamp("F%d_LiftLobbyL" % (f + 1), 1.0, 1.2, zc, 40, (1.0, 0.95, 0.85))
    lamp("F%d_StairL" % (f + 1), -2.85, 3.5, zc, 20, (0.9, 0.95, 1.0))
    # facade fins
    for s_, (ax, c) in (("S", ("x", Y1)), ("N", ("x", Y2))):
        sg = -1 if s_ == "S" else 1
        for i in range(8):
            a = -9.8 + i * 2.8 + 0.7
            if f == 0 and -3 < a < 3 and s_ == "S":
                continue
            FIN.box(a - 0.04, min(c + sg * 0.05, c + sg * 0.35), z0, a + 0.04, max(c + sg * 0.05, c + sg * 0.35), z1, "FrameAlu")
    for s_, c in (("W", X1), ("E", X2)):
        sg = -1 if s_ == "W" else 1
        for i in range(8):
            a = -9.8 + i * 2.8 + 0.7
            FIN.box(min(c + sg * 0.05, c + sg * 0.35), a - 0.04, z0, max(c + sg * 0.05, c + sg * 0.35), a + 0.04, z1, "FrameAlu")
FIN.obj("Fins", kind="trim")
slab("Roof", xi1, yi1, xi2, yi2, Z[NF], 0.35, holes=[hole, SHAFT], top="Concrete")

# elevator cars (game: move along "levels")
for k, (x1_, x2_) in enumerate(((-1.55, 0.55), (0.65, 2.75))):
    mb = MB()
    mb.box(x1_, SHAFT[1] + 0.05, 0, x2_, CY2 - 0.15, 0.05, "MarbleBlack")
    mb.box(x1_, CY2 - 0.2, 0, x2_, CY2 - 0.15, 2.5, "Chrome"); mb.box(x1_, SHAFT[1] + 0.05, 0, x1_ + 0.05, CY2 - 0.15, 2.5, "Chrome")
    mb.box(x2_ - 0.05, SHAFT[1] + 0.05, 0, x2_, CY2 - 0.15, 2.5, "Chrome")
    mb.box(x1_, SHAFT[1] + 0.05, 2.45, x2_, CY2 - 0.15, 2.5, "LightCool")
    mb.box(x1_ + 0.1, CY2 - 0.25, 0.9, x2_ - 0.1, CY2 - 0.2, 0.95, "Brass")
    car = mb.obj("ElevatorCar%d" % k, kind="elevator", walkable=True)
    car["elevator"] = k; car["levels"] = json.dumps(levels); car["interact"] = "elevator"

# ---------------------------------------------------------------- lobby
reception(0.0, -5.0, 0, 0, 4.0)
office_chair(-0.8, -4.2, 0, 180); office_chair(0.8, -4.2, 0, 180)
for x in (-7.0, 7.0):
    sofa(x, -6.5, 0, 90 if x < 0 else 270, 2.4, "LeatherBlack"); coffee_table(x + (1.1 if x < 0 else -1.1), -6.5, 0, 90, 1.1, 0.6, "MarbleBlack")
    plant(x, -9.2, 0, 0, 1.6, "Concrete", "tall"); plant(x, -3.5, 0, 0, 1.6, "Concrete", "palm")
mb = MB()                                                        # security gates
for i in range(4):
    mb.box(-1.6 + i * 1.05, -0.2, 0, -1.45 + i * 1.05, 0.2, 1.0, "Chrome"); mb.box(-1.6 + i * 1.05, -0.2, 1.0, -1.45 + i * 1.05, 0.2, 1.02, "LED")
furn("Turnstiles", mb, 1.0, -1.5, 0, 0, "use")
mb = MB(); mb.box(-2.5, 0, 0, 2.5, 0.06, 1.2, "MarbleBlack"); furn("WallLogo", mb, 0.0, CY1 - 0.2, 1.8, 0)
text("LobbyLogo", "HARBOR FINANCE 海港金融", 0.0, CY1 - 0.21, 2.4, 0.3, "Brass", extrude=0.01)
for i, x in enumerate((-6, -2, 2, 6)):
    for j, y in enumerate((-7.5, -3.5)):
        lamp("LobbyL%d%d" % (i, j), x, y, Z[1] - 0.3, 120, (1.0, 0.92, 0.8), kind="pendant")
mb = MB()                                                        # entrance canopy
mb.box(-4.0, Y1 - 3.0, 4.0, 4.0, Y1, 4.25, "FrameAlu"); mb.box(-3.9, Y1 - 2.95, 3.98, 3.9, Y1 - 0.05, 4.0, "LightCool")
for x in (-3.8, 3.8):
    mb.cyl(x, Y1 - 2.8, 0, 4.0, 0.08, "Chrome", seg=12)
mb.obj("Canopy", kind="structure")
text("Address", "1 HARBOR AVE", 0.0, Y1 - 3.02, 4.12, 0.18, "LabelGlow", extrude=0.005)

# ---------------------------------------------------------------- office floors
def restroom(f):
    z0 = Z[f]; zc = Z[f + 1] - 0.3
    iwall("F%d_RR_W" % (f + 1), "y", CY1 + 0.12, CY2 - 0.12, 4.1, z0, zc, t=0.12) if False else None
    iwall("F%d_RR_E" % (f + 1), "y", 0.5, 5.0, 7.5, z0, zc, ops=[(0.8, 1.7, z0, z0 + 2.1, "door")])
    iwall("F%d_RR_S" % (f + 1), "x", 4.12, 7.5, 0.5, z0, zc)
    iwall("F%d_RR_N" % (f + 1), "x", 4.12, 7.5, 5.0, z0, zc)
    for i in range(3):
        toilet(4.7 + i * 0.95, 4.6, z0, 0)
    vanity(5.6, 1.0, z0, 180, 2.0)
    ob("F%d_RRFloor" % (f + 1), [(4.12, 0.56, z0, 7.44, 4.94, z0 + 0.008)], ["TileWhite"], kind="floor", walkable=True)
    lamp("F%d_RRL" % (f + 1), 5.8, 2.7, zc, 30)

for f in range(1, NF):
    z0 = Z[f]; zc = Z[f + 1] - 0.3; h = zc - z0
    restroom(f)
    vacant = f in (5, 6, 7, 8)
    if vacant:
        for i, (x, y) in enumerate(((-5, -5), (5, -5), (-6, 6), (6, 7))):
            lamp("F%d_VacL%d" % (f + 1, i), x, y, zc, 40, (0.9, 0.95, 1.0))
        sign_board("F%d_Lease" % (f + 1), "FOR LEASE 招租", 0.0, Y1 + 0.32, z0 + 1.3, 2.4, 0.5, 0, "White", "Black", 0.26)
        ob("F%d_VacantMarker" % (f + 1), [(-0.5, -0.5, z0, 0.5, 0.5, z0 + 0.001)], ["Concrete"], kind="floor", vacant=True)
        continue
    if f == NF - 1:          # executive top floor
        desk(-5.0, -7.0, z0, 0, 2.2, 0.9, "WoodDark"); armchair(-6.0, -4.6, z0, 200, "LeatherBlack"); armchair(-4.0, -4.6, z0, 160, "LeatherBlack")
        sofa(5.5, -8.6, z0, 0, 3.0, "LeatherBlack"); coffee_table(5.5, -7.2, z0, 0, 1.6, 0.8, "MarbleBlack"); rug(5.5, -7.2, z0, 0, 4.0, 3.0, "CarpetRed")
        meeting_table(-5.0, 6.5, z0, 0, 4.0, 1.4)
        bar_counter(6.0, 7.5, z0, 180, 3.0, "MarbleBlack", "Marble", stools=True)
        bookshelf(-9.5, -2.0, z0, 90, 3.0, 2.6, 0.4)
        for x in (-6, 0, 6):
            for y in (-6, 6):
                lamp("F%d_ExL%d%d" % (f + 1, x, y), x, y, zc, 80, kind="pendant" if y > 0 else "ceiling")
        plant(-9.2, -9.2, z0, 0, 1.6, kind="palm"); plant(9.2, -9.2, z0, 0, 1.6, kind="palm")
        continue
    room("office", xi1, yi1, xi2, -0.4, z0, h, "N")
    if f == 1:
        iwall("F2_MeetW", "x", xi1, -4.6, 2.0, z0, zc, ops=[(-6.5, -5.6, z0, z0 + 2.1, "door_glass")])
        iwall("F2_MeetE", "y", 2.06, yi2, -4.6, z0, zc, m="GlassFrost")
        room("meeting", xi1, 2.06, -4.6, yi2, z0, h, "S")
        kitchen_run(-3.0 + 9.0, 9.4, z0, 0, 3.0, "White", "Marble") if False else kitchen_run(8.0, 9.4, z0, 0, 2.6, "White", "Marble")
        cafe_set(5.0, 7.5, z0, 0); cafe_set(2.6, 7.5, z0, 0); vending(9.3, 6.0, z0, 270, "NeonRed")
    else:
        iwall("F%d_ServerW" % (f + 1), "x", xi1, -4.6, 2.0, z0, zc, ops=[(-6.5, -5.6, z0, z0 + 2.1, "door_metal")])
        iwall("F%d_ServerE" % (f + 1), "y", 2.06, yi2, -4.6, z0, zc)
        for i in range(4):
            server_rack(-9.0 + i * 1.0, 8.9, z0, 0)
        console(-6.5, 3.4, z0, 180, 2.0, 2)
        sofa(6.5, 8.9, z0, 0, 2.4, "FabricNavy"); coffee_table(6.5, 7.8, z0, 0); plant(9.2, 9.2, z0, 0, 1.2, kind="tall")
    for i, x in enumerate((-6.5, -2, 2.5, 7)):
        for j, y in enumerate((-7.5, -3.5)):
            lamp("F%d_OfL%d%d" % (f + 1, i, j), x, y, zc, 55, (0.95, 0.97, 1.0))
    lamp("F%d_NL1" % (f + 1), -6.5, 6.0, zc, 50); lamp("F%d_NL2" % (f + 1), 6.0, 7.0, zc, 50)

# ---------------------------------------------------------------- roof
zr = Z[NF]
ob("Parapet", [(X1, Y1, zr, X2, Y1 + 0.3, zr + 1.2), (X1, Y2 - 0.3, zr, X2, Y2, zr + 1.2),
               (X1, Y1 + 0.3, zr, X1 + 0.3, Y2 - 0.3, zr + 1.2), (X2 - 0.3, Y1 + 0.3, zr, X2, Y2 - 0.3, zr + 1.2)], ["PanelSteel"], kind="wall")
ob("Crown", [(X1 - 0.1, Y1 - 0.1, zr + 1.2, X2 + 0.1, Y1 + 0.1, zr + 1.35), (X1 - 0.1, Y2 - 0.1, zr + 1.2, X2 + 0.1, Y2 + 0.1, zr + 1.35),
             (X1 - 0.1, Y1, zr + 1.2, X1 + 0.1, Y2, zr + 1.35), (X2 - 0.1, Y1, zr + 1.2, X2 + 0.1, Y2, zr + 1.35)], ["NeonCyan"], kind="light_fixture")
ring("RoofCore", CX1, CY1, CX2, CY2, zr, zr + 3.0, "Concrete", "Concrete", 0.25, 0.0,
     {"S": [(-2.9, -1.9, zr, zr + 2.1, "door_metal")]})
slab("RoofCoreTop", CX1, CY1, CX2, CY2, zr + 3.2, 0.2, top="Concrete")
lamp("RoofCoreL", -2.0, 2.5, zr + 3.0, 25)
mb = MB()                                                        # helipad
mb.cyl(0, 0, 0, 0.12, 5.2, "Concrete", seg=40); mb.cyl(0, 0, 0.12, 0.14, 4.9, "PaintRed", seg=40); mb.cyl(0, 0, 0.14, 0.15, 4.6, "Concrete", seg=40)
mb.box(-1.6, -0.3, 0.15, 1.6, 0.3, 0.16, "White"); mb.box(-1.6, -2.0, 0.15, -1.0, 2.0, 0.16, "White"); mb.box(1.0, -2.0, 0.15, 1.6, 2.0, 0.16, "White")
furn("Helipad", mb, 0.0, -5.0, zr, 0, "use")
for i in range(2):
    mb = MB(); mb.box(-1.2, -1.2, 0, 1.2, 1.2, 2.2, "PanelSteel"); mb.cyl(0, 0, 2.2, 2.6, 1.0, "MetalDark", seg=24)
    furn("CoolingTower", mb, 6.5, 2.5 + i * 3.0, zr, 0)
water_tank(-7.0, 7.0, zr, 0, 1.0, 2.0, "PanelSteel"); antenna(-7.5, 3.0, zr, 5.0)

label_building(zr + 3.2 + 2.0, Y1 - 0.5, (2.6, Y1 - 0.05, 1.6), 10.0)
spawn("forecourt", 0.0, Y1 - 4.0, 0, 0)
