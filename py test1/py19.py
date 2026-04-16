# 导入线程模块
import threading
# 导入时间模块
import time
# def sing():
#     print("我会唱歌")
#     time.sleep(1)
# def dance():
#     print("我会跳舞")
#     time.sleep(1)
# sing()
# dance()

# 2. 多线程:同时运行多个线程，每个线程执行不同的任务
# 2.1 线程和进程
# 进程：进程是资源分配和调度的基本单位，没打开一个程序至少就会有一个进程
# 线程是cpu调度的最小单位，每一个进程至少都会有一个线程，
# 这个线程通常就是我们所说的主线程
# 一个进程默认有一个线程,进程里面可以创建多个线程,
# 线程是依附在进程上的，线程不能独立存在，必须依附在进程上才能存在
# 2.2 多线程
# 导入线程模块
# import threading
# Thread 线程类参数
# taret: 执行的任务名
# args: 以元组的形式给任务传参
# kwargs: 以字典的形式给任务传参

# def sing(name):
#     print(f"{name}会唱歌")
#     time.sleep(2)
#     print(f"{name}会唱歌结束")
# def dance(name2):
#     print(f"{name2}会跳舞")
#     time.sleep(2)
#     print(f"{name2}会跳舞结束")
#     # 主程序入口
# if __name__ == "__main__":
#     # 1. 创建子线程
#     t1 = threading.Thread(target=sing, args=("张三",)) 
#     # 以元组的形式传参,元组中只有一个元素,必须用逗号隔开
#     t2 = threading.Thread(target=dance, args=("李四",))
#     # 3. 守护线程,必须放在开启子线程之前:主线程执行结束,
#     # 子线程也会被强制结束
#     # t1.daemon = True
#     # t2.daemon = True
#     # 2. 启动子线程
#     t1.start()
#     t2.start()
#     # 4. 阻塞主线程join(),暂停的作用,等子线程结束后,
#     # 主线程才会继续执行后续代码,必须放在start()后面
#     t1.join()
#     t2.join()
#     # 5. 获取线程名字
#     print(t1.name)
#     print(t2.name)
#     # 6. 更改线程名字
#     t1.name = "唱歌线程"
#     t2.name = "跳舞线程"
#     print(t1.name)
#     print(t2.name)
#     # 7. 判断线程是否存活
#     print(t1.is_alive())
#     print(t2.is_alive())
#     print("完美谢幕,本次表演结束")

# 2.3 线程之间执行是无序的
# 线程执行是根据cpu调度决定的
# def task():
#     time.sleep(1)
#     print("当前线程是:", threading.current_thread().name)  #显示当前线程对象名
#     # 主程序入口
# if __name__ == "__main__":
#     for i in range(5):
#         # 每循环一次,创建一个字线程
#         t = threading.Thread(target=task)
#         #启动子线程
#         t.start()

# 2.4 线程之间共享资源
# li = []  #定义全局变量
# # 写入数据
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.01)

#     print("写入的数据是:", li)
# # 读取数据
# def rdata():
    
#         print("读取的数据是:", li)
        
# if __name__ == "__main__":
#      # 1. 创建子线程
#      wd = threading.Thread(target=wdata)
#      rd = threading.Thread(target=rdata)
#      # 2. 启动子线程
#      wd.start()
#      wd.join()
#      # 3. 阻塞主线程join(),暂停的作用,等子线程结束后,
#      # 主线程才会继续执行后续代码,必须放在start()后面
#      rd.start()
#      rd.join()          

# a = 0 
# b = 1000000
# def add():
#     for i in range(b):
#         global a
#         a += 1
#     print("这是第一次累加:", a)
# def add2():
#     for i in range(b):
#         global a
#         a += 1
#     print("这是第二次累加:", a)
# if __name__ == "__main__":
#     a1 = threading.Thread(target=add)
#     a2 = threading.Thread(target=add2)
#     a1.start()
    
#     a2.start()
    


# 3. 线程同步
# 主线程和创建的子线程之间各自执行完自己的代码直至结束
a = 0 
b = 1000000
# def add():
#     for i in range(b):
#         global a
#         a += 1
#     print("这是第一次累加:", a)
# def add2():
#     for i in range(b):
#         global a
#         a += 1
#     print("这是第二次累加:", a)
# if __name__ == "__main__":
#     a1 = threading.Thread(target=add)
#     a2 = threading.Thread(target=add2)
#     a1.start()
#     # 等待a1线程执行结束
#     a1.join()
#     a2.start()
#     a2.join()

# 4. 互斥锁
# 对共享数据进行锁定,保证多个线程访问共享数据不会出现
# 数据错误问题:保证同一时刻只能有一个线程去操作.
# 导入模块
from threading import Lock
# 1. 创建全局互斥锁

lock = Lock()

a = 0 
b = 1000000
def add():
    # 2. 加锁
    lock.acquire()
    for i in range(b):
        global a
        a += 1
    print("这是第一次累加:", a)
    # 3. 解锁
    lock.release()
def add2():
    # 2. 加锁
    lock.acquire()
    for i in range(b):
        global a
        a += 1
    print("这是第二次累加:", a)
    # 3. 解锁
    lock.release()
if __name__ == "__main__":
    a1 = threading.Thread(target=add)
    a2 = threading.Thread(target=add2)
    a1.start()

    a2.start()
 
 # 注意: 加锁和解锁必须成对出现,否则会导致死锁.
 # 死锁: 一直等待对方释放锁,导致程序无法继续执行.
 # 会造成应用程序停止响应.,不能再处理其他任务
 # 解决死锁的方法:
 # 1. 代码中检查是否有死锁的情况
 # 2. 代码中添加超时机制,如果超过一定时间没有释放锁,则强制解锁
#  4.2 总结
# 互斥锁的作用: 保证同一时刻只有一个线程去操作共享数据,
# 保证共享数据不会出现数据错误问题.
# 互斥锁的缺点: 会导致线程阻塞,影响程序的执行效率.
