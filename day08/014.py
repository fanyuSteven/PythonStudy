str1 = 'I love fishc.com'
# 字符串与元组相同，一旦定义不可以在里面插入和删除元素
# 访问字符串切片（子串），与元组相同
print(str1[5])
print(str1[:6])
# 插入字符
str2 = str1[:6] + '插入的字符串' + str1[6:]  # 记住切片是放在另一个存储空间中，拼接后任然放在另一个存储空间中并命名为str2，注意中间拼接类型是字符串类型，元组、序列拼接中间也要是相同的元组、序列的类型
print(str2)

str3 = 'haha'
print(str3)
print(str3.capitalize())

str4 = 'HAHA'
print(str4)
print(str4.casefold())

print(str4.center(40))

print(str4.count('A'))

print(str4.endswith('HA'))
print(str4.endswith('H'))

str5 = 'I\tlove\tfishc.com!'
print(str5.expandtabs())


