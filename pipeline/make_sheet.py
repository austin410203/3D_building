# blender -b --factory-startup -P make_sheet.py  -> renders/contact_sheet_day.png (+ _night)
import bpy, os, json, sys
import numpy as np
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
SD = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(SD, ".."))
cat = json.load(open(os.path.join(ROOT, "export", "catalog.json"), encoding="utf8"))["assets"]
ids = [a["asset_id"] for a in cat if a.get("category") != "environment"]
if "--ids" in argv:
    ids = argv[argv.index("--ids") + 1].split(",")
TAG = argv[argv.index("--tag") + 1] if "--tag" in argv else ""
RD = argv[argv.index("--dir") + 1] if "--dir" in argv else os.path.join(ROOT, "renders")
TW, TH, COLS = 600, 375, 4
for suf in ("_day", ""):
    rows = (len(ids) + COLS - 1) // COLS
    sheet = np.zeros((rows * TH, COLS * TW, 4), np.float32); sheet[..., 3] = 1
    for i, bid in enumerate(ids):
        p = os.path.join(RD, "%s_front%s.png" % (bid, suf))
        if not os.path.exists(p):
            continue
        im = bpy.data.images.load(p); im.scale(TW, TH)
        px = np.array(im.pixels[:], np.float32).reshape(TH, TW, 4)
        r, c = i // COLS, i % COLS
        sheet[(rows - 1 - r) * TH:(rows - r) * TH, c * TW:(c + 1) * TW] = px
        bpy.data.images.remove(im)
    out = bpy.data.images.new("sheet", COLS * TW, rows * TH, alpha=False)
    out.pixels.foreach_set(sheet.ravel())
    out.filepath_raw = os.path.join(ROOT, "renders", "contact_sheet%s%s.png" % (TAG, suf or "_night"))
    out.file_format = "PNG"; out.save()
    print("sheet", out.filepath_raw)
