import bpy
import bmesh
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
CM4_DEPTH = 2.0

CM4_THICKNESS = 1.5

Z = CM4_DEPTH + CM4_THICKNESS
main = base.create_cube(
    scale=(
        CM4_WIDTH + CM4_THICKNESS * 2,
        CM4_HEIGHT + CM4_THICKNESS * 2,
        Z,
    ),
)

base.cut_corners(
    target=main,
    width=CM4_WIDTH,
    height=CM4_HEIGHT,
    depth=CM4_DEPTH,
    thickness=CM4_THICKNESS,
)

base.add_cube(
    target=main,
    scale=(8, 25, Z),
    location=(-15, 25, 0),
    rotation=(0, 0, math.radians(-25)),
)
base.add_cube(
    target=main,
    scale=(8, 25, Z),
    location=(15, 25, 0),
    rotation=(0, 0, math.radians(25)),
)
base.add_cube(
    target=main,
    scale=(25, 25, Z),
    location=(0, 25, 0),
)

base.cut_cube(
    target=main,
    scale=(CM4_WIDTH - 12, CM4_HEIGHT - 12, CM4_DEPTH + CM4_THICKNESS),
)


M = 8.5
X_Width = 13.0

X_POS = 23.5
Y_POS = 28.5

base.cut_cube(
    target=main,
    scale=(X_Width, M, Z),
    location=(X_POS, Y_POS, 0),
)
base.cut_cylinder(
    target=main,
    radius=M / 2,
    depth=Z,
    location=(X_POS - X_Width / 2, Y_POS, 0),
)


base.add_cube(
    target=main,
    scale=(28.0, 4.5, 4.5),
    location=(0, 37.0, -2.5),
    rotation=(math.radians(30), 0, 0),
)


## ----------------------------------------------------------------------------------------------------------------

M = 2.3
X = (45.4 + M) / 2
Y = (30.5 + M) / 2

base.cut_holes(
    target=main,
    radius=1.25,
    depth=CM4_DEPTH + CM4_THICKNESS,
    positions=[(X, Y), (X, -Y), (-X, Y), (-X, -Y)],
)

## ----------------------------------------------------------------------------------------------------------------

x1 = 22.25
y1 = 15.0

t = [(3.5, 0, 0), (0, 3.5, 0), (0, 0, 0)]
triangle_positions = [
    (-x1, y1, t, 270),
    (x1, y1, t, 180),
    (x1, -y1, t, 90),
    (-x1, -y1, t, 0),
]

for i, (x, y, verts, rotation) in enumerate(triangle_positions):
    base.add_triangle(
        target=main,
        verts=verts,
        depth=CM4_DEPTH + CM4_THICKNESS,
        location=(x, y, (-CM4_THICKNESS - CM4_DEPTH) / 2),
        rotation=(0, 0, math.radians(rotation)),
    )


## ----------------------------------------------------------------------------------------------------------------

main.rotation_euler[0] = math.radians(-75)
main.location[2] = 37.4

### ----------------------------------------------------------------------------------------------------------------

BASE_PLATE_WIDTH = 40
BASE_PLATE_HEIGHT = 30
BASE_PLATE_THICKNESS = 2
CORNER_CUT_SIZE = 6.5

hexagonal_mesh = bpy.data.meshes.new("HexagonalPlate")
hexagonal_plate = bpy.data.objects.new("HexagonalPlate", hexagonal_mesh)
bpy.context.collection.objects.link(hexagonal_plate)
bmesh_obj = bmesh.new()

half_width = BASE_PLATE_WIDTH / 2
half_height = BASE_PLATE_HEIGHT / 2

hexagon_vertices = [
    # 上辺
    (-half_width + CORNER_CUT_SIZE, half_height, 0),
    (half_width - CORNER_CUT_SIZE, half_height, 0),
    # 右辺
    (half_width, half_height / 2 - CORNER_CUT_SIZE, 0),
    (half_width, -half_height / 2 + CORNER_CUT_SIZE, 0),
    # 下辺
    (half_width - CORNER_CUT_SIZE, -half_height, 0),
    (-half_width + CORNER_CUT_SIZE, -half_height, 0),
    # 左辺
    (-half_width, -half_height / 2 + CORNER_CUT_SIZE, 0),
    (-half_width, half_height / 2 - CORNER_CUT_SIZE, 0),
]

bmesh_vertices = []
for vertex in hexagon_vertices:
    bmesh_vertices.append(bmesh_obj.verts.new(vertex))

bmesh_obj.faces.new(bmesh_vertices)
extruded_geometry = bmesh.ops.extrude_face_region(bmesh_obj, geom=bmesh_obj.faces[:])
bmesh.ops.translate(
    bmesh_obj,
    vec=(0, 0, BASE_PLATE_THICKNESS),
    verts=[v for v in extruded_geometry["geom"] if isinstance(v, bmesh.types.BMVert)],
)

bmesh_obj.normal_update()
bmesh_obj.faces.ensure_lookup_table()
bmesh_obj.to_mesh(hexagonal_mesh)
bmesh_obj.free()

M3 = 1.75

base.cut_holes(
    target=hexagonal_plate,
    radius=M3,
    depth=5,
    positions=[(15.25, 0), (-15.25, 0)],
)

base.add_cube(
    target=hexagonal_plate,
    scale=(18.0, BASE_PLATE_THICKNESS, 6.5),
    location=(0, -(BASE_PLATE_HEIGHT - BASE_PLATE_THICKNESS) / 2, BASE_PLATE_THICKNESS),
)

hexagonal_plate.location[1] = -2.8
base.join(target=main, obj=hexagonal_plate)

## ----------------------------------------------------------------------------------------------------------------

base.cut_cube(
    target=main,
    scale=(CM4_WIDTH, CM4_HEIGHT, 10),
    location=(0, 0, -10 / 2),
)
