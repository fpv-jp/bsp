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

_test4_all = bpy.data.objects.get("test4-all_fixed")
if _test4_all:
    _test4_all.hide_set(True)

base.init()

if _test4_all:
    _test4_all.hide_set(False)


adjustment = 1.47  # アームの長さ/モータ位置を調整する倍率

INCH = 6.0 * 25.4 * adjustment  # 6inch

MOTOR_PITCH = INCH / 2

ARM_W = 14.5
ARM_W = 12.0

MOTOR_R = 38.2 / 2
MOTOR_D = MOTOR_R * 8

BODY_R = 30.0
BODY_D = BODY_R * 12

WALL = 1.5  # 壁厚mm

CUT = True
CUT = False

H = 65.0

if CUT:
    base.cut_cylinder(
        target=_test4_all,
        radius=94.0,
        depth=6 + H,
        location=(0.0, 0.0, -75.0 - H / 2),
        vertices=128,
    )
else:
    base.create_cylinder(
        radius=94.0,
        depth=6 + H,
        location=(0.0, 0.0, -75.0 - H / 2),
        vertices=128,
    )

if CUT:
    base.cut_cylinder(
        target=_test4_all,
        radius=BODY_R + 1,
        depth=6 + H,
        location=(0.0, 0.0, 115.0 + H / 2),
        vertices=128,
    )
else:
    base.create_cylinder(
        radius=BODY_R + 1,
        depth=6 + H,
        location=(0.0, 0.0, 115.0 + H / 2),
        vertices=128,
    )

if CUT:
    base.cut_cube(
        target=_test4_all,
        scale=(
            BODY_R,
            BODY_R * 2,
            BODY_R * 4,
        ),
        location=(0.0, BODY_R, BODY_R * 2),
    )
else:
    base.create_cube(
        scale=(
            BODY_R,
            BODY_R * 2,
            BODY_R * 4,
        ),
        location=(0.0, BODY_R, BODY_R * 2),
    )
