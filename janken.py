
import random
hand = ["グー", "チョキ", "パー"]

def judge(hands):
  if hands > 2 or hands < 0:
    return False
  return True

def battle(player):
  if player > 2 or player < 0:
    return

  com = random.randint(0, 2)
  print("COMは" + hand[com] + "を出しました。")
  
  if player == 0 and com == 2:
    print("負けです。")
  elif player == 1 and com == 0:
    print("負けです。")
  elif player == 2 and com == 1:
    print("負けです。")
  elif player == 0 and com == 1:
    print("勝ちです。")
  elif player == 1 and com == 2:
    print("勝ちです。")
  elif player == 2 and com == 0:
    print("勝ちです。")
  else:
    print("引き分けです。")

print("じゃんけんを開始します。")
print("0:グー、1:チョキ、2:パーです。")
input_number = int(input("数字を入力して下さい。"))

if judge(input_number):
  print("あなたは" + hand[input_number] + "を出しました。")
else:
  print("正しく入力して下さい。")

battle(input_number)
