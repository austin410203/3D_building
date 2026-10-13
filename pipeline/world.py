# Island, streets, render/world setup. Exec'd in the TownKit namespace.
import bpy, math, random
from mathutils import Vector, noise as mnoise

GROUND_Z = 0.15          # sidewalk / plot level; buildings sit here
WATER_Z = -0.6

def setup_render(night=True):
    sc = bpy.context.scene
    for eng in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
        try:
            sc.render.engine = eng; break
        except TypeError:
            pass
    sc.render.resolution_x = 1600; sc.render.resolution_y = 1000
    try:
        sc.eevee.taa_render_samples = 48
        sc.eevee.use_shadows = True
        sc.eevee.use_raytracing = True
        ids = [i.identifier for i in bpy.types.SceneEEVEE.bl_rna.properties["shadow_pool_size"].enum_items]
        sc.eevee.shadow_pool_size = ids[-1]
    except Exception:
        pass
    try:
        sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
    except Exception:
        pass
    sc.unit_settings.system = "METRIC"
    w = bpy.data.worlds.get("TK_World") or bpy.data.worlds.new("TK_World")
    sc.world = w; w.use_nodes = True
    nt = w.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new("ShaderNodeOutputWorld")
    bg = nt.nodes.new("ShaderNodeBackground")
    tc = nt.nodes.new("ShaderNodeTexCoord"); sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    nt.links.new(tc.outputs["Generated"], sep.inputs[0])
    # use the view direction Z for a vertical gradient
    nt.links.new(sep.outputs["Z"], ramp.inputs["Fac"])
    cr = ramp.color_ramp
    if night:
        cr.elements[0].position = 0.0; cr.elements[0].color = (0.035, 0.05, 0.09, 1)
        cr.elements[1].position = 0.45; cr.elements[1].color = (0.006, 0.012, 0.035, 1)
        strength = 1.0
    else:
        cr.elements[0].position = 0.0; cr.elements[0].color = (0.75, 0.82, 0.9, 1)
        cr.elements[1].position = 0.5; cr.elements[1].color = (0.25, 0.45, 0.85, 1)
        strength = 1.0
    nt.links.new(ramp.outputs["Color"], bg.inputs["Color"]); bg.inputs["Strength"].default_value = strength
    nt.links.new(bg.outputs[0], out.inputs[0])
    # moon / sun
    for o in [o for o in bpy.data.objects if o.name in ("TK_Sun",)]:
        bpy.data.objects.remove(o)
    ld = bpy.data.lights.new("TK_Sun", "SUN")
    if night:
        ld.energy = 0.35; ld.color = (0.55, 0.65, 1.0); ld.angle = math.radians(1.0)
        rot = (math.radians(55), 0, math.radians(-35))
    else:
        ld.energy = 4.0; ld.color = (1.0, 0.95, 0.88); ld.angle = math.radians(1.5)
        rot = (math.radians(45), 0, math.radians(-40))
    so = bpy.data.objects.new("TK_Sun", ld); so.rotation_euler = rot
    bpy.context.scene.collection.objects.link(so)
    sc["night"] = night

def set_lights_mode(night):
    """day: interior/street point lights dimmed (still useful in-game)"""
    for o in bpy.data.objects:
        if o.type == "LIGHT" and o.name != "TK_Sun":
            o.hide_render = not night and o.data.type == "POINT" and "StreetLampL" in o.name

# ----------------------------------------------------------------------------- island
def h_island(x, y):
    d = ((abs(x) / ISL[0]) ** 4 + (abs(y) / ISL[1]) ** 4) ** 0.25
    d += 0.05 * mnoise.noise(Vector((x * 0.02, y * 0.02, 0.3)))
    if d < 0.80:
        h = 0.0
    elif d < 0.97:
        t = (d - 0.80) / 0.17
        h = -1.3 * t * t if t > 0.2 else -0.05 * t
    else:
        h = -1.3 - (d - 0.97) * 40
    # north hill with plateau for the polar station
    hd = math.hypot(x - HILL[0], y - HILL[1])
    if hd < HILL[3]:
        t = 1.0 if hd < HILL[2] else 1 - (hd - HILL[2]) / (HILL[3] - HILL[2])
        t = t * t * (3 - 2 * t)
        h = max(h, HILL[4] * t + 0.4 * t * mnoise.noise(Vector((x * 0.15, y * 0.15, 1.0))) * (1 - t))
    return max(h, -6)

HILL = (0.0, 86.0, 10.0, 34.0, 7.0)    # cx, cy, plateau r, foot r, height
ISL = (300.0, 240.0)                    # island superellipse radii (v3: enlarged for 167 buildings)

def build_island():
    begin_building("island_town", "海港小鎮島", "Harbor Town Island", "Environment", "環境", "template", "environment",
                   ["any"], "Island terrain + streets + lamps + trees that hosts every TownKit building.", 0, (0, 0))
    CUR.root.name = "ENV_island"
    import bmesh
    bm = bmesh.new()
    S = 2.0; NX = 330; NY = 270
    vs = {}
    for j in range(NY + 1):
        for i in range(NX + 1):
            x = -NX * S / 2 + i * S; y = -NY * S / 2 + j * S
            vs[i, j] = bm.verts.new((x, y, h_island(x, y)))
    mats = ["Grass", "Sand", "Snow", "Stone"]
    for j in range(NY):
        for i in range(NX):
            f = bm.faces.new((vs[i, j], vs[i + 1, j], vs[i + 1, j + 1], vs[i, j + 1]))
            zc = sum(v.co.z for v in f.verts) / 4
            hd = math.hypot(f.calc_center_median().x - HILL[0], f.calc_center_median().y - HILL[1])
            f.material_index = 2 if (zc > 2.2 and hd < HILL[3]) else (1 if zc < -0.08 else 0)
            f.smooth = True
    me = bpy.data.meshes.new(_nm("Terrain")); bm.to_mesh(me); bm.free()
    for m in mats: me.materials.append(M[m])
    t = bpy.data.objects.new(_nm("Terrain"), me); CUR.col.objects.link(t); adopt(t, "terrain", walkable=True)
    # sea
    mb = MB(); mb.box(-600, -600, WATER_Z - 0.05, 600, 600, WATER_Z, "Water")
    mb.obj("Sea", kind="water")
    roads()
    return CUR

# carriageways (8 m) as (axis, centre, a1, a2): 'x' = runs along X at y=centre
ROADS = [("x", 0.0, -240, 240), ("y", 0.0, -170, 50), ("x", -62.0, -240, 240), ("x", -118.0, -228, 228), ("x", -170.0, -190, 190),
         ("x", 50.0, -240, 240), ("x", 100.0, -235, -42), ("x", 100.0, 42, 235), ("x", 150.0, -215, 215)]

def _minus(a, b, cuts):
    segs = [(a, b)]
    for c1, c2 in cuts:
        out = []
        for s1, s2 in segs:
            if c2 <= s1 or c1 >= s2:
                out.append((s1, s2)); continue
            if c1 > s1: out.append((s1, c1))
            if c2 < s2: out.append((c2, s2))
        segs = out
    return [sg for sg in segs if sg[1] - sg[0] > 0.5]

def roads():
    G = GROUND_Z
    bx, sw, curb, mk = [], [], [], []
    for (ax, c, a1, a2) in ROADS:
        bx.append((a1, c - 4, -0.05, a2, c + 4, 0.03) if ax == "x" else (c - 4, a1, -0.05, c + 4, a2, 0.03))
        cuts = [(o[1] - 7, o[1] + 7) for o in ROADS if o[0] != ax and o[2] - 4 <= c <= o[3] + 4]
        for (s1, s2) in _minus(a1, a2, cuts):
            for side in (-1, 1):
                lo, hi = sorted((c + side * 4, c + side * 7))
                sw.append((s1, lo, -0.05, s2, hi, G) if ax == "x" else (lo, s1, -0.05, hi, s2, G))
                q1, q2 = sorted((c + side * 3.85, c + side * 4.0))
                curb.append((s1, q1, 0, s2, q2, G + 0.01) if ax == "x" else (q1, s1, 0, q2, s2, G + 0.01))
            t = s1 + 2
            while t < s2 - 3:
                mk.append((t, c - 0.07, 0.03, t + 3, c + 0.07, 0.036) if ax == "x" else (c - 0.07, t, 0.03, c + 0.07, t + 3, 0.036))
                t += 6
            # zebra crossings at cut ends
            for e in (s1, s2):
                if a1 + 1 < e < a2 - 1:
                    for k in range(8):
                        u = c - 3.5 + k
                        off = -2.2 if e == s1 else 0.4
                        mk.append((e + off, u, 0.03, e + off + 1.8, u + 0.5, 0.036) if ax == "x" else (u, e + off, 0.03, u + 0.5, e + off + 1.8, 0.036))
            # street lamps
            t = s1 + 6
            k = 0
            while t < s2 - 4:
                if ax == "x":
                    street_lamp(t, c + 6.4, G, 0) if k % 2 == 0 else street_lamp(t, c - 6.4, G, 180)
                else:
                    street_lamp(c - 6.4, t, G, 270) if k % 2 == 0 else street_lamp(c + 6.4, t, G, 90)
                t += 12; k += 1
    ob("Road", bx, ["Asphalt"], kind="road", walkable=True)
    ob("Sidewalk", sw, ["StoneTile"], kind="sidewalk", walkable=True)
    ob("Curb", curb, ["Concrete"], kind="trim")
    ob("Markings", mk, ["White"], kind="trim")
    rr = random.Random(3)
    # beach palms + hill pines
    for i in range(160):
        a = rr.uniform(0, 2 * math.pi)
        x = math.cos(a) * ISL[0] * 0.86; y = math.sin(a) * ISL[1] * 0.86
        x += rr.uniform(-6, 6); y += rr.uniform(-6, 6)
        z = h_island(x, y)
        if -0.25 < z < 0.4 and math.hypot(x - 237, y + 190) > 30:
            tree(x, y, z, rr.uniform(0.8, 1.2), "palm", seed=100 + i)
    for i in range(40):
        a = rr.uniform(0, 2 * math.pi); r = rr.uniform(13, 30)
        x = HILL[0] + math.cos(a) * r; y = HILL[1] + math.sin(a) * r
        if abs(x) < 4 and y < HILL[1]:
            continue
        tree(x, y, h_island(x, y) - 0.1, rr.uniform(0.8, 1.4), "pine", seed=200 + i)
