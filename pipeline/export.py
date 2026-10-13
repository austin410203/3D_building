# Export game-ready GLBs + the AI-readable asset catalog from TownKit.blend
#   blender -b TownKit.blend -P export.py -- [--only id1,id2] [--notown]
# Output:
#   export/glb/<asset_id>.glb      one building, centred at its own origin (plot centre, ground = 0, front = -Y / glTF +Z)
#   export/glb/island_town.glb     terrain + streets + props
#   export/glb/town_full.glb       everything as placed on the island (labels included)
#   export/catalog.json            machine-readable catalog (metadata, entrances, spawns, files, previews)
import bpy, os, sys, json, math
from mathutils import Matrix
SD = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(SD, ".."))
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
ONLY = set(argv[argv.index("--only") + 1].split(",")) if "--only" in argv else None
DRACO = "--draco" in argv
GLB = os.path.join(ROOT, "export", "glb_draco" if DRACO else "glb"); os.makedirs(GLB, exist_ok=True)
if DRACO:   # compressed variant: 512 px textures (in memory only, the .blend is not saved)
    for im in bpy.data.images:
        if im.size[0] > 512 and im.source == "FILE":
            im.scale(512, 512)

def kids(o):
    out = []
    for c in o.children:
        out.append(c); out += kids(c)
    return out

def export(path, objs):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs:
        try:
            o.hide_set(False); o.select_set(True)
        except RuntimeError:
            pass
    bpy.ops.export_scene.gltf(filepath=path, export_format="GLB", use_selection=True, export_extras=True,
                              export_apply=True, export_lights=True, export_cameras=False, export_animations=False,
                              export_yup=True, export_image_format="WEBP" if DRACO else "AUTO", export_image_quality=80, export_import_convert_lighting_mode="RAW",
                              **(dict(export_draco_mesh_compression_enable=True, export_draco_mesh_compression_level=7,
                                      export_draco_position_quantization=14, export_draco_normal_quantization=10,
                                      export_draco_texcoord_quantization=12) if DRACO else {}))
    return os.path.getsize(path)

def meta(root):
    d = {}
    for k in root.keys():
        v = root[k]
        if isinstance(v, str) and v[:1] in "[{":
            try: v = json.loads(v)
            except Exception: pass
        d[k] = v if isinstance(v, (str, int, float, list, dict, bool)) else str(v)
    return d

# one collider hint for engines: material "Collider" objects are already tagged kind=collider
cat = []
roots = sorted([o for o in bpy.data.objects if o.type == "EMPTY" and (o.name.startswith("BLD_") or o.name == "ENV_island")],
               key=lambda o: o.name)
for r in roots:
    aid = r.get("asset_id", r.name)
    if ONLY and aid not in ONLY:
        continue
    objs = [r] + kids(r)
    game = [o for o in objs if o.get("kind") != "label"]
    m0, ro = r.matrix_world.copy(), r.rotation_euler.copy()
    loc = r.location.copy()
    if r.name != "ENV_island":                       # export each building at the origin
        r.location = (0, 0, 0); r.rotation_euler = (0, 0, 0)
        bpy.context.view_layer.update()
    path = os.path.join(GLB, "%s.glb" % aid)
    size = export(path, game) if "--catalog-only" not in argv else (os.path.getsize(path) if os.path.exists(path) else 0)
    r.location = loc; r.rotation_euler = ro
    bpy.context.view_layer.update()
    d = meta(r)
    d["files"] = {"blend": "TownKit.blend", "blend_collection": "BLD_%s" % aid if r.name != "ENV_island" else r.users_collection[0].name,
                  "glb": "export/glb/%s.glb" % aid, "glb_kb": size // 1024,
                  "preview_day": "renders/%s_front_day.png" % aid, "preview_night": "renders/%s_front.png" % aid,
                  "preview_plan": "renders/%s_cut_day.png" % aid}
    d["object_counts"] = {}
    for o in objs:
        k = o.get("kind", o.type.lower())
        d["object_counts"][k] = d["object_counts"].get(k, 0) + 1
    cat.append(d)
    print("[export] %-24s %6d KB" % (aid, size // 1024))

if "--notown" not in argv and not ONLY and "--catalog-only" not in argv:
    allobjs = [o for o in bpy.data.objects if o.type in ("MESH", "EMPTY", "LIGHT") and o.name != "TK_Cam"]
    print("[export] town_full", export(os.path.join(GLB, "town_full.glb"), allobjs) // 1024, "KB")

if not ONLY and not DRACO:
    doc = {"kit": "TownKit", "version": 1, "units": "metres", "up_axis_blend": "Z", "up_axis_glb": "Y",
           "conventions": {
               "front": "local -Y in Blender (glTF +Z); plot centre at origin; ground level z=0",
               "object_name": "<asset_id>.<part>  e.g. cafe_container.Cafe_WallS",
               "custom_props (glTF extras)": {
                   "kind": "wall|floor|stair|door|window|railing|collider|furniture|light|light_fixture|sign|label|trim|structure|roof|elevator|spawn|vegetation|terrain|water|cable|ladder",
                   "walkable": "true on floors / stairs / ramps / decks",
                   "collider": "'ramp' (invisible stair ramp) or 'wall' (invisible rail blocker)",
                   "interact": "sit|sleep|open|use|cook|wash|shop|play|work|elevator|elevator_call|climb",
                   "openable": "hinge (rotate Z by open_angle deg from closed_rot_z) | slide (move by open_offset) | drawer | tilt",
                   "use_points": "JSON list of local [x,y,z] seat/use anchors",
                   "levels": "elevator car: JSON list of floor heights"}},
           "assets": cat}
    with open(os.path.join(ROOT, "export", "catalog.json"), "w", encoding="utf8") as fp:
        json.dump(doc, fp, ensure_ascii=False, indent=1)
    print("catalog written:", len(cat))
