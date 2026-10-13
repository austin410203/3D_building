# District 6 — Asia (25). Names prefixed _d6_.

def _d6_meta(i, zh, en, st, stz, tier, cat, gs, desc):
    return (i, zh, en, st, stz, tier, cat, gs, desc)

def _d6_lions(ctx, dx=2.2):
    for sx in (-1, 1):
        mb = MB(); mb.box(-0.4, -0.4, 0, 0.4, 0.4, 0.8, "Stone"); mb.sph(0, 0, 1.15, 0.38, "Stone", sy=0.9, sz=1.1); mb.sph(0, -0.3, 1.5, 0.25, "Stone")
        furn("StoneLion", mb, sx * dx, ctx["y1"] - 1.4, ctx["Z"][0] - (ctx["Z"][0]), 0)

def _d6_lanterns(ctx, n=4, z=None):
    z = z or ctx["Z"][0] + 2.8
    for i in range(n):
        x = ctx["x1"] + 0.8 + i * (ctx["W"] - 1.6) / max(1, n - 1)
        lamp("RedLantern%d" % i, x, ctx["y1"] - 0.6, z, 20, (1.0, 0.35, 0.15), kind="lantern", glow="Lantern")

reg(_d6_meta("tw_townhouse", "台式透天厝", "Taiwanese Townhouse", "Taiwanese Townhouse", "台式透天厝", "standard", "house",
              ["realistic", "slice-of-life", "taiwan", "horror"], "Narrow 4-storey mosaic townhouse: G/F garage with roller door, family floors above, roof terrace with water tank."),
    dict(W=6.4, D=14, floors=4, ext="MosaicBeige", win="grille", ww=1.2, g_front=[("garage", 1)], g_back=[("kitchen", 1)],
         u_front=[("living", 1)], u_back=[("bedroom", 1)], s_ops0=[(-2.9, 0.6, 0, 2.6, "roller")], door_x=1.6, door_w=0.9, door_k="door_metal",
         balcony="alt", roof="terrace", decor=["ac", "tank", "pipes"], side=1.8))

def _d6_sanhe(ctx):
    y1 = ctx["y1"]
    for sx in (-1, 1):
        xa, xb = sorted((sx * (ctx["W"] / 2 - 3.6), sx * ctx["W"] / 2))
        def wing(xa=xa, xb=xb):
            ring("Wing%d" % sx, xa, y1 - 7.0, xb, y1 - 0.02, 0.0, 3.0, "Brick", "PlasterInt", 0.2, 0.03,
                 {"E" if sx < 0 else "W": [(y1 - 5.0, y1 - 4.0, 0, 2.1, "door", "PaintRed"), (y1 - 2.8, y1 - 1.4, 0.9, 2.1, "win", "WoodDark")]})
            slab("WingFloor%d" % sx, xa + 0.2, y1 - 6.8, xb - 0.2, y1 - 0.2, 0.0, 0.15, top="StoneTile", under="Concrete")
            gable_roof("WingRoof%d" % sx, xa, y1 - 7.0, xb, y1, 3.0, 28, 0.4, "RoofTile", "WoodDark", along="y", gable_m="Brick", cap="RoofRed")
            fillroom("bedroom", xa + 0.27, y1 - 6.8, xb - 0.27, y1 - 0.25, 0.0, 2.8, "E" if sx < 0 else "W")
        wing()
    ob("Courtyard", [(ctx["x1"] + 3.6, y1 - 7.0, 0.0, ctx["x2"] - 3.6, y1, 0.04)], ["Cobble"], kind="floor", walkable=True)
reg(_d6_meta("minnan_sanheyuan", "閩南三合院", "Minnan Courtyard House", "Minnan Sanheyuan", "閩南三合院", "upscale", "house",
             ["historical", "taiwan", "wuxia", "rpg-village", "realistic"], "Red-brick U-shaped courtyard house: ancestral hall in the centre, bedrooms in two wings, curled tile roofs, cobbled courtyard."),
    dict(W=20, D=8, floors=1, h0=3.4, ext="Brick", frame="WoodDark", win="win", g_front=[("bedroom", 1), ("chapel", 1.4), ("kitchen", 1)],
         roof="hip", roof_m="RoofTile", pitch=26, over=0.6, curl=0.35, ornaments=True, door_k="door_double", door_m="PaintRed", door_w=1.6,
         door_x=0.0, front=9.5, side=1.5, plot_m="StoneTile"), _d6_sanhe)

reg(_d6_meta("jp_family_house", "日式獨棟住宅", "Japanese Family House", "Contemporary Japanese House", "日式住宅", "standard", "house",
             ["anime", "slice-of-life", "japan", "realistic"], "Classic 2-storey Japanese suburban house: white siding, sliding windows, slate hip roof, small balcony, AC units."),
    dict(W=10, D=9.5, floors=2, ext="SidingWhite", frame="FrameAlu", win="slide", g_front=[("living", 1.4), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.7)],
         u_front=[("bedroom", 1), ("bedroom", 1)], u_back=[("studio", 1), ("bath", 0.6)], balcony="front", roof="hip", roof_m="SlateDark", pitch=24,
         over=0.6, door_k="door", door_m="WoodDark", decor=["ac", "plants"], plot_m="Grass"))

reg(_d6_meta("jp_ryokan", "月見溫泉旅館", "Tsukimi Hot-Spring Ryokan", "Japanese Ryokan", "溫泉旅館", "upscale", "ryokan",
             ["anime", "japan", "cozy", "romance", "realistic"], "2-storey ryokan: lobby and indoor hot-spring bath, tatami guest rooms upstairs, lanterns, curled slate roof."),
    dict(W=16, D=12, floors=2, ext0="WoodDark", ext="Plaster", frame="WoodDark", win="slide", ground="lobby", g_front=[("lobby", 1), ("onsen", 1)],
         g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("hotel", 1)] * 3, u_back=[("hotel", 1), ("bath", 0.6)], floor="Tatami",
         roof="hip", roof_m="SlateDark", pitch=26, over=0.8, curl=0.25, door_k="door_double", door_m="WoodLight", door_x=-4.0,
         sign=("湯の宿  月見", "WoodDark", "LabelGlow", 4.0), decor=["lanterns"], plot_m="Cobble"), lambda c: _d6_lanterns(c, 5))

reg(_d6_meta("manga_netcafe", "漫畫網咖", "Manga & Net Café", "Japanese Manga Café", "漫畫網咖", "budget", "net café",
             ["anime", "japan", "cyberpunk", "slice-of-life"], "3-storey manga café: G/F manga library, PC booth floors above, neon sign."),
    dict(W=9, D=11, floors=3, ext="PanelDark", ext0="TileWhite", frame="MetalDark", ground="library", g_front=[("library", 1)], g_back=[("bath", 1)],
         u_front=[("office", 1)], u_back=[("lounge", 1)], floor="CarpetGrey", door_x=-2.0, blade=("漫畫網咖", "NeonYellow"),
         sign=("MANGA CAFE 24H", "Black", "NeonCyan", 4.6), decor=["ac"]))

reg(_d6_meta("kr_mart_gosiwon", "首爾便利店考試院", "Seoul Mart & Gosiwon", "Korean Mixed-use Walk-up", "韓式住商", "budget", "shop + dorm",
             ["kdrama", "slice-of-life", "realistic", "horror"], "4-storey cream brick: 24h convenience store, tiny gosiwon study rooms above, rooftop."),
    dict(W=9, D=11, floors=4, ext="BrickCream", win="win", ground="market", g_front=[("market", 1)], g_back=[("storage", 1)],
         u_front=[("hotel", 1), ("hotel", 1)], u_back=[("hotel", 1)], door_x=-2.0, roof="terrace", decor=["ac", "pipes"],
         sign=("24 편의점 MART", "PlasticBlue", "White", 4.6)))

reg(_d6_meta("hk_dimsum_hall", "金龍酒家", "Golden Dragon Dim Sum Hall", "Hong Kong Teahouse", "港式茶樓", "standard", "restaurant",
             ["hk-cinema", "action", "realistic", "noir"], "3-storey tiled teahouse: banquet dining halls on every floor, kitchen, red/gold signage, lanterns."),
    dict(W=14, D=12, floors=3, ext="TileWhite", frame="Brass", win="win3", ground="restaurant", g_front=[("restaurant", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("restaurant", 1)], u_back=[("kitchen", 1), ("bath", 0.6)], floor="CarpetRed", door_x=-3.0, door_w=1.6,
         sign=("金龍酒家  DIM SUM", "PaintRed", "NeonYellow", 6.0), blade=("金龍酒家", "NeonRed")), lambda c: _d6_lanterns(c, 6))

reg(_d6_meta("sg_shophouse", "南洋店屋", "Straits Shophouse", "Peranakan Shophouse", "南洋店屋", "standard", "shophouse",
             ["realistic", "southeast-asia", "slice-of-life", "historical"], "3-storey pastel Peranakan shophouse: five-foot-way arcade, louvred shutters, tile gable, shop below, family above."),
    dict(W=7, D=14, floors=3, ext="PaintTeal", frame="FrameWhite", win="win", ww=1.1, ground="shop", g_front=[("shop", 1)], g_back=[("kitchen", 1)],
         u_front=[("living", 1)], u_back=[("bedroom", 1)], roof="gable_y", roof_m="RoofTile", pitch=30, over=0.4, gable_m="PaintTeal",
         decor=["shutters", "bands"], shutter_m="WoodLight", band_m="White", door_x=-1.5, front=3.5,
         sign=("南洋雜貨  KEDAI", "WoodDark", "LabelGlow", 4.0)))

reg(_d6_meta("vn_tube_house", "河內管狀屋", "Hanoi Tube House", "Vietnamese Tube House", "越南管狀屋", "budget", "house + café",
             ["realistic", "southeast-asia", "slice-of-life"], "5-storey 5.6 m-wide tube house: ground-floor cà phê, one room per floor, plant balconies, roof terrace."),
    dict(W=5.8, D=16, floors=5, h0=3.4, h=3.0, ext="MosaicPink", win="win", ww=1.1, ground="cafe", g_front=[("cafe", 1)], g_back=[("kitchen", 1)],
         u_front=[("living", 1)], u_back=[("bedroom", 1)], balcony="alt", roof="terrace", door_x=-1.4, door_w=0.9, side=1.6,
         decor=["ac", "pipes"], sign=("Cà Phê", "PlasticYellow", "PaintRed", 2.8)))

reg(_d6_meta("thai_stilt_house", "泰式高腳屋", "Thai Stilt House", "Thai Teak Stilt House", "泰式高腳屋", "standard", "house",
             ["southeast-asia", "realistic", "adventure", "cozy"], "Teak house raised 2 m on a plinth with front stair and porch, steep tile gable, open-plan living + bedroom."),
    dict(W=10, D=8, floors=1, h0=3.2, plinth=2.0, plinth_m="WoodDark", ext="WoodDark", int="WoodLight", frame="WoodLight", win="win",
         g_front=[("living", 1), ("bedroom", 1)], roof="gable_y", roof_m="RoofTile", pitch=40, over=0.7, gable_m="WoodDark", porch=True,
         porch_w=4.0, porch_d=2.0, porch_col="WoodDark", door_x=0.0, front=6.5, plot_m="Grass", decor=["plants"]))

reg(_d6_meta("bali_villa", "峇里島茅頂別墅", "Bali Thatch Villa", "Balinese Villa", "峇里島villa", "luxury", "villa",
             ["resort", "realistic", "romance", "tropical"], "Single-storey stone villa with a steep thatch hip roof and deep eaves, living / bedroom / outdoor-feel spa bath, palms."),
    dict(W=14, D=10, floors=1, h0=3.2, plinth=0.4, ext="Stone", frame="WoodDark", win="shop", ww=2.4, g_front=[("living", 1), ("bedroom", 1), ("onsen", 0.8)],
         roof="hip", roof_m="Bark", pitch=38, over=1.6, door_k="door_double", door_m="WoodDark", door_x=-1.5, plot_m="Grass", decor=["trees", "lanterns"]),
    lambda c: [tree(c["x1"] - 1.5, c["y1"] - 2.0, 0, 1.0, "palm", seed=611), tree(c["x2"] + 1.5, c["y1"] - 2.0, 0, 1.1, "palm", seed=612)])

def _d6_haveli(ctx):
    zr = ctx["roof_z"]
    for (x, y) in ((ctx["x1"] + 1.2, ctx["y1"] + 1.2), (ctx["x2"] - 1.2, ctx["y1"] + 1.2)):
        mb = MB()
        for (dx, dy) in ((-0.8, -0.8), (0.8, -0.8), (-0.8, 0.8), (0.8, 0.8)):
            mb.cyl(x + dx, y + dy, zr, zr + 2.0, 0.08, "BrickCream", seg=8)
        mb.box(x - 1.05, y - 1.05, zr + 2.0, x + 1.05, y + 1.05, zr + 2.2, "BrickCream")
        mb.obj("Chhatri_%d" % int(x), kind="structure"); dome("ChhatriDome_%d" % int(x), x, y, zr + 2.2, 1.0, "BrickCream", 0.9)
    ctx["top"] = zr + 3.3
reg(_d6_meta("rajasthan_haveli", "拉賈斯坦哈維利", "Rajasthani Haveli", "Indian Haveli", "印度哈維利", "upscale", "mansion",
             ["historical", "fantasy", "adventure", "realistic"], "3-storey sandstone haveli: carved jharokha screens, courtyard-style rooms, roof terrace with domed chhatri pavilions."),
    dict(W=12, D=12, floors=3, ext="BrickCream", frame="Brass", win="grille", g_front=[("lounge", 1), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1), ("lounge", 1)], u_back=[("bedroom", 1), ("bath", 0.6)], floor0="MarbleBlack", roof="terrace", parapet=1.0,
         door_k="door_double", door_m="WoodDark", door_w=1.6, door_x=-2.0, decor=["bands"], band_m="Stone", plot_m="Sand"), _d6_haveli)

reg(_d6_meta("shanghai_shikumen", "上海石庫門", "Shanghai Shikumen", "Shikumen Lane House", "石庫門", "standard", "townhouse",
             ["historical", "noir", "1930s", "realistic"], "3-storey grey-brick shikumen with a carved stone door frame, black double doors, slate gable, lane-house plan."),
    dict(W=8, D=13, floors=3, ext="BrickDark", frame="WoodDark", win="win", ww=1.1, g_front=[("living", 1)], g_back=[("kitchen", 1)],
         u_front=[("bedroom", 1)], u_back=[("studio", 1)], roof="gable", roof_m="SlateDark", pitch=30, over=0.3, gable_m="BrickDark", cap="SlateDark",
         door_k="door_double", door_m="Black", door_w=1.4, door_x=-1.4, decor=["bands"], band_m="Stone"),
    lambda c: ob("StoneFrame", [(-2.4, c["y1"] - 0.15, 0, -2.2, c["y1"], 2.9), (-0.6, c["y1"] - 0.15, 0, -0.4, c["y1"], 2.9),
                                (-2.6, c["y1"] - 0.2, 2.9, -0.2, c["y1"], 3.4)], ["Stone"], kind="trim"))

reg(_d6_meta("beijing_siheyuan_gate", "北京四合院門樓", "Beijing Siheyuan Gatehouse", "Beijing Siheyuan", "北京四合院", "upscale", "house",
             ["historical", "wuxia", "realistic", "kdrama"], "Grey-brick courtyard house front range: red lacquered gate, lanterns, stone lions, slate gable, living rooms behind."),
    dict(W=14, D=9, floors=1, h0=3.4, plinth=0.5, ext="BrickDark", frame="PaintRed", win="win3", g_front=[("living", 1), ("chapel", 0.8), ("bedroom", 1)],
         roof="gable", roof_m="SlateDark", pitch=30, over=0.6, gable_m="BrickDark", cap="SlateDark", door_k="door_double", door_m="PaintRed",
         door_w=1.6, door_x=0.0, front=5.0), lambda c: (_d6_lanterns(c, 2), _d6_lions(c, 2.0)))

def _d6_temple(ctx):
    y1 = ctx["y1"]
    mb = MB()
    for sx in (-1.4, 1.4):
        mb.cyl(sx, y1 - 0.8, ctx["Z"][0], ctx["Z"][0] + 3.2, 0.22, "Stone", seg=16)
        for k in range(10):
            a = k * 0.9
            mb.sph(sx + math.cos(a) * 0.24, y1 - 0.8 + math.sin(a) * 0.24, ctx["Z"][0] + 0.3 + k * 0.3, 0.09, "PlasticGreen")
    mb.obj("DragonColumns", kind="structure")
    mb = MB(); mb.cyl(0, 0, 0, 0.9, 0.6, "Brass", seg=16, r2=0.75); mb.cyl(0, 0, 0.9, 1.0, 0.8, "Brass", seg=16)
    furn("IncenseBurner", mb, 0.0, y1 - 4.0, 0, 0, "use")
reg(_d6_meta("tw_folk_temple", "福德宮", "Fude Folk Temple", "Taiwanese Folk Temple", "台灣廟宇", "landmark", "temple",
             ["taiwan", "wuxia", "fantasy", "horror", "realistic"], "Red temple hall on a stone plinth: dragon-wrapped columns, swallow-tail curled roof with ornaments, altar inside, incense burner."),
    dict(W=12, D=12, floors=1, h0=4.4, plinth=0.6, ext="PaintRed", int="PaintRed", frame="Brass", win="grille", g_front=[("chapel", 1)],
         roof="hip", roof_m="RoofTile", pitch=30, over=1.0, curl=0.9, ornaments=True, door_k="door_double", door_m="PaintRed", door_w=2.0,
         door_x=0.0, front=7.0, plot_m="StoneTile"), lambda c: (_d6_temple(c), _d6_lanterns(c, 4, 3.6)))

def _d6_market(ctx):
    y1 = ctx["y1"]
    for i in range(5):
        x = ctx["x1"] + 1.5 + i * (ctx["W"] - 3) / 4
        mb = MB(); mb.box(-0.9, -0.5, 0, 0.9, 0.5, 0.9, "Metal"); mb.box(-0.95, -0.55, 0.9, 0.95, 0.55, 0.95, "Chrome")
        for (dx, dy) in ((-0.85, -0.45), (0.85, -0.45), (-0.85, 0.45), (0.85, 0.45)):
            mb.box(dx - 0.02, dy - 0.02, 0.95, dx + 0.02, dy + 0.02, 2.3, "MetalDark")
        mb.box(-1.0, -0.6, 2.3, 1.0, 0.6, 2.35, ["AwningRed", "AwningGreen", "PlasticYellow", "AwningRed", "PlasticBlue"][i])
        furn("Stall", mb, x, y1 - 2.2, 0, 0, "shop")
        sign_board("StallSign%d" % i, ["鹽酥雞", "蚵仔煎", "臭豆腐", "大腸包小腸", "芒果冰"][i], x, y1 - 2.8, 2.6, 1.8, 0.35, 0, "Black", "NeonYellow", 0.22)
        lamp("StallL%d" % i, x, y1 - 2.2, 2.2, 25, (1.0, 0.8, 0.5), kind="point", fixture=False)
reg(_d6_meta("night_market_row", "夜市攤商街屋", "Night Market Row", "Taiwanese Night Market", "台灣夜市", "budget", "market",
             ["taiwan", "slice-of-life", "anime", "realistic"], "Tin-roofed open-front food hall with tables, five neon food stalls on the street, lanterns."),
    dict(W=16, D=9, floors=1, h0=3.8, ext="TinRust", int="TileWhite", ground="restaurant", g_front=[("restaurant", 1)],
         s_ops0=[(-7.6, 7.6, 0, 3.2, "open")], door_k="none", roof="shed", roof_m="TinRust", pitch=6, over=0.6, front=5.5,
         sign=("夜市美食街", "PaintRed", "NeonYellow", 6.0), sign_x=0.0), _d6_market)

reg(_d6_meta("bubble_tea_flats", "珍珠奶茶公寓", "Boba Tea Walk-up", "Taiwanese Shop Walk-up", "台式店面", "budget", "shop + flats",
             ["taiwan", "slice-of-life", "anime"], "3-storey white-tiled walk-up with a bubble-tea counter shop and flats above."),
    dict(W=7, D=10, floors=3, ext="TileWhite", win="grille", ww=1.1, ground="cafe", g_front=[("cafe", 1)], g_back=[("storage", 1)],
         u_front=[("living", 1)], u_back=[("bedroom", 1)], door_x=-1.4, awning="AwningGreen", decor=["ac"],
         sign=("珍珠奶茶  BOBA", "PlasticGreen", "White", 3.4)))

reg(_d6_meta("bento_shop", "池上便當店", "Railway Bento Shop", "Taiwanese Bento Shop", "便當店", "budget", "restaurant",
             ["taiwan", "slice-of-life", "anime"], "2-storey mosaic shop: bento counter with dining tables, kitchen behind, owner's flat upstairs."),
    dict(W=8, D=10, floors=2, ext="MosaicBeige", win="grille", ground="restaurant", g_front=[("restaurant", 1)], g_back=[("kitchen", 1)],
         u_front=[("living", 1)], u_back=[("bedroom", 1)], door_x=-1.8, awning="AwningRed", decor=["ac"],
         sign=("池上便當", "PlasticYellow", "PaintRed", 3.6)))

reg(_d6_meta("corner_pharmacy", "健康藥局", "Health Pharmacy", "Asian Neighbourhood Pharmacy", "社區藥局", "standard", "pharmacy",
             ["slice-of-life", "realistic", "zombie"], "3-storey white-tile pharmacy with shelves and counter, green cross sign, flats above."),
    dict(W=8, D=10, floors=3, ext="TileWhite", win="win", ground="shop", g_front=[("shop", 1)], g_back=[("storage", 1)],
         u_front=[("living", 1)], u_back=[("bedroom", 1)], door_x=-1.8, sign=("健康藥局  PHARMACY", "White", "PlasticGreen", 4.0)),
    lambda c: ob("GreenCross", [(c["x2"] - 1.2, c["y1"] - 0.12, 4.2, c["x2"] - 0.4, c["y1"] - 0.06, 4.4), (c["x2"] - 0.9, c["y1"] - 0.12, 3.9, c["x2"] - 0.7, c["y1"] - 0.06, 4.7)],
                 ["NeonGreen"], kind="sign"))

reg(_d6_meta("electronics_shop", "光華電器行", "Guanghua Electronics", "Asian Electronics Store", "電器行", "budget", "shop",
             ["cyberpunk", "slice-of-life", "anime", "realistic"], "3-storey pink-tile electronics store: TV walls and gadget shelves, neon sign, storeroom and flat above."),
    dict(W=9, D=11, floors=3, ext="MosaicPink", win="grille", ground="shop", g_front=[("shop", 1)], g_back=[("server", 1)],
         u_front=[("storage", 1)], u_back=[("bedroom", 1)], door_x=-2.2, blade=("電器行", "NeonBlue"), decor=["ac"],
         sign=("光華電器  ELECTRONICS", "Black", "NeonCyan", 4.6)),
    lambda c: [tv(c["x1"] + 1.0 + i * 1.5, c["y1"] + 0.6, 0.2, 180, 1.2, cab=False) for i in range(3)])

reg(_d6_meta("jp_tea_room", "侘寂茶室", "Wabi Tea Room", "Japanese Tea House", "日式茶室", "upscale", "tea house",
             ["japan", "zen", "anime", "realistic"], "Tiny single-storey tea room: tatami, low table, slate hip roof, stepping-stone garden with bamboo fence."),
    dict(W=7, D=7, floors=1, h0=2.8, plinth=0.4, ext="Plaster", int="Plaster", frame="WoodDark", win="slide", g_front=[("lounge", 1)],
         floor0="Tatami", roof="hip", roof_m="SlateDark", pitch=28, over=0.9, curl=0.2, door_k="door", door_m="WoodLight", door_x=0.0,
         front=6.0, plot_m="Grass"),
    lambda c: ob("SteppingStones", [(-0.35, c["y1"] - 1.0 - i * 0.9, 0.0, 0.35, c["y1"] - 0.4 - i * 0.9, 0.06) for i in range(5)], ["Stone"], kind="floor", walkable=True))

reg(_d6_meta("hanok_cafe", "韓屋咖啡廳", "Hanok Café", "Korean Hanok Café", "韓屋咖啡", "upscale", "café",
             ["kdrama", "cozy", "realistic", "anime"], "Single-storey hanok converted to a café: curved tile roof, timber posts, café tables inside."),
    dict(W=12, D=8, floors=1, h0=3.0, plinth=0.5, ext="Plaster", frame="WoodDark", win="slide", g_front=[("cafe", 1)], roof="hip", roof_m="SlateDark",
         pitch=28, over=1.4, curl=0.45, ornaments=True, door_k="door", door_m="WoodLight", door_x=0.0, front=4.5, plot_m="Cobble",
         sign=("韓屋카페", "WoodDark", "LabelGlow", 2.6)))

reg(_d6_meta("pachinko_parlor", "幸運小鋼珠", "Lucky 777 Pachinko", "Japanese Pachinko Parlor", "小鋼珠店", "standard", "game parlor",
             ["japan", "cyberpunk", "anime", "crime"], "2-storey black parlor: rows of machines (arcade cabinets), bar upstairs, giant neon 777 sign."),
    dict(W=14, D=12, floors=2, h0=4.0, ext="PanelDark", int="PanelDark", ground="arcade", g_front=[("arcade", 1)], g_back=[("storage", 1), ("bath", 0.6)],
         u_front=[("arcade", 1), ("bar", 1)], u_back=[("lounge", 1)], floor0="CarpetRed", door_x=-3.0, door_w=1.8,
         sign=("PACHINKO 777", "Black", "NeonPink", 7.0), blade=("パチンコ", "NeonYellow")))

reg(_d6_meta("brick_heritage_cafe", "紅磚老宅咖啡", "Red-Brick Heritage Café", "Taiwanese Heritage House", "老宅咖啡", "standard", "café",
             ["taiwan", "cozy", "slice-of-life", "realistic"], "Restored 1930s red-brick house: café downstairs, gallery loft upstairs, arched windows, potted plants."),
    dict(W=9, D=11, floors=2, ext="Brick", frame="WoodDark", win="win", g_front=[("cafe", 1)], g_back=[("kitchen", 1)],
         u_front=[("studio", 1)], u_back=[("library", 1)], door_x=-2.0, roof="flat", decor=["bands", "cornice", "plants"], band_m="Stone",
         sign=("老宅咖啡  1932", "WoodDark", "LabelGlow", 3.6)))

reg(_d6_meta("backpacker_hostel", "背包客棧", "Backpackers' Hostel", "Asian Backpacker Hostel", "背包客棧", "budget", "hostel",
             ["slice-of-life", "anime", "realistic", "adventure"], "5-storey hostel: lobby + bar, dorm floors with bunks, private rooms, roof terrace."),
    dict(W=10, D=11, floors=5, ext="Plaster", ext0="Brick", win="win", ground="lobby", g_front=[("lobby", 1), ("bar", 1)], g_back=[("bath", 1)],
         u_front=[("dorm", 1)], u_back=[("hotel", 1)], door_x=-2.4, roof="terrace", decor=["ac", "bands"], band_m="PaintTeal",
         sign=("BACKPACKERS 客棧", "PaintTeal", "White", 5.0)))
