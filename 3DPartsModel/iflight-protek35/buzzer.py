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

MAIN_WIDTH = 19.9
MAIN_HEIGHT = 9.8
MAIN_DEPTH = 4.8

MAIN_THICKNESS = 2.0

main = base.create_cube(
    scale=(MAIN_WIDTH + MAIN_THICKNESS, MAIN_HEIGHT + MAIN_THICKNESS, MAIN_DEPTH),
)
base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
    location=(0.0, 0.0, MAIN_THICKNESS / 2),
)

# ------------------------

ARM = 15.8 / 2
M = 1.25

for i, (x) in enumerate([ARM, -ARM]):
    base.add_ring(
        target=main,
        outer_radius=M * 2.25,
        inner_radius=M,
        depth=MAIN_DEPTH,
        location=(x, 0.0, 0.0),
    )

base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
    location=(0.0, 0.0, 2.25),
)

base.cut_cube(
    target=main,
    scale=(24.2, 5.2, MAIN_DEPTH),
    location=(0.0, 0.0, 3.25),
)

base.cut_cube(
    target=main,
    scale=(6.0, 3.0, MAIN_DEPTH),
    location=(-1.0, MAIN_HEIGHT/2, MAIN_THICKNESS),
)


for i, (x) in enumerate([ARM, -ARM]):
    base.cut_cylinder(
        target=main,
        radius=2.0,
        depth=MAIN_DEPTH,
        location=(x, 0.0, MAIN_THICKNESS / 2),
    )
