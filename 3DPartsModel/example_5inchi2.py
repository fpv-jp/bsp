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

M186 = 18.3 / 2 #+ .25

MAIN_WIDTH = 30.5 
MAIN_HEIGHT = 30.5 
MAIN_DEPTH = 12.5


#-------------------------------------
main = base.create_cube(
    scale=(MAIN_WIDTH, MAIN_HEIGHT, MAIN_DEPTH),
)
#base.add_cylinder(
#    target=main,
#    radius=22.0,
#    depth=3.0,
#    vertices=8,
#    location=(0.0, 0.0, MAIN_DEPTH/2-1.5),
#)

##-------------------------------------
P1 = 20.5 / 2  
for i, (x,y) in enumerate([(P1,P1),(-P1,P1),(P1,-P1),(-P1,-P1)]):
    base.add_ring(
        target=main,
        outer_radius=M186 + 2.0,
        inner_radius=M186,
        depth=MAIN_DEPTH,
        location=(x, y, 0.0),
    )

main.rotation_euler[2] = math.pi / 4

P1 = 24.6
for i, (x,y) in enumerate([(P1,0),(-P1,0),(0,P1),(-0,-P1)]):
    base.cut_cube(
        target=main,
        scale=(
            2.2,
            2.2,
            MAIN_DEPTH*2,
        ),
        location=(x, y, 0),
    )

##-------------------------------------

base.add_cylinder(
    target=main,
    radius=14.0,
    depth=2.0,
    vertices=8,
    location=(0.0, 0.0, MAIN_DEPTH/2-1.0),
)
P = 10.0
for i, (x,y) in enumerate([(P,0),(-P,0),(0,P),(0,-P)]):
    base.cut_cylinder(
        target=main,
        radius=1.25,
        depth=MAIN_DEPTH*2,
        location=(x, y, 0.0),
    )

##-------------------------------------

base.cut_cylinder(
    target=main,
    radius=1.75,
    depth=MAIN_DEPTH,
)
base.cut_cylinder(
    target=main,
    radius=3.7,
    depth=MAIN_DEPTH,
    location=(0.0, 0.0, 3.0),
)

##-------------------------------------

main.rotation_euler[2] = 0

#P = 19.0
#M = 1.25
#for i, (x,y) in enumerate([(P,0),(-P,0),(0,P),(0,-P)]):
#    base.cut_cylinder(
#        target=main,
#        radius=M,
#        depth=MAIN_DEPTH*2,
#        location=(x, y, 0.0),
#    )

#main.rotation_euler[0] = math.pi
