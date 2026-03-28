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

inner_box_size = 19.9
frame_thickness = 1.5
frame_depth = 7.5

frame = base.create_cube(
    scale=(
        inner_box_size + frame_thickness,
        inner_box_size + frame_thickness,
        frame_depth,
    ),
)

base.add_cube(
    target=frame,
    scale=(34.0, inner_box_size, frame_thickness),
    location=(0, 0, (frame_thickness-frame_depth)/2),
)

base.cut_cube(
    target=frame,
    scale=(inner_box_size, inner_box_size, frame_depth),
    location=(0, 0, frame_thickness),
)
base.cut_cube(
    target=frame,
    scale=(14.0, 14.0, 14.0),
)
base.cut_cube(
    target=frame,
    scale=(9.0, 8.0, 10),
    location=(0, -9.0, 0),
)

########################################

M3 = 1.75
z = (frame_depth - frame_thickness) / 2

PITCH = 16.4
y = 10.0

base.add_cube(
    target=frame,
    scale=(PITCH * 2, M3 * 4, frame_thickness),
    location=(0, y, -z),
)

holes = [(-PITCH, y), (PITCH, y)]
for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=frame,
        outer_radius=M3 * 2,
        inner_radius=M3,
        location=(x, y, -z),
        depth=frame_thickness,
    )

##########################################

depth_antenna = 10
radius_antenn = 7.5

antenna = base.create_cylinder(
    radius=radius_antenn,
    depth=depth_antenna,
)


base.cut_cylinder(
    target=antenna,
    radius=radius_antenn - frame_thickness,
    location=(0, 0, -frame_thickness),
    depth=depth_antenna - frame_thickness,
)

base.cut_cylinder(
    target=antenna,
    radius=3.25,
    depth=depth_antenna + 1,
)

antenna.location = (0, 21, -3)
antenna.rotation_euler = (-math.pi / 6, 0, 0)

base.modifier_apply(obj=antenna, target=frame)

base.cut_cube(
    target=frame,
    scale=(60, 60, 10),
    location=(0, 0, -frame_depth/2-5),
)

#############################################

erls = 5
erls_depth = 7.5

x = 11.1
y = 17.5

def create_erls():
    e = base.create_cube(
        scale=(erls + frame_thickness * 2, erls + frame_thickness * 2, erls_depth),
    )
    base.cut_cube(
        target=e,
        scale=(erls, erls, erls_depth + 0.5),
    )
    base.cut_cube(
        target=e,
        scale=(erls, erls, erls_depth),
        location=(frame_thickness, 0, frame_thickness),
    )
    return e

# -----------

erls1 = create_erls()
erls2 = create_erls()

erls1.location = (x, y, 0)
erls2.location = (-x, y, 0)

erls2.rotation_euler = (0, 0, math.pi)

base.modifier_apply(obj=erls1, target=frame)
base.modifier_apply(obj=erls2, target=frame)

#############################################

frame.location=(0, 0, frame_depth/2)

#############################################

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
        location=(0, -frame_depth, 0),
    )
    antenna.rotation_euler[0] = -math.pi / 2
    antenna.rotation_euler[2] = math.pi 
    return antenna


X = inner_box_size/2+OUTER+frame_thickness/2
Y = -13.0

right = create_antenna()
right.location = (X, Y, OUTER)

left = create_antenna()
left.location = (-X, Y, OUTER)

base.modifier_apply(obj=right, target=frame, operation="UNION")
base.modifier_apply(obj=left, target=frame, operation="UNION")
