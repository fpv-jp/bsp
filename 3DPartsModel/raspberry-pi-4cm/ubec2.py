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

PLATE_THICKNESS = 1.5

RPI_PWR = 30.0
USB_FEM = 17.0

PLATE_WIDTH = RPI_PWR + USB_FEM
PLATE_HEIGHT = 26.0

main = base.create_cube(
    scale=(PLATE_WIDTH, PLATE_HEIGHT, PLATE_THICKNESS),
)

# --- RPI_PWR --------------------------
main.location = ((PLATE_WIDTH - RPI_PWR) / 2, 0, 0)

M = 2.3

X = 20.4 + M
Y = PLATE_HEIGHT / 2 - (3.5 + M / 2)

base.cut_holes(
    target=main,
    radius=M / 2,
    depth=10,
    positions=[(X / 2, Y), (-X / 2, Y)],
)


# --- mount --------------------------

PITCH = 30.5
P = PITCH / 2

M = 2.8

holes = [
    (P, P),
    (-P, P),
    (P, -P),
    (-P, -P),
]

scale = (PITCH, M * 2, PLATE_THICKNESS)
base.add_cube(target=main, scale=scale, location=(0, P, 0))
base.add_cube(target=main, scale=scale, location=(0, -P, 0))
for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=M,
        inner_radius=M / 2,
        depth=PLATE_THICKNESS,
        location=(x, y, 0),
    )


# --- USB_FEM --------------------------

main.location = (-(PLATE_WIDTH - USB_FEM) / 2, 0, 0)

M = 2.6

X = 9.2 + M
Y = PLATE_HEIGHT / 2 - 13.0

base.cut_holes(
    target=main,
    radius=M / 2,
    depth=10,
    positions=[
        (X / 2, Y),
        (-X / 2, Y),
        (X / 2 + 0.75, Y + 6.0),
        (-X / 2 - 0.75, Y + 6.0),
    ],
)

scale = (10.0, 2.0, 10)

base.cut_cube(target=main, scale=scale, location=(0, Y + 3.3, 0))
base.cut_cube(target=main, scale=scale, location=(0, Y - 3.3, 0))

# --- ubec --------------------
main.location = (0, 0, 0)

PLATE_HEIGHT = 21.7
PLATE_DEPTH = 7.8

main2 = base.create_cube(
    scale=(
        PLATE_WIDTH + PLATE_THICKNESS,
        PLATE_HEIGHT + PLATE_THICKNESS * 2,
        PLATE_DEPTH,
    ),
)

base.cut_cube(
    target=main2,
    scale=(
        PLATE_WIDTH,
        PLATE_HEIGHT,
        PLATE_DEPTH,
    ),
    location=(-PLATE_THICKNESS / 2, 0, 0),
)

main2.location = ((PLATE_WIDTH - RPI_PWR) / 2, 0, 0)

base.add_cube(
    target=main2,
    scale=(PLATE_THICKNESS, PLATE_HEIGHT, 3.2),
    location=(0, 0, (PLATE_DEPTH - 3.2) / 2 - PLATE_THICKNESS),
)

X = 20.4

base.cut_cube(
    target=main2,
    scale=(5, 5, PLATE_DEPTH),
    location=(X / 2, PLATE_HEIGHT / 2, 0),
)
base.cut_cube(
    target=main2,
    scale=(5, 5, PLATE_DEPTH),
    location=(-X / 2, PLATE_HEIGHT / 2, 0),
)

main2.location = (PLATE_THICKNESS / 2, 0, (PLATE_THICKNESS - PLATE_DEPTH) / 2)

base.modifier_apply(obj=main2, target=main, name="main2_union", operation="UNION")

main.rotation_euler = (math.pi, 0, 0)
