# District 3 — shops, food & hospitality (12). Names prefixed _d3_.

def _d3_cart(x, y, rot=0):
    mb = MB()
    mb.box(-0.3, -0.45, 0.4, 0.3, 0.45, 0.42, "Chrome")
    for sx in (-0.3, 0.28):
        mb.box(sx, -0.45, 0.4, sx + 0.02, 0.45, 0.95, "Chrome")
    for sy in (-0.45, 0.43):
        mb.box(-0.3, sy, 0.4, 0.3, sy + 0.02, 0.95, "Chrome")
    mb.box(-0.3, 0.45, 1.0, 0.3, 0.55, 1.03, "PlasticRed")
    for sx in (-0.25, 0.25):
        for sy in (-0.4, 0.4):
            mb.cyl(sx, sy, 0, 0.1, 0.05, "Rubber", seg=8)
    return furn("Cart", mb, x, y, 0, rot, "use")

def _d3_market(ctx):
    y1 = ctx["y1"]
    for i in range(5):
        _d3_cart(ctx["x2"] - 1.2 - i * 0.25, y1 - 1.2, 0)
    mk = [(-11 + i * 3.0, y1 - 9.5, 0.0, -10.9 + i * 3.0, y1 - 4.5, 0.012) for i in range(8)]
    ob("ParkingLines", mk, ["White"], kind="trim")
    for i, x in enumerate((-9.5, -3.5, 2.5)):
        car(x, y1 - 7.0, 0, 0, ["PlasticRed", "White", "PlasticBlue"][i])
reg(("supermarket", "好鄰居超市", "Good Neighbor Supermarket", "Suburban Supermarket", "郊區超市",
     "standard", "supermarket", ["realistic", "survival", "zombie", "slice-of-life", "sims"],
     "Large steel-clad supermarket: aisles of double shelves, wall of drink fridges, checkout counters, carts, front parking."),
    dict(W=24, D=18, floors=1, h0=4.6, ext="PanelSteel", int="White", frame="FrameAlu", ground="market", g_front=[("market", 1)],
         door_x=-6.0, door_w=2.0, door_k="door_glass", roof="flat", parapet=1.2, parapet_m="PanelDark", front=11.0,
         sign=("好鄰居超市  SUPERMARKET", "White", "PlasticGreen", 9.0), sign_x=0.0, plot_m="Asphalt"), _d3_market)

def _d3_diner(ctx):
    zr = ctx["roof_z"]
    sign_board("RoofSign", "DINER  24H", 0.0, ctx["y1"] + 1.0, zr + 1.6, 6.0, 1.4, 0, "Black", "NeonRed", 0.9, frame="NeonCyan")
    mb = MB(); mb.box(-0.1, -0.1, 0, 0.1, 0.1, 1.0, "MetalDark"); mb.box(2.9, -0.1, 0, 3.1, 0.1, 1.0, "MetalDark")
    mb.obj("RoofSignLegs", -1.5, ctx["y1"] + 1.06, zr + 0.6, kind="trim")
    ctx["top"] = zr + 2.4
reg(("american_diner", "海港餐車", "Harborline Diner", "1950s American Diner", "美式復古餐車",
     "budget", "diner", ["retro", "realistic", "horror", "road-movie", "cartoon"],
     "Single-storey steel diner: counter with stools, booth tables, kitchen, striped awning, big neon roof sign."),
    dict(W=14, D=9, floors=1, h0=3.6, ext="PanelSteel", int="TileWhite", frame="Chrome", ground="restaurant",
         g_front=[("bar", 1), ("restaurant", 1)], floor0="TileBlue", door_x=-0.5, door_w=1.2, roof="flat", parapet=0.4,
         awning="AwningRed", awning_stripes="AwningWhite", awning_span=(-6.8, 6.8), front=5.0, plot_m="Asphalt"), _d3_diner)

def _d3_gas():
    meta = ("gas_station", "海港加油站", "Harbor Gas & Go", "Roadside Gas Station", "公路加油站", "budget", "gas station",
            ["realistic", "road-movie", "survival", "horror", "open-world"],
            "Convenience kiosk with shelves and counter, big illuminated canopy over four pumps, price pylon.")
    BX(meta, 1)
    ctx = std(dict(W=10, D=9, floors=1, h0=3.6, ext="PanelSteel", int="White", frame="FrameAlu", ground="shop", g_front=[("shop", 1)],
                   door_x=-2.0, door_k="door_glass", roof="flat", parapet=0.5, parapet_m="PlasticRed", front=14.0, side=7.0,
                   plot_m="Asphalt", sign=("便利商店  24H", "PlasticRed", "White", 5.0)))
    y1 = ctx["y1"]
    mb = MB()
    mb.box(-8.0, y1 - 12.0, 5.0, 8.0, y1 - 3.0, 5.6, "White"); mb.box(-8.05, y1 - 12.05, 5.2, 8.05, y1 - 2.95, 5.6, "PlasticRed")
    mb.box(-7.9, y1 - 11.9, 4.98, 7.9, y1 - 3.1, 5.0, "LightCool")
    for x in (-4.0, 4.0):
        mb.box(x - 0.25, y1 - 7.75, 0, x + 0.25, y1 - 7.25, 5.0, "White")
        mb.box(x - 1.6, y1 - 8.4, 0, x + 1.6, y1 - 6.6, 0.18, "Concrete")
    mb.obj("Canopy", kind="structure")
    for x in (-4.0, 4.0):
        for dx in (-0.9, 0.9):
            gas_pump(x + dx, y1 - 7.5, 0.18, 0 if dx < 0 else 180)
        lamp("CanopyL%d" % int(x), x, y1 - 7.5, 4.9, 250, (0.95, 0.97, 1.0), kind="point", fixture=False)
    car(-6.0, y1 - 7.5, 0, 0, "PlasticBlue")
    mb = MB(); mb.box(-0.15, -0.15, 0, 0.15, 0.15, 4.0, "MetalDark"); mb.box(-1.0, -0.2, 4.0, 1.0, 0.2, 6.5, "PlasticRed")
    mb.box(-0.9, -0.21, 4.2, 0.9, -0.2, 6.0, "White")
    mb.obj("PricePylon", 7.5, y1 - 12.5, 0, kind="sign")
    for i, (t, z) in enumerate((("GAS", 6.0), ("92  32.5", 5.2), ("95  34.0", 4.6))):
        text("Price%d" % i, t, 7.5, y1 - 12.73, z, 0.32 if i else 0.4, "Black" if i else "PlasticRed", extrude=0.01)
    ctx["top"] = 6.5
    finish_std(ctx)
regx(("gas_station",), _d3_gas, 24.0, 4.5 + 14.0, 4.5 + 2.0)

def _d3_motel(ctx):
    for i in range(4):
        car(-9.0 + i * 5.0, ctx["y1"] - 6.0, 0, 0, ["PlasticRed", "White", "PlasticDark", "PlasticYellow"][i])
    neon_vertical("MotelBlade", "MOTEL", ctx["x2"] + 1.2, ctx["y1"] - 2.0, 4.5, 4.0, 0, "NeonPink", "Black", 0.6)
reg(("seaview_motel", "海景汽車旅館", "Seaview Motor Inn", "American Roadside Motel", "公路汽車旅館",
     "budget", "motel", ["road-movie", "horror", "noir", "realistic", "retro"],
     "Two-storey motel strip: office/lobby, rows of guest rooms each with its own balcony walkway, neon MOTEL sign, parking."),
    dict(W=24, D=10, floors=2, h0=3.2, h=3.0, ext="BrickCream", frame="FrameWhite", win="win", bay=4.0, ground="lobby",
         g_front=[("lobby", 1)] + [("hotel", 1)] * 4, g_back=[("storage", 1), ("hotel", 1), ("hotel", 1), ("bath", 0.6)],
         u_front=[("hotel", 1)] * 5, u_back=[("hotel", 1)] * 4, balcony="front", balc_rail="bar", door_x=-9.6, door_k="door_glass",
         roof="flat", parapet=0.5, decor=["ac"], front=8.0, plot_m="Asphalt",
         sign=("海景汽車旅館  SEAVIEW MOTEL", "Black", "NeonCyan", 9.0)), _d3_motel)

def _d3_deco(ctx):
    zr = ctx["roof_z"]; x1, x2, y1 = ctx["x1"], ctx["x2"], ctx["y1"]
    mb = MB()
    for i, (w, h_) in enumerate(((10.0, 1.4), (7.0, 1.4), (4.0, 1.6))):
        z0 = zr + 1.0 + i * 1.4
        mb.box(-w / 2, y1 + 0.5, z0, w / 2, y1 + 3.5 - i * 0.5, z0 + h_, "BrickCream")
        mb.box(-w / 2 - 0.05, y1 + 0.45, z0 + h_ - 0.12, w / 2 + 0.05, y1 + 0.5, z0 + h_, "Brass")
    mb.cyl(0, y1 + 1.8, zr + 5.2, zr + 8.0, 0.08, "Brass", seg=8, r2=0.01)
    mb.obj("DecoCrown", kind="structure")
    for x in (-5.0, -1.5, 1.5, 5.0):
        ob("DecoFin%d" % int(x * 10), [(x - 0.12, y1 - 0.35, ctx["Z"][1], x + 0.12, y1 - 0.03, zr + 1.0)], ["BrickCream"], kind="trim")
    ctx["top"] = zr + 8.0
    mb = MB(); mb.box(-2.4, -2.6, 3.3, 2.4, 0.0, 3.5, "Brass"); mb.box(-2.3, -2.5, 3.28, 2.3, -0.1, 3.3, "LightWarm")
    mb.obj("EntryCanopy", -3.0, y1, 0, kind="structure")
reg(("hotel_artdeco", "裝飾藝術大飯店", "Grand Deco Hotel", "Art Deco Hotel", "裝飾藝術風",
     "luxury", "hotel", ["noir", "1920s", "realistic", "mystery", "bioshock-like"],
     "6-storey Art Deco hotel: black-marble lobby with reception + bar, restaurant, 24 guest rooms, brass-trimmed stepped crown, vertical fins."),
    dict(W=16, D=14, floors=6, h0=4.2, h=3.2, ext="BrickCream", ext0="MarbleBlack", frame="Brass", win="win", bay=2.8, ww=1.2,
         ground="lobby", g_front=[("lobby", 1.4), ("bar", 1)], g_back=[("restaurant", 1), ("bath", 0.5)],
         u_front=[("hotel", 1)] * 4, u_back=[("hotel", 1)] * 2, floor0="Marble", floor="CarpetRed", door_x=-3.0, door_w=1.8,
         roof="flat", decor=["bands", "cornice"], band_m="Stone", blade=("HOTEL", "NeonYellow"),
         sign=("GRAND DECO 裝飾大飯店", "MarbleBlack", "Brass", 6.0), sign_x=-3.0, front=5.0), _d3_deco)

reg(("bakery_corner", "麥香麵包坊", "Wheat & Hearth Bakery", "European Bakery", "歐式麵包店",
     "standard", "bakery + flat", ["cozy", "anime", "slice-of-life", "realistic", "ghibli"],
     "Cream-brick 2-storey bakery: bread display, oven, café table, striped awning; baker's flat upstairs."),
    dict(W=9, D=10, floors=2, ext="BrickCream", frame="WoodDark", win="win", ground="bakery", g_front=[("bakery", 1)],
         g_back=[("kitchen", 1)], u_front=[("living", 1)], u_back=[("bedroom", 1)], door_x=-2.4, roof="gable", roof_m="RoofTile",
         pitch=32, over=0.4, gable_m="BrickCream", awning="AwningRed", awning_stripes="AwningWhite", decor=["boxes", "chimney"],
         sign=("麥香麵包坊 BAKERY", "WoodDark", "PlasticYellow", 4.0)))

def _d3_izakaya(ctx):
    y1 = ctx["y1"]
    for i in range(6):
        lamp("Chochin%d" % i, -3.6 + i * 1.4, y1 - 0.6, 2.9, 15 if i % 2 else 0.01, (1.0, 0.4, 0.15), kind="lantern", glow="Lantern")
    mb = MB()
    for i in range(12):
        mb.box(-0.9 + i * 0.15, -0.01, 0, -0.84 + i * 0.15, 0.01, 0.8, "FabricNavy")
    mb.obj("Noren", -1.0, y1 - 0.08, 1.6, kind="trim")
    for i in range(3):
        crate(ctx["x2"] + 0.8, y1 + 1.0 + i * 0.7, 0, 15 * i, 0.5, "PlasticBlue")
reg(("izakaya_suikei", "居酒屋 酔鯨", "Izakaya Drunken Whale", "Japanese Izakaya", "日式居酒屋",
     "budget", "bar + flat", ["anime", "slice-of-life", "japan", "realistic", "noir"],
     "Timber-fronted izakaya: counter bar with stools, tables, kitchen, red lanterns and noren; small flat above; slate gable."),
    dict(W=9, D=10, floors=2, ext0="WoodDark", ext="Plaster", frame="WoodDark", win="slide", ground="bar", g_front=[("bar", 1)],
         g_back=[("kitchen", 1)], u_front=[("living", 1)], u_back=[("bedroom", 1)], door_x=-1.0, door_k="door_glass",
         shop_k="slide", shop_frame="WoodDark", roof="gable", roof_m="SlateDark", pitch=28, over=0.5, gable_m="Plaster", cap="SlateDark",
         sign=("居酒屋  酔鯨", "WoodDark", "LabelGlow", 3.6)), _d3_izakaya)

def _d3_ktv(ctx):
    for i, zz in enumerate(ctx["Z"][1:-1]):
        ob("NeonBand%d" % i, [(ctx["x1"] - 0.08, ctx["y1"] - 0.09, zz - 0.18, ctx["x2"] + 0.08, ctx["y1"] - 0.05, zz - 0.1)],
           [["NeonPink", "NeonPurple", "NeonCyan"][i % 3]], kind="light_fixture")
    lamp("KTVGlow", 0, ctx["y1"] - 1.5, 4.0, 80, (1.0, 0.3, 0.9), kind="point", fixture=False)
reg(("karaoke_stardust", "星光KTV", "Stardust Karaoke Club", "Neon Karaoke Club", "霓虹KTV",
     "standard", "karaoke club", ["cyberpunk", "anime", "nightlife", "realistic", "kdrama"],
     "4-storey black KTV: G/F bar, private karaoke lounges on upper floors (sofa + TV), neon floor bands, vertical blade sign."),
    dict(W=12, D=12, floors=4, h0=3.6, h=3.2, ext="PanelDark", int="CarpetRed", frame="MetalDark", win="win", ground="bar",
         g_front=[("bar", 1)], g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("lounge", 1), ("lounge", 1)], u_back=[("lounge", 1), ("bath", 0.6)],
         floor="CarpetRed", door_x=-2.5, door_w=1.4, roof="flat", blade=("KTV星光", "NeonPink"),
         sign=("STARDUST  星光KTV", "Black", "NeonPurple", 6.0), decor=["ac"]), _d3_ktv)

reg(("bookstore_cafe", "書與咖啡", "Books & Beans", "Brick Bookshop Café", "紅磚書店咖啡",
     "standard", "bookstore + café", ["cozy", "anime", "slice-of-life", "realistic", "mystery"],
     "3-storey brick bookshop: G/F bookstacks, 2F café with counter and tables, 3F reading loft flat, green awning."),
    dict(W=10, D=11, floors=3, ext="Brick", frame="WoodDark", win="win3", ground="library", g_front=[("library", 1)],
         g_back=[("storage", 1), ("bath", 0.6)], prog={1: ([("cafe", 1)], [("kitchen", 1), ("bath", 0.6)]),
                                                     2: ([("living", 1)], [("bedroom", 1)])},
         door_x=-2.4, door_k="door_glass", roof="flat", awning="AwningGreen", decor=["cornice", "boxes"], band_m="Stone",
         sign=("書與咖啡  BOOKS & BEANS", "AwningGreen", "White", 5.0)))

reg(("laundromat_flats", "泡泡自助洗衣", "Bubbles Laundromat", "Urban Laundromat Walk-up", "自助洗衣公寓",
     "budget", "laundromat + flats", ["slice-of-life", "anime", "realistic", "noir"],
     "Narrow 3-storey mosaic block: G/F coin laundry with washer wall and bench, two small flats above."),
    dict(W=8, D=10, floors=3, ext="MosaicBeige", ext0="TileWhite", win="grille", ground="laundry", g_front=[("laundry", 1)],
         g_back=[("storage", 1)], u_front=[("living", 1)], u_back=[("bedroom", 1)], door_x=-2.4, roof="terrace", decor=["ac", "pipes"],
         sign=("泡泡自助洗衣 24H", "PlasticBlue", "White", 4.5)))

def _d3_arcade(ctx):
    ob("ArcadeNeonTop", [(ctx["x1"] - 0.1, ctx["y1"] - 0.12, ctx["roof_z"] - 0.4, ctx["x2"] + 0.1, ctx["y1"] - 0.06, ctx["roof_z"] - 0.3)],
       ["NeonCyan"], kind="light_fixture")
    lamp("ArcadeGlow", 0, ctx["y1"] - 1.5, 3.0, 80, (1.0, 0.3, 0.8), kind="point", fixture=False)
reg(("galaxy_arcade", "銀河遊戲中心", "Galaxy Game Center", "Neon Game Arcade", "霓虹遊樂場",
     "standard", "arcade", ["cyberpunk", "anime", "retro", "nightlife", "realistic"],
     "2-storey black game centre: rows of arcade cabinets, claw machines, upstairs arcade + bar, neon signage."),
    dict(W=14, D=12, floors=2, h0=3.8, ext="PanelDark", int="PanelDark", frame="MetalDark", ground="arcade", g_front=[("arcade", 1)],
         g_back=[("storage", 1), ("bath", 0.6)], u_front=[("arcade", 1), ("bar", 1)], u_back=[("lounge", 1), ("bath", 0.6)],
         floor0="CarpetRed", floor="CarpetGrey", door_x=-3.5, door_w=1.6, roof="flat", blade=("遊戲中心", "NeonCyan"),
         sign=("GALAXY 銀河遊戲中心", "Black", "NeonPink", 7.0)), _d3_arcade)

def _d3_florist(ctx):
    y1 = ctx["y1"]
    for i in range(8):
        plant(ctx["x1"] + 0.6 + i * 0.85, y1 - 0.8 - (i % 2) * 0.5, 0, 0, 0.6 + (i % 3) * 0.2, RNG.choice(["Terracotta", "PlasticBlue", "White"]),
              ["bush", "tall", "bush", "palm"][i % 4])
reg(("florist_petal", "花語花店", "Petal Talk Florist", "Cottage Flower Shop", "鄉村花店",
     "standard", "shop + flat", ["cozy", "anime", "romance", "slice-of-life", "ghibli"],
     "White clapboard 2-storey flower shop: plant-filled shop floor, flower stands on the pavement, green awning, flat above with flower boxes."),
    dict(W=8, D=9.5, floors=2, ext="SidingWhite", frame="PaintTeal", win="win", ground="shop", g_front=[("shop", 1)], g_back=[("storage", 1)],
         u_front=[("living", 1)], u_back=[("bedroom", 1)], door_x=-1.8, roof="gable", roof_m="SlateBlue", pitch=35, over=0.4,
         gable_m="SidingWhite", cap="SlateDark", awning="AwningGreen", decor=["boxes"], front=4.0,
         sign=("花語花店  FLORIST", "White", "PaintTeal", 3.6)), _d3_florist)
