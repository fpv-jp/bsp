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

#############################################################


X = 3.4
Y = 20.0
Y2 = 27.2
Z = 8.3
M = 0.8
P = 11.8


x = 13.75
y = 0.0


main = base.create_cube(scale=(x * 2, cube_height, Z / 2))

base.add_cube(
    target=main, scale=(x * 2 + M2_5 * 4, cube_height / 2, Z / 2), location=(0, cube_height / 4, 0)
)


holes2 = [
    (x, y),
    (-x, y),
]

for i, (x, y) in enumerate(holes2):
    base.add_ring(
        target=main,
        outer_radius=M2_5 * 2,
        inner_radius=M2_5,
        location=(x, y, 0),
        depth=Z / 2,
    )

main.location = (0.0, -(Y2 + cube_height) / 2, Z / 4)

################################################################

main2 = base.create_cube(scale=(X, Y2, Z), location=(0, 0, -Z / 2))

for i, (y) in enumerate([P, -P]):
    base.add_ring(
        target=main2,
        outer_radius=1.8,
        inner_radius=M,
        location=(0, y, 0),
        depth=X,
        rotation=(0, math.pi / 2, 0),
    )

base.cut_cube(target=main2, scale=(X, Y, Z))

main2.location = (15.0, 0.0, Z)

################################################################

main3 = base.create_cube(scale=(X, Y2, Z), location=(0, 0, -Z / 2))

# Y = Y - Z

base.add_ring(
    target=main3,
    outer_radius=Z / 2,
    inner_radius=1.8,
    location=(0, (Y - Z) / 2 - 0.1, 0),
    depth=X,
    rotation=(0, math.pi / 2, 0),
)


base.cut_cube(
    target=main3,
    scale=(X, Y, Z),
    location=(0, -Z, 0),
)

base.cut_cube(
    target=main3,
    scale=(X, Y, Z * 2),
    location=(0, Y, 0),
)

main3.location = (-15.0, 0.0, Z)

################################################################

base.modifier_apply(obj=main2, target=main, operation="UNION")
base.modifier_apply(obj=main3, target=main, operation="UNION")
