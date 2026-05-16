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

# 初期化
base.init()

INCH = 6 * 25.4  # 6inch

MOTOR_X = INCH / 2 * 1.47


# arm ----------------------------------------

arm_width = 14.5
arm_height = arm_width*3
arm_power = 0.75

def create_arm():
    arm = base.create_tear_beam(
        depth=MOTOR_X,  # ビームの長さ（Y軸）
        width=arm_width,  # 断面の幅（X）
        height=arm_height,  # 断面の涙型の高さ（Z）
        power=arm_power,
    )
    inner = base.create_tear_beam(
        depth=MOTOR_X*1.5,  # ビームの長さ（Y軸）
        width=arm_width *0.85,  # 断面の幅（X）
        height=arm_height *0.85,  # 断面の涙型の高さ（Z）
        power=arm_power,
    )
    base.modifier_apply(inner, arm, operation="DIFFERENCE")
    base.cut_cube(
        target=arm,
        scale=(12.0, INCH, 5.0),
        location=(0, 0, -3.9),
    )
    return arm

### motor ----------------------------------------

def create_dummy():
    motor_dummy = base.create_cylinder(radius=38.2 / 2, depth=30.7)
    prop_dummy = base.create_cylinder(radius=INCH / 2, depth=9.0, location=(0, 0, (30.7 + 9.0) / 2))
    base.modifier_apply(obj=prop_dummy, target=motor_dummy, operation="UNION")
    return motor_dummy

def create_motor():

    R = 38.2 / 2
    D = R * 6

    motor = base.create_cylinder(radius=R, depth=D)
    base.taper(motor, segments=64, curve="tear", power=0.75)
    
    # arm attach --------------------------------
    
    arm = create_arm()
    arm.location = (0, MOTOR_X / 2, -6.085)
    base.modifier_apply(obj=arm, target=motor, operation="UNION")
    
    # 内側をくり抜く（壁厚1.5mm）
    inner = base.create_cylinder(radius=R*0.97, depth=D*0.97)
    base.taper(inner, segments=64, curve="tear", power=0.75)
    base.modifier_apply(inner, motor, operation="DIFFERENCE")
    
    base.cut_cylinder(
        target=motor,
        radius=R,
        depth=100.0,
        location=(0, 0, 50*0.75),
    )
    
    # 中身を確認するために透過
    base.cut_cube(
        target=motor,
        scale=(50, 50, 250),
        location=(0, -25, 0),
    )

    # dummy --------------------------------
#    dummy = create_dummy()
#    dummy.location = (0, 0, 3.4)
#    base.modifier_apply(obj=dummy, target=motor, operation="UNION")

    return motor



motor1 = create_motor()
motor1.location = (0, -MOTOR_X, 0)

#motor2 = create_motor()
#motor2.location = (MOTOR_X, 0, 0)
#motor2.rotation_euler[2] = math.pi / 2

#motor3 = create_motor()
#motor3.location = (-MOTOR_X, 0, 0)
#motor3.rotation_euler[2] = -math.pi / 2

#motor4 = create_motor()
#motor4.location = (0, MOTOR_X, 0)
#motor4.rotation_euler[2] = math.pi

## body ----------------------------------------

# 涙型の流線型ボディ
R = 33.0
D = R * 10

body = base.create_cylinder(radius=R, depth=D)
base.taper(body, segments=64, curve="tear", power=0.60)

## arm attach
#base.modifier_apply(obj=arm1, target=body, operation="UNION")
##base.modifier_apply(obj=arm2, target=body, operation="UNION")
##base.modifier_apply(obj=arm3, target=body, operation="UNION")
##base.modifier_apply(obj=arm4, target=body, operation="UNION")

# 内側をくり抜く（壁厚1.5mm）
inner = base.create_cylinder(radius=R*0.97, depth=D*0.97)
base.taper(inner, segments=64, curve="tear", power=0.60)
base.modifier_apply(inner, body, operation="DIFFERENCE")

# 無駄な底辺をカット
base.cut_cube(
    target=body,
    scale=(100, 100, 500),
    location=(0, 0, 320),
)


### ----------------------------------------

# 中身を確認するために透過
base.cut_cube(
    target=body,
    scale=(80, 40, 500),
    location=(0, -20, 0),
)

