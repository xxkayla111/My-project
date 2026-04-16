import multiprocessing
from multiprocessing import Process,Queue
import os

import threading
import time

# from queue import Queue
# 20. 进程
# 1.1 含义:
# 是操作系统进行资源分配和调度的基本单位.是操作系统结构的基础
# 一个正在运行的程序或者软件就是一个进程
# 注意:进程里面可以创建多个线程,多进程也可以完成多任务
# 1.2 进程的状态
# 1. 就绪状态: 进程已经创建,但是还没有开始,等待被调度器选中执行.
# 2. 运行状态: 进程正在被调度器选中执行.
# 3. 阻塞(等待)状态: 进程因为某种原因,导致无法继续执行,等待被调度器选中执行.
# 4. 进程结束状态: 进程已经执行完毕,或者因为某种原因,导致无法继续执行.



# 2. 进程语法结构
# multiprocessing.Process 类代表进程对象
# 2.1 Process类参数
# target: 执行的目标任务名,即子进程要执行的任务
# args: 以元组的形式传递参数
# kwargs: 以字典的形式传递参数

# 2.2 进程对象的方法
# 1.start(): 启动子进程
# 2.join(): 主进程等待子进程结束
# 3.is_alive(): 判断子进程是否还在运行,存活则返回True,否则返回False

# 2.3 常用的属性
# 1.name: 当前进程的别名.默认为Process-N
# 2.pid: 当前进程的进程编号ID
# 导入模块


# def sing():
#     # os.getppid() # 查看父进程的进程编号ID
#     # os.getpid() # 查看当前进程的进程编号ID
#     print(f"sing进程的编号ID为:{os.getpid()},父进程的id为:{os.getppid()}")
#     print("我会唱歌")
# def dance():
#     print(f"dance进程的编号ID为:{os.getpid()},父进程的id为:{os.getppid()}")
#     print("我会跳舞")
# if __name__ == "__main__":
#     # 创建子进程
#     # 修改子进程名字第一种方式
#     p1 = Process(target=sing,name="子进程1")
#     p2 = Process(target=dance,name="子进程2")
#     # 启动子进程
#     p1.start()
#     p2.start()
#     # 修改子进程名字第二种方式
#     p1.name = "子进程1-修改"
#     p2.name = "子进程2-修改"
#     # 访问name属性
#     print(p1.name)
#     print(p2.name)
#     # 查看子进程的进程编号ID
#     print(p1.pid)
#     print(p2.pid)
#     print(f"主进程pid为:{os.getpid()},主进程的父进程pid为:{os.getppid()}")

# 主进程的父进程编号就是当前软件的进程编号ID


# def eat(name):
#     print(f"{name}在干饭")
# def sleep(name):
#     print(f"{name}在睡觉")
# if __name__ == "__main__":
#     # 创建子进程
#     p1 = Process(target=eat,args=("bingbing",))
#     p2 = Process(target=sleep,args=("wangxin",))
#     # 启动子进程
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     print("p1存活状态:",p1.is_alive())
#     print("p2存活状态:",p2.is_alive())
# 写在主进程中判断存活状态时需要加入join方法阻塞一下

# 2.4 进程间不共享全局变量

# li = []
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.5)

#     print("写入的数据是:", li)
# # 读取数据
# def rdata():
    
#         print("读取的数据是:", li)
# #1.  防止别人导入文件时执行main里面的方法
# #2.  防止Windows系统递归创建子进程
# if __name__ == "__main__":
# #      # 1. 创建子进程
#      p1 = Process(target=wdata)
#      p2 = Process(target=rdata)
#      # 2. 启动子进程
#      p1.start()
    
#      p2.start()
# 进程不共享全局变量,每个进程都有自己的全局变量


# 3. 进程间通信
# Queue(队列) 
# q.put() 向队列中放数据
# q.get() 从队列中取数据
# q.empty() 判断队列是否为空
# q.full() 判断队列是否已满
# q.qsize() 获取队列中数据的数量
# 初始化一个队列对象
# q = Queue(3)  # 最多可以接收3个数据,没写代表没有上限,直到内存尽头
# q.put("爱你到老")
# q.put("你好")
# print("队列是否已满:",q.full())
# q.put("你在做梦")
# # q.put("你好") # 报错,队列已满
# print("队列是否已满:",q.full())
# # print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.empty())
# print(q.get())
# print(q.empty())
# print(q.qsize())

li = ["张三","李四","王五","赵六","王二"]
def wdata(q1):
    for i in range(5):
        print(f"写入数据:{i}")
        q1.put(i)
        time.sleep(0.5)

    print("写入的数据是:", li)
# 读取数据
def rdata(q2):
    while True:
        #判断是否为空
        if q2.empty():
            break
        else:
            print("取出数据是",q2.get())
    print(f"读取的数据是:",li)
        
#1.  防止别人导入文件时执行main里面的方法
#2.  防止Windows系统递归创建子进程
if __name__ == "__main__":
#      # 1. 创建队列对象
     q = Queue()
    
     p1 = Process(target=wdata,args=(q,))
     p2 = Process(target=rdata,args=(q,))
     # 2. 启动子进程
     p1.start()
     p1.join()
     p2.start()
     p2.join()
     