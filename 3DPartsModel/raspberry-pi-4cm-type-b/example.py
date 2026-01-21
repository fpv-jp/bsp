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

CM4_WIDTH = 56.2
CM4_HEIGHT = 41.1

CM4_DEPTH_TOP = 5.4
CM4_DEPTH_BOTTOM = 7.3
CM4_DEPTH = CM4_DEPTH_TOP + CM4_DEPTH_BOTTOM

CM4_THICKNESS = 1.5

X_ALL = CM4_WIDTH + CM4_THICKNESS * 2
Y_ALL = CM4_HEIGHT + CM4_THICKNESS * 2
Z_ALL = CM4_DEPTH + CM4_THICKNESS * 2

main = base.create_cube(scale=(X_ALL, Y_ALL, Z_ALL))

M = 1.25
holes = [(X_ALL/2, Y_ALL/4), (-X_ALL/2, -Y_ALL/4)]
for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=M + CM4_THICKNESS,
        inner_radius=M,
        depth=Z_ALL,
        location=(x, y, 0),
    )

TRIM_SCALE = (M + CM4_THICKNESS, CM4_HEIGHT, CM4_DEPTH)
TRIM_LOCATION = (X_ALL + M + CM4_THICKNESS)/2
base.cut_cube(target=main, scale=TRIM_SCALE, location=(TRIM_LOCATION, 0, 0))
base.cut_cube(target=main, scale=TRIM_SCALE, location=(-TRIM_LOCATION, 0, 0))

base.cut_corners(
    target=main,
    width=CM4_WIDTH,
    height=CM4_HEIGHT,
    depth=CM4_DEPTH + CM4_THICKNESS,
    thickness=CM4_THICKNESS,
)

X = CM4_WIDTH / 2 - CM4_THICKNESS * 1.66
Y = CM4_HEIGHT / 2 - CM4_THICKNESS * 1.66
positions = [(X, Y), (-X, Y), (X, -Y), (-X, -Y)]

base.cut_holes(target=main, radius=2.5, depth=CM4_DEPTH, positions=positions)
base.cut_cube(target=main, scale=(CM4_WIDTH - 5, CM4_HEIGHT, CM4_DEPTH))
base.cut_cube(target=main, scale=(CM4_WIDTH, CM4_HEIGHT - 5, CM4_DEPTH))
base.cut_cube(target=main,scale=(CM4_WIDTH - 12, CM4_HEIGHT - 12, CM4_DEPTH + CM4_THICKNESS * 2), location=(0, 0, -CM4_THICKNESS))

M = 2.3
X = (45.4 + M) / 2
Y = (30.5 + M) / 2
Z = 1.3
holes = [(X, Y), (X, -Y), (-X, Y), (-X, -Y)]
for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=2.5,
        inner_radius=M / 2,
        depth=CM4_THICKNESS + Z,
        location=(x, y, -CM4_DEPTH / 2),
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
        depth=CM4_THICKNESS,
        location=(x, y, -CM4_DEPTH / 2 - CM4_THICKNESS),
        rotation=(0, 0, math.radians(rotation)),
    )

# ===============================




# ===============================

#scale=(
#    X_ALL + CM4_THICKNESS*4,
#    Y_ALL + CM4_THICKNESS*4,
#    CM4_DEPTH_TOP + CM4_THICKNESS,
#)
#location=(0, 0, (CM4_DEPTH-CM4_DEPTH_TOP+CM4_THICKNESS)/2)
#base.cut_cube(target=main, scale=scale, location=location)

# ===============================

#scale=(
#    X_ALL + CM4_THICKNESS*4,
#    Y_ALL + CM4_THICKNESS*4,
#    CM4_DEPTH_BOTTOM+CM4_THICKNESS,
#)
#location=(0, 0, (-CM4_DEPTH+CM4_DEPTH_BOTTOM-CM4_THICKNESS)/2)
#base.cut_cube(target=main, scale=scale, location=location)
#main.rotation_euler[1] = math.pi
