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


M2_5 = 1.5
M3 = 1.75

cube_width = 19.3
cube_height = M2_5 * 4
cube_depth = 14.0

cube_thickness = 1.75

#############################################################

x = 13.75
y = 0.0

holes2 = [
    (x, y),
    (-x, y),
]

main = base.create_cube(scale=(x * 2, M2_5 * 4, cube_thickness))

for i, (x, y) in enumerate(holes2):
    base.add_ring(
        target=main,
        outer_radius=M2_5 * 2,
        inner_radius=M2_5,
        location=(x, y, 0),
        depth=cube_thickness,
    )

main.location = (0.0, 0.0, (-cube_thickness - cube_depth) / 2)

##############################################################

M2 = 1.25
M5 = 2.75


base.add_cube(
    target=main,
    scale=(cube_width + cube_thickness * 2, cube_height, cube_depth),
)

base.add_ring(
    target=main,
    outer_radius=M5,
    inner_radius=M2,
    depth=cube_width + cube_thickness * 2,
    location=(0.0, cube_height / 2, cube_depth / 2 - M5),
    rotation=(0.0, math.pi / 2, 0.0),
)

base.cut_cube(
    target=main,
    scale=(cube_width, cube_height * 2, cube_depth + 0.01),
)
