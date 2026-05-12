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

batteryD = 57*2

Thickness = 1.75

# body ----------------------------------------

# 涙型の流線型ボディ
R = 28.5
D = R*6
body = base.create_cylinder(
    radius=R,
    depth=D,
)
base.taper(body, segments=64, curve="tear", power=0.75)

# 内側をくり抜く（壁厚1.5mm）
inner = base.create_cylinder(
    radius=R-Thickness,
    depth=D,
)
base.taper(inner, segments=16, curve="tear", power=0.75)
base.modifier_apply(inner, body, operation="DIFFERENCE")

base.cut_cylinder(
    target=body,
    radius=R,
    depth=120.0,
    location = (0, 0, 41.0)
)

body.location = (0, 0, -batteryD /2+19)

## battery ----------------------------------------

#R = 28.5
battery = base.create_cylinder(
    radius=R,
    depth=batteryD,
)

base.cut_cylinder(
    target=battery,
    radius=R-Thickness,
    depth=batteryD,
)

base.modifier_apply(obj=battery, target=body, operation="UNION")

## motor ----------------------------------------

#R = 37.5/2
#D = R*6
#motor = base.create_cylinder(
#    radius=R,
#    depth=D,
#)
#base.taper(motor, segments=64, curve="tear", power=0.75)

## 内側をくり抜く（壁厚1.5mm）
##inner = base.create_cylinder(
##    radius=R-1.5,
##    depth=D,
##)
##base.taper(inner, segments=16, curve="tear", power=0.75)
##base.modifier_apply(inner, motor, operation="DIFFERENCE")

#INCH = 152.4 # 6inch

#MOTOR_X = INCH / 2 * 1.47
#motor.location = (MOTOR_X, 0, 0)
##motor.location = (MOTOR_X, 0, 10)

## arm ----------------------------------------¬

#arm = base.create_tear_beam(
#    depth=MOTOR_X,       # ビームの長さ（Y軸）
#    width=8,             # 断面の幅（X）
#    height=20,           # 断面の涙型の高さ（Z）
#    power=0.75,
#    location=(MOTOR_X / 2, 0, 0),
#    rotation=(0, 0, -math.pi / 2),  # Y軸→X軸方向に回転
#)
##arm.location = (MOTOR_X / 2, 0, 2.5)
