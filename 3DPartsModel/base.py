import bpy
import bmesh
import math

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


def create_cylinder_smooth(radius, depth, location=(0, 0, 0), rotation=(0, 0, 0), vertices=32, name="Cylinder"):
    """Create a cylinder with smooth shading and return it."""
    obj = create_cylinder(radius, depth, location=location, rotation=rotation, vertices=vertices, name=name)
    bpy.ops.object.shade_smooth()
    return obj


def add_cylinder(target, radius, depth, location=(0, 0, 0), rotation=(0, 0, 0), vertices=32, name="add_cylinder"):
    """Add a cylinder to target (UNION)."""
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, vertices=vertices, location=location, rotation=rotation)
    _apply_boolean(target, bpy.context.active_object, "UNION", name)


def cut_cylinder(target, radius, depth, location=(0, 0, 0), rotation=(0, 0, 0), vertices=32, name="cut_cylinder"):
    """Cut a cylinder from target (DIFFERENCE)."""
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, vertices=vertices, location=location, rotation=rotation)
    _apply_boolean(target, bpy.context.active_object, "DIFFERENCE", name)


def create_rounded_cone(radius, depth, location=(0, 0, 0), rotation=(0, 0, 0), vertices=64, rings=24, name="Rounded_Cone"):
    """Create a rounded tapered cone along the Z axis and return it."""
    verts = []
    faces = []

    for ring in range(rings):
        t = ring / rings
        z = -depth / 2 + depth * t
        # Smoothstep taper: wide at the base, rounded to a point at the tip.
        smooth = t * t * (3 - 2 * t)
        r = radius * (1 - smooth)

        for i in range(vertices):
            angle = 2 * math.pi * i / vertices
            verts.append((r * math.cos(angle), r * math.sin(angle), z))

    for ring in range(rings - 1):
        for i in range(vertices):
            a = ring * vertices + i
            b = ring * vertices + (i + 1) % vertices
            c = (ring + 1) * vertices + (i + 1) % vertices
            d = (ring + 1) * vertices + i
            faces.append((a, b, c, d))

    top_center = len(verts)
    verts.append((0, 0, depth / 2))
    last_ring = (rings - 1) * vertices
    for i in range(vertices):
        faces.append((last_ring + i, last_ring + (i + 1) % vertices, top_center))

    bottom_center = len(verts)
    verts.append((0, 0, -depth / 2))
    for i in range(vertices):
        faces.append((bottom_center, i, (i + 1) % vertices))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()

    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    obj.rotation_euler = rotation
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.ops.object.shade_smooth()
    return obj


# =============================================================================
# Tear Beam (teardrop cross-section beam)
# =============================================================================

def create_tear_beam(depth, width, height, segments=32, power=0.7, location=(0, 0, 0), rotation=(0, 0, 0), name="Tear_Beam"):
    """Create a beam with teardrop cross-section.
    depth: beam length (Y axis).
    width: cross-section width (X).
    height: cross-section teardrop height (Z).
    """
    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    bm = bmesh.new()

    # Teardrop profile in XZ plane (right half, bottom to top)
    pts = []
    for i in range(segments + 1):
        t = i / segments
        z = -height / 2 + height * t
        x = width / 2 * math.sin(math.pi * t ** power)
        pts.append((x, z))

    # Full profile: right half + left half (mirrored)
    profile = list(pts)
    profile += [(-x, z) for x, z in reversed(pts[1:-1])]

    n = len(profile)
    y_front = -depth / 2
    y_back = depth / 2

    front = [bm.verts.new((x, y_front, z)) for x, z in profile]
    back = [bm.verts.new((x, y_back, z)) for x, z in profile]

    for i in range(n):
        j = (i + 1) % n
        bm.faces.new([front[i], front[j], back[j], back[i]])

    bm.faces.new(list(reversed(front)))
    bm.faces.new(back[:])

    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    bm.to_mesh(mesh)
    bm.free()

    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    obj.rotation_euler = rotation
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.ops.object.shade_smooth()
    return obj


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


def cut_inner_corners(target, width, height, depth, thickness):
    """Add fillets to inner corners of a rectangular hole."""
    x, y = width / 2 - thickness, height / 2 - thickness
    cut_holes(target, thickness, depth, [(x, y), (x, -y), (-x, y), (-x, -y)], z=thickness)
    cut_cube(target, (width - thickness * 2, height, depth), (0, 0, thickness))
    cut_cube(target, (width, height - thickness * 2, depth), (0, 0, thickness))


# =============================================================================
# Mesh Deformation
# =============================================================================

def taper(obj, top_scale=0.0, bottom_scale=1.0, segments=16, curve="cos", power=None, peak=0.35):
    """Taper object along Z axis by scaling vertex rings.
    segments: number of Z subdivisions to add for smooth deformation.
    curve: 'cos' (dome), 'linear' (cone), 'sqrt' (bullet), 'tear' (teardrop).
    power: exponent for 'tear' curve (default 0.5, larger = smoother nose).
    peak: position of widest point for 'tear' curve, 0=bottom 1=top (default 0.35).
    """
    bm = bmesh.new()
    bm.from_mesh(obj.data)

    # Add Z subdivisions on vertical edges
    z_edges = [e for e in bm.edges if abs(e.verts[0].co.z - e.verts[1].co.z) > 0.001]
    if z_edges and segments > 1:
        bmesh.ops.subdivide_edges(bm, edges=z_edges, cuts=segments)

    # Scale each vertex ring by curve
    z_min = min(v.co.z for v in bm.verts)
    z_max = max(v.co.z for v in bm.verts)
    z_range = z_max - z_min

    if z_range > 0:
        for v in bm.verts:
            t = (v.co.z - z_min) / z_range  # 0=bottom, 1=top
            if curve == "cos":
                factor = bottom_scale + (top_scale - bottom_scale) * (1 - math.cos(t * math.pi / 2))
            elif curve == "tear":
                p = power if power is not None else 0.5
                if t < peak:
                    factor = math.sin(math.pi / 2 * (t / peak) ** p)
                else:
                    factor = math.cos(math.pi / 2 * ((t - peak) / (1 - peak)) ** p)
            elif curve == "sqrt":
                factor = bottom_scale + (top_scale - bottom_scale) * math.sqrt(t)
            else:  # linear
                factor = bottom_scale + (top_scale - bottom_scale) * t
            v.co.x *= factor
            v.co.y *= factor

    # Merge overlapping vertices at tip
    bmesh.ops.remove_doubles(bm, verts=bm.verts[:], dist=0.01)

    bm.to_mesh(obj.data)
    bm.free()
    obj.data.update()
    return obj


# =============================================================================
# Object Operations
# =============================================================================

def modifier_apply(obj, target, operation="UNION", name="modifier_apply"):
    """Apply boolean modifier between two objects."""
    _apply_boolean(target, obj, operation, name)


def copy(obj, location=None, rotation=None, name=None):
    """Copy an object and return the new copy."""
    new_mesh = obj.data.copy()
    new_obj = obj.copy()
    new_obj.data = new_mesh
    if name:
        new_obj.name = name
    if location is not None:
        new_obj.location = location
    if rotation is not None:
        new_obj.rotation_euler = rotation
    bpy.context.collection.objects.link(new_obj)
    return new_obj


def join(target, obj):
    """Join two objects into one."""
    bpy.context.view_layer.objects.active = target
    target.select_set(True)
    obj.select_set(True)
    bpy.ops.object.join()

# fmt: on
