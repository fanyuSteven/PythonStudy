# def recursion1():
#     return recursion1()  # 这里递归会一直递归下去直到内存耗光，但python3提前设定了递归最多只能递归100层就停止
#
#
# recursion1()
#
# # 但如果你想要递归更多层可以用sys包中的setrecursionlimit()函数
# import sys
#
# sys.setrecursionlimit(1000)  # 这样就能修改最大递归层数为1000层

x = int(input('请输入一个数字求阶乘: '))


def factorial(x):  # 求阶乘的函数，用递归实现
    if (x == 1):  # 递归先写出什么时候退出递归
        return 1
    return x * factorial(x - 1)  # 然后写出递归体，即实现什么功能


print(factorial(x))

# 循环实现求阶乘

fact = 1
while (x >= 1):
    fact = fact * x
    x = x - 1
print(fact)
