# District 1 — world residential styles (12). Exec'd into the shared namespace: keep names prefixed _d1_.

def _d1_paris(ctx):
    for i, x in enumerate((-5.0, -1.5, 2.0)):
        cafe_set(x, ctx["y1"] - 2.0, 0.0, 0, "Marble", "PlasticDark")
reg(("paris_haussmann", "巴黎奧斯曼公寓", "Parisian Haussmann Apartment", "Haussmann Parisian", "巴黎奧斯曼式",
     "upscale", "apartment", ["realistic", "romance", "anime", "noir", "europe"],
     "Cream stone 4-storey block: corner café with terrace, wrought-iron balconies, mansard slate roof with dormers, cornice."),
    dict(W=14, D=11, floors=4, h0=4.0, h=3.3, ext="BrickCream", ext0="Stone", frame="FrameWhite", win="win3", head=2.7, bay=3.2, ww=1.5,
         ground="cafe", g_front=[("cafe", 1)], g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("living", 2), ("dining", 1)],
         u_back=[("bedroom", 1.2), ("bath", 0.7)], balcony="front", balc_rail="bar", roof="mansard", roof_m="SlateBlue", mansard_h=2.6,
         decor=["bands", "cornice", "boxes", "chimney"], band_m="Stone", awning="AwningRed", sign=("Café de la Rue  街角咖啡", "Black", "LabelGlow"),
         front=4.5, door_x=-4.0), _d1_paris)

reg(("nyc_brownstone", "紐約褐石排屋", "Brooklyn Brownstone", "New York Brownstone", "紐約褐石屋",
     "upscale", "townhouse", ["realistic", "noir", "sitcom", "crime", "urban"],
     "Narrow 4-storey brownstone with raised stoop, double timber door, cornice, sash windows, flat roof with water tank."),
    dict(W=8, D=13, floors=4, h0=3.4, h=3.2, plinth=1.4, plinth_m="Stone", ext="Brick", frame="WoodDark", win="win", bay=2.4, ww=1.1, head=2.5,
         ground="living", g_front=[("living", 1)], g_back=[("kitchen", 1)], u_front=[("living", 1)], u_back=[("bedroom", 1)],
         door_k="door_double", door_m="WoodDark", door_w=1.4, door_x=-1.6, roof="flat", decor=["cornice", "bands", "tank", "walllamps"],
         band_m="Stone", front=4.5))

def _d1_london(ctx):
    for k, (a, b) in enumerate(((-3.6, -1.4),)):
        bay_window("Bay%d" % k, "S", a, b, 0.8 + 0.6, 0.6 + 2.5, ctx["y1"] - 0.03, 0.7, "FrameWhite", "SlateDark", base="Brick")
reg(("london_terrace", "倫敦紅磚聯排", "London Victorian Terrace", "Victorian Terrace", "維多利亞聯排屋",
     "standard", "townhouse", ["realistic", "detective", "europe", "steampunk", "horror"],
     "Red-brick 3-storey Victorian terrace: bay window, black front door with fanlight, slate gable roof, chimney stacks."),
    dict(W=9, D=11, floors=3, h0=3.3, h=3.0, plinth=0.6, ext="Brick", frame="FrameWhite", win="win", bay=2.4, ww=1.1, head=2.4,
         ground="living", g_front=[("living", 1)], g_back=[("kitchen", 1)], u_front=[("bedroom", 1)], u_back=[("bath", 1)],
         door_k="door", door_m="Black", door_x=1.2, roof="gable", roof_m="SlateDark", pitch=38, over=0.3, gable_m="Brick", cap="SlateDark",
         decor=["chimney", "bands", "walllamps"], band_m="Stone", s_ops0=[(-3.6, -1.4, 1.4, 3.1, "open")]), _d1_london)

def _d1_tudor(ctx):
    halftimber(ctx, ctx["Z"][1], ctx["Z"][2])
    sign_board("InnSign", "皇冠酒館", ctx["x1"] - 0.4, ctx["y1"] - 0.9, 3.0, 1.0, 0.7, 90, "WoodDark", "Brass", 0.22)
reg(("tudor_inn", "皇冠都鐸酒館", "The Crown Tudor Inn", "English Tudor", "英式都鐸",
     "standard", "pub + inn", ["medieval", "fantasy", "rpg-village", "realistic", "europe"],
     "Stone ground-floor pub with bar and booths, half-timbered upper floor of guest rooms, steep tile gable, lanterns, hanging sign."),
    dict(W=12, D=11, floors=2, h0=3.4, h=3.0, ext0="Stone", ext="Plaster", frame="WoodDark", win="win", bay=2.4, ww=1.0,
         ground="bar", g_front=[("bar", 1)], g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("hotel", 1), ("hotel", 1)], u_back=[("hotel", 1)],
         door_k="door_double", door_m="WoodDark", roof="gable", roof_m="RoofTile", pitch=48, over=0.4, gable_m="Plaster",
         decor=["chimney", "lanterns"], shop_k="win3", shop_frame="WoodDark"), _d1_tudor)

reg(("swiss_chalet", "阿爾卑斯木屋", "Alpine Swiss Chalet", "Swiss Alpine Chalet", "瑞士山屋",
     "upscale", "house", ["realistic", "cozy", "winter", "anime", "europe"],
     "Stone base + log upper storey, wide low gable with deep eaves, wrap balcony with flower boxes, red shutters."),
    dict(W=11, D=10, floors=2, h0=3.2, h=3.0, plinth=0.6, ext0="Stone", ext="WoodLight", int="WoodLight", frame="WoodDark", win="win",
         ground="living", g_front=[("living", 1.4), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1), ("bedroom", 1)], u_back=[("bath", 1)], balcony="front", balc_rail="wood", balc_floor="WoodLight",
         roof="gable", roof_m="WoodDark", pitch=24, over=1.3, gable_m="WoodLight", cap="WoodDark",
         decor=["shutters", "boxes", "chimney"], shutter_m="PaintRed", door_m="WoodDark", plot_m="Grass"))

def _d1_cabin(ctx):
    fireplace(ctx["x1"] + 0.55, 0.0, 0.0, 90, "Stone")
    for i in range(3):
        crate(ctx["x2"] + 0.8, -2.0 + i * 0.7, 0.0, 10 * i, 0.5, "WoodLight")
reg(("nordic_cabin", "北歐黑木小屋", "Nordic Black Cabin", "Scandinavian Cabin", "北歐小屋",
     "standard", "cabin", ["realistic", "survival", "horror", "cozy", "winter"],
     "Single-storey black-timber cabin with a steep slate gable, big picture window, fireplace, firewood stack."),
    dict(W=8, D=9, floors=1, h0=3.0, ext="WoodDark", int="WoodLight", frame="Black", win="win", ww=1.6,
         g_front=[("living", 1.3), ("bedroom", 1)], roof="gable_y", roof_m="SlateDark", pitch=50, over=0.4, gable_m="WoodDark", cap="SlateDark",
         door_m="WoodLight", door_k="door", decor=["walllamps"], plot_m="Grass"), _d1_cabin)

reg(("med_villa", "地中海白屋", "Mediterranean White House", "Mediterranean", "地中海風",
     "upscale", "house", ["realistic", "summer", "romance", "anime"],
     "Whitewashed 2-storey house with blue door and shutters, terracotta hip roof, balcony, bougainvillea boxes."),
    dict(W=12, D=10, floors=2, ext="Plaster", frame="FrameWhite", win="win", ground="living",
         g_front=[("living", 1.4), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("bedroom", 1), ("lounge", 1)],
         u_back=[("bedroom", 1), ("bath", 0.6)], balcony="alt", roof="hip", roof_m="RoofTile", pitch=22, over=0.5,
         decor=["shutters", "boxes", "plants"], shutter_m="PlasticBlue", door_m="PlasticBlue", door_k="door", plot_m="Grass"))

def _d1_hacienda(ctx):
    mb = MB()
    for i in range(6):
        x = ctx["x1"] + 1.2 + i * (ctx["W"] - 2.4) / 5
        mb.box(x - 0.25, ctx["y1"] - 2.4, 0, x + 0.25, ctx["y1"] - 1.9, 2.8, "Plaster")
    mb.box(ctx["x1"], ctx["y1"] - 2.5, 2.8, ctx["x2"], ctx["y1"], 3.1, "Plaster")
    mb.obj("Arcade", kind="structure")
    ob("Veranda", [(ctx["x1"], ctx["y1"] - 2.5, 0.0, ctx["x2"], ctx["y1"], 0.05)], ["Terracotta"], kind="floor", walkable=True)
    gable_roof("VerandaRoof", ctx["x1"], ctx["y1"] - 2.5, ctx["x2"], ctx["y1"], 3.1, 12, 0.2, "RoofTile", "WoodDark", along="x", cap=None)
    for i in range(3):
        plant(ctx["x1"] + 2 + i * 5, ctx["y1"] - 3.2, 0, 0, 1.2, "Terracotta", "palm")
reg(("spanish_hacienda", "西班牙莊園", "Spanish Hacienda", "Spanish Colonial", "西班牙殖民風",
     "upscale", "house", ["western", "realistic", "telenovela", "rpg-village"],
     "Long single-storey stucco ranch house with arched veranda, terracotta roof, living/dining/kitchen/bedrooms."),
    dict(W=16, D=11, floors=1, h0=3.4, ext="Plaster", frame="WoodDark", win="win", g_front=[("living", 1.2), ("dining", 1), ("kitchen", 0.8), ("bedroom", 1)],
         roof="hip", roof_m="RoofTile", pitch=18, over=0.6, door_m="WoodDark", door_k="door_double", door_w=1.6, front=5.5, plot_m="Sand",
         decor=["walllamps"]), _d1_hacienda)

def _d1_riad(ctx):
    zr = ctx["roof_z"]
    for i in range(4):
        lamp("RiadLantern%d" % i, ctx["x1"] + 1.5 + i * 3, ctx["y1"] - 0.5, 2.8, 25, (1.0, 0.6, 0.3), kind="lantern", glow="Lantern")
    mb = MB(); x = ctx.get("door_x", -2.0)
    mb.prism([(-1.0, 0), (1.0, 0), (1.0, 3.2), (0.6, 3.6), (0.0, 3.8), (-0.6, 3.6), (-1.0, 3.2)], ctx["y1"] - 0.12, ctx["y1"] - 0.04, "MosaicBeige", plane="xz")
    o = mb.obj("ArchFrame", -2.0, 0, 0, kind="trim")
reg(("moroccan_riad", "摩洛哥庭園宅", "Moroccan Riad House", "Moroccan Riad", "摩洛哥風",
     "upscale", "guesthouse", ["fantasy", "desert", "realistic", "adventure"],
     "Ochre 2-storey riad: carved arch door, mashrabiya grilles, tiled lounge, guest rooms, roof terrace with lanterns."),
    dict(W=12, D=12, floors=2, ext="BrickCream", int="Plaster", frame="Brass", win="grille", ground="lounge",
         g_front=[("lounge", 1.4), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("hotel", 1), ("hotel", 1)],
         u_back=[("hotel", 1), ("bath", 0.6)], floor0="TileBlue", roof="terrace", parapet=1.2, umbrella="AwningRed",
         door_k="door_double", door_m="WoodDark", door_w=1.6, door_x=-2.0, decor=["plants"], plot_m="Sand"), _d1_riad)

def _d1_machiya(ctx):
    for i, x in enumerate((-2.6, 1.6)):
        lamp("Chochin%d" % i, x, ctx["y1"] - 0.5, 2.7, 25, (1.0, 0.5, 0.2), kind="lantern", glow="Lantern")
    mb = MB()
    for i in range(10):
        mb.box(-0.55 + i * 0.11, -0.01, 0, -0.5 + i * 0.11, 0.01, 0.9, "FabricNavy" if i % 2 else "FabricWhite")
    mb.obj("Noren", -1.0, ctx["y1"] - 0.08, 1.5, kind="trim")
reg(("kyoto_machiya", "京都町家", "Kyoto Machiya Townhouse", "Japanese Machiya", "日式町家",
     "standard", "shop + house", ["anime", "realistic", "slice-of-life", "japan", "cozy"],
     "Narrow timber townhouse: G/F sweets shop with noren curtain and lanterns, tatami living above, sliding lattice windows, slate gable."),
    dict(W=8, D=12, floors=2, h0=3.0, h=2.8, ext0="WoodDark", ext="Plaster", frame="WoodDark", win="slide", ww=1.6,
         ground="shop", g_front=[("shop", 1)], g_back=[("kitchen", 1)], u_front=[("living", 1)], u_back=[("bedroom", 1)], floor="Tatami",
         roof="gable", roof_m="SlateDark", pitch=26, over=0.6, gable_m="Plaster", cap="SlateDark", door_x=-1.0, door_k="door_glass",
         sign=("和菓子 甘味処", "WoodDark", "LabelGlow", 3.0), shop_frame="WoodDark"), _d1_machiya)

def _d1_hanok(ctx):
    ob("Maru", [(ctx["x1"], ctx["y1"] - 1.4, 0.0, ctx["x2"], ctx["y1"], 0.6)], ["WoodLight"], kind="floor", walkable=True)
    mb = MB()
    for i in range(6):
        x = ctx["x1"] + 0.3 + i * (ctx["W"] - 0.6) / 5
        mb.cyl(x, ctx["y1"] - 1.25, 0.6, 3.6, 0.12, "WoodDark", seg=12)
    mb.obj("Posts", kind="structure")
reg(("korean_hanok", "韓式韓屋", "Korean Hanok", "Korean Hanok", "韓屋",
     "upscale", "house", ["historical", "kdrama", "realistic", "anime"],
     "Single-storey hanok on a stone plinth: timber posts, raised wooden maru veranda, paper sliding doors, curved tiled hip roof."),
    dict(W=14, D=9, floors=1, h0=3.0, plinth=0.6, plinth_m="Stone", ext="Plaster", frame="WoodDark", win="slide", ww=1.6,
         g_front=[("living", 1), ("bedroom", 1), ("kitchen", 0.8)], roof="hip", roof_m="SlateDark", pitch=28, over=1.6, curl=0.5,
         ornaments=True, door_k="door", door_m="WoodLight", front=5.0, plot_m="Grass", decor=["trees"]), _d1_hanok)

reg(("hk_tonglau", "旺角唐樓", "Hong Kong Tong Lau", "Hong Kong Tenement", "香港唐樓",
     "budget", "tenement", ["cyberpunk", "noir", "realistic", "action", "hk-cinema"],
     "6-storey mosaic tenement: cha chaan teng diner, caged balconies, AC units, neon blade sign, laundry, rooftop."),
    dict(W=8, D=12, floors=6, h0=3.6, h=3.0, ext="MosaicBeige", ext0="TileWhite", win="grille", bay=2.2, ww=1.0,
         ground="restaurant", g_front=[("restaurant", 1)], g_back=[("kitchen", 1)], u_front=[("living", 1)], u_back=[("bedroom", 1)],
         balcony="alt", balc_rail="bar", roof="terrace", decor=["ac", "pipes", "antenna"], sign=("茶餐廳 冰室", "PlasticYellow", "PlasticRed", 3.4),
         blade=("旺角大廈", "NeonRed"), door_x=-2.0))
