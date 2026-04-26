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

MAIN_WIDTH = 34.0
MAIN_HEIGHT = 34.0
MAIN_DEPTH = 3.5

MAIN_THICKNESS = 2.5

main = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS * 2,
        MAIN_HEIGHT + MAIN_THICKNESS * 2,
        MAIN_DEPTH,
    ),
)

base.cut_corners(
    target=main,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH - MAIN_THICKNESS,
    thickness=MAIN_THICKNESS,
)

R = 1.75
X = 30.5 / 2
Y = 30.5 / 2

base.cut_holes(
    target=main,
    radius=R,
    depth=10.0,
    positions=[(X, Y), (-X, Y), (X, -Y), (-X, -Y)],
)

## -------------------------------- 
main2 = base.create_cube(
    scale=(
        22.0,
        60.0,
        MAIN_DEPTH,
    ),
    location=(0.0, -5.0, 0.0),
)
base.cut_cube(
    target=main2,
    scale=(
        8.0,
        60.0,
        MAIN_DEPTH,
    ),
    location=(0.0, -5.0, 0.0),
)
base.modifier_apply(obj=main2, target=main, operation="UNION")

## -------------------------------- 

base.cut_cube(
    target=main,
    scale=(
        3.0,
        16.0,
        MAIN_DEPTH*2,
    ),
    location=(MAIN_WIDTH/3, MAIN_HEIGHT/3, 0.0),
    rotation = (0.0, 0.0, math.pi/4),
)

## -------------------------------- 

M = 1.5
ARM = 36.4
base.add_cube(
    target=main,
    scale=(
        ARM,
        M * 4,
        MAIN_DEPTH,
    ),
    location=(0.0, -32.0, 0.0),
)
for i, (x) in enumerate([ARM / 2, -ARM / 2]):
    base.add_ring(
        target=main,
        outer_radius=M * 2,
        inner_radius=M,
        depth=MAIN_DEPTH,
        location=(x, -32.0, 0.0),
    )

# -------------------------------- wif

MAIN_WIDTH = 33.3
MAIN_HEIGHT = 33.3

base.cut_cube(
    target=main,
    scale=(
        MAIN_WIDTH - MAIN_THICKNESS / 2,
        MAIN_HEIGHT - MAIN_THICKNESS / 2,
        MAIN_DEPTH,
    ),
    location=(0.0, 0.0, 2.0),
    rotation = (0.0, 0.0, math.pi/4)
)

base.cut_cylinder(
    target=main,
    radius=13.4,
    depth=10.0,
)


main.location = (0.0, 0.0, (MAIN_DEPTH) / 2)

## -------------------------------- ubec

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

ubec.location = (0.0, 36.0, (MAIN_DEPTH) / 2)
base.modifier_apply(obj=ubec, target=main, operation="UNION")
