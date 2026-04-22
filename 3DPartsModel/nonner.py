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

MAIN_WIDTH = 32.5
MAIN_HEIGHT = 14.6
MAIN_DEPTH = 2.5
MAIN_THICKNESS = 2.0

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


# ------------------------

M = 1.0
ARM = 17.9

for i, (x) in enumerate([ARM, -ARM]):
    base.add_ring(
        target=main,
        outer_radius=M * 2,
        inner_radius=M,
        depth=MAIN_DEPTH,
        location=(x, 0.0, 0.0),
    )

# ------------------------

base.cut_inner_corners(
    target=main,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH + MAIN_THICKNESS * 3,
    thickness=MAIN_THICKNESS / 2,
)

# ------------------------

main.location = (0 - 0, MAIN_HEIGHT / 2 + M * 2 + 4.0, 0.0)

M = 1.5
ARM = 30.25

for i, (x) in enumerate([ARM / 2, -ARM / 2]):
    base.add_cube(
        target=main,
        scale=(
            M * 2,
            M * 4,
            MAIN_DEPTH,
        ),
        location=(x, M * 2, 0.0),
    )
    base.add_ring(
        target=main,
        outer_radius=M * 2,
        inner_radius=M,
        depth=MAIN_DEPTH,
        location=(x, 0.0, 0.0),
    )
