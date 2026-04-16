# 1.文件就是存储在某种长期存储设备上的一段数据
#1.2步骤：
    # 1.打开文件
    # 2.读、写文件内容
    # 3.关闭文件
# 1.3文件对象的方法
    # 1.open() : 打开文件，创建一个flie对象，默认是只读模式打开
    # 2.read(n) : 读取文件内容,n表示从文件中读取的数据长度,默认是读取所有内容
    # 3.write() : 写入文件内容
    # 4.close() : 关闭文件  

# 1.4 属性
# 文件名.name : 返回要打开文件的文件名，可以包含文件的具体路径
# 文件名.mode : 返回打开文件的模式，默认是只读模式
# 文件名.closed : 检测文件是否关闭，默认是关闭，关闭就返回True
# #打开文件
# f = open('test.txt','r')
# print(f.name)
# print(f.mode)
# print(f.closed)
# # #关闭文件
# f.close(   )

# 2.读写操作
# 2.1 read(n):
# 读取文件内容,n表示从文件中读取的数据长度,默认或者负值就是一次性读取所有内容
# f = open('test.txt','r') # r 表示只读模式
# print(f.name) #文件所在的绝对路径
# print(f.read())
# f.close()

# 2.2 readlines()
# 读取文件内容,返回一个列表,每个元素是一个字符串
# f = open('test.txt','r')
# text = f.readlines()
# print(text)
# print(type(text))
# for line in text:
#     print(line)
# f.close()
# 2.3 readline() 一次读取一行内容，方法执行完，会把文件指针移到下一行，准备再次读取
# 读取文件内容,返回一个字符串,每次读取一行
# f = open('test.txt','r')
# # print(f.readline())
# # print(f.readline())
# # while True:
# #     line = f.readline()
# #     if not line:
# #         break
# #     print(line)
# for line in f.readlines():
#     print(line)
# f.close()

# 2.4 访问模式
#2.4.1  r 表示只读模式 也是默认模式，文件必须存在，不存在就会报错
#2.4.2  w 表示写入模式，文件存在就会清空文件内容，再写入添加内容，不存在就创建新文件

# file = open('test.txt','w')  # w 表示写入模式
# file.write("chengcong  hi    nihao  ok")  # 写入文件内容,重新编辑内容，原有内容就会被覆盖
# file.close()  # 关闭文件

# # file = open('test01.txt','r')  # r 表示只读模式
# # print(file.read())
# # file.close()

# #2.4.3  a 表示追加模式，文件存在就会在文件末尾追加内容，不存在就创建新文件
# file = open('test.txt','a')  # a 表示追加模式
# file.write("\nchengcong  hi    nihao  ok")    # 写入文件内容,追加内容，原有内容不会被覆盖
# file.close()  # 关闭文件

# 2.4.4 + :表示可以同时读写某个文件
#使用+会影响文件的读写效率，开发过程中不建议使用+模式
# r+ : 可读写文件，文件必须存在，不存在就会报错
# w+ : 先写再读文件，文件存在就会重新编辑，不存在就创建新文件

#文件指针 : 指向文件当前位置的指针，默认是文件开头
# tell()：显示文件指针当前位置
# seek()：移动文件指针到指定位置
# f = open('test.txt','w+')  
# f.write("hello world")
# f.seek(0)
# print(f.read())
# f.write("\nchengcong  hi    nihao  ok")
# f.close()

# try:
#     f = open('test.txt','r')
#     print(f.name)
#     print(f.mode)
#     print(f.closed)
# except FileNotFoundError:
#     print("文件不存在，正在创建...")
#     # 先创建文件
#     with open('test.txt', 'w') as create_file:
#         pass
#     # 再以只读模式打开
#     f = open('test.txt','r')
#     print(f.name)
#     print(f.mode)
#     print(f.closed)
# finally:
#     # 确保文件被关闭
#     if 'f' in locals():
#         f.close()
#         print("文件已关闭")
#         print(f.closed)

# 3.1  with open
# 作用：代码执行完，系统会自动调用f.close()方法关闭文件
# with open('test.txt','w+') as f:  # f是文件对象
#     f.write("hello world")
#     f.seek(0)
#     print(f.read())

# print(f.closed)

# 4 编码格式
# with open('test.txt','w',encoding='utf-8') as f: 
#     # 编码格式是utf-8，可以写入中文
#     f.write("你好！王鑫")

# with open('test.txt','r',encoding='utf-8') as f:
#     # 编码格式是utf-8，可以读取中文
#     print(f.read())

# 案例：图片复制，读取图片或者视频文件 "rb"
"""
 读取图片
 图片文件是二进制文件，只能用二进制模式读取，想要写入必须先拿到

"""
with open(r'C:\Users\Xx\Desktop\新建文件夹\1.mp4','rb') as f:
    # 读取文件内容
    mp = f.read()
    print(mp)
# 将读取到的内容写入到当前文件
with open(r'D:\python\py test1\2.mp4','wb') as f:
    f.write(mp)

