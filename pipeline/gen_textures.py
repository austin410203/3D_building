# blender -b --factory-startup -P gen_textures.py
import os
SD = os.path.dirname(os.path.abspath(__file__))
g = {"LIB": os.path.join(SD, "lib_core.py"), "__name__": "__tk__"}
for f in ("textures.py", "textures2.py"):
    exec(open(os.path.join(SD, f), encoding="utf8").read(), g)
