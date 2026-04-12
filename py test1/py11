# 1.作用域
#含义：变量的作用范围，决定了变量在程序中的可见性和生命周期
# 1.1 全局作用域
# 在函数外部定义的变量具有全局作用域，可以在函数内部访问和修改
# name = "bingbing"  #全局变量
# def func():
#     print(name)  #在函数内部访问全局变量
# func()  #输出：bingbing


# a = 100 #全局变量

# def func1():
#     print(a)  #在函数内部访问全局变量
# func1()  #输出：100  
# print(a)  #在函数外部访问全局变量，输出：100

# #1.2 局部作用域
# # 在函数内部定义的变量具有局部作用域，只能在函数内部访问和修改
# def func2():
#     age = 18  #局部变量
#     print(age)  #在函数内部访问局部变量
# func2()  #输出：18
# print(age)  #在函数外部访问局部变量，会报错，age未定义    

# num = 10  #全局变量
# def funa(): #调用函数，输出：10
#     num = 20  #局部变量，函数内部的num与函数外部的num是两个不同的变量

#     print(num)  #在函数外部访问全局变量，输出：20
# funa()  #调用函数，输出：10

# def funb():
#     global num  #声明num是一个全局变量，告诉Python在函数内部使用全局变量num，而不是创建一个新的局部变量
#     num = 40 
#     #修改全局变量num的值为40
#     # num = 30  #局部变量，函数内部的num与函数外部的num是两个不同的变量
#     print(num)  #在函数内部访问全局变量，输出：30
     
# funb()  #调用函数，输出：10
# #在函数内部修改全局变量需要使用global关键字，否则会创建一个新的局部变量，导致全局变量的值不变
# print(num)  #在函数外部访问全局变量，输出：40

# def study():
#     global num ,age #声明num是一个全局变量，告诉Python在函数内部使用全局变量num，而不是创建一个新的局部变量
#     num = "python基础"
#     age = 18
#     print("我正在学习"+num+str(age))#str(age)将整数类型的age转换成字符串类型，才能与字符串类型的num进行拼接
#     print(f"我正在学习{num}{age}" )  #在函数内部访问全局变量，输出：我正在学习python基础
# study()  #调用函数，输出：我正在学习python基础
# print(num,age)  #在函数外部访问全局变量，输出：python基础


# def work():
#     print("我正在工作"+num)
# work()  #调用函数，输出：我正在工作python基础


#nonlocal 关键字：在函数内部修改外层函数的变量
# def outer():
#     num = "python基础"
#     age = 38
#     def inner():
#         nonlocal num,age #声明num是一个外层函数的变量，告诉Python在函数内部使用外层函数的变量num，而不是创建一个新的局部变量
#         num = "python高级"
#         age = 28
#         print("我正在学习"+num+str(age))#str(age)将整数类型的age转换成字符串类型，才能与字符串类型的num进行拼接
#         print(f"我正在学习{num}{age}" )  #在函数内部访问外层函数的变量，输出：我正在学习python高级
#     inner()  #调用内层函数，输出：我正在学习python高级
#     print(num,age)  #在外层函数中访问内层函数修改后的变量，输出：python高级 28
# outer()  #调用外层函数，输出：我正在学习python高级  python高级 28

#2.匿名函数
#2.1 lambda表达式
# lambda表达式是一种匿名函数，可以用来创建简单的函数对象，lambda表达
#式的语法格式为：lambda 参数列表: 表达式
# lambda表达式可以接受任意数量的参数，但只能有一个表达式，表达式的结果就是函数的返回值
# add = lambda a, b: a + b  #创建一个匿名函数，接受两个参数a和b，返回a和b的和
# print(add(1, 2))  #调用匿名函数，输出：3
# print(add("hello ", "world"))  #调用匿名函数，输出：hello world


# def add(a, b):
#     return a * b
# print(add(2,5)) #10

# add = lambda a, b: a * b  #创建一个匿名函数，接受两个参数a和b，返回a和b的积
# print(add(2, 5))  #调用匿名函数，输出：10

# # 2.2 lambda的参数形式
# # 2.2.1 无参数
# no_arg = lambda: "hello world"  #创建一个无参数的匿名函数，返回字符串"hello world"
# print(no_arg())  #调用匿名函数，输出：hello world

# #2.2.2 一个参数
# square = lambda x: x ** 2  #创建一个接受一个参数x的匿名函数，返回x的平方
# print(square(5))  #调用匿名函数，输出：25
# # 2.2.3 多个参数
# power = lambda x, y: x ** y  #创建一个接受两个参数x和y的匿名函数，返回x的y次幂
# print(power(2, 3))  #调用匿名函数，输出：8

# # 2.2.4 关键字参数
# fund = lambda *args, **kwargs: (args, kwargs)  #创建一个接受任意数量的位置参数和关键字参数的匿名函数，返回一个包含位置参数和关键字参数的元组
# print(fund(1, 2, 3, a=4, b=5))  #调用匿名函数，输出：((1, 2, 3), {'a': 4, 'b': 5})

# # 2.2.5 lambda 结合if判断
# a = 5
# b = 8
# #为真结果 if 判断条件 else 为假结果
# print("a大于b") if a > b else print("a小于等于b")  #调用匿名函数，输出：a小于等于b
# comp = lambda a , b: "a大于b" if a > b else "a小于等于b"  #创建一个接受两个参数a和b的匿名函数，返回一个字符串，表示a和b的大小关系
# print(comp(5, 8))  #调用匿名函数，输出：a小于等于b
# print(comp(10, 8))  #调用匿名函数，输出：a大于b
# lambda表达式适用于需要一个简单函数对象的场景，可以用来简化代码，提高代码的可读性和可维护性，但不适合复杂的函数逻辑，应该使用普通的函数定义来实现复杂的功能

#3. 内置函数
#查看所有的内置函数
# import builtins
# print(dir(builtins))  #输出所有的内置函数
# # 大写字母开头一般是内置常量名
# #小写字母开头一般是内置函数名

# abs()  #返回数字的绝对值
# print(abs(-5))  #调用内置函数abs，输出：5

# #sum()  #返回可迭代对象中所有元素的和
# print(sum([1, 2, 3, 4, 5])) #只能放可迭代对象  
#  #调用内置函数sum，输出：15

#  # min()  #返回可迭代对象中最小的元素
# print(min([1, 2, 3, 4, 5]))  #调用内置函数min，输出：1

# # max()  #返回可迭代对象中最大的元素
# print(max([1, 2, 3, 4, 5]))  #调用内置函数max，输出：5

# print(max(-10,5,key=abs))  #调用内置函数max，输出：-10

# # zip()  #将多个可迭代对象中的元素打包成一个个元组，返回一个可迭代对象
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# zipped = zip(a, b)  #调用内置函数zip，返回一个可迭代对象
# print(list(zipped))  #将可迭代对象转换成列表，输出：[(1, 'a'), (2, 'b'), (3, 'c')]

# map()  #将一个函数作用于可迭代对象中的每个元素，返回一个可迭代对象
# li = [1, 2, 3, 4, 5]
# # def funa (x):
# #     return x ** 2
# funa = lambda x: x ** 2  #创建一个匿名函数，接受一个参数x，返回x的平方
# mp = map(funa, li)  #调用内置函数map，将函数funa作用于列表li中的每个元素，返回一个可迭代对象
# print(mp)
# # 用for循环取出可迭代对象中的元素，输出：1 4 9 16 25
# # for i in mp:  #遍历可迭代对象，输出：1 4 9 16 25
# #     print(i)
# # 转换成列表，输出：[1, 4, 9, 16, 25]
# print(list(mp))  #调用内置函数list，将可迭代对象转换成列表，输出：[]
# # map对象只能被迭代一次，迭代后就会被消耗掉，再次迭代会得到一个空的可迭代对象
# print(list(mp))  #输出：[]

# reduce()  #将一个函数作用于可迭代对象中的元素，进行累积计算，返回一个结果
# from functools import reduce
# add=reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  #调用内置函数reduce，将一个匿名函数作用于列表中的元素，进行累积计算，输出：15
# #reduce()函数接受两个参数，第一个参数是一个函数，第二个参数是一个可迭代对象，reduce()函数会将可迭代对象中的元素依次传递给函数进行计算，最终返回一个结果
# print(add)

# a = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])  #调用内置函数reduce，将一个匿名函数作用于列表中的元素，进行累积计算，输出：120
# print(a)

# 4.拆包 和解包
# 4.1 拆包 
#对于多个函数中的对各返回数据，去掉元组，列表或字典，直接获取其中的元素
# tua = (1, 2, 3,4,5,6,7,8,9)
# # print(tua)  #(1, 2, 3)
# # a, b, c = tua  #将元组中的元素依次赋值给变量a、b、c
# # print(a)  #1
# # print(b)  #2
# # print(c)  #3
# # print(a, b, c)  #1 2 3
# a,*b =tua  #将元组中的第一个元素赋值给变量a，剩余的元素赋值给变量b，b是一个列表
# print(a,b)
# c, *d = b  #将元组中的第一个元素赋值给变量c，剩余的元素赋值给变量d，d是一个列表
# print(c,d)

# 4.2 解包
#导入包方式1 
import mokuai.reg  #导入mokuai包中的reg模块，使用包名.模块名的方式调用函数
# mokuai.reg.reg()  #调用mokuai包中的reg模块中的reg函数

# #导包方式2

# 4.7 __all__ 变量：定义在模块中的__all__变量是一个列表，包含了模块中可以被导入的函数、类和变量的名字，当使用from 模块名 import *的方式导入模块时，只有__all__变量中列出的函数、类和变量会被导入到当前命名空间中，其他的函数、类和变量不会被导入
# 在mokuai模块中定义__all__变量，列出可以被导入的函数、类和变量的名字
# __all__ = ['reg']  #定义一个列表，包含了模块中可以被导入的函数、类和变量的名字
# from mokuai import *  #从mokuai模块中导入所有的
# 函数、类和变量，使用函数名直接调用函数
# reg()  #调用mokuai模块中的reg函数，输出：这是一个注册函数
# 使用from mokuai import *的方式导入模块时，只有__all__变量中列出的函数、类和变量会被导入到当前命名空间中，其他的函数、类和变量不会被导入，所以只能调用reg函数，不能调用其他的函数、类和变量
# 如果没有定义__all__变量，使用from mokuai import *的方式导入模块时，所有的函数、类和变量都会被导入到当前命名空间中，可以直接调用模块中的所有函数、类和变量，但不推荐使用这种方式导入模块，因为会导致命名冲突和代码混乱
#  
from mokuai import *  #从mokuai包中导入所有模块，使用函数名直接调用函数
reg.reg()  #调用mokuai包中的reg模块中的reg函数，输出：这是一个注册函数