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
WALL = 1.5  # 壁厚mm



INCH = 6 * 25.4 * 2  # 6inch x 2

MOTOR_PITCH = INCH / 2 #* 1.47

# --- モーター ---
MOTOR_R = 38.2 / 2
MOTOR_D = R * 6

motor1 = base.create_cylinder(radius=MOTOR_R, depth=MOTOR_D)
base.taper(motor1, segments=64, curve="tear", power=0.75)
motor1.location=(0,MOTOR_PITCH,0)

motor2 = base.copy(motor1, location=(0, -MOTOR_PITCH, 0))

# --- 腕 ---
arm1 = base.create_tear_beam(depth=INCH, width=14.5, height=14.5*3, power=0.75)

base.modifier_apply(obj=motor1, target=arm1, operation="UNION")
base.modifier_apply(obj=motor2, target=arm1, operation="UNION")

arm2 = base.copy(arm1, rotation=(0, 0, math.pi / 2))

# --- 胴体 ---
body = base.create_cylinder_smooth(radius=R, depth=D/3-8) # 中央

body1 = base.create_cylinder_smooth(radius=R, depth=D) # 上部
base.taper(body1, segments=64, curve="tear", power=0.66)

body2 = base.create_cylinder_smooth(radius=R, depth=D) # 下部
base.taper(body2, segments=64, curve="tear", power=0.66, peak=0.66)

# --- 外形結合 ---
base.modifier_apply(obj=arm1, target=body, operation="UNION")
base.modifier_apply(obj=arm2, target=body, operation="UNION")
base.modifier_apply(obj=body1, target=body, operation="UNION")
base.modifier_apply(obj=body2, target=body, operation="UNION")

## --- 中空化 ---
#inner = base.create_cylinder_smooth(radius=R-WALL, depth=D/3-8)

#inner1 = base.create_cylinder_smooth(radius=R-WALL, depth=D)
#base.taper(inner1, segments=64, curve="tear", power=0.66)
#inner2 = base.create_cylinder_smooth(radius=R-WALL, depth=D)
#base.taper(inner2, segments=64, curve="tear", power=0.66, peak=0.66)

#arm1_inner = base.create_tear_beam(
#    depth=INCH, width=arm_width-WALL*2, height=arm_height-WALL*2, power=arm_power,
#)
#arm2_inner = base.create_tear_beam(
#    depth=INCH, width=arm_width-WALL*2, height=arm_height-WALL*2, power=arm_power,
#)
#arm2_inner.rotation_euler[2] = math.pi / 2

#base.modifier_apply(obj=inner1, target=inner, operation="UNION")
#base.modifier_apply(obj=inner2, target=inner, operation="UNION")
#base.modifier_apply(obj=arm1_inner, target=inner, operation="UNION")
#base.modifier_apply(obj=arm2_inner, target=inner, operation="UNION")
#base.modifier_apply(obj=inner, target=body, operation="DIFFERENCE")

## --- 前面カット ---
##base.cut_cube(target=body, scale=(200, 200, 500), location=(0, -100, 0))

