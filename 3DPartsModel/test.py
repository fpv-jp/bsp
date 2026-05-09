import bpy
import bmesh
import math
import sys
import types

text = bpy.data.texts.get("base.py")
module_name = "base"
module = types.ModuleType(module_name)
exec(text.as_string(), module.__dict__)
sys.modules[module_name] = module

import base

# 初期化
base.init()

# main = base.create_rounded_cone(
#     radius=15.0,
#     depth=60,
#     vertices=96,
#     rings=32,
# )
main = base.create_cylinder(
    radius=15.0,
    depth=60,
)

base.taper(main, top_scale=0.0, segments=16, curve="cos")

inner = base.create_cylinder(
    radius=13.5,
    depth=60,
    location=(0, 0, -1.5),
)
base.taper(inner, top_scale=0.0, segments=16, curve="cos")
base.modifier_apply(inner, main, operation="DIFFERENCE")
