def MyFirstFunction():
    count = 10


def MySecondFunction():
    global count  # 添加global关键字
    count = 100


count = 5
MyFirstFunction()
print(count)  # 执行完MyFirstFunction仍然为5
MySecondFunction()
print(count)  # MySecondFunction里有global关键字，所以count会被修改


def Fun1():
    print('Fun1正在被调用...')

    def Fun2():  # Fun2是Fun1的内部函数
        print('Fun2正在被调用...')


Fun1()  # 这里打印结果为：Fun1正在被调用... ，可以看到Fun1里的Fun2未被运行是因为Fun1中没有调用Fun2


# Fun2()  # 这里调用Fun2会被报错，因为内部函数只有包裹住他的函数体内可以使用，在外面不能调用


def Fun3():
    print('Fun3正在被调用...')

    def Fun4():
        print('Fun4正在被调用...')

    Fun4()  # 注意这里是在Fun3中调用Fun4，python的缩进是用于充当C中{ }大括号，划分函数体用的，这段是属于Fun3的，不是Fun4的


Fun3()


# 运行结果为
# Fun3正在被调用...
# Fun4正在被调用...


def FunX(x):
    def FunY(y):
        return x * y  # 这里内部函数对外部函数的变量x进行调用了，注意函数的参数也是作为函数内部的变量的

    return FunY  # 这里外部函数的返回值为内部函数，注意这里内部函数不用带()


a = FunX(8)
print(a)  # 打印结果：<function FunX.<locals>.FunY at 0x00000168D5E58680>
print(type(a))  # 打印结果发现a的类型为<class 'function'>，函数类型，所以a本身就是一个函数，
# 在python中这个函数其实就是内部函数
print(a(5))  # 这里我们给a传个参数，打印结果为40 ，即之前的8，乘以后面再传过去的5

# 也可以直接这样
b = FunX(8)(5)  # 第一个括号参数传给外部函数，后面括号中参数传给的是内部函数
print(b)  # 打印结果为40


# def Fun1():
#     x = 8
#
#     def Fun2():
#         x *= x  # x = x * x，这里内部函数本来想对外部函数的x进行调用，但是因为下面是调用Fun2(),这样就和之前一样，外部函数的变量在内部函数中不可改变，内部函数会在自己内部的空间创建一个x，所以内部函数的x没有赋值，会报错。
#         return x
#
#     return Fun2()  # 这里返回内部函数不能带()，带()的话相当于调用Fun2，就不再是闭包，而执行Fun2，Fun2里的x相当于是自己有新建了一个变量x，没有调用外部函数的参数
#
#
# Fun1()


def Fun1():
    x = 8

    def Fun2():
        nonlocal x # 声明这里不是这个函数的局部变量，所以会用外部函数的x
        x *= x  # x = x * x，这里内部函数对外部函数的变量x进行调用
        return x

    return Fun2()

print(Fun1())
# 运行结果为64

