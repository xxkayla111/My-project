# # 1.递归函数
# # 含义：函数调用自身的函数，递归函数必须有一个终止条件，否则会导致无限递归，最终导致栈溢出错误。
# def add():
#     s= 0
#     for i in range(1, 101):
#         s += i
#     print(s)
# add()

# # 2.递归函数
# def add(n):
#     # 终止条件, n= 1时，返回1
#     if n == 1:
#         return 1
#     # 递归调用，n= 5时，返回5 + add(4)，add(4)返回4 + add(3)，add(3)返回3 + add(2)，add(2)返回2 + add(1)，add(1)返回1
#     return n + add(n - 1)
# #计算1到100的和
# print(add(100))
# # 斐波那契数列：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(10))
# #优点：递归函数的代码简洁，易于理解和维护，适合解决一些复杂的问题，如树形结构、图形结构等。
# #缺点：递归函数的性能较差，尤其是当递归深度较大时，会导致栈溢出错误。此外，递归函数可能会重复计算相同的子问题，导致效率低下。

# #2.闭包函数
# def outer(): #·外部函数
#     x = 10 #外部函数的局部变量
#     def inner(): #内部函数
#         print(x) #内部函数可以访问外部函数的局部变量
#     return inner #外部函数返回内部函数的引用
# f = outer() #调用外部函数，返回内部函数的引用，并赋值给变量f
# f()  # 输出10

#带参数的闭包函数
# def outer(m):
#     n = 10
#     def inner(o):
#         print('计算结果：',m+n+o)
#     return inner
# f = outer(5) #调用外部函数，传入参数5，返回内部函数的引用，并赋值给变量f
# f(15) #调用内部函数，传入参数15，输出计算结果：30
# #id()函数：用于获取对象的内存地址，返回一个整数值，表示对象在内存中的位置。每个对象都有一个唯一的内存地址，可以通过id()函数来获取。
# a = 1
# b = 1
# print(id(a)) #输出a的内存地址
# print(id(b)) #输出b的内存地址

# # 2.2 每次开启内函数都在使用同一份闭包变量
# def outer(m):
#     print('外部函数的参数：',m)
#     def inner(n):
#         print('内部函数访问外部函数的参数：',n)
#         return m + n  #在inner函数中返回m和n的和
#     return inner
# ot = outer(5) #调用外部函数，传入参数5，返回内部函数的引用，并赋值给变量ot
# print(ot(10)) #调用内部函数，传入参数10，输出内部函数访问外部函数的参数：10，并返回15

# print(ot(20)) #调用内部函数，传入参数20，输出内部函数访问外部函数的参数：20，并返回25

# 3.装饰器函数
# def test1():
#     print('这是一个测试函数')
# def test(fn):
#     print('开始注册')
#     print('注册成功')
#     fn() #调用传入的函数
# test(test1) #调用test函数，传入test1函数作为参数，输出开始注册、注册成功和这是一个测试函数

# 在不改变原有函数的基础上，给函数添加新的功能，这就是装饰器函数的作用。装饰器函数通常使用@符号来修饰原有函数，使其具有新的功能。
# def decorator(fn):
#     def wrapper():
#         print('这是装饰器函数，给原有函数添加新的功能')
#         fn() #调用原有函数
#     return wrapper
# @decorator #使用装饰器函数修饰原有函数
# def test2():
#     print('这是一个测试函数')
# test2() #调用test2函数，输出这是装饰器函数，给原有函数添加新的功能和这是一个测试函数

# def test(fn):
#     print('登录')
#     print('注册')
#     fn() #调用传入的函数
# def test2():
#     print('发送消息')
# test(test2) #调用test函数，输出登录和注册

# 1.标准版装饰器
# def send():
#     print('发送消息')
# # send() #调用send函数，输出发送消息
# def send2():
#     print('转账520')
# #闭包的三个条件
# # 1.函数嵌套
# # 2.内函数要使用外函数的局部变量
# # 3.外函数的返回值是内函数的函数名
# def outer(fn):
#     def inner():
#         print('这是内函数')
#         fn() #调用传入的函数  =send()，输出发送消息

#     return inner
# ot = outer(send2) #调用外函数，传入send函数作为参数，返回内函数的引用，并调用内函数，输出这是内函数和发送消息   
# ot() #调用内函数，输出这是内函数和发送消息

# 2.语法糖
#格式：@装饰器函数名

# def outer(fn):
#     def inner():
#         print('登录。。。')
#         fn() #调用传入的函数  =send()，输出发送消息

#     return inner
# @outer #使用装饰器函数修饰send函数，使其具有新的功能
# # 装饰器名称后面不要加括号，否则会立即调用装饰器函数，而不是返回装饰器函数的引用
# def send():
#     print('发送消息:笑死我了！')
# send()
# @outer
# def send2():
#     print('转账520')
# send2()

# 被装饰的函数有参数
# def outer(fn):
#     def inner(*args, **kwargs): #使用*args和**kwargs来接受被装饰函数的参数
#         print('登录。。。')
#         fn(*args, **kwargs) #调用传入的函数，并传入参数

#     return inner
# # @outer  等价于 send = outer(send)  #调用外函数，传入send函数作为参数，返回内函数的引用，并调用内函数，输出登录。。。和发送消息:笑死我了！张三
# def send(*args, **kwargs):
#     print(args, kwargs) #输出被装饰函数的参数
#     # print(f'发送消息:笑死我了！{args[0]}, {kwargs.get("name", "未知用户")}')#调用被装饰的函数，并传入参数，输出登录。。。和发送消息:笑死我了！张三
# # send('susu', name='张三') #调用被装饰的函数，并传入参数，输出登录。。。和发送消息:笑死我了！张三
# # send('susu', name='李四') #调用被装饰的函数，并传入参数，输出登录。。。和发送消息:笑死我了！李四
# ot = outer(send) #调用外函数，传入send函数作为参数，返回内函数的引用，并调用内函数，输出登录。。。和发送消息:笑死我了！张三
# ot()
# # ot("susu", name='李四') #调用内函数，传入参数，输出登录。。。和发送消息:笑死我了！李四 

#多个装饰器
# 第一个装饰器
def decol(fn):
    def inner():
        return'哈哈哈'+fn()+'哈哈哈'
    return inner
# 第二个装饰器
def decol2(fn):
    def inner():
        return '嘻嘻嘻' + fn() + '嘻嘻嘻'
    return inner
# 第三个装饰器
def decol3(fn):
    def inner():
        return '嘿嘿嘿' + fn() + '嘿嘿嘿'
    return inner
# 被装饰的函数一
@decol #使用第一个装饰器修饰test1函数，使其具有新的功能
@decol2 #使用第二个装饰器修饰test1函数，使其具有新的功能
@decol3 #使用第三个装饰器修饰test1函数，使其具有新的功能
#离得最近的装饰器先执行，所以先执行decol2，再执行decol
#decol将 '嘻嘻嘻' + fn() + '嘻嘻嘻'  当作fn()的返回值，传入decol中，最终输出哈哈哈嘻嘻嘻晚上再学习吧嘻嘻嘻哈哈哈
def test1():
    return '晚上再学习吧'
print(test1()) #调用被装饰的函数，输出晚上再学习吧

