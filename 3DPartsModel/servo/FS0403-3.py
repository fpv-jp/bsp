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
cube_height = 8.8

#############################################################

X = 3.4
Y = 20.0
Y2 = 27.2
Z = 16.0

CENTER = Y / 2 - 4.0

main = base.create_cube(
    scale=(34.0, cube_height, 3.0),
    # location=(4.75, CENTER, 1.5),
)

X2 = 4.75
base.cut_cylinder(
    target=main,
    radius=1.5,
    depth=3.0,
    location=(-X2, 0.0, 0.0),
)

P2 = 2.0

holes = [
    (-X2 - 5.5 - P2 * 1),
    (-X2 - 5.5 - P2 * 0),
    (-X2 + 5.5 + P2 * 0),
    (-X2 + 5.5 + P2 * 1),
    (-X2 + 5.5 + P2 * 2),
    (-X2 + 5.5 + P2 * 3),
]

for i, (y) in enumerate(holes):
    base.cut_cylinder(
        target=main,
        radius=0.5,
        depth=3.0,
        location=(y, 0.0, 0.0),
    )

main.location = (X2, CENTER, 1.5)

##################################################################

main2 = base.create_cube(scale=(X, Y2, Z), location=(0, 0, -Z / 2))

M = 0.7
P = 11.8

for i, (y) in enumerate([P, -P]):
    base.add_ring(
        target=main2,
        outer_radius=1.8,
        inner_radius=M,
        location=(0, y, 0),
        depth=X,
        rotation=(0, math.pi / 2, 0),
    )

base.cut_cube(target=main2, scale=(X, Y, Z * 2), location=(0, 0, 3.0))

main2.location = (22.0, 0.0, Z)

###################################################################

main3 = base.create_cube(scale=(X, Y2, Z), location=(0, 0, -Z / 2))

base.add_ring(
    target=main3,
    outer_radius=4.4,
    inner_radius=2.2,
    location=(0, CENTER, 0),
    depth=X,
    rotation=(0, math.pi / 2, 0),
)


base.cut_cube(
    target=main3,
    scale=(X, Y, Z),
    location=(0, CENTER - Y / 2 - 4.4, -Z / 2 + 3.0),
)

base.cut_cube(
    target=main3,
    scale=(X, Y, Z * 2),
    location=(0, CENTER + Y / 2 + 4.4, 0),
)

main3.location = (-12.0, 0.0, Z)

##################################################################

main4 = base.create_cube(
    scale=(34.0, 3.6, 3.0),
    location=(X2, -P, 1.5),
)

##################################################################

base.modifier_apply(obj=main2, target=main, operation="UNION")
base.modifier_apply(obj=main3, target=main, operation="UNION")
base.modifier_apply(obj=main4, target=main, operation="UNION")

# main.location = (0.0, 0.0, 0.0)
