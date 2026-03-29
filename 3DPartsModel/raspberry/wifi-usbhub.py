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


M = 1.5
ARM = 32.3 + M * 6
MAIN_THICKNESS = 2.5


def bar():
    b = base.create_cube(
        scale=(
            ARM,
            M * 4,
            MAIN_THICKNESS,
        ),
    )
    for i, (x) in enumerate([ARM / 2, -ARM / 2]):
        base.add_ring(
            target=b,
            outer_radius=M * 2,
            inner_radius=M,
            depth=MAIN_THICKNESS,
            location=(x, 0.0, 0.0),
        )
    return b


#############################################################

MAIN_WIDTH = 32.3
MAIN_HEIGHT = 32.3
MAIN_DEPTH = 4.1

MAIN_BOTTOM = -MAIN_DEPTH / 2

wifi = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS,
        MAIN_HEIGHT + MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
)

# ------------------------

M = 1.75
ARM =  56.2 + M * 6
BAR_THICKNESS = 1.25

def bar():
    b = base.create_cube(
        scale=(
            ARM,
            M * 4,
            BAR_THICKNESS,
        ),
    )
    for i, (x) in enumerate([ARM / 2, -ARM / 2]):
        base.add_ring(
            target=b,
            outer_radius=M * 2,
            inner_radius=M,
            depth=BAR_THICKNESS,
            location=(x, 0.0, 0.0),
        )
    return b

b = bar()
b.location = (0.0, 0.0, (BAR_THICKNESS-MAIN_DEPTH)/2 )
base.modifier_apply(obj=b, target=wifi, operation="UNION")

# ------------------------

base.cut_cube(
    target=wifi,
    scale=(
        MAIN_WIDTH,
        MAIN_HEIGHT,
        MAIN_DEPTH,
    ),
    location=(0.0, 0.0, MAIN_THICKNESS / 2),
)

base.cut_cube(
    target=wifi,
    scale=(
        20.0,
        5.0,
        MAIN_DEPTH,
    ),
    location=(0.0, MAIN_HEIGHT / 2, 0.0),
)

# ------------------------

def ring():
    main = base.create_cylinder(
        radius=3.5,
        depth=MAIN_DEPTH,
    )
    base.cut_cylinder(
        target=main,
        radius=2.2,
        depth=MAIN_DEPTH,
    )
    return main

positions=[
    (-12.5, 0.0),
    (13.0, 8.75),
    (13.0, -8.75),
]

for i, (x, y) in enumerate(positions):
    base.cut_cylinder(target=wifi, radius=1.15, depth=MAIN_DEPTH, location=(x, y, 0.0))
    ring_ = ring()
    ring_.location = (x, y, 0.0)
    base.modifier_apply(obj=ring_, target=wifi, operation="UNION")

base.cut_cube(
    target=wifi,
    scale=(
        MAIN_WIDTH,
        MAIN_HEIGHT,
        MAIN_DEPTH,
    ),
    location=(0.0, 0.0, MAIN_THICKNESS / 2 + 1.4),
)
