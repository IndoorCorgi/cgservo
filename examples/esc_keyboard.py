#!/usr/bin/env python3
"""
キーボード入力でM1に接続されたESCとモーターを制御
------------------------------------------
値を指定
  1   2   3   4   5   6   7   8   9   0
 10  20  30  40  50  60  70  80  90  100
  Q   W   E   R   T   Y   U   I   O   P
-10 -20 -30 -40 -50 -60 -70 -80 -90 -100
                Space
                  0
------------------------------------------
現在の値から+/-
  A   S   D
 +1  +5  +20
  Z   X   C
 -1  -5  -20
------------------------------------------
"""

from cgservo import Servo
from cgservo import MotorParam
import termios
import tty
import sys


def main():
  """
  メインルーチン
  """
  current_value = 0  # 現在の入力値
  max_value = 100  # 入力範囲の最大値

  # ESCの種類を選択. 種類に応じて入力範囲を調整する
  while True:
    print('ESCの種類を選択してEnterを押してください')
    print('1) -100〜100  逆回転/ブレーキのある車用ESC')
    print('2)    0〜100  順回転のみの飛行機/ドローン用ESC')
    choice = input('[1-2]:').lower()
    if choice == '1':
      min_value = -100  # 入力範囲の最小値. 車用ESCでは-100〜100
      break
    elif choice == '2':
      min_value = 0  # 入力範囲の最小値. 飛行機/ドローン用ESCでは0〜100
      break

  esc = Servo()  # PWMでESCを制御するクラス
  esc.m1_param = MotorParam(  # M1端子用の設定. M2端子に変更する場合は esc.m2_param... のようにする
      input_start=min_value,  # 入力範囲の最小値
      input_end=max_value,  # 入力範囲の最大値
  )
  esc.init()  # コントローラーICをリセット. 制御開始前に実行する

  print(__doc__)  # 使い方を表示

  try:
    while True:
      # キーボード入力に応じて入力値current_valueを増減する
      current_value = change_value_by_keyboard(current_value, min_value, max_value)

      # ESCのM1端子の入力値を変更. PWMパルス幅が変わりモーターの回転も変わる.
      # M2端子に変更する場合は esc.m2... のようにする
      esc.m1 = current_value
      print(current_value)  # 入力値を表示

  except KeyboardInterrupt:
    esc.init()  # キーボードでCtrl+Cが押されたらリセットして終了


def input_single_char():
  """
  Enter不要でキーボードから1文字入力
  大文字は小文字に変換して返す
  """
  fd = sys.stdin.fileno()
  settings = termios.tcgetattr(fd)
  tty.setcbreak(fd)

  try:
    char = sys.stdin.read(1)
  except KeyboardInterrupt:
    termios.tcsetattr(fd, termios.TCSADRAIN, settings)
    raise KeyboardInterrupt

  termios.tcsetattr(fd, termios.TCSADRAIN, settings)
  return char.lower()


def change_value_by_keyboard(current_value, min_value, max_value):
  """
  キーボード入力に応じてcurrent_valueを変更し, 
  min_valueとmax_valueの範囲内に収まるように調整して返す
  """
  char = input_single_char()
  if char == 'a':
    current_value = current_value + 1
  if char == 'z':
    current_value = current_value - 1
  if char == 's':
    current_value = current_value + 5
  if char == 'x':
    current_value = current_value - 5
  if char == 'd':
    current_value = current_value + 20
  if char == 'c':
    current_value = current_value - 20
  if char == '1':
    current_value = 10
  if char == '2':
    current_value = 20
  if char == '3':
    current_value = 30
  if char == '4':
    current_value = 40
  if char == '5':
    current_value = 50
  if char == '6':
    current_value = 60
  if char == '7':
    current_value = 70
  if char == '8':
    current_value = 80
  if char == '9':
    current_value = 90
  if char == '0':
    current_value = 100
  if char == 'q':
    current_value = -10
  if char == 'w':
    current_value = -20
  if char == 'e':
    current_value = -30
  if char == 'r':
    current_value = -40
  if char == 't':
    current_value = -50
  if char == 'y':
    current_value = -60
  if char == 'u':
    current_value = -70
  if char == 'i':
    current_value = -80
  if char == 'o':
    current_value = -90
  if char == 'p':
    current_value = -100
  if char == ' ':
    current_value = 0

  if current_value > max_value:
    return max_value
  elif current_value < min_value:
    return min_value
  else:
    return current_value


if __name__ == '__main__':
  main()  # mainを実行
