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

MAIN_WIDTH = 25.5
MAIN_HEIGHT = 24.2
MAIN_DEPTH = 1.75

MAIN_THICKNESS = 1.5

main = base.create_cube(scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH))

X = 10.25
Y = -MAIN_HEIGHT / 2 + MAIN_THICKNESS + 1.1
Y2 = 13.5
base.cut_cylinder(
    target=main,
    radius=1.1,
    depth=MAIN_THICKNESS * 2,
    location=(X, Y, 0),
)
base.cut_cylinder(
    target=main,
    radius=1.1,
    depth=MAIN_THICKNESS * 2,
    location=(-X, Y, 0),
)
base.cut_cylinder(
    target=main,
    radius=1.1,
    depth=MAIN_THICKNESS * 2,
    location=(X, Y + Y2, 0),
)
base.cut_cylinder(
    target=main,
    radius=1.1,
    depth=MAIN_THICKNESS * 2,
    location=(-X, Y + Y2, 0),
)

MAIN_ARM = 65.0

base.add_cylinder(
    target=main,
    radius=2.3,
    depth=MAIN_ARM,
    location=(0, MAIN_ARM / 2, 0),
    rotation=(math.pi / 2, 0, 0),
    vertices=6,
)

MAIN_WIDTH = 14.2
MAIN_HEIGHT = 50.2
MAIN_ARM = 90.0


def create_arm():
    arm = base.create_cube(scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH))
    base.add_cylinder(
        target=arm,
        radius=2.3,
        depth=MAIN_ARM,
        location=(0, MAIN_ARM / 2, 0),
        rotation=(math.pi / 2, 0, 0),
        vertices=6,
    )
    return arm


X = 45
Y = 19

right = create_arm()
right.rotation_euler = (0, 0, -math.pi / 6)
right.location = (-X, -Y, 0)

left = create_arm()
left.rotation_euler = (0, 0, math.pi / 6)
left.location = (X, -Y, 0)

base.modifier_apply(obj=right, target=main, operation="UNION")
base.modifier_apply(obj=left, target=main, operation="UNION")

main.location = (0, -65, 0)

base.add_cube(
    target=main,
    scale=(52.5, MAIN_THICKNESS, 20.0),
    location=(0, 0, 10.0 - MAIN_THICKNESS / 2),
)

base.cut_cylinder(
    target=main,
    radius=1.1,
    depth=MAIN_THICKNESS * 2,
    location=(23.85, 0, 16.8),
    rotation=(math.pi / 2, 0, 0),
)
base.cut_cylinder(
    target=main,
    radius=1.1,
    depth=MAIN_THICKNESS * 2,
    location=(-23.85, 0, 16.8),
    rotation=(math.pi / 2, 0, 0),
)

base.cut_cube(
    target=main,
    scale=(500, 500, MAIN_DEPTH),
    location=(0, 0, -MAIN_THICKNESS),
)

main.location = (0, 0, 0)
