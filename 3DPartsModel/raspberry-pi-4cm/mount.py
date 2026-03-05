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

CM4_WIDTH = 48.5
CM4_HEIGHT = 25.0
CM4_DEPTH = 2.0

CM4_THICKNESS = 1.5

Z = CM4_DEPTH + CM4_THICKNESS

main = base.create_cube(scale=(CM4_WIDTH, CM4_HEIGHT, Z))

X_POS = 16.0
M = 9.0

base.cut_cylinder(target=main, radius=M / 2, depth=Z, location=(X_POS, 0, 0))
base.cut_cube(target=main, scale=(M, M, Z), location=(X_POS + M / 2, 0, 0))

X_POS = 24.5
RAD = 20.0
scale = (11, 42, Z)

base.cut_cube(target=main, scale=scale, location=(X_POS, 0, 0), rotation=(0, 0, math.radians(RAD)))
base.cut_cube(
    target=main, scale=scale, location=(-X_POS, 0, 0), rotation=(0, 0, math.radians(-RAD))
)

base.cut_cube(target=main, scale=scale, location=(21.0, 0, 0))
base.cut_cube(target=main, scale=scale, location=(-21.0, 0, 0))

X = 8.0
Y = -4.0

base.cut_holes(
    target=main,
    radius=1.75,
    depth=Z,
    positions=[(X, Y), (-X, Y)],
)

### ----------------------------------------------------------------------------------------------------------------

main.rotation_euler[0] = math.radians(-75)
main.location = (0.0, 8.0, 13.0)

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
X_PITCH = 15.25
base.cut_holes(
    target=hexagonal_plate,
    radius=M3,
    depth=5,
    positions=[(X_PITCH, 0), (-X_PITCH, 0)],
)

### ----------------------------------------------------------------------------------------------------------------

base.join(target=main, obj=hexagonal_plate)
