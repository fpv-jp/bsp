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
