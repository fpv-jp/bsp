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

### ----------------------------------------------------------------------------------------------------------------
Z = 10.0

# csi
X = 22.7
Y = 2.8

POS_X = (CM4_WIDTH - X) / 2 - 15.8
POS_Y = CM4_THICKNESS - CM4_HEIGHT / 2

base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        POS_X,
        POS_Y + 2.5,
        Z / 2 - 0.1,
    ),
)
# dsi
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        POS_X,
        POS_Y + 10.5,
        Z / 2 - 0.1,
    ),
)

# wifi
X = 32.1
Y = 32.4

POS_X = 10.15
POS_Y = 11.0
POS_Z = CM4_DEPTH - 0.8

PIN = 3.5

base.add_cube(
    target=main,
    scale=(X + CM4_THICKNESS * 2, CM4_THICKNESS * 2, PIN),
    location=(POS_X, POS_Y + 6.0, POS_Z),
)
base.add_cube(
    target=main,
    scale=(X + CM4_THICKNESS * 2, CM4_THICKNESS * 2, PIN),
    location=(POS_X, POS_Y - 10.0, POS_Z),
)

YY = POS_Y - CM4_THICKNESS
ZZ = CM4_DEPTH - 0.8

base.add_cube(
    target=main,
    scale=(CM4_THICKNESS * 2, Y, PIN),
    location=(POS_X - 11.0, YY, POS_Z),
)
base.add_cube(
    target=main,
    scale=(CM4_THICKNESS * 2, Y, PIN),
    location=(POS_X + 11.0, YY, POS_Z),
)

base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        POS_X,
        POS_Y,
        Z / 2 - 0.1,
    ),
)

ZZZ = 0.75
ZZZZ = CM4_DEPTH + CM4_THICKNESS - ZZZ / 2

base.add_cube(
    target=main,
    scale=(X, Y, ZZZ),
    location=(
        POS_X,
        POS_Y,
        ZZZZ,
    ),
)
base.cut_cube(
    target=main,
    scale=(11.0, Y, Z),
    location=(
        POS_X,
        POS_Y,
        Z / 2 - 0.1,
    ),
)
base.cut_cube(
    target=main,
    scale=(29.5, Y, Z),
    location=(
        POS_X,
        POS_Y + 6.5,
        Z / 2 - 0.1,
    ),
)

base.cut_cube(
    target=main,
    scale=(CM4_WIDTH, CM4_HEIGHT, Z),
    location=(
        0,
        CM4_HEIGHT + CM4_THICKNESS,
        Z / 2 - 0.1,
    ),
)


### ----------------------------------------------------------------------------------------------------------------

# eth
X = 16.7
Y = 14.6

base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        (X - CM4_WIDTH) / 2 + 1.3,
        (CM4_HEIGHT - Y) / 2 + CM4_THICKNESS,
        Z / 2 - 0.1,
    ),
)

### ----------------------------------------------------------------------------------------------------------------

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

### ----------------------------------------------------------------------------------------------------------------

# switch1
X = 4.3
Y = 6.2
Z = 3.4
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        -CM4_WIDTH / 2,
        (Y - CM4_HEIGHT) / 2 + 10.8,
        Z / 2 - 0.1,
    ),
)

### ----------------------------------------------------------------------------------------------------------------

# switch2
X = 5.1
Y = 8.5
Z = 2.1
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        CM4_WIDTH / 2,
        (Y - CM4_HEIGHT) / 2 + 8.4,
        Z / 2 - 0.1,
    ),
)

# audio
X = 14.1
Y = 5.2
Z = 5.0
base.cut_cube(
    target=main,
    scale=(X, Y, Z),
    location=(
        CM4_WIDTH / 2,
        (-Y + CM4_HEIGHT) / 2 - 10.6,
        Z / 2 - 0.1,
    ),
)

main.rotation_euler[0] = math.radians(0)
