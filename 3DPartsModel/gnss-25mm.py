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

MAIN_WIDTH = 25.2
MAIN_HEIGHT = 25.2
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
        9.0,
        MAIN_DEPTH,
    ),
    location=(0, MAIN_HEIGHT / 2, MAIN_THICKNESS),
)

M = 1.5
ARM = 29.0


def bar():
    b = base.create_cube(
        scale=(
            ARM,
            M * 4,
            MAIN_THICKNESS,
        ),
    )
    for i, (x) in enumerate([ARM / 2, -ARM / 2]):
        base.add_ring(
            target=b,
            outer_radius=M * 2,
            inner_radius=M,
            depth=MAIN_THICKNESS,
            location=(x, 0.0, 0.0),
        )
    return b


b = bar()
b.location = (0.0, -MAIN_HEIGHT / 2 - M * 2, (MAIN_THICKNESS - MAIN_DEPTH) / 2)
base.modifier_apply(obj=b, target=main, operation="UNION")
