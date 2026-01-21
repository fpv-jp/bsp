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

MAIN_WIDTH = 19.0
MAIN_HEIGHT = 30.0
MAIN_DEPTH = 1.25

MAIN_THICKNESS = 2.5

MAIN_BOTTOM = -MAIN_DEPTH / 2

hub = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS,
        MAIN_HEIGHT + MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
)

R = 1.25
POSX = MAIN_WIDTH/2+R/2
POSY = -MAIN_HEIGHT/2 + R*2

base.cut_holes(
    target=hub,
    radius=1.25,
    depth=MAIN_DEPTH,
    positions=[
        (0.0, MAIN_HEIGHT/2),
        (POSX, POSY),
        (-POSX, POSY),
    ],
)

hub.location = (0.0, 0.0, MAIN_DEPTH / 2)
