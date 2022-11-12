# 專案內的主要執行檔，一定要使用 __name__ 來判斷式
# 猜數字小遊戲，範圍 1～100
# 沒有限制次數

import random
# 文件變數，範圍（Scope）作用到整份文件
mini = 1
maxx = 100
count = 0
rand_value = random.randint(mini, maxx)
print(f"{rand_value}\n")  # 直接公佈答案，偷吃步

if __name__ == "__main__":
    print(f"檔案性質：{__name__}")
    print(f"變數屬性：{type(__name__)}")
    print(f"檔案所在：{__file__}")
    print("這是整個專案的「主要執行檔」，會被 Python 執行\n")

    print(f"====== 猜數字 {mini} ~ {maxx} ======")

    while True:
        count += 1
        keyin = int(input(f"輸入一個數字{mini}~{maxx}："))
        # keyin 也是「文件變數」，這點是 Python 與其它程式語言的大不同

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
