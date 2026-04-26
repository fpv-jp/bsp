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


MAIN_WIDTH = 5.5
MAIN_HEIGHT = 5.5
MAIN_DEPTH = 3.0

main = base.create_cube(
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
)
base.cut_cylinder(
    target=main,
    radius=3.5,
    depth=10.0,
)
base.add_ring(
    target=main,
    outer_radius=7.5,
    inner_radius=3.5,
    depth=MAIN_DEPTH,
)

for i, (x) in enumerate([8.0, -8.0]):
    base.add_ring(
        target=main,
        outer_radius=3.5,
        inner_radius=1.5,
        depth=MAIN_DEPTH,
        location=(0.0, x, 0.0),
    )


def triangle():
    main2 = base.create_cube(
        scale=(
            15.0,
            2.0,
            35.0,
        ),
    )
    for i, (x, y) in enumerate([(-11.25, math.pi / 20), (11.25, -math.pi / 20)]):
        base.cut_cube(
            target=main2,
            scale=(
                15.0,
                2.0,
                35.0 * 1.25,
            ),
            location=(x, 0, 0),
            rotation=(0, y, 0),
        )
    return main2


t1 = triangle()
t1.location = (0.0, 0.0, 15.0)

t2 = triangle()
t2.rotation_euler = (0, 0, math.pi / 2)
t2.location = (0, 0.0, 15.0)

base.modifier_apply(obj=t1, target=main, operation="UNION")
base.modifier_apply(obj=t2, target=main, operation="UNION")

base.cut_cube(
    target=main,
    scale=(50.0, 50.0, 30.0),
    location=(0, 0, -15.0 - MAIN_DEPTH / 2),
)
base.cut_cube(
    target=main,
    scale=(50.0, 50.0, 30.0),
    location=(0, 0, 15.0 + MAIN_DEPTH / 2 + 30.0),
)
