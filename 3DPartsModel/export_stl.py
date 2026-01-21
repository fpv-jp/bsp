#!/usr/bin/env python3
"""
Command-line STL exporter for Blender scripts.
Usage: blender --background --python export_stl.py -- <script.py> [output.stl]
"""
import bpy
import sys
import os
import types
import importlib.util


def init():
    """Clear all objects in the scene (headless-compatible)."""
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def load_module_from_file(filepath, module_name):
    """Load a Python module from file path."""
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def main():
    # Get arguments after "--"
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        print("Usage: blender --background --python export_stl.py -- <script.py> [output.stl]")
        sys.exit(1)

    if len(argv) < 1:
        print("Error: No input script specified")
        sys.exit(1)

    input_script = argv[0]
    output_stl = argv[1] if len(argv) > 1 else input_script + ".stl"

    script_dir = os.path.dirname(os.path.abspath(input_script))

    # Load base module from the same directory
    base_path = os.path.join(script_dir, "base.py")
    if os.path.exists(base_path):
        base_module = load_module_from_file(base_path, "base")
        # Override init to be headless-compatible
        base_module.init = init

    # Clear the scene
    init()

    # Execute the script with modified globals
    script_globals = {
        "__name__": "__main__",
        "__file__": input_script,
        "bpy": bpy,
    }

    # Read and modify the script to skip the bpy.data.texts import
    with open(input_script, "r") as f:
        script_content = f.read()

    # Remove the bpy.data.texts import block and replace with direct import
    lines = script_content.split("\n")
    new_lines = []
    skip_until_import_base = False

    for line in lines:
        # Skip the bpy.data.texts based import mechanism
        if "bpy.data.texts.get" in line:
            skip_until_import_base = True
            continue
        if skip_until_import_base:
            if line.strip().startswith("import base"):
                skip_until_import_base = False
                new_lines.append("import base")
            continue
        # Skip base.init() call since we already called init()
        if line.strip() == "base.init()":
            continue
        new_lines.append(line)

    modified_script = "\n".join(new_lines)
    exec(compile(modified_script, input_script, "exec"), script_globals)

    # Select all mesh objects and export
    bpy.ops.object.select_all(action="DESELECT")
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH":
            obj.select_set(True)

    bpy.ops.wm.stl_export(filepath=output_stl)
    print(f"Exported: {output_stl}")


if __name__ == "__main__":
    main()
