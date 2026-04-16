# 1.可迭代对象Iterable
#遍历（迭代）：依次从对象中把一个个元素取出来的过程
#数据类型：列表、元组、字符串、字典、集合等

# 1.2可迭代对象的条件
# 1.2.1 可迭代对象必须有__iter__()方法
# __iter__()方法返回一个迭代器对象
# 1.2.2 可迭代对象必须有__next__()方法

# 1.3 for循环工作原理
# 1.3.1 先调用__iter__()方法获取一个迭代器对象
# 1.3.2 然后调用__next__()方法获取第一个元素
# 1.3.3 重复以上步骤，直到获取到所有元素
# 1.3.4 最后调用__next__()方法获取一个StopIteration异常

# 1.4 迭代器Iterator ：判断一个对象是否是可迭代对象或者是一个已知的数据类型
#导入模块
# from collections.abc import Iterable
#isinstance(o,t) o对象 t类型
# 函数：判断一个对象是否是一个已知的数据类型
# print(isinstance("123",Iterable))

# for i in "123":
#     print(i)
   
# 2.迭代器 Iterator
#是一个可以记住遍历位置的对象，在上次停留的位置继续去做一些事情
# li = [1,2,3,4,5]
# # 1. 创建迭代器对象
# li2 = iter(li)
# print(li2)
# #2.获取下一条数据
# print(next(li2))  # 1
# print(next(li2))  # 2
# print(next(li2))  # 3
# print(next(li2))  # 4
# print(next(li2))  # 5
# 3. 获取下一条数据时，如果迭代器对象没有数据了，会报错
# print(next(li2))
# 报错信息：StopIteration: next() of iterator did not return an item        

#步骤：
# iter()调用对象的__iter__()方法，返回一个迭代器对象
# next()调用迭代器对象的__next__()方法，返回下一个元素
# 重复以上步骤，直到获取到所有元素
# 最后调用__next__()方法获取一个StopIteration异常

# 2.2 可迭代对象Iterable和迭代器Iterator的区别
# 凡是可以作用于for循环的对象，都是可迭代对象
# 凡是可以调用next()方法的对象，都是迭代器对象
# from collections.abc import Iterable,Iterator

# name = "张三"
# print(isinstance(name,Iterable))
# n = iter(name)
# print(isinstance(n,Iterator))

# 迭代器对象一定是可迭代对象
# 可迭代对象不一定是迭代器对象，可以通过iter()函数将其转换为迭代器对象
#如果一个对象拥有__iter__()方法，那么它就是可迭代对象
#如果一个对象拥有__next__()方法，那么它就是迭代器对象

# dir()函数：查看一个对象的所有属性和方法

# 2.3 迭代器协议
# 对象必须提供一个next()方法，执行该方法要么就返回迭代中的下一项，
# 要么就抛出一个StopIteration异常，停止迭代


# 2.4 自定义迭代器类
# 两个特性：--iter()方法和__next__()方法
# class Test(object):
#     # 初始值是1，逐步递增1
#     def __init__(self):
#         self.num = 1
#     def funa(self):
#         print(self.num)
#         self.num += 1
# te = Test()
# print(te)
# te.funa()

# class MyIterator(object):
#     def __init__(self):
#         self.num = 0
#     def __iter__(self):
#         return self     #返回当前迭代器的实例对象
#     def __next__(self):
       
#        # 加上判断，如果num大于5，抛出异常
#        if self.num > 10:
#            raise StopIteration("迭代结束,没有数据了")
#        self.num += 1
#        return self.num 
# mi = MyIterator()
# print(mi)
# print(next(mi))

# for i in mi:
#     print(i)

# 3. 生成器 generator
 # python中一边循环一边计算的机制，叫做生成器
 # 生成器是一种特殊的迭代器，它可以在需要时计算下一个元素，而不是在创建时就计算好所有元素
# 3.1 生成器表达式
# 列表推导式
# for i in range(10):
#     print(i*5)
# li = [i * 5 for i in range(10)]
# gen = (i * 5 for i in range(10)) # 列表推导式的[]改成（）就是生成器表达式

# print(li)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# 3.2 生成器函数
# python中使用了yield关键字，就可以定义一个生成器函数
# 1. 类似return，将指定值或者多个值返回给调用者
# yield语句一次返回一个结果，在每个结果中间，挂起函数，执行next()方法时，继续执行
# 使函数中断，并保存中断的状态
# def test():
#     li = []
    
#     li.append("a")
#     print(li)
# test()
# test()

# 生成器函数
# def gen():
#     print("开始了")
#     yield 1  #返回一个1，并暂停函数，在此处挂起，等待下一次调用next()方法时，继续执行
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     print("结束了")
# g = gen()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen2(n):
#     li = []
#     a = 0
#     while a < n:
#         li.append(a)
#         yield a
        
#         a += 1
#     # for i in range(n):
#     #     li.append(i)
#     print("li:" ,li)
# # gen2(9)
# for i in gen2(9):
#     print(i)

# 使用了yield关键字，就是生成器函数
def test_1():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
for i in test_1():
    print(i)
# print(test_1())
# print(next(test_1()))
# print(next(test_1()))
# print(next(test_1()))
# te = test_1()
# print(next(te))       
# print(next(te))
# print(next(te))
# print(next(te))
# print(next(te))

# 三者关系
# 可迭代对象：指实现了python迭代协议，可以通过for()循环遍历的对象
# 迭代器对象：可以记住自己遍历位置的对象，可以通过next()方法获取下一个元素的对象，只能往前不能往后，
# 当遍历完毕后，next()方法会抛出一个IterationError异常，停止迭代
# 生成器对象：是特殊的迭代器，需要注意迭代器并不一定是生成器，它是python中提供的
# 通过简便的方法写出迭代器的一种手段。
# 包含关系：可迭代对象>迭代器对象>生成器对象