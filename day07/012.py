# 比较操作符>、<、==、<=、>=、!=，返回bool值
list1 = [123]
list2 = [234]
print(list1 > list2)  # False
list1 = [123, 456]
list2 = [234, 123]
print(list1 > list2)  # False,比较操作先从两个列表的第一个元素开始比较，若不同则返回比较结果，后面的就不在进行比较
list3 = [123, 234]
print(list1 > list3)  # True，若第一个元素相同再比较两个序列的第二个元素

member1 = ['abc', 'abc']
member2 = ['acd', 'abc']
print(member1 < member2)  # 字符串列表比较大小是从字符串第一个字符的ASCII码大小开始比较

# 逻辑操作符and、or......，返回bool值
print((list1 == list2) and (list1 > list3))

# 拼接操作符 + ，注意不是加法，拼接操作符两侧必须是序列才能拼接，而不能添加元素，添加元素上面学了
list4 = list1 + list2
print(list4)  # 打印结果[123, 456, 234, 123]
# list5 = list1 + 'hahaha'  # 这个是不行的，因为列表和元素不能拼接会报错

# 重复操作符
list3 *= 5  # 相当于list3 = list3 * 5
print(list3)  # list3重复5次

# 成员关系操作符 in, not in（用于判断某一元素在(in)或不在(not in)某序列中），返回bool值
print(123 in list1)
member = ['小甲鱼', '小布丁', '哈哈', '嘻嘻', '黑夜', '迷途', '啊呜', '略略', '林小溪']
print('小甲鱼' in member)
print('hahaha' in member)
print('hahaha' not in member)

# 访问列表中的列表中的元素
member = ['小甲鱼', ['haha', 'xixi'], '小布丁', '黑夜', '迷途', '林小溪']
# 访问xixi
print(member[1][1])
# 判断haha是否在member元素的列表元素中
print('haha' in member[1])

# 列表的其他一些方法
# count()方法，返回某元素出现次数
list3 = [123, 234, 123, 234, 123, 234, 123, 234, 123, 234]
print(list3.count(123))  # 123在list3中出现5次

# index()方法,index(元素，[startIndex]，[endIndex])方法,返回某元素第一次出现的位置,[]是可选添加参数，若指定则从该区间找，如果不指定就整个列表找
print(list3.index(234))  # 234第一次出现在1号位置
print(list3.index(234, 5, 9))  # 234在5-9号位第一次出现位置

# reverse()方法，调转列表元素顺序
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list5)
list5.reverse()
print(list5)

# sort(),给列表从小到大排序，里面元素必须是整型或浮点型，使用的是归并排序
list6 = [3, 5, 2, 1, 56, 36, 7, 10, 28]
print(list6)
list6.sort()
print(list6)
# 如果要从大到小排
list6 = [3, 5, 2, 1, 56, 36, 7, 10, 28]
list6.sort(reverse=True)
print(list6)

# 关于取列表的分片（子列表）拷贝到另一列表中需注意到的东西
list6 = [3, 5, 2, 1, 56, 36, 7]
list7 = list6[:]  # 取出list6中的分片拷贝到另一个空间，该空间给一个名字为list7，前面学过python中变量只是给某一空间的命名而已
list8 = list6  # 这个操作相当于把list8这个名字也匹配上list6所命名的空间，故list6和list8是同一个东西，排序后列表相同
list6.sort()
print(list6)
print(list7)
print(list8)
