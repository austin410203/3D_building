# District 2 — civic & public buildings (10). Names prefixed _d2_.

def _d2_truck(x, y, rot=0, body="PlasticRed", ladder=True):
    mb = MB()
    mb.box(-1.2, -4.2, 0.5, 1.2, 2.0, 2.9, body); mb.box(-1.2, -4.2, 2.9, 1.2, -2.6, 3.1, body)
    mb.box(-1.15, -4.25, 1.6, 1.15, -4.2, 2.7, "GlassDark")
    for v in (-3.2, 0.6, 1.6):
        for sx in (-1.2, 1.05):
            mb.cyl(sx, v, 0.5, 0.5, 0.5, "Rubber", seg=16, axis="x") if False else mb.cyl(sx, v, 0.5, 0.5, 0.0, "Rubber", seg=4) if False else None
    for v in (-3.2, 0.6, 1.6):
        mb.cyl(-1.25, v, 0.5, 2.5, 0.48, "Rubber", seg=18, axis="x")
    mb.box(-1.22, -2.4, 1.0, 1.22, 1.9, 1.05, "Chrome"); mb.box(-0.3, -4.26, 3.0, 0.3, -4.2, 3.12, "NeonRed")
    if ladder:
        mb.box(-0.4, -2.0, 3.1, -0.3, 2.6, 3.2, "Chrome"); mb.box(0.3, -2.0, 3.1, 0.4, 2.6, 3.2, "Chrome")
        for i in range(12):
            mb.box(-0.3, -1.9 + i * 0.38, 3.12, 0.3, -1.86 + i * 0.38, 3.18, "Chrome")
    return furn("FireTruck", mb, x, y, 0.0, rot, "use")

def _d2_fire(ctx):
    x1, y2, Zs = ctx["x1"], ctx["y2"], ctx["Z"]
    _d2_truck(-4.0, -2.3); _d2_truck(3.4, -2.3)
    for i, x in enumerate((-4.0, 3.4)):
        lamp("BayL%d" % i, x, -2.0, Zs[1] - 0.3, 120, (0.95, 0.97, 1.0))
    mb = MB()                                                    # hose-drying tower at the back-left corner
    mb.box(x1 - 3.2, y2 - 3.2, 0, x1, y2, 15.0, "Brick")
    for z in (5.0, 8.0, 11.0):
        mb.box(x1 - 2.2, y2 - 3.21, z, x1 - 1.0, y2 - 3.19, z + 1.6, "GlassDark")
    mb.box(x1 - 3.4, y2 - 3.4, 15.0, x1 + 0.2, y2 + 0.2, 15.4, "Stone")
    mb.obj("HoseTower", kind="structure")
    mb = MB(); mb.box(-0.1, -0.1, 0, 0.1, 0.1, 0.9, "PlasticRed"); mb.cyl(0, 0, 0.9, 1.0, 0.13, "PlasticRed", seg=12)
    furn("Hydrant", mb, ctx["x2"] + 1.0, ctx["y1"] - 1.5, 0, 0)
reg(("fire_station", "海港消防局", "Harbor Fire Station", "Civic Fire Station", "消防局",
     "civic", "fire station", ["realistic", "rescue-sim", "anime", "action"],
     "Brick 2-storey station: double apparatus bay with two ladder trucks behind roller doors, hose tower, upstairs dorm + lounge."),
    dict(W=16, D=14, floors=2, h0=4.6, h=3.2, ext="Brick", frame="FrameWhite", win="win", ground="garage",
         g_front=[("none", 1), ("none", 1)], g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("dorm", 1), ("lounge", 1)],
         u_back=[("storage", 1), ("bath", 0.6)], s_ops0=[(-7.4, -0.6, 0, 4.0, "roller"), (0.6, 6.2, 0, 4.0, "roller")],
         door_k="door", door_x=7.0, door_w=0.9, roof="flat", decor=["bands", "antenna"], band_m="Stone", side=5.0,
         sign=("海港消防局  FIRE STATION", "PaintRed", "White", 7.0), sign_x=-0.3, front=6.0), _d2_fire)

def _d2_police(ctx):
    mb = MB(); mb.box(-0.25, -0.25, 0, 0.25, 0.25, 0.4, "PlasticBlue"); mb.box(-0.2, -0.2, 0.4, 0.2, 0.2, 0.42, "NeonBlue")
    mb.obj("BlueLamp", ctx["door_x_"], ctx["y1"] - 0.3, 3.3, kind="light_fixture") if "door_x_" in ctx else None
    car(ctx["x1"] + 2.0, ctx["y1"] - 4.0, 0.0, 90, "White"); car(ctx["x1"] + 5.2, ctx["y1"] - 4.0, 0.0, 90, "PlasticBlue")
    lamp("PoliceBlue", -1.0, ctx["y1"] - 0.4, 3.2, 40, (0.2, 0.4, 1.0), kind="point", fixture=False)
reg(("police_station", "海港警察局", "Harbor Police Station", "Civic Police Station", "警察局",
     "civic", "police station", ["realistic", "crime", "action", "detective", "anime"],
     "Concrete 2-storey precinct: public lobby with front desk, squad office, holding/storage, upstairs open office, briefing room, server room."),
    dict(W=18, D=13, floors=2, h0=3.6, ext="Concrete", ext0="BrickDark", frame="FrameAlu", win="win3", ground="lobby",
         g_front=[("lobby", 1.2), ("office", 1)], g_back=[("storage", 1), ("bath", 0.6)], u_front=[("office_open", 1.5), ("meeting", 1)],
         u_back=[("server", 1), ("bath", 0.6)], door_k="door_glass", door_x=-4.0, door_w=1.6, roof="flat", decor=["antenna", "walllamps"],
         sign=("海港警察局  POLICE", "PlasticBlue", "White", 6.0), front=7.0), _d2_police)

def _d2_hosp(ctx):
    mb = MB(); mb.box(-0.6, -0.12, -0.6, 0.6, 0.0, 0.6, "White"); mb.box(-0.5, -0.13, -0.15, 0.5, -0.12, 0.15, "NeonRed")
    mb.box(-0.15, -0.13, -0.5, 0.15, -0.12, 0.5, "NeonRed"); mb.obj("RedCross", ctx["x2"] - 1.5, ctx["y1"] - 0.05, ctx["Z"][3] - 1.5, kind="sign")
    mb = MB()                                                    # drop-off canopy
    mb.box(-3.0, -4.0, 3.2, 3.0, 0.0, 3.45, "White"); mb.box(-2.9, -3.9, 3.15, 2.9, -0.1, 3.2, "LightCool")
    for x in (-2.8, 2.8):
        mb.cyl(x, -3.8, 0, 3.2, 0.1, "Chrome", seg=12)
    mb.obj("Canopy", -5.0, ctx["y1"], 0, kind="structure")
    mb = MB(); mb.box(-1.0, -2.6, 0.4, 1.0, 2.6, 2.6, "White"); mb.box(-1.01, -1.0, 1.2, 1.01, 0.0, 1.6, "PlasticRed")
    mb.box(-0.95, -2.62, 1.5, 0.95, -2.6, 2.3, "GlassDark")
    for v in (-1.6, 1.6):
        mb.cyl(-1.05, v, 0.42, 2.1, 0.4, "Rubber", seg=16, axis="x")
    furn("Ambulance", mb, 2.0, ctx["y1"] - 4.5, 0, 90, "use")
reg(("hospital_general", "仁心綜合醫院", "Renxin General Hospital", "Modern Hospital", "現代醫院",
     "civic", "hospital", ["realistic", "horror", "medical-drama", "zombie", "anime"],
     "3-storey tiled hospital: lobby + triage clinics, wards with beds, exam rooms, roof terrace, drop-off canopy, ambulance, red cross."),
    dict(W=22, D=15, floors=3, h0=3.8, h=3.4, ext="TileWhite", frame="FrameAlu", win="win3", ground="lobby",
         g_front=[("lobby", 1.3), ("clinic", 1), ("clinic", 1)], g_back=[("ward", 1), ("bath", 0.5)],
         u_front=[("ward", 1), ("ward", 1), ("clinic", 1)], u_back=[("clinic", 1), ("bath", 0.5)], door_x=-5.0, door_w=1.8,
         roof="terrace", decor=["bands", "ac"], band_m="PlasticBlue", sign=("仁心綜合醫院  HOSPITAL", "White", "PlasticRed", 8.0),
         sign_x=3.0, front=7.0), _d2_hosp)

def _d2_school(ctx):
    mb = MB(); mb.cyl(0, 0, 0, 9.0, 0.05, "Chrome", seg=8); mb.box(0.05, -0.01, 7.6, 1.6, 0.01, 8.6, "PaintRed")
    mb.obj("FlagPole", ctx["x1"] - 1.5, ctx["y1"] - 4.0, 0, kind="trim")
    mb = MB(); mb.cyl(0, -0.05, 0, 0, 0.6, "White", seg=32, axis="y"); mb.cyl(0, -0.08, -0.02, 0.02, 0.62, "Black", seg=32, axis="y") if False else None
    mb.box(-0.02, -0.12, 0, 0.02, -0.1, 0.45, "Black"); mb.box(0, -0.12, -0.02, 0.32, -0.1, 0.02, "Black")
    mb.obj("Clock", 0.0, ctx["y1"] - 0.02, ctx["roof_z"] - 1.0, kind="sign")
    mb = MB()                                                    # basketball court + hoops in the front yard
    mb.box(-6.0, -3.0, 0.0, 6.0, 3.0, 0.02, "PlasticBlue"); mb.box(-0.03, -3.0, 0.02, 0.03, 3.0, 0.025, "White")
    for sx in (-1, 1):
        mb.cyl(sx * 6.4, 0, 0, 3.0, 0.06, "MetalDark", seg=8); mb.box(sx * 6.4 - 0.05, -0.9, 2.8, sx * 6.4 + 0.05, 0.9, 3.9, "White")
        mb.cyl(sx * 5.9, 0, 3.05, 3.08, 0.23, "PlasticRed", seg=16)
    mb.obj("Court", 4.0, ctx["y1"] - 4.8, 0, kind="floor")["walkable"] = True
reg(("school_primary", "海港國民小學", "Harbor Primary School", "Asian Public School", "公立學校",
     "civic", "school", ["slice-of-life", "anime", "horror", "realistic", "school-life"],
     "3-storey brick school: classrooms with desks/whiteboards on every floor, library, front-yard basketball court, flagpole, clock."),
    dict(W=26, D=13, floors=3, h0=3.6, h=3.4, ext="Brick", frame="FrameWhite", win="win3", bay=3.0, ww=2.0, ground="lobby",
         g_front=[("classroom", 1), ("lobby", 0.7), ("classroom", 1)], g_back=[("library", 1), ("bath", 0.6)],
         u_front=[("classroom", 1), ("classroom", 1), ("classroom", 1)], u_back=[("classroom", 1), ("bath", 0.6)],
         door_x=0.4, door_w=1.8, door_k="door_glass", roof="flat", decor=["bands", "cornice"], band_m="Concrete",
         sign=("海港國民小學", "White", "Black", 4.0), front=9.5), _d2_school)

def _d2_lib(ctx):
    mb = MB()
    for i in range(9):
        x = ctx["x1"] + 1.0 + i * (ctx["W"] - 2.0) / 8
        mb.box(x - 0.15, ctx["y1"] - 1.0, ctx["Z"][1] - 0.3, x + 0.15, ctx["y1"], ctx["roof_z"] + 0.4, "Concrete")
    mb.box(ctx["x1"] - 0.5, ctx["y1"] - 1.2, ctx["roof_z"] + 0.4, ctx["x2"] + 0.5, ctx["y1"] + 0.2, ctx["roof_z"] + 1.0, "Concrete")
    mb.obj("BrutalFins", kind="structure")
reg(("library_brutalist", "市立混凝土圖書館", "Concrete Public Library", "Brutalist", "粗獷主義",
     "civic", "library", ["realistic", "dystopian", "mystery", "anime", "post-apocalyptic"],
     "Massive exposed-concrete library: tall reading hall of stacks, upper reading room + meeting room, deep concrete fins and slab crown."),
    dict(W=18, D=14, floors=2, h0=4.4, h=4.0, ext="Concrete", frame="MetalDark", win="win", bay=3.4, ww=1.0, sill=0.6, head=3.6,
         ground="library", g_front=[("library", 1)], g_back=[("library", 1), ("bath", 0.5)], u_front=[("library", 1), ("meeting", 0.7)],
         u_back=[("lounge", 1)], floor="CarpetGrey", door_x=-3.0, door_w=1.8, door_k="door_glass", roof="flat", parapet=0.4,
         sign=("市立圖書館  PUBLIC LIBRARY", "Concrete", "Black", 7.0), front=5.0), _d2_lib)

reg(("bank_classical", "海港儲蓄銀行", "Harbor Savings Bank", "Neoclassical Bank", "新古典銀行",
     "luxury", "bank", ["realistic", "heist", "noir", "western", "civic"],
     "Granite neoclassical bank on a podium: columned portico with pediment, banking hall with teller counter, vault/server room, offices upstairs."),
    dict(W=14, D=13, floors=2, h0=5.0, h=3.6, plinth=1.2, plinth_m="Stone", ext="Stone", frame="Brass", win="win", bay=3.0, ww=1.2, head=3.6,
         ground="bank", g_front=[("bank", 1)], g_back=[("server", 1), ("bath", 0.6)], u_front=[("office_open", 1)], u_back=[("meeting", 1)],
         floor0="Marble", porch=True, porch_roof="Marble", porch_w=9.0, porch_d=2.8, porch_col="Marble", porch_h=4.6, porch_floor="Marble", door_k="door_double",
         door_m="WoodDark", door_w=1.8, door_x=-1.0, roof="flat", roof_m="Stone", decor=["cornice", "pilasters", "quoins"], band_m="Marble",
         front=7.0))

def _d2_post(ctx):
    mb = MB(); mb.box(-0.3, -0.25, 0, 0.3, 0.25, 1.2, "PlasticGreen"); mb.cyl(0, 0, 1.2, 1.25, 0.3, "PlasticGreen", seg=16)
    mb.box(-0.2, -0.26, 0.9, 0.2, -0.25, 0.95, "Black"); furn("PostBox", mb, ctx["x2"] - 1.0, ctx["y1"] - 1.2, 0, 0, "use")
reg(("post_office", "海港郵局", "Harbor Post Office", "Civic Post Office", "郵局",
     "civic", "post office", ["realistic", "slice-of-life", "anime", "rpg-village"],
     "Single-storey cream-brick post office: counter hall with rope queue, parcel storage, green post box, flag."),
    dict(W=12, D=10, floors=1, h0=4.0, ext="BrickCream", frame="PlasticGreen", win="win", ground="bank",
         g_front=[("bank", 1.4), ("storage", 1)], door_x=-2.0, door_w=1.6, door_k="door_glass", roof="flat", decor=["cornice"],
         band_m="Stone", sign=("郵局  POST OFFICE", "PlasticGreen", "White", 5.0)), _d2_post)

def _d2_chapel(ctx):
    x1, y1 = ctx["x1"], ctx["y1"]
    mb = MB()
    mb.box(x1 - 3.2, y1, 0, x1, y1 + 3.2, 12.0, "Stone")
    for z in (6.0, 9.4):
        mb.box(x1 - 2.2, y1 - 0.01, z, x1 - 1.0, y1 + 0.01, z + 1.6, "GlassBlue")
    mb.box(x1 - 3.4, y1 - 0.2, 12.0, x1 + 0.2, y1 + 3.4, 12.3, "Stone")
    mb.cyl(x1 - 1.6, y1 + 1.6, 12.3, 18.5, 1.9, "SlateDark", seg=4, r2=0.02)
    mb.box(x1 - 1.62, y1 + 1.55, 18.5, x1 - 1.58, y1 + 1.65, 19.7, "Brass"); mb.box(x1 - 1.95, y1 + 1.55, 19.1, x1 - 1.25, y1 + 1.65, 19.18, "Brass")
    mb.cyl(x1 - 1.6, y1 + 1.6, 10.0, 11.6, 0.6, "Brass", seg=20, r2=0.35)
    mb.obj("BellTower", kind="structure")
    ctx["top"] = 19.7
    mb = MB(); mb.cyl(0, 0, 0, 0, 1.2, "GlassBlue", seg=24, axis="y")
    mb.obj("RoseWindow", 0.0, y1 - 0.06, 4.6, kind="window") if False else None
reg(("stone_chapel", "海角石砌教堂", "Cape Stone Chapel", "Gothic Revival Chapel", "哥德復興教堂",
     "landmark", "chapel", ["realistic", "horror", "romance", "fantasy", "wedding"],
     "Stone nave with tall lancet windows, rows of pews and altar, steep slate gable, square bell tower with brass bell and spire."),
    dict(W=10, D=17, floors=1, h0=5.6, plinth=0.5, ext="Stone", int="Plaster", frame="Frame", win="win", sill=1.4, head=4.4, bay=2.6, ww=0.9,
         g_front=[("chapel", 1)], roof="gable_y", roof_m="SlateDark", pitch=50, over=0.4, gable_m="Stone", cap="SlateDark",
         door_k="door_double", door_m="WoodDark", door_w=1.8, door_x=0.0, door_h=3.0, side=5.0, plot_m="Grass", decor=["trees"]), _d2_chapel)

reg(("power_gym", "能量健身工廠", "PowerHouse Gym", "Industrial Fitness Hall", "工業風健身房",
     "standard", "gym", ["realistic", "sports", "slice-of-life", "anime"],
     "Steel-clad sawtooth hall full of treadmills and weight benches, glass front, neon sign."),
    dict(W=16, D=12, floors=1, h0=5.0, ext="PanelSteel", int="Concrete", frame="MetalDark", win="win3", ground="gym",
         g_front=[("gym", 1)], roof="sawtooth", roof_m="PanelDark", floor0="CarpetGrey", door_x=-5.0, door_w=1.6, door_k="door_glass",
         sign=("能量健身 POWER GYM", "Black", "NeonOrange", 6.0)))

def _d2_kinder(ctx):
    y1 = ctx["y1"]
    mb = MB()                                                    # slide
    mb.box(-0.4, 0.6, 0, 0.4, 1.4, 1.6, "PlasticYellow"); mb.quad([(-0.3, 0.6, 1.6), (0.3, 0.6, 1.6), (0.3, -1.6, 0.2), (-0.3, -1.6, 0.2)], "PlasticRed", 0.05)
    furn("Slide", mb, ctx["x1"] + 2.0, y1 - 3.5, 0, 0, "play")
    mb = MB()                                                    # swings
    for x in (-1.2, 1.2):
        mb.prism([(-0.8, 0), (0.8, 0), (0.05, 2.2), (-0.05, 2.2)], x - 0.05, x + 0.05, "PlasticBlue", plane="yz")
    mb.box(-1.25, -0.05, 2.15, 1.25, 0.05, 2.25, "PlasticBlue")
    for x in (-0.5, 0.5):
        mb.box(x - 0.2, -0.12, 0.45, x + 0.2, 0.12, 0.5, "PlasticRed"); mb.box(x - 0.01, -0.01, 0.5, x + 0.01, 0.01, 2.15, "Chrome")
    furn("Swings", mb, ctx["x2"] - 3.0, y1 - 3.5, 0, 0, "play")
    ob("Sandbox", [(-1.2 - 0.0, y1 - 5.5, 0.0, 1.2, y1 - 3.8, 0.25)], ["Sand"], kind="floor", walkable=True)
reg(("kindergarten", "彩虹幼兒園", "Rainbow Kindergarten", "Playful Kindergarten", "童趣幼兒園",
     "civic", "kindergarten", ["anime", "slice-of-life", "cozy", "horror", "cartoon"],
     "Single-storey cheerful kindergarten: classroom + play lounge, red tile gable, playground with slide, swings and sandbox."),
    dict(W=14, D=10, floors=1, h0=3.4, ext="Plaster", frame="PlasticBlue", win="win", ground="classroom",
         g_front=[("classroom", 1), ("lounge", 1)], roof="gable_y", roof_m="RoofTile", pitch=30, over=0.6, gable_m="Plaster",
         door_k="door", door_m="PlasticYellow", door_x=0.0, front=7.0, plot_m="Grass", decor=["plants"],
         sign=("彩虹幼兒園", "PlasticYellow", "PlasticRed", 3.4)), _d2_kinder)
