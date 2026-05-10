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


# body ----------------------------------------

# 涙型の流線型ボディ
R = 30.0
D = R*6
body = base.create_cylinder(
    radius=R,
    depth=D,
)
base.taper(body, segments=64, curve="tear", power=0.7)

# 内側をくり抜く（壁厚1.5mm）
inner = base.create_cylinder(
    radius=R-1.5,
    depth=D,
)
base.taper(inner, segments=16, curve="tear", power=0.7)
base.modifier_apply(inner, body, operation="DIFFERENCE")

# motor ----------------------------------------

R = 20.0
D = R*6
motor = base.create_cylinder(
    radius=R,
    depth=D,
)
base.taper(motor, segments=64, curve="tear", power=0.75)

# 内側をくり抜く（壁厚1.5mm）
inner = base.create_cylinder(
    radius=R-1.5,
    depth=D,
)
base.taper(inner, segments=16, curve="tear", power=0.75)
base.modifier_apply(inner, motor, operation="DIFFERENCE")

INCH = 152.4 # 6inch

MOTOR_X = INCH / 2 * 1.47
motor.location = (MOTOR_X, 0, 10)

# arm ----------------------------------------

arm = base.create_tear_beam(
    depth=MOTOR_X,       # ビームの長さ（Y軸）
    width=8,             # 断面の幅（X）
    height=20,           # 断面の涙型の高さ（Z）
    power=0.7,
    location=(MOTOR_X / 2, 0, 0),
    rotation=(0, 0, -math.pi / 2),  # Y軸→X軸方向に回転
)
