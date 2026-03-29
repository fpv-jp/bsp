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

M2 = 1.25
M3 = 1.75
M4 = 2.25
M5 = 2.75
M6 = 3.25
M7 = 3.75

cut_y = 22.6
cut_z = 12.4

plate_thickness = 2.5

plate_width = 45.0
plate_height = cut_y + plate_thickness * 4
plate_depth = 33.0

main = base.create_cube(
    scale=(plate_width, plate_height, plate_depth),
)
base.cut_cube(
    target=main,
    scale=(plate_width, plate_height, plate_depth),
    location=(plate_thickness, 0, plate_thickness),
)

x_cut = plate_width - plate_thickness * 4
y_cut = plate_height - plate_thickness * 4

base.cut_cube(
    target=main,
    scale=(x_cut, y_cut, plate_depth),
)
z_cut = plate_depth/2 - plate_thickness*2
base.cut_cube(
    target=main,
    scale=(x_cut, y_cut, z_cut),
    location=(-plate_width/2, 0, (z_cut-plate_depth)/2+plate_thickness),
)
z = (plate_depth - cut_z) / 2 - plate_thickness
base.cut_cube(
    target=main,
    scale=(plate_width, cut_y, cut_z),
    location=(0, 0, z),
)

x = (plate_thickness - plate_width) / 2
y = 13.6

holes = [(x, y), (x, -y)]

for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=M6,
        inner_radius=M2,
        location=(x, y, z),
        depth=plate_thickness,
        rotation=(0, math.pi / 2, 0),
    )


################################################################

base.add_cube(
    target=main,
    scale=(plate_width, plate_thickness, plate_depth),
    location=(0, 4, 0),
)
base.add_cube(
    target=main,
    scale=(plate_width, plate_thickness, plate_depth),
    location=(0, -4, 0),
)
base.add_cube(
    target=main,
    scale=(plate_thickness*2, plate_height, plate_depth),
)
base.cut_cube(
    target=main,
    scale=(plate_width, plate_height, plate_depth),
    location=(plate_thickness, 0, plate_thickness),
)


##################################################################

x = (plate_width - plate_thickness) / 2

base.add_cube(
    target=main,
    scale=(plate_thickness, M3 * 4, z + plate_depth / 2),
    location=(x, -6.3, -z / 2),
)

base.add_cube(
    target=main,
    scale=(plate_thickness, M3 * 4, plate_thickness),
    location=(x-plate_thickness/2, -6.3, plate_thickness-plate_depth/2),
    rotation=(0, math.pi / 4, 0),
)

base.add_ring(
    target=main,
    outer_radius=M3 * 2,
    inner_radius=M3,
    location=(x, -6.3, z),
    depth=plate_thickness,
    rotation=(0, math.pi / 2, 0),
)

#################################################################

main.location = (0, -plate_height/2-M3 * 2, (plate_depth-plate_thickness)/2)

x = 18.9
y = 0.0

holes = [(x, y), (-x, y)]

for i, (x, y) in enumerate(holes):
    base.add_cube(
        target=main,
        scale=(M3 * 4, M3 * 2, plate_thickness),
        location=(x, -M3, 0),
    )
    base.add_ring(
        target=main,
        outer_radius=M3 * 2,
        inner_radius=M3,
        location=(x, 0, 0),
        depth=plate_thickness,
    )
