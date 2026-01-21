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

plate_width = 23.5
plate_height = 23.5
plate_depth = 8

main = base.create_cube(
    scale=(plate_width, plate_height, plate_depth),
    location=(0, 0, 0),
    name="main",
)


############################################################

cube_width = 20
cube_height = 20

M2 = 1.25
M5 = 2.75

base.add_cylinder(
    target=main,
    radius=M5,
    depth=23.5,
    location=(0, 0, 5.75),
    rotation=(0, math.pi / 2, 0),
    name="Cylinder",
)

base.add_cube(
    target=main,
    scale=(23.5, M5 * 2, 5),
    location=(0, 0, 5.75 - M5),
    name="CubeCut",
)

base.cut_cylinder(
    target=main,
    radius=M2,
    depth=24,
    location=(0, 0, 5.75),
    rotation=(0, math.pi / 2, 0),
    name="Hole",
)

# =======================================

base.cut_cube(
    target=main,
    scale=(cube_width, cube_height, 14),
    location=(0, 0, 4.5),
    name="CubeCut",
)

base.cut_cube(
    target=main,
    scale=(10.9, 3.6, plate_depth),
    location=(2.0, 2.5, 0),
    name="CubeCut",
)

main.rotation_euler = (math.pi / 2.5, 0, 0)

base.add_cube(
    target=main,
    scale=(33, 18, 2),
    location=(0, 3, -11.41),
    name="Cube",
)

prop_x1 = 13.75
prop_y1 = 9.25
M3 = 1.75

holes = [
    (prop_x1, prop_y1),
    (-prop_x1, prop_y1),
]

for i, (x, y) in enumerate(holes):
    base.cut_cylinder(
        target=main,
        radius=M3,
        depth=2.5,
        location=(x, y, -11.41),
        name="Cylinder",
    )
