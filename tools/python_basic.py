# 最简单基本的命令
# t = 3
# s = "test"
# str1 = 'python'
# a = input("input str: ")
# b = int(input("int input: "))
# c = float(input('input float: '))
# t = 3; s = 'world'; 多条语句在一行就要用分号隔开
# print(a)
# print(b)
# print(t)

# 练习
# a = 2
# b = "jinqianbao"
# c = int(input("enter int: "))
# print(a + c)

# 基本的数字运算
# a = 9
# b = 5.0
# a += 1
# a *= b + 1
# a -= 1
# b /= 2
# a %= 2
# t = a + b  # 加减乘除和普通运算函数中，如果参与运算的有小数，结果一定带小数
# c = a / b  # 单纯的除法——除法的结果一定带小数（9 / 3 = 3.0）
# d = a // b  # 只取除法结果的整数部分（9 // 5 = 1）（9 // 5.0 = 1.0 ）
# e = a % b
# f = a ** b  # a的b次方
# g = pow(a, b)  # a的b次方
# h = abs(a)
# i = round(2.336, 2)  # 四舍五入保留两位小数
# j = round(2.336)  # 四舍五入保留整数
# h = max(a, b, c, d)
# k = min(a, b, b, c)
# m = int(3.14)  # 等于3
# n = int("3")  # 等于3
# o = int("2.72")  # 等于2
# p = float("2.72")  # 等于2.72
# q = float("2")  # 等于2.0
# x, y, z = 1, 2.2, 3  # 多变量同时初始化

# 练习
# a, b = 3, 2
# c = 10 / b  # c = 5.0
# d = a ** b  # d = 9
# e = d // 5.0  # e = 1.0
# a *= b + 3  # a = 15
# f = min(a, b, c)  # f = 2

# 字符串操作
# a = "菌菌"
# b = "爱Smart"
# c = a + b  # c = "菌菌爱Smart"
# d = a * 3  # d = "菌菌菌菌菌菌"
# e = b[3]  # e = "a"  正着数从0开始
# f = b[-2]  # f = "r"  倒着数从-1开始
# g = b[3:-2]  # g = "a" 左闭右开，取左不取右
# h = b[:-2]  # h = "爱Sma"
# i = b[3:]  # i = "art"
# j = b[:]  # j = "爱Smart"
# k = str(3.14)  # k = "3.14"
# l = b.upper()  # l = "爱SMART"
# m = b.lower()  # m = "爱smart"
# n = len(b)  # n = 6
# o = "X:{},Y:{}".format(a, b)  # o = "X:菌菌,Y:Smart"
# p = "X:{1},Y:{0}".format(a, b)  # p = "X:Smart,Y:菌菌"

# print输出
# print("太", "好", "啦", sep="！", end="! lalala\n")  # sep——separate，分隔字符串, end——结尾
# print("太", "好", "啦")  # 不写sep=相当于sep=" "，用空格分隔；不写end=相当于end=\n，用换行符结尾
# print("黑\t色", "白\t色", sep='\n', end="~\n")

# if语句
# score = int(input("pls enter ur score: "))
# if score >= 90:
#     s = "bravo!"
# elif score >= 80:
#     s = "not bad~"
# else:
#     s = "study harder!"
# print(s)

# a = int(input("pls enter int1: "))
# b = int(input("pls enter int2: "))
# if a > 90 and b > 90:
#     print(a + b)
# elif a < 60 or b < 60:
#     print(a * b)
# else:
#     print(a - b)

# 循环语句
# a = 5
# while a > 0:
#     print(a)
#     a -= 1
#
# list1 = [1, 2, 3, 4, 5, 6, 7]
# sum1 = 0
# for i in range(0, 10, 1):  # rang(a)等同于range(0, a, 1)，注意：取出的数是不包含数a的，是0——a-1
#     sum1 += i
#     print(sum1)
# sum1 = 0
# num = [1, 2, 3, 5, 6, 7]
# for i in num:
#     print(i)
#     sum1 += i
# print(sum1)

# ans = 0
# step = 1
# for i in range(1, 101):
#     step *= i
#     ans += step
# print(ans)

# l1, l2 = 0, 0
# for l1 in range(0, 36):
#     for l2 in range(0, 36):
#         if l1 + l2 == 35 and l1 * 2 + l2 * 4 == 94:
#             print(l1, l2)

# 列表 中括号中可以有任何类型，任何数量的内容
# b = 5
# a = [1, b, "学习"]
# # 元组
# c = (1, a, "hello")
# # 集合
# d = {1, c, "world"}
# # 字典
# e = {"first": 55, "second": 66}

# def test(a, b):
#     print(a + b)
#     return a - b
#
#
# a = test(3, 5)
# print(a)

# import math
#
# a = lambda x, y: x + y  # 相当于声明a(x, y) = x + y
# print(a(3, 5))
# b = a(5, 5)
# print(math.pow(b, 2))
# print(int(math.sqrt(b)))

# class TestCase:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def logintest(self, a):
#         print("start test login: ", self.x + a)
#
#     def re(self):
#         return self.y
#
#
# class newTest(TestCase):
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#     def ge(self):
#         return self.y + self.z
#
#
# aA = TestCase(6, 6)
# aA.logintest(4)
# print(aA.re())
# bB = newTest(4, 5, 6)
# print(bB.ge())
#
# a = open("/Users/yinjun/mytest_shell/tone", "r+")
# a.write("666python")
# a.writelines(["7", "8", "9"])
# print(a.read(10))
# # print(a.read())
# b = a.readlines()
# print(b)
# a.close()

# a = eval(input("pls enter anything: "))
# b = "my name is %s, I'm %d years old~" % ("junjun", 26)
# print(b)
# c = b.replace("junjun", "string")
# print(c)
# print(type(a))

import datetime
# name = "string"
# age = 22
# #today = datetime.date.today()
# now = datetime.datetime.now()
# nowday = now.date()
# nowtime = now.time()
# print(f"hihi my name is {name} and im {age} years old~")
# print(f"now is {now}")
# print(f"now is {nowtime:%H:%M:%S}")
# print(f"today is {nowday:%Y-%m-%d}")


# def testone(compute):
#     res = compute(1, 2)
#     print(f"the ans is: {res}")
#
#
# testone(lambda x, y: x + y)
import time

# a = open("/Users/yinjun/newtest/tryit", "r", encoding="UTF-8")
# print(type(a))
# print(a.read())
# l = a.readlines()
# print(l)
# for i in l:
#     print(i)
# for line in a:
#     print(line)
#     time.sleep(3)
# a.close()

# with open("/Users/yinjun/newtest/tryit", "a+", encoding="UTF-8") as a:
#     a.write("my new new hello everybody!\n")
#     a.flush()
#     time.sleep(10)
# try:
#     a = open("/Users/yinjun/tt", "r", encoding = "UTF-8")
# except Exception as e:
#     print(e)
# else:
#     for line in a:
#         print(line)
# finally:
#     print("Im f-King!")
#     a.close()

# import json
#
# data = [{"name": "菌菌", "age": 20}, {"name": "sy", "age": 25}]
# dataj = json.dumps(data, ensure_ascii=False)
# print(type(dataj))
# print(dataj)
# datap = json.loads(dataj)
# print(type(datap))
# print(datap)


# class Student:
#     def __init__(self, x, y, z):
#         self.name = x
#         self.gender = y
#         self.age = z
#
#     def rest(self):
#         print(self.name)
#         print(self.gender)
#         print(self.age)
#
#
# stu1 = Student("juju", "femal", 20)
# stu1.rest()


arr = input("pls input arr: ").split(",")
print(arr)


def solution():
    fre = {}
    idx = {}
    for i in range(len(arr)):
        if fre.get(arr[i]) is None:
            fre[arr[i]] = 0
            idx[arr[i]] = i
        fre[arr[i]] += 1
    tmp = list(idx.keys())
    tmp.sort(key=lambda x: (-fre[x], idx[x]))
    return tmp


print(solution(), sep=",")