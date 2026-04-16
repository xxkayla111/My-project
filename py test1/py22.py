# 1.协程:单线程下的开发,又称为微线程
# 注意线程和进程的操作是由程序触发系统接口,最后的执行这是系统
# 协程的操作则是程序员自己控制
# 1.1 简单实现协程
import time
# def task1():
#     while True:
        
#         yield "hahahah"
#         time.sleep(1)
# def task2():
#     while True:
        
#         yield "嘿嘿嘿"
#         time.sleep(1)
# if __name__ == "__main__":
#     # 1. 创建协程对象
#     t1 = task1()
#     t2 = task2()
#     # 2. 启动协程
#     while True:
#         print(next(t1))
#         print(next(t2))

# 1.2 协程的应用
# 1.如果一个线程里面有io操作比较多的时候,可以使用协程
#  io操作:input/output:输入和输出操作,
#   网络请求,文件读写,数据库操作等
# 2.适合高并发处理

# 2.greenlet:是一个由c语言实现的协程模块,基于python的协程库
# 通过设置switch函数,实现任意函数的切换执行
# 2.1 安装第三方模块
# python -m pip install greenlet
# 卸载:
# python -m pip uninstall greenlet
# 查看:
# python -m pip list
# 2.2 注意:greenlet属于手动切换,当遇到io操作,程序会阻塞,
# 而不能进行自动切换,直到io操作完成,才会切换到下一个协程
# 2.3 通过greenlet实现任务的切换
# 导入模块
from greenlet import greenlet

# def sing():
#     print("在唱歌")
#     g2.switch() # 切换到g2中去运行
#     print("唱完歌了")
# def dance():
#     print("在跳舞")
#     # greenlet.switch()
#     print("跳舞完了") 
#     g1.switch() # 切换到g1中去运行
# if __name__ == "__main__":
#     # 1. 创建协程对象
#     g1 = greenlet(sing)
#     g2 = greenlet(dance)
#     # 2. 启动协程
#     g1.switch() # 切换到g1中去运行
#     g2.switch() # 切换到g2中去运行
   
# 3. gevent:是一个基于greenlet的协程模块,用于实现高并发处理
# 遇到io操作,会自动切换到下一个协程,属于主动式切换
# 3.1 安装第三方模块
# python -m pip install gevent
# 3.2 导入模块
import gevent
# 使用: gevent.spawn(函数名): 创建协程对象
# gevent.sleep(秒数): 暂停协程,等待指定秒数后,切换到下一个协程
# gevent.joinall(协程对象列表): 等待所有协程执行完成,再继续执行
# 3.3 gevent 自带耗时操作
# def sing():
#     print("在唱歌")
#     gevent.sleep(3)
#     print("唱完歌了")
# def dance():
#     print("在跳舞")
#     gevent.sleep(2)
#     print("跳完舞了") 
# if __name__ == "__main__":
#     # 1. 创建协程对象
#     g1 = gevent.spawn(sing)
#     g2 = gevent.spawn(dance)
#     # 2. 阻塞,等待协程执行完成
#     g1.join() # 等待g1执行完成
#     g2.join() # 等待g2执行完成
   
# 3.4 joinall()函数
# 3.4.1 作用:等待所有协程执行完成,再继续执行
# 3.4.2 参数:协程对象列表
# 3.4.3 返回值:无
# def sing(name):
#     for i in range(5):
#         print(f"{name}在唱歌,被送走了第 {i}次")
#         gevent.sleep(0.1)
# if __name__ == "__main__":
#     gevent.joinall([
#         gevent.spawn(sing, "张三"), 
#         gevent.spawn(sing, "李四")
#         ])

# 3.5 monkey补丁:拥有在模块运行时替换的功能
# 导入模块
# from gevent import monkey
# # 1. 启用monkey补丁
# monkey.patch_all() #将用到的time模块,替换为gevent模块
# #注意:monkey补丁只能在模块被打补丁前,调用
# def sing(name):
#     for i in range(3):
#         time.sleep(1)
#         print(f"{name}在唱歌,被送走了第 {i}次")
        
# if __name__ == "__main__":
#     gevent.joinall([
#         gevent.spawn(sing, "张三"), 
#         gevent.spawn(sing, "李四")
#         ])
    
# 4. 总结
# 4.1 线程是cpu调度的基本单位,进程是资源分配的基本单位
# 4.2 协程是单线程下的开发,又称为微线程
# 进程: 切换需要的资源最大效率最低
# 线程: 切换需要的资源一般,效率一般
# 协程: 切换需要的资源最小,效率高
# 多线程适合io密集型操作(网络请求,文件读写,数据库操作,爬虫等)
# 多进程适合cpu密集型操作(科学计算,加密,对视频进行高清解码等)
# 进程、线程、协程都是可以完成多任务的，可以根据自己实际情况开发需要选择使用

# 4.3 gevent是一个基于greenlet的协程模块,用于实现高并发处理
# 4.4 monkey补丁:拥有在time模块运行时替换的功能
