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

main = base.create_cube(scale=(30.0, 8.0, MAIN_DEPTH))
base.add_cube(
    target=main,
    scale=(30.0, 2.0, 2.0),
    location=(0, 0, MAIN_THICKNESS/2),
)

base.add_cube(
    target=main,
    scale=(8.0, 40.0, MAIN_DEPTH),
    location=(0, -20, 0),
)
base.add_cube(
    target=main,
    scale=(2.0, 40.0, 2.0),
    location=(0, -20, MAIN_THICKNESS/2),
)


X = 20.5/2
Y = 13.5/2

def camera_mount():
    mount = base.create_cube(scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH))
    mount.location=(0, -2.75, 0)
    positions = [
        (X, Y),
        (-X, Y),
        (X, -Y),
        (-X, -Y),
    ]
    for i, (x, y) in enumerate(positions):
        base.cut_cylinder(
            target=mount,
            radius=1.1,
            depth=MAIN_THICKNESS * 2,
            location=(x, y, 0),
        )
    mount.location=(0, 0, 0)
    return mount

##############################################

v1 = camera_mount()
v1.location=(-27.7, 0, 0)

##############################################

v3 = camera_mount()
v3.location=(27.7, 0, 0)

##############################################


base.modifier_apply(obj=v1, target=main, operation="UNION")
base.modifier_apply(obj=v3, target=main, operation="UNION")
