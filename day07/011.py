member = ['小甲鱼', '小布丁', '哈哈', '嘻嘻', '黑夜', '迷途', '啊呜', '略略', '林小溪']
print(member)
print(member[0])  # 列表相当于数组从0开始取数据也类似
print(member[1])

# 交换member[0]和member[1]元素位置
temp = member[0]
member[0] = member[1]
member[1] = temp
print(member)

# 从列表删除元素
# 方法1，已知列表中某一元素并删除 remove( )方法
member.remove('小甲鱼')
print(member)

# 方法2，删除列表某一位置的元素  使用del语句
del member[1]  # del是一个语句，不是方法，member.del(1)是错的，方法才要有.()
print(member)
# del member则会删除整个列表

# 方法3，列表因为用栈存储故可以用  pop( )方法
print(member.pop())  # 栈是从栈尾开始弹出元素
print(member)
print(member.pop(1))  # 也可以弹出某一位置的元素
print(member)

# 列表分片，取出其中一段连续的子列表，用法  列表名[startIndex:endIndex+1]
member = ['小甲鱼', '小布丁', '哈哈', '嘻嘻', '黑夜', '迷途', '啊呜', '略略', '林小溪']
print(member)
print(member[1:3])  # 输出member[1]和member[2]，因为3 - 1 = 2只输出两个元素，这也是为什么上面endIndex+1
print(member[:3])  # 前面未写则从最开始到3-1
print(member[1:])  # 后面未写则从1到最后
print(member[:])  # 前后都未写则从最开始到结尾
member2 = member[2:5]
print(member2)
