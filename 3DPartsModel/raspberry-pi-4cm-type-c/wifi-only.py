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

MAIN_WIDTH = 32.3
MAIN_HEIGHT = 32.3
MAIN_DEPTH = 3.5

MAIN_THICKNESS = 2.5

MAIN_BOTTOM = -MAIN_DEPTH / 2

wifi = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS,
        MAIN_HEIGHT + MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
)
base.cut_corners(
    target=wifi,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH - MAIN_THICKNESS / 2,
    thickness=MAIN_THICKNESS / 2,
)

base.cut_cube(
    target=wifi,
    scale=(
        MAIN_WIDTH - MAIN_THICKNESS / 2,
        MAIN_HEIGHT - MAIN_THICKNESS / 2,
        MAIN_DEPTH,
    ),
    location=(0.0, 0.0, MAIN_THICKNESS / 2),
)

base.cut_cube(
    target=wifi,
    scale=(
        20.0,
        MAIN_HEIGHT,
        MAIN_DEPTH,
    ),
    location=(0.0, MAIN_HEIGHT / 4, 0.0),
)

wifi.location = (0.0, 0.0, MAIN_DEPTH / 2)
