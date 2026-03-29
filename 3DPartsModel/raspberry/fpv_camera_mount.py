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


M3 = 1.75

cube_width = 20
cube_height = 20
cube_thickness = 1.75


#############################################################

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


#############################################################

main2 = base.create_cube(
    scale=(cube_width + cube_thickness * 3, cube_height, M3*3),
)

M2 = 1.25
M5 = 2.75

base.add_ring(
    target=main2,
    outer_radius=M5,
    inner_radius=M2,
    depth=cube_width + cube_thickness * 3,
    location=(0.0, cube_height/2-M3*1.5, M3),
    rotation=(0.0, math.pi / 2, 0.0),
)

base.cut_cube(
    target=main2,
    scale=(cube_width, cube_height*2, cube_width),
)

main2.rotation_euler = (math.pi / 2, 0, 0.0)
main2.location = (0.0, 0.0, 6.0)

base.cut_cube(
    target=main2,
    scale=(30.0, 30.0, 10.0),
    location=(0.0, 0.0, -5.0-cube_thickness/2),
)
base.join(main, main2)
