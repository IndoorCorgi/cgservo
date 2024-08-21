#!/usr/bin/env python3

from cgservo import Servo
import time

# モーター1の角度をパルス幅で指定する例

# サーボモーター制御クラス
# モーターのパラメーターを指定しないと, デフォルト値になる
servo = Servo(
    i2c_addr=0x40,  # I2Cアドレス. 0x41を使用している場合は変更する
    pwm_freq_target=50,  # PWM周波数[Hz]. ほとんどのモーターが50Hzに対応. 問題なければ100-200Hzに変更してOK. 
)

servo.init()  # コントローラーICをリセットして周波数を設定. 制御開始前に実行する

servo.m1p = 1.5  # パルス幅1.5[ms]でPWM出力. 多くのモーターで中間の位置に移動.
time.sleep(3)
servo.m1p = 1.0  # パルス幅1.0[ms]でPWM出力.
time.sleep(3)
servo.m1p = 2.0  # パルス幅2.0[ms]でPWM出力.
time.sleep(3)
servo.m1p = 0  # 0を指定するとPWM出力を停止.
