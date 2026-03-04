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
CM4_DEPTH = 5.4

CM4_THICKNESS = 1.5

main = base.create_cube(
    scale=(59.2, 44.1, 6.9),
)

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

base.cut_corners(
    target=main,
    width=56.2,
    height=41.1,
    depth=5.4,
    thickness=1.5,
)

base.cut_holes(
    target=main,
    radius=2.5,
    depth=5.4,
    z=0.75,
    positions=[(25.61, 18.06), (-25.61, 18.06), (25.61, -18.06), (-25.61, -18.06)],
)

base.cut_cube(
    target=main,
    scale=(51.2, 41.1, 5.4),
    location=(0, 0, 0.75),
)
base.cut_cube(
    target=main,
    scale=(56.2, 36.1, 5.4),
    location=(0, 0, 0.75),
)
main.rotation_euler[0] = math.radians(180)
main.location[2] = 3.45

### ----------------------------------------------------------------------------------------------------------------

# csi
base.cut_cube(
    target=main,
    scale=(22.7, 2.8, 10.0),
    location=(0.95, -16.55, 4.9),
)
# dsi
base.cut_cube(
    target=main,
    scale=(22.7, 2.8, 10.0),
    location=(0.95, -8.55, 4.9),
)

# wifi

# ----pin
base.add_cube(
    target=main,
    scale=(35.1, 3.0, 1.2),
    location=(10.15, 17.0, 5.6),
)
base.add_cube(
    target=main,
    scale=(35.1, 3.0, 1.2),
    location=(10.15, 1.0, 5.6),
)
base.add_cube(
    target=main,
    scale=(3.0, 32.4, 1.2),
    location=(-0.85, 9.5, 5.6),
)
base.add_cube(
    target=main,
    scale=(3.0, 32.4, 1.2),
    location=(21.15, 9.5, 5.6),
)
# ----cut
base.cut_cube(
    target=main,
    scale=(32.1, 32.4, 10.0),
    location=(10.15, 11.0, 4.9),
)

# ----wifi-ptate
base.add_cube(
    target=main,
    scale=(32.1, 32.4, 0.75),
    location=(10.15, 11.0, 6.525),
)
base.cut_cube(
    target=main,
    scale=(56.2, 41.1, 10.0),
    location=(0, 42.6, 4.9),
)

# ----wifi-ptate-cut
base.cut_cube(
    target=main,
    scale=(11.0, 32.4, 10.0),
    location=(10.15, 11.0, 4.9),
)
base.cut_cube(
    target=main,
    scale=(29.5, 32.4, 10.0),
    location=(10.15, 17.5, 4.9),
)


### ----------------------------------------------------------------------------------------------------------------

# eth
base.cut_cube(
    target=main,
    scale=(16.7, 14.6, 10.0),
    location=(-18.45, 14.75, 4.9),
)

### ----------------------------------------------------------------------------------------------------------------

# usb-A
base.cut_cube(
    target=main,
    scale=(13.4, 10.2, 10.0),
    location=(-18.6, -16.95, 4.9),
)

# usb-A2
base.cut_cube(
    target=main,
    scale=(14.6, 2.3, 10.0),
    location=(-18.7, -11.6, 4.9),
)

# hdmi
base.cut_cube(
    target=main,
    scale=(11.5, 7.5, 3.1),
    location=(20.85, -20.55, 1.45),
)

### ----------------------------------------------------------------------------------------------------------------

# switch1
base.cut_cube(
    target=main,
    scale=(4.3, 6.2, 3.4),
    location=(-28.1, -6.65, 1.6),
)

### ----------------------------------------------------------------------------------------------------------------

# switch2
base.cut_cube(
    target=main,
    scale=(5.1, 8.5, 2.1),
    location=(28.1, -7.9, 0.95),
)

# audio
base.cut_cube(
    target=main,
    scale=(14.1, 5.2, 5.0),
    location=(28.1, 7.35, 2.4),
)

main.rotation_euler[0] = math.radians(0)
