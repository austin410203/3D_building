# District 8 — modern / future / industrial (25). Names prefixed _d8_.

def _d8_m(i, zh, en, st, stz, tier, cat, gs, desc):
    return (i, zh, en, st, stz, tier, cat, gs, desc)

reg(_d8_m("minimal_white_box", "極簡白盒屋", "Minimal White Box", "Minimalist Modern", "極簡主義", "upscale", "house",
          ["modern", "realistic", "architectural", "anime"], "Pure white 2-storey box with a few large picture windows, flush door, roof terrace."),
    dict(W=10, D=9.5, floors=2, ext="Plaster", frame="White", win="shop", bay=4.5, ww=2.6, sill=0.4, g_front=[("living", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1)], u_back=[("studio", 1)], roof="terrace", parapet=0.9, door_k="door", door_m="White", plot_m="Grass", decor=["trees"]))

def _d8_canti(ctx):
    zr = ctx["Z"][1]
    slab("CantiDeck", ctx["x2"], ctx["y1"] + 0.5, ctx["x2"] + 4.5, ctx["y2"] - 0.5, zr, 0.4, top="WoodLight", under="Concrete")
    rails_rect("CantiRail", ctx["x2"], ctx["y1"] + 0.5, ctx["x2"] + 4.5, ctx["y2"] - 0.5, zr, "SNE", style="glass")
    umbrella_table(ctx["x2"] + 2.2, 0.0, zr, 0, "AwningWhite")
reg(_d8_m("cantilever_house", "懸挑清水宅", "Cantilever Concrete House", "Brutalist Cantilever", "懸挑住宅", "luxury", "house",
          ["modern", "thriller", "architectural", "realistic"], "Concrete 2-storey house whose upper floor projects into a 4.5 m cantilevered terrace with glass rail."),
    dict(W=12, D=10, floors=2, ext="Concrete", frame="Black", win="shop", ww=2.8, g_front=[("living", 1), ("kitchen", 1)], g_back=[("bedroom", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1), ("studio", 1)], u_back=[("bath", 1)], roof="flat", parapet=0.3, door_k="door", door_m="WoodLight", side=7.0, plot_m="Grass"), _d8_canti)

reg(_d8_m("green_roof_house", "綠屋頂住宅", "Living-Roof House", "Eco Green-Roof House", "綠屋頂", "upscale", "house",
          ["solarpunk", "modern", "cozy", "realistic"], "Timber 2-storey house with a sedum-planted shed roof, big south glazing and planters."),
    dict(W=12, D=10, floors=2, ext="WoodLight", frame="Black", win="win3", ww=2.2, g_front=[("living", 1.2), ("kitchen", 1)], g_back=[("bedroom", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1), ("studio", 1)], u_back=[("bath", 1)], roof="shed", roof_m="Grass", pitch=10, over=0.8, door_m="Black", plot_m="Grass", decor=["plants"]))

reg(_d8_m("solar_row_house", "太陽能社區屋", "Solar Row House", "Net-Zero Row House", "太陽能住宅", "standard", "house",
          ["solarpunk", "modern", "realistic"], "2-storey net-zero house: whole shed roof is a solar array, heat-pump unit, light timber cladding."),
    dict(W=9, D=10, floors=2, ext="SidingWhite", frame="FrameAlu", win="win", g_front=[("living", 1)], g_back=[("kitchen", 1)],
         u_front=[("bedroom", 1)], u_back=[("bath", 1)], roof="shed", roof_m="Solar", pitch=18, over=0.4, door_m="WoodLight", decor=["ac"], plot_m="Grass"))

reg(_d8_m("container_flats", "三色貨櫃公寓", "Tricolour Container Flats", "Shipping-Container Apartments", "貨櫃公寓", "budget", "apartment",
          ["industrial", "post-apocalyptic", "modern", "realistic"], "3-storey stack clad in blue / yellow / grey corrugated container steel, plywood interiors, roof terrace."),
    dict(W=12, D=10, floors=3, ext_f=["ContBlue", "ContYellow", "ContGrey"], int="WoodLight", frame="MetalDark", win="win", g_front=[("living", 1), ("bedroom", 1)],
         g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("studio", 1), ("bedroom", 1)], u_back=[("kitchen", 1), ("bath", 0.6)], balcony="alt",
         roof="terrace", door_k="door_metal", decor=["pipes"]))

def _d8_dome():
    meta = _d8_m("printed_dome_home", "3D列印圓頂屋", "3D-Printed Dome Home", "3D-Printed Concrete Dome", "3D列印建築", "standard", "house",
                 ["sci-fi", "solarpunk", "post-apocalyptic", "mars-colony"], "Single-storey printed concrete drum with a smooth dome roof, round windows, sleeping and living niches.")
    def furnish(f, z, r):
        bed(-1.8, 1.6, z, 135, 1.4, 2.0, "FabricBeige"); sofa(1.8, 1.4, z, 225, 2.0, "FabricNavy"); kitchen_run(0.0, 3.6, z, 0, 2.4, "White", "Marble", uppers=False)
    ctx = _d5_round(meta, 16, 4.8, 1, 3.0, "Concrete", "Plaster", roof="none", plot_m="Sand", furnish=furnish, win_segs=[2, 6, 10, 14])
    dome("PrintedDome", 0, 0, ctx["zt"] + 0.25, 4.9, "Concrete", 0.55, seg=40)
    ctx["top"] = ctx["zt"] + 3.0; finish_std(ctx)
regx(("printed_dome_home",), _d8_dome, 14.0, 9.0, 7.0)

reg(_d8_m("startup_hq", "新創科技總部", "Startup HQ", "Tech Startup Office", "科技新創", "upscale", "office",
          ["modern", "corporate", "slice-of-life", "cyberpunk"], "3-storey dark-glass office: lobby café, open-plan desks, meeting rooms, server room, roof terrace."),
    dict(W=16, D=14, floors=3, h0=4.0, h=3.6, ext="PanelDark", frame="MetalDark", win="shop", ww=3.0, sill=0.2, ground="lobby", g_front=[("lobby", 1), ("cafe", 1)],
         g_back=[("server", 1), ("bath", 0.6)], u_front=[("office_open", 1.4), ("meeting", 1)], u_back=[("lounge", 1), ("bath", 0.6)], floor="CarpetGrey",
         roof="terrace", decor=["solar"], door_x=-3.6, door_w=1.8, sign=("NOVA LABS", "Black", "LabelGlowCyan", 4.0)))

def _d8_esports(ctx):
    ob("LEDWall", [(ctx["x1"] + 1.0, ctx["y1"] - 0.08, 3.6, ctx["x2"] - 1.0, ctx["y1"] - 0.04, 4.6)], ["Screen"], kind="sign")
reg(_d8_m("esports_arena", "電競競技館", "Esports Arena", "Esports Venue", "電競館", "upscale", "arena",
          ["cyberpunk", "modern", "anime", "sports"], "2-storey black venue: tall ground floor of gaming PC rows and a stage, lounge & bar upstairs, LED facade."),
    dict(W=18, D=14, floors=2, h0=5.0, h=3.6, ext="PanelDark", int="PanelDark", frame="MetalDark", win="win", ground="lobby", g_front=[("office", 1.4), ("lobby", 1)],
         g_back=[("server", 1), ("bath", 0.6)], u_front=[("bar", 1), ("lounge", 1)], u_back=[("office", 1)], floor0="CarpetGrey", door_x=2.0, door_w=2.0,
         sign=("ARENA X  電競館", "Black", "NeonPurple", 7.0), blade=("電競", "NeonCyan")), _d8_esports)

reg(_d8_m("stream_studio", "直播工作室", "Live-Stream Studio", "Creator Studio Loft", "直播工作室", "standard", "studio",
          ["modern", "slice-of-life", "anime", "cyberpunk"], "3-storey creator building: street-level set, editing suites and a loft flat, pink neon."),
    dict(W=9, D=10, floors=3, ext="BrickDark", frame="Black", win="win3", ground="lounge", g_front=[("studio", 1)], g_back=[("server", 1)],
         u_front=[("office", 1)], u_back=[("lounge", 1)], door_x=-2.0, sign=("ON AIR", "Black", "NeonRed", 2.6), blade=("直播中", "NeonPink")))

reg(_d8_m("cowork_hub", "共享辦公大樓", "Co-Work Hub", "Co-working Office", "共享辦公", "standard", "office",
          ["modern", "slice-of-life", "realistic"], "4-storey brick-and-glass co-working building: café lobby, hot-desk floors, meeting pods, roof terrace."),
    dict(W=14, D=12, floors=4, ext="BrickDark", frame="MetalDark", win="win3", ww=2.4, ground="cafe", g_front=[("cafe", 1), ("lounge", 1)],
         g_back=[("meeting", 1), ("bath", 0.6)], u_front=[("office_open", 1)], u_back=[("meeting", 1), ("bath", 0.6)], roof="terrace", door_x=-3.0,
         sign=("CO-WORK HUB", "Black", "LabelGlow", 4.0)))

def _d8_ev():
    meta = _d8_m("ev_charging_hub", "電動車超充站", "EV Supercharge Hub", "EV Charging Station", "電動車充電站", "standard", "charging station",
                 ["modern", "sci-fi", "gta-like", "realistic"], "Lounge kiosk with café and shelves, solar canopy over six fast chargers with parked EVs.")
    BX(meta, 1)
    ctx = std(dict(W=10, D=8, floors=1, h0=3.6, ext="PanelDark", frame="MetalDark", win="shop", ww=2.6, g_front=[("cafe", 1)], door_x=-2.0,
                   roof="flat", parapet=0.4, front=13.0, side=7.0, plot_m="Asphalt", sign=("SUPERCHARGE ⚡", "Black", "LabelGlowCyan", 4.6)))
    y1 = ctx["y1"]
    mb = MB(); mb.quad([(-9.0, y1 - 12.0, 4.6), (9.0, y1 - 12.0, 4.6), (9.0, y1 - 3.0, 5.0), (-9.0, y1 - 3.0, 5.0)], "Solar", 0.12)
    for x in (-8.0, 0.0, 8.0):
        mb.box(x - 0.15, y1 - 7.6, 0, x + 0.15, y1 - 7.4, 4.8, "Chrome")
    mb.obj("SolarCanopy", kind="structure")
    for i, x in enumerate((-6.5, -4.0, -1.5, 1.5, 4.0, 6.5)):
        m2 = MB(); m2.box(-0.2, -0.15, 0, 0.2, 0.15, 1.6, "White"); m2.box(-0.15, -0.16, 1.2, 0.15, -0.15, 1.45, "LED")
        furn("Charger", m2, x, y1 - 4.0, 0, 0, "use")
        if i % 2 == 0:
            car(x, y1 - 6.6, 0, 0, ["White", "PlasticBlue", "PlasticDark"][i // 2])
        lamp("CanopyL%d" % i, x, y1 - 7.5, 4.5, 120, (0.9, 0.97, 1.0), kind="point", fixture=False)
    ctx["top"] = 5.2; finish_std(ctx)
regx(("ev_charging_hub",), _d8_ev, 24.0, 4.0 + 13.0, 4.0 + 2.0)

reg(_d8_m("parking_tower", "立體停車塔", "Multi-storey Car Park", "Parking Structure", "立體停車場", "utility", "parking",
          ["realistic", "action", "gta-like", "urban"], "5-storey open concrete car park with parked cars on every deck, stair core, big P sign."),
    dict(W=16, D=14, floors=5, h0=3.2, h=3.0, ext="Concrete", int="Concrete", frame="Frame", win="open", ww=3.0, bay=3.6, sill=1.0, head=2.6,
         g_front=[("garage", 1), ("garage", 1)], g_back=[("garage", 1)], u_front=[("garage", 1), ("garage", 1)], u_back=[("garage", 1)],
         floor0="Concrete", floor="Concrete", s_ops0=[(-7.5, -1.5, 0, 2.6, "open"), (0.5, 6.5, 0, 2.6, "open")], door_k="none", roof="flat", parapet=1.1,
         sign=("P  PARKING", "PlasticBlue", "White", 4.0), sign_x=0.0))

def _d8_wh(ctx):
    for i, x in enumerate((-6.0, 3.0)):
        mb = MB(); mb.box(-1.2, -1.1, 0.5, 1.2, 4.6, 3.6, "White"); mb.box(-1.2, -2.6, 0.5, 1.2, -1.1, 2.8, "PlasticBlue")
        mb.box(-1.1, -2.62, 1.8, 1.1, -2.6, 2.6, "GlassDark")
        for v in (-2.0, 3.0):
            mb.cyl(-1.25, v, 0.5, 2.5, 0.48, "Rubber", seg=16, axis="x")
        furn("Truck", mb, x, ctx["y1"] - 8.5, 0, 0, "use")
reg(_d8_m("logistics_warehouse", "物流倉儲中心", "Logistics Warehouse", "Distribution Warehouse", "物流倉庫", "utility", "warehouse",
          ["realistic", "industrial", "zombie", "action"], "Single tall steel warehouse: racking aisles, three roller loading docks, delivery trucks in the yard."),
    dict(W=24, D=16, floors=1, h0=7.0, ext="PanelSteel", int="Concrete", frame="MetalDark", win="win", sill=4.5, head=6.2, ww=2.0, g_front=[("storage", 1)],
         floor0="Concrete", s_ops0=[(-10.5, -6.5, 0, 4.2, "roller"), (-4.0, 0.0, 0, 4.2, "roller"), (2.5, 6.5, 0, 4.2, "roller")], door_x=9.0,
         door_k="door_metal", roof="flat", parapet=0.8, front=12.0, side=2.0, plot_m="Asphalt", sign=("SWIFT LOGISTICS", "PanelDark", "White", 6.0), sign_x=0.0), _d8_wh)

reg(_d8_m("cold_storage", "冷鏈冷凍廠", "Cold-Chain Plant", "Cold Storage Facility", "冷凍廠", "utility", "factory",
          ["realistic", "horror", "thriller", "industrial"], "Windowless white insulated-panel plant: freezer storage halls, control office, roof chillers."),
    dict(W=16, D=12, floors=1, h0=6.0, ext="White", int="White", frame="MetalDark", win="win", sill=4.0, head=5.2, bay=6.0, ww=1.0, g_front=[("storage", 1), ("office", 0.7)],
         floor0="Concrete", door_k="door_metal", door_x=5.0, roof="flat", parapet=0.6, sign=("FROSTLINE  冷鏈", "PlasticBlue", "White", 5.0), sign_x=-2.0),
    lambda c: [furn("Chiller", (lambda mb: (mb.box(-1.0, -1.0, 0, 1.0, 1.0, 1.4, "PanelSteel"), mb.cyl(0, 0, 1.4, 1.6, 0.85, "MetalDark", seg=20), mb)[-1])(MB()),
                    -4.0 + i * 3.6, 1.0, c["roof_z"], 0) for i in range(3)])

def _d8_brew(ctx):
    for i in range(4):
        mb = MB(); mb.cyl(0, 0, 0.6, 4.6, 0.9, "Chrome", seg=24); mb.cyl(0, 0, 4.6, 5.3, 0.9, "Chrome", seg=24, r2=0.15)
        for (dx, dy) in ((-0.6, -0.6), (0.6, -0.6), (0, 0.8)):
            mb.box(dx - 0.05, dy - 0.05, 0, dx + 0.05, dy + 0.05, 0.8, "MetalDark")
        furn("BrewTank", mb, ctx["x2"] + 1.6, ctx["y1"] + 1.6 + i * 2.4, 0, 0)
reg(_d8_m("craft_brewery", "精釀啤酒廠", "Harbor Craft Brewery", "Craft Brewery Taproom", "精釀酒廠", "standard", "brewery",
          ["realistic", "slice-of-life", "industrial", "rpg"], "2-storey brick brewhouse: taproom bar downstairs, brewing floor above, row of stainless fermentation tanks outside."),
    dict(W=14, D=12, floors=2, h0=4.6, ext="Brick", frame="MetalDark", win="win3", ground="bar", g_front=[("bar", 1), ("restaurant", 1)],
         g_back=[("storage", 1), ("bath", 0.6)], u_front=[("workshop", 1), ("storage", 1)], u_back=[("office", 1)], floor0="Concrete", door_x=-3.0,
         roof="sawtooth", roof_m="TinRust", side=5.0, sign=("HARBOR BREW CO.", "Black", "Brass", 5.0)), _d8_brew)

def _d8_tyres(ctx):
    for i in range(8):
        mb = MB(); mb.cyl(0, 0, 0, 0.25, 0.34, "Rubber", seg=16); mb.cyl(0, 0, -0.01, 0.26, 0.18, "Black", seg=12)
        furn("TyreStack", mb, ctx["x1"] - 1.0 + (i % 2) * 0.7, ctx["y1"] + 0.5 + (i // 2) * 0.9, (i % 3) * 0.25, 0)
reg(_d8_m("auto_repair", "老王汽車修理廠", "Wang's Auto Repair", "Auto Repair Garage", "汽車修理廠", "budget", "garage",
          ["realistic", "gta-like", "slice-of-life", "crime"], "Single-storey steel garage: two service bays with roller doors and cars on stands, workbenches, tyre stacks."),
    dict(W=14, D=10, floors=1, h0=4.5, ext="PanelSteel", int="Concrete", frame="MetalDark", win="win", g_front=[("garage", 1), ("garage", 1)],
         floor0="Concrete", s_ops0=[(-6.4, -1.4, 0, 3.6, "roller"), (0.2, 5.2, 0, 3.6, "roller")], door_x=6.2, door_w=0.9, door_k="door_metal",
         roof="flat", parapet=0.5, side=4.0, plot_m="Asphalt", sign=("老王汽修  AUTO REPAIR", "PlasticYellow", "Black", 6.0), sign_x=-0.6), _d8_tyres)

reg(_d8_m("cyberware_clinic", "義體改造診所", "Cyberware Clinic", "Cyberpunk Ripperdoc", "賽博義體診所", "budget", "clinic",
          ["cyberpunk", "sci-fi", "horror", "neo-noir"], "3-storey grimy teal clinic: neon-lit surgery bay with exam beds, server room, cramped quarters."),
    dict(W=8, D=10, floors=3, ext="GrimeTeal", int="TileWhite", frame="MetalDark", win="grille", ground="clinic", g_front=[("clinic", 1)], g_back=[("server", 1)],
         u_front=[("ward", 1)], u_back=[("bedroom", 1)], door_x=-2.0, door_k="door_metal", decor=["ac", "pipes"], blade=("義體改造", "NeonGreen"),
         sign=("RIPPERDOC", "Black", "NeonCyan", 3.4)))

def _d8_club(ctx):
    for i, zz in enumerate((ctx["Z"][1] - 0.15, ctx["roof_z"] - 0.2)):
        ob("ClubBand%d" % i, [(ctx["x1"] - 0.08, ctx["y1"] - 0.1, zz - 0.06, ctx["x2"] + 0.08, ctx["y1"] - 0.06, zz)], [["NeonPurple", "NeonCyan"][i]], kind="light_fixture")
reg(_d8_m("club_nova", "新星夜店", "Club Nova", "Neon Nightclub", "霓虹夜店", "standard", "nightclub",
          ["cyberpunk", "nightlife", "crime", "anime"], "2-storey black nightclub: dance floor + bar, VIP lounge upstairs, neon bands, queue rope."),
    dict(W=14, D=12, floors=2, h0=4.4, ext="PanelDark", int="PanelDark", frame="MetalDark", side_windows=False, ground="bar", g_front=[("bar", 1), ("lounge", 1)],
         g_back=[("storage", 1), ("bath", 0.6)], u_front=[("lounge", 1), ("bar", 1)], u_back=[("office", 1)], floor0="MarbleBlack", door_x=-2.0,
         door_k="door_metal", sign=("CLUB NOVA", "Black", "NeonPink", 5.0)),
    lambda c: (_d8_club(c), rope_posts(-2.0, c["y1"] - 2.0, 0, 0, 3.0)))

reg(_d8_m("pod_apartments", "未來膠囊陽台公寓", "Pod Balcony Apartments", "Futurist Pod Housing", "未來公寓", "upscale", "apartment",
          ["sci-fi", "modern", "solarpunk", "anime"], "6-storey white panel block with glass pod balconies on every flat, solar roof terrace."),
    dict(W=12, D=11, floors=6, h=3.0, ext="PanelSteel", frame="White", win="shop", ww=2.2, sill=0.4, ground="lobby", g_front=[("lobby", 1)],
         g_back=[("bath", 1)], u_front=[("living", 1), ("bedroom", 1)], u_back=[("kitchen", 1), ("bath", 0.6)], balcony="front", balc_rail="glass",
         roof="terrace", decor=["solar"], door_x=-3.0))

reg(_d8_m("vertical_farm", "垂直農場", "Vertical Farm Tower", "Vertical Farm", "垂直農場", "utility", "farm",
          ["solarpunk", "sci-fi", "farming-sim", "realistic"], "5-storey glass tower of LED-lit hydroponic racks, shop for produce, solar roof."),
    dict(W=14, D=12, floors=5, h=3.2, ext="GlassBlue", int="White", frame="White", win="shop", ww=3.0, sill=0.2, ground="market",
         g_front=[("market", 1)], g_back=[("storage", 1)], u_front=[("farm", 1)], u_back=[("farm", 1)], floor="Concrete", roof="terrace",
         decor=["solar"], door_x=-3.0, sign=("GREEN STACK FARM", "White", "PlasticGreen", 6.0)))

reg(_d8_m("harbor_aquarium", "海港水族館", "Harbor Aquarium", "Public Aquarium", "水族館", "landmark", "aquarium",
          ["family", "modern", "slice-of-life", "anime"], "Low dark hall of glowing fish tanks and benches under a big glass dome."),
    dict(W=18, D=14, floors=1, h0=5.0, ext="PanelDark", int="PanelDark", frame="MetalDark", win="win", side_windows=False, g_front=[("aquarium", 1), ("aquarium", 1)],
         floor0="MarbleBlack", door_k="door_glass", door_w=2.0, door_x=0.0, roof="dome", roof_m="GlassBlue", dome_k=0.75, dome_sz=0.5,
         sign=("海港水族館  AQUARIUM", "PanelDark", "LabelGlowCyan", 7.0), sign_x=0.0))

reg(_d8_m("science_museum", "海港科學館", "Harbor Science Museum", "Science Museum", "科學館", "landmark", "museum",
          ["family", "sci-fi", "mystery", "realistic"], "2-storey concrete museum with a glazed sawtooth roof: exhibit halls of consoles and models, library and meeting room."),
    dict(W=20, D=14, floors=2, h0=4.6, h=4.0, ext="Concrete", frame="MetalDark", win="win3", ww=2.4, ground="lobby", g_front=[("lobby", 1), ("server", 1)],
         g_back=[("library", 1), ("bath", 0.5)], u_front=[("library", 1), ("meeting", 1)], u_back=[("lounge", 1)], roof="sawtooth", roof_m="PanelSteel",
         door_x=-4.0, door_w=2.0, sign=("SCIENCE MUSEUM  科學館", "Concrete", "PlasticBlue", 7.0)))

def _d8_drone(ctx):
    zr = ctx["roof_z"]
    for i, x in enumerate((-2.5, 2.5)):
        mb = MB(); mb.cyl(0, 0, 0, 0.06, 1.8, "Concrete", seg=24); mb.cyl(0, 0, 0.06, 0.07, 1.6, "PlasticYellow", seg=24); mb.cyl(0, 0, 0.07, 0.08, 1.45, "Concrete", seg=24)
        mb.box(-0.6, -0.1, 0.08, 0.6, 0.1, 0.09, "Black"); mb.box(-0.1, -0.6, 0.08, 0.1, 0.6, 0.09, "Black")
        furn("DronePad", mb, x, 1.0, zr, 0)
        d = MB(); d.box(-0.25, -0.25, 0, 0.25, 0.25, 0.12, "PanelDark")
        for (dx, dy) in ((-0.4, -0.4), (0.4, -0.4), (-0.4, 0.4), (0.4, 0.4)):
            d.cyl(dx, dy, 0.12, 0.14, 0.18, "Black", seg=12)
        furn("Drone", d, x, 1.0, zr + 0.1, 30 * i)
reg(_d8_m("drone_hub", "無人機物流站", "Drone Delivery Hub", "Drone Logistics Hub", "無人機站", "utility", "logistics",
          ["sci-fi", "modern", "cyberpunk"], "3-storey steel hub: parcel storage and control room, roof landing pads with delivery drones."),
    dict(W=12, D=12, floors=3, ext="PanelSteel", frame="MetalDark", win="win3", ground="lobby", g_front=[("storage", 1), ("lobby", 1)], g_back=[("server", 1)],
         u_front=[("storage", 1), ("office", 1)], u_back=[("server", 1)], roof="terrace", door_x=-2.0, door_k="door_metal",
         sign=("SKYDROP", "PanelDark", "LED", 3.6)), _d8_drone)

def _d8_loop(ctx):
    pipe_run("LoopTube", [(ctx["x1"] - 6.0, ctx["y2"] + 1.4, 2.2), (ctx["x2"] + 6.0, ctx["y2"] + 1.4, 2.2)], 1.3, "GlassBlue")
    mb = MB(); mb.box(-2.5, -0.9, 1.4, 2.5, 0.9, 3.0, "White"); mb.box(-2.4, -0.91, 2.0, 2.4, -0.9, 2.6, "LightCool")
    furn("Pod", mb, 0.0, ctx["y2"] + 1.4, 0, 90)
reg(_d8_m("hyperloop_station", "超迴路列車站", "Hyperloop Station", "Hyperloop Terminal", "超迴路車站", "landmark", "station",
          ["sci-fi", "modern", "cyberpunk"], "Single-storey steel-and-glass terminal hall with ticket lobby, behind it a transparent hyperloop tube with a waiting pod."),
    dict(W=20, D=10, floors=1, h0=5.5, ext="PanelSteel", int="White", frame="FrameAlu", win="shop", ww=3.0, sill=0.2, ground="lobby", g_front=[("lobby", 1), ("cafe", 1)],
         floor0="Marble", door_k="door_glass", door_w=2.4, door_x=-4.0, roof="flat", parapet=0.6, back=5.0, side=7.0,
         sign=("HYPERLOOP  超迴路", "PanelDark", "LabelGlowCyan", 7.0), sign_x=0.0), _d8_loop)

def _d8_arco(ctx):
    for i, zz in enumerate(ctx["Z"][2:-1:2]):
        for (k, a, b) in ctx["rooms"][0][1]:
            planter((a + b) / 2, ctx["y1"] - 1.12, zz, 0, b - a - 0.8, 0.3, 0.35, "Concrete", trailing=True)
    for i in range(4):
        tree(ctx["x1"] + 2.0 + i * 4.0, ctx["y2"] - 2.0, ctx["roof_z"], 0.6, "broad", seed=880 + i)
reg(_d8_m("arcology_block", "生態巨構塊", "Arcology Block", "Arcology Megablock", "生態巨構", "luxury", "megablock",
          ["solarpunk", "sci-fi", "utopia", "cyberpunk"], "8-storey concrete megablock: market hall, apartments with planted balconies, roof forest and solar canopy."),
    dict(W=16, D=16, floors=8, h=3.0, ext="Concrete", frame="Black", win="win3", ww=2.2, ground="market", g_front=[("market", 1), ("cafe", 1)],
         g_back=[("storage", 1), ("bath", 0.6)], u_front=[("living", 1), ("bedroom", 1)], u_back=[("kitchen", 1), ("bath", 0.6)], balcony="front",
         balc_rail="glass", balc_plants=False, roof="terrace", decor=["solar"], door_x=-4.0, door_w=1.8,
         sign=("ARCOLOGY ONE", "Concrete", "PlasticGreen", 5.0)), _d8_arco)
