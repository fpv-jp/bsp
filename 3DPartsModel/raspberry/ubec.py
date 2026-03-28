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

MAIN_WIDTH = 39.2
MAIN_HEIGHT = 21.5
MAIN_DEPTH = 8.0

MAIN_THICKNESS = 2.5

MAIN_BOTTOM = -MAIN_DEPTH / 2

ubec = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS,
        MAIN_HEIGHT + MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
)

base.cut_corners(
    target=ubec,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH - MAIN_THICKNESS / 2,
    thickness=MAIN_THICKNESS / 2,
)
base.cut_cube(
    target=ubec,
    scale=(
        MAIN_WIDTH,
        MAIN_HEIGHT,
        MAIN_DEPTH,
    ),
    location=(0.0, 0.0, MAIN_THICKNESS / 2),
)
base.cut_cube(
    target=ubec,
    scale=(
        MAIN_WIDTH,
        MAIN_HEIGHT - MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
    location=(MAIN_THICKNESS, 0.0, MAIN_THICKNESS),
)

H = 3.5
base.add_cube(
    target=ubec,
    scale=(
        MAIN_THICKNESS,
        MAIN_HEIGHT,
        H,
    ),
    location=(29.0 - MAIN_WIDTH / 2, 0, (H - MAIN_DEPTH) / 2),
)

ubec.location = (0.0, 0.0, MAIN_DEPTH / 2)
# ------------------------


M = 2.5
BAR_THICKNESS = 1.25

base.add_cube(
    target=ubec,
    scale=(
        49.7+M * 2,
        M * 4,
        BAR_THICKNESS,
    ),
    location=(0.0, 3.75, BAR_THICKNESS/2),
)
for i, (x) in enumerate([49.7/2+M, -49.7/2-M]):
    base.add_ring(
        target=ubec,
        outer_radius=M * 2,
        inner_radius=M,
        depth=BAR_THICKNESS,
        location=(x, 3.75, BAR_THICKNESS/2),
    )
# --------------------

X = 14.5
Y = 6.0

base.cut_cylinder(
    target=ubec,
    radius=1.5,
    depth=MAIN_DEPTH,
    location = (X, Y, 0.0)
)

base.cut_cylinder(
    target=ubec,
    radius=1.5,
    depth=MAIN_DEPTH,
    location = (X, -Y, 0.0)
)

