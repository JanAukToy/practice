#フルーツ買い物計算

fruits = {"apple":150,"banana":100,"grape":300}

input_money = input("所持金を入力して下さい。")

if int(input_money) < 100:
  print("お金が足りません。")

elif int(input_money) < 0:
  print("正しく入力して下さい。")
else:
  for fruits_key in fruits:
    input_fruits = input(fruits_key+"を何個購入しますか？")
    print(fruits_key + "を" + input_fruits + "個購入します。")
    count = fruits[fruits_key] * int(input_fruits)
    print("代金は" + str(count) + "円です")
    if count < int(input_money):
      input_money = int(input_money) - count
      print("所持金は" + str(input_money) + "円です。")
    else:
      print("所持金が足りません。")
