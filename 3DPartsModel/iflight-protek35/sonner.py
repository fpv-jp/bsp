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

M = 1.5

MAIN_WIDTH = 35.8
MAIN_HEIGHT = M * 5
MAIN_DEPTH = 1.5

main = base.create_cube(
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
    location=(0.0, 0.0, 0.0),
)

# ------------------------

ARM = 35.8
for i, (x) in enumerate([ARM / 2, -ARM / 2]):
    base.add_ring(
        target=main,
        outer_radius=M * 2.5,
        inner_radius=M,
        depth=3.5,
        location=(x, 0.0, 3.5 / 2 - MAIN_DEPTH / 2),
    )
    base.cut_cylinder(
        target=main,
        radius=2.5,
        depth=3.5,
        location=(x, 0.0, 3.5 / 2 + MAIN_DEPTH / 2),
    )

# ------------------------

ARM = 15.8 / 2
M = 1.25

for i, (x) in enumerate([ARM, -ARM]):
    base.add_ring(
        target=main,
        outer_radius=M * 2.5,
        inner_radius=M,
        depth=3.5,
        location=(x, 0.0, 3.5 / 2 - MAIN_DEPTH / 2),
    )
