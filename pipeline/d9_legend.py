# District 9 — fantasy / myth / world landmarks (25). Names prefixed _d9_.

def _d9_m(i, zh, en, st, stz, tier, cat, gs, desc):
    return (i, zh, en, st, stz, tier, cat, gs, desc)

def _d9_towers(ctx, r=1.6, cone="SlateBlue", m="Stone", extra_h=1.5):
    for (cx, cy) in ((ctx["x1"], ctx["y1"]), (ctx["x2"], ctx["y1"])):
        mb = MB(); mb.cyl(0, 0, 0, ctx["roof_z"] + extra_h, r, m, seg=16)
        mb.cyl(0, 0, ctx["roof_z"] + extra_h, ctx["roof_z"] + extra_h + r * 2.8, r + 0.3, cone, seg=16, r2=0.05)
        for z in (3.0, 6.5, 10.0):
            if z < ctx["roof_z"]:
                mb.box(-0.25, -r - 0.02, z, 0.25, -r + 0.02, z + 1.2, "GlassBlue")
        mb.obj("Tower_%d" % int(cx * 10), cx, cy, 0, kind="structure")
    ctx["top"] = max(ctx["top"], ctx["roof_z"] + extra_h + r * 2.8)

reg(_d9_m("dwarf_stonehall", "矮人石廳", "Dwarven Stonehall", "Dwarven Hall", "矮人石屋", "standard", "forge hall",
          ["fantasy", "rpg", "medieval", "dnd"], "Squat granite hall with a heavy round door, runic lanterns, forge and anvil inside, low stone roof."),
    dict(W=10, D=9, floors=1, h0=3.4, plinth=0.6, ext="Stone", int="Stone", frame="Brass", win="grille", ww=0.8, g_front=[("forge", 1), ("dining", 0.8)],
         floor0="StoneTile", roof="hip", roof_m="SlateDark", pitch=18, over=0.4, door_k="door_double", door_m="WoodDark", door_x=0.0,
         plot_m="Cobble", decor=["lanterns"]), lambda c: round_door(0.0, c["y1"] - 0.08, c["Z"][0], 1.25, "WoodDark", "Stone"))

def _d9_hobbit(ctx):
    dome("Mound", 0.0, 2.6, 0.0, max(ctx["W"], ctx["D"]) * 0.7, "Grass", 0.42, seg=40)
    round_door(0.0, ctx["y1"] - 0.15, 0.05, 1.1, "PlasticGreen", "WoodLight")
    for x in (-2.6, 2.6):
        mb = MB(); mb.cyl(0, -0.05, 0, 0, 0.55, "WoodLight", seg=20, axis="y"); mb.cyl(0, -0.08, 0, 0, 0.45, "Glass", seg=20, axis="y")
        mb.obj("RoundWin_%d" % int(x * 10), x, ctx["y1"] - 0.2, 1.4, kind="window")
    ctx["top"] = max(ctx["W"], ctx["D"]) * 0.3 + 1.0
reg(_d9_m("hobbit_hole", "哈比山丘洞屋", "Hillside Smial", "Halfling Hill House", "哈比洞屋", "standard", "house",
          ["fantasy", "cozy", "ghibli", "rpg-village"], "Home dug into a grassy mound: round green door, round windows, cosy living room, pantry and bedroom."),
    dict(W=9, D=8, floors=1, h0=2.6, ext="Plaster", int="WoodLight", frame="WoodLight", win="win", side_windows=False, g_front=[("living", 1), ("bedroom", 1)],
         floor0="WoodFloor", roof="flat", parapet=0.1, door_k="door", door_m="PlasticGreen", door_x=0.0, front=5.0, side=4.0, plot_m="Grass"), _d9_hobbit)

def _d9_witch(ctx):
    mb = MB(); mb.cyl(0, 0, 0, 0.7, 0.55, "MetalDark", seg=16, r2=0.45); mb.cyl(0, 0, 0.55, 0.62, 0.48, "NeonGreen", seg=16)
    furn("Cauldron", mb, 0.0, 0.5, 0, 0, "cook")
    pipe_run("CrookedChimney", [(ctx["x2"] - 1.0, 1.0, ctx["roof_z"]), (ctx["x2"] - 0.8, 1.0, ctx["top"] + 0.4), (ctx["x2"] - 0.4, 1.3, ctx["top"] + 1.4)], 0.3, "BrickDark")
    lamp("WitchGlow", 0.0, 0.5, 1.4, 50, (0.4, 1.0, 0.3), kind="point", fixture=False)
    tree(ctx["x1"] - 2.0, ctx["y1"] - 1.5, 0, 0.8, "broad", seed=901)
reg(_d9_m("witch_cottage", "林間女巫小屋", "Witch's Woodland Cottage", "Storybook Witch Cottage", "女巫小屋", "budget", "cottage",
          ["fantasy", "horror", "ghibli", "halloween"], "Tiny dark timber cottage with a needle-steep roof, crooked chimney, bubbling green cauldron, herb shelves."),
    dict(W=7, D=7, floors=1, h0=2.8, ext="WoodDark", int="WoodDark", frame="PaintTeal", win="win", ww=0.9, g_front=[("shop", 1)], roof="gable_y",
         roof_m="SlateDark", pitch=62, over=0.5, gable_m="WoodDark", cap="SlateDark", door_m="PaintTeal", door_x=1.2, plot_m="Grass"), _d9_witch)

reg(_d9_m("mage_academy", "星輝魔法學院", "Astral Mage Academy", "Fantasy Magic Academy", "魔法學院", "landmark", "academy",
          ["fantasy", "anime", "magic-school", "rpg"], "3-storey stone academy: lecture halls, grand library, slate gable, twin conical towers flanking the front."),
    dict(W=20, D=14, floors=3, h0=4.0, h=3.6, plinth=0.8, ext="Stone", int="Plaster", frame="WoodDark", win="win", ww=1.1, head=3.0,
         g_front=[("classroom", 1), ("lobby", 0.8), ("library", 1)], g_back=[("library", 1), ("bath", 0.5)], u_front=[("classroom", 1), ("library", 1), ("classroom", 1)],
         u_back=[("bedroom", 1), ("bath", 0.5)], floor="CarpetRed", roof="gable", roof_m="SlateBlue", pitch=40, over=0.4, gable_m="Stone", cap="SlateDark",
         door_k="door_double", door_m="WoodDark", door_w=1.8, door_x=0.0, decor=["lanterns"], side=4.0), lambda c: _d9_towers(c, 1.8))

reg(_d9_m("blacksmith_forge", "鐵匠鋪", "Ironhand Blacksmith", "Medieval Blacksmith", "鐵匠鋪", "budget", "forge",
          ["medieval", "fantasy", "rpg", "survival"], "Stone forge with half-timber gable: furnace, anvil, workbench and an open front for customers."),
    dict(W=10, D=8, floors=1, h0=3.4, ext="Stone", int="Stone", frame="WoodDark", win="win", g_front=[("forge", 1)], floor0="StoneTile",
         s_ops0=[(-4.6, 1.8, 0, 2.8, "open")], door_x=3.4, door_w=0.9, door_m="WoodDark", roof="gable", roof_m="SlateDark", pitch=38, over=0.6,
         gable_m="Plaster", cap="SlateDark", plot_m="Cobble", decor=["chimney"], chimney_m="Stone"),
    lambda c: sign_board("Anvil", "鐵匠 SMITH", c["x2"] + 0.5, c["y1"] - 0.7, 2.6, 1.2, 0.5, 90, "WoodDark", "Brass", 0.24))

def _d9_barracks(ctx):
    x1, x2, y1, y2 = ctx["x1"], ctx["x2"], ctx["y1"], ctx["y2"]
    crenellate("Merlons", [Vector((x1, y1, 0)), Vector((x2, y1, 0)), Vector((x2, y2, 0)), Vector((x1, y2, 0))], ctx["roof_z"] + 1.0, 0.7, 0.6, 0.4, "Stone")
    for i, x in enumerate((-4.0, 0.0, 4.0)):
        mb = MB(); mb.box(-0.05, -0.02, 0, 0.05, 0.02, 2.6, "MetalDark"); mb.box(0.05, -0.01, 1.2, 1.0, 0.01, 2.6, ["PaintRed", "PlasticBlue", "PaintRed"][i])
        mb.obj("Banner%d" % i, x, y1 - 0.25, ctx["roof_z"] + 1.0, kind="trim")
    for i in range(4):
        mb = MB(); mb.cyl(0, 0, 0, 1.6, 0.05, "WoodDark", seg=8); mb.cyl(0, 0, 1.0, 1.6, 0.3, "Bark", seg=10); furn("TrainingDummy", mb, -6.0 + i * 1.6, y1 - 3.5, 0, 0, "use")
reg(_d9_m("knight_barracks", "騎士兵營", "Knights' Barracks", "Medieval Barracks", "騎士兵營", "civic", "barracks",
          ["medieval", "fantasy", "strategy", "rpg"], "2-storey stone barracks with crenellated roof walk and banners: mess hall, armoury, bunk rooms, training yard with dummies."),
    dict(W=16, D=10, floors=2, h0=3.6, ext="Stone", int="Stone", frame="Frame", win="win", ww=0.6, sill=1.2, g_front=[("dining", 1), ("workshop", 1)],
         g_back=[("storage", 1)], u_front=[("dorm", 1), ("dorm", 1)], u_back=[("dorm", 1)], floor0="StoneTile", roof="terrace", parapet=1.0, parapet_m="Stone",
         door_k="door_double", door_m="WoodDark", door_x=-2.0, front=6.0, plot_m="Cobble"), _d9_barracks)

def _d9_potion(ctx):
    halftimber(ctx, ctx["Z"][1], ctx["Z"][2])
    for i in range(12):
        mb = MB(); mb.sph(0, 0, 0.12, 0.1, RNG.choice(["NeonGreen", "NeonPurple", "NeonPink", "NeonCyan"])); mb.cyl(0, 0, 0.2, 0.3, 0.03, "Glass", seg=8)
        furn("Potion", mb, ctx["x1"] + 0.6 + (i % 6) * 0.3, ctx["y1"] - 0.25, 1.1 + (i // 6) * 0.35, 0)
    ob("PotionShelf", [(ctx["x1"] + 0.4, ctx["y1"] - 0.4, 1.05, ctx["x1"] + 2.4, ctx["y1"] - 0.1, 1.1), (ctx["x1"] + 0.4, ctx["y1"] - 0.4, 1.4, ctx["x1"] + 2.4, ctx["y1"] - 0.1, 1.45)],
       ["WoodDark"], kind="furniture")
reg(_d9_m("potion_shop", "月影藥水店", "Moonshade Potion Shop", "Fantasy Apothecary", "藥水店", "standard", "shop",
          ["fantasy", "rpg", "anime", "cozy"], "Crooked 2-storey half-timbered apothecary: glowing potion displays outside and in, alchemist's flat upstairs."),
    dict(W=7, D=9, floors=2, ext0="Stone", ext="Plaster", frame="WoodDark", win="win", ww=1.0, ground="shop", g_front=[("shop", 1)], g_back=[("storage", 1)],
         u_front=[("studio", 1)], u_back=[("bedroom", 1)], door_x=1.4, shop_k="win3", shop_frame="WoodDark", roof="gable_y", roof_m="SlateDark", pitch=50,
         over=0.4, gable_m="Plaster", cap="SlateDark", sign=("POTIONS 藥水", "WoodDark", "NeonPurple", 2.8), sign_x=1.4), _d9_potion)

def _d9_guild(ctx):
    halftimber(ctx, ctx["Z"][1], ctx["Z"][3])
    mb = MB(); mb.box(-1.0, -0.05, 0, 1.0, 0.05, 1.4, "WoodDark")
    for i in range(6):
        mb.box(-0.9 + (i % 3) * 0.6, -0.06, 0.15 + (i // 3) * 0.65, -0.5 + (i % 3) * 0.6, -0.05, 0.6 + (i // 3) * 0.65, "Paper")
    furn("QuestBoard", mb, ctx["x2"] - 1.6, ctx["y1"] - 0.6, 0.8, 0, "use")
reg(_d9_m("adventurers_guild", "冒險者公會", "Adventurers' Guild Hall", "Fantasy Guild Hall", "冒險者公會", "landmark", "guild",
          ["fantasy", "rpg", "anime", "isekai", "dnd"], "3-storey stone-and-timber guild: tavern hall with quest board, guild office, upstairs dormitory and library."),
    dict(W=16, D=12, floors=3, h0=4.0, h=3.2, ext0="Stone", ext="Plaster", frame="WoodDark", win="win", g_front=[("bar", 1.4), ("lounge", 1)],
         g_back=[("kitchen", 1), ("bath", 0.5)], u_front=[("office", 1), ("library", 1)], u_back=[("dorm", 1), ("bath", 0.5)], floor0="StoneTile",
         shop_k="win3", shop_frame="WoodDark", door_k="door_double", door_m="WoodDark", door_x=-1.0, roof="gable", roof_m="SlateDark", pitch=45, over=0.5,
         gable_m="Plaster", cap="SlateDark", decor=["lanterns", "chimney"], sign=("冒險者公會  GUILD", "WoodDark", "Brass", 5.0)), _d9_guild)

def _d9_alch():
    meta = _d9_m("alchemy_tower", "翠焰煉金塔", "Emerald Alchemy Tower", "Alchemist Tower", "煉金塔", "landmark", "tower",
                 ["fantasy", "steampunk", "rpg", "magic-school"], "8-sided dark-brick tower with a copper cone: brewing floors with green-glowing flasks, spiral stair, observatory top.")
    def furnish(f, z, r):
        mb = MB(); mb.box(-0.6, -0.3, 0, 0.6, 0.3, 0.85, "WoodDark")
        for j in range(4):
            mb.cyl(-0.4 + j * 0.27, 0, 0.85, 1.15, 0.06, RNG.choice(["NeonGreen", "GlassBlue", "NeonGreen"]), seg=10)
        furn("Bench", mb, 1.7, -1.3, z, 30, "use")
        if f == 0:
            mb = MB(); mb.cyl(0, 0, 0, 0.8, 0.5, "MetalDark", seg=16, r2=0.4); mb.cyl(0, 0, 0.7, 0.8, 0.42, "NeonGreen", seg=16)
            furn("Cauldron", mb, -1.6, 1.4, z, 0, "cook")
        lamp("AlchGlow%d" % f, 1.7, -1.3, z + 1.3, 30, (0.4, 1.0, 0.4), kind="point", fixture=False)
    ctx = _d5_round(meta, 8, 3.6, 4, 3.2, "BrickDark", "Plaster", roof="cone", roof_m="PanelCopper", roof_h=5.0, hole_r=1.2, furnish=furnish, plot_m="Cobble")
    finish_std(ctx)
regx(("alchemy_tower",), _d9_alch, 14.0, 9.0, 7.0)

def _d9_goth(ctx):
    for i in range(int(ctx["W"] / 0.5)):
        x = ctx["x1"] + 0.25 + i * 0.5
        mb = MB(); mb.cyl(0, 0, 0, 1.4, 0.02, "Black", seg=6); mb.cyl(0, 0, 1.4, 1.6, 0.05, "Black", seg=6, r2=0.0)
        mb.obj("Spike%d" % i, x, ctx["y1"] - 4.0, 0, kind="railing")
    lamp("RedWindowGlow", 0.0, ctx["y1"] + 1.0, ctx["Z"][2] + 1.5, 60, (1.0, 0.1, 0.1), kind="point", fixture=False)
    tree(ctx["x2"] + 2.0, ctx["y1"] - 2.0, 0, 1.0, "pine", seed=930)
reg(_d9_m("gothic_manor", "血月哥德莊園", "Bloodmoon Gothic Manor", "Gothic Revival Manor", "哥德莊園", "luxury", "mansion",
          ["horror", "gothic", "vampire", "mystery", "otome"], "3-storey black-brick manor: tall lancet windows, steep slate mansard with dormers, iron spike fence, red-lit windows."),
    dict(W=14, D=11, floors=3, h0=4.0, h=3.6, plinth=1.0, ext="BrickDark", int="PlasterInt", frame="Black", win="win", ww=0.9, sill=1.0, head=3.2,
         g_front=[("lounge", 1), ("dining", 1)], g_back=[("library", 1), ("bath", 0.6)], u_front=[("bedroom", 1), ("library", 1)], u_back=[("bedroom", 1), ("bath", 0.6)],
         floor0="CarpetRed", floor="CarpetRed", roof="mansard", roof_m="SlateDark", door_k="door_double", door_m="Black", door_w=1.6, door_x=0.0,
         decor=["cornice", "chimney"], band_m="Stone", chimney_m="BrickDark", front=5.5, plot_m="Grass"), _d9_goth)

def _d9_haunt(ctx):
    mb = MB()
    for i, (x, z, a) in enumerate(((-2.4, 1.2, 0.3), (2.2, 4.6, -0.4), (-1.0, 4.9, 0.6))):
        b = MB(); b.box(-0.8, -0.03, -0.1, 0.8, 0.03, 0.1, "WoodLight"); o = b.obj("BoardUp%d" % i, x, ctx["y1"] - 0.08, z, kind="trim"); o.rotation_euler.y = a
    tree(ctx["x1"] - 2.0, ctx["y1"] - 2.0, 0, 1.2, "broad", seed=940)
    lamp("GhostLight", 0.0, ctx["y1"] + 2.0, 4.5, 30, (0.6, 0.8, 1.0), kind="point", fixture=False)
reg(_d9_m("haunted_house", "荒山鬼屋", "Hollow Hill Haunted House", "Haunted Victorian", "鬼屋", "budget", "house",
          ["horror", "halloween", "mystery", "zombie"], "Decaying 2-storey timber house: boarded-up windows, rusted tin gable, creaky interior, cold blue light upstairs."),
    dict(W=10, D=9, floors=2, plinth=0.8, ext="WoodDark", int="PlasterInt", frame="Frame", win="win", g_front=[("living", 1), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.6)],
         u_front=[("bedroom", 1), ("bedroom", 1)], u_back=[("storage", 1)], roof="gable_y", roof_m="TinRust", pitch=50, over=0.4, gable_m="WoodDark",
         cap="Rust", porch=True, porch_col="WoodDark", door_m="WoodDark", plot_m="Grass"), _d9_haunt)

def _d9_candy(ctx):
    for i, x in enumerate((ctx["x1"] - 0.6, ctx["x2"] + 0.6)):
        mb = MB()
        for k in range(10):
            mb.cyl(0, 0, k * 0.25, k * 0.25 + 0.25, 0.15, "White" if k % 2 else "PlasticRed", seg=12)
        mb.obj("CandyCane%d" % i, x, ctx["y1"] - 0.6, 0, kind="trim")
    for i in range(4):
        mb = MB(); mb.cyl(0, 0, 0, 1.2, 0.03, "White", seg=6); mb.cyl(0, 0, 1.2, 1.25, 0.3, RNG.choice(["NeonPink", "PlasticYellow", "PlasticBlue"]), seg=20, axis="y") if False else mb.sph(0, 0, 1.35, 0.3, RNG.choice(["NeonPink", "PlasticYellow", "PlasticBlue", "PlasticGreen"]), sy=0.3)
        furn("Lollipop", mb, ctx["x1"] + 1.0 + i * 1.6, ctx["y1"] - 2.5, 0, 0)
    ob("Icing", [(ctx["x1"] - 0.15, ctx["y1"] - 0.15, ctx["roof_z"] - 0.2, ctx["x2"] + 0.15, ctx["y1"], ctx["roof_z"])], ["White"], kind="trim")
reg(_d9_m("gingerbread_house", "薑餅糖果屋", "Gingerbread Candy House", "Fairy-tale Candy House", "糖果屋", "standard", "house",
          ["fantasy", "christmas", "cartoon", "family"], "Gingerbread-brick cottage with icing trim, candy-cane posts and giant lollipops; pink frosting roof."),
    dict(W=8, D=7, floors=1, h0=3.0, ext="BrickCream", int="PlasterInt", frame="PlasticRed", win="win", g_front=[("living", 1), ("kitchen", 1)],
         roof="gable_y", roof_m="NeonPink", pitch=45, over=0.5, gable_m="BrickCream", cap="White", door_m="PlasticRed", plot_m="Grass", front=4.0), _d9_candy)

def _d9_pirate(ctx):
    mb = MB(); mb.cyl(0, -0.05, 0, 0, 0.7, "WoodDark", seg=24, axis="y"); mb.cyl(0, -0.1, 0, 0, 0.55, "WoodLight", seg=24, axis="y")
    for k in range(8):
        a = k * math.pi / 4; mb.box(math.cos(a) * 0.75 - 0.04, -0.12, math.sin(a) * 0.75 - 0.04, math.cos(a) * 0.95 + 0.04, -0.06, math.sin(a) * 0.95 + 0.04, "WoodDark")
    mb.obj("ShipWheel", 0.0, ctx["y1"] - 0.08, ctx["Z"][1] - 0.6, kind="sign")
    for i in range(5):
        barrel(ctx["x1"] + 0.5 + i * 0.7, ctx["y1"] - 1.0, 0, 0, "WoodDark")
    for k in range(3):
        cable("Rope%d" % k, (ctx["x1"], ctx["y1"] - 0.1, 3.0 + k * 0.4), (ctx["x2"], ctx["y1"] - 0.1, 3.0 + k * 0.4), 0.5)
reg(_d9_m("pirate_tavern", "黑帆海盜酒館", "Black Sail Pirate Tavern", "Pirate Port Tavern", "海盜酒館", "budget", "tavern",
          ["pirate", "fantasy", "adventure", "rpg"], "2-storey tarred-timber tavern: rum bar and tables, rooms upstairs, ship's-wheel sign, rope festoons, barrels."),
    dict(W=12, D=10, floors=2, ext="WoodDark", int="WoodDark", frame="Brass", win="win", ground="bar", g_front=[("bar", 1), ("restaurant", 1)],
         g_back=[("storage", 1)], u_front=[("hotel", 1), ("hotel", 1)], u_back=[("hotel", 1)], shop_k="win", shop_frame="Brass", door_k="door_double",
         door_m="WoodDark", door_x=2.0, roof="gable", roof_m="TinRust", pitch=30, over=0.5, gable_m="WoodDark", cap="Rust", decor=["lanterns"], plot_m="Cobble",
         sign=("BLACK SAIL", "Black", "Brass", 4.0), sign_x=2.0), _d9_pirate)

def _d9_lantern():
    meta = _d9_m("lantern_festival_tower", "元宵燈籠塔", "Lantern Festival Tower", "Chinese Lantern Tower", "燈籠塔", "landmark", "tower",
                 ["wuxia", "festival", "anime", "fantasy"], "8-sided vermilion tower hung with dozens of red lanterns, tile cone roof, spiral stair to a lookout.")
    ctx = _d5_round(meta, 8, 3.2, 3, 3.2, "PaintRed", "Plaster", roof="cone", roof_m="RoofTile", roof_h=3.6, hole_r=1.2, plot_m="StoneTile")
    for f in range(3):
        for k in range(8):
            a = k * math.pi / 4 + math.pi / 8
            lamp("FestL_%d_%d" % (f, k), math.cos(a) * 3.9, math.sin(a) * 3.9, f * 3.2 + 3.0, 10 if k % 2 else 0.01, (1.0, 0.35, 0.12), kind="lantern", glow="Lantern")
    finish_std(ctx)
regx(("lantern_festival_tower",), _d9_lantern, 14.0, 9.0, 7.0)

reg(_d9_m("wuxia_inn", "龍門客棧", "Dragon Gate Inn", "Wuxia Desert Inn", "武俠客棧", "standard", "inn",
          ["wuxia", "historical", "fantasy", "action"], "2-storey timber-and-plaster inn: tavern hall of tables and a bar, guest rooms above, curled slate roof, banner pole."),
    dict(W=14, D=11, floors=2, h0=3.6, ext0="WoodDark", ext="Plaster", frame="WoodDark", win="win3", ground="restaurant", g_front=[("restaurant", 1), ("bar", 1)],
         g_back=[("kitchen", 1), ("storage", 0.6)], u_front=[("hotel", 1)] * 3, u_back=[("hotel", 1)], shop_k="win3", shop_frame="WoodDark",
         roof="hip", roof_m="SlateDark", pitch=28, over=0.9, curl=0.5, ornaments=True, door_k="door_double", door_m="WoodDark", door_x=0.0, plot_m="Sand",
         sign=("龍門客棧", "Black", "Brass", 3.0), decor=["lanterns"]),
    lambda c: (pipe_run("BannerPole", [(c["x2"] + 1.2, c["y1"] - 1.0, 0), (c["x2"] + 1.2, c["y1"] - 1.0, 8.0)], 0.07, "WoodDark"),
               ob("Banner", [(c["x2"] + 1.27, c["y1"] - 1.02, 4.5, c["x2"] + 2.4, c["y1"] - 0.98, 7.8)], ["PaintRed"], kind="sign"),
               text("BannerTxt", "客\n棧", c["x2"] + 1.83, c["y1"] - 1.05, 6.2, 0.6, "Black", extrude=0.01)))

def _d9_tao(ctx):
    mb = MB(); mb.cyl(0, 0, 0, 0.9, 0.6, "Brass", seg=16, r2=0.75); mb.cyl(0, 0, 0.9, 1.0, 0.8, "Brass", seg=16)
    furn("Censer", mb, 0.0, ctx["y1"] - 4.0, 0, 0, "use")
    mb = MB(); mb.cyl(0, 0, 0, 0.05, 1.6, "Black", seg=8); mb.cyl(0, 0, 0.05, 0.06, 1.0, "White", seg=32)
    mb.obj("Bagua", 0.0, ctx["y1"] - 6.0, 0.0, kind="floor")
reg(_d9_m("taoist_temple", "紫霄道觀", "Purple Cloud Taoist Temple", "Taoist Temple", "道觀", "landmark", "temple",
          ["wuxia", "fantasy", "xianxia", "realistic"], "Vermilion hall on a tall stone plinth with sweeping curled roof and ornaments, altar inside, censer and bagua courtyard."),
    dict(W=12, D=10, floors=1, h0=4.6, plinth=1.2, ext="PaintRed", int="PaintRed", frame="Brass", win="grille", g_front=[("chapel", 1)],
         roof="hip", roof_m="SlateDark", pitch=30, over=1.2, curl=0.7, ornaments=True, door_k="door_double", door_m="PaintRed", door_w=2.0, door_x=0.0,
         front=8.0, plot_m="StoneTile", decor=["lanterns"]), _d9_tao)

def _d9_castle(ctx):
    for zz in ctx["Z"][1:-1]:
        skirt_ring(ctx, zz - 0.4, 1.1, "SlateDark", 0.35)
    for sx in (-1, 1):
        mb = MB(); mb.cyl(0, 0, 0, 0.5, 0.25, "Brass", seg=10, r2=0.1); mb.sph(0, -0.1, 0.6, 0.18, "Brass", sz=1.4)
        mb.obj("Shachihoko%d" % sx, sx * (ctx["W"] / 2 - 1.0), 0.0, ctx["top"] - 0.1, kind="trim")
reg(_d9_m("japanese_castle", "白鷺天守閣", "White Heron Castle Keep", "Japanese Castle Tenshu", "日式天守閣", "landmark", "castle",
          ["japan", "samurai", "anime", "historical", "strategy"], "3-storey white tenshu on a 3 m battered stone base: tiered curled roofs at every floor, golden shachihoko, samurai hall inside."),
    dict(W=12, D=10, floors=3, h0=3.6, h=3.4, plinth=3.0, plinth_m="Stone", ext="Plaster", int="WoodLight", frame="Black", win="win", ww=1.0,
         g_front=[("lounge", 1), ("dining", 1)], g_back=[("storage", 1)], u_front=[("library", 1), ("lounge", 1)], u_back=[("bedroom", 1)], floor="Tatami",
         roof="hip", roof_m="SlateDark", pitch=32, over=1.2, curl=0.5, ornaments=True, door_k="door_double", door_m="WoodDark", door_x=0.0, front=8.0,
         side=4.0, plot_m="Grass"), _d9_castle)

def _d9_palace(ctx):
    for sx in (-1, 1):
        x = sx * (ctx["W"] / 2 + 1.6)
        mb = MB(); mb.cyl(0, 0, 0, ctx["roof_z"] + 6.0, 0.9, "BrickCream", seg=16)
        mb.cyl(0, 0, ctx["roof_z"] + 4.0, ctx["roof_z"] + 4.3, 1.3, "Brass", seg=16)
        mb.obj("Minaret%d" % sx, x, ctx["y1"] + 1.0, 0, kind="structure")
        dome("MinaretDome%d" % sx, x, ctx["y1"] + 1.0, ctx["roof_z"] + 6.0, 0.95, "Brass", 1.3)
    ctx["top"] = max(ctx["top"], ctx["roof_z"] + 7.3)
reg(_d9_m("desert_palace", "沙漠蘇丹宮殿", "Desert Sultan's Palace", "Arabian Palace", "中東宮殿", "luxury", "palace",
          ["fantasy", "desert", "aladdin", "rpg", "adventure"], "2-storey cream palace under a golden onion-style dome with twin minarets: throne hall, banquet, chambers and library."),
    dict(W=18, D=14, floors=2, h0=4.4, h=3.8, plinth=0.8, ext="BrickCream", int="Plaster", frame="Brass", win="grille", ww=1.2, head=3.4,
         g_front=[("lounge", 1), ("lobby", 1), ("dining", 1)], g_back=[("kitchen", 1), ("bath", 0.5)], u_front=[("bedroom", 1), ("library", 1)],
         u_back=[("bedroom", 1), ("onsen", 1)], floor0="Marble", floor="CarpetRed", roof="dome", roof_m="Brass", dome_k=0.6, dome_sz=1.25,
         door_k="door_double", door_m="WoodDark", door_w=2.0, door_x=0.0, decor=["cornice"], band_m="Brass", side=5.0, plot_m="Sand"), _d9_palace)

def _d9_egypt(ctx):
    y1 = ctx["y1"]
    for sx in (-1, 1):
        mb = MB(); mb.prism([(-2.6, 0), (2.6, 0), (2.0, 7.5), (-2.0, 7.5)], y1 - 1.2, y1 + 0.2, "BrickCream", plane="xz")
        mb.box(-2.1, y1 - 1.3, 7.5, 2.1, y1 + 0.3, 7.9, "BrickCream"); o = mb.obj("Pylon%d" % sx, sx * (ctx["W"] / 2 - 1.0), 0, 0, kind="structure")
    mb = MB(); mb.cyl(0, 0, 0, 9.0, 0.6, "Stone", seg=4, r2=0.25); mb.cyl(0, 0, 9.0, 9.8, 0.25, "Brass", seg=4, r2=0.0)
    mb.obj("Obelisk", ctx["x2"] + 2.5, y1 - 3.0, 0, kind="structure")
    ctx["top"] = max(ctx["top"], 9.8)
reg(_d9_m("egyptian_temple", "尼羅神殿", "Temple of the Nile", "Ancient Egyptian Temple", "埃及神殿", "landmark", "temple",
          ["historical", "fantasy", "adventure", "mummy"], "Sandstone temple: battered pylon gateway, columned portico, sanctuary hall with altar, obelisk."),
    dict(W=14, D=14, floors=1, h0=5.4, plinth=0.6, ext="BrickCream", int="BrickCream", frame="Brass", win="win", ww=0.6, sill=3.0, head=4.6,
         g_front=[("chapel", 1)], floor0="StoneTile", roof="flat", parapet=0.6, porch=True, porch_w=8.0, porch_d=3.0, porch_col="BrickCream", porch_h=5.0,
         porch_roof="BrickCream", door_k="door_double", door_m="Brass", door_w=2.0, door_x=0.0, front=7.0, side=4.0, plot_m="Sand"), _d9_egypt)

def _d9_maya():
    meta = _d9_m("maya_pyramid", "羽蛇金字塔", "Feathered Serpent Pyramid", "Mesoamerican Step Pyramid", "馬雅金字塔", "landmark", "pyramid",
                 ["adventure", "historical", "fantasy", "tomb-raider"], "Nine-tier stepped stone pyramid with a central stair to a summit temple room (altar, torches).")
    BX(meta, 2)
    ob("Plot", [(-15.0, -17.5, -0.4, 15.0, 14.0, 0.0)], ["Sand"], kind="floor", walkable=True)
    tiers, step = 9, 1.1
    bx = []
    for k in range(tiers):                       # tiers split around a 3.2 m stair channel on the south face
        h = 12.0 - k * 1.1; z0, z1 = k * step, (k + 1) * step
        bx += [(-h, -h, z0, -1.6, h, z1), (1.6, -h, z0, h, h, z1), (-1.6, -3.2, z0, 1.6, h, z1)]
    ob("Pyramid", bx, ["Stone"], kind="structure", walkable=True)
    top = tiers * step
    nS = round(top / 0.18); tr = 0.22
    stair("GrandStair", 0.0, -3.2 - (nS - 1) * tr, 0.0, top, "+y", 3.1, tr, "Stone", rails="none", solid=True)
    ring("Temple", -3.0, -3.0, 3.0, 3.0, top, top + 3.2, "Stone", "Stone", 0.4, 0.0, {"S": [(-0.8, 0.8, top, top + 2.4, "open")]})
    slab("TempleRoof", -3.0, -3.0, 3.0, 3.0, top + 3.4, 0.4, top="Stone", under="Stone")
    crenellate("Crest", [Vector((-3, -3, 0)), Vector((3, -3, 0)), Vector((3, 3, 0)), Vector((-3, 3, 0))], top + 3.4, 0.9, 0.5, 0.3, "Stone")
    mb = MB(); mb.box(-0.9, -0.5, 0, 0.9, 0.5, 0.9, "Stone"); furn("Altar", mb, 0.0, 1.5, top, 0, "use")
    for sx in (-1, 1):
        lamp("Torch%d" % sx, sx * 1.4, -3.3, top + 2.2, 40, (1.0, 0.5, 0.15), kind="point", fixture=False)
        mb = MB(); mb.cyl(0, 0, 0, 1.6, 0.06, "WoodDark", seg=8); mb.sph(0, 0, 1.7, 0.15, "NeonOrange"); mb.obj("TorchPost%d" % sx, sx * 1.4, -3.3, top + 0.4, kind="light_fixture")
    CUR.main_door = (0.0, -12.0, 0.0)
    finish_std(dict(top=top + 4.3, y1=-12.0, W=24.0))
regx(("maya_pyramid",), _d9_maya, 30.0, 17.5, 14.0)

def _d9_viking(ctx):
    for sx in (-1, 1):
        mb = MB(); mb.cyl(0, 0, 0, 1.6, 0.12, "WoodDark", seg=8, r2=0.08); mb.sph(0, -0.15, 1.7, 0.2, "WoodDark", sy=1.6)
        o = mb.obj("DragonHead%d" % sx, 0.0, sx * (ctx["D"] / 2 + 0.6), ctx["top"] - 0.4, kind="trim"); o.rotation_euler.x = sx * 0.5
    fireplace(0.0, 0.0, 0.0, 0, "Stone")
reg(_d9_m("viking_longhouse", "維京長屋", "Viking Longhouse", "Norse Longhouse", "維京長屋", "standard", "longhouse",
          ["viking", "fantasy", "survival", "rpg", "medieval"], "Long single-storey timber hall with a steep shingled roof and carved dragon-head gable ends: feast hall, hearth, sleeping benches."),
    dict(W=20, D=8, floors=1, h0=3.0, ext="WoodDark", int="WoodDark", frame="WoodDark", win="win", ww=0.6, bay=4.0, g_front=[("dining", 1.4), ("lounge", 1), ("dorm", 1)],
         floor0="WoodFloor", roof="gable", roof_m="WoodDark", pitch=48, over=0.5, gable_m="WoodDark", cap="WoodDark", door_k="door_double",
         door_m="WoodLight", door_x=0.0, plot_m="Grass", decor=["lanterns"]), _d9_viking)

def _d9_yurt():
    meta = _d9_m("mongol_yurt", "草原蒙古包", "Steppe Ger (Yurt)", "Mongolian Ger", "蒙古包", "budget", "yurt",
                 ["nomad", "survival", "historical", "cozy"], "16-sided felt ger with a low cone roof: stove, beds and rugs around a central hearth.")
    def furnish(f, z, r):
        bed(-2.2, 1.0, z, 110, 1.0, 1.9, "FabricRed", "WoodLight"); bed(2.2, 1.0, z, 250, 1.0, 1.9, "FabricBlue", "WoodLight")
        rug(0.0, 0.0, z, 0, 3.0, 3.0, "CarpetRed"); fireplace(0.0, 2.8, z, 180, "MetalDark")
    ctx = _d5_round(meta, 16, 3.6, 1, 2.3, "FabricWhite", "FabricBeige", roof="cone", roof_m="FabricWhite", roof_h=1.6, plot_m="Grass", furnish=furnish,
                    win_segs=[3, 13])
    finish_std(ctx)
regx(("mongol_yurt",), _d9_yurt, 14.0, 9.0, 7.0)

def _d9_tipi():
    meta = _d9_m("tipi_camp", "平原帳篷營地", "Plains Tipi Camp", "Plains Tipi Encampment", "帳篷營地", "budget", "camp",
                 ["western", "survival", "historical", "nomad"], "Three hide tipis around a stone-ringed campfire, drying rack and log seats.")
    BX(meta, 1)
    ob("Plot", [(-10.0, -10.0, -0.4, 10.0, 8.0, 0.0)], ["Grass"], kind="terrain", walkable=True)
    for i, (x, y, r) in enumerate(((0.0, 3.0, 2.6), (-5.0, -1.0, 2.0), (5.0, -1.0, 2.2))):
        mb = MB(); mb.cyl(0, 0, 0, r * 2.4, r, "FabricBeige", seg=12, r2=0.15)
        for k in range(8):
            a = k * math.pi / 4; mb.cyl(math.cos(a) * 0.1, math.sin(a) * 0.1, r * 2.3, r * 2.9, 0.03, "WoodDark", seg=5)
        mb.box(-0.4, -r - 0.02, 0, 0.4, -r + 0.3, 1.4, "Black")
        mb.obj("Tipi%d" % i, x, y, 0, 0 if i == 0 else (60 if i == 1 else -60), kind="structure")
    mb = MB()
    for k in range(10):
        a = k * math.pi / 5; mb.sph(math.cos(a) * 0.7, math.sin(a) * 0.7, 0.1, 0.18, "Stone")
    mb.sph(0, 0, 0.2, 0.35, "NeonOrange", sz=0.8); furn("Campfire", mb, 0.0, -2.5, 0, 0, "use")
    lamp("Fire", 0.0, -2.5, 0.8, 120, (1.0, 0.5, 0.15), kind="point", fixture=False)
    for i in range(3):
        a = i * 2 * math.pi / 3 + 0.5
        mb = MB(); mb.cyl(-0.8, 0, 0.2, 0.2, 0.2, "Bark", seg=10, axis="x") if False else mb.cyl(-0.8, 0, 0.22, 1.8 - 0.2, 0.2, "Bark", seg=10, axis="x")
        furn("LogSeat", mb, math.cos(a) * 2.0, -2.5 + math.sin(a) * 2.0, 0, math.degrees(a) + 90, "sit")
    CUR.main_door = (0.0, -2.0, 0.0)
    finish_std(dict(top=7.0, y1=-3.0, W=14.0))
regx(("tipi_camp",), _d9_tipi, 20.0, 10.0, 8.0)

def _d9_colony():
    meta = _d9_m("space_colony_dome", "火星殖民穹頂", "Mars Colony Dome", "Sci-Fi Habitat Dome", "太空殖民地", "landmark", "habitat",
                 ["sci-fi", "survival", "mars", "solarpunk"], "16-sided habitat ring under a big glass dome: hydroponic farm racks, crew lounge, consoles; airlock entrance.")
    def furnish(f, z, r):
        for k in range(6):
            a = k * math.pi / 3 + 0.3
            mb = MB(); mb.box(-0.5, -0.25, 0, 0.5, 0.25, 2.0, "MetalDark")
            for j in range(4):
                zz = 0.25 + j * 0.45
                mb.box(-0.48, -0.23, zz, 0.48, 0.23, zz + 0.06, "White"); mb.sph(0, 0, zz + 0.14, 0.12, "PlantGreen", sx=3.6, sy=1.4, sz=0.7)
                mb.box(-0.46, -0.21, zz + 0.38, 0.46, 0.21, zz + 0.4, "NeonPurple")
            furn("FarmRack", mb, math.cos(a) * (r - 1.0), math.sin(a) * (r - 1.0), z, math.degrees(a) + 90, "use")
        console(0.0, 2.6, z, 180, 2.4, 3); sofa(0.0, -1.5, z, 180, 2.4, "FabricWhite")
    ctx = _d5_round(meta, 16, 7.0, 1, 3.4, "PanelSteel", "White", roof="none", plot_m="Sand", furnish=furnish, win_segs=[1, 4, 7, 10, 14], plot=10.0)
    dome("GlassDome", 0, 0, ctx["zt"] + 0.25, 7.2, "GlassBlue", 0.7, seg=48)
    mb = MB(); mb.box(-1.4, -1.6, 0, 1.4, 0.0, 2.8, "PanelSteel"); mb.box(-1.0, -1.61, 0.1, 1.0, -1.6, 2.4, "MetalDark")
    mb.obj("Airlock", 0.0, -6.8, 0, kind="structure")
    ctx["top"] = ctx["zt"] + 5.4; finish_std(ctx)
regx(("space_colony_dome",), _d9_colony, 20.0, 12.0, 10.0)

def _d9_totem(ctx):
    for sx in (-1, 1):
        mb = MB()
        for k in range(5):
            mb.cyl(0, 0, k * 1.1, (k + 1) * 1.1, 0.45, ["PaintRed", "WoodLight", "PaintTeal", "WoodDark", "PlasticYellow"][k], seg=12)
            mb.sph(0, -0.42, k * 1.1 + 0.6, 0.12, "Black");
        mb.box(-1.2, -0.1, 5.0, 1.2, 0.1, 5.3, "PaintRed")
        mb.obj("Totem%d" % sx, sx * (ctx["W"] / 2 + 1.0), ctx["y1"] - 1.0, 0, kind="structure")
reg(_d9_m("totem_lodge", "圖騰長屋", "Totem Plank Lodge", "Pacific Northwest Plank House", "西北海岸長屋", "standard", "lodge",
          ["historical", "adventure", "survival", "fantasy"], "Cedar plank longhouse with a low gable, painted façade band and two carved totem poles: great room with hearth and sleeping platforms."),
    dict(W=14, D=9, floors=1, h0=3.4, ext="WoodLight", int="WoodLight", frame="WoodDark", win="win", ww=0.8, g_front=[("lounge", 1), ("dorm", 1)],
         floor0="WoodFloor", roof="gable", roof_m="WoodDark", pitch=20, over=0.6, gable_m="WoodLight", cap="WoodDark", door_k="door", door_m="WoodDark",
         door_x=0.0, side=4.0, plot_m="Grass", decor=["bands"], band_m="PaintRed"), _d9_totem)
