import bpy
import bmesh
import math
import sys
import types

text = bpy.data.texts.get("base.py")
module_name = "base"
module = types.ModuleType(module_name)
exec(text.as_string(), module.__dict__)
sys.modules[module_name] = module

import base

# 初期化
base.init()

PLATE_WIDTH = 28
PLATE_HEIGHT = 12.5
PLATE_DEPTH = 1.5

M3 = 1.8
M7 = 3.75

main = base.create_cylinder(
    radius=M7 + PLATE_DEPTH,
    depth=PLATE_HEIGHT,
    rotation=(math.radians(90), 0, 0),
)
base.add_cube(
    target=main,
    scale=((M7 + PLATE_DEPTH) * 2, PLATE_HEIGHT, PLATE_DEPTH * 2),
    location=(0, 0, -PLATE_DEPTH),
)
base.cut_cylinder(
    target=main,
    radius=M7,
    depth=PLATE_HEIGHT + 1,
    rotation=(math.radians(90), 0, 0),
)
base.cut_cube(
    target=main,
    scale=(M7 + PLATE_DEPTH * 2.5, PLATE_HEIGHT, PLATE_DEPTH * 2),
    location=(0, 0, -PLATE_DEPTH),
)

main.location = (0, 0, PLATE_DEPTH)

base.cut_cube(
    target=main,
    scale=(PLATE_WIDTH, PLATE_HEIGHT + 10, PLATE_HEIGHT),
    location=(0, PLATE_HEIGHT / 2 - M3 * 2, -(PLATE_DEPTH + PLATE_HEIGHT) / 2),
)

main.location[1] = PLATE_HEIGHT / 2 - M3 * 2

base.add_cube(
    target=main,
    scale=(PLATE_WIDTH, M3 * 4, PLATE_DEPTH),
)
base.cut_cube(
    target=main,
    scale=(M7 + PLATE_DEPTH * 2.5, PLATE_HEIGHT, PLATE_DEPTH * 2),
    location=(0, 0, 0),
)

holes = [
    (-14, 0),
    (14, 0),
]

for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=M3 * 2,
        inner_radius=M3,
        depth=PLATE_DEPTH,
        location=(x, y, 0),
    )
