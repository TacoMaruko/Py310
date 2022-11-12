# 定義 function
def sayHello():
    print("Hello!")


def sayHello_withName(name):
    print(f"Hello {name}")


def square_area(f_side):  # 有邊長的參數
    f_area = f_side ** 2  # function 變數
    return f_area  # 回傳 function 變數


def rectangle(f_width, f_height):
    f_area = f_width * f_height
    return f_area


if __name__ == "__main__":
    sayHello()
    # 呼叫 function
    sayHello_withName("Maruko")

    side = eval(input("輸入正方形邊長："))
    Sq_area = square_area(side)  # 文件變數，與 function 變數同名，也可以
    print(f"正方形面積：{Sq_area} 平方公分")

    Rec_area = rectangle(15.5, 30)
    print(f"長方形面積：{Rec_area} 平方公分")
