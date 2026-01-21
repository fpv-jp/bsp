import bpy
import bmesh

# =============================================================================
# Naming Convention
# =============================================================================
# create_* : Create new object and return it
# add_*    : Add to target (Boolean UNION)
# cut_*    : Subtract from target (Boolean DIFFERENCE)
#
# Parameter Order:
# 1. target (if applicable)
# 2. shape params (scale, radius, depth, vertices, etc.)
# 3. location, rotation
# 4. name (optional)
# =============================================================================

# fmt: off

def init():
    """Clear all objects in the scene."""
    for area in bpy.context.screen.areas:
        if area.type == "VIEW_3D":
            with bpy.context.temp_override(area=area):
                bpy.ops.object.select_all(action="SELECT")
                bpy.ops.object.delete()
            break
    else:
        raise RuntimeError("No 3D View found. Please run the script in a 3D View.")


def _apply_boolean(target, obj, operation, name):
    """Apply boolean modifier and remove the tool object."""
    modifier = target.modifiers.new(name=name, type="BOOLEAN")
    modifier.operation = operation
    modifier.solver = "EXACT"
    modifier.use_self = True
    modifier.double_threshold = 0.0001
    modifier.object = obj
    bpy.context.view_layer.objects.active = target
    bpy.ops.object.modifier_apply(modifier=modifier.name)
    bpy.data.objects.remove(obj, do_unlink=True)


# =============================================================================
# Cube
# =============================================================================

def create_cube(scale, location=(0, 0, 0), rotation=(0, 0, 0), name="Cube"):
    """Create a cube and return it."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(scale=True)
    return obj


def add_cube(target, scale, location=(0, 0, 0), rotation=(0, 0, 0), name="add_cube"):
    """Add a cube to target (UNION)."""
    bpy.ops.mesh.primitive_cube_add(size=1, scale=scale, location=location, rotation=rotation)
    _apply_boolean(target, bpy.context.active_object, "UNION", name)


def cut_cube(target, scale, location=(0, 0, 0), rotation=(0, 0, 0), name="cut_cube"):
    """Cut a cube from target (DIFFERENCE)."""
    bpy.ops.mesh.primitive_cube_add(size=1, scale=scale, location=location, rotation=rotation)
    _apply_boolean(target, bpy.context.active_object, "DIFFERENCE", name)


# =============================================================================
# Cylinder (vertices=32: circle, vertices=6: hexagon)
# =============================================================================

def create_cylinder(radius, depth, location=(0, 0, 0), rotation=(0, 0, 0), vertices=32, name="Cylinder"):
    """Create a cylinder and return it."""
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, vertices=vertices, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    bpy.ops.object.transform_apply(scale=True)
    return obj


def add_cylinder(target, radius, depth, location=(0, 0, 0), rotation=(0, 0, 0), vertices=32, name="add_cylinder"):
    """Add a cylinder to target (UNION)."""
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, vertices=vertices, location=location, rotation=rotation)
    _apply_boolean(target, bpy.context.active_object, "UNION", name)


def cut_cylinder(target, radius, depth, location=(0, 0, 0), rotation=(0, 0, 0), vertices=32, name="cut_cylinder"):
    """Cut a cylinder from target (DIFFERENCE)."""
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, vertices=vertices, location=location, rotation=rotation)
    _apply_boolean(target, bpy.context.active_object, "DIFFERENCE", name)


# =============================================================================
# Triangle
# =============================================================================

def _create_triangle_mesh(verts, depth, location, rotation):
    """Internal: create extruded triangle mesh."""
    mesh = bpy.data.meshes.new("Triangle_Mesh")
    bm = bmesh.new()
    face = bm.faces.new([bm.verts.new(v) for v in verts])
    bm.normal_update()
    extruded = bmesh.ops.extrude_face_region(bm, geom=[face])
    extruded_verts = [e for e in extruded["geom"] if isinstance(e, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, verts=extruded_verts, vec=(0, 0, depth))
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new("Triangle_Temp", mesh)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    obj.rotation_euler = rotation
    return obj


def add_triangle(target, verts, depth, location=(0, 0, 0), rotation=(0, 0, 0), name="add_triangle"):
    """Add a triangle to target (UNION)."""
    obj = _create_triangle_mesh(verts, depth, location, rotation)
    _apply_boolean(target, obj, "UNION", name)


def cut_triangle(target, verts, depth, location=(0, 0, 0), rotation=(0, 0, 0), name="cut_triangle"):
    """Cut a triangle from target (DIFFERENCE)."""
    obj = _create_triangle_mesh(verts, depth, location, rotation)
    _apply_boolean(target, obj, "DIFFERENCE", name)


# =============================================================================
# Composite Shapes
# =============================================================================

def add_ring(target, outer_radius, inner_radius, depth, location=(0, 0, 0), rotation=(0, 0, 0), vertices=32, name="add_ring"):
    """Add a ring (cylinder with hole) to target."""
    add_cylinder(target, outer_radius, depth, location, rotation, vertices, f"{name}_outer")
    cut_cylinder(target, inner_radius, depth + 1, location, rotation, vertices, f"{name}_inner")


def add_frame(target, inner, thickness, location=(0, 0, 0), rotation=(0, 0, 0), name="add_frame"):
    """Add a square frame to target."""
    outer = inner + thickness * 2
    add_cube(target, (outer, outer, thickness), location, rotation, f"{name}_outer")
    cut_cube(target, (inner, inner, thickness + 1), location, rotation, f"{name}_inner")


# =============================================================================
# Batch Operations
# =============================================================================

def add_plates(target, plates, name="add_plates"):
    """Add multiple cubes. plates: [(scale, location, rotation), ...]"""
    for i, (scale, loc, rot) in enumerate(plates):
        add_cube(target, scale, loc or (0, 0, 0), rot or (0, 0, 0), f"{name}_{i}")


def cut_plates(target, plates, name="cut_plates"):
    """Cut multiple cubes. plates: [(scale, location, rotation), ...]"""
    for i, (scale, loc, rot) in enumerate(plates):
        cut_cube(target, scale, loc or (0, 0, 0), rot or (0, 0, 0), f"{name}_{i}")


def add_pins(target, radius, depth, positions, z=0, rotation=(0, 0, 0), vertices=32, name="add_pins"):
    """Add multiple cylinders. positions: [(x, y), ...]"""
    for i, (x, y) in enumerate(positions):
        add_cylinder(target, radius, depth, (x, y, z), rotation, vertices, f"{name}_{i}")


def cut_holes(target, radius, depth, positions, z=0, rotation=(0, 0, 0), vertices=32, name="cut_holes"):
    """Cut multiple cylinders. positions: [(x, y), ...]"""
    for i, (x, y) in enumerate(positions):
        cut_cylinder(target, radius, depth, (x, y, z), rotation, vertices, f"{name}_{i}")


def cut_corners(target, width, height, depth, thickness):
    """Cut corners and add rounded pins."""
    x, y = width / 2, height / 2
    px, py = x + thickness, y + thickness
    s = (thickness * 2, thickness * 2, depth + thickness)
    cut_plates(target, [(s, (px, py, 0), None), (s, (px, -py, 0), None), (s, (-px, py, 0), None), (s, (-px, -py, 0), None)])
    add_pins(target, thickness, depth + thickness, [(x, y), (x, -y), (-x, y), (-x, -y)])


# =============================================================================
# Object Operations
# =============================================================================

def modifier_apply(obj, target, operation="UNION", name="modifier_apply"):
    """Apply boolean modifier between two objects."""
    _apply_boolean(target, obj, operation, name)


def join(target, obj):
    """Join two objects into one."""
    bpy.context.view_layer.objects.active = target
    target.select_set(True)
    obj.select_set(True)
    bpy.ops.object.join()

# fmt: on
