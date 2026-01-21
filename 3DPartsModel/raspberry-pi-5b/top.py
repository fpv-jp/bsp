import bpy
import sys
import types
import math

text = bpy.data.texts.get("base.py")
module_name = "base"
module = types.ModuleType(module_name)
exec(text.as_string(), module.__dict__)
sys.modules[module_name] = module

import base

base.init()

MAIN_WIDTH = 85.0
MAIN_HEIGHT = 56.0
MAIN_DEPTH = 14.5
MAIN_THICKNESS = 2.0

main = base.create_cube(
    scale=(MAIN_WIDTH + MAIN_THICKNESS, MAIN_HEIGHT + MAIN_THICKNESS, MAIN_DEPTH),
)

BASE_X = MAIN_WIDTH / 2
BASE_Y = MAIN_HEIGHT / 2

M2_7 = 1.35

scale = (M2_7 * 2, M2_7 * 2, MAIN_DEPTH)
rotation = (0.0, 0.0, 0.0)

base.cut_plates(
    target=main,
    plates=[
        (scale, (BASE_X, BASE_Y, 0), rotation),
        (scale, (BASE_X, -BASE_Y, 0), rotation),
        (scale, (-BASE_X, BASE_Y, 0), rotation),
        (scale, (-BASE_X, -BASE_Y, 0), rotation),
    ],
)
c = [
    (BASE_X - M2_7, BASE_Y - M2_7),
    (BASE_X - M2_7, -BASE_Y + M2_7),
    (-BASE_X + M2_7, BASE_Y - M2_7),
    (-BASE_X + M2_7, -BASE_Y + M2_7),
]
base.add_pins(
    target=main,
    radius=M2_7 * 1.74,
    depth=MAIN_DEPTH,
    positions=c,
)

H = -MAIN_THICKNESS / 2

base.cut_holes(
    target=main,
    radius=M2_7 + 0.1,
    depth=MAIN_DEPTH,
    z=H,
    positions=c,
)

GAP = 0.2

base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH - M2_7 * 2, MAIN_HEIGHT + GAP, MAIN_DEPTH),
    location=(0, 0, H),
)
base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH + GAP, MAIN_HEIGHT - M2_7 * 2, MAIN_DEPTH),
    location=(0, 0, H),
)

################################################

P_X = -BASE_X + 3.5
P_Y = BASE_Y - 3.5

XX = 58.0
YY = 49.0

BORN = 2.75

base.cut_cube(
    target=main,
    scale=(XX + BORN, YY + BORN, MAIN_DEPTH),
    location=(-10.0, 0, MAIN_THICKNESS),
)
base.cut_cube(
    target=main,
    scale=(XX - 5, YY + BORN, MAIN_DEPTH),
    location=(-10.0, 1, MAIN_THICKNESS),
)

c = [
    (P_X, P_Y),
    (P_X, P_Y - YY),
    (P_X + XX, P_Y),
    (P_X + XX, P_Y - YY),
]
base.add_pins(
    target=main,
    radius=M2_7 + 1,
    depth=MAIN_THICKNESS / 2,
    positions=c,
    z=MAIN_DEPTH / 2 - MAIN_THICKNESS / 4,
)
base.cut_holes(
    target=main,
    radius=M2_7,
    depth=MAIN_DEPTH + MAIN_THICKNESS,
    positions=c,
)

################################################

BASE_Z = (MAIN_DEPTH - MAIN_THICKNESS) / 2


def cube_cut(scale, Y):
    X = BASE_X - scale[0] / 2 + 1
    Z = BASE_Z - scale[2] / 2
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut(scale=(10, 13.2, 14.5), Y=-BASE_Y + 29.1)
cube_cut(scale=(10, 13.2, 14.5), Y=-BASE_Y + 47.0)


def cube_cut2(scale, Y):
    X = BASE_X - scale[0] / 2 + 1
    Z = BASE_Z - scale[2] / 2 - 3.0
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut2(scale=(20, 16.2, 13.3), Y=-BASE_Y + 10.2)


def cube_cut3(scale, Y):
    X = -BASE_X + scale[0] / 2 - 1
    Z = BASE_Z - scale[2] / 2
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut3(scale=(10, 9.0, 14.5), Y=2)


def cube_cut4(scale, Y):
    X = -BASE_X + scale[0] / 2 - 1
    Z = BASE_Z - scale[2] / 2 - 3
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut4(scale=(10, 3.0, 3.0), Y=-BASE_Y + 15)

################################################

base.cut_cube(
    target=main,
    scale=(XX + BORN + 4, MAIN_HEIGHT + MAIN_THICKNESS, MAIN_DEPTH),
    location=(-14.0, 0, -5.7),
)

main.rotation_euler = (math.radians(180), 0, 0)

## main.location=(BASE_X, BASE_Y, 0)
