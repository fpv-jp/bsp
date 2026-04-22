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

MAIN_WIDTH = 20.2
MAIN_HEIGHT = 10.2
MAIN_DEPTH = 5.0

MAIN_THICKNESS = 1.25

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

## ------------------------

M = 1.75
ARM = 30.25

Y2 = MAIN_HEIGHT / 2 + M * 2 + 2.5

base.add_cube(
    target=main,
    scale=(ARM, M * 2, MAIN_DEPTH),
    location=(0.0, -Y2, 0.0),
)
base.add_cube(
    target=main,
    scale=(M * 2, M * 3, MAIN_DEPTH),
    location=(ARM / 4, -Y2 + M * 2, 0.0),
)
base.add_cube(
    target=main,
    scale=(M * 2, M * 3, MAIN_DEPTH),
    location=(-ARM / 4, -Y2 + M * 2, 0.0),
)
base.cut_cube(
    target=main,
    scale=(11.6, 8.0, MAIN_DEPTH),
    location=(0.0, -Y2, 0.0),
)

for i, (x) in enumerate([ARM / 2, -ARM / 2]):
    base.add_ring(
        target=main,
        outer_radius=M * 2,
        inner_radius=M,
        depth=MAIN_DEPTH,
        location=(x, -Y2, 0.0),
    )

## ------------------------

base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH, 5.7, MAIN_DEPTH),
)
base.cut_cube(
    target=main,
    scale=(24.2, 5.2, MAIN_DEPTH - MAIN_THICKNESS),
    location=(0.0, 0.0, -MAIN_THICKNESS / 2),
)
base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
    location=(0.0, 0.0, -MAIN_THICKNESS / 2),
)
base.cut_cylinder(
    target=main,
    radius=4.5,
    depth=MAIN_DEPTH,
)

main.rotation_euler = (math.pi, 0.0, 0.0)

# ------------------------

M = 0.75

base.cut_cylinder(
    target=main,
    radius=M,
    depth=MAIN_THICKNESS * 2,
    location=(M * 4, MAIN_HEIGHT / 2, MAIN_DEPTH / 2),
    rotation=(math.pi / 2, 0.0, 0.0),
)
base.cut_cylinder(
    target=main,
    radius=M,
    depth=MAIN_THICKNESS * 2,
    location=(M, MAIN_HEIGHT / 2, MAIN_DEPTH / 2),
    rotation=(math.pi / 2, 0.0, 0.0),
)
base.cut_cylinder(
    target=main,
    radius=M,
    depth=MAIN_THICKNESS * 2,
    location=(-M * 2, MAIN_HEIGHT / 2, MAIN_DEPTH / 2),
    rotation=(math.pi / 2, 0.0, 0.0),
)

# ------------------------
