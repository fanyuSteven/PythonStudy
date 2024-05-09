# 一般定义函数使用def，且必须有函数名，而用lambda表达式可以定义一个匿名函数
lambda x: 2 * x + 1


# 对应用def定义
def Fun(x):
    return 2 * x + 1


# 可以看出lambda定义函数的 : 冒号前是参数，后面是返回语句
# lambda表达式定义的匿名函数的使用
g = lambda x: 2 * x + 1  # lambda表达式定义的匿名函数调用前，要先赋值给一个变量，由该变量调用
print(type(g))  # 可以看出lambda表达式定义的是一个函数类型<class 'function'>
print(g(5))  # 用变量g()进行参数输入，打印结果为：11

# lambda表达式定义的匿名函数要多个参数时用 , 逗号隔开
f = lambda x, y: x + y


# 对应def
def add(x, y):
    return x + y


list1 = [0, 1, -2, True, False]
print(filter(None, list1))  # 返回的是一个迭代器对象<filter object at 0x0000027B6330DF60>
print(filter(None, [0, 1, -2, True, False]))  # 这样写也行
print(list(filter(None, list1)))  # 用list()函数转换[1, -2, True]
# 前面为None时，即没有任何条件，故只把序列中为False的元素删除，注意0在机器里面表示的是false
print(list1)  # 原来的序列没有改变，filter()会将新的序列放入另一片存储空间


def odd(x):
    return x % 2  # 可以被2整除返回0即False，不能被2整除返回1即True，判断奇偶数


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
show = filter(odd, list2)  # 应为偶数返回0即False，奇数返回1为True，所以只会留下奇数
print(list(show))  # 打印结果[1, 3, 5, 7, 9]

# 当然还可以用lambda表达式定义的匿名函数,这样可以看出精简许多
show = filter(lambda x: x % 2, list2)
print(list(show))  # 打印结果[1, 3, 5, 7, 9]


def add(x):
    return x + 10


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
show = map(add, list2)  # 第一个参数为函数
print(list(show))  # 打印结果：[11, 12, 13, 14, 15, 16, 17, 18, 19]
show = map(lambda x: x + 10, list2)  # 第一个参数为lambda表达式定义的匿名函数
print(list(show))  # 打印结果：[11, 12, 13, 14, 15, 16, 17, 18, 19]
