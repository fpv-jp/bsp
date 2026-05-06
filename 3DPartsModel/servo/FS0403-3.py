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


MAIN_WIDTH = 37.2
MAIN_HEIGHT = (11.8 + 1.8) * 2
MAIN_DEPTH = 3.0

MAIN_THICKNESS = 3.0

# -------------------------------------
main = base.create_cube(
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
)

SIDE = (MAIN_WIDTH - MAIN_THICKNESS) / 2

H = 20.0

y = 6.0

base.add_cube(
    target=main,
    scale=(MAIN_THICKNESS, 8.8, H),
    location=(SIDE, y, H / 2),
)

base.add_ring(
    target=main,
    outer_radius=4.4,
    inner_radius=2.2,
    depth=MAIN_THICKNESS,
    location=(SIDE, y, H),
    rotation=(0, math.pi / 2, 0),
)

X2 = 4.75
base.cut_cylinder(
    target=main,
    radius=1.5,
    depth=3.0,
    location=(X2, y, 0.0),
)

P2 = 2.0

holes = [
    (X2 + 5.6),
    (X2 - 5.6),
    (X2 - 15.6),
]

for i, (y2) in enumerate(holes):
    base.cut_cylinder(
        target=main,
        radius=0.9,
        depth=3.0,
        location=(y2, y, 0.0),
    )


##############################################################

P = 11.8

for i, (y) in enumerate([P, -P]):
    base.add_cube(
        target=main,
        scale=(MAIN_THICKNESS, 3.6, H),
        location=(-SIDE, y, H / 2),
    )

    base.add_ring(
        target=main,
        outer_radius=1.8,
        inner_radius=0.7,
        location=(-SIDE, y, H),
        depth=MAIN_THICKNESS,
        rotation=(0, math.pi / 2, 0),
    )


##############################################################

base.cut_cube(
    target=main,
    scale=(15.0, MAIN_HEIGHT, MAIN_DEPTH),
    location=(X2, -11, 0),
)

base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH * 2, MAIN_HEIGHT, MAIN_DEPTH),
    location=(0, -21.5, 0),
    rotation=(0, 0, math.pi / 7.5),
)

base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH * 2, MAIN_HEIGHT, MAIN_DEPTH),
    location=(0, 25.8, 0),
    rotation=(0, 0, -math.pi / 34),
)
