# 列表，相当于数组，但数组里面只能是同种数据类型，但列表中各元素的数据类型可以不同可以相同
# 普通列表
member = ['小甲鱼', '小布丁', '哈哈', '嘻嘻', '黑夜', '迷途']  # 列表用中括号[ ]括起来
numer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 混合列表，可以存放各种数据类型，字符串，整型，浮点型，列表，对象
mix = ['小甲鱼', 1, 3.14, numer, member]
# 当不知道想往列表中存放什么数据时，可以先创建一个空列表，里面元素可以之后添加
empty = []  # 空列表

# 往列表中添加元素
# 用（append方法）
print(len(empty))  # 最初empty长度为0
empty.append('哈哈')  # extend中只能添加一个元素
for i in empty:
    print(i, end=' ')
print('\n')

# 用extend方法
empty.extend(['嘻嘻', '略略'])  # extend方法能多个元素，但参数是一个列表才行
for i in empty:
    print(i, end=' ')
print('\n')

# 用insert方法
# 前两个方法只能在列表末尾添加元素，而insert方法可以在任何位置添加一个或多个元素
empty.insert(0, '啊呜')  # insert方法有两个参数，第一个是插入位置，注意位置是从0开始的，第二个是插入元素
for i in empty:
    print(i, end=' ')
print('\n')
empty.insert(2, ['haha','xixi','luoluo'])  # 第二个参数可以是单个元素，也可以是一个列表
for i in empty:
    print(i, end=' ')
print('\n')