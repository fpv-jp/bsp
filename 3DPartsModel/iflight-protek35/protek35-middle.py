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

# 初期化
base.init()

plate_width = 63.5
plate_height = 172
plate_depth = 2

gap_depth = plate_depth / 2

main = base.create_cube(scale=(plate_width, plate_height, plate_depth), name="main")

M2 = 1.25
M2_5 = 1.5
M3 = 1.75
M48 = 48.25

prop_x = 57.0
prop_y = 48.0

holes = [
    (prop_x, prop_y),
    (prop_x, -prop_y),
    (-prop_x, prop_y),
    (-prop_x, -prop_y),
]

base.cut_holes(
    target=main,
    radius=M48,
    depth=plate_depth + 1,
    positions=holes,
    z=0,
    vertices=128,
    name="cylinder_large",
)

prop_x1 = 13.75
prop_y1 = 83.0

prop_x2 = 28.75
prop_y2 = 0.0

prop_x3 = 7.0
prop_y3 = 43.5

holes = [
    (prop_x1, prop_y1),
    (prop_x1, -prop_y1),
    (-prop_x1, prop_y1),
    (-prop_x1, -prop_y1),
    (prop_x2, prop_y2),
    (-prop_x2, prop_y2),
    (prop_x3, prop_y3),
    (-prop_x3, prop_y3),
]

base.cut_holes(
    target=main,
    radius=M2_5,
    depth=plate_depth + 1,
    positions=holes,
    z=0,
    name="cylinder_small",
)

base.cut_cube(
    target=main,
    scale=(32, 32, plate_depth + 1),
    location=(0, 5, 0),
    rotation=(0, 0, math.radians(45)),
    name="cube_cut_center",
)

prop_x1 = 32.5
prop_y1 = 77.0

holes = [
    (prop_x1, -prop_y1),
    (-prop_x1, prop_y1),
]

for i, (x, y) in enumerate(holes):
    base.cut_triangle(
        target=main,
        verts=[(0, x, 0), (-9, 0, 0), (9, 0, 0)],
        depth=plate_depth + 1,
        location=(0, y, -plate_depth / 1.5),
        name=f"triangle_cut_1_{i}",
    )

verts = [(0, -20, 0), (-11, 11, 0), (0, 0, 0)]

base.cut_triangle(
    target=main,
    verts=verts,
    depth=plate_depth + 1,
    location=(-2.5, -23, -plate_depth / 1.5),
    name="triangle_cut_2_left",
)

base.cut_triangle(
    target=main,
    verts=verts,
    depth=plate_depth + 1,
    location=(2.5, -23, -plate_depth / 1.5),
    rotation=(0, math.radians(180), 0),
    name="triangle_cut_2_right",
)

prop_x1 = 21.5
prop_y1 = 86.0

holes = [
    (prop_x1, prop_y1),
    (prop_x1, -prop_y1),
    (-prop_x1, prop_y1),
    (-prop_x1, -prop_y1),
]

for i, (x, y) in enumerate(holes):
    base.cut_cube(
        target=main,
        scale=(10, 10, plate_depth + 1),
        location=(x, y, 0),
        rotation=(0, 0, math.radians(45)),
        name=f"cube_cut_corner_{i}",
    )

ant_y = -80
ant_z = 3

base.add_cylinder(
    target=main,
    radius=3.4,
    depth=12,
    location=(0, ant_y, ant_z),
    rotation=(math.radians(25), 0, 0),
    name="antenna_outer",
)
base.cut_cylinder(
    target=main,
    radius=2.15,
    depth=12.1,
    location=(0, ant_y, ant_z),
    rotation=(math.radians(25), 0, 0),
    name="antenna_inner",
)
base.cut_cube(
    target=main,
    scale=(1.5, 3, 20),
    location=(0, 3 + ant_y, ant_z),
    rotation=(math.radians(25), 0, 0),
    name="antenna_slot_1",
)
base.cut_cube(
    target=main,
    scale=(1.5, 3, 20),
    location=(0, 3 + ant_y, ant_z),
    rotation=(math.radians(25), 0, 0),
    name="antenna_slot_2",
)

base.cut_cube(
    target=main,
    scale=(5.5, 3, 4),
    location=(14, -3.9, 0),
    rotation=(0, 0, math.radians(45)),
    name="cube_cut_diag",
)

base.cut_cube(
    target=main,
    scale=(plate_width, plate_height, 10),
    location=(0, 0, -6),
    name="cube_cut_bottom",
)
