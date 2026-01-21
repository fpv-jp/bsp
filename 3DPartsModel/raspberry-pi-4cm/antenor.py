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


BASE_PLATE_WIDTH = 34.0
BASE_PLATE_HEIGHT = 22.0
BASE_PLATE_THICKNESS = 2

hexagonal_mesh = bpy.data.meshes.new("HexagonalPlate")
main = bpy.data.objects.new("HexagonalPlate", hexagonal_mesh)
bpy.context.collection.objects.link(main)
OBJ = bmesh.new()

W = BASE_PLATE_WIDTH / 2  # half width
H = BASE_PLATE_HEIGHT / 2  # half height
C = 4.5  # CORNER_CUT_SIZE

hexagon_vertices = [
    (-W + C + 2, H, 0),
    (W - C - 2, H, 0),
    (W, H / 2 - C, 0),
    (W, -H / 2 + C, 0),
    (W - C, -H, 0),
    (-W + C, -H, 0),
    (-W, -H / 2 + C, 0),
    (-W, H / 2 - C, 0),
]

VERTICES = []
for vertex in hexagon_vertices:
    VERTICES.append(OBJ.verts.new(vertex))
OBJ.faces.new(VERTICES)

GEOMETRY = bmesh.ops.extrude_face_region(OBJ, geom=OBJ.faces[:])
bmesh.ops.translate(
    OBJ,
    vec=(0, 0, BASE_PLATE_THICKNESS),
    verts=[v for v in GEOMETRY["geom"] if isinstance(v, bmesh.types.BMVert)],
)

OBJ.normal_update()
OBJ.faces.ensure_lookup_table()
OBJ.to_mesh(hexagonal_mesh)
OBJ.free()

##  ------------
x = 12.75
M3 = 1.8
base.cut_holes(
    target=main,
    radius=M3,
    depth=BASE_PLATE_THICKNESS + 2,
    positions=[(x, 0), (-x, 0)],
)

##  ------------

base.cut_cylinder(
    target=main,
    radius=3.25,
    depth=BASE_PLATE_THICKNESS + 2,
)

##  ------------

main.location = (0, -7.95, 0)
D = 6.0
base.add_ring(
    target=main,
    outer_radius=3.5 / 2 + 1.25,
    inner_radius=3.5 / 2,
    depth=D,
    location=(0, 0, D / 2),
)
base.cut_cylinder(
    target=main,
    radius=3.5 / 2,
    depth=7.0,
    location=(0, 0, D / 2 + 1),
    rotation=(0, math.pi / 2, 0),
)
base.cut_cube(
    target=main,
    scale=(7.0, 3.5, 4.0),
    location=(0, 0, D / 2 + BASE_PLATE_THICKNESS + 1),
)
base.cut_cube(
    target=main,
    scale=(1.1, 7.0, 15.0),
    location=(0, 3.5, 0),
)

##  ------------

xy = 20.15
z = 6.7

main.location = (0, 17.0, -(z + BASE_PLATE_THICKNESS) / 2)

base.add_cube(
    target=main,
    scale=(xy + BASE_PLATE_THICKNESS, xy + BASE_PLATE_THICKNESS + 0.2, z + BASE_PLATE_THICKNESS),
)
base.cut_cube(
    target=main,
    scale=(xy, xy, z),
    location=(0, 0, BASE_PLATE_THICKNESS),
)
base.cut_cube(
    target=main,
    scale=(9.0, 8.5, 10.0),
    location=(0, -xy / 2, 0),
)
