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

MAIN_WIDTH = 20.2
MAIN_HEIGHT = 10.2
MAIN_DEPTH = 4.5
MAIN_THICKNESS = 2.0

main = base.create_cube(
    scale=(MAIN_WIDTH + MAIN_THICKNESS, MAIN_HEIGHT + MAIN_THICKNESS, MAIN_DEPTH),
)

# ------------------------

M = 1.75
ARM = 30.5


def bar():
    b = base.create_cube(
        scale=(
            ARM,
            M * 4,
            MAIN_DEPTH,
        ),
    )
    for i, (x) in enumerate([ARM / 2, -ARM / 2]):
        base.add_ring(
            target=b,
            outer_radius=M * 2,
            inner_radius=M,
            depth=MAIN_DEPTH,
            location=(x, 0.0, 0.0),
        )
    return b


b = bar()
base.modifier_apply(obj=b, target=main, operation="UNION")

# ------------------------

base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH, 5.7, MAIN_DEPTH),
)
base.cut_cube(
    target=main,
    scale=(24.2, 5.2, MAIN_DEPTH - MAIN_THICKNESS),
    location=(0.0, 0.0, -MAIN_THICKNESS / 2),
)
base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
    location=(0.0, 0.0, -MAIN_THICKNESS / 2),
)
base.cut_cylinder(
    target=main,
    radius=4.5,
    depth=MAIN_DEPTH,
)

main.rotation_euler = (math.pi, 0.0, 0.0)


# ------------------------
M = 0.75
base.cut_cylinder(
    target=main,
    radius=M,
    depth=MAIN_THICKNESS,
    location=(M * 4, MAIN_HEIGHT / 2, MAIN_DEPTH / 2),
    rotation=(math.pi / 2, 0.0, 0.0),
)
base.cut_cylinder(
    target=main,
    radius=M,
    depth=MAIN_THICKNESS,
    location=(M, MAIN_HEIGHT / 2, MAIN_DEPTH / 2),
    rotation=(math.pi / 2, 0.0, 0.0),
)
base.cut_cylinder(
    target=main,
    radius=M,
    depth=MAIN_THICKNESS,
    location=(-M * 2, MAIN_HEIGHT / 2, MAIN_DEPTH / 2),
    rotation=(math.pi / 2, 0.0, 0.0),
)
