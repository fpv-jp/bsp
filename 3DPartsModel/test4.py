import bpy
import math
import sys
import types

text = bpy.data.texts.get("base.py")
module_name = "base"
module = types.ModuleType(module_name)
exec(text.as_string(), module.__dict__)
sys.modules[module_name] = module

import base

base.init()
R = 35.0
D = R * 10

segments=64
curve="tear"
power=0.60

body = base.create_cylinder_smooth(radius=R, depth=D)
base.taper(body, segments=segments, curve=curve, power=power)

# 内側をくり抜く（壁厚1.5mm）
inner = base.create_cylinder_smooth(radius=R*0.95, depth=D)
base.taper(inner, segments=segments, curve=curve, power=power)
base.modifier_apply(inner, body, operation="DIFFERENCE")


INCH = 12 * 25.4  # 6inch

arm_width = 14.5
arm_height = arm_width*3
arm_power = 0.75

arm = base.create_tear_beam(
    depth=INCH,  # ビームの長さ（Y軸）
    width=arm_width,  # 断面の幅（X）
    height=arm_height,  # 断面の涙型の高さ（Z）
    power=arm_power,
)