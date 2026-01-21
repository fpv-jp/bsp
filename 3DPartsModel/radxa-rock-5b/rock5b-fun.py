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

# 初期化
base.init()

# main -----------------------------------
MAIN_WIDTH = 31
MAIN_HEIGHT = 31
MAIN_THICKNESS = 1.5

main = base.create_cube(
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_THICKNESS),
)

base.cut_cube(
    target=main,
    scale=(26, 26, MAIN_THICKNESS + 1),
)

prop_x1 = 10
prop_y1 = 10
M3 = 1.75

POS = 1.3
holes = [
    (prop_x1, prop_y1, POS, POS, 4.75, 5.25),
    (-prop_x1, prop_y1, -POS, POS, 5.25, 4.75),
    (prop_x1, -prop_y1, POS, -POS, 5.25, 4.75),
#    (-prop_x1, -prop_y1, -POS, -POS, 4.75, 5.25),
]

for i, (x, y, a, b, n, m) in enumerate(holes):
    base.add_cylinder(
        target=main,
        radius=M3 * 1.55,
        depth=MAIN_THICKNESS,
        location=(x, y, 0),
        name=f"ring_outer_{i}",
    )
    base.add_cube(
        target=main,
        scale=(n, m, MAIN_THICKNESS),
        location=(x + a, y + b, 0),
        rotation=(0, 0, math.radians(45)),
        name=f"ring_tab_{i}",
    )
    base.cut_cylinder(
        target=main,
        radius=M3,
        depth=MAIN_THICKNESS + 1,
        location=(x, y, 0),
        name=f"ring_inner_{i}",
    )
#------------------
MAIN_WIDTH = (51.7+55.8)/2
MAIN_HEIGHT = (30.6+34.4)/2

main2 = base.create_cube(
    scale=(MAIN_WIDTH+MAIN_THICKNESS*3, MAIN_HEIGHT+MAIN_THICKNESS*3, MAIN_THICKNESS),
)

base.cut_cube(
    target=main2,
    scale=(MAIN_WIDTH-MAIN_THICKNESS, MAIN_HEIGHT-MAIN_THICKNESS, MAIN_THICKNESS),
)

M3 = 1.6

P_X1 =  MAIN_WIDTH/2
P_X2 =  -P_X1

P_Y1 =  MAIN_HEIGHT/2
P_Y2 =  -P_Y1

holes2 = [(P_X1, P_Y1), (P_X1, P_Y2), (P_X2, P_Y1),(P_X2, P_Y2)]

for i, (x, y) in enumerate(holes2):
    base.add_ring(
        target=main2,
        outer_radius=M3 * 2,
        inner_radius=M3,
        depth=MAIN_THICKNESS,
        location=(x, y, 0),
    )

main2.location=(8.0, 2.0, 0)

base.modifier_apply(obj=main2, target=main, operation="UNION")
