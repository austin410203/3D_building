# Player character + sports car for the web game.
#   blender -b --factory-startup -P make_actors.py -- <out_dir> [--render]
# hero.glb : rigid-skinned humanoid (14 bones), NLA animations Idle / Walk / Run / Jump / Drive. Faces Blender -Y (glTF +Z).
# car.glb  : lofted sports coupe, wheels Wheel_FL/FR/RL/RR (origin = hub, spin about local X), FrontPivot_L/R for steering,
#            SteeringWheel, BrakeLights material "CarBrake", empties Seat_Driver / Exit_L / Cam_Chase. Front = Blender -Y.
import bpy, bmesh, math, os, sys
from mathutils import Vector, Matrix, Quaternion
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = os.path.abspath(argv[0]) if argv else os.path.abspath(".")
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o)

MATS = {}
def mat(name, col, rough=0.5, metal=0.0, emit=None, coat=0.0, alpha=1.0):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = (*col, 1); b.inputs["Roughness"].default_value = rough; b.inputs["Metallic"].default_value = metal
    if coat:
        for k in ("Coat Weight", "Clearcoat"):
            if k in b.inputs: b.inputs[k].default_value = coat
    if emit:
        b.inputs["Emission Color"].default_value = (*emit[0], 1); b.inputs["Emission Strength"].default_value = emit[1]
    if alpha < 1:
        b.inputs["Alpha"].default_value = alpha
        try: m.surface_render_method = "BLENDED"
        except Exception: pass
    MATS[name] = m
    return m

class MB:
    def __init__(s):
        s.bm = bmesh.new(); s.mats = []; s.groups = {}
        s.dl = s.bm.verts.layers.deform.verify()
    def _tag(s, vs, m, smooth=True, group=None):
        if m not in s.mats: s.mats.append(m)
        i = s.mats.index(m)
        for f in {f for v in vs for f in v.link_faces}:
            f.material_index = i; f.smooth = smooth
        if group:
            gi = s.groups.setdefault(group, len(s.groups))
            for v in vs: v[s.dl][gi] = 1.0
    def box(s, c, size, m, group=None, smooth=False):
        r = bmesh.ops.create_cube(s.bm, size=1.0)
        bmesh.ops.scale(s.bm, vec=size, verts=r["verts"]); bmesh.ops.translate(s.bm, vec=c, verts=r["verts"])
        s._tag(r["verts"], m, smooth, group); return r["verts"]
    def cyl(s, a, b, r1, m, r2=None, seg=16, group=None, cap=True):
        a, b = Vector(a), Vector(b); d = b - a
        res = bmesh.ops.create_cone(s.bm, cap_ends=cap, segments=seg, radius1=r1, radius2=r1 if r2 is None else r2, depth=d.length)
        q = Vector((0, 0, 1)).rotation_difference(d.normalized())
        bmesh.ops.rotate(s.bm, verts=res["verts"], cent=(0, 0, 0), matrix=q.to_matrix())
        bmesh.ops.translate(s.bm, verts=res["verts"], vec=(a + b) / 2)
        s._tag(res["verts"], m, True, group); return res["verts"]
    def sph(s, c, r, m, scale=(1, 1, 1), group=None, sub=3):
        res = bmesh.ops.create_icosphere(s.bm, subdivisions=sub, radius=r)
        bmesh.ops.scale(s.bm, vec=scale, verts=res["verts"]); bmesh.ops.translate(s.bm, vec=c, verts=res["verts"])
        s._tag(res["verts"], m, True, group); return res["verts"]
    def obj(s, name, coll=None):
        bmesh.ops.recalc_face_normals(s.bm, faces=s.bm.faces)
        me = bpy.data.meshes.new(name); s.bm.to_mesh(me); s.bm.free()
        for m in s.mats: me.materials.append(m)
        o = bpy.data.objects.new(name, me); (coll or bpy.context.scene.collection).objects.link(o)
        for g, i in sorted(s.groups.items(), key=lambda kv: kv[1]):
            o.vertex_groups.new(name=g)
        return o

# =============================================================== HERO
SKIN = mat("Skin", (0.86, 0.64, 0.5), 0.6); SHIRT = mat("Jacket", (0.12, 0.32, 0.62), 0.7)
TEE = mat("Shirt", (0.92, 0.92, 0.9), 0.8); PANTS = mat("Jeans", (0.12, 0.14, 0.2), 0.8)
SHOE = mat("Shoes", (0.9, 0.9, 0.88), 0.5); SOLE = mat("Sole", (0.05, 0.05, 0.05), 0.8)
HAIR = mat("Hair", (0.07, 0.05, 0.04), 0.6); EYE = mat("Eye", (0.02, 0.02, 0.02), 0.2); BAG = mat("Strap", (0.25, 0.15, 0.08), 0.6)

BONES = {  # name: (head, tail, parent)
    "hips": ((0, 0, 0.94), (0, 0, 1.04), None),
    "spine": ((0, 0, 1.04), (0, 0, 1.24), "hips"), "chest": ((0, 0, 1.24), (0, 0, 1.44), "spine"),
    "neck": ((0, 0, 1.44), (0, 0, 1.53), "chest"), "head": ((0, 0, 1.53), (0, 0, 1.76), "neck"),
}
for sd, sx in (("L", 1), ("R", -1)):
    BONES.update({
        "upper_arm.%s" % sd: ((sx * 0.2, 0, 1.4), (sx * 0.25, 0.0, 1.13), "chest"),
        "forearm.%s" % sd: ((sx * 0.25, 0.0, 1.13), (sx * 0.27, -0.02, 0.88), "upper_arm.%s" % sd),
        "hand.%s" % sd: ((sx * 0.27, -0.02, 0.88), (sx * 0.28, -0.03, 0.76), "forearm.%s" % sd),
        "thigh.%s" % sd: ((sx * 0.095, 0, 0.94), (sx * 0.1, 0.0, 0.5), "hips"),
        "shin.%s" % sd: ((sx * 0.1, 0.0, 0.5), (sx * 0.1, 0.02, 0.09), "thigh.%s" % sd),
        "foot.%s" % sd: ((sx * 0.1, 0.02, 0.09), (sx * 0.1, -0.13, 0.03), "shin.%s" % sd),
    })

arm_d = bpy.data.armatures.new("HeroRig"); rig = bpy.data.objects.new("Hero", arm_d)
bpy.context.scene.collection.objects.link(rig)
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode="EDIT")
for n, (h, t, p) in BONES.items():
    b = arm_d.edit_bones.new(n); b.head = h; b.tail = t; b.roll = 0
for n, (h, t, p) in BONES.items():
    if p: arm_d.edit_bones[n].parent = arm_d.edit_bones[p]; arm_d.edit_bones[n].use_connect = False
bpy.ops.object.mode_set(mode="OBJECT")

mb = MB()
mb.sph((0, 0, 0.99), 0.17, PANTS, (1.05, 0.75, 0.55), "hips")                       # pelvis
mb.cyl((0, 0, 1.03), (0, 0, 1.26), 0.15, SHIRT, 0.17, group="spine")                 # abdomen
mb.cyl((0, 0, 1.25), (0, 0, 1.43), 0.17, SHIRT, 0.19, group="chest")                 # chest
mb.sph((0, 0, 1.42), 0.2, SHIRT, (1.0, 0.62, 0.32), "chest")                         # shoulders
mb.box((0, -0.115, 1.3), (0.12, 0.02, 0.26), TEE, "chest")                           # open jacket shirt
mb.cyl((0, 0, 1.44), (0, 0, 1.55), 0.055, SKIN, group="neck")
mb.sph((0, -0.01, 1.64), 0.115, SKIN, (0.9, 1.0, 1.1), "head", sub=4)
mb.sph((0, 0.015, 1.68), 0.122, HAIR, (0.95, 1.02, 0.95), "head")                    # hair cap (behind / top)
for sx in (-1, 1):
    mb.sph((sx * 0.04, -0.105, 1.655), 0.014, EYE, group="head")
    mb.sph((sx * 0.112, 0.0, 1.635), 0.025, SKIN, (0.5, 1, 1.2), "head")             # ears
mb.sph((0, -0.118, 1.62), 0.018, SKIN, (1, 1.2, 1.3), "head")                        # nose
for sd, sx in (("L", 1), ("R", -1)):
    mb.cyl((sx * 0.2, 0, 1.41), (sx * 0.25, 0.0, 1.12), 0.06, SHIRT, 0.052, group="upper_arm.%s" % sd)
    mb.sph((sx * 0.2, 0, 1.41), 0.065, SHIRT, group="upper_arm.%s" % sd)
    mb.cyl((sx * 0.25, 0.0, 1.13), (sx * 0.27, -0.02, 0.9), 0.05, SHIRT, 0.04, group="forearm.%s" % sd)
    mb.box((sx * 0.275, -0.025, 0.83), (0.035, 0.075, 0.12), SKIN, "hand.%s" % sd, smooth=True)
    mb.cyl((sx * 0.095, 0, 0.95), (sx * 0.1, 0.0, 0.5), 0.085, PANTS, 0.06, group="thigh.%s" % sd)
    mb.cyl((sx * 0.1, 0.0, 0.5), (sx * 0.1, 0.02, 0.1), 0.06, PANTS, 0.045, group="shin.%s" % sd)
    mb.box((sx * 0.1, -0.045, 0.06), (0.1, 0.25, 0.09), SHOE, "foot.%s" % sd, smooth=True)
    mb.box((sx * 0.1, -0.045, 0.012), (0.105, 0.255, 0.025), SOLE, "foot.%s" % sd)
body = mb.obj("HeroMesh")
for p in body.data.polygons: p.use_smooth = True
body.parent = rig
md = body.modifiers.new("Armature", "ARMATURE"); md.object = rig

# ---- animation helpers: rotate bones about GLOBAL axes in their rest frame
def gaxis(bone, axis):
    return (bone.matrix_local.to_3x3().inverted() @ Vector(axis)).normalized()
PB = rig.pose.bones
for pb in PB:
    pb.rotation_mode = "QUATERNION"
rig.animation_data_create()

def make_action(name, frames, fn, loop=True):
    act = bpy.data.actions.new(name)
    rig.animation_data.action = act
    for f in range(frames + 1):
        t = (f / frames) * 2 * math.pi
        for pb in PB:
            pb.rotation_quaternion = Quaternion(); pb.location = (0, 0, 0)
        fn(t, f)
        for pb in PB:
            pb.keyframe_insert("rotation_quaternion", frame=f + 1)
            if pb.name == "hips":
                pb.keyframe_insert("location", frame=f + 1)
    tr = rig.animation_data.nla_tracks.new(); tr.name = name
    st = tr.strips.new(name, 1, act); st.action_frame_end = frames + 1
    rig.animation_data.action = None
    return act

def R(name, ax, ang):
    pb = PB[name]
    pb.rotation_quaternion = Quaternion(gaxis(pb.bone, ax), ang) @ pb.rotation_quaternion

X = (1, 0, 0); Y = (0, 1, 0); Z = (0, 0, 1)
def bob(dz):
    PB["hips"].location = gaxis(PB["hips"].bone, Z) * dz

def gait(t, amp_leg, amp_knee, amp_arm, elbow, lean, bounce, twist=0.0):
    s = math.sin(t)
    for sd, ph in (("L", 0.0), ("R", math.pi)):
        sl = math.sin(t + ph)
        R("thigh.%s" % sd, X, -amp_leg * sl)
        R("shin.%s" % sd, X, amp_knee * max(0.0, math.sin(t + ph - 1.2)) + 0.08)
        R("foot.%s" % sd, X, 0.25 * math.sin(t + ph + 0.5))
        R("upper_arm.%s" % sd, X, amp_arm * sl)
        R("forearm.%s" % sd, X, -elbow - 0.2 * max(0.0, -sl))
    R("spine", X, lean); R("chest", Z, twist * s); R("hips", Z, -twist * s * 0.6)
    R("head", X, -lean * 0.6)
    bob(-bounce * abs(math.cos(t)))

make_action("Idle", 60, lambda t, f: (R("chest", X, 0.03 * math.sin(t)), R("upper_arm.L", Y, -0.12), R("upper_arm.R", Y, 0.12),
                                      R("forearm.L", X, -0.15), R("forearm.R", X, -0.15), R("head", Z, 0.08 * math.sin(t * 0.5)), bob(0.008 * math.sin(t))))
make_action("Walk", 32, lambda t, f: gait(t, 0.45, 0.9, 0.38, 0.25, 0.04, 0.035, 0.08))
make_action("Run", 20, lambda t, f: gait(t, 0.85, 1.6, 0.75, 1.3, 0.22, 0.07, 0.15))
def jump(t, f):
    for sd in ("L", "R"):
        R("thigh.%s" % sd, X, -0.9 if sd == "L" else -0.3); R("shin.%s" % sd, X, 1.3 if sd == "L" else 0.5)
        R("upper_arm.%s" % sd, X, -1.2); R("upper_arm.%s" % sd, Y, -0.4 if sd == "L" else 0.4); R("forearm.%s" % sd, X, -0.6)
    R("spine", X, 0.1)
make_action("Jump", 10, jump)
def drive(t, f):
    for sd, sx in (("L", 1), ("R", -1)):
        R("thigh.%s" % sd, X, -1.45); R("shin.%s" % sd, X, 1.2); R("foot.%s" % sd, X, -0.2)
        R("upper_arm.%s" % sd, X, -0.85); R("upper_arm.%s" % sd, Y, -sx * 0.25); R("forearm.%s" % sd, X, -0.55)
    R("spine", X, -0.12); bob(-0.02)
make_action("Drive", 10, drive)
bpy.context.scene.frame_set(1)

# =============================================================== CAR
car_col = bpy.data.collections.new("Car"); bpy.context.scene.collection.children.link(car_col)
PAINT = mat("CarPaint", (0.62, 0.02, 0.02), 0.22, 0.55, coat=1.0)
BLACK = mat("CarBlack", (0.02, 0.02, 0.025), 0.45); TRIM = mat("CarTrim", (0.08, 0.08, 0.09), 0.3, 0.6)
GLASS = mat("CarGlass", (0.02, 0.025, 0.03), 0.05, 0.3, alpha=0.88); CHROME = mat("CarChrome", (0.9, 0.9, 0.92), 0.08, 1.0)
TIRE = mat("Tire", (0.03, 0.03, 0.03), 0.85); RIM = mat("Rim", (0.55, 0.56, 0.58), 0.25, 1.0)
HEAD = mat("CarHeadlight", (0.9, 0.95, 1.0), 0.1, emit=((0.9, 0.95, 1.0), 6.0))
BRAKE = mat("CarBrake", (0.5, 0.02, 0.02), 0.3, emit=((1.0, 0.05, 0.03), 1.5))
LEATHER = mat("CarLeather", (0.08, 0.06, 0.05), 0.5); CALIPER = mat("Caliper", (0.9, 0.7, 0.05), 0.4)

L, WB, TRK, WR = 4.5, 2.72, 0.83, 0.345
YF, YR = -WB / 2 - 0.05, WB / 2 - 0.05          # wheel centres (front at -Y)
def lerp(a, b, t): return a + (b - a) * t
def prof(s):
    """s=0 nose .. 1 tail -> (half width, z_bottom, z_top)"""
    w = 0.93 - 0.13 * (1 - min(1, s / 0.12)) ** 2 - 0.06 * (max(0, s - 0.9) / 0.1) ** 2
    zt = (0.56 + 0.26 * min(1, s / 0.36) if s < 0.36 else 0.84 + 0.08 * min(1, (s - 0.36) / 0.4))
    zt = zt - 0.06 * (max(0, s - 0.93) / 0.07)
    zb = 0.17
    for yc in (YF, YR):
        sc = (yc + L / 2) / L
        d = abs(s - sc) * L
        if d < 0.48:
            zb = max(zb, 0.17 + math.sqrt(max(0, 0.48 ** 2 - d * d)) * 0.95)
    return w, zb, zt

def loft(name, NS, NR, fn, m, coll, closed_ends=True):
    bm = bmesh.new(); rings = []
    for i in range(NS + 1):
        s = i / NS
        rings.append([bm.verts.new(p) for p in fn(s, NR)])
    for i in range(NS):
        a, b = rings[i], rings[i + 1]
        for j in range(NR):
            k = (j + 1) % NR
            f = bm.faces.new((a[j], a[k], b[k], b[j])); f.smooth = True
    if closed_ends:
        bm.faces.new(rings[0]); bm.faces.new(list(reversed(rings[-1])))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free(); me.materials.append(m)
    o = bpy.data.objects.new(name, me); coll.objects.link(o)
    sd = o.modifiers.new("Sub", "SUBSURF"); sd.levels = 1; sd.render_levels = 1
    return o

def body_ring(s, NR):
    w, zb, zt = prof(s); y = -L / 2 + s * L
    pts = []
    for j in range(NR):
        a = 2 * math.pi * j / NR
        c, sn = math.cos(a), math.sin(a)
        ex = 2 / 5.0
        x = w * math.copysign(abs(c) ** ex, c)
        zc = (zb + zt) / 2; hz = (zt - zb) / 2
        z = zc + hz * math.copysign(abs(sn) ** (2 / 4.0), sn)
        if z < zc:                                   # tuck the lower sides in
            x *= 1 - 0.08 * ((zc - z) / hz) ** 2
        pts.append((x, y, z))
    return pts
loft("CarBody", 44, 28, body_ring, PAINT, car_col)

def cabin_ring(s, NR):
    # greenhouse from s=0.37 (windshield base) to 0.83
    y = lerp(-L / 2 + 0.37 * L, -L / 2 + 0.85 * L, s)
    if s < 0.38:   zt = lerp(0.86, 1.24, (s / 0.38) ** 0.9)
    elif s < 0.62: zt = 1.24
    else:          zt = lerp(1.24, 0.94, ((s - 0.62) / 0.38) ** 1.1)
    wb_ = 0.8; wt = 0.6 if 0.3 < s < 0.7 else 0.55
    zb = 0.84 + 0.06 * s
    pts = []
    for j in range(NR):
        t = j / (NR - 1) if NR > 1 else 0
    corners = [(-wb_, zb), (wb_, zb), (wt, zt), (-wt, zt)]
    out = []
    for (x0, z0), (x1, z1) in zip(corners, corners[1:] + corners[:1]):
        for k in range(NR // 4):
            u = k / (NR // 4)
            out.append((lerp(x0, x1, u), y, lerp(z0, z1, u)))
    return out
loft("CarCabin", 16, 16, cabin_ring, GLASS, car_col)

mb = MB()
mb.box((0, 0.15, 1.245), (1.15, 1.25, 0.03), PAINT)                         # roof skin
for sx in (-1, 1):
    mb.box((sx * 0.86, -0.42, 0.96), (0.06, 0.04, 0.22), PAINT)            # A-pillar base / mirror stalk
    mb.box((sx * 0.98, -0.45, 0.98), (0.14, 0.06, 0.08), PAINT, smooth=True)     # mirror
    mb.box((sx * 0.64, -2.22, 0.58), (0.36, 0.06, 0.07), HEAD)             # headlights
    mb.box((sx * 0.62, 2.24, 0.82), (0.42, 0.05, 0.06), BRAKE)             # tail light bars
    mb.cyl((sx * 0.38, 2.2, 0.3), (sx * 0.38, 2.36, 0.3), 0.05, CHROME, seg=12)  # exhaust
    mb.box((sx * 0.94, 0.0, 0.42), (0.02, 1.6, 0.02), BLACK)               # side skirt line
    mb.box((sx * 0.935, -0.25, 0.68), (0.02, 0.01, 0.4), BLACK)            # door shut line
mb.box((0, -2.27, 0.36), (1.0, 0.04, 0.16), BLACK)                         # grille
mb.box((0, -2.29, 0.25), (0.34, 0.02, 0.12), mat("Plate", (0.95, 0.95, 0.9), 0.5))
mb.box((0, 2.24, 0.5), (0.34, 0.02, 0.12), MATS["Plate"])
mb.box((0, 2.05, 1.08), (1.7, 0.28, 0.03), BLACK)                          # spoiler wing
for sx in (-0.6, 0.6):
    mb.box((sx, 2.02, 0.98), (0.05, 0.14, 0.18), BLACK)
mb.box((0, 2.3, 0.22), (1.5, 0.06, 0.12), BLACK)                           # diffuser
# interior
for sx in (-0.38, 0.38):
    mb.box((sx, 0.32, 0.5), (0.5, 0.5, 0.12), LEATHER, smooth=True); mb.box((sx, 0.6, 0.85), (0.5, 0.12, 0.65), LEATHER, smooth=True)
mb.box((0, -0.42, 0.78), (1.5, 0.35, 0.18), BLACK)                         # dashboard
mb.box((0, 0.0, 0.55), (0.25, 1.0, 0.2), BLACK)                            # tunnel
deco = mb.obj("CarDetails", car_col)

# wheels + steering pivots
def wheel(name, x, y):
    mb = MB()
    mb.cyl((-0.13, 0, 0), (0.13, 0, 0), WR, TIRE, seg=32)
    mb.cyl((-0.135, 0, 0), (0.135, 0, 0), WR * 0.68, RIM, seg=32)
    for k in range(5):
        a = k * 2 * math.pi / 5
        mb.box((math.copysign(0.12, x), math.cos(a) * WR * 0.38, math.sin(a) * WR * 0.38), (0.03, 0.06, WR * 0.62), RIM)
    mb.cyl((math.copysign(0.1, x), 0, 0), (math.copysign(0.14, x), 0, 0), 0.06, CHROME, seg=12)
    o = mb.obj(name, car_col); o.location = (x, y, WR)
    return o
for nm, x, y, front in (("FL", TRK, YF, True), ("FR", -TRK, YF, True), ("RL", TRK, YR, False), ("RR", -TRK, YR, False)):
    w = wheel("Wheel_" + nm, x, y)
    mb = MB(); mb.box((math.copysign(0.0, x), 0.12, 0.1), (0.05, 0.12, 0.12), CALIPER); cal = mb.obj("Caliper_" + nm, car_col)
    if front:
        p = bpy.data.objects.new("FrontPivot_" + nm[1], None); p.location = (x, y, WR); car_col.objects.link(p)
        w.parent = p; w.location = (0, 0, 0); cal.parent = p
    else:
        cal.location = (x, y, WR)
    if not front:
        pass
mb = MB()
mb.cyl((0, 0, -0.02), (0, 0, 0.02), 0.19, BLACK, r2=0.19, seg=24); mb.box((0, 0, 0), (0.3, 0.04, 0.03), BLACK)
sw = mb.obj("SteeringWheel", car_col); sw.location = (0.38, -0.3, 0.92); sw.rotation_euler = (math.radians(-65), 0, 0)
for nm, loc in (("Seat_Driver", (0.38, 0.25, 0.44)), ("Exit_L", (1.6, 0.0, 0.0)), ("Cam_Chase", (0, 6.5, 2.4))):
    e = bpy.data.objects.new(nm, None); e.location = loc; car_col.objects.link(e)
root = bpy.data.objects.new("Car", None); car_col.objects.link(root)
for o in car_col.objects:
    if o is not root and o.parent is None:
        o.parent = root

# =============================================================== export
os.makedirs(OUT, exist_ok=True)
def export(path, objs, anim):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs:
        o.select_set(True)
    bpy.ops.export_scene.gltf(filepath=path, export_format="GLB", use_selection=True, export_apply=True, export_yup=True,
                              export_animations=anim, export_animation_mode="NLA_TRACKS" if anim else "ACTIONS",
                              export_skins=True, export_extras=True, export_lights=False)
    print("exported", path, os.path.getsize(path) // 1024, "KB")
export(os.path.join(OUT, "hero.glb"), [rig, body], True)
export(os.path.join(OUT, "car.glb"), list(car_col.objects), False)

if "--render" in argv:
    sc = bpy.context.scene
    for eng in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
        try: sc.render.engine = eng; break
        except TypeError: pass
    sc.render.resolution_x, sc.render.resolution_y = 1400, 700
    w = bpy.data.worlds.new("W"); sc.world = w; w.use_nodes = True
    w.node_tree.nodes["Background"].inputs[0].default_value = (0.6, 0.7, 0.8, 1)
    sun = bpy.data.objects.new("Sun", bpy.data.lights.new("Sun", "SUN")); sun.data.energy = 3.5
    sun.rotation_euler = (math.radians(50), 0, math.radians(30)); sc.collection.objects.link(sun)
    gnd = bpy.data.meshes.new("G"); bm = bmesh.new(); bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=20); bm.to_mesh(gnd)
    g = bpy.data.objects.new("G", gnd); sc.collection.objects.link(g); g.data.materials.append(mat("Ground", (0.4, 0.4, 0.4), 0.9))
    root.location = (-2.5, 0, 0); root.rotation_euler.z = math.radians(-35)
    rig.location = (1.4, 0, 0)
    cam = bpy.data.objects.new("C", bpy.data.cameras.new("C")); sc.collection.objects.link(cam); sc.camera = cam
    cam.location = (3.5, -9.5, 3.0); cam.rotation_euler = (Vector((-0.5, 0, 0.8)) - cam.location).to_track_quat("-Z", "Y").to_euler()
    tr = {t.name: t for t in rig.animation_data.nla_tracks}
    for anim, fr in (("Walk", 9), ("Run", 6), ("Drive", 3), ("Idle", 1)):
        for t in tr.values(): t.mute = t.name != anim
        sc.frame_set(fr)
        sc.render.filepath = os.path.join(OUT, "_preview_%s.png" % anim)
        bpy.ops.render.render(write_still=True)
