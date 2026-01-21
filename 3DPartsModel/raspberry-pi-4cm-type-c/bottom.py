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
CM4_DEPTH = 7.4

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

X = CM4_WIDTH / 2 - CM4_THICKNESS * 1.66
Y = CM4_HEIGHT / 2 - CM4_THICKNESS * 1.66
base.cut_holes(
    target=main,
    radius=2.5,
    depth=CM4_DEPTH,
    z=CM4_THICKNESS / 2,
    positions=[(X, Y), (-X, Y), (X, -Y), (-X, -Y)],
)

base.cut_cube(
    target=main,
    scale=(CM4_WIDTH - 5, CM4_HEIGHT, CM4_DEPTH),
    location=(0, 0, CM4_THICKNESS / 2),
)
base.cut_cube(
    target=main,
    scale=(CM4_WIDTH, CM4_HEIGHT - 5, CM4_DEPTH),
    location=(0, 0, CM4_THICKNESS / 2),
)
base.cut_cube(
    target=main,
    scale=(CM4_WIDTH - 12, CM4_HEIGHT - 12, CM4_DEPTH + CM4_THICKNESS),
)

# ----------------------------------------------------------------------------------------------------------------

M = 2.3
X = (45.4 + M) / 2
Y = (30.5 + M) / 2
Z = 2.0
holes = [(X, Y), (X, -Y), (-X, Y), (-X, -Y)]
for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=2.5,
        inner_radius=M / 2,
        depth=CM4_THICKNESS + Z,
        location=(x, y, (Z - CM4_DEPTH) / 2),
    )

# ----------------------------------------------------------------------------------------------------------------

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
        depth=CM4_THICKNESS,
        location=(x, y, (-CM4_THICKNESS - CM4_DEPTH) / 2),
        rotation=(0, 0, math.radians(rotation)),
    )
