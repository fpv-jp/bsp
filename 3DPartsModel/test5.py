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

adjustment = 1.47  # アームの長さ/モータ位置を調整する倍率

INCH = 6 * 25.4 * adjustment  # 6inch

ARM_L = INCH / 2


MOTOR_SIZE = 37.5
MOTOR_PITCH = 19.0

MAIN_DEPTH = 5.0

M3 = 3.0

# モーター
motor = base.create_cube(scale=(MOTOR_PITCH + M3 * 1.141, MOTOR_PITCH - M3 * 1.75, MAIN_DEPTH))
base.add_cube(target=motor, scale=(MOTOR_PITCH - M3 * 1.75, MOTOR_PITCH + M3 * 1.141, MAIN_DEPTH))

# 腕
base.add_cube(target=motor, scale=(12, ARM_L, MAIN_DEPTH), location=(0.0, ARM_L / 2, 0.0))


# モータ取り付け穴
motor.rotation_euler[2] = math.pi / 4
MOTOR_HOLES = [
    (MOTOR_PITCH / 2, 0),
    (-MOTOR_PITCH / 2, 0),
    (0, MOTOR_PITCH / 2),
    (0, -MOTOR_PITCH / 2),
]

for i, (x, y) in enumerate(MOTOR_HOLES):
    base.add_ring(
        target=motor,
        outer_radius=M3 * 1.5,
        inner_radius=M3 / 2,
        depth=MAIN_DEPTH,
        location=(x, y, 0.0),
        vertices=64,
    )

# 中心を変える(ボディ取り付け角カット)----------------------------
motor.rotation_euler[2] = 0
motor.location = (0.0, -ARM_L, 0.0)
base.set_origin(motor, (0.0, 0.0, 0.0))  # 回転の起点をシーンの(0,0,0)に設定

# ボディ取り付け角カット----------------------------
motor.rotation_euler[2] = math.pi / 4
base.cut_cube(target=motor, scale=(20, 10, 10), location=(0.0, 5.0, 0.0))
motor.rotation_euler[2] = -math.pi / 4
base.cut_cube(target=motor, scale=(20, 10, 10), location=(0.0, 5.0, 0.0))
motor.rotation_euler[2] = 0

# ボディ取り付け穴----------------------------
base.cut_cylinder(target=motor, radius=M3 / 2, depth=MAIN_DEPTH * 2)
base.cut_cylinder(target=motor, radius=M3 / 2, depth=MAIN_DEPTH * 2, location=(0.0, -30.5 / 2, 0.0))

# 中心を戻す----------------------------
#motor.location = (0.0, ARM_L/2, 0.0)
#base.set_origin(motor, (0.0, 0.0, 0.0))  # 回転の起点をシーンの(0,0,0)に設定

