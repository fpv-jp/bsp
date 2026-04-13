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
cube_depth = 12.0

cube_thickness = 1.75

#############################################################

x = 13.75
y = 0.0

holes2 = [
    (x, y),
    (-x, y),
]

main = base.create_cube(scale=(x * 2, cube_height, cube_thickness))

for i, (x, y) in enumerate(holes2):
    base.add_ring(
        target=main,
        outer_radius=M2_5 * 2,
        inner_radius=M2_5,
        location=(x, y, 0),
        depth=cube_thickness,
    )

###############################################################

M_O = 3.4
M_I = 2.15


cube_depth = 16.0
Z = 5.0

base.add_ring(
    target=main,
    outer_radius=M_O,
    inner_radius=M_I,
    depth=cube_depth,
    location=(0.0, -M_O * 1.15, Z),
    rotation=(math.radians(25), 0.0, 0.0),
)

base.cut_cube(
    target=main,
    scale=(1.3, M_O, cube_depth * 2),
    location=(0.0, -M_O * 2.15, Z),
    rotation=(math.radians(25), 0.0, 0.0),
)

###############################################################

main.location = (0.0, 0.0, cube_thickness / 2)
base.cut_cube(target=main, scale=(30, 30, 10), location=(0.0, 0.0, -5))
