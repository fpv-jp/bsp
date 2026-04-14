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

depth = 2.0

main = base.create_cylinder(
    radius=10.0,
    depth=2.0,
    vertices=6,
)
main.rotation_euler = (0, 0, math.pi / 4)

P = 6.0
for i, (x, y) in enumerate([(P, 0), (-P, 0), (0, P), (0, -P)]):
    base.cut_cylinder(
        target=main,
        radius=1.25,
        depth=depth,
        location=(x, y, 0),
    )

main.rotation_euler = (0, 0, math.pi / 2)


def triangle():
    main2 = base.create_cube(
        scale=(
            10.0,
            2.0,
            20.0,
        ),
    )
    base.cut_cube(
        target=main2,
        scale=(
            12.0,
            2.0,
            30.0,
        ),
        location=(-5, 0, 0),
        rotation=(0, math.pi / 10, 0),
    )
    return main2


t1 = triangle()
t1.location = (-5.0, 0, 10.0)

t2 = triangle()
t2.rotation_euler = (0, 0, math.pi / 2)
t2.location = (0, -5.0, 10.0)

t3 = triangle()
t3.rotation_euler = (0, 0, -math.pi / 2)
t3.location = (0, 5.0, 10.0)

t4 = triangle()
t4.rotation_euler = (0, 0, math.pi)
t4.location = (5.0, 0, 10.0)

base.modifier_apply(obj=t1, target=main, operation="UNION")
base.modifier_apply(obj=t2, target=main, operation="UNION")
base.modifier_apply(obj=t3, target=main, operation="UNION")
base.modifier_apply(obj=t4, target=main, operation="UNION")

base.cut_cube(
    target=main,
    scale=(20.0, 20.0, 20.0),
    location=(0, 0, 28.0),
)
