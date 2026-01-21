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

CM4_WIDTH = 55.4
CM4_HEIGHT = 40.3
CM4_DEPTH = 4.4

CM4_THICKNESS = 1.5

main = base.create_cube(
    scale=(
        CM4_WIDTH + CM4_THICKNESS * 2,
        CM4_HEIGHT + CM4_THICKNESS * 2,
        CM4_DEPTH + CM4_THICKNESS,
    ),
)

base.cut_corners(
    target=main,
    width=CM4_WIDTH,
    height=CM4_HEIGHT,
    depth=CM4_DEPTH,
    thickness=CM4_THICKNESS,
)

X = CM4_WIDTH / 2 - CM4_THICKNESS * 1.66
Y = CM4_HEIGHT / 2 - CM4_THICKNESS * 1.66
base.cut_holes(
    target=main,
    radius=2.5,
    depth=CM4_DEPTH,
    z=CM4_THICKNESS / 2,
    positions=[(X, Y), (-X, Y), (X, -Y), (-X, -Y)],
)

base.cut_cube(
    target=main,
    scale=(CM4_WIDTH - 5, CM4_HEIGHT, CM4_DEPTH),
    location=(0, 0, CM4_THICKNESS / 2),
)
base.cut_cube(
    target=main,
    scale=(CM4_WIDTH, CM4_HEIGHT - 5, CM4_DEPTH),
    location=(0, 0, CM4_THICKNESS / 2),
)
main.rotation_euler[0] = math.radians(180)
main.location[2] = (CM4_DEPTH + CM4_THICKNESS) / 2

#### ----------------------------------------------------------------------------------------------------------------
Z = 10.0

M = 7.5

base.cut_cylinder(
    target=main, radius=M, depth=Z, location=(-CM4_WIDTH / 2 + M + 22.25, 0, CM4_DEPTH / 2)
)

#### ----------------------------------------------------------------------------------------------------------------

# usb-C
X = 9.1
Y = 7.0
Z = 3.4

base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        (CM4_WIDTH - X) / 2 - 3.6,
        (CM4_HEIGHT - Y) / 2 + CM4_THICKNESS,
        Z / 2 - 0.1,
    ),
)

# switch-1
X = 6.3
Y = 4.4
Z = 3.3

base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        (X - CM4_WIDTH) / 2 + 2.2,
        (CM4_HEIGHT - Y) / 2 + CM4_THICKNESS,
        Z / 2 - 0.1,
    ),
)

### ----------------------------------------------------------------------------------------------------------------
Z = 10.0

# usb-A
X = 13.4
Y = 10.2
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        (X - CM4_WIDTH) / 2 + 2.8,
        (Y - CM4_HEIGHT) / 2 - CM4_THICKNESS,
        Z / 2 - 0.1,
    ),
)

# usb-A2
X = 14.6
Y = 2.3
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        (X - CM4_WIDTH) / 2 + 2.1,
        (Y - CM4_HEIGHT) / 2 + 7.8,
        Z / 2 - 0.1,
    ),
)

# hdmi
X = 11.5
Y = 7.5
Z = 3.1
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        (CM4_WIDTH - X) / 2 - 1.5,
        -CM4_HEIGHT / 2,
        Z / 2 - 0.1,
    ),
)

# dsi
X = 19.1
Y = 6.9
Z = 1.8
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        1.85,
        -CM4_HEIGHT / 2,
        Z / 2 - 0.1,
    ),
)
# 35.2
# 38.9

#### ----------------------------------------------------------------------------------------------------------------

# switch2
X = 8.4
Y = 8.6
Z = 2.1
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        -CM4_WIDTH / 2,
        (CM4_HEIGHT - Y) / 2 - 13.4,
        Z / 2 - 0.1,
    ),
)

### ----------------------------------------------------------------------------------------------------------------

# switch2
X = 5.1
Y = 11.3
Z = 1.7
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        CM4_WIDTH / 2,
        (CM4_HEIGHT - Y) / 2 - 13.5,
        Z / 2 - 0.1,
    ),
)


main.rotation_euler[0] = math.radians(0)
