#!/usr/bin/env python3

from cgservo import Servo
from cgservo import MotorParam
import time

# 基板1枚目のモーター1と基板2枚目のモーター1を制御する例

# 基板1
servo1 = Servo(
    i2c_addr=0x40,  # I2Cアドレス. 0x40に設定した基板を制御
    pwm_freq_target=50,

    # モーター1のパラメーター
    m1_param=MotorParam(
        min_pulse_width=0.5,
        max_pulse_width=2.5,
        input_start=-90,
        input_end=90,
    ),
)

# 基板2
servo2 = Servo(
    i2c_addr=0x41,  # I2Cアドレス. 0x41に設定した基板を制御
    pwm_freq_target=50,

    # モーター1のパラメーター
    m1_param=MotorParam(
        min_pulse_width=0.5,
        max_pulse_width=2.5,
        input_start=-90,
        input_end=90,
    ),
)

servo1.init()  # 両方の基板がリセットされ, 基板1を初期設定
servo2.init(reset=False)  # 基板2を初期設定. 2枚目の基板はreset=Falseを指定する

# 各基板のモーター1を動かす
servo1.m1 = 0
time.sleep(2)
servo2.m1 = 0
time.sleep(2)
servo1.m1 = -90
time.sleep(2)
servo2.m1 = -90
time.sleep(2)
servo1.m1 = 90
time.sleep(2)
servo2.m1 = 90
time.sleep(2)
