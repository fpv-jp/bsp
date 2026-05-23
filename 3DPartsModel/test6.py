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

_test6 = bpy.data.objects.get("test6")
if _test6:
    _test6.hide_set(True)

base.init()

if _test6:
    _test6.hide_set(False)
