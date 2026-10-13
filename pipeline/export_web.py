# Web/game export for the three.js client.
#   blender -b TownKit.blend -P export_web.py -- <out_models_dir> [--stats]
# Per building:  b_<id>.gltf (+ .bin)   shell (static, merged per material)
#                i_<id>.gltf            interior (furniture etc., distance culled in game)
#                doors live as separate nodes inside the shell file (extras: openable/open_angle/…)
# Shared:        textures/*.webp (512 px), env.gltf (terrain, roads, props), collider.glb (merged, untextured)
import bpy, bmesh, os, sys, json, math
from mathutils import Matrix, Vector
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = os.path.abspath(argv[0]) if argv and not argv[0].startswith("--") else None
STATS = "--stats" in argv

VISUAL_SKIP = {"collider", "spawn", "label"}      # labels are drawn as canvas sprites in the web client
INTERIOR = {"furniture"}
COLLIDE = {"wall", "floor", "terrain", "road", "sidewalk", "structure", "roof", "collider", "window", "elevator", "stair_ramp"}

def kids(o):
    out = []
    for c in o.children:
        out.append(c); out += kids(c)
    return out

# ---- 1. drop bevels + lights, scale textures
for o in bpy.data.objects:
    for m in list(getattr(o, "modifiers", [])):
        if m.type == "BEVEL":
            o.modifiers.remove(m)
for o in [o for o in bpy.data.objects if o.type == "LIGHT" or o.name == "TK_Cam"]:
    bpy.data.objects.remove(o)
def _tris(o):
    return sum(len(p.vertices) - 2 for p in o.data.polygons) if o.type == "MESH" else 0
for o in bpy.data.objects:
    if o.type != "MESH":
        continue
    n = _tris(o)
    txt = "_Txt" in o.name or o.name.endswith(("GateNeonA", "GateNeonB", "LobbyLogo", "Address", "SignBig")) or o.name.split(".")[-1].startswith("Price")
    ratio = 0.3 if (txt and n > 1500) else (0.45 if (o.get("kind") == "furniture" and n > 4000) else None)
    if ratio:
        d = o.modifiers.new("WebDecimate", "DECIMATE"); d.ratio = ratio
for im in bpy.data.images:
    if im.source == "FILE" and im.size[0] > 512:
        im.scale(512, 512)
dg = bpy.context.evaluated_depsgraph_get()

def kind_of(o):
    k = o.get("kind")
    if k:
        return k
    p = o.parent
    while p is not None and not p.name.startswith(("BLD_", "ENV_")):
        if p.get("kind"):
            return p.get("kind")
        p = p.parent
    return ""

def top_furniture(o):
    """furniture children (wardrobe doors, fridge doors) belong to their furniture"""
    p = o
    while p.parent is not None and not p.parent.name.startswith(("BLD_", "ENV_")):
        p = p.parent
    return p

class Joiner:
    def __init__(s):
        s.bm = bmesh.new(); s.mats = []; s.n = 0
    def add(s, o, mw=None):
        if o.type not in ("MESH", "FONT", "CURVE"):
            return
        oe = o.evaluated_get(dg)
        try:
            me = bpy.data.meshes.new_from_object(oe)
        except RuntimeError:
            return
        me.transform(mw or o.matrix_world)
        if mw is not None and mw.determinant() < 0 or (mw is None and o.matrix_world.determinant() < 0):
            me.flip_normals()
        remap = []
        for m in me.materials:
            if m is None:
                remap.append(0); continue
            if m not in s.mats:
                s.mats.append(m)
            remap.append(s.mats.index(m))
        if remap:
            idx = [0] * len(me.polygons); me.polygons.foreach_get("material_index", idx)
            me.polygons.foreach_set("material_index", [remap[i] if i < len(remap) else 0 for i in idx])
        if not me.uv_layers:
            me.uv_layers.new(name="UVMap")
        for uv in list(me.uv_layers):
            if uv.name != "UVMap" and len(me.uv_layers) > 1:
                me.uv_layers.remove(uv)
        me.uv_layers[0].name = "UVMap"
        s.bm.from_mesh(me)
        bpy.data.meshes.remove(me)
        s.n += 1
    def obj(s, name, coll, local=None):
        if s.n == 0:
            s.bm.free(); return None
        me = bpy.data.meshes.new(name); s.bm.to_mesh(me); s.bm.free()
        for m in s.mats:
            me.materials.append(m)
        if local is not None:
            me.transform(local.inverted())
        o = bpy.data.objects.new(name, me)
        if local is not None:
            o.matrix_world = local
        coll.objects.link(o)
        return o

def box_from(o):
    """oriented bounding box of an object as a mesh in world space (cheap furniture collider)"""
    bb = [o.matrix_world @ Vector(c) for c in o.bound_box]
    bm = bmesh.new()
    vs = [bm.verts.new(p) for p in bb]
    for f in ((0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)):
        try: bm.faces.new([vs[i] for i in f])
        except ValueError: pass
    return bm

web = bpy.data.collections.new("WEB"); bpy.context.scene.collection.children.link(web)
roots = [o for o in bpy.data.objects if o.type == "EMPTY" and (o.name.startswith("BLD_") or o.name == "ENV_island")]
col_all = Joiner()
manifest = {"buildings": [], "env": None}
stats = []
for r in roots:
    bid = r.get("asset_id", "island_town")
    objs = [o for o in kids(r) if o.type in ("MESH", "FONT", "CURVE")]
    shell, inter, doors = Joiner(), Joiner(), []
    tri = [0, 0]
    for o in objs:
        k = kind_of(o)
        if o.get("collider") == "ramp":
            col_all.add(o); continue
        if k in VISUAL_SKIP:
            if k == "collider":
                col_all.add(o)
            continue
        top = top_furniture(o)
        tk = top.get("kind", "")
        if k == "door" and o.get("openable") in ("hinge", "slide") and tk != "furniture":
            doors.append(o); continue
        if tk == "furniture" or k == "furniture":
            inter.add(o)
            if o is top and o.get("kind") == "furniture" and max(o.dimensions) > 0.25:
                b = box_from(o); me = bpy.data.meshes.new("tmpbox"); b.to_mesh(me); b.free(); col_all.bm.from_mesh(me); bpy.data.meshes.remove(me)
            continue
        if k == "stair":
            shell.add(o); continue                     # visual steps; collision uses the ramp colliders
        shell.add(o)
        if k in COLLIDE and o.get("kind") != "label":
            col_all.add(o)
    so = shell.obj("S_" + bid, web)
    io = inter.obj("I_" + bid, web)
    dobjs = []
    for d in doors:
        j = Joiner(); j.add(d)
        do = j.obj("D_" + d.name.replace(".", "_"), web, local=d.matrix_world.copy())
        if do:
            for kk in ("openable", "open_angle", "closed_rot_z", "open_offset", "interact"):
                if kk in d.keys():
                    v = d[kk]; do[kk] = v if isinstance(v, (int, float, str)) else json.dumps(list(v))
            dobjs.append(do)
    meta = {k: r[k] for k in r.keys() if isinstance(r[k], (str, int, float))}
    if so:
        for k, v in meta.items():
            so[k] = v
    for o in [so, io] + dobjs:
        if o: tri[0 if o is not io else 1] += sum(len(p.vertices) - 2 for p in o.data.polygons)
    stats.append((bid, tri[0], tri[1], len(dobjs)))
    ent = dict(id=bid, shell="b_%s.gltf" % bid, interior=("i_%s.gltf" % bid) if io else None,
               pos=list(r.matrix_world.translation), rotz=r.rotation_euler.z,
               name_zh=meta.get("name_zh", ""), name_en=meta.get("name_en", ""), style=meta.get("style", ""),
               style_zh=meta.get("style_zh", ""), tier=meta.get("tier", ""), size=json.loads(meta.get("size_m", "[0,0,0]")),
               description=meta.get("description", ""), category=meta.get("category", ""),
               spawns=json.loads(meta.get("spawns", "[]")) if "spawns" in meta else [])
    if bid == "island_town":
        manifest["env"] = ent
    else:
        manifest["buildings"].append(ent)
    r["_web"] = json.dumps([o.name for o in [so, io] + dobjs if o])
colo = col_all.obj("COLLIDER", web)
print("collider tris", sum(len(p.vertices) - 2 for p in colo.data.polygons))
tot = [0, 0]
for s in stats:
    tot[0] += s[1]; tot[1] += s[2]
    print("%-24s shell %7d  interior %7d  doors %3d" % s)
print("TOTAL shell %d interior %d" % tuple(tot))
if STATS or not OUT:
    sys.exit(0)

# ---- export
os.makedirs(OUT, exist_ok=True)
def export(path, objs, fmt="GLTF_SEPARATE", draco=True, textures=True):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs:
        o.select_set(True)
    kw = dict(filepath=path, export_format=fmt, use_selection=True, export_extras=True, export_apply=True,
              export_lights=False, export_cameras=False, export_animations=False, export_yup=True,
              export_draco_mesh_compression_enable=draco, export_draco_mesh_compression_level=7,
              export_draco_position_quantization=14, export_draco_normal_quantization=8, export_draco_texcoord_quantization=11)
    if fmt == "GLTF_SEPARATE":
        kw.update(export_texture_dir="textures", export_image_format="WEBP", export_image_quality=78)
    if not textures:
        kw.update(export_materials="NONE")
    bpy.ops.export_scene.gltf(**kw)

for r in roots:
    names = json.loads(r["_web"]); bid = r.get("asset_id", "island_town")
    sh = [bpy.data.objects[n] for n in names if not n.startswith("I_")]
    it = [bpy.data.objects[n] for n in names if n.startswith("I_")]
    export(os.path.join(OUT, ("env.gltf" if bid == "island_town" else "b_%s.gltf" % bid)), sh)
    if it:
        export(os.path.join(OUT, "i_%s.gltf" % bid), it)
    print("exported", bid)
manifest["env"]["shell"] = "env.gltf"
sc = bpy.context.scene
manifest["roads"] = json.loads(sc.get("tk_roads", "[]")); manifest["isl"] = json.loads(sc.get("tk_isl", "[300, 240]"))
export(os.path.join(OUT, "collider.glb"), [colo], fmt="GLB", textures=False)
json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf8"), ensure_ascii=False)
print("done", OUT)
