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
M2_5 = 1.5

MAIN_WIDTH = 30.5 + M3 * 2
MAIN_HEIGHT = 30.5 + M3 * 2
MAIN_DEPTH = 6.0

R = 42 / 2
T = 1.5

# -------------------------------------
main = base.create_cylinder(
    radius=R + T,
    depth=MAIN_DEPTH,
    vertices=8,
)

INCH = 152.4
ARM = 12.0
MOTOR = 33.5

for i, (x, y) in enumerate([(INCH * 1.3, ARM), (ARM, INCH * 1.3)]):
    base.add_cube(
        target=main,
        scale=(x, y, MAIN_DEPTH),
    )

# -------------------------------------
P1 = 30.5 / 2
for i, (x, y) in enumerate([(P1, 0), (-P1, 0), (0, P1), (0, -P1)]):
    base.add_ring(
        target=main,
        outer_radius=M3 * 6,
        inner_radius=M3,
        depth=MAIN_DEPTH,
        location=(x, y, 0.0),
    )
    base.cut_cylinder(
        target=main,
        radius=M3,
        depth=MAIN_DEPTH * 2,
        location=(x, y, 0),
    )

P1 = 12.0 / 2
for i, (x, y) in enumerate([(P1, 0), (-P1, 0), (0, P1), (0, -P1)]):
    base.cut_cylinder(
        target=main,
        radius=M3,
        depth=MAIN_DEPTH * 2,
        location=(x, y, 0),
    )

main.rotation_euler[2] = math.pi / 4
P1 = 33.0 / 2
for i, (x, y) in enumerate([(P1, 0), (-P1, 0), (0, P1), (0, -P1)]):
    base.cut_cylinder(
        target=main,
        radius=M3,
        depth=MAIN_DEPTH * 2,
        location=(x, y, 0),
    )

## -------------------------------------

def create_arm():
    arm = base.create_cylinder(
        radius=MOTOR / 2,
        #        radius=INCH / 2,
        depth=MAIN_DEPTH,
        vertices=6,
    )
    base.cut_cylinder(
        target=arm,
        radius=4.1,
        depth=MAIN_DEPTH * 2,
    )
    P3 = 19.0 / 2
    arm.rotation_euler[2] = math.pi / 4
    for i, (x, y) in enumerate([(P3, 0), (-P3, 0), (0, P3), (0, -P3)]):
        base.cut_cylinder(
            target=arm,
            radius=M3,
            depth=MAIN_DEPTH * 2,
            location=(x, y, 0.0),
        )
    arm.rotation_euler[2] = 0
    return arm

main.rotation_euler[2] = 0
P2 = INCH / 2 * 1.47

for i, (x, y) in enumerate([(0, P2)]):
    arm = create_arm()
    arm.location = (x, y, 0.0)
    base.modifier_apply(obj=arm, target=main, operation="UNION")

## -------------------------------------

main.rotation_euler[2] = math.pi / 4

base.cut_cube(
    target=main,
    scale=(400, 400, 10),
    location=(200, 0.0, 0.0),
)
base.cut_cube(
    target=main,
    scale=(400, 400, 10),
    location=(0.0, -200, 0.0),
)
