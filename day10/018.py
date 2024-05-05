def MyFirstFunction(name):
    '函数定义过程中的name是叫形参，因为Ta只是一个形式，表示占据一个参数位置'  # 注意这里不是叫字符串，而是自己写的函数文档用' '来包裹
    # 如果要多个句子可以用'''   '''三重引号，如下
    # '''
    # 数定义过程中的name是叫形参。
    # 因为Ta只是一个形式，表示占据一个参数位置。
    # '''
    print('传递进来的' + name + '叫做实参，因为Ta是具体的参数值！')


MyFirstFunction('哈哈')  # 函数调用
print(MyFirstFunction.__doc__)  # 调用方式为：函数.__doc__，用.是因为__doc__是函数的一个属性，属性和方法都要用. ，注意doc两边是双下划线__ __
# 打印的函数文档为：函数定义过程中的name是叫形参，因为Ta只是一个形式，表示占据一个参数位置
help(MyFirstFunction)  # 函数文档也可以通过help来查看，就像BIF内置函数那里学的一样
# 输出结果：
# MyFirstFunction(name)
# 函数定义过程中的name是叫形参，因为Ta只是一个形式，表示占据一个参数位置




def MyThirdFunction(name, word):
    print(name + '->' + word)


MyThirdFunction('Q.M.F.', '改变世界')  # Q.M.F.->改变世界
MyThirdFunction('改变世界', 'Q.M.F.', )  # 改变世界->Q.M.F.
# 上面参数位置发生转换，打印结果也会不同
# 如果想要参数位置无论在哪，打印结果要相同，可以使用关键字进行传参
MyThirdFunction(word='改变世界', name='Q.M.F.')  # 加上参数关键字，这样即便顺序不一样执行结果仍然相同
# 结果：Q.M.F.->改变世界



def MyForthFunction(name='嘻嘻', word='xixi'):  # 这里函数定义时已经给了参数默认值，即便不传参数仍有正常输出
    print(name + '->' + word)


MyForthFunction()  # 如果定义时没有给出参数默认值，找个就会报错
# 不传任何参数使用默认参数，打印结果：嘻嘻->xixi
MyForthFunction('Q.M.F.')  # 传一个，打印结果：Q.M.F.->xixi
MyForthFunction(word='改变世界')  # 传一个，打印结果：嘻嘻->改变世界，注意因为word在第二个参数，故要用关键字指明是哪个参数


def MyFifthFunction(*param):  # *param代表参数可变
    print('参数长度为:' + str(len(param)))  # 用可变参数，会将传来的参数放在一个元组中
    print(param)  # 参数放在元组中，所以这里打印的是一个元组
    print(param[0:len(param)])  # 打印元组中第一个元素


MyFifthFunction(1, 2, 3, 4, 5, 6, 7)
# 运行结果为
# 参数长度为:7             参数元组中元素个数
# (1, 2, 3, 4, 5, 6, 7)  参数元组
# 1                       参数中第一个元素


# 定义一个可变参数和固定参数
# def MySixthFunction(word, *alter):  #方法一 alter为可变参数，word为固定参数
def MySixthFunction(*alter, word):  # 方法二，调换一下参数顺序，alter为可变参数，word为固定参数
    print('可变参数为:', end='')
    print(alter)
    print('固定参数为:', end='')
    print(word)


# MySixthFunction('haha', 'xixi', 1, 2, 3)  # 如果按方法二，这样传参会报错，因为这里所有参数都会传给可变参数alter，就没有参数穿个word参数了，所以要添加关键参数
# 方法一定义函数运行结果为
# 可变参数为:('xixi', 1, 2, 3)
# 固定参数为:haha
MySixthFunction('haha', 'xixi', 1, 2, 3, word=4)
# 方法二定义函数运行结果为
# 可变参数为:('haha', 'xixi', 1, 2, 3)
# 固定参数为:4
