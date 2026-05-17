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

adjustment = 1.47 # アームの長さ/モータ位置を調整する倍率

INCH = 6 * 25.4 * adjustment  # 6inch

MOTOR_PITCH = INCH / 2 #* 1.47

ARM_W = 14.5

MOTOR_R = 38.2 / 2
MOTOR_D = MOTOR_R * 8

BODY_R = 35.0
BODY_D = BODY_R * 10

WALL = 1.5  # 壁厚mm

# --------------------------------------------
# --- 外形 -----------------------------------
# --------------------------------------------

# --- モーター ---
motor1 = base.create_cylinder_smooth(radius=MOTOR_R, depth=MOTOR_D)
base.taper(motor1, segments=32, curve="tear", power=0.88)
motor1.location=(0,MOTOR_PITCH,0)

motor2 = base.copy(motor1, location=(0, -MOTOR_PITCH, 0))

# --- 腕 ---
arm1 = base.create_tear_beam(depth=INCH, width=ARM_W, height=ARM_W*3, power=0.75)

base.modifier_apply(obj=motor1, target=arm1, operation="UNION")
base.modifier_apply(obj=motor2, target=arm1, operation="UNION")

arm2 = base.copy(arm1, rotation=(0, 0, math.pi / 2))

# --- 胴体 ---
body = base.create_cylinder_smooth(radius=BODY_R, depth=BODY_D/3-8) # 中央

body1 = base.create_tear_body(radius=BODY_R, depth=BODY_D, power=0.66) # 上部
body2 = base.create_tear_body(radius=BODY_R, depth=BODY_D, power=0.66, peak=0.66) # 下部

# --- 外形結合 ---
base.modifier_apply(obj=arm1, target=body, operation="UNION")
base.modifier_apply(obj=arm2, target=body, operation="UNION")
base.modifier_apply(obj=body1, target=body, operation="UNION")
base.modifier_apply(obj=body2, target=body, operation="UNION")

# --------------------------------------------
# --- 中空化 ---------------------------------
# --------------------------------------------
#body_inner = base.create_cylinder_smooth(radius=BODY_R-WALL, depth=BODY_D/3-8)
#body_inner1 = base.create_tear_body(radius=BODY_R-WALL, depth=BODY_D, power=0.66)
#body_inner2 = base.create_tear_body(radius=BODY_R-WALL, depth=BODY_D, power=0.66, peak=0.66)

#arm_inner = base.create_tear_beam(depth=INCH, width=ARM_W-WALL*2, height=ARM_W*3-WALL*2, power=0.75)
#arm_inner2 = base.copy(arm_inner, rotation=(0, 0, math.pi / 2))

#base.modifier_apply(obj=body_inner1, target=body_inner, operation="UNION")
#base.modifier_apply(obj=body_inner2, target=body_inner, operation="UNION")
#base.modifier_apply(obj=arm_inner,   target=body_inner, operation="UNION")
#base.modifier_apply(obj=arm_inner2,  target=body_inner, operation="UNION")

## --- 確認のため前面カット ---
#test = base.create_cube(scale=(400, 400, 400), location=(0, -200, 0))
#base.modifier_apply(obj=test,  target=body_inner, operation="UNION")

#base.modifier_apply(obj=body_inner,  target=body,  operation="DIFFERENCE")

# --- 確認のため前面カット ---
#test = base.create_cube(scale=(400, 400, 400), location=(0, -200, 0))
#base.modifier_apply(obj=test, target=body, operation="DIFFERENCE")

# ------------------------
test = base.create_cube(scale=(400, 400, 400), location=(0, 0, 200))
base.modifier_apply(obj=test,  target=body, operation="DIFFERENCE")
body.rotation_euler[0] = math.pi
body.rotation_euler[2] = math.pi / 4
