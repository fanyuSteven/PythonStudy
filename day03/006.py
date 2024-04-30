a = 5
a = a + 5
a += 3  # 相当于a = a + 3
print(a)
b = 3
b -= 1  # 相当于 a = a - 1
print(b)
a = b = c = d = e = f = g = 10
a += 1
b -= 3
c *= 10
d /= 8  # 不再像C语言一样整数除法为小数然后舍去小数部分，python是直接把结果转为正常除法得到小数。
e //= 8  # 这个就像C语言一样的除法，舍弃小数。学术名字叫地板除法。
f %= 8  # 正常取余运算
g **= 2  # 幂运算，即g^2 —— g的2次方
print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))
print('d = ' + str(d))
print('e = ' + str(e))
print('f = ' + str(f))
print('g = ' + str(g))
