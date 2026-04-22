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

MAIN_WIDTH = 22.8
MAIN_HEIGHT = 11.7
MAIN_DEPTH = 3.0

MAIN_THICKNESS = 3.0

main = base.create_cube(
    scale=(MAIN_WIDTH + MAIN_THICKNESS * 2, MAIN_HEIGHT + MAIN_THICKNESS * 2, MAIN_DEPTH),
)

M2 = 1.25
X = 12.5 + M2

for i, (x) in enumerate([X, -X]):
    base.add_ring(
        target=main,
        outer_radius=M2 * 2,
        inner_radius=M2,
        depth=MAIN_DEPTH,
        location=[x, 0.0, 0.0],
    )

base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH * 2),
)

M3 = 1.5
X = 18.85

main.location = (MAIN_WIDTH / 2 - 11.5 / 2, (MAIN_HEIGHT) / 2 + M3 * 3, 0.0)

base.add_cube(
    target=main,
    scale=(X * 2, M3 * 4, MAIN_DEPTH),
)
for i, (x) in enumerate([X, -X]):
    base.add_ring(
        target=main,
        outer_radius=M3 * 2.5,
        inner_radius=M3,
        depth=MAIN_DEPTH,
        location=[x, 0.0, 0.0],
    )
