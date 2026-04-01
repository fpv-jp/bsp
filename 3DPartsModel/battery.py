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

MAIN_WIDTH = 101.5
MAIN_HEIGHT = 29.0
MAIN_DEPTH = 12.0

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

# base.cut_cube(
#    target=main,
#    scale=(
#        MAIN_WIDTH,
#        MAIN_HEIGHT,
#        MAIN_DEPTH,
#    ),
#    location=(0, 0, MAIN_THICKNESS),
# )

R = 14.0
R2 = 5.0
L = 48.5
L2 = 50.0

T = L2 - L


def cut_battery(x, y):
    base.cut_cube(
        target=main,
        scale=(L, R, R),
        location=(x, y, R / 2),
    )
    base.cut_cube(
        target=main,
        scale=(L2, R2, R),
        location=(T / 2 + x, y, R / 2),
    )

    base.cut_cylinder(
        target=main,
        radius=R / 2,
        depth=L,
        location=(x, y, 0),
        rotation=(0, math.pi / 2, 0),
    )
    base.cut_cylinder(
        target=main,
        radius=R2 / 2,
        depth=L2,
        location=(T / 2 + x, y, 0),
        rotation=(0, math.pi / 2, 0),
    )


X = L + T * 3
cut_battery(X / 2, R / 2)
cut_battery(X / 2, -R / 2)
cut_battery(-X / 2, R / 2)
cut_battery(-X / 2, -R / 2)


def cut_battery2(y):
    base.cut_cylinder(
        target=main,
        radius=R2 / 2,
        depth=L,
        location=(-MAIN_WIDTH / 2, y, 0),
        rotation=(0, math.pi / 2, 0),
    )


cut_battery2(R / 2)
cut_battery2(-R / 2)


L3 = MAIN_WIDTH / 2 + 1.75

holes = [
    (L3, R / 2),
    (L3, -R / 2),
    (-L3, R / 2),
    (-L3, -R / 2),
]

for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=1.4,
        inner_radius=0.7,
        depth=MAIN_DEPTH / 4,
        location=(x, y, -MAIN_DEPTH / 2 + (MAIN_DEPTH / 8)),
    )

L4 = 1.75
holes = [
    (L4, R / 2),
    (L4, -R / 2),
    (-L4, R / 2),
    (-L4, -R / 2),
]

for i, (x, y) in enumerate(holes):
    base.cut_cylinder(
        target=main,
        radius=0.7,
        depth=MAIN_DEPTH / 3,
        location=(x, y, -MAIN_DEPTH / 2 + (MAIN_DEPTH / 6)),
    )
