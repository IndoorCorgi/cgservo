#!/usr/bin/env python3

from cgservo import Servo
from cgservo import MotorParam
import time

# モーター1と2を制御する例

# サーボモーター制御クラス
servo = Servo(
    i2c_addr=0x40,  # I2Cアドレス. 0x41を使用している場合は変更する
    pwm_freq_target=200,  # PWM周波数[Hz]. ほとんどのモーターが50Hzに対応. 問題なければ100-200Hzに変更してOK. 

    # モーター1のパラメーター -90°〜90°で角度
    m1_param=MotorParam(
        min_pulse_width=0.5,
        max_pulse_width=2.5,
        input_start=-90,
        input_end=90,
    ),

    # モーター2のパラメーター 0°〜180°で角度指定
    m2_param=MotorParam(
        min_pulse_width=0.5,
        max_pulse_width=2.5,
        input_start=0,
        input_end=180,
    ),
)

servo.reset()  # コントローラーICをリセットして周波数を設定. 制御開始前に実行する

# モーター1, 2を動かす
servo.m1 = 0
servo.m2 = 0
time.sleep(3)

servo.m1 = -90
servo.m2 = 90
time.sleep(3)

servo.m1 = 90
servo.m2 = 180
time.sleep(3)
