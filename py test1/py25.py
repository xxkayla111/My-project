# 1. os 模块
import os
# 用于和操作系统交互
# 1. os.name: 返回操作系统类型
# print(os.name)
# # 对于Windows系统，返回'nt'
# # 对于Linux系统，返回'posix'
# # 对于MacOS系统，返回'darwin'

# # 2. os.getenv(环境变量名):
# # 返回指定环境变量的值
# print(os.getenv("PATH"))
# 返回环境变量PATH的值
# 注意：返回的是字符串，需要使用split()方法将其转换为列表

# 3. os.path.split(路径):
# 把目录名和文件名分离出来，以元组的形式接收
# 要使用[0]和[1]分别获取目录部分和文件名部分
# 第一个元素是目录路径，第二个元素是文件名路径
# print(os.path.split(r"sixs\tar"))
# 返回('sixs\\','tar')

# 4. os.path.dirname(路径):  显示split()方法分割的第一个元素，即目录路径
# print(os.path.dirname(r"sixs\tar"))
# 返回sixs\\

# 5. os.path.basename(路径):  显示split()方法分割的第二个元素，即文件名路径
# print(os.path.basename(r"sixs\tar"))
# 返回tar
# 注意如果路径以\结尾，会报错，如果以/结尾，那么就返回空值

# 6. os.path.exists(路径):  判断路径（文件或者目录）是否存在，返回值为布尔值
# print(os.path.exists(r"D:\python\py test1\py25.py"))
# # 返回True

# # 7. os.path.isfile(路径):  判断路径是否为文件，返回值为布尔值
# print(os.path.isfile(r"D:\python\py test1\py25.py"))
# # 返回True

# # 8. os.path.isdir(路径):  判断路径是否为目录，返回值为布尔值
# print(os.path.isdir(r"D:\python\py test1"))
# # 返回True

# # 9. os.path.abspath(路径):  获取当前路径下的绝对路径
# print(os.path.abspath(r"py25.py"))
# # 返回D:\python\py test1\py25.py

# # 10. os.path.isabs(路径):  判断路径是否为绝对路径，返回值为布尔值
# print(os.path.isabs(r"D:\python\py test1\py25.py"))
# # 返回True



# 二、 sys 模块
# 作用负责程序跟python解释器交互
import sys
# 1. sys.getdefaultencoding():  获取系统默认的编码方式
# print(sys.getdefaultencoding())

# # 2. sys.path: 获取环境变量的路径，跟解释器相关
# print(sys.path[0]) # 以列表的形式返回，第一项为当前所在的工作目录

# # 3. sys.platform: 获取操作系统类型
# print(sys.platform)
# # 对于Windows系统，返回'win32'
# # 对于Linux系统，返回'linux2'
# # 对于MacOS系统，返回'darwin'

# # 4. sys.version: 获取python版本信息
# print(sys.version)
# 返回python版本信息，包括版本号、版本号字符串、版本号元组等

# 三、 time 模块
import time

# 三种时间表示
# 时间戳（timestamp）
# 格式化的时间字符串（formatted time ）
# 时间元组（time tuple）
# 1. time.sleep(秒数):  暂停程序执行，指定秒数
# print(12)
# 2.time.time():  获取当前时间戳
# print(time.time())
# 返回当前时间戳，单位为秒  
# 注意：时间戳是1970年1月1日0时0分0秒到当前时间的秒数
# 3. time.localtime(时间戳):  将时间戳转换为本地时间元组
# print(time.localtime())
# 返回当前时间的本地时间元组，九个元素
# 4. time.asctime(时间元组):  获取当前时间的格式化时间字符串
# print(time.asctime())
# print(time.asctime(time.localtime()))
# 5.time.ctime(时间戳):  将时间戳转换为UTC时间字符串
# print(time.ctime(time.time()))
# 返回UTC时间字符串，格式为YYYY-MM-DD HH:MM:SS.SSS
# 6. time.strftime(格式化字符串,时间元组):  格式化时间元组
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 返回格式化后的时间字符串，格式为YYYY-MM-DD HH:MM:SS
# 7. time.strptime(时间字符串,格式化字符串):  解析时间字符串为时间元组
# print(time.strptime("2023-08-01 12:00:00","%Y-%m-%d %H:%M:%S"))
# 返回解析后的时间元组，九个元素

# 四、logging 模块
import logging
# 1.作用：用于记录日志信息
# 2.日志的作用
#   1.程序调试
#   2.了解软件程序运行情况是否正常
#   3.软件程序运行故障分析与定位
#3.级别排序（从高到低）
#   1.Critical: 严重错误，程序无法继续运行
#   2.Error: 错误，程序继续运行，但是有异常情况
#   3.Warning: 警告，程序继续运行，但是有异常情况
#   4.Info: 信息，程序继续运行，但是没有异常情况
#   5.Debug: 调试信息，程序继续运行，但是没有异常情况
#   6.NotSet: 未设置级别，程序继续运行，但是没有异常情况
#   7. None: 未设置级别，程序继续运行，但是没有异常情况

# logging.debug("我是debug日志")
# logging.info("我是info日志")
# logging.warning("我是warning日志")
# logging.error("我是error日志")
# logging.critical("我是critical日志")
#logging默认的level是warning，也就是说logging只会显示级别大于等于warning的日志
# 可以通过logging.basicConfig(level=level)来设置日志级别
# logging.basicConfig(level=logging.DEBUG) #配置root日志记录器，设置级别为debug
# 这样，logging就会显示所有级别的日志了

# 4.logging.basicConfig(level=level):  配置root日志记录器，设置级别为level
#  1.filename:  指定日志文件名，所有会显示的日志都会写入这个文件中
# logging.basicConfig(filename="log.log",filemode="w",level=logging. NOTSET,encoding="utf-8")
# logging.debug("我是debug日志")
# logging.info("我是info日志")
# logging.warning("我是warning日志")
# logging.error("我是error日志")
# logging.critical("我是critical日志")
# 这样，logging就会将所有级别的日志都写入log.txt文件中
#  2.filemode:  指定日志文件打开模式，默认是'a'，即追加写入
#  3.encoding:  指定日志文件的编码方式，默认是utf-8
#  4.format:  指定日志格式，默认是'(%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# logging.basicConfig(filename="log.log",filemode="w",level=logging. NOTSET,encoding="utf-8",format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logging.debug("我是debug日志")
# logging.info("我是info日志")
# logging.warning("我是warning日志")
# logging.error("我是error日志")
# logging.critical("我是critical日志")


# 五、random 模块
import random
# 作用：用于实现各种分布的伪随机数生成器，可以根据不同的实数分布来随机生成值
# 1.random.random():  生成一个0到1之间的随机浮点数
# print(random.random())
# 2. random.uniform(下限,上限):  生成一个随机浮点数，包括下限和上限
# print(random.uniform(1,10))
# 3. random.randint(下限,上限):  生成一个随机整数，包括下限和上限
# print(random.randint(1,10))
# 4.random.randrange(下限,上限,步长):  生成一个随机整数，包括开头但是不包含结尾，步长为1
print(random.randrange(1,10,2))
