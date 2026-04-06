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

# base.init()

MAIN_WIDTH = 37.0
MAIN_HEIGHT = 37.0
MAIN_DEPTH = 3.5

MAIN_THICKNESS = 2.5

MAIN_BOTTOM = -MAIN_DEPTH / 2

main = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS * 2,
        MAIN_HEIGHT + MAIN_THICKNESS * 2,
        MAIN_DEPTH,
    ),
)

base.add_cube(
    target=main,
    scale=(
        16.9,
        66.0,
        MAIN_THICKNESS,
    ),
    location=(0.0, 0.0, (MAIN_THICKNESS - MAIN_DEPTH) / 2),
)


base.cut_corners(
    target=main,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH - MAIN_THICKNESS,
    thickness=MAIN_THICKNESS,
)

base.cut_inner_corners(
    target=main,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH,
    thickness=MAIN_THICKNESS,
)


R = 1.75
X = 30.5 / 2
Y = 30.5 / 2

base.cut_holes(
    target=main,
    radius=R,
    depth=MAIN_THICKNESS,
    z=MAIN_BOTTOM + MAIN_THICKNESS / 2,
    positions=[(X, Y), (-X, Y), (X, -Y), (-X, -Y)],
)

X = 23.8 / 4
Y = 56 / 2

base.cut_holes(
    target=main,
    radius=R,
    depth=MAIN_THICKNESS,
    z=MAIN_BOTTOM + MAIN_THICKNESS / 2,
    positions=[(X, Y), (-X, Y), (X, -Y), (-X, -Y)],
)


main.location = (0.0, 0.0, (MAIN_DEPTH) / 2)

# -------------------------------- hub

R = 1.25
POSX = 19.0 / 2 + R / 2 - 2.6
POSY = 27.5 / 2

base.cut_holes(
    target=main,
    radius=1.25,
    depth=20.0,
    positions=[
        (0.0, POSY),
        (POSX, -POSY),
        (-POSX, -POSY),
    ],
)

# -------------------------------- wif

MAIN_WIDTH = 33.3
MAIN_HEIGHT = 33.3

MAIN_BOTTOM = -MAIN_DEPTH / 2

wifi = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS,
        MAIN_HEIGHT + MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
)

base.cut_cube(
    target=wifi,
    scale=(
        MAIN_WIDTH - MAIN_THICKNESS / 2,
        MAIN_HEIGHT - MAIN_THICKNESS / 2,
        MAIN_DEPTH,
    ),
    location=(0.0, 0.0, MAIN_THICKNESS / 2),
)

base.cut_cube(
    target=wifi,
    scale=(
        8.0,
        8.0,
        20.0,
    ),
    location=(-MAIN_WIDTH / 2, MAIN_HEIGHT / 2, 0.0),
)
base.cut_cube(
    target=wifi,
    scale=(
        8.0,
        8.0,
        20.0,
    ),
    location=(-MAIN_WIDTH / 2, -MAIN_HEIGHT / 2, 0.0),
)


wifi.location = (-37.0, 0.0, (MAIN_DEPTH) / 2)

base.modifier_apply(obj=wifi, target=main, operation="UNION")

base.cut_cube(
    target=main,
    scale=(
        MAIN_WIDTH - 4,
        20.0,
        20.0,
    ),
    location=(MAIN_WIDTH / 6 - 35.0, 0.0, 0.0),
)

# -------------------------------- ubec


MAIN_WIDTH = 39.7
MAIN_HEIGHT = 21.5
MAIN_DEPTH = 10.5

MAIN_THICKNESS = 2.5

MAIN_BOTTOM = -MAIN_DEPTH / 2

ubec = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS * 2,
        MAIN_HEIGHT + MAIN_THICKNESS * 2,
        MAIN_DEPTH,
    ),
)
base.cut_corners(
    target=ubec,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH - MAIN_THICKNESS,
    thickness=MAIN_THICKNESS,
)
base.cut_cube(
    target=ubec,
    scale=(
        MAIN_WIDTH,
        MAIN_HEIGHT,
        MAIN_DEPTH,
    ),
    location=(0.0, 0.0, MAIN_THICKNESS / 2),
)
base.cut_cube(
    target=ubec,
    scale=(
        MAIN_WIDTH,
        MAIN_HEIGHT - MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
    location=(MAIN_THICKNESS, 0.0, MAIN_THICKNESS),
)
H = 3.5
base.add_cube(
    target=ubec,
    scale=(
        MAIN_THICKNESS,
        MAIN_HEIGHT,
        H,
    ),
    location=(29.0 - MAIN_WIDTH / 2, 0, (H - MAIN_DEPTH) / 2),
)

base.cut_cube(
    target=ubec,
    scale=(
        10.0,
        3.0,
        8.0,
    ),
    location=(-MAIN_WIDTH / 2, MAIN_HEIGHT / 3, MAIN_DEPTH / 2),
)
base.cut_cube(
    target=ubec,
    scale=(
        10.0,
        3.0,
        8.0,
    ),
    location=(-MAIN_WIDTH / 2, -MAIN_HEIGHT / 3, MAIN_DEPTH / 2),
)

base.cut_cube(
    target=ubec,
    scale=(
        25.0,
        10.0,
        20.0,
    ),
)

ubec.rotation_euler = (0, 0, -math.pi / 2)
ubec.location = (31.75, 0.0, (MAIN_DEPTH) / 2)

base.modifier_apply(obj=ubec, target=main, operation="UNION")
