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

MAIN_WIDTH = 42.0
MAIN_HEIGHT = 12.0
MAIN_DEPTH = 2.0

main = base.create_cube(
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
)

# ------------------------

M = 1.5
ARM = 36.4
for i, (x) in enumerate([ARM / 2, -ARM / 2]):
    base.add_ring(
        target=main,
        outer_radius=M * 2,
        inner_radius=M,
        depth=MAIN_DEPTH,
        location=(x, 5.0, 0.0),
    )

M = 1.75
ARM = 42.0

for i, (x) in enumerate([ARM / 2, -ARM / 2]):
    base.add_ring(
        target=main,
        outer_radius=M * 2,
        inner_radius=M,
        depth=MAIN_DEPTH,
        location=(x, -5.0, 0.0),
    )
