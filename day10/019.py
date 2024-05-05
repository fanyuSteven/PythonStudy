def discounts(price, rate):
    # 函数里面定义的变量是局部变量，作用域在函数里面
    final_price = price * rate  # 最终价格，注意变量是可以带 _ 下划线的，不要以为是别的东西
    old_price = 88  # 这里试图修改全局变量，python会在函数的空间内再创建一个同名的变量，而不会使用全局变量
    print('函数里的修改后old_price的值是：', old_price)#所以这里old_price值在函数里虽然修改，但只是修改了函数里的这个变量，而全局变量并没有修改
    return final_price


# 函数外面定义的变量是全局变量，作用域是全局
old_price = float(input('请输入原价：'))  # float是将输入数据转化为浮点型
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price, rate)
# print('打折后价格是：', final_price)#这里会报错，因为函数里的局部变量旨在函数里面有用，而在外面是无法访问的
print('修改后old_price的值是：', old_price)
print('打折后价格是：', new_price)
