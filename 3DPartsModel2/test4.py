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

_test5 = bpy.data.objects.get("test5")
if _test5:
    _test5.hide_set(True)

base.init()

if _test5:
    _test5.hide_set(False)

adjustment = 1.47  # アームの長さ/モータ位置を調整する倍率

DRONE_SIZE = 6.0 * 25.4 * adjustment  # 6inch

MOTOR_PITCH = DRONE_SIZE / 2  # モータとボディのピッチ/アームの長さ

ARM_width = 12.0  # アームの幅
ARM_position = 55.0  # ボディに対してアームを取り付ける位置

MOTOR_radius = 38.2 / 2  # モータの半径

BODY_radius = 30.0  # ボディの半径
BODY_height = BODY_radius * 12  # ボディの高さ

WALL_hickness = 1.5  # 基本とする壁の厚み

TEST_CUT = True
TEST_CUT = False


# -------------------------------------------------------
# モータ
# -------------------------------------------------------
def create_motor(sharpen):

    # --- スピンナー(モータ直径より少し小さくする) ---
    motor = base.create_cylinder(
        radius=MOTOR_radius * 0.9 - sharpen,
        depth=MOTOR_radius * 8,
        vertices=64,
    )
    # テーバをつける
    base.taper(motor, segments=64, curve="tear", power=0.75)
    return motor


# -------------------------------------------------------
# アーム
# -------------------------------------------------------
def create_arm(sharpen):

    sharpen2 = sharpen * 2

    # --- アーム 中央 ---
    arm = base.create_cube(
        scale=(
            ARM_width - sharpen2,
            DRONE_SIZE / 1.75,
            ARM_width * 3 - sharpen2,
        ),
        location=(0.0, DRONE_SIZE / 4, 0.0),
    )

    # --- アーム 上部 ---
    arm_top = base.create_tear_beam(
        depth=DRONE_SIZE / 1.75,
        width=ARM_width - sharpen2,
        height=ARM_width * 3 - sharpen2,
        power=0.75,
        location=(0.0, DRONE_SIZE / 4, -ARM_width * 1.2),
    )

    # --- アーム 中央 上部 結合し傾けて少し上にずらす ---
    base.modifier_apply(obj=arm_top, target=arm, operation="UNION")
    arm.rotation_euler = (math.pi / 8, 0, 0)
    arm.location = (0.0, 0.0, -ARM_width * 1.9)

    # --- 下を少しカット ---
    base.cut_cube(
        target=arm,
        scale=(ARM_width, DRONE_SIZE, ARM_width * 4),
        location=(0.0, DRONE_SIZE / 4, ARM_width * 1.75),
    )

    # --- アーム 下部 ---
    arm_bottom = base.create_tear_beam(
        depth=DRONE_SIZE / 2,
        width=ARM_width - sharpen2,
        height=ARM_width * 3 - sharpen2,
        power=0.75,
        location=(0.0, DRONE_SIZE / 4, 0.0),
    )

    # --- アーム 中央 上部 と 下部 を 結合 ---
    base.modifier_apply(obj=arm_bottom, target=arm, operation="UNION")

    return arm


# -------------------------------------------------------
# アーム + モータ
# -------------------------------------------------------
def create_motor_arm():

    # --- アーム(中をくり抜く) ---
    arm = create_arm(0)
    arm_inner = create_arm(WALL_hickness)
    base.modifier_apply(obj=arm_inner, target=arm, operation="DIFFERENCE")

    location = (0, MOTOR_PITCH, 16.0)  # アーム に対して モータ を取り付ける位置

    # --- モータ ---
    motor = create_motor(0)
    motor.location = location

    # --- アーム と モータ を結合 ---
    base.modifier_apply(obj=motor, target=arm, operation="UNION")

    # --- モータの 中をくり抜く ---
    motor_inner = create_motor(WALL_hickness)
    motor_inner.location = location
    base.modifier_apply(obj=motor_inner, target=arm, operation="DIFFERENCE")

    # --- モータ の下部をカット ---
    base.cut_cylinder(
        target=arm,
        radius=MOTOR_radius + WALL_hickness,
        depth=100.0,
        location=(0.0, MOTOR_PITCH, 50.0),
        vertices=64,
    )

    return arm


# -------------------------------------------------------
# ボディ
# -------------------------------------------------------
def create_body(sharpen):

    # --- ボディ 中央 ---
    body = base.create_cylinder(
        radius=BODY_radius - 0.1 - sharpen,
        depth=BODY_height / 2.5,
        location=(0.0, 0.0, 11.0),
        vertices=64,
    )

    # --- ボディ 上部 ---
    body_top = base.create_tear_body(
        radius=BODY_radius - sharpen, depth=BODY_height, power=0.66, smooth=False
    )

    # --- ボディ 下部 ---
    body_bottom = base.create_tear_body(
        radius=BODY_radius - sharpen, depth=BODY_height, power=0.66, peak=0.75, smooth=False
    )

    # --- ボディ を結合 ---
    base.modifier_apply(obj=body_top, target=body, operation="UNION")
    base.modifier_apply(obj=body_bottom, target=body, operation="UNION")
    return body


# --------------------------------------------
# --- アッセンブリ -----------------------------
# --------------------------------------------

# アーム + モータ
motor_arm1 = create_motor_arm()
motor_arm1.location[2] = ARM_position  # ボディに対して取り付ける位置を調整

# 他の アーム + モータ をコピー
motor_arm2 = base.copy(motor_arm1, rotation=(math.pi / 8, 0, math.pi))
motor_arm3 = base.copy(motor_arm1, rotation=(math.pi / 8, 0, math.pi / 2))
motor_arm4 = base.copy(motor_arm1, rotation=(math.pi / 8, 0, -math.pi / 2))

# --- ボディ ---
body = create_body(0)

# --- ボディ の下部をカット ---
base.cut_cylinder(
    target=body,
    radius=BODY_radius,
    depth=100.0,
    location=(0.0, 0.0, 190.0),
)

# --- ボディ に腕を結合 ---
base.modifier_apply(obj=motor_arm1, target=body, operation="UNION")
base.modifier_apply(obj=motor_arm2, target=body, operation="UNION")
base.modifier_apply(obj=motor_arm3, target=body, operation="UNION")
base.modifier_apply(obj=motor_arm4, target=body, operation="UNION")

# --- ボディ を中空化 ---
body_inner = create_body(WALL_hickness)
base.modifier_apply(obj=body_inner, target=body, operation="DIFFERENCE")

# パーツに分けた時の止め合わせを追加
location = (0.0, 0.0, 11.0)
depth = BODY_height / 4
base.add_cube(
    target=body,
    location=(location),
    scale=(BODY_radius * 2 - 0.5, 3.0, depth),
)
base.add_cube(
    target=body,
    location=(location),
    scale=(3.0, BODY_radius * 2 - 0.5, depth),
)
base.cut_cylinder(
    target=body,
    location=(location),
    radius=BODY_radius - 3.5,
    depth=depth + 0.1,
    vertices=128,
)

# アームの骨格と重なる部分をカット
location = (0.0, 0.0, 21.0 + ARM_position)
base.cut_cube(
    target=body,
    location=(location),
    scale=(ARM_width + 0.1, DRONE_SIZE, 6.1),
)
base.cut_cube(
    target=body,
    location=(location),
    scale=(DRONE_SIZE, ARM_width + 0.1, 6.1),
)

# --- 確認のため前面カット ---
if TEST_CUT:
    base.bisect(body, plane_co=(0, 0, 0), plane_no=(0, 1, 0), clear_outer=True)

# そのままだと3Dプリンタのサイズを超えるので調整
body.rotation_euler = (math.pi, 0, math.pi / 4)
