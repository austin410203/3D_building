# Helper library for building Nobita's house (units: metres)
import bpy, bmesh, math
from mathutils import Vector, Matrix

def coll(name, parent=None):
    c = bpy.data.collections.get(name)
    if not c:
        c = bpy.data.collections.new(name)
        (parent or bpy.context.scene.collection).children.link(c)
    return c

def _inp(node, ident):
    for s in node.inputs:
        if s.identifier == ident or s.name == ident:
            return s
    return None

import os
TEXDIR = os.path.abspath(os.path.join(os.path.dirname(LIB), "..", "textures"))

def _img(path, data):
    img = bpy.data.images.load(path, check_existing=True)
    if data:
        img.colorspace_settings.name = "Non-Color"
    return img

M = {}
def mat(name, color, rough=0.6, metal=0.0, alpha=1.0, tex=None, tile=1.0, nstr=0.5):
    """tex: base name of <tex>_col.jpg / <tex>_nrm.jpg in TEXDIR; tile = metres per texture repeat."""
    m = bpy.data.materials.get(name)
    if m is None:
        m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    for n in [n for n in nt.nodes if n.type in ("TEX_IMAGE", "NORMAL_MAP")]:
        nt.nodes.remove(n)
    _inp(b, "Base Color").default_value = (*color, 1)
    _inp(b, "Roughness").default_value = rough
    _inp(b, "Metallic").default_value = metal
    m["tile"] = tile
    if tex and os.path.exists(os.path.join(TEXDIR, tex + "_col.jpg")):
        ti = nt.nodes.new("ShaderNodeTexImage"); ti.location = (-600, 300)
        ti.image = _img(os.path.join(TEXDIR, tex + "_col.jpg"), False)
        nt.links.new(ti.outputs["Color"], _inp(b, "Base Color"))
        tn = nt.nodes.new("ShaderNodeTexImage"); tn.location = (-600, -100)
        tn.image = _img(os.path.join(TEXDIR, tex + "_nrm.jpg"), True)
        nm = nt.nodes.new("ShaderNodeNormalMap"); nm.location = (-300, -100)
        _inp(nm, "Strength").default_value = nstr
        nt.links.new(tn.outputs["Color"], _inp(nm, "Color"))
        nt.links.new(nm.outputs["Normal"], _inp(b, "Normal"))
    if alpha < 1:
        _inp(b, "Alpha").default_value = alpha
        for attr, val in (("surface_render_method", "BLENDED"), ("blend_method", "BLEND")):
            try: setattr(m, attr, val)
            except Exception: pass
    m.diffuse_color = (*color, alpha)
    M[name] = m
    return m

def srgb(*c):
    return tuple(((v + 0.055) / 1.055) ** 2.4 if v > 0.04045 else v / 12.92 for v in c)

# palette sampled from the reference illustration (sRGB, converted to linear)
PALETTE = {
    "WallTeal": (0.40, 0.64, 0.66), "WallTealDark": (0.30, 0.50, 0.55), "WallBlue": (0.38, 0.56, 0.68),
    "WallYellow": (0.86, 0.72, 0.40), "WallMauve": (0.56, 0.44, 0.48), "WallSand": (0.74, 0.66, 0.52),
    "WallInt": (0.92, 0.87, 0.77), "WallIntWarm": (0.90, 0.80, 0.62), "Ceiling": (0.95, 0.93, 0.88),
    "Concrete": (0.56, 0.60, 0.60), "ConcreteDark": (0.40, 0.44, 0.46), "RoofTin": (0.50, 0.44, 0.42),
    "RoofRust": (0.62, 0.40, 0.30), "Frame": (0.26, 0.24, 0.25), "FrameTeal": (0.24, 0.40, 0.42),
    "DoorOrange": (0.80, 0.46, 0.28), "WoodBrown": (0.56, 0.35, 0.22), "WoodLight": (0.78, 0.60, 0.40),
    "WoodDark": (0.36, 0.24, 0.17), "FloorWood": (0.66, 0.48, 0.32), "FloorTile": (0.80, 0.78, 0.72),
    "Metal": (0.62, 0.64, 0.66), "MetalDark": (0.30, 0.32, 0.34), "Awning": (0.86, 0.42, 0.30),
    "AwningStripe": (0.95, 0.85, 0.70), "PlazaTile": (0.62, 0.50, 0.46), "Asphalt": (0.26, 0.30, 0.34),
    "Plant": (0.32, 0.50, 0.28), "PlantDark": (0.20, 0.36, 0.22), "Pot": (0.72, 0.40, 0.28),
    "ACWhite": (0.86, 0.87, 0.84), "Dish": (0.88, 0.76, 0.76), "Black": (0.05, 0.05, 0.06),
    "White": (0.95, 0.95, 0.93), "FabricRed": (0.72, 0.30, 0.26), "FabricBlue": (0.30, 0.42, 0.62),
    "FabricGreen": (0.40, 0.55, 0.38), "FabricCream": (0.92, 0.86, 0.74), "Rug": (0.66, 0.36, 0.30),
    "Book1": (0.75, 0.25, 0.2), "Book2": (0.2, 0.45, 0.7), "Book3": (0.9, 0.75, 0.3), "Book4": (0.35, 0.6, 0.4),
    "SignRed": (0.85, 0.30, 0.25), "CityBlue": (0.42, 0.58, 0.70), "CityBlue2": (0.34, 0.50, 0.64),
    "Cable": (0.08, 0.08, 0.09), "Collider": (1.0, 0.0, 1.0),
}
GLOW = {"GlassWarm": (1.0, 0.72, 0.38), "LampGlow": (1.0, 0.85, 0.55), "SignGlow": (1.0, 0.55, 0.30),
        "ScreenGlow": (0.55, 0.85, 1.0), "CityWindow": (1.0, 0.78, 0.45)}

def glow_mat(name, color, strength=3.0):
    m = mat(name, srgb(*color), 0.3)
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    _inp(b, "Emission Color").default_value = (*srgb(*color), 1)
    _inp(b, "Emission Strength").default_value = strength
    m["glow"] = strength
    return m

def init_materials():
    for k, c in PALETTE.items():
        mat(k, srgb(*c), 0.8)
    mat("Glass", srgb(0.75, 0.88, 0.95), 0.05, 0, 0.3)
    for k, c in GLOW.items():
        glow_mat(k, c)

def _add_box(bm, b):
    x1, y1, z1, x2, y2, z2 = b
    x1, x2 = sorted((x1, x2)); y1, y2 = sorted((y1, y2)); z1, z2 = sorted((z1, z2))
    if x2 - x1 < 1e-4 or y2 - y1 < 1e-4 or z2 - z1 < 1e-4:
        return []
    r = bmesh.ops.create_cube(bm, size=1.0)
    for v in r["verts"]:
        v.co.x = x1 if v.co.x < 0 else x2
        v.co.y = y1 if v.co.y < 0 else y2
        v.co.z = z1 if v.co.z < 0 else z2
    return r["verts"]

def mesh_obj(name, boxes, mats, col, origin="bottom"):
    """boxes: list of (x1,y1,z1,x2,y2,z2[,mat_index]). World coords; origin moved to bottom centre."""
    if not isinstance(mats, (list, tuple)):
        mats = [mats]
    bm = bmesh.new()
    for b in boxes:
        mi = b[6] if len(b) > 6 else 0
        vs = _add_box(bm, b[:6])
        faces = {f for v in vs for f in v.link_faces}
        for f in faces:
            f.material_index = mi
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    xs = [v.co.x for v in bm.verts]; ys = [v.co.y for v in bm.verts]; zs = [v.co.z for v in bm.verts]
    if origin == "bottom" and xs:
        o = Vector(((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, min(zs)))
    else:
        o = Vector((0, 0, 0))
    bmesh.ops.translate(bm, vec=-o, verts=bm.verts)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me); bm.free()
    for m in mats:
        me.materials.append(M[m] if isinstance(m, str) else m)
    ob = bpy.data.objects.new(name, me)
    ob.location = o
    col.objects.link(ob)
    return ob

def wall(name, axis, a1, a2, c1, c2, z1, z2, m, col, openings=()):
    """axis 'x': wall runs along X from a1..a2, occupies Y c1..c2. openings: (o1,o2,zb,zt)"""
    # grid of cells split at every opening edge; solid cells are boxes that share whole faces,
    # so after welding we can delete the shared (internal) faces -> one clean watertight shell
    ops = [(o1, o2, max(zb, z1), min(zt, z2)) for o1, o2, zb, zt in openings]
    A = sorted({a1, a2, *[v for o in ops for v in o[:2]]})
    Z = sorted({z1, z2, *[v for o in ops for v in o[2:]]})
    bx = []
    for i in range(len(A) - 1):
        for j in range(len(Z) - 1):
            ca, cz = (A[i] + A[i + 1]) / 2, (Z[j] + Z[j + 1]) / 2
            if any(o1 < ca < o2 and zb < cz < zt for o1, o2, zb, zt in ops):
                continue
            p1, p2, q1, q2 = A[i], A[i + 1], Z[j], Z[j + 1]
            bx.append((p1, c1, q1, p2, c2, q2) if axis == "x" else (c1, p1, q1, c2, p2, q2))
    ob = mesh_obj(name, bx, m, col)
    weld_internal_faces(ob)
    return ob

def weld_internal_faces(ob):
    """Merge coincident verts and delete faces shared by two cells (internal partitions)."""
    me = ob.data
    bm = bmesh.new(); bm.from_mesh(me)
    seen = {}
    for f in bm.faces:
        seen.setdefault(tuple(round(c, 4) for c in f.calc_center_median()), []).append(f)
    dup = [f for fs in seen.values() if len(fs) > 1 for f in fs]
    if dup:
        bmesh.ops.delete(bm, geom=dup, context="FACES_ONLY")
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    loose = [v for v in bm.verts if not v.link_faces]
    if loose:
        bmesh.ops.delete(bm, geom=loose, context="VERTS")
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-6)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me); bm.free()

def _orient(axis, p1, p2, c1, c2, q1, q2, mi=0):
    return (p1, c1, q1, p2, c2, q2, mi) if axis == "x" else (c1, p1, q1, c2, p2, q2, mi)

def window(name, axis, o1, o2, c1, c2, zb, zt, col, panes=2):
    """Japanese two-track sliding window (hikichigai-mado): fixed outer frame + 2 sashes.
    The inner sash (_SashB) slides along the wall axis; custom props drive the game/animation."""
    f = 0.04; cm = (c1 + c2) / 2
    bx = [_orient(axis, o1, o1 + f, cm - 0.05, cm + 0.05, zb, zt),
          _orient(axis, o2 - f, o2, cm - 0.05, cm + 0.05, zb, zt),
          _orient(axis, o1, o2, cm - 0.05, cm + 0.05, zb, zb + f),
          _orient(axis, o1, o2, cm - 0.05, cm + 0.05, zt - f, zt),
          _orient(axis, o1 - 0.03, o2 + 0.03, c1 - 0.04, c2 + 0.04, zb - 0.03, zb)]   # sill
    mesh_obj(name + "_Frame", bx, "Frame", col)
    inner = (o2 - o1) - 2 * f
    half = inner / 2 + 0.02
    zs, ze = zb + f, zt - f
    sf = 0.035
    sashes = []
    for k, (start, n1, n2) in enumerate(((o1 + f, cm - 0.038, cm - 0.006), (o2 - f - half, cm + 0.006, cm + 0.038))):
        b = [_orient(axis, start, start + sf, n1, n2, zs, ze, 0), _orient(axis, start + half - sf, start + half, n1, n2, zs, ze, 0),
             _orient(axis, start, start + half, n1, n2, zs, zs + sf, 0), _orient(axis, start, start + half, n1, n2, ze - sf, ze, 0),
             _orient(axis, start + sf, start + half - sf, (n1 + n2) / 2 - 0.003, (n1 + n2) / 2 + 0.003, zs + sf, ze - sf, 1)]
        s = mesh_obj(name + ("_SashA" if k == 0 else "_SashB"), b, ["Frame", "Glass"], col)
        if k == 1:
            d = -(half - 2 * sf)
            s["openable"] = "slide"
            s["open_offset"] = (d, 0.0, 0.0) if axis == "x" else (0.0, d, 0.0)
        sashes.append(s)
    return sashes[1]

def door(name, axis, o1, o2, c1, c2, zb, zt, col, m="WoodLight", open_deg=0.0, swing=1, hinge_end=False):
    """Door leaf with origin at hinge (rotate Z to open). swing=+1/-1 chooses room side."""
    w = (o2 - o1) - 0.02; h = (zt - zb) - 0.02; t = 0.04
    cm = (c1 + c2) / 2
    # casing
    cas = [_orient(axis, o1 - 0.05, o1, c1 - 0.01, c2 + 0.01, zb, zt + 0.05),
           _orient(axis, o2, o2 + 0.05, c1 - 0.01, c2 + 0.01, zb, zt + 0.05),
           _orient(axis, o1 - 0.05, o2 + 0.05, c1 - 0.01, c2 + 0.01, zt, zt + 0.05)]
    mesh_obj(name + "_Casing", cas, "Frame", col)
    bm = bmesh.new()
    _add_box(bm, (0, -t / 2, 0, w, t / 2, h))
    vs = _add_box(bm, (w - 0.12, -t / 2 - 0.06, h * 0.45, w - 0.08, t / 2 + 0.06, h * 0.45 + 0.03))
    for f in {f for v in vs for f in v.link_faces}:
        f.material_index = 1
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    me.materials.append(M[m]); me.materials.append(M["Metal"])
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    base = 0.0 if axis == "x" else 90.0
    hp = o1 + 0.01
    if hinge_end:
        base += 180.0; hp = o2 - 0.01
    ob.location = (hp, cm, zb + 0.01) if axis == "x" else (cm, hp, zb + 0.01)
    ob.rotation_euler.z = math.radians(base + swing * open_deg)
    ob["door"] = True
    ob["openable"] = "hinge"
    ob["open_angle"] = swing * 88.0
    ob["closed_rot_z"] = math.radians(base)
    return ob

def cyl(name, x, y, z1, z2, r, m, col, seg=32, r2=None):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=seg, radius1=r, radius2=r if r2 is None else r2, depth=z2 - z1)
    bmesh.ops.translate(bm, vec=(0, 0, (z2 - z1) / 2), verts=bm.verts)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    me.materials.append(M[m])
    ob = bpy.data.objects.new(name, me); ob.location = (x, y, z1)
    col.objects.link(ob)
    return ob

def sphere(name, x, y, z, r, m, col, sx=1, sy=1, sz=1):
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=3, radius=r)
    bmesh.ops.scale(bm, vec=(sx, sy, sz), verts=bm.verts)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth = True
    me.materials.append(M[m])
    ob = bpy.data.objects.new(name, me); ob.location = (x, y, z)
    col.objects.link(ob)
    return ob

def poly_prism(name, pts2d, axis, c1, c2, m, col):
    """Extrude a 2D polygon (in the plane spanned by the wall axis and Z) through c1..c2."""
    bm = bmesh.new()
    def v3(p, c):
        return (p[0], c, p[1]) if axis == "x" else (c, p[0], p[1])
    a = [bm.verts.new(v3(p, c1)) for p in pts2d]
    b = [bm.verts.new(v3(p, c2)) for p in pts2d]
    bm.faces.new(a); bm.faces.new(list(reversed(b)))
    n = len(pts2d)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((a[i], a[j], b[j], b[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    me.materials.append(M[m])
    ob = bpy.data.objects.new(name, me); col.objects.link(ob)
    return ob

def slab_quad(name, corners, thick, m, col):
    """Thin slab from 4 world-space corners (top surface), extruded down by thick along Z."""
    bm = bmesh.new()
    top = [bm.verts.new(c) for c in corners]
    bot = [bm.verts.new((c[0], c[1], c[2] - thick)) for c in corners]
    bm.faces.new(top); bm.faces.new(list(reversed(bot)))
    for i in range(4):
        j = (i + 1) % 4
        bm.faces.new((top[i], bot[i], bot[j], top[j]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    me.materials.append(M[m])
    ob = bpy.data.objects.new(name, me); col.objects.link(ob)
    return ob

# ---------------- detail / finishing helpers ----------------
def tile_roof(name, e1, e2, svec, col, w=0.30, row=0.24, t=0.035, A=0.045, segs=8, m="RoofRed"):
    """Japanese wave-tile (sangawara) roof surface. e1-e2 = eave line, svec = eave->ridge vector."""
    e1, e2, svec = Vector(e1), Vector(e2), Vector(svec)
    u = e2 - e1; ulen = u.length; u.normalize()
    slen = svec.length; s = svec.normalized()
    n = u.cross(s)
    if n.z < 0:
        e1, e2 = e2, e1; u = -u; n = u.cross(s)
    n.normalize()
    nt = max(1, round(ulen / w)); w = ulen / nt
    us = [ulen * i / (nt * segs) for i in range(nt * segs + 1)]
    hs = [A * (0.5 - 0.5 * math.cos(2 * math.pi * x / w)) for x in us]
    lines = [(0.0, 0.0)]
    r = 0
    while r * row < slen - 1e-3:
        lines.append((r * row, t)); lines.append((min((r + 1) * row, slen), t * 0.25)); r += 1
    bm = bmesh.new()
    rows = [[bm.verts.new(e1 + u * x + s * v + n * (off + h)) for x, h in zip(us, hs)] for v, off in lines]
    for a, b in zip(rows, rows[1:]):
        for i in range(len(us) - 1):
            bm.faces.new((a[i], a[i + 1], b[i + 1], b[i]))
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    me.materials.append(M[m])
    ob = bpy.data.objects.new(name, me); col.objects.link(ob)
    return ob

def uv_box(ob):
    """World-space box projection, 1 UV unit = material['tile'] metres (consistent texel density)."""
    me = ob.data
    if not me.uv_layers:
        me.uv_layers.new(name="UVMap")
    bm = bmesh.new(); bm.from_mesh(me)
    uvl = bm.loops.layers.uv.verify()
    mw = ob.matrix_world; rot = mw.to_3x3()
    tiles = [(mt.get("tile", 1.0) if mt else 1.0) for mt in me.materials] or [1.0]
    for f in bm.faces:
        nn = rot @ f.normal
        ax = max(range(3), key=lambda i: abs(nn[i]))
        t = tiles[min(f.material_index, len(tiles) - 1)]
        for l in f.loops:
            p = mw @ l.vert.co
            uv = (p.x, p.y) if ax == 2 else ((p.y, p.z) if ax == 0 else (p.x, p.z))
            l[uvl].uv = (uv[0] / t, uv[1] / t)
    bm.to_mesh(me); bm.free()

def finish(ob, bevel=0.0, segs=3, angle=40):
    if ob.type != "MESH":
        return
    me = ob.data
    try:
        me.shade_smooth()
    except AttributeError:
        for p in me.polygons: p.use_smooth = True
    bm = bmesh.new(); bm.from_mesh(me)
    lim = math.radians(angle)
    for e in bm.edges:
        if len(e.link_faces) != 2 or e.calc_face_angle(0.0) > lim:
            e.smooth = False
    bm.to_mesh(me); bm.free()
    if bevel > 0 and "Bevel" not in ob.modifiers:
        md = ob.modifiers.new("Bevel", "BEVEL")
        md.width = bevel; md.segments = segs
        md.limit_method = "ANGLE"; md.angle_limit = math.radians(30)
        md.use_clamp_overlap = True; md.harden_normals = True

def drawer_chest(name, x1, y1, x2, y2, z, h, n, face, col, m="WoodLight", plinth=0.05):
    """Hollow carcass + n real drawers that slide out. face = pull direction: '-x', '+x', '-y', '+y'."""
    t = 0.018
    D = (x2 - x1) if face in ("-x", "+x") else (y2 - y1)
    Wd = (y2 - y1) if face in ("-x", "+x") else (x2 - x1)
    def wb(w1, w2, d1, d2, z1, z2, mi=0):
        if face == "-x": return (x2 - d2, y1 + w1, z + z1, x2 - d1, y1 + w2, z + z2, mi)
        if face == "+x": return (x1 + d1, y1 + w1, z + z1, x1 + d2, y1 + w2, z + z2, mi)
        if face == "-y": return (x1 + w1, y2 - d2, z + z1, x1 + w2, y2 - d1, z + z2, mi)
        return (x1 + w1, y1 + d1, z + z1, x1 + w2, y1 + d2, z + z2, mi)
    carcass = [wb(0, Wd, 0, D, h - t, h), wb(0, Wd, 0, D, plinth, plinth + t),
               wb(0, t, 0, D, 0, h), wb(Wd - t, Wd, 0, D, 0, h), wb(0, Wd, 0, t, 0, h),
               wb(t, Wd - t, 0, D - 0.03, 0, plinth)]
    hd = (h - plinth - 2 * t) / n
    for i in range(1, n):
        zz = plinth + t + hd * i
        carcass.append(wb(t, Wd - t, D - 0.06, D, zz - 0.006, zz + 0.006))
    body = mesh_obj(name, carcass, m, col)
    pull = {"-x": (-1, 0, 0), "+x": (1, 0, 0), "-y": (0, -1, 0), "+y": (0, 1, 0)}[face]
    travel = (D - t) * 0.72
    drawers = []
    for i in range(n):
        z0 = plinth + t + hd * i + 0.004; z1 = z0 + hd - 0.008
        g = 0.004; bt = 0.012
        b = [wb(t + g, Wd - t - g, D - 0.02, D, z0, z1, 0),                         # front panel
             wb(t + 0.01, Wd - t - 0.01, t + 0.01, D - 0.02, z0, z0 + bt, 0),      # bottom
             wb(t + 0.01, t + 0.01 + bt, t + 0.01, D - 0.02, z0, z1 - 0.03, 0),    # sides
             wb(Wd - t - 0.01 - bt, Wd - t - 0.01, t + 0.01, D - 0.02, z0, z1 - 0.03, 0),
             wb(t + 0.01, Wd - t - 0.01, t + 0.01, t + 0.01 + bt, z0, z1 - 0.03, 0),  # back
             wb(Wd / 2 - 0.05, Wd / 2 + 0.05, D, D + 0.022, (z0 + z1) / 2 - 0.01, (z0 + z1) / 2 + 0.01, 1)]  # handle
        dr = mesh_obj("%s_Drawer%d" % (name, i + 1), b, [m, "Metal"], col)
        dr["openable"] = "drawer"
        dr["open_offset"] = tuple(p * travel for p in pull)
        drawers.append(dr)
    return body, drawers
