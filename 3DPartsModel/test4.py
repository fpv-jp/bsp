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

BODY_R = 35.0
BODY_D = BODY_R * 10

WALL = 1.5  # 壁厚mm

TEST_CUT = True

def create_motor(sharpen):
    # --- モータ ---
    motor = base.create_cylinder_smooth(radius=MOTOR_R - sharpen, depth=MOTOR_D)
    base.taper(motor, segments=32, curve="tear", power=0.88)
    motor.location = (0, MOTOR_PITCH, 15)
    return motor


def create_arm_motor(sharpen):
    # --- モータ ---
    motor1 = create_motor(sharpen)
    motor2 = base.copy(motor1, location=(0, -MOTOR_PITCH, 0))

    # --- 腕 ---
    arm = base.create_tear_beam(depth=INCH, width=ARM_W - sharpen * 2, height=ARM_W * 3 - sharpen * 2, power=0.75)

    # --- 腕にモータを結合 ---
    base.modifier_apply(obj=motor1, target=arm, operation="UNION")
    base.modifier_apply(obj=motor2, target=arm, operation="UNION")
    return arm


def create_body(sharpen):
    # --- 胴体 中央 ---
    body = base.create_cylinder_smooth(radius=BODY_R - sharpen, depth=BODY_D / 3 - 8)

    # --- 胴体 上部 ---
    body_top = base.create_tear_body(radius=BODY_R - sharpen, depth=BODY_D, power=0.66)

    # --- 胴体 下部 ---
    body_bottom = base.create_tear_body(radius=BODY_R - sharpen, depth=BODY_D, power=0.66, peak=0.66)

    # --- 胴体結合 ---
    base.modifier_apply(obj=body_top, target=body, operation="UNION")
    base.modifier_apply(obj=body_bottom, target=body, operation="UNION")
    return body


# --------------------------------------------
# --- 外形 -----------------------------------
# --------------------------------------------

armY = create_arm_motor(0)
armY.location = (0.0, 0.0, 35)

armX = base.copy(armY, rotation=(0, 0, math.pi / 2))

# --- 外形結合 ---
body = create_body(0)
base.modifier_apply(obj=armY, target=body, operation="UNION")
base.modifier_apply(obj=armX, target=body, operation="UNION")

# --------------------------------------------
# --- 中空化 ---------------------------------
# --------------------------------------------
armY_inner = create_arm_motor(WALL)
armY_inner.location = (0.0, 0.0, 35)

armX_inner = base.copy(armY_inner, rotation=(0, 0, math.pi / 2))

# ---内形結合 ---
body_inner = create_body(WALL)
base.modifier_apply(obj=armY_inner, target=body_inner, operation="UNION")
base.modifier_apply(obj=armX_inner, target=body_inner, operation="UNION")

# ---中空化 ---
base.modifier_apply(obj=body_inner, target=body, operation="DIFFERENCE")

# --- 確認のため前面カット ---
if TEST_CUT:
    base.bisect(body, plane_co=(0, 0, 0), plane_no=(0, 1, 0), clear_outer=True)
