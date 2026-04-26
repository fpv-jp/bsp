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

# ----------------------------------------------------------------------------------------------------------------

M = 3.5
ARM = 57.0
POS = -4.0

base.add_cube(
    target=main,
    scale=(
        M * 3,
        ARM,
        FULL,
    ),
    location=(POS, 0.0, 0.0),
)

for i, (y) in enumerate([ARM / 2, -ARM / 2]):
    base.add_ring(
        target=main,
        outer_radius=M * 1.5,
        inner_radius=M,
        depth=FULL,
        location=(POS, y, 0.0),
    )

# ----------------------------------------------------------------------------------------------------------------

M = 2.3
X = (45.4 + M) / 2
Y = (30.5 + M) / 2

M = 1.4
H = 8.0
for i, (x, y) in enumerate(
    [(X, Y), (X, -Y), (-X, Y), (-X, -Y)],
):
    base.add_ring(
        target=main,
        outer_radius=M * 2.5,
        inner_radius=M,
        depth=H,
        location=(x, y, H / 2 - FULL / 2),
    )

# ----------------------------------------------------------------------------------------------------------------

X = 13.0
Y = -8.0
base.cut_holes(
    target=main,
    radius=1.75,
    depth=FULL,
    positions=[(X, Y), (X, -Y)],
)

# ----------------------------------------------------------------------------------------------------------------

R = 1.25
POSX = 26.0 / 2
POSY = 17.0 / 2

P = -6.0
base.cut_holes(
    target=main,
    radius=1.25,
    depth=20.0,
    positions=[
        (POSX + P, 0.0),
        (-POSX + P, POSY),
        (-POSX + P, -POSY),
    ],
)

# ----------------------------------------------------------------------------------------------------------------

X = 6.0
Y = CM4_HEIGHT / 2 - 1.25

for i, (x, y) in enumerate(
    [(X, Y), (X, -Y), (-X, Y), (-X, -Y)],
):
    base.cut_cylinder(
        target=main,
        radius=1.75,
        depth=FULL,
        location=(x + 12.0, y, 0.0),
    )
# ----------------------------------------------------------------------------------------------------------------

CM4_WIDTH2 = 22.0
CM4_HEIGHT2 = CM4_HEIGHT - 12

base.cut_cube(
    target=main,
    scale=(CM4_WIDTH2, CM4_HEIGHT2, FULL * 2),
    location=(-CM4_WIDTH2 / 2 + 5.25, 0.0, 0.0),
)

# ----------------------------------------------------------------------------------------------------------------
