# blender -b TownKit.blend -P render.py -- --bld apt_urban_5f[,..|all] [--view front|back|overview|cut|top] [--res 1280] [--day]
#   cut = hide everything above --cutz (local metres) to see the plan of a floor
import bpy, os, sys, math
from mathutils import Vector, Matrix
SD = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(SD, ".."))
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def arg(k, d=None):
    return argv[argv.index(k) + 1] if k in argv else d
VIEW = arg("--view", "front"); RES = int(arg("--res", "1280")); OUTD = arg("--outdir", os.path.join(ROOT, "renders"))
CUTZ = float(arg("--cutz", "2.6")); SAMPLES = int(arg("--samples", "32"))
os.makedirs(OUTD, exist_ok=True)
sc = bpy.context.scene
sc.render.resolution_x = RES; sc.render.resolution_y = int(RES * 0.625)
try:
    sc.eevee.taa_render_samples = SAMPLES
    ids = [i.identifier for i in bpy.types.SceneEEVEE.bl_rna.properties["shadow_pool_size"].enum_items]
    sc.eevee.shadow_pool_size = ids[-1]
except Exception as e:
    print("eevee setting", e)
if "--day" in argv:
    for o in bpy.data.objects:
        if o.name == "TK_Sun":
            o.data.energy = 4.0; o.data.color = (1, 0.95, 0.88); o.rotation_euler = (math.radians(50), 0, math.radians(-40))
    w = sc.world
    for n in w.node_tree.nodes:
        if n.type == "VALTORGB":
            n.color_ramp.elements[0].color = (0.75, 0.82, 0.9, 1); n.color_ramp.elements[1].color = (0.25, 0.45, 0.85, 1)
roots = {o.name[4:]: o for o in bpy.data.objects if o.name.startswith("BLD_") and o.type == "EMPTY"}
sel = arg("--bld", "all")
ids = list(roots) if sel == "all" else sel.split(",")

def kids(o):
    out = []
    for c in o.children:
        out.append(c); out += kids(c)
    return out

def bounds(objs):
    pts = [o.matrix_world @ Vector(c) for o in objs if o.type == "MESH" and o.get("kind") not in ("collider", "cable") for c in o.bound_box]
    mn = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    mx = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return mn, mx

cam = bpy.data.objects.get("TK_Cam") or bpy.data.objects.new("TK_Cam", bpy.data.cameras.new("TK_Cam"))
if cam.name not in sc.collection.objects:
    sc.collection.objects.link(cam)
sc.camera = cam; cam.data.lens = 32; cam.data.clip_end = 2000

def aim(loc, target):
    cam.location = loc
    cam.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()

if VIEW == "overview":
    cam.data.lens = 30
    aim((150, -190, 150), (0, 5, 0))
    sc.render.filepath = os.path.join(OUTD, "overview" + ("_day" if "--day" in argv else "") + ".png")
    bpy.ops.render.render(write_still=True)
    sys.exit(0)

for bid in ids:
    r = roots[bid]
    objs = kids(r)
    vis = []
    for o in bpy.data.objects:                       # other buildings' floating labels would clutter the shot
        if o.get("kind") == "label" and o not in objs and not o.hide_render:
            o.hide_render = True; vis.append(o)
    if VIEW == "cut":
        for o in objs:
            if o.get("kind") == "label":
                o.hide_render = True; vis.append(o)
    mn, mx = bounds([o for o in objs if o.get("kind") not in ("label", "trim") or (VIEW != "cut" and o.get("kind") == "label")])
    c = (mn + mx) / 2; size = (mx - mn).length
    rot = r.rotation_euler.z
    R3 = Matrix.Rotation(rot, 3, "Z")
    if VIEW == "front":
        d = R3 @ Vector((-0.55, -1.0, 0.45))
    elif VIEW == "back":
        d = R3 @ Vector((0.6, 1.0, 0.5))
    elif VIEW == "cut":
        d = Vector((0, 0, 1.0)); cam.data.lens = 30
    else:
        d = Vector((0.01, -0.01, 1))
    d.normalize()
    dist = size * (1.05 if VIEW != "cut" else 0.95)
    if VIEW in ("front", "back"):
        dist = max(dist, (mx.z - mn.z) * 1.75)
    tgt = c if VIEW != "cut" else Vector((c.x, c.y, r.matrix_world.translation.z + 1.0))
    aim(tgt + d * dist, tgt)
    cam.data.clip_start = 0.1
    if VIEW == "cut":
        cam.rotation_euler = (0, 0, rot)   # horizontal-ish section through the storey via the near clip plane
        cam.data.clip_start = max(0.1, (cam.location.z - (r.matrix_world.translation.z + CUTZ)) / d.z * 1.0)
    sc.render.filepath = os.path.join(OUTD, "%s_%s%s.png" % (bid, VIEW, "_day" if "--day" in argv else ""))
    bpy.ops.render.render(write_still=True)
    for o in vis:
        o.hide_render = False
    print("rendered", sc.render.filepath)
