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

BODY_R = 22.5
#BODY_R = 28.5

## -------------------------------------
MAIN_DEPTH = 2.5
body = base.create_cylinder(
    radius=BODY_R,
    depth=MAIN_DEPTH,
    vertices=64,
)

M4 = 2.25
base.cut_cylinder(
    target=body,
    radius=M4,
    depth=MAIN_DEPTH*2,
)

FC_PITCH = 30.5 / 2
M3 = 1.75
for i, (x, y) in enumerate([(FC_PITCH, 0), (-FC_PITCH, 0), (0, FC_PITCH), (0, -FC_PITCH)]):
    base.cut_cylinder(
        target=body,
        radius=M3,
        depth=MAIN_DEPTH * 2,
        location=(x, y, 0.0),
    )

## -------------------------------------

H = 5.0/2+2.5/2
body2 = base.copy(body, location=(0, 0, 0))
body.location=(0.0, 0.0, H)
body2.location=(0.0, 0.0, -H)

## -------------------------------------
## -------------------------------------
## -------------------------------------

INCH = 152.4
ARM = 12.0
MAIN_DEPTH = 5.0
main = base.create_cube(
    scale=(INCH/1.5, ARM, MAIN_DEPTH),
    location=(INCH/3, 0.0, 0.0),
)
base.add_cylinder(
    target=main,
    radius=BODY_R,
    depth=MAIN_DEPTH,
    vertices=64,
)

M4 = 2.25
base.cut_cylinder(
    target=main,
    radius=M4,
    depth=MAIN_DEPTH*2,
)

# -------------------------------------
MOTOR = 37.5
m = base.create_cylinder(
    radius=MOTOR/2,
#    radius=INCH/2,
    depth=MAIN_DEPTH,
    vertices=64,
)
base.cut_cylinder(
    target=m,
    radius=5.1,
    depth=MAIN_DEPTH*2,
)
MOTOR_PITCH = 19.0 / 2
M3 = 1.75
for i, (x, y) in enumerate([(MOTOR_PITCH, 0), (-MOTOR_PITCH, 0), (0, MOTOR_PITCH), (0, -MOTOR_PITCH)]):
    base.cut_cylinder(
        target=m,
        radius=M3,
        depth=MAIN_DEPTH * 2,
        location=(x, y, 0.0),
    )

m.rotation_euler[2] = math.pi / 4
m.location=(INCH / 2 * 1.47, 0.0, 0.0)
base.modifier_apply(obj=m, target=main, operation="UNION")

# -------------------------------------

M3 = 1.75
FC = 30.5 / 2

base.cut_cylinder(
    target=main,
    radius=M3,
    depth=MAIN_DEPTH * 2,
    location=(FC, 0.0, 0.0),
)

# -------------------------------------
MAX = 95/8
scale =( 400.0, 400.0, MAIN_DEPTH*2)
LX = 200.0
#base.cut_cube(
#    target=main,
#    scale=scale,
#    location=(0.0, LX+MAX, 0.0),
#)
#base.cut_cube(
#    target=main,
#    scale=scale,
#    location=(0.0, -LX-MAX, 0.0),
#)
main.rotation_euler[2] = math.pi / 4
base.cut_cube(
    target=main,
    scale=scale,
    location=(-LX, 0.0, 0.0),
)
main.rotation_euler[2] = -math.pi / 4
base.cut_cube(
    target=main,
    scale=scale,
    location=(-LX, 0.0, 0.0),
)

main.rotation_euler[2] = 0

# -------------------------------------

main2 = base.copy(main, location=(0, 0, 0))
main2.rotation_euler[2] = math.pi

main3 = base.copy(main, location=(0, 0, 0))
main3.rotation_euler[2] = math.pi / 2

main4 = base.copy(main, location=(0, 0, 0))
main4.rotation_euler[2] = -math.pi / 2

#### -------------------------------------

###cfrp = base.create_cube(
###    scale=(145, 95, MAIN_DEPTH),
###    location=(0.0, MOTOR/2, 0.0),
###)
