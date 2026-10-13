# python gen_catalog_md.py  -> ../CATALOG.md  (reads ../export/catalog.json)
import json, os
SD = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(SD, ".."))
doc = json.load(open(os.path.join(ROOT, "export", "catalog.json"), encoding="utf8"))
A = [a for a in doc["assets"] if a.get("category") != "environment"]
env = [a for a in doc["assets"] if a.get("category") == "environment"]
order = {"budget": 0, "utility": 1, "civic": 2, "standard": 3, "upscale": 4, "luxury": 5, "landmark": 6}
A.sort(key=lambda a: (order.get(a["tier"], 9), a["asset_id"]))
L = []
L.append("# TownKit 建築資產目錄 / Building Asset Catalog\n")
L.append("Procedurally built in Blender 5.2 (`scripts/`), placed on one island template (`TownKit.blend`). "
         "Every building is walkable inside (stairs, doors, furnished rooms) and carries machine-readable metadata.\n")
L.append("## 快速索引 Quick index\n")
L.append("| asset_id | 名稱 | Name | 風格 Style | Tier | Type | Floors | Size W×D×H (m) | Game styles |")
L.append("|---|---|---|---|---|---|---|---|---|")
for a in A:
    s = a["size_m"]
    L.append("| `%s` | %s | %s | %s / %s | %s | %s | %s | %.1f × %.1f × %.1f | %s |" % (
        a["asset_id"], a["name_zh"], a["name_en"], a["style_zh"], a["style"], a["tier"], a["category"], a["floors"],
        s[0], s[1], a["height_m"], ", ".join(a["game_styles"])))
L.append("")
L.append("## 如何取用 How to fetch an asset\n")
L.append("* **Blender (append/link):** `TownKit.blend` → collection `BLD_<asset_id>` (marked as Asset with tags; root empty `BLD_<asset_id>`). "
         "Labels live in the child collection `LBL_<asset_id>` — exclude it for in-game use.")
L.append("```python\nimport bpy\npath = r\"C:/Users/Administrator/Documents/Gaming/TownKit/TownKit.blend\"\n"
         "with bpy.data.libraries.load(path, link=False) as (src, dst):\n    dst.collections = [\"BLD_cafe_container\"]\n"
         "for c in dst.collections:\n    bpy.context.scene.collection.children.link(c)\n```")
L.append("* **Game engines:** `export/glb/<asset_id>.glb` — origin = plot centre at ground level, front = glTF +Z (Blender −Y), "
         "metres, Y-up. Node custom properties arrive as glTF `extras` (see conventions below). Labels are not included.")
L.append("* **Compressed (recommended for games / web):** `export/glb_draco/<asset_id>.glb` — Draco geometry + 512 px WebP textures, "
         "~5–12 MB each (full-res originals in `export/glb/`). Needs a Draco decoder (three.js DRACOLoader, Godot 4 / Blender native, Unity glTFast + Draco package).")
L.append("* **Whole island:** `export/glb/town_full.glb` (everything placed) and `export/glb/island_town.glb` (terrain/streets only).")
L.append("* **Machine catalog:** `export/catalog.json` (all fields below + entrances/spawns/interactables/object counts).")
L.append("* **Rebuild / edit:** `blender -b --factory-startup -P scripts/build.py` (all) or `-- --only <id>`; "
         "then `blender -b TownKit.blend -P scripts/export.py`.\n")
L.append("## 慣例 Conventions (glTF extras / Blender custom props)\n")
for k, v in doc["conventions"]["custom_props (glTF extras)"].items():
    L.append("* `%s` — %s" % (k, v))
L.append("* front: %s" % doc["conventions"]["front"])
L.append("* object names: %s\n" % doc["conventions"]["object_name"])
L.append("## 建築明細 Buildings\n")
for a in A:
    f = a["files"]
    L.append("### %s %s — `%s`\n" % (a["name_zh"], a["name_en"], a["asset_id"]))
    L.append("![day](%s) ![night](%s) ![plan](%s)\n" % (f["preview_day"], f["preview_night"], f["preview_plan"]))
    L.append("* **Style:** %s / %s · **Tier:** %s · **Type:** %s · **Floors:** %s" % (a["style_zh"], a["style"], a["tier"], a["category"], a["floors"]))
    L.append("* **Fits game styles:** %s" % ", ".join(a["game_styles"]))
    L.append("* **Description:** %s" % a["description"])
    L.append("* **Size:** %.1f × %.1f m footprint, %.1f m tall · %s objects · ~%s tris · %s lights · %s furniture pieces" % (
        a["size_m"][0], a["size_m"][1], a["height_m"], a["objects"], a["triangles_approx"], a["lights"], a["furniture"]))
    ent = ", ".join("%s(%s side)" % (e["name"].split(".")[-1], e["side"]) for e in a["entrances"]) or "-"
    L.append("* **Exterior doors:** %s · interior doors: %s" % (ent, a["interior_doors"]))
    L.append("* **Spawn points (local m):** %s" % ", ".join("%s %s" % (s["name"], tuple(s["local"])) for s in a["spawns"]))
    L.append("* **Interactions:** %s" % ", ".join(a["interactables"]))
    L.append("* **Placed on island at:** %s, rotZ %s° · **Files:** `%s`, Blender collection `%s`\n" % (
        tuple(a["position"]), a["rotation_z_deg"], f["glb"], f["blend_collection"]))
if env:
    e = env[0]
    L.append("## 環境 Environment — `%s`\n" % e["asset_id"])
    L.append("Island ~300×225 m: town flats, two crossing streets with sidewalks, curbs, lane markings, zebra crossings, "
             "street lamps, beach palms, snowy north hill (polar station plateau, z = 7 m), sea plane at z = −0.6 m. "
             "File: `%s`.\n" % e["files"]["glb"])
open(os.path.join(ROOT, "CATALOG.md"), "w", encoding="utf8").write("\n".join(L))
print("CATALOG.md written,", len(A), "buildings")
