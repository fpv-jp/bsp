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

MAIN_WIDTH = 30.5 + M3 * 2
MAIN_HEIGHT = 30.5 + M3 * 2
MAIN_DEPTH = 5.0


# -------------------------------------
main = base.create_cube(
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
)
base.add_cylinder(
    target=main,
    radius=22.0,
    depth=2.0,
    vertices=8,
    location=(0.0, 0.0, -MAIN_DEPTH/2+1.0),
)

main.rotation_euler[2] = math.pi / 4

base.add_cube(
    target=main,
    scale=(162.0, 10.0, MAIN_DEPTH),
)
base.add_cube(
    target=main,
    scale=(10.0, 162.0, MAIN_DEPTH),
)

base.cut_cylinder(
    target=main,
    radius=5.0,
    depth=MAIN_DEPTH,
)
#base.cut_cylinder(
#    target=main,
#    radius=3.7,
#    depth=2.0,
#    location=(0,0, -MAIN_DEPTH / 2 +1.0),
#)
#    
# -------------------------------------
P1 = 30.5 / 2
for i, (x, y) in enumerate([(P1, 0), (-P1, 0), (0, P1), (0, -P1)]):
    base.add_ring(
        target=main,
        outer_radius=M3 * 5,
        inner_radius=M3,
        depth=MAIN_DEPTH,
        location=(x, y, 0.0),
    )
    base.cut_cylinder(
        target=main,
        radius=3.2,
        depth=2.0,
        location=(x, y, MAIN_DEPTH / 2 - 1.0),
    )

# -------------------------------------


def create_arm():
    arm = base.create_cylinder(
        radius=27.8 / 2,
#        radius=127 / 2,
        depth=MAIN_DEPTH,
    )
    base.cut_cylinder(
        target=arm,
        radius=4.1,
        depth=MAIN_DEPTH * 2,
    )
    PX = (13.5 + 18.2) / 4
    PY = (16.5 + 21.3) / 4
    for i, (x, y) in enumerate([(PX, 0), (-PX, 0), (0, PY), (0, -PY)]):
        base.cut_cylinder(
            target=arm,
            radius=1.75,
            depth=MAIN_DEPTH * 2,
            location=(x, y, 0.0),
        )
        base.cut_cylinder(
            target=arm,
            radius=3.0,
            depth=3.0,
            location=(x, y, MAIN_DEPTH / 2 - 1.5),
        )
    return arm


P2 = 127 / 2 * 1.48

for i, (x, y) in enumerate([(P2, 0), (-P2, 0)]):
    arm = create_arm()
    arm.rotation_euler[2] = math.pi / 4
    arm.location = (x, y, 0.0)
    base.modifier_apply(obj=arm, target=main, operation="UNION")

for i, (x, y) in enumerate([(0, P2), (0, -P2)]):
    arm = create_arm()
    arm.rotation_euler[2] = -math.pi / 4
    arm.location = (x, y, 0.0)
    base.modifier_apply(obj=arm, target=main, operation="UNION")


# -------------------------------------

main.rotation_euler[2] = 0

P = 19.3
M = 1.25
for i, (x,y) in enumerate([(P,0),(-P,0),(0,P),(0,-P)]):
    base.cut_cylinder(
        target=main,
        radius=M,
        depth=MAIN_DEPTH*2,
        location=(x, y, MAIN_DEPTH/2-1.0),
    )
