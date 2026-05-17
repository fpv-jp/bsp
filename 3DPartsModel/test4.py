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

MOTOR_PITCH = INCH / 2

ARM_W = 14.5

MOTOR_R = 38.2 / 2
MOTOR_D = MOTOR_R * 8

BODY_R = 33.0
BODY_D = BODY_R * 10

WALL = 1.5  # 壁厚mm

# TEST_CUT = True
TEST_CUT = False


def create_motor(sharpen):
    # --- モータ ---
    motor = base.create_cylinder(radius=MOTOR_R - sharpen, depth=MOTOR_D, vertices=64)
    base.taper(motor, segments=32, curve="tear", power=0.88)
    if sharpen > 0:
        base.add_cylinder(target=motor, radius=MOTOR_R, depth=100, location=(0.0, 0.0, 30))
    return motor


def create_arm_motor(sharpen):
    # --- 腕 ---
    arm = base.create_tear_beam(
        depth=INCH, width=ARM_W - sharpen * 2, height=ARM_W * 3 - sharpen * 2, power=0.75, smooth=False
    )

    # --- モータ ---
    motor1 = create_motor(sharpen)
    motor1.location = (0, MOTOR_PITCH, 0)
    motor2 = create_motor(sharpen)
    motor2.location = (0, -MOTOR_PITCH, 0)
    
    arm.location = (0.0, 0.0, -15)
    
    # --- 腕にモータを結合 ---
    base.modifier_apply(obj=motor1, target=arm, operation="UNION")
    base.modifier_apply(obj=motor2, target=arm, operation="UNION")

    arm2 = base.copy(arm, rotation=(0, 0, math.pi / 2))
    base.modifier_apply(obj=arm2, target=arm, operation="UNION")
    return arm


def create_body(sharpen):
    # --- 胴体 中央 ---
    body = base.create_cylinder(radius=BODY_R - sharpen, depth=BODY_D / 2.5, location=(0.0,0.0,11.0), vertices=64)

    # --- 胴体 上部 ---
    body_top = base.create_tear_body(radius=BODY_R - sharpen, depth=BODY_D, power=0.66, smooth=False)

    # --- 胴体 下部 ---
    body_bottom = base.create_tear_body(radius=BODY_R - sharpen, depth=BODY_D, power=0.66, peak=0.75, smooth=False)
    if sharpen > 0:
        base.add_cylinder(
            target=body_bottom, radius=BODY_R, depth=100, location=(0.0, 0.0, BODY_D / 1.9)
        )

    # --- 胴体結合 ---
    base.modifier_apply(obj=body_top, target=body, operation="UNION")
    base.modifier_apply(obj=body_bottom, target=body, operation="UNION")

    return body


# --------------------------------------------
# --- 外形 -----------------------------------
# --------------------------------------------

# --- 外形結合 ---
body = create_body(0)
arm = create_arm_motor(0)
arm.location = (0.0, 0.0, 80)
base.modifier_apply(obj=arm, target=body, operation="UNION")

# --------------------------------------------
# --- 中空化 ---------------------------------
# --------------------------------------------

# ---内形結合 ---
body_inner = create_body(WALL)
arm_inner = create_arm_motor(WALL)
arm_inner.location = (0.0, 0.0, 80)
base.modifier_apply(obj=arm_inner, target=body_inner, operation="UNION")

# ---中空化 ---
base.modifier_apply(obj=body_inner, target=body, operation="DIFFERENCE")

## --- 確認のため前面カット ---
# if TEST_CUT:
#    base.bisect(body, plane_co=(0, 0, 0), plane_no=(0, 1, 0), clear_outer=True)

# base.create_cylinder(
#    radius=BODY_R/3,
#    depth=450,
# )
