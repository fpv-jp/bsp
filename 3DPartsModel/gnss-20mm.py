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

MAIN_WIDTH = 20.2
MAIN_HEIGHT = 20.2
MAIN_DEPTH = 7.2

MAIN_THICKNESS = 1.25

MAIN_BOTTOM = -MAIN_DEPTH / 2

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

base.cut_inner_corners(
    target=main,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH,
    thickness=MAIN_THICKNESS,
)

###---------------------------------------

base.cut_cube(
    target=main,
    scale=(
        9.0,
        8.0,
        MAIN_DEPTH,
    ),
    location=(0, MAIN_HEIGHT / 2, 0),
)


base.cut_cube(
    target=main,
    scale=(
        18.0,
        18.0,
        MAIN_DEPTH,
    ),
    location=(0, MAIN_HEIGHT / 2, MAIN_THICKNESS),
)

main.location = (0, 0, (MAIN_DEPTH - MAIN_THICKNESS) / 2)

###---------------------------------------

M = 1.25
ARM = 14.0

positions = [
    (7.0, MAIN_HEIGHT / 2 + M / 2),
    (-7.0, MAIN_HEIGHT / 2 + M / 2),
]
for i, (x, y) in enumerate(positions):
    base.add_ring(
        target=main,
        outer_radius=M * 2,
        inner_radius=M,
        depth=MAIN_THICKNESS,
        location=(x, y, 0.0),
    )

positions = [
    (0.0, -MAIN_HEIGHT / 2 - M * 2),
]
for i, (x, y) in enumerate(positions):
    base.add_ring(
        target=main,
        outer_radius=M * 2,
        inner_radius=M,
        depth=MAIN_THICKNESS * 1.0,
        location=(x, y, 0.5),
    )
