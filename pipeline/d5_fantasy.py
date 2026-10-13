# District 5 — fantasy / landmark (9). Names prefixed _d5_.

def _d5_round(meta, n=12, r=4.0, floors=3, h=3.4, ext="Stone", intm="Plaster", ext_f=None, roof="cone", roof_m="SlateBlue",
              roof_h=5.0, hole_r=1.5, win_segs=None, plot=7.0, plot_m="Cobble", furnish=None, roof_access=False, floor_m="WoodFloor", doors=(0,)):
    BX(meta, floors)
    ob("Plot", [(-plot, -plot - 2.0, -0.4, plot, plot, 0.0)], [plot_m], kind="floor", walkable=True)
    front_seg = (3 * n) // 4 - 1                    # segment whose centre faces -Y
    win_segs = win_segs if win_segs is not None else [i for i in range(n) if i % 3 == 1]
    a0 = 0.0
    for f in range(floors):
        z0, z1 = f * h, (f + 1) * h
        ops = {}
        for i in win_segs:
            ops.setdefault(i, []).append((-0.35, 0.35, z0 + 1.0, z0 + 2.3, "win", "WoodDark"))
        if f in doors:
            ops[front_seg] = [(-0.55, 0.55, z0, z0 + 2.3, "door", "WoodDark")]
        poly_wall("F%d" % (f + 1), 0, 0, r, n, z0, z1, (ext_f[f] if ext_f else ext), intm, 0.35, ops)
        disc_floor("F%d_Floor" % (f + 1), 0, 0, r - 0.05, n, z0 + (0.0 if f == 0 else 0.0), 0.22, hole_r if f > 0 else 0.0, floor_m)
        if f < floors - 1 or roof_access:
            a0 = spiral_stair("F%d_Spiral" % (f + 1), 0, 0, z0, z1, hole_r - 0.06, 0.2, a0, 1.0, "WoodDark", "WoodDark")
        if f > 0:                                    # rail round the stair well, gap at the arrival
            pts = []
            for k in range(25):
                ang = math.radians(a0 + 35 + k * (290 / 24))
                pts.append((math.cos(ang) * (hole_r + 0.05), math.sin(ang) * (hole_r + 0.05), z0 + 0.95))
            pipe_run("F%d_WellRail" % (f + 1), pts, 0.03, "WoodDark", kind="railing")
        lamp("F%d_L" % (f + 1), 0.0, -r * 0.5, z1 - 0.3, 60, (1.0, 0.75, 0.45), kind="lantern", glow="Lantern")
        if furnish:
            furnish(f, z0, r)
    zt = floors * h
    disc_floor("RoofDeck", 0, 0, r + 0.1, n, zt + 0.25, 0.25, hole_r if roof_access else 0.0, "Stone" if roof != "cone" else "WoodDark", "Plaster")
    CUR.main_door = (0.0, -r * math.cos(math.pi / n), 0.0)
    top = zt
    if roof == "cone":
        mb = MB(); mb.cyl(0, 0, zt + 0.25, zt + 0.25 + roof_h, r + 0.9, roof_m, seg=n, r2=0.05)
        mb.cyl(0, 0, zt + 0.25 + roof_h, zt + 0.25 + roof_h + 1.0, 0.05, "Brass", seg=8); mb.sph(0, 0, zt + 0.35 + roof_h + 1.0, 0.18, "Brass")
        mb.obj("ConeRoof", kind="roof"); top = zt + roof_h + 1.4
    elif roof == "crenel":
        pts = [Vector(p) for p in _poly(r + 0.05, n, math.pi / n)]
        mb = MB()
        for i in range(n):
            a, b = pts[i], pts[(i + 1) % n]; d = (b - a)
            for j in range(2):
                c = a + d * ((j + 0.5) / 2)
                sub = MB(); sub.box(-0.45, -0.2, 0, 0.45, 0.2, 1.1, ext)
                sub.obj("Merlon_%d_%d" % (i, j), c.x, c.y, zt + 0.25, math.degrees(math.atan2(d.y, d.x)), kind="trim")
        top = zt + 1.4
    return dict(top=top, y1=-r, W=2 * r, zt=zt, n=n, r=r)

def _d5_wizard():
    meta = ("wizard_tower", "星辰法師塔", "Starlight Wizard Tower", "High-Fantasy Wizard Tower", "奇幻法師塔", "landmark", "tower",
            ["fantasy", "rpg", "anime", "magic-school", "ghibli"],
            "12-sided stone tower: library, alchemy lab, bedchamber and star-gazing study linked by a spiral stair; tall blue cone roof, glowing crystals.")
    def furnish(f, z, r):
        for k in range(5 if f != 2 else 3):
            a = math.radians(30 + k * 60)
            x, y = math.cos(a) * (r - 0.75), math.sin(a) * (r - 0.75)
            rot = math.degrees(a) + 90
            if f == 0:
                bookshelf(x, y, z, rot, 1.4, 2.6, 0.4)
            elif f == 1:
                mb = MB(); mb.box(-0.7, -0.35, 0, 0.7, 0.35, 0.85, "WoodDark")
                for j in range(4):
                    mb.cyl(-0.5 + j * 0.33, 0, 0.85, 1.1, 0.06, RNG.choice(["NeonGreen", "NeonPurple", "NeonCyan", "GlassBlue"]), seg=10)
                furn("AlchemyTable", mb, x, y, z, rot, "use")
            elif f == 2 and k == 0:
                bed(x, y, z, rot, 1.4, 2.0, "FabricNavy", "WoodDark")
            elif f == 2:
                wardrobe(x, y, z, rot, 1.0, 2.1, 0.55, "WoodDark")
        if f == 3:
            telescope(2.0, 2.0, z, 225)
            mb = MB(); mb.cyl(0, 0, 0, 0.9, 0.25, "WoodDark", seg=12); mb.sph(0, 0, 1.15, 0.28, "NeonPurple", sub=3)
            furn("ScryingOrb", mb, -2.2, 1.6, z, 0, "use")
            lamp("OrbGlow", -2.2, 1.6, z + 1.3, 30, (0.6, 0.3, 1.0), kind="point", fixture=False)
        if f == 1:
            mb = MB(); mb.cyl(0, 0, 0, 0.7, 0.55, "MetalDark", seg=16, r2=0.45); mb.cyl(0, 0, 0.5, 0.62, 0.48, "NeonGreen", seg=16)
            furn("Cauldron", mb, -2.2, -1.2, z, 0, "cook")
    ctx = _d5_round(meta, 12, 4.2, 4, 3.4, "Stone", "Plaster", roof_m="SlateBlue", roof_h=7.0, furnish=furnish, plot_m="Grass")
    for i in range(5):
        a = i * 2 * math.pi / 5
        mb = MB(); mb.sph(0, 0, 0, 0.3, "NeonPurple", sx=0.6, sy=0.6, sz=1.6)
        mb.obj("Crystal%d" % i, math.cos(a) * 6.0, math.sin(a) * 6.0, 1.5 + (i % 2) * 0.8, kind="light_fixture")
    lamp("CrystalGlow", 0, -6.0, 2.0, 60, (0.6, 0.3, 1.0), kind="point", fixture=False)
    finish_std(ctx)
regx(("wizard_tower",), _d5_wizard, 14.0, 9.0, 7.0)

def _d5_lighthouse():
    meta = ("lighthouse_cape", "海角燈塔", "Cape Lighthouse", "Maritime Lighthouse", "海事燈塔", "landmark", "lighthouse",
            ["realistic", "horror", "mystery", "adventure", "ghibli"],
            "Red/white striped 5-storey round tower with spiral stair, gallery deck, glazed lantern room with glowing lens; keeper's cottage.")
    def furnish(f, z, r):
        if f == 0:
            crate(-1.8, 1.8, z, 20, 0.6); barrel(2.0, 1.5, z, 0, "Rust")
        if f == 2:
            mb = MB(); mb.box(-0.6, -0.3, 0, 0.6, 0.3, 0.8, "WoodDark"); furn("ChartTable", mb, 1.6, -1.4, z, 30, "use")
    ctx = _d5_round(meta, 12, 3.2, 5, 3.2, "White", "Plaster", ext_f=["Stone", "PaintRed", "White", "PaintRed", "White"], roof="none",
                    hole_r=1.3, furnish=furnish, roof_access=True, plot_m="Stone", plot=9.0)
    zt = ctx["zt"] + 0.25
    disc_floor("Gallery", 0, 0, 4.4, 12, zt, 0.25, 0.0, "MetalDark", "MetalDark")
    pts = [(math.cos(k * math.pi / 12) * 4.3, math.sin(k * math.pi / 12) * 4.3, zt + 1.0) for k in range(25)]
    pipe_run("GalleryRail", pts, 0.035, "MetalDark", kind="railing")
    poly_wall("Lantern", 0, 0, 2.3, 12, zt, zt + 2.8, "Glass", "Glass", 0.06, {8: [(-0.4, 0.4, zt, zt + 2.0, "door_metal")]})
    mb = MB(); mb.cyl(0, 0, zt + 2.8, zt + 4.6, 2.7, "PaintRed", seg=12, r2=0.1); mb.sph(0, 0, zt + 4.7, 0.2, "Brass")
    mb.cyl(0, 0, zt, zt + 1.2, 0.5, "Brass", seg=12); mb.sph(0, 0, zt + 1.7, 0.6, "LightWarm", sub=3)
    mb.obj("LanternTop", kind="roof")
    lamp("Beacon", 0, 0, zt + 1.7, 2000, (1.0, 0.92, 0.75), kind="point", fixture=False)
    # keeper's cottage east of the tower
    ring("Cottage", 4.0, -2.5, 9.0, 2.5, 0.0, 2.8, "Plaster", "PlasterInt", 0.2, 0.03,
         {"S": [(5.5, 6.5, 0.0, 2.1, "door", "PaintRed"), (7.2, 8.4, 0.9, 2.0, "win")], "E": [(-1.0, 1.0, 0.9, 2.0, "win")]})
    slab("CottageFloor", 4.2, -2.3, 8.8, 2.3, 0.0, 0.2, top="WoodFloor", under="Stone")
    gable_roof("CottageRoof", 4.0, -2.5, 9.0, 2.5, 2.8, 35, 0.4, "SlateDark", "WoodDark", along="x", gable_m="Plaster", cap="SlateDark")
    bed(7.6, 1.2, 0.0, 270, 1.0, 1.9, "FabricBlue"); table(5.4, 1.4, 0.0, 0, 1.0, 0.6); chair(5.4, 0.8, 0.0, 180)
    fireplace(4.6, 0.0, 0.0, 90, "Stone"); lamp("CottageL", 6.5, 0.0, 2.6, 40)
    ctx["top"] = zt + 4.8
    finish_std(ctx)
regx(("lighthouse_cape",), _d5_lighthouse, 18.0, 11.0, 9.0)

def _d5_windmill():
    meta = ("windmill_dutch", "風車磨坊", "Old Dutch Windmill", "Dutch Tower Windmill", "荷蘭風車", "landmark", "windmill",
            ["rpg-village", "fantasy", "cozy", "farming-sim", "realistic"],
            "8-sided brick windmill: grain store, millstone floor with reefing gallery, miller's loft; timber cap with four lattice sails (rotate prop).")
    def furnish(f, z, r):
        if f == 0:
            for i in range(4):
                barrel(-1.8 + (i % 2) * 0.7, 1.6 + (i // 2) * 0.7, z, 0, "WoodLight")
            for i in range(3):
                crate(1.6, -1.2 + i * 0.7, z, 10 * i, 0.6, "Paper")
        if f == 1:
            mb = MB(); mb.cyl(0, 0, 0, 0.35, 1.0, "Stone", seg=24); mb.cyl(0, 0, 0.35, 0.65, 0.95, "Stone", seg=24); mb.cyl(0, 0, 0.65, 1.6, 0.08, "WoodDark", seg=8)
            furn("Millstone", mb, -1.6, -1.6, z, 0, "use")
        if f == 2:
            bed(1.6, 1.0, z, 225, 1.0, 1.9, "FabricRed", "WoodLight")
    ctx = _d5_round(meta, 8, 3.4, 3, 3.0, "BrickDark", "WoodLight", roof="cone", roof_m="WoodDark", roof_h=3.0, hole_r=1.2,
                    furnish=furnish, plot_m="Grass", win_segs=[1, 3, 6], doors=(0, 1))
    disc_floor("ReefDeck", 0, 0, 5.2, 8, 3.0, 0.15, 3.45, "WoodLight", "WoodDark")
    pts = [(math.cos(k * math.pi / 12) * 5.1, math.sin(k * math.pi / 12) * 5.1, 4.0) for k in range(25)]
    pipe_run("DeckRail", pts, 0.03, "WoodDark", kind="railing")
    zh = 9.6
    mb = MB(); mb.cyl(0, 0, 0, 1.2, 0.35, "WoodDark", seg=12, axis="y") if False else mb.cyl(0, -0.6, 0, 0, 0.35, "WoodDark", seg=12, axis="y") if False else None
    mb.box(-0.3, -0.3, -0.3, 0.3, 0.3, 0.3, "WoodDark")
    for k in range(4):
        sub_ang = k * 90
        ca, sa = math.cos(math.radians(sub_ang)), math.sin(math.radians(sub_ang))
        for i in range(12):
            d = 0.6 + i * 0.6
            mb.box(ca * d - 0.06 - sa * 0.0, -0.12, sa * d - 0.06, ca * d + 0.06, -0.08, sa * d + 0.06, "WoodDark")
        # sail cloth panel
        p0 = (ca * 1.0, sa * 1.0); p1 = (ca * 7.6, sa * 7.6); n_ = (-sa * 1.4, ca * 1.4)
        mb.quad([(p0[0], -0.1, p0[1]), (p1[0], -0.1, p1[1]), (p1[0] + n_[0], -0.1, p1[1] + n_[1]), (p0[0] + n_[0], -0.1, p0[1] + n_[1])], "FabricBeige", 0.0)
    sails = mb.obj("Sails", 0.0, -4.9, zh, kind="trim")
    pipe_run("WindShaft", [(0.0, -4.8, zh), (0.0, -2.6, zh)], 0.18, "WoodDark")
    sails["openable"] = "rotate"; sails["rotate_axis"] = "local_Y"; sails["interact"] = "use"
    lamp("MillDoorL", 0.9, -3.5, 2.4, 20, kind="wall")
    ctx["top"] = ctx["top"] + 1.0
    finish_std(ctx)
regx(("windmill_dutch",), _d5_windmill, 14.0, 9.0, 7.0)

def _d5_tavern(ctx):
    halftimber(ctx, ctx["Z"][1], ctx["Z"][2])
    fireplace(ctx["x1"] + 0.6, -1.0, 0.0, 90, "Stone")
    mb = MB(); mb.box(-0.03, -1.2, 0, 0.03, 0.0, 0.05, "MetalDark"); mb.box(-0.02, -1.0, -0.8, 0.02, -0.4, 0.0, "WoodDark")
    mb.obj("SignArm", ctx["x1"] + 0.2, ctx["y1"], 3.0, 90, kind="trim")
    sign_board("HangSign", "躍馬", ctx["x1"] - 0.5, ctx["y1"] - 0.75, 2.5, 0.9, 0.6, 90, "WoodDark", "Brass", 0.3)
    for i in range(4):
        barrel(ctx["x2"] - 0.6, ctx["y1"] - 0.6 - i * 0.65, 0, 0, "WoodLight")
    mb = MB(); mb.cyl(0, 0, 0, 0.8, 0.8, "Stone", seg=16); mb.cyl(0, 0, 0.8, 0.85, 0.6, "Water", seg=16)
    for sx in (-0.75, 0.75):
        mb.box(sx - 0.06, -0.06, 0.8, sx + 0.06, 0.06, 2.3, "WoodDark")
    mb.box(-0.9, -0.06, 2.2, 0.9, 0.06, 2.3, "WoodDark"); furn("Well", mb, ctx["x2"] + 3.0, ctx["y1"] - 2.5, 0, 0, "use")
reg(("medieval_tavern", "躍馬旅店", "The Prancing Stag Tavern", "Medieval Fantasy Tavern", "中世紀酒館",
     "standard", "tavern + inn", ["fantasy", "medieval", "rpg", "realistic", "anime"],
     "Stone-and-timber tavern: great hearth, bar, kitchen; half-timbered guest rooms upstairs; slate roof, hanging sign, ale barrels, well."),
    dict(W=14, D=11, floors=2, h0=3.4, h=3.0, ext0="Stone", ext="Plaster", frame="WoodDark", win="win", ww=1.0, ground="bar",
         g_front=[("bar", 1.4), ("restaurant", 1)], g_back=[("kitchen", 1), ("storage", 0.6)], u_front=[("hotel", 1)] * 3,
         u_back=[("hotel", 1), ("bath", 0.6)], floor0="StoneTile", door_k="door_double", door_m="WoodDark", door_x=-1.0,
         shop_k="win3", shop_frame="WoodDark", roof="gable", roof_m="SlateDark", pitch=50, over=0.5, gable_m="Plaster", cap="SlateDark",
         decor=["chimney", "lanterns"], chimney_m="Stone", side=6.0, plot_m="Cobble"), _d5_tavern)

def _d5_keep(ctx):
    x1, x2, y1, y2, zr = ctx["x1"], ctx["x2"], ctx["y1"], ctx["y2"], ctx["roof_z"]
    pts = [Vector((x1, y1, 0)), Vector((x2, y1, 0)), Vector((x2, y2, 0)), Vector((x1, y2, 0))]
    crenellate("Merlons", pts, zr + 1.0, 0.8, 0.6, 0.4, "Stone")
    for (cx, cy) in ((x1, y1), (x2, y1), (x1, y2), (x2, y2)):
        mb = MB(); mb.cyl(0, 0, 0, zr + 2.6, 1.3, "Stone", seg=12); mb.cyl(0, 0, zr + 2.6, zr + 5.6, 1.7, "SlateBlue", seg=12, r2=0.05)
        mb.box(-0.12, -1.31, zr - 3.0, 0.12, -1.28, zr - 2.2, "Black")
        mb.obj("Turret_%d_%d" % (int(cx), int(cy)), cx, cy, 0, kind="structure")
    for i, x in enumerate((-2.0, 2.0)):
        mb = MB(); mb.box(-0.05, -0.02, 0, 0.05, 0.02, 3.0, "MetalDark"); mb.box(0.05, -0.01, 1.4, 1.2, 0.01, 3.0, ["PaintRed", "PlasticBlue"][i])
        mb.obj("Banner%d" % i, x, y1 - 0.25, zr + 1.0, kind="trim")
    ctx["top"] = zr + 5.6
reg(("castle_keep", "獅鷲城堡塔", "Griffin Castle Keep", "Medieval Castle Keep", "中世紀城堡",
     "landmark", "castle", ["fantasy", "medieval", "rpg", "strategy", "realistic"],
     "4-storey square stone keep with corner turrets: great hall, armoury/storage, lord's chamber + library, crenellated roof walk with banners."),
    dict(W=12, D=12, floors=4, h0=4.0, h=3.6, plinth=0.9, plinth_m="Stone", ext="Stone", int="Stone", frame="Frame", win="win", ww=0.5,
         sill=1.2, head=2.6, bay=2.4, ground="dining", g_front=[("dining", 1), ("lounge", 1)], g_back=[("workshop", 1)],
         u_front=[("bedroom", 1), ("library", 1)], u_back=[("storage", 1)], floor0="StoneTile", floor="WoodFloor", stair_m="Stone",
         door_k="door_double", door_m="WoodDark", door_w=1.8, door_h=3.0, door_x=-2.0, roof="terrace", parapet=1.0, parapet_m="Stone",
         side=5.0, plot_m="Cobble"), _d5_keep)

def _d5_tree():
    meta = ("treehouse_oak", "老橡樹樹屋", "Old Oak Treehouse", "Storybook Treehouse", "童話樹屋", "standard", "treehouse",
            ["cozy", "ghibli", "adventure", "cartoon", "fantasy"],
            "Giant oak with a wrap deck at 4.5 m reached by a timber stair, a gabled cabin (bed, desk, lantern) and a rope ladder to a crow's-nest lookout.")
    BX(meta, 2)
    DZ = 4.5
    ob("Plot", [(-8.0, -10.0, -0.4, 8.0, 8.0, 0.0)], ["Grass"], kind="terrain", walkable=True)
    mb = MB()
    mb.cyl(0, 0, -0.2, 6.0, 1.3, "Bark", seg=16, r2=1.0); mb.cyl(0, 0, 6.0, 12.0, 1.0, "Bark", seg=14, r2=0.6)
    for a in range(6):
        t_ = a * math.pi / 3 + 0.2
        mb.sph(math.cos(t_) * 1.5, math.sin(t_) * 1.5, 0.1, 0.7, "Bark", sx=1.8, sy=0.8, sz=0.6)
    mb.obj("Trunk", kind="structure")
    pipe_run("BranchA", [(0.6, 0.4, 7.0), (3.5, 2.0, 9.5), (5.5, 2.5, 11.5)], 0.35, "Bark")
    pipe_run("BranchB", [(-0.5, -0.3, 8.0), (-3.8, 1.6, 10.2), (-5.0, 3.0, 12.0)], 0.3, "Bark")
    rr_ = random.Random(77)
    mb = MB()
    for i in range(22):
        mb.sph(rr_.uniform(-6, 6), rr_.uniform(-5, 6), rr_.uniform(10.5, 15.5), rr_.uniform(1.8, 2.8), rr_.choice(["Leaf", "PlantGreen", "Leaf"]), sub=2)
    mb.obj("Canopy", kind="vegetation")
    slab("Deck", -3.6, -3.6, 3.6, 3.6, DZ, 0.25, holes=[(-1.35, -1.35, 1.35, 1.35)], top="WoodLight", under="WoodDark", ft=0.05)
    mb = MB()
    for (x, y) in ((-3.5, -3.5), (3.5, -3.5), (-3.5, 3.5), (3.5, 3.5)):
        mb.bc(x, y, 0, 0.22, 0.22, DZ - 0.25, "WoodDark")
    mb.obj("DeckPosts", kind="structure")
    n = round(DZ / 0.18); L = (n - 1) * 0.28
    stair("Stair", 4.3, -3.6 - 0.0, 0.0, DZ, "+y", 1.0, 0.28, "WoodLight", rails="both", rail_style="wood") if False else None
    st = stair("Stair", -2.9, -3.6 - L, 0.0, DZ, "+y", 1.0, 0.28, "WoodLight", rails="both", rail_style="wood")
    rail("DeckS", -2.35, -3.6, 3.6, -3.6, DZ, 1.0, "wood"); rail("DeckE", 3.6, -3.6, 3.6, 3.6, DZ, 1.0, "wood")
    rail("DeckW", -3.6, -3.6, -3.6, 3.6, DZ, 1.0, "wood"); rail("DeckN", -3.6, 3.6, 0.2, 3.6, DZ, 1.0, "wood")
    # cabin on the east half (wraps the trunk on its west face)
    ring("Cabin", 1.45, -2.6, 3.5, 3.5, DZ, DZ + 2.6, "SidingTeal", "WoodLight", 0.15, 0.03,
         {"S": [(1.9, 2.8, DZ, DZ + 2.0, "door", "PaintRed")], "E": [(-0.8, 0.8, DZ + 1.0, DZ + 1.9, "win", "PaintRed")],
          "N": [(2.0, 3.0, DZ + 1.1, DZ + 1.9, "win", "PaintRed")]}, sides="SNE")
    gable_roof("CabinRoof", 1.3, -2.6, 3.6, 3.5, DZ + 2.6, 40, 0.35, "RoofTile", "WoodDark", along="y", gable_m="SidingTeal", cap="RoofRed")
    bed(2.6, 2.4, DZ, 0, 0.9, 1.8, "FabricRed", "WoodLight"); desk(2.9, -0.8, DZ, 270, 1.0, 0.5, "WoodLight", pc=False, chair_=False)
    lamp("CabinLantern", 2.4, 0.4, DZ + 2.4, 30, (1.0, 0.6, 0.3), kind="lantern", glow="Lantern")
    CUR.main_door = (2.35, -2.6, DZ)
    # crow's nest + rope ladder
    disc_floor("Nest", -2.4, 2.0, 1.4, 8, 9.5, 0.15, 0.0, "WoodLight", "WoodDark")
    pts = [(-2.4 + math.cos(k * math.pi / 8) * 1.35, 2.0 + math.sin(k * math.pi / 8) * 1.35, 10.4) for k in range(17)]
    pipe_run("NestRail", pts, 0.03, "WoodDark", kind="railing")
    mb = MB()
    for sx in (-0.25, 0.25):
        mb.box(sx - 0.015, -0.015, 0, sx + 0.015, 0.015, 9.5 - DZ, "FabricBeige")
    for i in range(int((9.5 - DZ) / 0.3)):
        mb.box(-0.25, -0.02, 0.2 + i * 0.3, 0.25, 0.02, 0.24 + i * 0.3, "WoodLight")
    lad = mb.obj("RopeLadder", -2.4, 0.62, DZ, kind="ladder"); lad["interact"] = "climb"; lad["top_z"] = 9.5
    for i in range(6):
        lamp("Fairy%d" % i, -3.4 + i * 1.3, -3.7, DZ + 2.2, 5, (1.0, 0.7, 0.4), kind="point", fixture=False)
    swing = MB(); swing.box(-0.3, -0.12, 0.5, 0.3, 0.12, 0.55, "WoodLight")
    for sx in (-0.28, 0.28):
        swing.box(sx - 0.01, -0.01, 0.55, sx + 0.01, 0.01, 4.2, "FabricBeige")
    furn("TyreSwing", swing, 5.0, 3.0, 0, 0, "play")
    ctx = dict(top=16.0, y1=-3.6, W=7.2)
    finish_std(ctx)
regx(("treehouse_oak",), _d5_tree, 16.0, 10.0 + 4.5, 8.0)

def _d5_steam(ctx):
    x1, x2, y1, zr = ctx["x1"], ctx["x2"], ctx["y1"], ctx["roof_z"]
    for i, (x, z, r) in enumerate(((x1 + 2.0, 5.5, 1.1), (x1 + 3.6, 7.0, 0.7), (x2 - 2.2, 8.2, 0.9))):
        mb = MB(); mb.cyl(0, 0, 0, 0.12, r, "Brass", seg=24, axis="y"); mb.cyl(0, 0, 0.12, 0.2, r * 0.3, "Rust", seg=12, axis="y")
        for k in range(16):
            a = k * 2 * math.pi / 16
            mb.box(math.cos(a) * r - 0.07, 0, math.sin(a) * r - 0.07, math.cos(a) * r + 0.07, 0.12, math.sin(a) * r + 0.07, "Brass")
        mb.obj("Gear%d" % i, x, y1 - 0.18, z, kind="trim")["openable"] = "rotate"
    for i, x in enumerate((x1 + 1.5, x2 - 1.5)):
        mb = MB(); mb.cyl(0, 0, 0, 4.0, 0.35, "Rust", seg=16); mb.cyl(0, 0, 4.0, 4.4, 0.45, "MetalDark", seg=16)
        mb.cyl(0, 0, 4.38, 4.4, 0.3, "NeonOrange", seg=16)
        mb.obj("Stack%d" % i, x, ctx["y2"] - 1.2, zr, kind="trim")
    for k in range(5):
        pipe_run("SteamPipe%d" % k, [(x1 - 0.15, y1 + 1.0 + k * 1.6, 0.3), (x1 - 0.15, y1 + 1.0 + k * 1.6, 3.0 + k * 1.3),
                                     (x1 - 0.15, y1 + 1.6 + k * 1.6, 3.4 + k * 1.3), (x1 - 0.15, y1 + 1.6 + k * 1.6, zr + 1.0)],
                 0.06 + 0.02 * (k % 2), ["Brass", "Rust", "PanelCopper"][k % 3])
    mb = MB(); mb.cyl(0, 0, 0, 6.0, 0.1, "Brass", seg=10); mb.cyl(0, 0, 6.0, 6.3, 0.5, "Brass", seg=16); mb.sph(0, 0, 6.5, 0.25, "NeonOrange")
    mb.obj("MooringMast", 0.0, 0.5, ctx["top"], kind="trim")
    ctx["top"] += 6.5
reg(("steampunk_works", "齒輪蒸汽工坊", "Cog & Steam Works", "Steampunk Workshop", "蒸汽龐克工坊",
     "standard", "workshop", ["steampunk", "fantasy", "victorian", "anime", "rpg"],
     "3-storey copper-and-brick workshop: machine shop, drafting library, inventor's loft; giant brass gears, steam pipes, smokestacks, airship mooring mast."),
    dict(W=12, D=11, floors=3, h0=3.8, h=3.4, ext="PanelCopper", ext0="BrickDark", frame="Brass", win="win3", ground="workshop",
         g_front=[("workshop", 1)], g_back=[("storage", 1), ("bath", 0.6)], u_front=[("workshop", 1), ("library", 1)], u_back=[("lounge", 1)],
         prog={2: ([("studio", 1)], [("bedroom", 1)])}, floor0="Parquet", door_k="door_double", door_m="Brass", door_x=1.8, roof="gable",
         roof_m="TinRust", pitch=30, over=0.4, gable_m="PanelCopper", cap="Brass", side=4.0, sign=("齒輪工坊 COG & STEAM", "WoodDark", "Brass", 5.0),
         decor=["lanterns"]), _d5_steam)

def _d5_obs():
    meta = ("observatory_dome", "星穹天文台", "Starvault Observatory", "Domed Observatory", "圓頂天文台", "landmark", "observatory",
            ["sci-fi", "realistic", "mystery", "anime", "academy"],
            "12-sided white drum: visitor/lab floor, control room, telescope floor under a copper dome with an opening slit and a large telescope.")
    def furnish(f, z, r):
        if f == 0:
            for k in range(3):
                a = math.radians(40 + k * 60); console(math.cos(a) * (r - 1.0), math.sin(a) * (r - 1.0), z, math.degrees(a) + 90, 1.6, 2)
            bookshelf(-(r - 0.8), 1.2, z, 270, 1.4, 2.2)
        if f == 1:
            for k in range(4):
                a = math.radians(200 + k * 40); desk(math.cos(a) * (r - 1.0), math.sin(a) * (r - 1.0), z, math.degrees(a) + 90, 1.2, 0.6)
    ctx = _d5_round(meta, 12, 5.0, 2, 3.8, "White", "PlasterInt", roof="none", hole_r=1.3, furnish=furnish, plot_m="StoneTile",
                    roof_access=True)
    zt = ctx["zt"] + 0.25
    dome("Dome", 0, 0, zt, 5.1, "PanelCopper", 0.95, seg=40)
    for k in range(11):
        th = math.radians(k * 8.0)
        mb = MB(); mb.box(-0.55, -0.6, -0.04, 0.55, 0.6, 0.06, "Black")
        o_ = mb.obj("Slit%d" % k, 0.0, 5.12 * math.sin(th), zt + 5.12 * 0.95 * math.cos(th), kind="trim")
        o_.rotation_euler = (-th, 0, 0)
    telescope(0.0, 2.2, zt, 180)
    lamp("DomeL", 0.0, -2.0, zt + 3.5, 60, (1.0, 0.85, 0.7))
    ctx["top"] = zt + 5.0
    finish_std(ctx)
regx(("observatory_dome",), _d5_obs, 14.0, 9.0, 7.0)

def _d5_shrine(ctx):
    y1 = ctx["y1"]
    mb = MB()
    for sx in (-1.9, 1.9):
        mb.cyl(sx, 0, 0, 4.2, 0.2, "PaintRed", seg=16); mb.cyl(sx, 0, 0, 0.4, 0.28, "Black", seg=16)
    mb.box(-2.9, -0.25, 4.2, 2.9, 0.25, 4.55, "Black"); mb.box(-2.6, -0.2, 3.5, 2.6, 0.2, 3.75, "PaintRed")
    mb.box(-0.25, -0.18, 3.75, 0.25, 0.18, 4.2, "PaintRed")
    mb.obj("Torii", 0.0, y1 - 6.0, 0, kind="structure")
    for sx in (-1, 1):
        mb = MB(); mb.box(-0.25, -0.25, 0, 0.25, 0.25, 0.15, "Stone"); mb.cyl(0, 0, 0.15, 0.75, 0.08, "Stone", seg=8)
        mb.box(-0.22, -0.22, 0.75, 0.22, 0.22, 0.82, "Stone"); mb.box(-0.16, -0.16, 0.82, 0.16, 0.16, 1.1, "LightSoft")
        mb.cyl(0, 0, 1.1, 1.32, 0.34, "Stone", seg=4, r2=0.04); furn("Toro", mb, sx * 1.8, y1 - 3.0, 0, 45)
    ob("Sando", [(-0.9, y1 - 8.5, 0.0, 0.9, y1, 0.03)], ["StoneTile"], kind="floor", walkable=True)
    mb = MB(); mb.box(-0.6, -0.3, 0, 0.6, 0.3, 0.7, "WoodDark"); mb.box(-0.62, -0.32, 0.7, 0.62, 0.32, 0.75, "WoodLight")
    furn("OfferingBox", mb, 0.0, y1 - 1.0, ctx["Z"][0], 0, "use")
    mb = MB(); mb.box(-0.02, -0.02, 0, 0.02, 0.02, 1.6, "FabricRed"); mb.cyl(0, 0, 1.6, 1.9, 0.15, "Brass", seg=12, r2=0.1)
    mb.obj("BellRope", 0.0, y1 - 0.4, ctx["Z"][0] + 1.0, kind="trim")["interact"] = "use"
    tree(ctx["x2"] + 3.0, y1 - 1.0, 0, 1.4, "broad", seed=901)
    mb = MB(); mb.cyl(0, 0, 2.2, 2.4, 0.95, "FabricWhite", seg=20); mb.obj("Shimenawa", ctx["x2"] + 3.0, y1 - 1.0, 0, kind="trim")
reg(("shinto_shrine", "朱鳥神社", "Vermilion Bird Shrine", "Japanese Shinto Shrine", "日式神社",
     "landmark", "shrine", ["anime", "japan", "fantasy", "horror", "realistic"],
     "Vermilion shrine hall on a stone plinth with sliding paper doors and a curved slate gable; torii gate, stone lanterns, offering box, bell, sacred tree."),
    dict(W=10, D=8, floors=1, h0=3.4, plinth=0.9, plinth_m="Stone", ext="PaintRed", int="WoodLight", frame="WoodDark", win="slide", ww=1.6,
         g_front=[("chapel", 1)], floor0="Tatami", roof="gable", roof_m="SlateDark", pitch=28, over=1.3, gable_m="WoodDark", cap="SlateDark",
         door_k="door_double", door_m="WoodLight", door_w=1.8, door_x=0.0, front=10.0, side=5.0, plot_m="Cobble"), _d5_shrine)
