def MyFirstFunction():  # 函数定义
    print("这是我创建的第一个函数")
    print("我表示很激动")
    print("在此，我要感谢TVB，感谢CCTV，感谢各位")


MyFirstFunction()  # 函数调用


def MySecondFunction(name):  # 这里函数的参数不用像C语言那样定义类型，只用定义名字就可以
    print(name + "我爱你!")  # 因为这里name + ‘我爱你’，如果name是字符串就是+就是连接符，但一定不能是数字类型，因为字符串和数字无法相加，如果是数字类型会报错


MySecondFunction('Q.M.F.')


def MyThirdFunction(a, b):  # 两个参数
    result = a + b
    print(result)


MyThirdFunction(1, 2)


def add(num1, num2):
    return num1 + num2  # 返回值用return


result = add(3, 4)
print(result)
