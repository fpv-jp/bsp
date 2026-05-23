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

_test4_all = bpy.data.objects.get("test4_all")
if _test4_all:
    _test4_all.hide_set(True)

base.init()

if _test4_all:
    _test4_all.hide_set(False)
