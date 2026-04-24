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

MAIN_WIDTH = 33.1 / 6
MAIN_HEIGHT = 33.1
MAIN_DEPTH = 1.5

MAIN_THICKNESS = 1.75

R = 1.25

# --------------------------------

main = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS * 2,
        MAIN_HEIGHT + MAIN_THICKNESS * 2,
        MAIN_THICKNESS,
    ),
)

base.add_ring(
    target=main,
    outer_radius=R * 2,
    inner_radius=R,
    depth=MAIN_DEPTH,
    location=(MAIN_WIDTH / 2 + R * 2, 0.0, 0.0),
)
