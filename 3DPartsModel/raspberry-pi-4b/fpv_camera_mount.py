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

plate_depth = 7.5

cube_width = 20
cube_height = 20
cube_thickness = 1.75


#############################################################

M3 = 1.75

x = 18.9
y = 0.0

holes2 = [
    (x, y),
    (-x, y),
]

main = base.create_cube(scale=(x * 2, M3 * 4, cube_thickness))

for i, (x, y) in enumerate(holes2):
    base.add_ring(
        target=main,
        outer_radius=M3 * 2,
        inner_radius=M3,
        location=(x, y, 0),
        depth=cube_thickness,
    )


base.cut_cube(
    target=main,
    scale=(40.0, 15.0, cube_thickness),
    location=(0, 0, -cube_thickness),
)

#########################################

base.add_cube(
    target=main,
    scale=(25.75, 9.5, cube_thickness),
    location=(0, 8.0, 0),
)

#############################################################
z = 0.0

M4_5 = 2.5

PITCH = 27.0
y = 17.7

base.add_cube(
    target=main,
    scale=(PITCH * 2, M4_5 * 4, cube_thickness),
    location=(0, y, z),
)

holes = [(-PITCH, y), (PITCH, y)]

for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=M4_5 * 2,
        inner_radius=M4_5,
        location=(x, y, z),
        depth=cube_thickness,
    )

# #########################################

PITCH = 16.0
y = y - 3.0

holes = [(-PITCH, y), (PITCH, y)]

for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=6.5,
        inner_radius=3.25,
        location=(x, y, z),
        depth=cube_thickness,
    )


main2 = base.create_cube(
    scale=(cube_width + cube_thickness * 2, cube_height + cube_thickness * 2, plate_depth),
)
base.cut_cube(
    target=main2,
    scale=(9.9, 3.7, plate_depth),
    location=(0, 8.15, 0),
)

M2 = 1.25
M5 = 2.75

base.add_ring(
    target=main2,
    outer_radius=M5,
    inner_radius=M2,
    location=(0, 0, 4.0),
    depth=cube_width + cube_thickness * 2,
    rotation=(0, math.pi / 2, 0),
)
base.cut_cube(
    target=main2,
    scale=(cube_width, cube_height, plate_depth * 2),
    location=(0, 0, cube_thickness + plate_depth / 2),
)
main2.rotation_euler = (math.pi / 2.5, 0, 0)
main2.location = (0, 2.85, cube_width / 2 + 1.0)
base.cut_cube(
    target=main2,
    scale=(30.0, 15.0, cube_thickness + 0.5),
    location=(0, 0, -cube_thickness),
)
base.join(main, main2)
