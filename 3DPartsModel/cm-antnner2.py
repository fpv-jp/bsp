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

# 初期化
base.init()

frame_thickness = 2.0

#########################################

M3 = 2.3

PITCH = 27.2

frame = base.create_cube(
    scale=(PITCH * 2, M3 * 4, frame_thickness),
)

holes = [PITCH, -PITCH]
for i, (x) in enumerate(holes):
    base.add_ring(
        target=frame,
        outer_radius=M3 * 2,
        inner_radius=M3,
        location=(x, 0, 0),
        depth=frame_thickness,
    )

frame.location = (0, 0, frame_thickness / 2)

################################################

OUTER = 7.0
INNER = 5.1
DEPTH = 11.5
DEPTH2 = 2.0
DEPTH3 = 6.0


def create_antenna():
    antenna = base.create_cube(scale=(OUTER * 2, OUTER, DEPTH), location=(0, OUTER / 2, 0))
    base.add_ring(target=antenna, outer_radius=OUTER, inner_radius=INNER, depth=DEPTH)
    base.add_ring(
        target=antenna,
        outer_radius=OUTER,
        inner_radius=3.25,
        depth=DEPTH2,
        location=(0, 0, (DEPTH - DEPTH2) / 2),
    )
    base.cut_cube(
        target=antenna,
        scale=(OUTER * 2, OUTER * 2, DEPTH3),
        location=(0, -DEPTH3, 0),
    )
    antenna.rotation_euler[0] = -math.pi / 2
    antenna.rotation_euler[2] = math.pi
    return antenna


X = 15.5
Y = 7.0

right = create_antenna()
right.location = (X, Y, OUTER)

left = create_antenna()
left.location = (-X, Y, OUTER)

base.modifier_apply(obj=right, target=frame, operation="UNION")
base.modifier_apply(obj=left, target=frame, operation="UNION")
