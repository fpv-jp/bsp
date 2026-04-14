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

MAIN_WIDTH = 19.3
MAIN_HEIGHT = 19.3
MAIN_DEPTH = 5.2

MAIN_THICKNESS = 1.25

MAIN_BOTTOM = -MAIN_DEPTH / 2

PITCH = 6.225

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

base.add_cube(
    target=main,
    scale=(MAIN_WIDTH, MAIN_DEPTH, MAIN_DEPTH),
    location=(MAIN_THICKNESS, 0.0, PITCH - MAIN_DEPTH / 2),
)

base.add_ring(
    target=main,
    outer_radius=MAIN_DEPTH / 2,
    inner_radius=0.7,
    location=(MAIN_THICKNESS, 0, PITCH),
    depth=MAIN_WIDTH,
    rotation=(0, math.pi / 2, 0),
)

for i, (y) in enumerate([PITCH, -PITCH]):
    base.cut_cylinder(
        target=main,
        radius=0.7,
        depth=MAIN_WIDTH,
        location=(MAIN_THICKNESS, y, 0.0),
        rotation=(0, math.pi / 2, 0),
    )


base.add_cylinder(
    target=main,
    radius=1.75,
    depth=MAIN_WIDTH,
    location=(-5.0, 0.0, 0.0),
    rotation=(0, math.pi / 2, 0),
)
base.cut_cylinder(
    target=main,
    radius=1.1,
    depth=MAIN_WIDTH * 2,
    rotation=(0, math.pi / 2, 0),
)

####################################################

base.cut_inner_corners(
    target=main,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH * 3,
    thickness=MAIN_THICKNESS,
)
