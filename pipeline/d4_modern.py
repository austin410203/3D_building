# District 4 — modern / industrial (10). Names prefixed _d4_.

def _d4_bauhaus(ctx):
    y1 = ctx["y1"]
    mb = MB(); mb.box(-2.4, -1.8, 2.7, 1.2, 0.0, 2.9, "White"); mb.obj("Canopy", ctx.get("dx", 0) - 2.0, y1, 0, kind="structure")
    ob("RedPanel", [(ctx["x2"] - 2.0, y1 - 0.06, ctx["Z"][1], ctx["x2"], y1 - 0.03, ctx["Z"][2])], ["PaintRed"], kind="trim")
reg(("bauhaus_house", "包浩斯白宅", "Bauhaus White House", "Bauhaus Modernism", "包浩斯",
     "upscale", "house", ["realistic", "modern", "architectural", "anime"],
     "Crisp white cubic 2-storey house: ribbon windows, flat roof terrace, cantilever entrance canopy, red accent panel."),
    dict(W=12, D=10, floors=2, ext="Plaster", frame="Black", win="win3", bay=3.4, ww=2.6, ground="living",
         g_front=[("living", 1.4), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("bedroom", 1), ("studio", 1)],
         u_back=[("bedroom", 1), ("bath", 0.6)], door_x=-2.0, door_k="door", door_m="Black", roof="terrace", parapet=0.9,
         plot_m="Grass", decor=["trees"]), _d4_bauhaus)

def _d4_mcm(ctx):
    y1, x2 = ctx["y1"], ctx["x2"]
    mb = MB(); mb.box(-0.6, -0.5, 0, 0.6, 0.5, ctx["top"] + 1.0, "Stone"); mb.obj("StoneChimney", ctx["x1"] + 3.0, 0.5, 0, kind="trim")
    mb = MB()
    mb.box(x2, y1 - 1.0, 2.8, x2 + 5.0, y1 + 5.0, 3.0, "WoodLight")
    for (x, y) in ((x2 + 4.8, y1 - 0.8), (x2 + 4.8, y1 + 4.8)):
        mb.box(x - 0.08, y - 0.08, 0, x + 0.08, y + 0.08, 2.8, "MetalDark")
    mb.obj("Carport", kind="structure"); car(x2 + 2.6, y1 + 2.0, 0, 0, "PlasticYellow")
reg(("midcentury_house", "中世紀現代宅", "Palm Springs Mid-Century House", "Mid-Century Modern", "中世紀現代",
     "upscale", "house", ["retro", "realistic", "mad-men", "modern", "gta-like"],
     "Low single-storey timber house with floor-to-ceiling glass, butterfly-flat shed roof with deep eaves, stone chimney, carport."),
    dict(W=16, D=10, floors=1, h0=3.0, ext="WoodLight", int="PlasterInt", frame="FrameAlu", win="shop", sill=0.1, head=2.7, bay=3.2, ww=2.6,
         g_front=[("living", 1.5), ("kitchen", 1), ("bedroom", 1)], roof="shed", roof_m="WoodDark", pitch=4, over=1.4, door_x=-2.0,
         door_k="door", door_m="PaintTeal", side=7.0, plot_m="Grass", decor=["plants"]), _d4_mcm)

reg(("concrete_minimal", "清水模住宅", "Fair-faced Concrete House", "Japanese Minimalist Concrete", "日式清水模",
     "luxury", "house", ["realistic", "modern", "thriller", "zen", "architectural"],
     "Introverted fair-faced concrete 2-storey house: few deep windows, minimal interior, flat roof, single maple tree."),
    dict(W=10, D=12, floors=2, ext="Concrete", int="Concrete", frame="Black", win="win", bay=4.0, ww=1.4, side_windows=False,
         ground="living", g_front=[("living", 1)], g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("bedroom", 1)], u_back=[("studio", 1)],
         door_x=-2.4, door_k="door", door_m="WoodLight", roof="flat", parapet=0.3, plot_m="Grass", decor=["trees"]))

reg(("glass_cube_office", "黑玻璃創意辦公", "Obsidian Cube Offices", "Contemporary Glass Office", "當代玻璃辦公",
     "upscale", "office", ["modern", "corporate", "cyberpunk", "realistic", "thriller"],
     "4-storey dark glass cube: lobby + café, open-plan offices and meeting rooms, roof terrace with solar canopy."),
    dict(W=16, D=16, floors=4, h0=4.0, h=3.6, ext="PanelDark", frame="MetalDark", win="shop", sill=0.1, head=3.0, bay=3.4, ww=3.0,
         ground="lobby", g_front=[("lobby", 1), ("cafe", 1)], g_back=[("meeting", 1), ("bath", 0.6)],
         u_front=[("office_open", 1.4), ("meeting", 1)], u_back=[("office", 1), ("bath", 0.6)], floor="CarpetGrey", door_x=-3.6, door_w=1.8,
         roof="terrace", decor=["solar"], sign=("OBSIDIAN  黑曜創意", "Black", "LabelGlowCyan", 6.0), front=5.0))

reg(("warehouse_loft", "紅磚倉庫Loft", "Red-Brick Warehouse Lofts", "Industrial Warehouse Loft", "工業倉庫改建",
     "standard", "loft + workshop", ["realistic", "industrial", "crime", "cyberpunk", "post-apocalyptic"],
     "Converted brick warehouse: G/F workshop and garage bay with roller door, two double-height studio lofts above, sawtooth glazed roof."),
    dict(W=20, D=14, floors=2, h0=5.0, h=4.0, ext="Brick", frame="MetalDark", win="win3", bay=3.4, ww=2.2, head=3.4, ground="workshop",
         g_front=[("workshop", 1), ("garage", 1)], g_back=[("storage", 1), ("bath", 0.6)], u_front=[("studio", 1), ("studio", 1)],
         u_back=[("lounge", 1), ("bath", 0.6)], floor0="Concrete", floor="Parquet",
         s_ops0=[(-9.0, -6.8, 1.0, 4.2, "win3", "MetalDark"), (-6.0, -3.8, 1.0, 4.2, "win3", "MetalDark"), (1.6, 7.6, 0, 4.2, "roller")],
         door_x=-2.4, door_k="door_metal", roof="sawtooth", roof_m="TinRust", decor=["pipes"], pipe_m="Rust",
         sign=("NO.9 WAREHOUSE  九號倉庫", "Black", "PlasticYellow", 6.0), sign_x=-4.0))

def _d4_dc(ctx):
    zr = ctx["roof_z"]
    for i in range(4):
        mb = MB(); mb.box(-1.0, -1.0, 0, 1.0, 1.0, 1.4, "PanelSteel"); mb.cyl(0, 0, 1.4, 1.6, 0.85, "MetalDark", seg=20)
        furn("Chiller", mb, -6.0 + i * 3.4, 2.0, zr, 0)
    for i in range(2):
        mb = MB(); mb.box(-1.4, -0.7, 0, 1.4, 0.7, 1.8, "PlasticYellow"); mb.cyl(1.0, 0, 1.8, 2.6, 0.12, "MetalDark", seg=10)
        furn("Generator", mb, ctx["x2"] + 2.4, -3.0 + i * 3.0, 0, 90)
reg(("data_center", "雲端資料中心", "Nimbus Data Center", "Hyperscale Data Center", "資料中心",
     "utility", "data center", ["cyberpunk", "sci-fi", "thriller", "realistic", "hacker"],
     "Windowless steel data hall: server rooms with rack rows and consoles, NOC office, roof chillers, backup generators."),
    dict(W=18, D=14, floors=2, h0=4.2, h=4.0, ext="PanelSteel", int="White", frame="MetalDark", win="win", bay=6.0, ww=1.0,
         side_windows=False, ground="server", g_front=[("server", 1), ("server", 1)], g_back=[("office", 1), ("bath", 0.5)],
         u_front=[("server", 1), ("office_open", 1)], u_back=[("server", 1), ("bath", 0.5)], floor0="Concrete", floor="Concrete",
         door_x=-5.0, door_k="door_metal", roof="flat", parapet=1.6, parapet_m="PanelDark", side=6.0,
         sign=("NIMBUS DATA", "PanelDark", "LED", 4.0)), _d4_dc)

reg(("capsule_tower", "蜂巢膠囊旅館", "Hive Capsule Hotel", "Capsule Hotel Tower", "膠囊旅館",
     "budget", "capsule hotel", ["cyberpunk", "anime", "sci-fi", "realistic", "japan"],
     "7-storey slim capsule hotel: lobby, floors of stacked bunk capsules + lounges, roof terrace, neon blade sign."),
    dict(W=9, D=11, floors=7, h0=3.4, h=2.9, ext="PanelDark", ext0="GrimeTeal", frame="MetalDark", win="win", bay=2.0, ww=0.8,
         ground="lobby", g_front=[("lobby", 1)], g_back=[("bath", 1)], u_front=[("dorm", 1)], u_back=[("lounge", 1)],
         floor="CarpetGrey", door_x=-2.4, roof="terrace", decor=["ac", "pipes"], blade=("膠囊旅館", "NeonCyan"),
         sign=("HIVE 蜂巢", "Black", "NeonYellow", 3.4)))

def _d4_eco(ctx):
    for f, zz in enumerate(ctx["Z"][1:-1]):
        for (k, a, b) in ctx["rooms"][f + 1][1]:
            if b - a > 2.4:
                planter((a + b) / 2, ctx["y1"] - 1.12, zz, 0, b - a - 0.8, 0.3, 0.35, "WoodDark", trailing=True)
    for i in range(3):
        tree(ctx["x1"] + 2.0 + i * 4.0, ctx["y2"] - 2.0, ctx["roof_z"], 0.6, "broad", seed=700 + i)
reg(("eco_apartments", "綠廊生態公寓", "Green Terrace Eco Apartments", "Biophilic Eco Housing", "綠建築生態宅",
     "upscale", "apartment", ["solarpunk", "realistic", "modern", "anime", "utopia"],
     "5-storey timber-clad eco block: every flat has a planted balcony with trailing greenery, roof garden with trees and solar."),
    dict(W=14, D=12, floors=5, ext="WoodLight", ext0="Concrete", frame="Black", win="win3", ground="cafe", g_front=[("cafe", 1)],
         g_back=[("storage", 1), ("bath", 0.6)], u_front=[("living", 1.4), ("bedroom", 1)], u_back=[("kitchen", 1), ("bath", 0.6)],
         balcony="front", balc_rail="glass", balc_plants=False, roof="terrace", decor=["solar"], door_x=-3.0,
         sign=("綠廊 GREEN TERRACE", "WoodDark", "PlasticGreen", 5.0)), _d4_eco)

def _d4_green(ctx):
    x1, x2, y1, y2, zr = ctx["x1"], ctx["x2"], ctx["y1"], ctx["y2"], ctx["roof_z"]
    mb = MB()
    for i in range(int((x2 - x1) / 1.2) + 1):
        x = x1 + i * 1.2
        mb.box(x - 0.03, y1 - 0.04, 0, x + 0.03, y1 + 0.02, zr, "White"); mb.box(x - 0.03, y2 - 0.02, 0, x + 0.03, y2 + 0.04, zr, "White")
    for i in range(int((y2 - y1) / 1.2) + 1):
        y = y1 + i * 1.2
        mb.box(x1 - 0.04, y - 0.03, 0, x1 + 0.02, y + 0.03, zr, "White"); mb.box(x2 - 0.02, y - 0.03, 0, x2 + 0.04, y + 0.03, zr, "White")
    for zz in (1.0, 2.2):
        mb.box(x1 - 0.04, y1 - 0.04, zz, x2 + 0.04, y1 + 0.02, zz + 0.05, "White")
    mb.obj("GreenhouseFrame", kind="trim")
    for i in range(10):
        plant(x1 + 0.7 + (i % 5) * ((x2 - x1 - 1.4) / 4), (y2 - 0.6) if i < 5 else (y1 + 0.6), 0, 0, 1.0 + (i % 3) * 0.3, "Terracotta",
              ["palm", "tall", "bush"][i % 3])
reg(("greenhouse_cafe", "玻璃溫室咖啡", "Glasshouse Garden Café", "Victorian Glasshouse", "玻璃溫室",
     "upscale", "café", ["cozy", "ghibli", "romance", "solarpunk", "realistic"],
     "Single-storey white-framed glasshouse with a glass gable roof: café counter, tables among potted palms and ferns."),
    dict(W=12, D=9, floors=1, h0=3.4, T=0.06, ext="Glass", int="Glass", frame="White", ground="cafe", g_front=[("cafe", 1)],
         side_windows=False, roof="gable", roof_m="Glass", pitch=30, over=0.15, gable_m="Glass", cap="White", door_x=0.0, door_k="door_glass",
         plot_m="Cobble", decor=["plants"], front=4.0), _d4_green)

def _d4_aframe():
    meta = ("a_frame_cabin", "森林A字木屋", "Forest A-Frame Cabin", "A-Frame Cabin", "A字型木屋", "standard", "cabin",
            ["cozy", "horror", "survival", "realistic", "winter"],
            "Steep A-frame timber cabin: glazed front gable with door, living + kitchenette below, sleeping loft reached by a centre stair, deck.")
    BX(meta, 2)
    W, D, H = 8.0, 10.0, 7.6
    ob("Plot", [(-7.0, -9.0, -0.4, 7.0, 7.0, 0.0)], ["Grass"], kind="terrain", walkable=True)
    ob("Deck", [(-4.5, -8.0, 0.0, 4.5, -5.0, 0.35)], ["WoodLight"], kind="floor", walkable=True)
    slab("Floor", -3.9, -4.9, 3.9, 4.9, 0.35, 0.35, top="WoodFloor", under="WoodDark")
    mb = MB()
    for sx in (-1, 1):
        mb.quad([(sx * W / 2, -D / 2 - 0.6, 0.0), (sx * W / 2, D / 2 + 0.6, 0.0), (0, D / 2 + 0.6, H), (0, -D / 2 - 0.6, H)], "SlateDark", 0.0)
        mb.quad([(sx * (W / 2 - 0.25), -D / 2, 0.0), (sx * (W / 2 - 0.25), D / 2, 0.0), (0, D / 2, H - 0.36), (0, -D / 2, H - 0.36)], "WoodLight", 0.0)
    mb.obj("AFrameRoof", kind="roof")
    o = CUR.col.objects[_nm("AFrameRoof")]
    for p in o.data.polygons: p.use_smooth = False
    # front glazed gable with a real door hole
    zl = H * (1 - 0.55 / (W / 2))
    mb = MB()
    mb.prism([(-W / 2 + 0.25, 0.35), (-0.55, 0.35), (-0.55, zl - 0.3)], -D / 2, -D / 2 + 0.06, "Glass", plane="xz")
    mb.prism([(0.55, 0.35), (W / 2 - 0.25, 0.35), (0.55, zl - 0.3)], -D / 2, -D / 2 + 0.06, "Glass", plane="xz")
    mb.prism([(-0.55, 2.6), (0.55, 2.6), (0.55, zl - 0.3), (0.0, H - 0.4), (-0.55, zl - 0.3)], -D / 2, -D / 2 + 0.06, "Glass", plane="xz")
    for x in (-2.4, -1.2, 1.2, 2.4):
        zt = H * (1 - abs(x) / (W / 2)) - 0.3
        mb.box(x - 0.04, -D / 2 - 0.02, 0.35, x + 0.04, -D / 2 + 0.08, zt, "WoodDark")
    for z in (2.6, 4.6):
        hw = (W / 2) * (1 - z / H) - 0.25
        mb.box(-hw, -D / 2 - 0.02, z - 0.04, hw, -D / 2 + 0.08, z + 0.04, "WoodDark")
    mb.prism([(-W / 2 + 0.25, 0.35), (W / 2 - 0.25, 0.35), (0.0, H - 0.36)], D / 2 - 0.12, D / 2, "WoodDark", plane="xz")
    mb.obj("Gables", kind="wall")
    fill("FrontDoor", "S", -D / 2 - 0.02, -D / 2 + 0.08, -0.5, 0.5, 0.35, 2.55, "door", frame="WoodDark")
    CUR.main_door = (0.0, -D / 2, 0.35)
    # loft + centre stair
    slab("Loft", -2.3, 0.6, 2.3, 4.8, 3.2, 0.2, top="WoodFloor", under="WoodLight")
    stair("LoftStair", 0.0, 0.6 - (round((3.2 - 0.35) / 0.18) - 1) * 0.25, 0.35, 3.2, "+y", 0.8, 0.25, "WoodLight", rails="both", rail_style="wood")
    rail("LoftRailW", -2.3, 0.62, -0.42, 0.62, 3.2, 0.9, "wood"); rail("LoftRailE", 0.42, 0.62, 2.3, 0.62, 3.2, 0.9, "wood")
    bed(0.0, 3.6, 3.2, 0, 1.4, 2.0, "FabricRed", "WoodLight")
    sofa(-2.0, -3.2, 0.35, 90, 1.8, "FabricGreen"); coffee_table(-1.0, -3.2, 0.35, 90, 0.9, 0.5)
    fireplace(2.5, -3.0, 0.35, 270, "Stone")
    kitchen_run(1.6, 4.55, 0.35, 0, 2.0, "WoodLight", "WoodDark", uppers=False)
    table(-1.8, 2.6, 0.35, 0, 1.0, 0.7, 0.75, "WoodDark"); chair(-1.8, 2.0, 0.35, 180); chair(-1.8, 3.2, 0.35, 0)
    lamp("CabinL1", 0.0, -2.0, 5.2, 70, kind="pendant"); lamp("CabinL2", 0.0, 3.0, 5.8, 40, kind="pendant")
    for i in range(4):
        crate(4.6, -3.0 + i * 0.6, 0.0, 10 * i, 0.5, "WoodLight")
    for i, (x, y) in enumerate(((-6.0, 5.5), (6.0, 5.0), (-6.2, -2.0))):
        tree(x, y, 0, 1.1, "pine", seed=800 + i)
    lamp("PorchLamp", 0.9, -5.15, 2.4, 25, kind="wall")
    ctx = dict(top=H, y1=-D / 2, W=W)
    finish_std(ctx)
regx(("a_frame_cabin",), _d4_aframe, 14.0, 9.0, 7.0)
