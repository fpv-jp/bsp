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

CM4_WIDTH = 56.2
CM4_HEIGHT = 41.1
CM4_DEPTH = 7.3

CM4_THICKNESS = 1.5

main = base.create_cube(scale=(59.2, 44.1, 8.8))

M = 1.25
X_ALL = (CM4_WIDTH + CM4_THICKNESS * 2) / 2 + 2.5
Y_ALL = (CM4_HEIGHT + CM4_THICKNESS * 2) / 2.75

W = M + CM4_THICKNESS

holes = [(X_ALL, Y_ALL), (X_ALL, -Y_ALL)]
for i, (x, y) in enumerate(holes):
    base.add_cube(
        target=main,
        scale=(W, W * 2, CM4_THICKNESS),
        location=(x - W / 2, y, -CM4_DEPTH / 2),
    )

holes = [(-X_ALL, Y_ALL), (-X_ALL, -Y_ALL)]
for i, (x, y) in enumerate(holes):
    base.add_cube(
        target=main,
        scale=(W, W * 2, CM4_THICKNESS),
        location=(x + W / 2, y, -CM4_DEPTH / 2),
    )

holes = [(X_ALL, Y_ALL), (-X_ALL, Y_ALL), (X_ALL, -Y_ALL), (-X_ALL, -Y_ALL)]
for i, (x, y) in enumerate(holes):
    base.add_ring(
        target=main,
        outer_radius=W,
        inner_radius=M,
        depth=CM4_THICKNESS,
        location=(x, y, -CM4_DEPTH / 2),
    )
# ----------------------------------------------------------------------------------------------------------------

#M = 1.75
#ARM = CM4_WIDTH + M * 6
#MAIN_THICKNESS = 2.5


#def bar():
#    b = base.create_cube(
#        scale=(
#            ARM,
#            M * 4,
#            MAIN_THICKNESS,
#        ),
#    )
#    for i, (x) in enumerate([ARM / 2, -ARM / 2]):
#        base.add_ring(
#            target=b,
#            outer_radius=M * 2,
#            inner_radius=M,
#            depth=MAIN_THICKNESS,
#            location=(x, 0.0, 0.0),
#        )
#    return b

#b = bar()
#b.location = (0.0, 0.0, -8.8/2 + MAIN_THICKNESS/2 )
#base.modifier_apply(obj=b, target=main, operation="UNION")
# ----------------------------------------------------------------------------------------------------------------

base.cut_corners(
    target=main,
    width=56.2,
    height=41.1,
    depth=7.3,
    thickness=1.5,
)

base.cut_holes(
    target=main,
    radius=2.5,
    depth=7.3,
    z=0.75,
    positions=[(25.61, 18.06), (-25.61, 18.06), (25.61, -18.06), (-25.61, -18.06)],
)

base.cut_cube(
    target=main,
    scale=(51.2, 41.1, 7.3),
    location=(0, 0, 0.75),
)
base.cut_cube(
    target=main,
    scale=(56.2, 36.1, 7.3),
    location=(0, 0, 0.75),
)
base.cut_cube(
    target=main,
    scale=(44.2, 29.1, 8.8),
)

# ----------------------------------------------------------------------------------------------------------------

base.add_ring(
    target=main,
    outer_radius=2.5,
    inner_radius=1.15,
    depth=2.8,
    location=(23.85, 16.4, -3.0),
)
base.add_ring(
    target=main,
    outer_radius=2.5,
    inner_radius=1.15,
    depth=2.8,
    location=(23.85, -16.4, -3.0),
)
base.add_ring(
    target=main,
    outer_radius=2.5,
    inner_radius=1.15,
    depth=2.8,
    location=(-23.85, 16.4, -3.0),
)
base.add_ring(
    target=main,
    outer_radius=2.5,
    inner_radius=1.15,
    depth=2.8,
    location=(-23.85, -16.4, -3.0),
)

# ----------------------------------------------------------------------------------------------------------------

base.add_triangle(
    target=main,
    verts=[(3.5, 0, 0), (0, 3.5, 0), (0, 0, 0)],
    depth=1.5,
    location=(-22.25, 15.0, -4.4),
    rotation=(0, 0, math.radians(270)),
)
base.add_triangle(
    target=main,
    verts=[(3.5, 0, 0), (0, 3.5, 0), (0, 0, 0)],
    depth=1.5,
    location=(22.25, 15.0, -4.4),
    rotation=(0, 0, math.radians(180)),
)
base.add_triangle(
    target=main,
    verts=[(3.5, 0, 0), (0, 3.5, 0), (0, 0, 0)],
    depth=1.5,
    location=(22.25, -15.0, -4.4),
    rotation=(0, 0, math.radians(90)),
)
base.add_triangle(
    target=main,
    verts=[(3.5, 0, 0), (0, 3.5, 0), (0, 0, 0)],
    depth=1.5,
    location=(-22.25, -15.0, -4.4),
    rotation=(0, 0, math.radians(0)),
)

# ----------------------------------------------------------------------------------------------------------------
main.location[2] = -4.4

# eth
base.cut_cube(
    target=main,
    scale=(16.7, 4.5, 3.2),
    location=(-18.45, 20.55, -1.5),
)

# usb-c
base.cut_cube(
    target=main,
    scale=(11.2, 4.5, 3.8),
    location=(20.5, 20.55, -1.8),
)

# audio
base.cut_cube(
    target=main,
    scale=(14.1, 5.2, 0.5),
    location=(28.1, 7.35, -0.15),
)

# ----------------------------------------------------------------------------------------------------------------

base.add_cube(
    target=main,
    scale=(20.8, 1.5, 5.4),
    location=(4.5, 21.3, 2.2),
)
