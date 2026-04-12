#1.__init__() 和 __new__() 方法
# __init__() 方法是一个实例方法，在创建对象后会自动调用，用于初始化对象的属性和状态，__new__() 方法是一个静态方法，在创建对象之前会自动调用，用于创建对象并返回对象的实例，__new__() 方法通常用于实现单例模式或者元类等高级功能，而 __init__() 方法则用于初始化对象的属性和状态。
# class Person:
#     def __init__(self):
#         print("这是__init__方法，初始化对象的属性和状态")
# p = Person()  #创建一个Person对象p，输出：这是__init__方法，初始化对象的属性和状态，__init__方法在创建对象后会自动调用，用于初始化对象的属性和状态

# # 1.2 __new__() 方法,,用__init__必须先用__new__方法来返回对象.
# class Person:
#     def __init__(self):
#         print("这是__init__方法，初始化对象的属性和状态")
#     def __new__(cls):
#         print("这是__new__方法，创建对象并返回对象的实例")
#         # return super().__new__(cls)  #调用父类的__new__方法来创建对象并返回对象的实例
    
# p = Person()  #创建一个Person对象p，输出：这是__new__方法，创建对象并返回对象的实例，这是__init__方法，初始化对象的属性和状态，__new__方法在创建对象之前会自动调用，用于创建对象并返回对象的实例，而 __init__方法在创建对象后会自动调用，用于初始化对象的属性和状态

# 2.单例模式
#是一种常用的软件设计模式,主要目的是确保某一个类中只有一个实例存在,
#可以节省内存空间,增加代码的复用性
#可以理解成一个特殊的类,这个类只存在一个对象
#弊端:多线程访问的时候容易引发线程安全问题
# 2.2方式
# 1.通过@class method
# 2.通过装饰器实现
# 3.通过重写__new__()实现  (重点)
# 4.通过导入模块实现
# class A(object):
#     pass
# a1 = A()
# print(a1)
# a2 = A()
# print(a2)
#内存地址发生变化,说明是不同的对象
#实现单例模式,对象的地址都是一样的,只有一个对象
# 2.3通过重写__new__方法()实现单例模式
#设计流程
# 1.定义一个类属性,初始值为None,用来记录单例对象的引用
# 2.重写__new__()方法
# 3.进行判断,如果类属性是None,把__new__()返回的对象引用保存进去
# 4.返回类属性中记录的对象引用
# class Singleton(object):
#     #记录第一个被创建的对象的引用
#     obj = None

#     def __new__(cls,*args,**kwargs):
#         print("这是__new__()方法")
#         #判断类属性是否为空
#         if cls.obj == None:
#             cls.obj = super().__new__(cls) 
        
#         return cls.obj

#     def __init__(self):
#         print("这是__init__()方法")

# s = Singleton()
# print(s)
# s2 = Singleton()
# print(s2)   
# 单例模式：每一次实例化所创建的对象都是同一个，内存地址都一样

# 2.4  通过模块导入实现单例模式
from pytest02 import te as te01
print(te01,id(te01))
from pytest02 import te as te02
print(te02,id(te02))
