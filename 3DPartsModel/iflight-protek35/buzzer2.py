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

MAIN_WIDTH = 19.9
MAIN_HEIGHT = 9.8
MAIN_DEPTH = 3.0

MAIN_THICKNESS = 1.0

main = base.create_cube(
    scale=(MAIN_WIDTH + MAIN_THICKNESS * 2, MAIN_HEIGHT + MAIN_THICKNESS * 2, MAIN_DEPTH),
)
base.cut_cube(
    target=main,
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
)

base.cut_cube(
    target=main,
    scale=(24.2, 5.2, MAIN_DEPTH),
    location=(0.0, 0.0, 1.45),
)

main.location = (0.0, 0.0, MAIN_DEPTH / 2)
## ------------------------

ARM = 25.5 / 2
M = 1.25


def bar():
    b = base.create_cube(
        scale=(M * 4, M * 4, MAIN_THICKNESS),
        location=(0.0, -M * 2, MAIN_THICKNESS / 2),
    )
    base.add_ring(
        target=b,
        outer_radius=M * 2,
        inner_radius=M,
        depth=MAIN_THICKNESS,
        location=(0.0, 0.0, MAIN_THICKNESS / 2),
    )
    return b


bar1 = bar()
bar1.location = (ARM, 7.7, 0.0)
bar1.rotation_euler = (0, 0, -math.pi / 4)

bar2 = bar()
bar2.location = (-ARM, 7.7, 0.0)
bar2.rotation_euler = (0, 0, math.pi / 4)

base.modifier_apply(obj=bar1, target=main, operation="UNION")
base.modifier_apply(obj=bar2, target=main, operation="UNION")
