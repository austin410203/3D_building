# TownKit building framework (exec'd after lib_core.py in one namespace).
# Units: metres. Each building is authored in LOCAL coordinates: plot centre at (0,0), ground z=0,
# main facade facing -Y ("S" side). end_building() moves the root empty onto its plot.
import bpy, bmesh, math, json, os
from mathutils import Vector, Matrix

FONT_PATH = r"C:\Windows\Fonts\msjhbd.ttc"

# --------------------------------------------------------------------------- materials
MATDEF = {
    # name: (color(sRGB), rough, metal, tex, tile_m, normal_strength)
    "Plaster": ((0.93, 0.89, 0.80), .85, 0, "plaster_ext", 2.5, .6),
    "PlasterInt": ((0.94, 0.91, 0.85), .9, 0, "plaster_int", 2.5, .3),
    "Ceiling": ((0.97, 0.96, 0.93), .9, 0, "ceiling", 2.5, .2),
    "Concrete": ((0.6, 0.6, 0.58), .9, 0, "concrete", 2.0, .7),
    "Block": ((0.6, 0.6, 0.62), .9, 0, "block", 1.2, .8),
    "Brick": ((0.6, 0.3, 0.2), .9, 0, "brick_red", 0.9, 1.0),
    "BrickDark": ((0.3, 0.27, 0.26), .9, 0, "brick_dark", 0.9, 1.0),
    "BrickCream": ((0.86, 0.8, 0.68), .9, 0, "brick_cream", 0.9, 1.0),
    "MosaicBeige": ((0.85, 0.8, 0.7), .5, 0, "mosaic_beige", 0.9, .8),
    "MosaicPink": ((0.85, 0.66, 0.62), .5, 0, "mosaic_pink", 0.9, .8),
    "SidingTeal": ((0.22, 0.55, 0.55), .7, 0, "siding_teal", 1.6, 1.0),
    "SidingWhite": ((0.9, 0.88, 0.82), .7, 0, "siding_white", 1.6, 1.0),
    "ContYellow": ((0.92, 0.72, 0.1), .5, .3, "cont_yellow", 2.4, 1.2),
    "ContBlue": ((0.12, 0.28, 0.62), .5, .3, "cont_blue", 2.4, 1.2),
    "ContBlack": ((0.1, 0.1, 0.12), .5, .3, "cont_black", 2.4, 1.2),
    "ContGrey": ((0.62, 0.64, 0.66), .5, .3, "cont_grey", 2.4, 1.2),
    "TinRust": ((0.55, 0.5, 0.46), .7, .3, "tin_rust", 2.0, 1.2),
    "PanelCopper": ((0.62, 0.36, 0.18), .45, .6, "panel_copper", 2.4, .8),
    "PanelSteel": ((0.4, 0.44, 0.48), .45, .6, "panel_steel", 2.4, .8),
    "PanelDark": ((0.16, 0.18, 0.22), .5, .4, "panel_dark", 2.4, .8),
    "GrimeTeal": ((0.28, 0.38, 0.4), .7, .2, "grime_teal", 3.0, .8),
    "GrimeBlue": ((0.22, 0.34, 0.5), .7, .2, "grime_blue", 3.0, .8),
    "Stone": ((0.65, 0.63, 0.6), .8, 0, "stone", 2.0, .6),
    "StoneTile": ((0.62, 0.6, 0.56), .7, 0, "stone_tile", 1.2, .8),
    "Cobble": ((0.55, 0.52, 0.48), .85, 0, "cobble", 2.0, 1.2),
    "Marble": ((0.95, 0.94, 0.92), .15, 0, "marble_white", 1.5, .2),
    "MarbleBlack": ((0.1, 0.1, 0.11), .15, 0, "marble_black", 1.5, .2),
    "RoofTile": ((0.7, 0.25, 0.18), .7, 0, "roof_clay", 1.0, 1.0),
    "SlateBlue": ((0.3, 0.38, 0.46), .6, 0, "slate_blue", 1.2, 1.0),
    "SlateDark": ((0.22, 0.22, 0.24), .6, 0, "slate_dark", 1.2, 1.0),
    "WoodFloor": ((0.6, 0.42, 0.26), .5, 0, "wood_floor", 1.2, .6),
    "Parquet": ((0.55, 0.38, 0.22), .4, 0, "parquet", 1.2, .5),
    "TileWhite": ((0.9, 0.89, 0.85), .2, 0, "tile_white", 0.9, .6),
    "TileBlue": ((0.55, 0.72, 0.86), .2, 0, "tile_blue", 0.6, .6),
    "CarpetGrey": ((0.42, 0.42, 0.44), 1, 0, "carpet_grey", 1.0, .5),
    "CarpetRed": ((0.55, 0.14, 0.12), 1, 0, "carpet_red", 1.0, .5),
    "Tatami": ((0.7, 0.7, 0.45), .8, 0, "tatami", 0.9, .5),
    "WoodLight": ((0.8, 0.62, 0.42), .55, 0, "wood_light", 1.0, .4),
    "WoodDark": ((0.45, 0.3, 0.18), .55, 0, "wood_dark", 1.0, .4),
    "FabricRed": ((0.8, 0.3, 0.28), .95, 0, "fabric_red", 0.5, .5),
    "FabricBlue": ((0.3, 0.45, 0.75), .95, 0, "fabric_blue", 0.5, .5),
    "FabricNavy": ((0.25, 0.3, 0.55), .95, 0, "fabric_navy", 0.5, .5),
    "FabricGreen": ((0.4, 0.58, 0.4), .95, 0, "fabric_green", 0.5, .5),
    "FabricWhite": ((0.95, 0.95, 0.93), .95, 0, "fabric_white", 0.5, .5),
    "FabricBeige": ((0.8, 0.74, 0.62), .95, 0, "fabric_beige", 0.5, .5),
    "Asphalt": ((0.2, 0.2, 0.21), .9, 0, "asphalt", 4.0, .5),
    "Grass": ((0.3, 0.5, 0.2), .95, 0, "grass", 3.0, .6),
    "Sand": ((0.82, 0.74, 0.56), .95, 0, "sand", 4.0, .6),
    "Snow": ((0.92, 0.94, 0.98), .7, 0, "snow", 4.0, .5),
    "Bark": ((0.35, 0.25, 0.17), .9, 0, "bark", 1.0, 1.0),
    "Leaf": ((0.3, 0.5, 0.2), .8, 0, "leaf", 1.0, .6),
    "Paper": ((0.95, 0.94, 0.9), .9, 0, "paper", 1.0, .2),
    "PaintRed": ((0.8, 0.26, 0.23), .6, 0, "paint_red", 1.0, .3),
    "PaintTeal": ((0.3, 0.62, 0.66), .6, 0, "paint_teal", 1.0, .3),
    # untextured
    "Frame": ((0.16, 0.16, 0.17), .45, .6, None, 1, 0),
    "FrameWhite": ((0.9, 0.9, 0.88), .4, .1, None, 1, 0),
    "FrameAlu": ((0.7, 0.72, 0.74), .35, .8, None, 1, 0),
    "Metal": ((0.62, 0.64, 0.66), .35, .9, None, 1, 0),
    "MetalDark": ((0.22, 0.23, 0.25), .45, .8, None, 1, 0),
    "Chrome": ((0.9, 0.9, 0.92), .08, 1, None, 1, 0),
    "Brass": ((0.85, 0.65, 0.3), .25, 1, None, 1, 0),
    "Rust": ((0.45, 0.24, 0.13), .8, .4, None, 1, 0),
    "Black": ((0.03, 0.03, 0.035), .5, 0, None, 1, 0),
    "White": ((0.93, 0.93, 0.91), .5, 0, None, 1, 0),
    "Ceramic": ((0.96, 0.96, 0.95), .08, 0, None, 1, 0),
    "Plastic": ((0.85, 0.85, 0.82), .4, 0, None, 1, 0),
    "PlasticDark": ((0.12, 0.12, 0.13), .4, 0, None, 1, 0),
    "PlasticRed": ((0.8, 0.12, 0.1), .35, 0, None, 1, 0),
    "PlasticBlue": ((0.1, 0.3, 0.75), .35, 0, None, 1, 0),
    "PlasticYellow": ((0.95, 0.75, 0.1), .35, 0, None, 1, 0),
    "PlasticGreen": ((0.2, 0.6, 0.3), .35, 0, None, 1, 0),
    "Rubber": ((0.06, 0.06, 0.06), .9, 0, None, 1, 0),
    "Leather": ((0.35, 0.2, 0.12), .5, 0, None, 1, 0),
    "LeatherBlack": ((0.05, 0.05, 0.05), .45, 0, None, 1, 0),
    "Terracotta": ((0.72, 0.38, 0.24), .85, 0, None, 1, 0),
    "PlantGreen": ((0.2, 0.42, 0.16), .7, 0, None, 1, 0),
    "PlantDark": ((0.1, 0.26, 0.1), .7, 0, None, 1, 0),
    "Soil": ((0.2, 0.13, 0.08), 1, 0, None, 1, 0),
    "RoofRed": ((0.62, 0.2, 0.15), .7, 0, None, 1, 0),
    "AwningRed": ((0.78, 0.15, 0.12), .8, 0, None, 1, 0),
    "AwningGreen": ((0.2, 0.5, 0.3), .8, 0, None, 1, 0),
    "AwningWhite": ((0.94, 0.93, 0.9), .8, 0, None, 1, 0),
    "Mattress": ((0.95, 0.94, 0.9), .9, 0, None, 1, 0),
    "BookA": ((0.7, 0.2, 0.16), .7, 0, None, 1, 0), "BookB": ((0.18, 0.36, 0.6), .7, 0, None, 1, 0),
    "BookC": ((0.85, 0.7, 0.3), .7, 0, None, 1, 0), "BookD": ((0.25, 0.5, 0.3), .7, 0, None, 1, 0),
    "Water": ((0.05, 0.18, 0.25), .02, 0, None, 1, 0),
    "PoolWater": ((0.2, 0.6, 0.75), .02, 0, None, 1, 0),
    "Solar": ((0.05, 0.08, 0.2), .1, .5, None, 1, 0),
    "Collider": ((1, 0, 1), 1, 0, None, 1, 0),
}
GLASS = {"Glass": ((0.8, 0.9, 0.95), 0.25), "GlassDark": ((0.25, 0.35, 0.4), 0.55),
         "GlassBlue": ((0.4, 0.6, 0.8), 0.4), "GlassFrost": ((0.9, 0.92, 0.94), 0.75)}
GLOWDEF = {  # name: (sRGB colour, strength)
    "LightWarm": ((1.0, 0.8, 0.55), 8), "LightCool": ((0.85, 0.93, 1.0), 8), "LightSoft": ((1.0, 0.9, 0.75), 3),
    "NeonPink": ((1.0, 0.2, 0.7), 12), "NeonCyan": ((0.1, 0.9, 1.0), 12), "NeonYellow": ((1.0, 0.85, 0.2), 10),
    "NeonRed": ((1.0, 0.15, 0.1), 12), "NeonGreen": ((0.3, 1.0, 0.4), 10), "NeonPurple": ((0.65, 0.3, 1.0), 12),
    "NeonBlue": ((0.2, 0.4, 1.0), 12), "NeonOrange": ((1.0, 0.5, 0.1), 10),
    "Lantern": ((1.0, 0.45, 0.15), 6), "Screen": ((0.5, 0.8, 1.0), 4), "ScreenGreen": ((0.4, 1.0, 0.6), 4),
    "LabelGlow": ((1.0, 0.95, 0.8), 3), "LabelGlowCyan": ((0.6, 1.0, 1.0), 3), "LED": ((0.3, 1.0, 0.5), 15),
}

def tk_materials():
    for k, (c, r, mt, tex, tile, ns) in MATDEF.items():
        m = mat(k, srgb(*c), r, mt, tex=tex, tile=tile, nstr=ns)
    for k, (c, a) in GLASS.items():
        m = mat(k, srgb(*c), 0.04, 0, a)
        b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        try: _inp(b, "IOR").default_value = 1.45
        except Exception: pass
        m["glass"] = True
    for k, (c, s) in GLOWDEF.items():
        glow_mat(k, c, s)
    # tone down saturated ground textures
    for k, sat, val in (("Grass", 0.7, 0.75), ("Leaf", 0.8, 0.85)):
        nt = M[k].node_tree
        ti = next((n for n in nt.nodes if n.type == "TEX_IMAGE" and n.image and n.image.colorspace_settings.name != "Non-Color"), None)
        if ti:
            b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
            hs = nt.nodes.new("ShaderNodeHueSaturation")
            hs.inputs["Saturation"].default_value = sat; hs.inputs["Value"].default_value = val
            nt.links.new(ti.outputs["Color"], hs.inputs["Color"]); nt.links.new(hs.outputs["Color"], _inp(b, "Base Color"))
    # water: dark glossy with wave bump
    w = M["Water"]; nt = w.node_tree
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    nz = nt.nodes.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 3.0
    bp = nt.nodes.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = 0.15
    nt.links.new(nz.outputs["Fac"], bp.inputs["Height"]); nt.links.new(bp.outputs["Normal"], _inp(b, "Normal"))

# --------------------------------------------------------------------------- building context
CUR = None
BUILDINGS = []
LIGHT_K = 1.8          # global interior light multiplier
LABELS_ON = True

class Bld:
    pass

def begin_building(bid, name_zh, name_en, style, style_zh, tier, category, game_styles, desc, floors, plot):
    global CUR
    b = Bld()
    b.bid = bid; b.n = 0
    top = coll("TownKit_Buildings")
    b.col = coll("BLD_" + bid, top)
    b.lab = coll("LBL_" + bid, b.col)
    b.root = bpy.data.objects.new("BLD_" + bid, None)
    b.root.empty_display_type = "ARROWS"; b.root.empty_display_size = 2
    b.col.objects.link(b.root)
    b.meta = dict(asset_id=bid, name_zh=name_zh, name_en=name_en, style=style, style_zh=style_zh, tier=tier,
                  category=category, game_styles=game_styles, description=desc, floors=floors, plot=plot)
    b.entrances = []; b.lights = 0; b.spawns = []
    CUR = b
    return b

def _nm(name):
    return "%s.%s" % (CUR.bid, name)

def adopt(o, kind=None, **props):
    """parent an object to the current building root and tag it"""
    if CUR.col not in o.users_collection:
        for c in list(o.users_collection):
            c.objects.unlink(o)
        CUR.col.objects.link(o)
    o.parent = CUR.root
    if kind:
        o["kind"] = kind
    for k, v in props.items():
        o[k] = v
    return o

def ob(name, boxes, mats, kind=None, **props):
    o = mesh_obj(_nm(name), boxes, mats, CUR.col)
    return adopt(o, kind, **props)

# --------------------------------------------------------------------------- mesh builder (local frame)
class MB:
    """Compose primitives in a local frame, then emit one multi-material object."""
    def __init__(s):
        s.bm = bmesh.new(); s.mats = []
    def mi(s, m):
        if m not in s.mats: s.mats.append(m)
        return s.mats.index(m)
    def _tag(s, verts, m, smooth=False):
        i = s.mi(m)
        for f in {f for v in verts for f in v.link_faces}:
            f.material_index = i; f.smooth = smooth
        return s
    def box(s, x1, y1, z1, x2, y2, z2, m):
        vs = _add_box(s.bm, (x1, y1, z1, x2, y2, z2))
        return s._tag(vs, m) if vs else s
    def bc(s, cx, cy, z1, w, d, h, m):     # centred box
        return s.box(cx - w / 2, cy - d / 2, z1, cx + w / 2, cy + d / 2, z1 + h, m)
    def cyl(s, x, y, z1, z2, r, m, seg=24, r2=None, axis="z"):
        mtx = Matrix.Translation((0, 0, (z2 - z1) / 2))
        res = bmesh.ops.create_cone(s.bm, cap_ends=True, segments=seg, radius1=r, radius2=r if r2 is None else r2,
                                    depth=z2 - z1, matrix=mtx)
        vs = res["verts"]
        if axis == "x":
            bmesh.ops.rotate(s.bm, verts=vs, cent=(0, 0, 0), matrix=Matrix.Rotation(math.pi / 2, 3, "Y"))
        elif axis == "y":
            bmesh.ops.rotate(s.bm, verts=vs, cent=(0, 0, 0), matrix=Matrix.Rotation(-math.pi / 2, 3, "X"))
        bmesh.ops.translate(s.bm, verts=vs, vec=(x, y, z1) if axis == "z" else (x, y, z1))
        return s._tag(vs, m, smooth=True)
    def sph(s, x, y, z, r, m, sx=1, sy=1, sz=1, sub=2):
        res = bmesh.ops.create_icosphere(s.bm, subdivisions=sub, radius=r)
        vs = res["verts"]
        bmesh.ops.scale(s.bm, verts=vs, vec=(sx, sy, sz))
        bmesh.ops.translate(s.bm, verts=vs, vec=(x, y, z))
        return s._tag(vs, m, smooth=True)
    def prism(s, pts, y1, y2, m, plane="xz"):
        """extrude polygon pts (in xz plane) along y from y1..y2 (plane='yz': pts in yz, along x)"""
        def v(p, c):
            return (p[0], c, p[1]) if plane == "xz" else (c, p[0], p[1])
        a = [s.bm.verts.new(v(p, y1)) for p in pts]; b = [s.bm.verts.new(v(p, y2)) for p in pts]
        s.bm.faces.new(a); s.bm.faces.new(list(reversed(b)))
        for i in range(len(pts)):
            j = (i + 1) % len(pts)
            s.bm.faces.new((a[i], a[j], b[j], b[i]))
        return s._tag(a + b, m)
    def quad(s, pts, m, thick=0.0):
        vs = [s.bm.verts.new(p) for p in pts]
        if thick:
            vb = [s.bm.verts.new((p[0], p[1], p[2] - thick)) for p in pts]
            s.bm.faces.new(vs); s.bm.faces.new(list(reversed(vb)))
            for i in range(len(pts)):
                j = (i + 1) % len(pts); s.bm.faces.new((vs[i], vb[i], vb[j], vs[j]))
            vs = vs + vb
        else:
            s.bm.faces.new(vs)
        return s._tag(vs, m)
    def obj(s, name, x=0, y=0, z=0, rot=0, kind=None, parent=True, **props):
        bmesh.ops.recalc_face_normals(s.bm, faces=s.bm.faces)
        me = bpy.data.meshes.new(_nm(name)); s.bm.to_mesh(me); s.bm.free()
        for m in s.mats:
            me.materials.append(M[m])
        o = bpy.data.objects.new(_nm(name), me)
        o.location = (x, y, z); o.rotation_euler.z = math.radians(rot)
        CUR.col.objects.link(o)
        if parent:
            adopt(o, kind, **props)
        return o

def furn(name, mb, x, y, z=0, rot=0, interact=None, **props):
    CUR.n += 1
    o = mb.obj("%s_%02d" % (name, CUR.n), x, y, z, rot, kind="furniture", **props)
    if interact:
        o["interact"] = interact
    return o

# --------------------------------------------------------------------------- walls / openings
SIDE = {"S": ("x", -1), "N": ("x", 1), "W": ("y", -1), "E": ("y", 1)}

def ring(name, x1, y1, x2, y2, z1, z2, ext="Plaster", intm="PlasterInt", t=0.2, cl=0.03, ops=None, sides="SNWE"):
    """Exterior walls of a storey. ops = {side: [(a1, a2, zb, zt, kind), ...]} (absolute coordinates).
    kind: win | win3 | slide | grille | shop | door | door_glass | door_double | roller | open"""
    ops = ops or {}
    res = {}
    spec = {
        "S": ("x", x1, x2, y1, y1 + t, y1 - cl, y1, x1 - cl, x2 + cl),
        "N": ("x", x1, x2, y2 - t, y2, y2, y2 + cl, x1 - cl, x2 + cl),
        "W": ("y", y1 + t, y2 - t, x1, x1 + t, x1 - cl, x1, y1, y2),
        "E": ("y", y1 + t, y2 - t, x2 - t, x2, x2, x2 + cl, y1, y2),
    }
    for sd in sides:
        ax, a1, a2, c1, c2, k1, k2, ka1, ka2 = spec[sd]
        o = [(p[0], p[1], p[2], p[3]) for p in ops.get(sd, [])]
        if ext == intm or not cl:
            cc1, cc2 = (min(c1, k1), max(c2, k2)) if cl else (c1, c2)
            w = wall(_nm("%s_Wall%s" % (name, sd)), ax, a1, a2, cc1, cc2, z1, z2, ext, CUR.col, o)
            adopt(w, "wall")
        else:
            w = wall(_nm("%s_Wall%s" % (name, sd)), ax, a1, a2, c1, c2, z1, z2, intm, CUR.col, o)
            adopt(w, "wall")
            w2 = wall(_nm("%s_Clad%s" % (name, sd)), ax, ka1, ka2, k1, k2, z1, z2, ext, CUR.col, o)
            adopt(w2, "wall")
        res[sd] = w
        cmin, cmax = min(c1, k1), max(c2, k2)
        for i, p in enumerate(ops.get(sd, [])):
            kind = p[4] if len(p) > 4 else "win"
            fill("%s_%s%d" % (name, sd, i), sd, cmin, cmax, p[0], p[1], p[2], p[3], kind, frame=p[5] if len(p) > 5 else "Frame")
    return res

def iwall(name, axis, a1, a2, c, z1, z2, t=0.12, m="PlasterInt", ops=()):
    """interior partition centred on c. ops: (a1, a2, zb, zt, kind) with kind door/open"""
    o = [(p[0], p[1], p[2], p[3]) for p in ops]
    w = wall(_nm(name), axis, a1, a2, c - t / 2, c + t / 2, z1, z2, m, CUR.col, o)
    adopt(w, "wall")
    for i, p in enumerate(ops):
        kind = p[4] if len(p) > 4 else "door"
        side = "S" if axis == "x" else "W"
        fill("%s_%d" % (name, i), side, c - t / 2, c + t / 2, p[0], p[1], p[2], p[3], kind, interior=True)
    return w

def _b(axis, p1, p2, c1, c2, q1, q2):
    return (p1, c1, q1, p2, c2, q2) if axis == "x" else (c1, p1, q1, c2, p2, q2)

def fill(name, side, c1, c2, a1, a2, zb, zt, kind, interior=False, frame="Frame"):
    axis, sgn = SIDE[side]
    if kind == "open":
        return
    cm = (c1 + c2) / 2
    co = c1 if sgn < 0 else c2          # outer face
    ci = c2 if sgn < 0 else c1          # inner face
    mb = MB()
    def B(p1, p2, q1, q2, d1, d2, m):   # box in wall frame: along-axis p, height q, depth d (absolute c)
        x = _b(axis, p1, p2, min(d1, d2), max(d1, d2), q1, q2)
        mb.box(*x, m)
    f = 0.06
    if kind in ("win", "win3", "grille", "shop"):
        fd1, fd2 = cm - 0.04, cm + 0.04
        fm = frame if (kind != "shop" or frame != "Frame") else "FrameAlu"
        B(a1, a1 + f, zb, zt, fd1, fd2, fm); B(a2 - f, a2, zb, zt, fd1, fd2, fm)
        B(a1, a2, zb, zb + f, fd1, fd2, fm); B(a1, a2, zt - f, zt, fd1, fd2, fm)
        n = {"win": 2, "grille": 2, "win3": 3, "shop": max(1, round((a2 - a1) / 1.4))}[kind]
        for i in range(1, n):
            p = a1 + (a2 - a1) * i / n
            B(p - 0.025, p + 0.025, zb, zt, fd1, fd2, fm)
        if kind in ("win", "win3", "grille") and zt - zb > 1.2:
            tz = zt - (zt - zb) * 0.28                           # transom bar
            B(a1, a2, tz - 0.02, tz + 0.02, fd1, fd2, fm)
        if kind == "shop" and zt - zb > 2.6:
            B(a1, a2, zb + 2.3, zb + 2.36, fd1, fd2, fm)
        B(a1 + f, a2 - f, zb + f, zt - f, cm - 0.006, cm + 0.006, "Glass")
        if not interior and kind != "shop":                    # sills
            B(a1 - 0.04, a2 + 0.04, zb - 0.05, zb, co, co + sgn * 0.06, "Stone" if frame != "FrameWood" else "WoodDark")
            B(a1, a2, zb - 0.02, zb + 0.01, ci, ci - sgn * 0.04, "WoodLight")
        if kind == "grille":                                   # Taiwanese iron security cage
            o1, o2 = co, co + sgn * 0.22
            gm = "MetalDark"
            B(a1 - 0.05, a2 + 0.05, zb - 0.05, zb - 0.02, o1, o2, gm)
            B(a1 - 0.05, a2 + 0.05, zt + 0.02, zt + 0.05, o1, o2, gm)
            nb = max(3, int((a2 - a1) / 0.12))
            for i in range(nb + 1):
                p = a1 - 0.05 + (a2 - a1 + 0.1) * i / nb
                B(p - 0.008, p + 0.008, zb - 0.02, zt + 0.02, o2 - sgn * 0.016, o2, gm)
            for q in (zb + (zt - zb) * 0.33, zb + (zt - zb) * 0.66):
                B(a1 - 0.05, a2 + 0.05, q - 0.01, q + 0.01, o2 - sgn * 0.02, o2, gm)
            for p in (a1 - 0.05, a2 + 0.03):
                B(p, p + 0.02, zb - 0.02, zt + 0.02, o1, o2, gm)
        mb.obj(name + "_Win", kind="window")
        return
    if kind == "slide":
        window(_nm(name), axis, a1, a2, c1, c2, zb, zt, CUR.col)
        for o in [o for o in CUR.col.objects if o.name.startswith(_nm(name)) and o.parent is None]:
            adopt(o, "window")
        return
    if kind in ("door", "door_glass", "door_double", "door_metal"):
        # casing
        cm_ = "WoodDark" if kind in ("door", "door_double") else "FrameAlu"
        B(a1 - 0.05, a1, zb, zt + 0.05, c1 - 0.01, c2 + 0.01, cm_)
        B(a2, a2 + 0.05, zb, zt + 0.05, c1 - 0.01, c2 + 0.01, cm_)
        B(a1 - 0.05, a2 + 0.05, zt, zt + 0.05, c1 - 0.01, c2 + 0.01, cm_)
        if not interior:
            B(a1 - 0.05, a2 + 0.05, zb - 0.02, zb + 0.015, co + sgn * 0.12, ci, "Stone")   # threshold
        mb.obj(name + "_Casing", kind="trim")
        leaves = [(a1, a2, False)] if kind != "door_double" else [(a1, (a1 + a2) / 2, False), ((a1 + a2) / 2, a2, True)]
        swing = {"S": 1, "N": -1, "W": -1, "E": 1}[side]
        for k, (p1, p2, hend) in enumerate(leaves):
            _door_leaf(name + "_Door%d" % k, axis, p1, p2, cm, zb, zt, kind, swing, hend, interior,
                       None if frame == "Frame" else frame)
        CUR.entrances.append(dict(name=_nm(name), side=side, a=(a1 + a2) / 2, z=zb, interior=interior))
        return
    if kind == "roller":   # shop shutter rolled up: housing box + guide rails
        B(a1 - 0.08, a2 + 0.08, zt, zt + 0.35, co, co + sgn * 0.3, "MetalDark")
        B(a1 - 0.06, a1, zb, zt, co, co + sgn * 0.08, "Metal"); B(a2, a2 + 0.06, zb, zt, co, co + sgn * 0.08, "Metal")
        mb.obj(name + "_Shutter", kind="trim")
        CUR.entrances.append(dict(name=_nm(name), side=side, a=(a1 + a2) / 2, z=zb, interior=interior))
        return

def _door_leaf(name, axis, p1, p2, cm, zb, zt, kind, swing, hinge_end, interior, leaf_m=None):
    w = (p2 - p1) - 0.02; h = (zt - zb) - 0.02; t = 0.045
    mb = MB()
    if kind == "door_glass":
        fm = "FrameAlu"
        mb.box(0, -t / 2, 0, 0.07, t / 2, h, fm).box(w - 0.07, -t / 2, 0, w, t / 2, h, fm)
        mb.box(0, -t / 2, 0, w, t / 2, 0.12, fm).box(0, -t / 2, h - 0.07, w, t / 2, h, fm)
        mb.box(0.07, -0.006, 0.12, w - 0.07, 0.006, h - 0.07, "Glass")
        mb.box(w - 0.16, -t / 2 - 0.05, h * 0.3, w - 0.13, t / 2 + 0.05, h * 0.7, "Chrome")
    else:
        dm = {"door": "WoodLight", "door_double": "WoodDark", "door_metal": "PanelSteel"}[kind]
        if kind == "door" and interior:
            dm = "White"
        if leaf_m:
            dm = leaf_m
        mb.box(0, -t / 2, 0, w, t / 2, h, dm)
        # raised panels both sides
        for (q1, q2) in ((0.12, h * 0.45), (h * 0.52, h - 0.12)):
            for sd in (-1, 1):
                y0 = sd * t / 2
                mb.box(0.12, min(y0, y0 + sd * 0.012), q1, w - 0.12, max(y0, y0 + sd * 0.012), q2, dm)
        mb.box(w - 0.13, -t / 2 - 0.06, h * 0.46, w - 0.08, t / 2 + 0.06, h * 0.46 + 0.025, "Brass")
    base = 0.0 if axis == "x" else 90.0
    hp = p1 + 0.01
    if hinge_end:
        base += 180.0; hp = p2 - 0.01
    o = mb.obj(name, *(((hp, cm, zb + 0.01) if axis == "x" else (cm, hp, zb + 0.01))), rot=base, kind="door")
    o["openable"] = "hinge"; o["open_angle"] = swing * (-88.0 if hinge_end else 88.0)
    o["closed_rot_z"] = math.radians(base); o["interact"] = "open"
    if interior:   # interior doors shown ajar so the plan reads in previews
        o.rotation_euler.z = math.radians(base + o["open_angle"] * 0.9)
    return o

def bay_window(name, side, a1, a2, zb, zt, face, depth=0.6, frame="PaintRed", roof="TinRust", panes=3, base="SidingTeal"):
    """Box bay projecting `depth` outward from the wall face coordinate `face` on `side`, glazed on 3 sides.
    Pair it with an 'open' opening of the same a1..a2 / zb..zt in the wall."""
    axis, sgn = SIDE[side]
    mb = MB()
    def B(p1, p2, q1, q2, d1, d2, m):
        mb.box(*_b(axis, p1, p2, min(d1, d2), max(d1, d2), q1, q2), m)
    o = face + sgn * depth; f = 0.07
    B(a1 - 0.1, a2 + 0.1, zb - 0.45, zb, face, o + sgn * 0.1, base)              # base box / seat
    B(a1 - 0.15, a2 + 0.15, zt, zt + 0.08, face, o + sgn * 0.18, frame)          # head
    B(a1 - 0.2, a2 + 0.2, zt + 0.08, zt + 0.14, face, o + sgn * 0.3, roof)       # little roof
    for p in [a1 + (a2 - a1) * i / panes for i in range(panes + 1)]:
        B(p - f / 2, p + f / 2, zb, zt, o - sgn * f, o, frame)
    for q in (zb, zb + (zt - zb) * 0.7, zt - f):
        B(a1, a2, q, q + f, o - sgn * f, o, frame)
    B(a1, a2, zb + f, zt - f, o - sgn * 0.04, o - sgn * 0.03, "Glass")
    for p in (a1, a2 - f):                                                       # side cheeks
        B(p, p + f, zb, zt, face, o, frame)
        B(p + (f / 2 - 0.004), p + (f / 2 + 0.004), zb + f, zt - f, face, o - sgn * f, "Glass")
    B(a1, a2, zb - 0.02, zb + 0.03, face - sgn * 0.25, o, "WoodLight")           # inner seat board
    return mb.obj(name, kind="window")

def container(name, x1, y1, z, along="x", L=6.06, ext="ContYellow", intm="WoodLight", ops=None, sides="SNWE",
              floor="WoodFloor", roof=True, doors_end=None):
    """ISO shipping container shell (2.44 x 2.59 x L) you can walk into. Corrugated skin, ply interior,
    corner castings + rails. ops use absolute coords like ring(). doors_end: 'W'/'E'/'S'/'N' adds the cargo doors."""
    W, H = 2.44, 2.59
    x2, y2 = (x1 + L, y1 + W) if along == "x" else (x1 + W, y1 + L)
    res = ring(name, x1, y1, x2, y2, z, z + H, ext, intm, 0.06, 0.0 if ext == intm else 0.02, ops, sides)
    slab(name + "_Floor", x1 + 0.06, y1 + 0.06, x2 - 0.06, y2 - 0.06, z + 0.12, 0.12, top=floor, under="MetalDark")
    if roof:
        slab(name + "_Roof", x1, y1, x2, y2, z + H, 0.08, top=ext, under=intm, ft=0.04, walk=True)
    mb = MB(); c = 0.18
    for (px, py) in ((x1, y1), (x2 - c, y1), (x1, y2 - c), (x2 - c, y2 - c)):
        mb.box(px - 0.02, py - 0.02, z, px + c + 0.02, py + c + 0.02, z + c, "MetalDark")
        mb.box(px - 0.02, py - 0.02, z + H - c, px + c + 0.02, py + c + 0.02, z + H + 0.02, "MetalDark")
        mb.box(px - 0.015, py - 0.015, z, px + c + 0.015, py + c + 0.015, z + H, ext)          # corner posts
    for q1, q2 in ((z, z + 0.16), (z + H - 0.16, z + H + 0.01)):                                 # side rails
        mb.box(x1, y1 - 0.035, q1, x2, y1 + 0.01, q2, ext); mb.box(x1, y2 - 0.01, q1, x2, y2 + 0.035, q2, ext)
        mb.box(x1 - 0.035, y1, q1, x1 + 0.01, y2, q2, ext); mb.box(x2 - 0.01, y1, q1, x2 + 0.035, y2, q2, ext)
    if doors_end:
        axis, sgn = SIDE[doors_end]
        face = {"S": y1, "N": y2, "W": x1, "E": x2}[doors_end]
        a1, a2 = ((x1, x2) if axis == "x" else (y1, y2))
        for k in range(2):
            p1 = a1 + 0.1 + k * (a2 - a1 - 0.2) / 2; p2 = p1 + (a2 - a1 - 0.2) / 2 - 0.02
            mb.box(*_b(axis, p1, p2, min(face, face + sgn * 0.05), max(face, face + sgn * 0.05), z + 0.15, z + H - 0.15), ext)
            for bar in (0.25, 0.75):
                pb = p1 + (p2 - p1) * bar
                mb.box(*_b(axis, pb - 0.025, pb + 0.025, min(face, face + sgn * 0.1), max(face, face + sgn * 0.1), z + 0.2, z + H - 0.2), "Metal")
    mb.obj(name + "_Frame", kind="trim")
    return res

def hip_roof(name, x1, y1, x2, y2, z, pitch=30, over=0.6, m="SlateBlue", under="WoodDark", curl=0.3, thick=0.16,
             cap="SlateDark", seg=10, ornaments=True, kind="roof", inner=None):
    """inner=(ix1, iy1, ix2, iy2, iz): truncated 'skirt' roof rising from the eaves to that rectangle (pagoda tiers)."""
    """Hip roof over the rect (wall outer faces) with eave at z. East-Asian upturned corners via `curl`.
    Slope-aligned UVs (tile rows parallel to each eave). Ridge + hip caps and ridge-end ornaments."""
    ex1, ey1, ex2, ey2 = x1 - over, y1 - over, x2 + over, y2 + over
    W, D = ex2 - ex1, ey2 - ey1
    t = math.tan(math.radians(pitch))
    if W >= D:
        h = D / 2 * t; r0 = Vector((ex1 + D / 2, (ey1 + ey2) / 2, z + h)); r1 = Vector((ex2 - D / 2, (ey1 + ey2) / 2, z + h))
    else:
        h = W / 2 * t; r0 = Vector(((ex1 + ex2) / 2, ey1 + W / 2, z + h)); r1 = Vector(((ex1 + ex2) / 2, ey2 - W / 2, z + h))
    C = [Vector((ex1, ey1, z)), Vector((ex2, ey1, z)), Vector((ex2, ey2, z)), Vector((ex1, ey2, z))]
    if inner:
        ix1, iy1, ix2, iy2, iz = inner
        IC = [Vector((ix1, iy1, iz)), Vector((ix2, iy1, iz)), Vector((ix2, iy2, iz)), Vector((ix1, iy2, iz))]
        pitch = math.degrees(math.atan2(iz - z, max(1e-3, ix1 - ex1)))
        r0 = r1 = IC[0]
    # which ridge end (or inner corner) belongs to each eave corner
    def rn(c):
        if inner:
            return IC[min(range(4), key=lambda i: (C[i] - c).length)]
        return r0 if (c - r0).length < (c - r1).length else r1
    bm = bmesh.new(); uvl = bm.loops.layers.uv.new("UVMap")
    tile = M[m].get("tile", 1.2)
    def curlz(tt):
        return curl * (abs(tt - 0.5) * 2) ** 3
    sides = [(C[0], C[1]), (C[1], C[2]), (C[2], C[3]), (C[3], C[0])]
    sof = []
    for (a, b) in sides:
        e = (b - a); el = e.length; ed = e.normalized()
        sdir = Vector((-ed.y, ed.x, 0))                     # inward horizontal (CCW corners -> left normal)
        ra, rb = rn(a), rn(b)
        E = [a.lerp(b, i / seg) + Vector((0, 0, curlz(i / seg))) for i in range(seg + 1)]
        Rr = [ra.lerp(rb, i / seg) for i in range(seg + 1)]
        ev = [bm.verts.new(p) for p in E]; rv = [bm.verts.new(p) for p in Rr]
        for i in range(seg):
            if (Rr[i] - Rr[i + 1]).length < 1e-6:
                f = bm.faces.new((ev[i], ev[i + 1], rv[i]))
            else:
                f = bm.faces.new((ev[i], ev[i + 1], rv[i + 1], rv[i]))
            f.material_index = 0; f.smooth = False
            for l in f.loops:
                p = l.vert.co
                l[uvl].uv = ((p - a).dot(ed) / tile, ((p - a).dot(sdir) / math.cos(math.radians(pitch))) / tile)
        # fascia strip
        sv = [bm.verts.new(p - Vector((0, 0, thick))) for p in E]
        for i in range(seg):
            f = bm.faces.new((sv[i], sv[i + 1], ev[i + 1], ev[i])); f.material_index = 1
            for l in f.loops:
                l[uvl].uv = ((l.vert.co - a).dot(ed), l.vert.co.z)
        sof.append(sv)
        if inner:                                           # sloped underside for skirt roofs
            iv = [bm.verts.new(ra.lerp(rb, i / seg) - Vector((0, 0, thick))) for i in range(seg + 1)]
            for i in range(seg):
                f = bm.faces.new((sv[i + 1], sv[i], iv[i], iv[i + 1])); f.material_index = 1
    if not inner:
        # soffit (flat underside)
        ring_ = []
        for sv in sof:
            ring_ += sv[:-1]
        f = bm.faces.new(list(reversed(ring_))); f.material_index = 1
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(_nm(name)); bm.to_mesh(me); bm.free()
    me.materials.append(M[m]); me.materials.append(M[under])
    o = bpy.data.objects.new(_nm(name), me); CUR.col.objects.link(o); adopt(o, kind)
    o["uv_done"] = True
    # caps along ridge + hips, ornaments
    if cap:
        lines = [(r0, r1)] if (r0 - r1).length > 1e-3 and not inner else []
        for i, c in enumerate(C):
            lines.append((c + Vector((0, 0, curl)), rn(c)))
        for i, (a, b) in enumerate(lines):
            pipe_run(name + "_Cap%d" % i, [a + Vector((0, 0, 0.05)), b + Vector((0, 0, 0.05))], 0.075, cap, kind="trim")
        if ornaments:
            mb = MB()
            for rp in (() if inner else ((r0, r1) if (r0 - r1).length > 1e-3 else (r0,))):
                mb.cyl(rp.x, rp.y, rp.z, rp.z + 0.45, 0.12, cap, seg=10, r2=0.03)
                mb.sph(rp.x, rp.y, rp.z + 0.5, 0.07, cap)
            for c in C:
                d = (c - rn(c)); d.z = 0; d.normalize()
                p = c + Vector((0, 0, curl)) - d * 0.15
                mb.cyl(p.x, p.y, p.z, p.z + 0.35, 0.06, cap, seg=8, r2=0.01)
            mb.obj(name + "_Orn", kind="trim")
    return o, (inner[4] if inner else z + h)

def gable_roof(name, x1, y1, x2, y2, z, pitch=35, over=0.5, m="RoofTile", under="WoodDark", along="x", thick=0.15,
               gable_m=None, cap="RoofRed"):
    """Simple gable roof, ridge along `along`. gable_m: material for the triangular end walls (None = none)."""
    ex1, ey1, ex2, ey2 = x1 - over, y1 - over, x2 + over, y2 + over
    t = math.tan(math.radians(pitch))
    mb = MB()
    if along == "x":
        h = (y2 - y1) / 2 * t; hy = (ey2 - ey1) / 2 * t; cy = (y1 + y2) / 2
        for sgn in (-1, 1):
            ye = ey1 if sgn < 0 else ey2
            mb.quad([(ex1, ye, z - (hy - h)), (ex2, ye, z - (hy - h)), (ex2, cy, z + h), (ex1, cy, z + h)], m, thick)
        if gable_m:
            for xx in (x1, x2 - 0.2):
                mb.prism([(y1, z), (y2, z), (cy, z + h)], xx, xx + 0.2, gable_m, plane="yz")
    else:
        h = (x2 - x1) / 2 * t; hx = (ex2 - ex1) / 2 * t; cx = (x1 + x2) / 2
        for sgn in (-1, 1):
            xe = ex1 if sgn < 0 else ex2
            mb.quad([(xe, ey1, z - (hx - h)), (xe, ey2, z - (hx - h)), (cx, ey2, z + h), (cx, ey1, z + h)], m, thick)
        if gable_m:
            for yy in (y1, y2 - 0.2):
                mb.prism([(x1, z), (x2, z), (cx, z + h)], yy, yy + 0.2, gable_m, plane="xz")
    o = mb.obj(name, kind="roof")
    if cap:
        if along == "x":
            pipe_run(name + "_Ridge", [(ex1, (y1 + y2) / 2, z + h + 0.03), (ex2, (y1 + y2) / 2, z + h + 0.03)], 0.08, cap, kind="trim")
        else:
            pipe_run(name + "_Ridge", [((x1 + x2) / 2, ey1, z + h + 0.03), ((x1 + x2) / 2, ey2, z + h + 0.03)], 0.08, cap, kind="trim")
    return o, z + h

# --------------------------------------------------------------------------- slabs / stairs / rails
def slab(name, x1, y1, x2, y2, ztop, t=0.22, holes=(), top="WoodFloor", under="Ceiling", ft=0.025, walk=True):
    X = sorted({x1, x2, *[h[0] for h in holes], *[h[2] for h in holes]})
    Y = sorted({y1, y2, *[h[1] for h in holes], *[h[3] for h in holes]})
    bx = []
    for i in range(len(X) - 1):
        for j in range(len(Y) - 1):
            cx, cy = (X[i] + X[i + 1]) / 2, (Y[j] + Y[j + 1]) / 2
            if any(h[0] < cx < h[2] and h[1] < cy < h[3] for h in holes):
                continue
            bx.append((X[i], Y[j], ztop - ft, X[i + 1], Y[j + 1], ztop, 0))
            if t > ft:
                bx.append((X[i], Y[j], ztop - t, X[i + 1], Y[j + 1], ztop - ft, 1))
    o = mesh_obj(_nm(name), bx, [top, under], CUR.col)
    weld_internal_faces(o)
    adopt(o, "floor", walkable=walk)
    return o

def _rb(b, ox, oy, rot):
    """rotate a local box (u1,v1,z1,u2,v2,z2) by rot (0/90/180/270) and translate"""
    u1, v1, z1, u2, v2, z2 = b[:6]
    def r(u, v):
        return {0: (u, v), 90: (-v, u), 180: (-u, -v), 270: (v, -u)}[rot % 360]
    a = r(u1, v1); c = r(u2, v2)
    out = (ox + min(a[0], c[0]), oy + min(a[1], c[1]), z1, ox + max(a[0], c[0]), oy + max(a[1], c[1]), z2)
    return out + tuple(b[6:])

DIRROT = {"+y": 0, "-x": 90, "-y": 180, "+x": 270}

def stair(name, x, y, z0, z1, dirn="+y", w=1.0, tread=0.28, m="WoodLight", rails="both", solid=False, rail_style="bar"):
    """Straight flight. (x, y) = centre of the bottom edge; climbs along dirn. Returns end (x, y)."""
    n = max(2, round((z1 - z0) / 0.18)); r = (z1 - z0) / n
    rot = DIRROT[dirn]
    bx = []
    for i in range(1, n):
        top = z0 + i * r
        bot = z0 if solid else max(z0, top - 0.32)
        bx.append((-w / 2, (i - 1) * tread, bot, w / 2, i * tread, top, 0))
        bx.append((-w / 2, (i - 1) * tread - 0.02, top - 0.04, w / 2, i * tread, top, 1))   # tread nosing
    L = (n - 1) * tread
    o = mesh_obj(_nm(name), [_rb(b, x, y, rot) for b in bx], ["Concrete" if solid else m, m], CUR.col)
    adopt(o, "stair", walkable=True, riser=r, risers=n)
    # stringers (sloped plates) + ramp collider
    mb = MB()
    for sx in ((-w / 2 - 0.05, -w / 2) if rails in ("both", "left") else ()) + ((w / 2, w / 2 + 0.05) if rails in ("both", "right") else ()):
        pass
    ang = math.atan2(z1 - z0 - r, L)
    for side in (-1, 1):
        u0 = side * (w / 2 + 0.025)
        mb.prism([(0, -0.3 + 0.0001), (L, (z1 - z0) - r - 0.3), (L, (z1 - z0) - r + 0.1), (0, 0.1)], u0 - 0.025, u0 + 0.025, "MetalDark" if rail_style != "wood" else "WoodDark", plane="yz")
    so = mb.obj(name + "_Stringers", kind="trim")
    so.matrix_world = Matrix.Translation((x, y, z0)) @ Matrix.Rotation(math.radians(rot), 4, "Z") @ so.matrix_world
    # ramp collider (invisible) for character controllers
    cmb = MB()
    cmb.quad([(-w / 2, -tread, 0), (w / 2, -tread, 0), (w / 2, L, z1 - z0), (-w / 2, L, z1 - z0)], "Collider", thick=0.05)
    co = cmb.obj(name + "_RampCol", kind="collider", collider="ramp", walkable=True)
    co.matrix_world = Matrix.Translation((x, y, z0)) @ Matrix.Rotation(math.radians(rot), 4, "Z")
    co.hide_render = True; co.display_type = "WIRE"
    # handrails following the slope
    for side in ({"both": (-1, 1), "left": (-1,), "right": (1,), "none": ()}[rails]):
        u0 = side * (w / 2 + 0.02)
        p1 = Vector((x, y, z0)) + Matrix.Rotation(math.radians(rot), 3, "Z") @ Vector((u0, 0, 0))
        p2 = Vector((x, y, z0)) + Matrix.Rotation(math.radians(rot), 3, "Z") @ Vector((u0, L, z1 - z0 - r))
        rail_slope(name + "_Rail%d" % side, p1, p2, rail_style)
    end = Vector((x, y, 0)) + Matrix.Rotation(math.radians(rot), 3, "Z") @ Vector((0, L, 0))
    return end.x, end.y

def stair_u(name, x, y, z0, z1, dirn="+y", w=1.0, gap=0.12, tread=0.28, m="WoodLight", turn="right", landing_m=None,
            solid=False, rail_style="bar"):
    """Half-turn (U) stair. (x, y) = centre of the front edge of the whole stair box, climbing along dirn;
    flight 2 comes back on the `turn` side and arrives at the front edge. Returns (hole_rect, arrive_xy)."""
    H = z1 - z0
    n = max(4, 2 * round(H / 0.36)); r = H / n
    n1 = n // 2; zm = z0 + n1 * r
    L1 = (n1 - 1) * tread; L2 = (n - n1 - 1) * tread
    rot = DIRROT[dirn]; R3 = Matrix.Rotation(math.radians(rot), 3, "Z")
    s = 1 if turn == "right" else -1
    def P(u, v):
        p = Vector((x, y, 0)) + R3 @ Vector((u, v, 0)); return p.x, p.y
    opp = {"+y": "-y", "-y": "+y", "+x": "-x", "-x": "+x"}[dirn]
    u1 = -s * (w + gap) / 2; u2 = s * (w + gap) / 2
    stair(name + "_F1", *P(u1, 0), z0, zm, dirn, w, tread, m, rails="left" if s > 0 else "right", solid=solid, rail_style=rail_style)
    Lm = max(L1, L2)
    stair(name + "_F2", *P(u2, Lm), zm, z1, opp, w, tread, m, rails="left" if s > 0 else "right", solid=solid, rail_style=rail_style)
    land = (-(w + gap / 2), Lm, zm - 0.2, w + gap / 2, Lm + w + 0.05, zm)
    o = mesh_obj(_nm(name + "_Landing"), [_rb(land, x, y, rot)], [landing_m or ("Concrete" if solid else m)], CUR.col)
    adopt(o, "floor", walkable=True)
    # landing back-wall guard (rail on the outer edge)
    a = P(-(w + gap / 2), Lm + w + 0.05); b = P(w + gap / 2, Lm + w + 0.05)
    # centre divider rail between the flights
    c1 = P(0, 0.3); c2 = P(0, Lm)
    rail(name + "_Mid", c1[0], c1[1], c2[0], c2[1], z0 + 0.3, 0.9, rail_style if rail_style != "bar" else "bar", col=False)
    corners = [P(-(w + gap / 2), 0), P(w + gap / 2, Lm + w + 0.05)]
    hx1, hx2 = sorted((corners[0][0], corners[1][0])); hy1, hy2 = sorted((corners[0][1], corners[1][1]))
    arrive = P(u2, Lm - L2)
    return (hx1, hy1, hx2, hy2), arrive

def rail_slope(name, p1, p2, style="bar", h=0.95):
    mb = MB()
    d = p2 - p1; L = d.length
    nposts = max(2, int(L / 0.9) + 1)
    pm = "WoodDark" if style == "wood" else "MetalDark"
    for i in range(nposts):
        p = p1 + d * (i / (nposts - 1))
        mb.cyl(p.x, p.y, p.z, p.z + h, 0.02, pm, seg=8)
    if style == "bar":
        nb = int(L / 0.12)
        for i in range(1, nb):
            p = p1 + d * (i / nb)
            mb.cyl(p.x, p.y, p.z + 0.08, p.z + h - 0.04, 0.007, pm, seg=6)
    o = mb.obj(name, kind="railing")
    # top rail as a sloped thin box along the segment
    mb2 = MB()
    mb2.cyl(0, 0, 0, L, 0.025, pm if style != "wood" else "WoodLight", seg=10)
    o2 = mb2.obj(name + "_Top", kind="railing")
    z = Vector((0, 0, 1)); rotq = z.rotation_difference(d.normalized())
    o2.matrix_world = Matrix.Translation(p1 + Vector((0, 0, h))) @ rotq.to_matrix().to_4x4()
    return o

def rail(name, x1, y1, x2, y2, z, h=1.0, style="bar", col=True):
    """axis-aligned railing from (x1,y1) to (x2,y2) on level z. style: bar|glass|wood|solid|cable"""
    mb = MB()
    L = math.hypot(x2 - x1, y2 - y1)
    ax = "x" if abs(y2 - y1) < 1e-6 else "y"
    pm = {"wood": "WoodDark", "glass": "FrameAlu", "solid": "Concrete"}.get(style, "MetalDark")
    def at(t):
        return x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
    if style == "solid":
        a, b = (min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2))
        mb.box(a[0] - (0.06 if ax == "y" else 0), a[1] - (0.06 if ax == "x" else 0), z,
               b[0] + (0.06 if ax == "y" else 0), b[1] + (0.06 if ax == "x" else 0), z + h, "Concrete")
    else:
        n = max(1, round(L / 1.2))
        for i in range(n + 1):
            px, py = at(i / n)
            mb.bc(px, py, z, 0.05, 0.05, h, pm)
        a, b = (min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2))
        e = 0.03
        top = "WoodLight" if style == "wood" else pm
        mb.box(a[0] - e, a[1] - e, z + h - 0.05, b[0] + e, b[1] + e, z + h, top)
        if style == "glass":
            mb.box(a[0] - 0.006 if ax == "y" else a[0], a[1] - 0.006 if ax == "x" else a[1], z + 0.08,
                   b[0] + 0.006 if ax == "y" else b[0], b[1] + 0.006 if ax == "x" else b[1], z + h - 0.06, "Glass")
        elif style == "cable":
            for q in (0.25, 0.45, 0.65, 0.85):
                mb.box(a[0] - 0.004, a[1] - 0.004, z + h * q, b[0] + 0.004, b[1] + 0.004, z + h * q + 0.008, "Chrome")
        else:
            mb.box(a[0] - 0.01, a[1] - 0.01, z + 0.08, b[0] + 0.01, b[1] + 0.01, z + 0.12, pm)
            nb = int(L / 0.12)
            for i in range(1, nb):
                px, py = at(i / nb)
                mb.bc(px, py, z + 0.1, 0.018, 0.018, h - 0.14, pm)
    o = mb.obj(name, kind="railing")
    if col:
        c = MB()
        a, b = (min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2))
        c.box(a[0] - 0.03, a[1] - 0.03, z, b[0] + 0.03, b[1] + 0.03, z + 1.1, "Collider")
        co = c.obj(name + "_Col", kind="collider", collider="wall")
        co.hide_render = True; co.display_type = "WIRE"
    return o

def rails_rect(name, x1, y1, x2, y2, z, sides="SNWE", **kw):
    seg = {"S": (x1, y1, x2, y1), "N": (x1, y2, x2, y2), "W": (x1, y1, x1, y2), "E": (x2, y1, x2, y2)}
    for s in sides:
        rail("%s_%s" % (name, s), *seg[s], z, **kw)

# --------------------------------------------------------------------------- lights
def lamp(name, x, y, z, power=80, color=(1.0, 0.78, 0.55), kind="ceiling", radius=0.12, glow="LightWarm", fixture=True):
    """ceiling: z = ceiling height (fixture hangs below). pendant: drop 0.6. wall: sconce. point: no fixture"""
    CUR.lights += 1
    mb = MB()
    lz = z
    if fixture and kind == "ceiling":
        mb.cyl(0, 0, -0.06, 0, 0.22, "White", seg=20); mb.cyl(0, 0, -0.075, -0.06, 0.18, glow, seg=20)
        lz = z - 0.25
    elif fixture and kind == "pendant":
        mb.cyl(0, 0, -0.62, 0, 0.006, "Black", seg=6)
        mb.cyl(0, 0, -0.85, -0.62, 0.22, "MetalDark", seg=20, r2=0.04)
        mb.cyl(0, 0, -0.86, -0.84, 0.2, glow, seg=20)
        lz = z - 0.95
    elif fixture and kind == "wall":
        mb.bc(0, 0, -0.12, 0.12, 0.08, 0.24, "Brass"); mb.sph(0, -0.06, 0, 0.07, glow)
        lz = z
    elif fixture and kind == "lantern":
        mb.cyl(0, 0, -0.5, 0, 0.006, "Black", seg=6)
        mb.sph(0, 0, -0.72, 0.2, glow, sz=1.25, sub=3)
        mb.cyl(0, 0, -0.5, -0.46, 0.09, "Black", seg=12); mb.cyl(0, 0, -0.98, -0.94, 0.09, "Black", seg=12)
        lz = z - 0.72
    if fixture and kind != "point":
        mb.obj(name + "_Fixture", x, y, z, kind="light_fixture")
    ld = bpy.data.lights.new(_nm(name), "POINT")
    ld.energy = power * (1.0 if "StreetLamp" in name else LIGHT_K); ld.color = color; ld.shadow_soft_size = radius
    ld.use_shadow = power >= 150          # only big lights cast shadows (keeps EEVEE / game engines fast)
    try: ld.use_soft_falloff = True
    except Exception: pass
    lo = bpy.data.objects.new(_nm(name), ld); lo.location = (x, y, lz)
    CUR.col.objects.link(lo); adopt(lo, "light")
    return lo

def area_light(name, x, y, z, sx, sy, power=200, color=(1, 0.85, 0.7)):
    ld = bpy.data.lights.new(_nm(name), "AREA"); ld.shape = "RECTANGLE"; ld.size = sx; ld.size_y = sy
    ld.energy = power; ld.color = color
    lo = bpy.data.objects.new(_nm(name), ld); lo.location = (x, y, z)
    CUR.col.objects.link(lo); adopt(lo, "light")
    return lo

# --------------------------------------------------------------------------- text / signs / labels
_FONT = None
def font():
    global _FONT
    if _FONT is None:
        try:
            _FONT = bpy.data.fonts.load(FONT_PATH, check_existing=True)
        except Exception:
            _FONT = bpy.data.fonts.load(r"C:\Windows\Fonts\arialbd.ttf", check_existing=True)
    return _FONT

def text(name, body, x, y, z, size=0.4, m="LabelGlow", rot=0.0, align="CENTER", extrude=0.01, upright=True, col=None, kind="sign"):
    cu = bpy.data.curves.new(_nm(name), "FONT")
    cu.body = body; cu.font = font(); cu.size = size; cu.extrude = extrude
    cu.align_x = align; cu.align_y = "CENTER"
    try: cu.font_bold = font()
    except Exception: pass
    o = bpy.data.objects.new(_nm(name), cu)
    o.data.materials.append(M[m])
    o.location = (x, y, z)
    o.rotation_euler = (math.radians(90) if upright else 0, 0, math.radians(rot))
    (col or CUR.col).objects.link(o)
    o.parent = CUR.root; o["kind"] = kind
    return o

def sign_board(name, body, x, y, z, w, h, rot=0, board="Black", glow="NeonYellow", size=None, depth=0.08, frame=None):
    """flat box sign facing -Y (before rot) with glowing text on its front"""
    mb = MB()
    mb.box(-w / 2, 0, -h / 2, w / 2, depth, h / 2, board)
    if frame:
        mb.box(-w / 2 - 0.03, -0.01, -h / 2 - 0.03, w / 2 + 0.03, depth - 0.01, -h / 2, frame)
        mb.box(-w / 2 - 0.03, -0.01, h / 2, w / 2 + 0.03, depth - 0.01, h / 2 + 0.03, frame)
    o = mb.obj(name, x, y, z, rot, kind="sign")
    t = text(name + "_Txt", body, 0, -0.012, 0, size or h * 0.55, glow, 0, extrude=0.008)
    t.parent = o
    t.location = (0, -0.012, 0); t.rotation_euler = (math.radians(90), 0, 0)
    return o

def neon_vertical(name, body, x, y, z, h, rot=0, glow="NeonPink", board="Black", size=0.32):
    """vertical blade sign (CJK one char per line)"""
    s = "\n".join(list(body))
    n = len(body)
    w = size * 1.35
    hh = max(h, n * size * 1.25 + 0.3)
    mb = MB()
    mb.box(-w / 2, -0.06, -hh / 2, w / 2, 0.06, hh / 2, board)
    for sy in (-1, 1):                       # glowing border tubes on both faces
        y0, y1 = sorted((sy * 0.06, sy * 0.085))
        mb.box(-w / 2 - 0.03, y0, hh / 2, w / 2 + 0.03, y1, hh / 2 + 0.04, glow)
        mb.box(-w / 2 - 0.03, y0, -hh / 2 - 0.04, w / 2 + 0.03, y1, -hh / 2, glow)
        mb.box(-w / 2 - 0.03, y0, -hh / 2, -w / 2, y1, hh / 2, glow)
        mb.box(w / 2, y0, -hh / 2, w / 2 + 0.03, y1, hh / 2, glow)
    o = mb.obj(name, x, y, z, rot, kind="sign")
    for sgn, ry in ((-1, 0), (1, 180)):
        t = text(name + ("_TxtA" if sgn < 0 else "_TxtB"), s, 0, 0, 0, size, glow, 0, extrude=0.006)
        t.data.space_line = 0.95
        t.parent = o; t.location = (0, sgn * 0.075, 0)
        t.rotation_euler = (math.radians(90), 0, math.radians(ry))
    return o

def label_building(top_z, front_y, door_xyz=None, width=6.0):
    """Asset label: floating 2-line nameplate above the roof + bronze plaque by the main door.
    Both live in the LBL_<id> collection (prop kind='label') so a game can hide/strip them."""
    if not LABELS_ON:
        return
    m = CUR.meta
    l1 = "%s  %s" % (m["name_zh"], m["name_en"])
    l2 = "%s · %s  |  %s" % (m["style_zh"], m["style"], m["tier"])
    l3 = "id: %s" % m["asset_id"]
    z = top_z + 2.2
    mb = MB()
    pw = max(width, len(l1) * 0.36 + 1.0)
    mb.box(-pw / 2, -0.04, -0.95, pw / 2, 0.04, 0.95, "Black")
    mb.box(-pw / 2 - 0.05, -0.05, 0.95, pw / 2 + 0.05, 0.05, 1.0, "LabelGlowCyan")
    mb.box(-pw / 2 - 0.05, -0.05, -1.0, pw / 2 + 0.05, 0.05, -0.95, "LabelGlowCyan")
    mb.cyl(-pw / 2 + 0.3, 0.1, -(z - top_z) - 0.95, -0.95, 0.04, "MetalDark", seg=8)
    mb.cyl(pw / 2 - 0.3, 0.1, -(z - top_z) - 0.95, -0.95, 0.04, "MetalDark", seg=8)
    p = mb.obj("LABEL_Plate", 0, front_y, z, kind="label")
    for o_ in (p,):
        CUR.col.objects.unlink(o_); CUR.lab.objects.link(o_)
    for i, (s, sz, mt) in enumerate(((l1, 0.5, "LabelGlow"), (l2, 0.3, "LabelGlowCyan"), (l3, 0.22, "LabelGlow"))):
        t = text("LABEL_L%d" % i, s, 0, front_y - 0.05, z + (0.45, -0.15, -0.6)[i], sz, mt, col=CUR.lab, kind="label")
    if door_xyz:
        x, y, zz = door_xyz
        mb = MB()
        mb.box(-0.32, 0, -0.2, 0.32, 0.025, 0.2, "Brass")
        pl = mb.obj("LABEL_Plaque", x, y - 0.03, zz, kind="label")
        CUR.col.objects.unlink(pl); CUR.lab.objects.link(pl)
        t1 = text("LABEL_PlaqueA", m["name_zh"], x, y - 0.06, zz + 0.07, 0.11, "Black", col=CUR.lab, kind="label", extrude=0.004)
        t2 = text("LABEL_PlaqueB", "%s | %s" % (m["name_en"], m["style"]), x, y - 0.06, zz - 0.09, 0.055, "Black",
                  col=CUR.lab, kind="label", extrude=0.003)

def spawn(name, x, y, z=0.0, rot=0):
    e = bpy.data.objects.new(_nm("SPAWN_" + name), None)
    e.empty_display_type = "SINGLE_ARROW"; e.location = (x, y, z); e.rotation_euler.z = math.radians(rot)
    CUR.col.objects.link(e); adopt(e, "spawn")
    CUR.spawns.append(dict(name=name, local=(round(x, 2), round(y, 2), round(z, 2))))
    return e

# --------------------------------------------------------------------------- finish
def _all_children(o):
    out = []
    for c in o.children:
        out.append(c); out += _all_children(c)
    return out

def end_building(loc=(0, 0, 0), rot=0, bevel_kinds=("furniture", "trim", "window", "door", "railing")):
    b = CUR
    objs = _all_children(b.root)
    # text -> mesh (portable for glTF / engines)
    for o in [o for o in objs if o.type == "FONT"]:
        dg = bpy.context.evaluated_depsgraph_get()
        me = bpy.data.meshes.new_from_object(o.evaluated_get(dg))
        n = o.name; par = o.parent; mw = o.matrix_world.copy(); props = {k: o[k] for k in o.keys()}
        cols = list(o.users_collection); cu = o.data
        bpy.data.objects.remove(o); bpy.data.curves.remove(cu)
        no = bpy.data.objects.new(n, me)
        for c in cols: c.objects.link(no)
        no.parent = par; no.matrix_world = mw
        for k, v in props.items(): no[k] = v
    objs = _all_children(b.root)
    tris = 0
    for o in objs:
        if o.type != "MESH":
            continue
        if not o.get("uv_done"):
            uv_box(o)
        k = o.get("kind", "")
        finish(o, 0.008 if k in bevel_kinds else 0.0, 2)
        tris += sum(len(p.vertices) - 2 for p in o.data.polygons)
    # world placement
    b.root.location = loc; b.root.rotation_euler.z = math.radians(rot)
    bpy.context.view_layer.update()
    # bounds (world)
    pts = [o.matrix_world @ Vector(c) for o in objs if o.type == "MESH" and o.get("kind") not in ("label", "collider", "cable")
           for c in o.bound_box]
    mn = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    mx = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    m = b.meta
    m.update(position=tuple(round(v, 2) for v in loc), rotation_z_deg=rot,
             size_m=tuple(round(v, 2) for v in (mx - mn)), height_m=round(mx.z - loc[2], 2),
             entrances=[dict(e, a=round(e["a"], 2)) for e in b.entrances if not e["interior"]],
             interior_doors=sum(1 for e in b.entrances if e["interior"]), spawns=b.spawns,
             objects=len(objs), triangles_approx=tris, lights=b.lights,
             interactables=sorted({o.get("interact") for o in objs if o.get("interact")}),
             furniture=sum(1 for o in objs if o.get("kind") == "furniture"),
             collection="BLD_" + b.bid, root_object="BLD_" + b.bid, labels_collection="LBL_" + b.bid)
    for k, v in m.items():
        b.root[k] = json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict, tuple)) else v
    # Blender asset browser entry
    try:
        b.col.asset_mark()
        ad = b.col.asset_data
        ad.description = "%s %s | %s | %s | %s" % (m["name_zh"], m["name_en"], m["style"], m["tier"], m["description"])
        for t in [m["style"], m["style_zh"], m["tier"], m["category"], m["name_zh"]] + list(m["game_styles"]):
            ad.tags.new(str(t), skip_if_exists=True)
        try: ad.author = "TownKit"
        except Exception: pass
    except Exception as e:
        print("asset_mark failed", e)
    for o in objs:
        if o.get("kind") == "label":
            o.visible_shadow = False
    BUILDINGS.append(dict(m))
    print("[TownKit] %-24s objs=%4d tris=%7d lights=%3d size=%s" % (b.bid, len(objs), tris, b.lights, m["size_m"]))
    return b
