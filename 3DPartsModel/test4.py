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
R = 35.0
D = R * 10

# taper(obj, curve="tear", power=?, peak=?)
#
#   curve="tear" : 涙型の輪郭カーブを使う（流線型ボディ向け）
#
#   power : カーブの丸み（上下共通）
#           小さい(0.3) → 先端が鋭く、中央付近が急に膨らむ
#           大きい(1.0) → なだらかで丸みのある輪郭
#
#   peak  : 最大幅の位置（0.0=下端 〜 1.0=上端）
#           0.2 → 下寄り（涙型・細長い先端）
#           0.5 → 中央（ラグビーボール型）
#           0.8 → 上寄り（逆涙型）
#
# --- 形状プリセット例 ---
# 細長い流線型（ドローンボディ向け）
#   power=0.6, peak=0.3
#
# 丸みのある卵型
#   power=0.8, peak=0.45
#
# 先端が鋭いロケット型
#   power=0.4, peak=0.25


body = base.create_cylinder_smooth(radius=R, depth=D/3-8)
body_inner = base.create_cylinder_smooth(radius=R-1, depth=D/3-8)
base.modifier_apply(body_inner, body, operation="DIFFERENCE")

#base.cut_cube(
#    target=body,
#    scale=(R-1, R-1, D/3),
#    location=(0, 0, 0),
#)

body1 = base.create_cylinder_smooth(radius=R, depth=D)
base.taper(body1, segments=64, curve="tear", power=0.66)

body1_inner = base.create_cylinder_smooth(radius=R-1, depth=D)
base.taper(body1_inner, segments=64, curve="tear", power=0.66)
base.modifier_apply(body1_inner, body1, operation="DIFFERENCE")

body2 = base.create_cylinder_smooth(radius=R, depth=D)
base.taper(body2, segments=64, curve="tear", power=0.66, peak=0.66)

body2_inner = base.create_cylinder_smooth(radius=R-1, depth=D)
base.taper(body2_inner, segments=64, curve="tear", power=0.66, peak=0.66)
base.modifier_apply(body2_inner, body2, operation="DIFFERENCE")

base.modifier_apply(obj=body1, target=body, operation="UNION")
base.modifier_apply(obj=body2, target=body, operation="UNION")

base.cut_cube(
    target=body,
    scale=(200, 200, 500),
    location=(0, -100, 0),
)
#base.cut_cube(
#    target=body1,
#    scale=(200, 200, 500),
#    location=(0, -100, 0),
#)
#base.cut_cube(
#    target=body2,
#    scale=(200, 200, 500),
#    location=(0, -100, 0),
#)

#base.cut_cylinder(target=body, radius=R-1, depth=D/3-8)


#body.location = (0.0, 0.0, H)

#base.taper(body2, segments=64, curve="tear", power=0.66, peak=0.66)
# 内側をくり抜く（壁厚1.5mm）
#inner = base.create_cylinder_smooth(radius=R*0.95, depth=D)
#base.taper(inner, segments=64, curve="tear", power=0.6, peak=0.3)
#base.modifier_apply(inner, body, operation="DIFFERENCE")


#INCH = 12 * 25.4  # 12inch

#arm_width = 14.5
#arm_height = arm_width*3
#arm_power = 0.75

#arm = base.create_tear_beam(
#    depth=INCH,
#    width=arm_width,
#    height=arm_height,
#    power=arm_power,
#)
