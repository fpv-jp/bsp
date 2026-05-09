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

# 涙型の流線型ボディ
main = base.create_cylinder(
    radius=23.0,
    depth=160,
)
base.taper(main, segments=64, curve="tear", power=0.65)

# 内側をくり抜く（壁厚1.5mm）
inner = base.create_cylinder(
    radius=13.5,        # 15.0 - 1.5
    depth=60,
#    location=(0, 0, -1.5),  # 下にずらして底を開口、先端に1.5mm残す
)
base.taper(inner, segments=16, curve="tear", power=0.7)
base.modifier_apply(inner, main, operation="DIFFERENCE")
