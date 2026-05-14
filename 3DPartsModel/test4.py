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

# BODY_R = 22.5
BODY_R = 30.5 / 2

## -------------------------------------

MAIN_DEPTH = 3.0

body = base.create_cube(
    scale=(30.5, 30.5, MAIN_DEPTH),
    rotation=(0, 0, math.pi / 4),
)

M3 = 1.75

base.cut_cylinder(
    target=body,
    radius=M3,
    depth=MAIN_DEPTH * 2,
)

FC_PITCH = 30.5 / 2

for i, (x, y) in enumerate([(FC_PITCH, 0), (-FC_PITCH, 0), (0, FC_PITCH), (0, -FC_PITCH)]):
    base.add_ring(
        target=body,
        outer_radius=6.0,
        inner_radius=M3,
        depth=MAIN_DEPTH,
        location=(x, y, 0.0),
    )
## -------------------------------------

H = 5.0 / 2 + MAIN_DEPTH / 2
body.location = (0.0, 0.0, H)

## -------------------------------------
## -------------------------------------
## -------------------------------------

INCH = 152.4

CCC = 1.39
MAIN_DEPTH = 5.0
main = base.create_cube(
    scale=(INCH / CCC, 12.0, MAIN_DEPTH),
    location=(INCH / CCC / 2, 0.0, 0.0),
)
# ------------------------
MOTOR = 37.5
base.add_cylinder(
    target=main,
    radius=MOTOR / 2,
    #    radius=INCH/2,
    depth=MAIN_DEPTH,
    vertices=6,
    rotation=(0, 0, math.pi / 6),
)
base.cut_cylinder(
    target=main,
    radius=5.1,
    depth=MAIN_DEPTH * 2,
)
# ------------------------
MOTOR_PITCH = 19.0 / 2
M3 = 1.75

main.rotation_euler[2] = math.pi / 4
for i, (x, y) in enumerate(
    [(MOTOR_PITCH, 0), (-MOTOR_PITCH, 0), (0, MOTOR_PITCH), (0, -MOTOR_PITCH)]
):
    base.cut_cylinder(
        target=main,
        radius=M3,
        depth=MAIN_DEPTH * 2,
        location=(x, y, 0.0),
    )
main.rotation_euler[2] = 0
# ------------------------


main.location = (-INCH / CCC, 0.0, 0.0)
# M3 = 1.75
FC = 30.5 / 2

base.cut_cylinder(
    target=main,
    radius=M3,
    depth=MAIN_DEPTH * 2,
    location=(-FC, 0.0, 0.0),
)
base.cut_cylinder(
    target=main,
    radius=M3,
    depth=MAIN_DEPTH * 2,
)

# -------------------------------------

MAX = 95 / 8
scale = (400.0, 400.0, MAIN_DEPTH * 2)
LX = 200.0
base.cut_cube(
    target=main,
    scale=scale,
    location=(0.0, LX + MAX, 0.0),
)
base.cut_cube(
    target=main,
    scale=scale,
    location=(0.0, -LX - MAX, 0.0),
)
base.cut_cube(
    target=main,
    scale=scale,
    rotation=(0, 0, math.pi / 4),
    location=(0.0, LX * 1.41421, 0.0),
)

base.cut_cube(
    target=main,
    scale=scale,
    rotation=(0, 0, math.pi / 4),
    location=(0.0, -LX * 1.41421, 0.0),
)

# -------------------------------------

main2 = base.copy(main, location=(INCH / CCC, 0, 0))
main2.rotation_euler[2] = math.pi

main3 = base.copy(main, location=(0, -INCH / CCC, 0))
main3.rotation_euler[2] = math.pi / 2

main4 = base.copy(main, location=(0, INCH / CCC, 0))
main4.rotation_euler[2] = -math.pi / 2

# -------------------------------------

# CCC=INCH/CCC/2.45
# MAX=MAX*.85
# main2 = base.copy(main, location=(CCC, -MAX, 0))
# main2.rotation_euler[2] = math.pi

# main3 = base.copy(main, location=(-CCC, MAX, 0))

# main4 = base.copy(main, location=(CCC, MAX*3, 0))
# main4.rotation_euler[2] = math.pi

# main.location=(-CCC, -MAX*3, 0)

# cfrp = base.create_cube(
#    scale=(135, 85, MAIN_DEPTH/2),
# )
