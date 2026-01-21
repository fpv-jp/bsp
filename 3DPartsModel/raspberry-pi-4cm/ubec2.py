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
MAIN_HEIGHT = 21.3
MAIN_DEPTH = 8.0

MAIN_THICKNESS = 1.5

MAIN_BOTTOM = -MAIN_DEPTH / 2

main = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS,
        MAIN_HEIGHT + MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
)
base.cut_corners(
    target=main,
    width=MAIN_WIDTH,
    height=MAIN_HEIGHT,
    depth=MAIN_DEPTH - MAIN_THICKNESS / 2,
    thickness=MAIN_THICKNESS / 2,
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
base.cut_cube(
    target=main,
    scale=(
        MAIN_WIDTH,
        MAIN_HEIGHT - MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
    location=(MAIN_THICKNESS, 0, MAIN_THICKNESS),
)
H = 3.5
base.add_cube(
    target=main,
    scale=(
        MAIN_THICKNESS,
        MAIN_HEIGHT,
        H,
    ),
    location=(29.0 - MAIN_WIDTH / 2, 0, (H - MAIN_DEPTH) / 2),
)

## --- RPI_PWR --------------------------

RPI_PWR = 30.0
main.location = ((MAIN_HEIGHT - RPI_PWR) / 2, 0, 0)

M = 2.3

X = 20.4 + M
Y = MAIN_HEIGHT / 2 - (3.5 + M / 2)

base.cut_holes(
    target=main,
    radius=M / 2,
    depth=10,
    positions=[(X / 2, -Y), (-X / 2, -Y)],
)

## --- mount --------------------------

gap = 4.0
main.location = (MAIN_HEIGHT / 2 + gap, 0, 0)

X = 0.0
Y = 8.0
base.cut_holes(
    target=main,
    radius=1.75,
    depth=MAIN_DEPTH + MAIN_THICKNESS,
    positions=[(X, Y), (X, -Y)],
)

main.location = (MAIN_HEIGHT / 2 + gap, 0, -MAIN_THICKNESS)
base.cut_holes(
    target=main,
    radius=2.8,
    depth=MAIN_DEPTH,
    positions=[(X, Y), (X, -Y)],
)
