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
CM4_DEPTH = 1.25

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

# ----------------------------------------------------------------------------------------------------------------


M = 2.8

X = (45.4 + M) / 2
Y = (30.5 + M) / 2

holes = [(X, Y), (X, -Y), (-X, Y), (-X, -Y)]
for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=2.5,
        inner_radius=M / 2,
        depth=CM4_DEPTH + CM4_THICKNESS * 2,
        location=(x, y, CM4_THICKNESS / 2),
    )

# ----------------------------------------------------------------------------------------------------------------

main.location = (10.0, 0.0, 0.0)

X = 20.0 / 2
Y = 20.0 / 2
holes = [(X, Y), (X, -Y), (-X, Y), (-X, -Y)]
for i, (x, y) in enumerate(holes):
    base.cut_cylinder(
        target=main,
        radius=M / 2,
        depth=CM4_DEPTH + CM4_THICKNESS,
        location=(x, y, 0.0),
    )

base.cut_cylinder(
    target=main,
    radius=18.0 / 2,
    depth=CM4_DEPTH + CM4_THICKNESS,
)

# ----------------------------------------------------------------------------------------------------------------
Z = (CM4_DEPTH + CM4_THICKNESS) / 2
main.location = (33.85, 0.0, Z+CM4_THICKNESS/1.715)

CM4_WIDTH = 7.0
CM4_HEIGHT = 10.0
CM4_DEPTH = 12.0

CM4_THICKNESS = 1.75

Z = (CM4_DEPTH + CM4_THICKNESS) / 2

base.add_cube(
    target=main,
    scale=(CM4_WIDTH + CM4_THICKNESS * 2, CM4_HEIGHT, CM4_DEPTH),
    location=(0, 0, Z),
)

base.cut_cube(
    target=main,
    scale=(CM4_WIDTH, CM4_HEIGHT, CM4_DEPTH),
    location=(0, 0, Z + CM4_THICKNESS),
)
