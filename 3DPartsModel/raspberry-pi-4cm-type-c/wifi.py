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

main = base.create_cube(
    scale=(
        CM4_WIDTH + CM4_THICKNESS * 2,
        CM4_HEIGHT + CM4_THICKNESS * 2,
        CM4_DEPTH + CM4_THICKNESS,
    ),
)

base.cut_corners(
    target=main,
    width=CM4_WIDTH,
    height=CM4_HEIGHT,
    depth=CM4_DEPTH,
    thickness=CM4_THICKNESS,
)

## ----------------------------------------------------------------------------------------------------------------

M = 2.3
X = (45.4 + M) / 2
Y = (30.5 + M) / 2

base.cut_holes(
    target=main,
    radius=1.25,
    depth=CM4_DEPTH + CM4_THICKNESS,
    positions=[(X, Y), (X, -Y), (-X, Y), (-X, -Y)],
)

## ----------------------------------------------------------------------------------------------------------------

base.cut_cube(
    target=main,
    scale=(CM4_WIDTH - 12, CM4_HEIGHT - 12, CM4_DEPTH + CM4_THICKNESS),
)

## ----------------------------------------------------------------------------------------------------------------

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
        depth=CM4_DEPTH + CM4_THICKNESS,
        location=(x, y, (-CM4_THICKNESS - CM4_DEPTH) / 2),
        rotation=(0, 0, math.radians(rotation)),
    )


## ----------------------------------------------------------------------------------------------------------------

X = 32.3
Y = 32.3

base.add_cube(
    target=main,
    scale=(CM4_THICKNESS * 2, CM4_HEIGHT, CM4_DEPTH + CM4_THICKNESS),
    location=(X / 2, 0, 0),
)
base.add_cube(
    target=main,
    scale=(CM4_THICKNESS * 2, CM4_HEIGHT, CM4_DEPTH + CM4_THICKNESS),
    location=(-X / 2, 0, 0),
)

FULL = CM4_DEPTH + CM4_THICKNESS

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


def Xxxx(XX):
    base.cut_cube(
        target=main,
        scale=(1.7, Y / 2, Z),
        location=(XX, Y / 2, (Z - FULL) / 2),
    )


X = 0.75
Xxxx(8.4 - X)
Xxxx(6.0 - X)
Xxxx(3.6 - X)

Xxxx(-8.4)
Xxxx(-6.0)

## ----------------------------------------------------------------------------------------------------------------

X = CM4_WIDTH + CM4_THICKNESS * 2
Z = CM4_DEPTH + CM4_THICKNESS


right = base.create_cube(
    scale=(14.0, 7.0, 20.0),
    location=(0, 3.5, 0),
)

base.cut_cylinder(
    target=right,
    radius=5.1,
    depth=20.0,
    location=(0, 0, 1.5),
)

base.add_ring(
    target=right,
    outer_radius=7.0,
    inner_radius=5.1,
    depth=7.0,
    location=(0, 0, (20.0 - 7.0) / 2),
)

base.add_ring(
    target=right,
    outer_radius=7.0,
    inner_radius=3.25,
    depth=1.5,
    location=(0, 0, (-20.0 + 1.5) / 2),
)


## ----------------------------------------------------------------------------------------------------------------

left = base.create_cube(
    scale=(14.0, 7.0, 20.0),
    location=(0, 3.5, 0),
)

base.cut_cylinder(
    target=left,
    radius=5.1,
    depth=20.0,
    location=(0, 0, 1.5),
)

base.add_ring(
    target=left,
    outer_radius=7.0,
    inner_radius=5.1,
    depth=7.0,
    location=(0, 0, (20.0 - 7.0) / 2),
)

base.add_ring(
    target=left,
    outer_radius=7.0,
    inner_radius=3.25,
    depth=1.5,
    location=(0, 0, (-20.0 + 1.5) / 2),
)

## ----------------------------------------------------------------------------------------------------------------

right.location = (-(X / 2 + 7.0), 7.0, 5.25)
right.rotation_euler[0] = -math.pi / 2

left.location = (X / 2 + 7.0, 7.0, 5.25)
left.rotation_euler[0] = -math.pi / 2

base.modifier_apply(obj=right, target=main, operation="UNION")
base.modifier_apply(obj=left, target=main, operation="UNION")


main.location = (X / 2, 0, 0)
