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
MAIN_DEPTH = 5.2

MAIN_BOTTOM = -MAIN_DEPTH / 2

wifi = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS,
        MAIN_HEIGHT + MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
)

# ------------------------

GAP = -4.75

Z = (MAIN_THICKNESS - MAIN_DEPTH) / 2

b = bar()
b.location = (0.0, 15.5 + GAP, Z)
base.modifier_apply(obj=b, target=wifi, operation="UNION")

base.add_cube(
    target=wifi,
    scale=(
        M * 4,
        M * 4,
        MAIN_THICKNESS,
    ),
    location=(0.0, -16.5 + GAP + M * 2, Z),
)

base.add_ring(
    target=wifi,
    outer_radius=M * 2,
    inner_radius=M,
    depth=MAIN_THICKNESS,
    location=(0.0, -15.75 + GAP, Z),
)

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


def ring():
    main = base.create_cylinder(
        radius=5.0,
        depth=MAIN_DEPTH,
    )
    base.cut_cylinder(
        target=main,
        radius=3.0,
        depth=MAIN_DEPTH,
    )
    return main


X = 6.0
Y = 7.0

positions = [
    (X, Y),
    (-X, Y),
    (X, -Y),
    (-X, -Y),
]

for i, (x, y) in enumerate(positions):
    base.cut_cylinder(target=wifi, radius=1.5, depth=MAIN_DEPTH, location=(x, y, 0.0))
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
    location=(0.0, 0.0, MAIN_THICKNESS / 2 + 2.5),
)

############################################################


MAIN_WIDTH = 39.2
MAIN_HEIGHT = 21.5
MAIN_DEPTH = 8.0

MAIN_BOTTOM = -MAIN_DEPTH / 2

ubec = base.create_cube(
    scale=(
        MAIN_WIDTH + MAIN_THICKNESS,
        MAIN_HEIGHT + MAIN_THICKNESS,
        MAIN_DEPTH,
    ),
)

# ------------------------

b = bar()
b.location = (15.5, 0.0, (MAIN_THICKNESS - MAIN_DEPTH) / 2)
b.rotation_euler = (0, 0, math.pi / 2)
base.modifier_apply(obj=b, target=ubec, operation="UNION")

# ------------------------

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

base.cut_holes(
    target=ubec,
    radius=1.25,
    depth=MAIN_DEPTH,
    positions=[
        (-10.0, 0.0),
        (15.5, 8.75),
        (15.5, -8.75),
    ],
)

base.cut_holes(
    target=ubec,
    radius=1.5,
    depth=MAIN_DEPTH,
    positions=[
        (-15.75, 0.0),
    ],
)
