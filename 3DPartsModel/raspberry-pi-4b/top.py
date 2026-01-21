import bpy
import sys
import types
import math

text = bpy.data.texts.get("base.py")
module_name = "base"
module = types.ModuleType(module_name)
exec(text.as_string(), module.__dict__)
sys.modules[module_name] = module

import base

base.init()

MAIN_WIDTH = 67.0
MAIN_HEIGHT = 56.0
MAIN_DEPTH = 1.0
MAIN_THICKNESS = 2.0

main = base.create_cube(
    scale=(MAIN_WIDTH + MAIN_THICKNESS, MAIN_HEIGHT + MAIN_THICKNESS, MAIN_DEPTH),
)

H = 2.5

main.location = (1.25, 0, -H / 2)

M2_7 = 1.35
X = 58.0
Y = 49.0
M = M2_7 * 4

XXX = X / 2
YYY = Y / 2


base.add_cube(
    target=main,
    scale=(X, M, H),
    location=(0, YYY, 0),
)
base.add_cube(
    target=main,
    scale=(-X, M, H),
    location=(0, -YYY, 0),
)
base.add_cube(
    target=main,
    scale=(M, Y, H),
    location=(XXX, 0, 0),
)
base.add_cube(
    target=main,
    scale=(M, Y, H),
    location=(-XXX, 0, 0),
)

c = [(XXX, YYY), (-XXX, YYY), (XXX, -YYY), (-XXX, -YYY)]
for i, (x, y) in enumerate(c):
    base.add_ring(
        target=main,
        outer_radius=M2_7 * 2,
        inner_radius=M2_7,
        location=(x, y, 0),
        depth=H,
    )

main.location = (-11.0, 0, -H / 2)


P = 30.0
M = 5.6

base.add_cube(
    target=main,
    scale=(P + M, 6.0, H),
)
base.add_cube(
    target=main,
    scale=(6.0, P + M, H),
)


main.rotation_euler[2] = math.radians(45)
main.location = (0, 4.5, -H / 2)
base.add_cube(
    target=main,
    scale=(32, 6.0, H),
    location=(-20, 0, 0),
)
main.rotation_euler[2] = math.radians(-45)
main.location = (0, -4.5, -H / 2)
base.add_cube(
    target=main,
    scale=(32, 6.0, H),
    location=(-20, 0, 0),
)

main.rotation_euler[2] = 0
main.location = (-11.0, 0, -H / 2)


X = (P + M) / 2

c = [(X, 0.0), (-X, 0.0), (0.0, X), (0.0, -X)]
for i, (x, y) in enumerate(c):
    base.add_ring(
        target=main,
        outer_radius=3.0,
        inner_radius=1.5,
        location=(x, y, 0),
        depth=H+.01,
    )
