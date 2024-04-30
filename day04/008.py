# 按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，
# 写一个程序，当用户输入分数，自动转换为ABCD的形式打印。

# 方法一：纯if
score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
    print('A')
if 90 > score >= 80:
    print('B')
if 80 > score >= 60:
    print('C')
if 60 > score >= 0:
    print('D')
if score < 0 or score > 100:
    print('输入错误！')
# 方法二：if - else
score = int(input("请输入您的成绩："))  # 输入成绩
if score >= 90:
    print("A")
else:
    if (score < 90) and (score >= 80):
        print("B")
    else:
        if score >= 60 and score < 80:
            print("C")
        else:
            if score > 0 and score < 60:
                print("D")
            else:
                print("输入成绩错误")

# 方法三：if - elif，elif相当于C语言中的else if，就不用再像方法一那样写else: 再if(条件):,太多了
if score >= 90:
    print("A")
elif (score < 90) and (score >= 80):
    print("B")
elif score >= 60 and score < 80:
    print("C")
elif score > 0 and score < 60:
    print("D")
else:
    print("输入成绩错误")
