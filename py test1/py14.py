# 面向对象基础
 # 面向对象和面向过程的区别
# 面向对象：把现实世界中的事物抽象成对象，对象具有属性和方法
# 面向过程：把问题分解成一系列步骤，按照步骤来解决问题
# 面向对象的三大特征：封装、继承、多态
# 封装：把数据和操作数据的代码封装在一起，隐藏内部实现细节，只暴露接口
# 继承：子类继承父类的属性和方法，可以重写父类的方法，也可以添加新的方法
# 多态：同一个方法在不同的对象上表现出不同的行为
#类和对象
#1.类的三要素
# 类名：用来描述一类事物的名称，通常使用大写字母开头的驼峰命名法
# 属性：对象具有的特征，用来说明是什么样子的
# 方法：对象具有的行为（功能），用来说明能做什么
# 对象：类的实例

# 查看类属性  类名.属性名 = 值   
# class Washer:
#     brand = "小米"  #类属性，所有对象共享的属性
#     color = "白色"  #类属性，所有对象共享的属性
#     price = 1999  #类属性，所有对象共享的属性
# print(Washer.brand)  #小米
# print(Washer.color)  #白色
# print(Washer.price)  #1999
# # 创建对象  对象名 = 类名()  #调用类的构造方法，创建对象
# wa = Washer()  #创建一个洗衣机对象washer1
# #显示的对象在内存中的地址
# #第二次实例化
# wa2 = Washer()  #创建另一个洗衣机对象washer2
# print(wa)
# print(wa2)  #<__main__.Washer object at 0x000001E8B8C9F250> <__main__.Washer object at 0x000001E8B8C9F2B0>
# # wa和wa2是两个不同的对象，在内存中占用不同的地址

#2.实例方法和实例属性

# 2.1 实例方法
# 由对象调用的方法叫实例方法，实例方法的第一个参数必须是self，
# self代表当前对象的引用，可以通过self访问对象的属性和方法
# class Washer:
#     height = 100  #类属性，所有对象共享的属性
#     width = 50  #类属性，所有对象共享的属性
#     def wash(self):  #实例方法，必须有self参数
#         print('我会洗衣服')
# wa = Washer()  #创建一个洗衣机对象washer1
# wa.wash()  #调用实例方法wash，输出：我会洗衣服

# 实例属性
# #格式self.属性名 = 值
# class Preson:
#     Name = "chengcheng"  #类属性，所有对象共享的属性
#     Age = 18  #类属性，所有对象共享的属性
#     def introduce(self):  #实例方法，必须有self参数
#         print(f"大家好，我是{Preson.Name}，今年{self.Age}岁了") 
#          #通过self访问对象的属性
# pe = Preson()  #创建一个人对象person1
# pe.Age = 20  #修改实例属性Age的值为20
# pe.sex = "男"  #添加实例属性sex，值为男  
# # 可以通过对象名.属性名 = 值的方式修改实例属性的值，也可以添加新的实例属性，
# # 实例属性只属于当前对象，不会影响其他对象的属性值
# print(pe.sex)  #男
# pe.introduce()  #调用实例方法introduce，输出：大家好，我是chengcheng，今年18岁了    
# #访问类属性，类可以访问到，实例对象也可以访问到，但实例对象访问类属性时，如果实例对象没有该属性，就会访问类属性，如果实例对象有该属性，就会访问实例属性，实例属性会覆盖类属性的值
# print(Preson.Name)  #chengcheng
# print(pe.Name)  #chengcheng 访问类属性Name，输出：chengcheng 


#3.构造函数__init__()方法 注意是两个下划线
# 作用：在创建对象时自动调用，用来初始化对象的属性或者赋值操作
# class Test:
#     def __init__ (self):
#         print("这是构造函数__init__()方法")
# te = Test()  #创建一个Test对象test1，自动调用构造函数__init__()方法，输出：这是构造函数__init__()方法


 

# class Person:
#     def __init__(self, name, age):
#         self.name = name  #实例属性name，值为参数name的值
#         self.age = age

#     def say_hello(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# #实例化对象的时候就要传值，创建一个Person对象person1，传入参数name的值为"Alice"，age的值为30
# person1 = Person("Alice", 30)
# person1.say_hello()  #Hello, my name is Alice and I am 30   
# #实例化第二次
# pe = Person("bingbing", 18)  #创建一个Person对象person2，传入参数name的值为"bingbing"，age的值为18
# pe.say_hello()  #Hello, my name is bingbing and I am 18 

#4.析构函数__del__()方法 注意是两个下划线
# 作用：在对象被销毁时自动调用，用来释放对象占用的资源或者进行清理操作
# class Person:
#     def __init__(self):
#         print("这是构造函数__init__()方法")
#     def __del__(self):
#         print("我被销毁了")
# p = Person()  #创建一个Person对象person1，自动调用构造函数__init__()方法
# # 输出：这是构造函数__init__()方法
# print('这是最后一行代码')  #输出：这是最后一行代码
# # 正常运行结束后，Python会自动销毁对象person1，调用析构函数__del__()方法，输出：我被销毁了
# # del p  #销毁对象person1，自动调用析构函数__del__()方法，输出：我被销毁了
# #__del__()主要是表示该程序块或者函数已经全部执行完毕，或者对象已经不再被使用了，可以进行垃圾回收了，释放内存空间了

# # 5.封装   
# # 面向对象三大特性：封装、继承、多态
# # 封装：把数据和操作数据的代码封装在一起，隐藏内部实现细节，只暴露接口
# class Person:
#     name = "bingbing"  #类属性，所有对象共享的属性
#     age = 18  #类属性，所有对象共享的属性
    
# pe = Person()  #创建一个Person对象person1，传入参数name的值为"bingbing"，age的值为18
# print(pe.name)  #bingbing 访问类属性name，输出：bingbing
# Person.name = "chengcheng"  #修改类属性name的值为"chengcheng"
# print(pe.name)  #chengcheng 访问类属性name，输出：chengcheng
# # 类属性被所有对象共享，修改类属性的值会影响所有对象访问该属性的值

#5.2私有属性和私有方法
# 1.xxx:普通属性/方法，外部可以直接访问

# 2._xxx:私有属性/方法，外部可以访问，但不建议访问，通常用于表示这是一个内部属性/方法，不应该被外部代码直接使用

# 3.__xxx:隐藏属性/方法，外部无法直接访问，只能通过公有方法来访问隐藏属性/方法，这样可以保护数据的安全性和完整性，防止外部代码对数据进行非法操作或者修改。子类不会继承父类的私有属性和私有方法，无法直接访问父类的私有属性和私有方法，但可以通过父类的公有方法来访问父类的私有属性和
# 隐藏方法：在方法名前加两个下划线__，表示这是一个私有方法，外部无法直接调用，只能通过公有方法来调用私有方法，这样可以保护方法的安全性和完整性，防止外部代码对方法进行非法操作或者修改。
# class Person:
#     name = "bingbing"  #类属性，所有对象共享的属性
#     __age = 18  #隐藏属性，外部无法直接访问
#     def introduce(self):  #实例方法，必须有self参数
#         Person.__age = 30  #在实例方法中修改隐藏属性__age，输出：30
#         print(f"大家好，我是{self.name}，今年{self.__age}岁了") 
#         #通过self访问对象的属性，包括隐藏属性

# pe = Person()  #创建一个Person对象person1，传入参数name的值为"bingbing"，age的值为18
# # print(pe.name)  #bingbing 访问类属性name，输出：bingbing
# # print(pe.__age)  #会报错，无法访问隐藏属性__age

#不正规方式访问隐藏属性，虽然可以访问到，但不建议使用这种方式，因为隐藏属性的命名规则是为了保护数据的安全性和完整性，防止外部代码对数据进行非法操作或者修改，如果使用不正规方式访问隐藏属性，可能会导致数据被修改或者破坏，影响程序的正常运行。
#隐藏属性实际上是将名称改为_类名__属性名的形式来访问的，所以可以通过这种方式来访问私有属性
# print(pe._Person__age)  #18 访问隐藏属性__age，输出

#第二种方法，在类的内部访问，通过实例方法来访问隐藏属性
# pe.introduce()  #调用实例方法introduce，输出：大家好，我是bingbing，今年18岁了

#5.3_xxx,单下划线开头
# class Person:
#     name = "wx"  
#     __age = 18   #隐藏属性，外部无法直接访问
#     _sex = "女"  #私有属性，外部可以访问，但不建议访问，通常用于表示这是一个内部属性，不应该被外部代码直接使用
#     def introduce(self):
#         print(f"大家好，我是{self.name}")  #通过self访问单下划线开头的属性
# pe = Person()  #创建一个Person对象person1，传入参数name的值为"wx"，age的值为18，sex的值为"女"
# print(pe._sex)  #女 访问单下划线开头的属性，输出：女
# pe.introduce()

# 5.4隐藏方法：在方法名前加两个下划线__，表示这是一个私有方法，外部无法直接访问，只能通过公有方法来访问隐藏方法，这样可以保护方法的安全
# class Man:
#     def __play(self):  #隐藏方法，外部无法直接访问
#         print("我会玩游戏")
#     def funa(self):
#         print('平平无奇的方法')
#         self.__play()  #在实例方法funa中调用隐藏方法__play，输出：我会玩游戏
# ma = Man()  #创建一个Man对象ma
# ma.funa()  #调用实例方法funa，输出：平平无奇的方法
# # ma.__play()  #会报错，无法访问隐藏方法__play  

# 5.5私有方法
class Girl:
    def _funb(self):  #私有方法
        print("我会唱歌")
        
girl = Girl()   #创建一个Girl对象girl
girl._funb()  #调用私有方法_funb，输出：我会唱歌
#虽然可以访问到私有方法，但不建议使用这种方式，因为私有方法的命名规则是为了保护方法的安全性和完整性，防止外部代码对方法进行非法操作或者修改，如果使用不正规方式访问私有方法，可能会导致方法被修改或者破坏，影响程序的正常运行。     
























# def __init__(self, name, age):
#         self.__name = name  #私有属性，外部无法直接访问
#         self.__age = age  #私有属性，外部无法直接访问
#     def get_name(self):  #公有方法，外部可以调用
#         return self.__name  #通过公有方法访问私有属性
#     def get_age(self):  #公有方法，外部可以调用
#         return self.__age  #通过公有方法访问私有属性
# 私有属性的命名规则：在属性名前加两个下划线__，表示这是一个私有属性，外部无法直接访问，只能通过公有方法来访问私有属性，这样可以保护数据的安全性和完整性，防止外部代码对数据进行非法操作或者修改。

# 继承：子类继承父类的属性和方法，可以重写父类的方法，也可以添加新的方法
# 多态：同一个方法在不同的对象上表现出不同的行为
