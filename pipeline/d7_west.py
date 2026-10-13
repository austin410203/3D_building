# District 7 — Europe & the Americas (25). Names prefixed _d7_.

def _d7_m(i, zh, en, st, stz, tier, cat, gs, desc):
    return (i, zh, en, st, stz, tier, cat, gs, desc)

def _d7_fence(ctx, m="White", d=4.0):
    mb = MB(); y = ctx["y1"] - d
    x = ctx["x1"] - 1.5
    while x < ctx["x2"] + 1.5:
        if abs(x - (CUR.main_door[0] if CUR.main_door else 0)) > 0.8:
            mb.box(x - 0.04, y - 0.02, 0, x + 0.04, y + 0.02, 0.95, m); mb.prism([(x - 0.04, 0.95), (x + 0.04, 0.95), (x, 1.05)], y - 0.02, y + 0.02, m, plane="xz")
        x += 0.2
    mb.box(ctx["x1"] - 1.5, y - 0.03, 0.3, ctx["x2"] + 1.5, y + 0.03, 0.36, m); mb.box(ctx["x1"] - 1.5, y - 0.03, 0.7, ctx["x2"] + 1.5, y + 0.03, 0.76, m)
    mb.obj("PicketFence", kind="railing")

reg(_d7_m("dutch_canal_house", "阿姆斯特丹運河屋", "Amsterdam Canal House", "Dutch Canal House", "荷蘭運河屋", "upscale", "townhouse",
          ["europe", "realistic", "romance", "anime"], "Tall narrow 4-storey brick canal house with a steep stepped gable, white sash windows and a hoist beam."),
    dict(W=6.4, D=12, floors=4, h0=3.4, h=3.0, ext="BrickDark", frame="FrameWhite", win="win", ww=1.1, bay=2.0, g_front=[("living", 1)],
         g_back=[("kitchen", 1)], u_front=[("bedroom", 1)], u_back=[("studio", 1)], roof="gable_y", roof_m="SlateDark", pitch=58, over=0.1,
         gable_m="BrickDark", cap="SlateDark", door_k="door", door_m="PlasticGreen", door_x=-1.6, side=1.8, decor=["bands"], band_m="White"),
    lambda c: ob("HoistBeam", [(-0.1, c["y1"] - 1.0, c["roof_z"] + 2.2, 0.1, c["y1"], c["roof_z"] + 2.4)], ["WoodDark"], kind="trim"))

reg(_d7_m("german_fachwerk", "德式木筋屋", "German Fachwerk House", "German Half-Timbered", "德國木筋屋", "standard", "house + shop",
          ["europe", "fantasy", "rpg-village", "christmas", "realistic"], "3-storey Fachwerk: stone shop floor, half-timbered upper floors, steep red tile roof, flower boxes."),
    dict(W=11, D=10, floors=3, ext0="Stone", ext="Plaster", frame="WoodDark", win="win", ww=1.0, ground="bakery", g_front=[("bakery", 1)],
         g_back=[("kitchen", 1)], u_front=[("living", 1), ("bedroom", 1)], u_back=[("bedroom", 1)], roof="gable", roof_m="RoofTile", pitch=52,
         over=0.4, gable_m="Plaster", door_x=-2.4, decor=["boxes", "chimney"], sign=("BÄCKEREI", "WoodDark", "Brass", 3.2)),
    lambda c: (halftimber(c, c["Z"][1], c["Z"][2]), halftimber(c, c["Z"][2], c["Z"][3])))

def _d7_falu(ctx):
    mb = MB()
    for (cx, cy) in ((ctx["x1"], ctx["y1"]), (ctx["x2"], ctx["y1"]), (ctx["x1"], ctx["y2"]), (ctx["x2"], ctx["y2"])):
        mb.box(cx - 0.12, cy - 0.12, 0, cx + 0.12, cy + 0.12, ctx["roof_z"], "White")
    mb.obj("CornerBoards", kind="trim")
reg(_d7_m("swedish_red_cottage", "瑞典法倫紅屋", "Swedish Falu-Red Cottage", "Swedish Stuga", "瑞典紅木屋", "standard", "house",
          ["europe", "cozy", "realistic", "anime", "winter"], "2-storey falu-red timber cottage with white corner boards and frames, slate gable, porch."),
    dict(W=10, D=8.6, floors=2, ext="PaintRed", int="WoodLight", frame="FrameWhite", win="win", g_front=[("living", 1), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1), ("bedroom", 1)], u_back=[("bath", 1)], roof="gable", roof_m="SlateDark", pitch=38, over=0.5, gable_m="PaintRed",
         cap="SlateDark", porch=True, porch_col="White", door_m="WoodLight", plot_m="Grass", decor=["plants"]), _d7_falu)

reg(_d7_m("iceland_turf_house", "冰島草頂屋", "Icelandic Turf House", "Icelandic Turf House", "冰島草屋", "standard", "house",
          ["fantasy", "viking", "survival", "cozy"], "Single-storey black timber house with a grass-covered gable roof, stone chimney, living room and bed nook."),
    dict(W=9, D=7, floors=1, h0=2.8, ext="WoodDark", int="WoodLight", frame="FrameWhite", win="win", ww=1.0, g_front=[("living", 1), ("bedroom", 1)],
         roof="gable_y", roof_m="Grass", pitch=40, over=0.3, gable_m="WoodDark", cap=None, door_m="PaintRed", plot_m="Grass", decor=["chimney"], chimney_m="Stone"))

reg(_d7_m("russian_izba", "俄羅斯木刻屋", "Russian Izba", "Russian Log Izba", "俄羅斯木屋", "standard", "house",
          ["fantasy", "folk-tale", "winter", "realistic"], "Log izba with carved teal window surrounds and shutters, steep plank gable, stove and bed inside."),
    dict(W=9, D=8, floors=1, h0=3.0, plinth=0.5, ext="WoodLight", int="WoodLight", frame="PaintTeal", win="win", ww=1.0, g_front=[("living", 1), ("bedroom", 1)],
         roof="gable_y", roof_m="WoodDark", pitch=45, over=0.5, gable_m="WoodLight", cap="WoodDark", door_m="WoodDark", decor=["shutters", "chimney"],
         shutter_m="PaintTeal", plot_m="Snow"), lambda c: fireplace(c["x1"] + 0.6, 0.0, 0.5, 90, "Plaster"))

reg(_d7_m("santorini_house", "聖托里尼藍頂屋", "Santorini Blue-Dome House", "Cycladic Greek", "希臘聖托里尼", "upscale", "house",
          ["summer", "romance", "realistic", "anime"], "Whitewashed cubic 2-storey house with a blue dome, blue doors and shutters, roof terrace edge."),
    dict(W=9, D=9, floors=2, ext="Plaster", frame="PlasticBlue", win="win", g_front=[("living", 1), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1)], u_back=[("bath", 1)], roof="dome", roof_m="PlasticBlue", dome_k=0.55, door_m="PlasticBlue", decor=["shutters", "plants"],
         shutter_m="PlasticBlue", plot_m="StoneTile"))

reg(_d7_m("tuscan_farmhouse", "托斯卡尼農舍", "Tuscan Farmhouse", "Tuscan Casale", "義大利托斯卡尼", "upscale", "farmhouse",
          ["europe", "romance", "farming-sim", "realistic"], "Stone 2-storey casale with a low terracotta hip roof, green shutters, cypress trees, rustic kitchen."),
    dict(W=14, D=10, floors=2, ext="Stone", frame="WoodDark", win="win", g_front=[("living", 1), ("kitchen", 1)], g_back=[("dining", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1), ("bedroom", 1)], u_back=[("bedroom", 1), ("bath", 0.6)], roof="hip", roof_m="RoofTile", pitch=20, over=0.6,
         door_m="WoodDark", decor=["shutters", "chimney"], shutter_m="PlasticGreen", plot_m="Grass"),
    lambda c: [tree(c["x1"] - 1.6 + i * 0.0, c["y1"] - 1.5 - i * 2.0, 0, 1.1, "pine", seed=720 + i) for i in range(3)])

def _d7_chateau(ctx):
    for (cx, cy) in ((ctx["x1"], ctx["y1"]), (ctx["x2"], ctx["y1"])):
        mb = MB(); mb.cyl(0, 0, 0, ctx["roof_z"] + 1.0, 1.6, "BrickCream", seg=16)
        mb.cyl(0, 0, ctx["roof_z"] + 1.0, ctx["roof_z"] + 5.5, 1.9, "SlateBlue", seg=16, r2=0.05)
        for z in (3.5, 7.0):
            mb.box(-0.3, -1.62, z, 0.3, -1.58, z + 1.3, "Glass")
        mb.obj("Turret_%d" % int(cx), cx, cy, 0, kind="structure")
    ctx["top"] = ctx["roof_z"] + 5.5
reg(_d7_m("loire_chateau", "羅亞爾小城堡", "Loire Petit Château", "French Château", "法式城堡", "luxury", "mansion",
          ["europe", "romance", "fantasy", "mystery", "otome"], "3-storey cream château with slate mansard + dormers and two conical corner turrets, grand salon and bedrooms."),
    dict(W=18, D=12, floors=3, h0=4.0, h=3.4, plinth=0.6, ext="BrickCream", frame="FrameWhite", win="win", ww=1.2, head=2.8,
         g_front=[("lounge", 1), ("dining", 1), ("library", 1)], g_back=[("kitchen", 1), ("bath", 0.5)], u_front=[("bedroom", 1)] * 3,
         u_back=[("bedroom", 1), ("bath", 0.6)], floor0="Parquet", roof="mansard", roof_m="SlateBlue", door_k="door_double", door_m="WoodDark",
         door_w=1.6, door_x=0.0, decor=["cornice", "bands", "quoins"], band_m="Stone", side=4.0, plot_m="Cobble"), _d7_chateau)

reg(_d7_m("english_cottage", "英式茅草小屋", "English Thatched Cottage", "English Country Cottage", "英式鄉村小屋", "standard", "cottage",
          ["cozy", "europe", "farming-sim", "anime", "ghibli"], "2-storey whitewashed cottage with a thick thatch gable, flower boxes, picket fence and garden path."),
    dict(W=9, D=8.6, floors=2, h0=3.0, h=2.8, ext="Plaster", frame="WoodDark", win="win", ww=1.0, g_front=[("living", 1)], g_back=[("kitchen", 1)],
         u_front=[("bedroom", 1)], u_back=[("bath", 1)], roof="gable", roof_m="Bark", pitch=50, over=0.6, gable_m="Plaster", cap="Bark",
         door_m="PlasticBlue", decor=["boxes", "chimney"], front=5.0, plot_m="Grass"), lambda c: _d7_fence(c, "White", 3.6))

reg(_d7_m("scottish_stone_house", "蘇格蘭石屋", "Highland Stone House", "Scottish Stone House", "蘇格蘭石屋", "standard", "house",
          ["europe", "realistic", "mystery", "fantasy"], "2-storey granite house with slate gable and twin end chimneys, deep-set windows, cosy hearth."),
    dict(W=10, D=8.6, floors=2, ext="Stone", int="Plaster", frame="FrameWhite", win="win", ww=1.0, g_front=[("living", 1), ("dining", 1)],
         g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("bedroom", 1), ("bedroom", 1)], u_back=[("bath", 1)], roof="gable", roof_m="SlateDark",
         pitch=42, over=0.2, gable_m="Stone", cap="SlateDark", door_m="PaintRed", plot_m="Grass"),
    lambda c: [ob("EndChimney%d" % i, [(x - 0.45, -0.5, c["roof_z"] - 0.5, x + 0.45, 0.5, c["top"] + 0.8)], ["Stone"], kind="trim") for i, x in enumerate((c["x1"] + 0.45, c["x2"] - 0.45))])

reg(_d7_m("irish_pub", "奧馬利愛爾蘭酒吧", "O'Malley's Irish Pub", "Irish Pub", "愛爾蘭酒吧", "standard", "pub",
          ["europe", "realistic", "slice-of-life", "crime"], "2-storey pub with a dark green timber shopfront, gold lettering, hanging baskets; bar downstairs, function room upstairs."),
    dict(W=10, D=10, floors=2, ext0="WoodDark", ext="Plaster", frame="WoodDark", win="win3", ground="bar", g_front=[("bar", 1)], g_back=[("kitchen", 1)],
         u_front=[("lounge", 1)], u_back=[("bath", 1)], shop_k="win3", shop_frame="WoodDark", door_x=-2.0, roof="flat", decor=["cornice", "lanterns"],
         sign=("O'MALLEY'S  PUB", "PlasticGreen", "Brass", 5.0)))

reg(_d7_m("lisbon_tile_house", "里斯本磁磚屋", "Lisbon Azulejo House", "Portuguese Azulejo", "葡萄牙磁磚屋", "standard", "townhouse",
          ["europe", "summer", "realistic", "romance"], "3-storey townhouse clad in blue azulejo tiles, wrought-iron balconies, red tile gable."),
    dict(W=8, D=11, floors=3, ext="TileBlue", frame="FrameWhite", win="win", ww=1.1, g_front=[("living", 1)], g_back=[("kitchen", 1)],
         u_front=[("bedroom", 1)], u_back=[("studio", 1)], balcony="front", balc_rail="bar", roof="gable", roof_m="RoofTile", pitch=28, over=0.4,
         gable_m="TileBlue", door_m="WoodDark", decor=["bands", "cornice"], band_m="Stone"))

reg(_d7_m("spanish_plaza_house", "西班牙廣場拱廊屋", "Spanish Plaza Arcade House", "Andalusian Arcade House", "西班牙拱廊屋", "standard", "house + shop",
          ["europe", "summer", "western", "realistic"], "2-storey white stucco house with a ground-floor arcade, iron balconies, terracotta hip roof."),
    dict(W=12, D=10, floors=2, ext="Plaster", frame="WoodDark", win="win", ground="cafe", g_front=[("cafe", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1), ("living", 1)], u_back=[("bedroom", 1)], balcony="front", roof="hip", roof_m="RoofTile", pitch=22, over=0.5,
         door_x=0.0, shop_frame="WoodDark", decor=["plants", "lanterns"], sign=("CAFÉ  LA PLAZA", "WoodDark", "LabelGlow", 4.0)))

reg(_d7_m("american_colonial", "美式殖民宅", "New England Colonial", "American Colonial", "美式殖民", "upscale", "house",
          ["realistic", "horror", "sitcom", "americana"], "Symmetric 2-storey white clapboard house: columned portico, black shutters, slate gable, twin chimneys, picket fence."),
    dict(W=14, D=10, floors=2, ext="SidingWhite", frame="FrameWhite", win="win", g_front=[("living", 1), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1), ("bedroom", 1)], u_back=[("bedroom", 1), ("bath", 0.6)], roof="gable", roof_m="SlateDark", pitch=34, over=0.4,
         gable_m="SidingWhite", cap="SlateDark", porch=True, porch_col="White", porch_w=3.4, door_k="door_double", door_m="Black", door_w=1.4,
         door_x=0.0, decor=["shutters", "chimney"], shutter_m="Black", front=6.0, plot_m="Grass"), lambda c: _d7_fence(c, "White", 5.2))

def _d7_silo(ctx):
    mb = MB(); mb.cyl(0, 0, 0, 9.0, 2.0, "PanelSteel", seg=24); dome_ = None
    mb.cyl(0, 0, 9.0, 10.2, 2.05, "Metal", seg=24, r2=0.3); mb.obj("Silo", ctx["x2"] + 2.6, ctx["y2"] - 2.2, 0, kind="structure")
    for i in range(6):
        crate(ctx["x1"] - 1.0, ctx["y1"] + 1.0 + i * 0.8, 0, 10 * i, 0.7, "Bark")
reg(_d7_m("red_barn", "美式紅穀倉", "Red Prairie Barn", "American Barn", "美式穀倉", "budget", "barn",
          ["farming-sim", "western", "horror", "americana"], "Big red gambrel barn: tractor/garage bay and workshop with roller door, hay loft above, steel grain silo."),
    dict(W=14, D=12, floors=2, h0=4.2, h=3.0, ext="PaintRed", int="WoodLight", frame="FrameWhite", win="win", ww=1.0, g_front=[("garage", 1), ("workshop", 1)],
         g_back=[("storage", 1), ("bath", 0.6)], u_front=[("storage", 1)], u_back=[("storage", 1)], roof="gambrel", roof_m="SlateDark", gable_m="PaintRed",
         s_ops0=[(-6.0, -0.8, 0, 3.6, "roller")], door_x=3.0, door_k="door", door_m="WoodDark", side=5.0, plot_m="Grass"), _d7_silo)

def _d7_saloon(ctx):
    false_front(ctx, "WoodLight", 2.4, "SALOON", "NeonYellow")
    for i in range(4):
        barrel(ctx["x1"] + 0.6 + i * 0.7, ctx["y1"] - 1.2, 0, 0, "WoodLight")
    mb = MB(); mb.box(-2.0, -0.05, 0.9, 2.0, 0.05, 1.0, "WoodDark"); mb.box(-1.9, -0.05, 0, -1.8, 0.05, 1.0, "WoodDark"); mb.box(1.8, -0.05, 0, 1.9, 0.05, 1.0, "WoodDark")
    furn("HitchingRail", mb, ctx["x2"] - 2.5, ctx["y1"] - 2.5, 0, 0)
reg(_d7_m("western_saloon", "荒野西部酒館", "Dusty Spur Saloon", "Wild West Saloon", "西部酒館", "budget", "saloon",
          ["western", "realistic", "cartoon", "rpg"], "2-storey timber saloon with false front, swinging doors, bar, card tables, rooms upstairs off a wooden balcony."),
    dict(W=12, D=11, floors=2, ext="WoodLight", int="WoodDark", frame="WoodDark", win="win", ground="bar", g_front=[("bar", 1), ("restaurant", 1)],
         g_back=[("storage", 1)], u_front=[("hotel", 1), ("hotel", 1)], u_back=[("hotel", 1)], balcony="front", balc_rail="wood", balc_floor="WoodLight",
         shop_k="win", shop_frame="WoodDark", door_k="door_double", door_m="WoodDark", door_x=0.0, roof="flat", plot_m="Sand"), _d7_saloon)

reg(_d7_m("sheriff_office", "警長辦公室", "Sheriff's Office", "Wild West Jailhouse", "西部警長屋", "budget", "jail",
          ["western", "cartoon", "rpg", "realistic"], "Single-storey timber sheriff's office with false front, desk and a barred cell."),
    dict(W=9, D=8, floors=1, h0=3.2, ext="WoodDark", int="WoodLight", frame="WoodDark", win="grille", g_front=[("office", 1), ("storage", 0.7)],
         door_m="WoodLight", roof="flat", parapet=0.2, plot_m="Sand"), lambda c: false_front(c, "WoodDark", 1.8, "SHERIFF", "Brass"))

reg(_d7_m("malibu_beach_house", "馬里布海灘屋", "Malibu Beach House", "California Beach House", "加州海灘屋", "luxury", "beach house",
          ["summer", "realistic", "gta-like", "modern"], "Raised 2-storey white beach house: full-height glass, wraparound balcony, shed roof, surfboards."),
    dict(W=12, D=10, floors=2, plinth=1.0, ext="SidingWhite", frame="FrameAlu", win="shop", sill=0.1, head=2.8, ww=2.6, g_front=[("living", 1.4), ("kitchen", 1)],
         g_back=[("bedroom", 1), ("bath", 0.6)], u_front=[("bedroom", 1), ("lounge", 1)], u_back=[("bath", 1)], balcony="front", balc_rail="glass",
         balc_floor="WoodLight", roof="shed", roof_m="WoodLight", pitch=8, over=1.0, door_k="door_glass", plot_m="Sand"),
    lambda c: [ob("Surfboard%d" % i, [(c["x2"] + 0.3, c["y1"] + 0.6 + i * 0.5, 0.0, c["x2"] + 0.38, c["y1"] + 1.0 + i * 0.5, 2.2)], [["PlasticYellow", "PlasticBlue", "PaintRed"][i]], kind="trim") for i in range(3)])

reg(_d7_m("nola_iron_balcony", "紐奧良鐵花陽台屋", "New Orleans Gallery House", "French Quarter Creole", "紐奧良法國區", "standard", "townhouse",
          ["noir", "jazz-age", "realistic", "horror"], "3-storey Creole townhouse wrapped in lacy cast-iron galleries, tall shuttered French doors, jazz bar downstairs."),
    dict(W=10, D=11, floors=3, ext="MosaicPink", frame="FrameWhite", win="win", ww=1.0, head=2.6, ground="bar", g_front=[("bar", 1)], g_back=[("kitchen", 1)],
         u_front=[("living", 1), ("bedroom", 1)], u_back=[("bedroom", 1)], balcony="front", balc_rail="bar", balc_plants=True, roof="flat",
         decor=["shutters", "cornice"], shutter_m="PlasticGreen", band_m="White", door_x=-2.4, sign=("JAZZ  BAR", "Black", "NeonBlue", 3.4)))

def _d7_lady(ctx):
    bay_window("Bay1", "S", ctx["x1"] + 0.6, ctx["x1"] + 3.0, ctx["Z"][1] + 0.8, ctx["Z"][1] + 2.5, ctx["y1"] - 0.03, 0.6, "FrameWhite", "SlateDark", base="SidingTeal")
reg(_d7_m("sf_painted_lady", "舊金山彩繪淑女屋", "San Francisco Painted Lady", "Victorian Painted Lady", "維多利亞彩屋", "upscale", "townhouse",
          ["realistic", "sitcom", "romance", "americana"], "3-storey Victorian with teal clapboard, white trim, bay window, steep front gable, stoop."),
    dict(W=7, D=12, floors=3, plinth=1.2, ext="SidingTeal", frame="FrameWhite", win="win", ww=1.0, g_front=[("living", 1)], g_back=[("kitchen", 1)],
         u_front=[("bedroom", 1)], u_back=[("bath", 1)], roof="gable_y", roof_m="SlateDark", pitch=48, over=0.3, gable_m="SidingTeal",
         door_m="PaintRed", door_x=1.6, decor=["cornice", "bands"], band_m="White", side=1.8), _d7_lady)

def _d7_mex(ctx):
    zr = ctx["roof_z"]
    for k in range(3):
        cable("Bunting%d" % k, (ctx["x1"] + 0.3, ctx["y1"] + 1 + k * 2.5, zr + 2.0), (ctx["x2"] - 0.3, ctx["y1"] + 1 + k * 2.5, zr + 2.0), 0.3)
        for i in range(10):
            x = ctx["x1"] + 0.8 + i * (ctx["W"] - 1.6) / 9
            ob("Flag%d_%d" % (k, i), [(x - 0.12, ctx["y1"] + 1 + k * 2.5, zr + 1.55, x + 0.12, ctx["y1"] + 1.01 + k * 2.5, zr + 1.85)],
               [RNG.choice(["PlasticRed", "PlasticYellow", "PlasticBlue", "PlasticGreen", "NeonPink"])], kind="trim")
reg(_d7_m("mexico_casa", "墨西哥彩色屋", "Casa Colorida", "Mexican Colonial", "墨西哥彩屋", "standard", "house",
          ["summer", "cartoon", "realistic", "coco-like"], "2-storey saturated red casa with blue door, roof terrace strung with papel picado bunting."),
    dict(W=9, D=9.5, floors=2, ext="PaintRed", frame="PlasticYellow", win="win", ww=1.1, g_front=[("living", 1)], g_back=[("kitchen", 1)],
         u_front=[("bedroom", 1)], u_back=[("bath", 1)], roof="terrace", parapet=0.8, door_m="PlasticBlue", decor=["plants", "boxes"], plot_m="Sand"), _d7_mex)

reg(_d7_m("favela_stack", "里約彩色堆疊屋", "Rio Hillside Stack", "Brazilian Favela Block", "巴西彩色堆疊屋", "budget", "apartment",
          ["realistic", "action", "urban-survival", "gta-like"], "4-storey self-built stack: every floor a different colour, rebar on the roof, AC units, tangled cables."),
    dict(W=8, D=10, floors=4, ext_f=["Brick", "PaintTeal", "PlasticYellow", "MosaicPink"], frame="Frame", win="win", g_front=[("living", 1)],
         g_back=[("kitchen", 1)], u_front=[("living", 1)], u_back=[("bedroom", 1)], roof="terrace", decor=["ac", "pipes", "antenna"], door_x=-2.0),
    lambda c: [cable("Tangle%d" % i, (c["x1"], c["y1"] + 0.5, 4.0 + i * 1.6), (c["x1"] - 5.0, c["y1"] - 4.0 - i, 5.5), 0.8) for i in range(5)])

reg(_d7_m("canadian_lodge", "加拿大木屋旅館", "Canadian Timber Lodge", "Canadian Log Lodge", "加拿大木屋", "upscale", "lodge",
          ["winter", "cozy", "survival", "realistic"], "2-storey log lodge: lobby with stone fireplace and restaurant, guest rooms above, deep timber gable."),
    dict(W=16, D=11, floors=2, ext="WoodLight", int="WoodLight", frame="WoodDark", win="win3", ground="lobby", g_front=[("lobby", 1), ("restaurant", 1)],
         g_back=[("kitchen", 1), ("bath", 0.6)], u_front=[("hotel", 1)] * 3, u_back=[("hotel", 1), ("bath", 0.6)], roof="gable", roof_m="WoodDark",
         pitch=35, over=0.8, gable_m="WoodLight", cap="WoodDark", door_k="door_double", door_m="WoodDark", door_x=-3.0, decor=["chimney"], chimney_m="Stone",
         plot_m="Snow", sign=("MAPLE LODGE", "WoodDark", "LabelGlow", 4.0)))

reg(_d7_m("lucky7_casino", "幸運7賭場", "Lucky 7 Casino", "Las Vegas Casino", "拉斯維加斯賭場", "luxury", "casino",
          ["crime", "heist", "gta-like", "neon", "retro"], "2-storey black-and-gold casino: gaming floor of machines, bar and lounge, upstairs VIP room, huge neon marquee."),
    dict(W=18, D=14, floors=2, h0=4.6, ext="PanelDark", int="CarpetRed", frame="Brass", ground="arcade", g_front=[("arcade", 1), ("bar", 1)],
         g_back=[("bank", 1), ("bath", 0.6)], u_front=[("lounge", 1), ("bar", 1)], u_back=[("office", 1)], floor0="CarpetRed", floor="CarpetRed",
         door_x=-3.0, door_w=2.0, roof="flat", decor=["cornice"], band_m="Brass", sign=("LUCKY 7  CASINO", "Black", "NeonYellow", 9.0), sign_x=0.0),
    lambda c: ob("Marquee", [(c["x1"] - 0.2, c["y1"] - 0.25, c["Z"][1] - 0.2, c["x2"] + 0.2, c["y1"] - 0.1, c["Z"][1]),
                              (c["x1"] - 0.2, c["y1"] - 0.25, c["roof_z"] - 0.3, c["x2"] + 0.2, c["y1"] - 0.1, c["roof_z"] - 0.1)], ["NeonPink"], kind="light_fixture"))

def _d7_escape(ctx):
    mb = MB(); x0, x1 = ctx["x2"] - 4.2, ctx["x2"] - 0.6; y0 = ctx["y1"] - 1.2
    for zz in ctx["Z"][1:-1]:
        mb.box(x0, y0, zz - 0.06, x1, ctx["y1"] - 0.03, zz, "MetalDark")
        for i in range(int((x1 - x0) / 0.15)):
            mb.box(x0 + i * 0.15, y0, zz, x0 + i * 0.15 + 0.02, y0 + 0.02, zz + 1.0, "MetalDark")
        mb.box(x0, y0, zz + 0.98, x1, y0 + 0.04, zz + 1.02, "MetalDark")
    mb.obj("FireEscape", kind="railing")
    for k, zz in enumerate(ctx["Z"][1:-2]):
        stair("EscStair%d" % k, x1 - 0.5 if k % 2 == 0 else x0 + 0.5, y0 + 0.5, zz, zz + (ctx["Z"][2] - ctx["Z"][1]), "+x" if k % 2 else "-x", 0.7, 0.25, "MetalDark",
              rails="none") if False else None
reg(_d7_m("chicago_walkup", "芝加哥紅磚公寓", "Chicago Brick Three-Flat", "Chicago Greystone/Brick Flat", "芝加哥公寓", "standard", "apartment",
          ["noir", "crime", "realistic", "americana"], "4-storey red-brick walk-up with black steel fire-escape balconies, cornice, one flat per floor."),
    dict(W=12, D=12, floors=4, ext="Brick", frame="FrameWhite", win="win", g_front=[("living", 1), ("bedroom", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("living", 1), ("bedroom", 1)], u_back=[("kitchen", 1), ("bath", 0.6)], roof="flat", decor=["cornice", "bands", "tank"], band_m="Stone",
         door_x=-3.0, door_k="door", door_m="WoodDark"), _d7_escape)
