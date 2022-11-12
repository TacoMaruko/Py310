import random

mini = 1
maxx = 100
count = 0
rand_value = random.randint(mini, maxx)
print(f"====== 猜數字 {mini} ~ {maxx} ======")

while True:
    count += 1
    keyin = int(input(f"輸入一個數字{mini}~{maxx}："))
    if keyin >= mini and keyin <= maxx:
        if (keyin == rand_value):
            print(f"\n答對了,是 {rand_value}！")
            print(f"你猜了 {count} 次")
            break

        elif keyin > rand_value:
            print(f"比 {keyin} 再小一些，第 {count} 次\n")

        elif keyin < rand_value:
            print(f"比 {keyin} 再大一些,第 {count} 次\n")

        else:
            print(f"{keyin} 不對，再猜～")
    else:
        print("超出遊戲範圍！")

print("遊戲結束！")
