#!/usr/bin/env python3

from cgservo import Servo
from cgservo import MotorParam
import time

# モーター1の角度を-90°〜+90°で指定する例

# サーボモーター制御クラス
servo = Servo(
    i2c_addr=0x40,  # I2Cアドレス. 0x41を使用している場合は変更する
    pwm_freq_target=50,  # PWM周波数[Hz]. ほとんどのモーターが50Hzに対応. 問題なければ100-200Hzに変更してOK. 
    m1_param=MotorParam(
        min_pulse_width=0.5,  # モーターの最小のパルス幅[ms]
        max_pulse_width=2.5,  # モーターの最大パルス幅[ms]
        input_start=-90,  # 角度, 位置などの入力範囲の開始値. この値を入力するとmin_pulse_widthを出力する.
        input_end=90,  # 角度, 位置などの入力範囲の終了値. この値を入力するとmax_pulse_widthを出力する.
    ),
)

servo.init()  # コントローラーICをリセットして周波数を設定. 制御開始前に実行する

servo.m1 = 0  # 0°の位置に移動
time.sleep(3)
servo.m1 = -90  # -90°の位置に移動
time.sleep(3)
servo.m1 = 90  # +90°の位置に移動
time.sleep(3)
