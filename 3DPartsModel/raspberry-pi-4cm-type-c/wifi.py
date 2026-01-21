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

CM4_WIDTH = 55.4
CM4_HEIGHT = 40.3
CM4_DEPTH = 2.0

CM4_THICKNESS = 1.5

FULL = CM4_DEPTH + CM4_THICKNESS

main = base.create_cube(
    scale=(
        CM4_WIDTH + CM4_THICKNESS * 2,
        CM4_HEIGHT + CM4_THICKNESS * 2,
        FULL,
    ),
)
base.cut_corners(
    target=main,
    width=CM4_WIDTH,
    height=CM4_HEIGHT,
    depth=CM4_DEPTH,
    thickness=CM4_THICKNESS,
)
base.add_cube(
    target=main,
    scale=(
        CM4_WIDTH + CM4_THICKNESS * 2,
        3.0,
        FULL,
    ),
    location=(0, CM4_HEIGHT / 2, 0),
)

base.cut_cube(
    target=main,
    scale=(CM4_WIDTH - 12, CM4_HEIGHT - 12, CM4_DEPTH + CM4_THICKNESS),
)

x1 = 22.25
y1 = 15.0

t = [(3.5, 0, 0), (0, 3.5, 0), (0, 0, 0)]
triangle_positions = [
    (-x1, y1, t, 270),
    (x1, y1, t, 180),
    (x1, -y1, t, 90),
    (-x1, -y1, t, 0),
]

for i, (x, y, verts, rotation) in enumerate(triangle_positions):
    base.add_triangle(
        target=main,
        verts=verts,
        depth=FULL,
        location=(x, y, (-CM4_THICKNESS - CM4_DEPTH) / 2),
        rotation=(0, 0, math.radians(rotation)),
    )


### ----------------------------------------------------------------------------------------------------------------

M = 2.3
X = (45.4 + M) / 2
Y = (30.5 + M) / 2

base.cut_holes(
    target=main,
    radius=1.4,
    depth=FULL,
    positions=[(X, Y), (X, -Y), (-X, Y), (-X, -Y)],
)

### ----------------------------------------------------------------------------------------------------------------

X = 32.3
Y = 32.3


Z = 1.1
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(0, 0, (-Z + FULL) / 2),
)

Z = FULL - Z
base.cut_cube(
    target=main,
    scale=(18.5, Y / 2, Z + 3),
    location=(0, Y / 4 + CM4_THICKNESS, (Z - FULL) / 2),
)

base.cut_cube(
    target=main,
    scale=(24.0, 24.0, Z + 3),
)


### ----------------------------------------------------------------------------------------------------------------


def Wire(POS):
    base.cut_cube(
        target=main,
        scale=(1.7, Y / 2, Z),
        location=(POS, Y / 2, (Z - FULL) / 2),
    )


X = 0.75
Wire(8.4 - X)
Wire(6.0 - X)
Wire(3.6 - X)

Wire(-8.4)
Wire(-6.0)

### ----------------------------------------------------------------------------------------------------------------

OUTER = 7.0
INNER = 5.1
DEPTH = 11.5
DEPTH2 = 2.0
DEPTH3 = 6.0


def create_antenna():
    antenna = base.create_cube(scale=(OUTER * 2, OUTER, DEPTH), location=(0, OUTER / 2, 0))
    base.add_ring(target=antenna, outer_radius=OUTER, inner_radius=INNER, depth=DEPTH)
    base.add_ring(
        target=antenna,
        outer_radius=OUTER,
        inner_radius=3.25,
        depth=DEPTH2,
        location=(0, 0, (DEPTH - DEPTH2) / 2),
    )
    base.cut_cube(
        target=antenna,
        scale=(OUTER * 2, OUTER * 2, DEPTH3),
        location=(0, -FULL, 0),
    )
    return antenna


X = 26.2
Y = CM4_HEIGHT / 2 + OUTER + CM4_THICKNESS
Z = OUTER - FULL / 2

ROT = math.pi / 2

right = create_antenna()
right.location = (-X, Y, Z)
right.rotation_euler[0] = -ROT
right.rotation_euler[2] = -ROT

left = create_antenna()
left.location = (X, Y, Z)
left.rotation_euler[0] = -ROT
left.rotation_euler[2] = ROT

base.modifier_apply(obj=right, target=main, operation="UNION")
base.modifier_apply(obj=left, target=main, operation="UNION")

### ----------------------------------------------------------------------------------------------------------------

T = 10.0
base.add_cube(
    target=main,
    scale=(24.5, T, CM4_DEPTH + CM4_THICKNESS),
    location=(0, -(CM4_HEIGHT + T) / 2, 0),
)

X = 8.0
Y = -26.0
base.cut_holes(
    target=main,
    radius=1.75,
    depth=CM4_DEPTH + CM4_THICKNESS,
    positions=[(X, Y), (-X, Y)],
)
