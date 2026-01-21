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

MAIN_WIDTH = 65.6
MAIN_HEIGHT = 37.0
MAIN_DEPTH = 18.3

MAIN_THICKNESS = 1.5

MAIN_BOTTOM = -MAIN_DEPTH / 2

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

base.cut_cube(
    target=main,
    scale=(
        MAIN_WIDTH,
        MAIN_HEIGHT,
        MAIN_DEPTH,
    ),
    location=(0, 0, MAIN_THICKNESS),
)


R = 2.5
X = MAIN_WIDTH / 2 - R * 2
Y = MAIN_HEIGHT / 2 - R * 2

base.cut_holes(
    target=main,
    radius=R,
    depth=MAIN_THICKNESS,
    z=MAIN_BOTTOM + MAIN_THICKNESS / 2,
    positions=[(X, Y), (-X, Y), (X, -Y), (-X, -Y)],
)
