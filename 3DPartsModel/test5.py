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


adjustment = 1.47  # アームの長さ/モータ位置を調整する倍率

INCH = 6 * 25.4 * adjustment  # 6inch

ARM_L = INCH / 2
ARM_W = 12.0

MOTOR_PITCH = 19.0 / 2

MAIN_DEPTH = 6.0

M3 = 3.0
M5 = 5.0

FC_PITCH = 30.5 / 2

### ------------------------------------------------------------------------------------
### モータ・腕
### ------------------------------------------------------------------------------------

# モータ
motor = base.create_cube(scale=(MOTOR_PITCH * 2.08, MOTOR_PITCH * 2.08, MAIN_DEPTH))

# 参考：モータ+プロペラ<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
PROP_INCH = 6 * 25.4  # 6inch
PROP_DEPTH = 9.0

MOTOR_SIZE = 37.0

MOTOR_Z1 = 45.30
MOTOR_Z2 = 39.10
MOTOR_Z3 = 16.60

MOTOR_MAIN_DEPTH = MOTOR_Z2 - MOTOR_Z3
MOTOR_MOUNT_DEPTH = MOTOR_Z1 - MOTOR_Z2

m = base.create_cylinder( 
    radius=5.0 / 2,
    depth=MOTOR_Z1,
)
base.add_cylinder(
    target=m,
    radius=MOTOR_SIZE / 2, 
    depth=MOTOR_MAIN_DEPTH,
    location=(0.0, 0.0, (MOTOR_Z1-MOTOR_MAIN_DEPTH)/2-MOTOR_MOUNT_DEPTH),
)
base.add_cylinder(
    target=m, 
    radius=19.0 / 2,
    depth=MOTOR_MOUNT_DEPTH,
    location=(0.0, 0.0, (MOTOR_Z1 - MOTOR_MOUNT_DEPTH) / 2),
)
base.add_cylinder(
    target=m,
    radius=PROP_INCH / 2,
    depth=PROP_DEPTH,
    location=(0.0, 0.0, (MOTOR_Z1 - PROP_DEPTH) / 2-MOTOR_MAIN_DEPTH-MOTOR_MOUNT_DEPTH),
)
m.location=(0.0,0.0,-(MOTOR_Z1+MAIN_DEPTH)/2)
#m.rotation_euler[0] = math.pi
base.modifier_apply(obj=m, target=motor, operation="UNION")
# 参考：モータ+プロペラ<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 腕
base.add_cube(target=motor, scale=(ARM_W, ARM_L, MAIN_DEPTH), location=(0.0, ARM_L / 2, 0.0))

# モータ取り付け穴
MOTOR_HOLES = [
    (MOTOR_PITCH, 0),
    (-MOTOR_PITCH, 0),
    (0, MOTOR_PITCH),
    (0, -MOTOR_PITCH),
]
motor.rotation_euler[2] = math.pi / 4
for i, (x, y) in enumerate(MOTOR_HOLES):
    base.add_ring(
        target=motor,
        outer_radius=M3 * 1.5,
        inner_radius=M3 / 2,
        depth=MAIN_DEPTH,
        location=(x, y, 0.0),
        vertices=64,
    )

# 中心を変える(ボディ取り付け角カット)----------------------------
motor.rotation_euler[2] = 0
motor.location = (0.0, -ARM_L, 0.0)
base.set_origin(motor, (0.0, 0.0, 0.0))  # 回転の起点をシーンの(0,0,0)に設定

# ボディ取り付け角カット----------------------------
motor.rotation_euler[2] = math.pi / 4
base.cut_cube(target=motor, scale=(20, 10, 10), location=(0.0, 5.0, 0.0))
motor.rotation_euler[2] = -math.pi / 4
base.cut_cube(target=motor, scale=(20, 10, 10), location=(0.0, 5.0, 0.0))

# ボディ取り付け穴----------------------------
base.cut_cylinder(target=motor, radius=M5 / 2, depth=MAIN_DEPTH * 2)
base.cut_cylinder(
    target=motor, radius=M3 / 2, depth=MAIN_DEPTH * 2, location=(-FC_PITCH / 2, -FC_PITCH / 2, 0.0)
)
motor.rotation_euler[2] = 0

# 中心を戻す(step出力用)----------------------------
##motor.location = (0.0, ARM_L / 2, 0.0)
##base.set_origin(motor, (0.0, 0.0, 0.0))  # 回転の起点をシーンの(0,0,0)に設定

# 他の腕を複製----------------------------
motor2 = base.copy(motor, rotation=(0, 0, math.pi / 2))
motor3 = base.copy(motor, rotation=(0, 0, math.pi))
motor4 = base.copy(motor, rotation=(0, 0, -math.pi / 2))

### ------------------------------------------------------------------------------------
### 胴体
### ------------------------------------------------------------------------------------
MAIN_DEPTH = 3.0

# 天板----------------------------
body = base.create_cube(
    scale=(FC_PITCH * 2 + ARM_W / 1.42, FC_PITCH * 2 + ARM_W / 1.42, MAIN_DEPTH)
)
base.cut_cylinder(target=body, radius=M5 / 2, depth=MAIN_DEPTH * 2)

FC_HOLES = [
    (FC_PITCH, FC_PITCH),
    (FC_PITCH, -FC_PITCH),
    (-FC_PITCH, FC_PITCH),
    (-FC_PITCH, -FC_PITCH),
]

for i, (x, y) in enumerate(FC_HOLES):
    base.add_ring(
        target=body,
        outer_radius=ARM_W / 2,
        inner_radius=M3 / 2,
        depth=MAIN_DEPTH,
        location=(x, y, 0.0),
        vertices=64,
    )

body.location = (0.0, 0.0, 3.0 + 1.5)
body.rotation_euler[2] = math.pi / 4

## 底板を複製----------------------------
body2 = base.copy(body, location=(0.0, 0.0, -3.0 - 1.5))

### ------------------------------------------------------------------------------------
### 参考
### ------------------------------------------------------------------------------------

battery = base.create_cube(scale=(40, 40, 70))
battery1 = base.copy(battery)
fc = base.create_cube(scale=(42, 42, 10))
# esc = base.create_cube(scale=(60, 60, 10))
esc = base.create_cube(scale=(42, 42, 10))

battery.location = (0.0, 0.0, 120.0)
battery1.location = (0.0, 0.0, 45.0)
fc.location = (0.0, 0.0, -12.0)
esc.location = (0.0, 0.0, -23.0)


bpy.ops.object.select_all(action="SELECT")
bpy.context.view_layer.objects.active = next(iter(bpy.context.scene.objects))
bpy.ops.object.join()
bpy.context.active_object.rotation_euler[0] = math.pi
bpy.context.active_object.location.z += 55
