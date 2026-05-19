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

# test5オブジェクトをinitの削除から保護
#_test5 = bpy.data.objects.get("test5")
#if _test5:
#    _test5.hide_set(True)

base.init()

#if _test5:
#    _test5.hide_set(False)

adjustment = 1.47  # アームの長さ/モータ位置を調整する倍率

INCH = 6 * 25.4 * adjustment  # 6inch

MOTOR_PITCH = INCH / 2

ARM_W = 14.5

MOTOR_R = 38.2 / 2
MOTOR_D = MOTOR_R * 8

BODY_R = 33.0
BODY_D = BODY_R * 10

WALL = 1.5  # 壁厚mm

#TEST_CUT = True
TEST_CUT = False


def create_motor(sharpen):
    # --- モータ ---
    motor = base.create_cylinder(radius=MOTOR_R - sharpen, depth=MOTOR_D, vertices=64)
    base.taper(motor, segments=32, curve="tear", power=0.75)
#    if sharpen > 0:
#        base.add_cylinder(target=motor, radius=MOTOR_R + 0.25, depth=100, location=(0.0, 0.0, 60))


    return motor


def create_arm(sharpen):
    # --- 腕 中央 ---
    arm = base.create_cube(
        scale=(ARM_W - sharpen * 2, INCH / 1.75, ARM_W * 3 - sharpen * 2),
        location=(0.0, INCH / 4, 0.0),
    )

    # --- 腕 上部 ---
    arm_top = base.create_tear_beam(
        depth=INCH / 1.75,
        width=ARM_W - sharpen * 2,
        height=ARM_W * 3 - sharpen * 2,
        power=0.75,
        location=(0.0, INCH / 4, -ARM_W * 1.2),
    )

    base.modifier_apply(obj=arm_top, target=arm, operation="UNION")
    arm.rotation_euler = (math.pi / 8, 0, 0)
    arm.location = (0.0, 0.0, -ARM_W * 1.4)

    base.cut_cube(
        target=arm,
        scale=(ARM_W, INCH, ARM_W * 4),
        location=(0.0, INCH / 4, ARM_W * 1.75),
    )

    # --- 腕 下部 ---
    arm_bottom = base.create_tear_beam(
        depth=INCH / 2,
        width=ARM_W - sharpen * 2,
        height=ARM_W * 3 - sharpen * 2,
        power=0.75,
        location=(0.0, INCH / 4, 0.0),
    )
    base.modifier_apply(obj=arm_bottom, target=arm, operation="UNION")
    
    #test-------------------------------------
#    base.add_cube(
#        target=arm,
#        scale=(ARM_W+1, INCH, 6.0),
#        location=(0.0, 0.0, -5.0),
#    )
#    base.add_cylinder(
#        target=arm,
#        radius=MOTOR_R,
#        depth=6.0,
#        location=(0.0, MOTOR_PITCH, -5.0),
#    )

    return arm


def create_body(sharpen):
    # --- 胴体 中央 ---
    body = base.create_cylinder(
        radius=BODY_R - sharpen, depth=BODY_D / 2.5, location=(0.0, 0.0, 11.0), vertices=64
    )

    # --- 胴体 上部 ---
    body_top = base.create_tear_body(
        radius=BODY_R - sharpen, depth=BODY_D, power=0.66, smooth=False
    )

    # --- 胴体 下部 ---
    body_bottom = base.create_tear_body(
        radius=BODY_R - sharpen, depth=BODY_D, power=0.66, peak=0.75, smooth=False
    )
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

arm = create_arm(0)
motor = create_motor(0)

motor.location = (0, MOTOR_PITCH, 15)

# --- 腕にモータを結合 ---
base.modifier_apply(obj=motor, target=arm, operation="UNION")

# bottom cut-------------------------------------
base.cut_cylinder(
    target=arm,
    radius=MOTOR_R+WALL,
    depth=100.0,
    location=(0.0, MOTOR_PITCH, 50.0+6.0),
)
    
arm.location = (0.0, 0.0, 34)

arm2 = base.copy(arm, rotation=(math.pi / 8, 0, math.pi))
arm3 = base.copy(arm2, rotation=(math.pi / 8, 0, math.pi / 2))
arm4 = base.copy(arm2, rotation=(math.pi / 8, 0, -math.pi / 2))

# --- 胴体に腕を結合 ---
body = create_body(0)
base.modifier_apply(obj=arm, target=body, operation="UNION")
base.modifier_apply(obj=arm2, target=body, operation="UNION")
base.modifier_apply(obj=arm3, target=body, operation="UNION")
base.modifier_apply(obj=arm4, target=body, operation="UNION")


## --------------------------------------------
## --- 中空化 ---------------------------------
## --------------------------------------------

## ---内形結合 ---
# body_inner = create_body(WALL)
# arm_inner = create_arm_motor(WALL)
# arm_inner.location = (0.0, 0.0, 60)
# base.modifier_apply(obj=arm_inner, target=body_inner, operation="UNION")

## ---中空化 ---
# base.modifier_apply(obj=body_inner, target=body, operation="DIFFERENCE")

## --- test5でDIFFERENCE ---
##if _test5:
##    _test5.hide_set(False)
##    base.modifier_apply(obj=_test5, target=body, operation="DIFFERENCE")

# --- 確認のため前面カット ---
if TEST_CUT:
    base.bisect(body, plane_co=(0, 0, 0), plane_no=(0, 1, 0), clear_outer=True)
