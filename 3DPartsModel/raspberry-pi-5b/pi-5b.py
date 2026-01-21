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

base.init()

MAIN_WIDTH = 85.0
MAIN_HEIGHT = 56.0

MAIN_DEPTH_BOTTOM = 14.7
MAIN_DEPTH_TOP = 7.8

MAIN_DEPTH = MAIN_DEPTH_TOP + MAIN_DEPTH_BOTTOM


MAIN_THICKNESS = 2.0

main = base.create_cube(
    scale=(MAIN_WIDTH + MAIN_THICKNESS, MAIN_HEIGHT + MAIN_THICKNESS, MAIN_DEPTH),
)

BASE_X = MAIN_WIDTH / 2
BASE_Y = MAIN_HEIGHT / 2

M2_7 = 1.35

positions = [
    (BASE_X, BASE_Y),
    (-BASE_X, BASE_Y),
    (BASE_X, -BASE_Y),
    (-BASE_X, -BASE_Y),
]
for i, (x, y) in enumerate(positions):
    base.cut_cube(
        target=main,
        scale=(M2_7 * 2, M2_7 * 2, MAIN_DEPTH),
        location=(x, y, 0),
    )


positions = [
    (BASE_X - M2_7, BASE_Y - M2_7),
    (BASE_X - M2_7, -BASE_Y + M2_7),
    (-BASE_X + M2_7, BASE_Y - M2_7),
    (-BASE_X + M2_7, -BASE_Y + M2_7),
]
for i, (x, y) in enumerate(positions):
    base.add_cylinder(
        target=main,
        radius=M2_7 * 1.74,
        depth=MAIN_DEPTH,
        location=(x, y, 0),
    )
    base.cut_cylinder(
        target=main,
        radius=M2_7 + 0.1,
        depth=MAIN_DEPTH - MAIN_THICKNESS,
        location=(x, y, 0),
    )


GAP1 = -M2_7 * 2
GAP2 = 0.2

positions = [
    (MAIN_WIDTH + GAP1, MAIN_HEIGHT + GAP2),
    (MAIN_WIDTH + GAP2, MAIN_HEIGHT + GAP1),
]
for i, (x, y) in enumerate(positions):
    base.cut_cube(
        target=main,
        scale=(x, y, MAIN_DEPTH - MAIN_THICKNESS),
    )


##################################################

X = 29.0
Y = 24.5

main.location = (BASE_X - X - 3.5, 0, 0)

positions = [
    (X, Y),
    (-X, Y),
    (X, -Y),
    (-X, -Y),
]
for i, (x, y) in enumerate(positions):
    base.add_cylinder(
        target=main,
        radius=M2_7 + 1,
        depth=MAIN_THICKNESS,
        location=(x, y, MAIN_DEPTH / 2 - MAIN_THICKNESS),
    )

for i, (x, y) in enumerate(positions):
    base.cut_cylinder(
        target=main,
        radius=M2_7,
        depth=MAIN_DEPTH,
        location=(x, y, 0),
    )

base.cut_cube(
    target=main,
    scale=(1, 35, 20),
    location=(X - 5.5, MAIN_HEIGHT / 2, -MAIN_DEPTH / 2),
)
base.cut_cube(
    target=main,
    scale=(1, 35, 20),
    location=(X - 11.5, MAIN_HEIGHT / 2, -MAIN_DEPTH / 2),
)

base.cut_cube(
    target=main,
    scale=(20.0, 20.0, MAIN_THICKNESS),
    location=(-1.0, 1.0, -MAIN_DEPTH / 2),
)

base.cut_cube(
    target=main,
    scale=(52.2, 6.3, MAIN_THICKNESS),
    location=(0, -Y, -MAIN_DEPTH / 2),
)

main.location = (0, 0, 0)


#################################################


BASE_Z = (MAIN_DEPTH - MAIN_THICKNESS) / 2


def cube_cut3(scale, Y):
    X = -BASE_X + scale[0] / 2 - 1
    Z = BASE_Z - scale[2] / 2 + 1
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, -Z),
    )


cube_cut3(scale=(7.0, 9.0, 7.5), Y=-2.0)  # NVMe (AI Hat)

#################################################


BASE_Z = (MAIN_DEPTH - MAIN_THICKNESS) / 2 - 3.5


def cube_cut(scale, Y):
    X = BASE_X - scale[0] / 2 + 1
    Z = BASE_Z - scale[2] / 2
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut(scale=(20, 16.2, 13.3), Y=BASE_Y - 10.2)  # ETH

#################################################


def cube_cut1(scale, Y):
    X = BASE_X - scale[0] / 2 + 1
    Z = BASE_Z - scale[2] / 2 - 0.5
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut1(scale=(10, 13.2, 15.2), Y=BASE_Y - 29.1)  # USB
cube_cut1(scale=(10, 13.2, 15.2), Y=BASE_Y - 47.0)  # USB


###############################################


def cube_cut2(scale, X):
    Y = BASE_Y - scale[1] / 2 + 1
    Z = BASE_Z - scale[2] / 2
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut2(scale=(9.1, 10.0, 3.8), X=-BASE_X + 11.2)  # USB-C Power
cube_cut2(scale=(7.1, 10.0, 4.1), X=-BASE_X + 25.8)  # Micro HDMI
cube_cut2(scale=(7.1, 10.0, 4.1), X=-BASE_X + 39.2)  # Micro HDMI


###############################################


def cube_cut6(scale, X):
    Y = BASE_Y - scale[1] / 2 + 10
    Z = BASE_Z - scale[2] / 2 - 7
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut6(scale=(3.0, 10.0, 1.8), X=-BASE_X + 18.5)  # RTC Battery
cube_cut6(scale=(4.5, 10.0, 1.8), X=-BASE_X + 32.5)  # UART


################################################


def cube_cut5(scale, Y):
    X = -BASE_X + scale[0] / 2 - 1
    Z = BASE_Z - scale[2] / 2
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut5(scale=(20, 2.0, 1.2), Y=BASE_Y - 13.3)  # LED
cube_cut5(scale=(20, 3.0, 3.0), Y=BASE_Y - 18.4)  # Switch


###############################################


def cube_cut4(scale, Y):
    X = -BASE_X + scale[0] / 2 - 1
    Z = BASE_Z - scale[2] / 2 + 3.5
    base.cut_cube(
        target=main,
        scale=scale,
        location=(X, Y, Z),
    )


cube_cut4(scale=(20, 12.0, 1.75), Y=0)  # SD Card


###############################################


# ===============================
# base.cut_cube(target=main,
# scale=(
#    MAIN_WIDTH+MAIN_THICKNESS*2 ,
#    MAIN_HEIGHT+MAIN_THICKNESS*2 ,
#    MAIN_DEPTH_TOP,
# ),
# location=(
#    0,
#    0,
#    (MAIN_DEPTH-MAIN_DEPTH_TOP)/2,
# ),
# )

# ===============================
# base.cut_cube(target=main,
#    scale=(
#        MAIN_WIDTH+MAIN_THICKNESS*2 ,
#        MAIN_HEIGHT+MAIN_THICKNESS*2 ,
#        MAIN_DEPTH_BOTTOM,
#    ),
#    location=(
#        0,
#        0,
#        (-MAIN_DEPTH+MAIN_DEPTH_BOTTOM)/2,
#    ),
# )
# main.rotation_euler[1] = math.pi
