# 1.正则表达式
# 字符串处理工具
# 注意需要导入re模块

import re

# 1.2 特点
# 语法比较复杂，可读性较差
# 通用性很强，适用于多种编程语言

# 1.3 步骤：
        # 1.导入re模块
        # 2. 使用match方法进行匹配操作
        # re.match(正则表达式,字符串)能匹配出以xxx开头的字符串
        # 如果起始位置没有匹配成功，返回None
# re.match(pattern, string,flags)
# pattern: 正则表达式
# string: 要匹配的字符串
# flags: 匹配标志位,可以设置为0,或多个标志位的或操作
# res = re.match(r"hello","hello world")
# print(res.group())

        # 3. 如果上一步匹配成功，使用group()方法提取数据\
# 注意：match是从开始位置匹配，匹配不到就没有，且匹配的是整体

# 2. 匹配单个字符

# 1  .: 匹配任意单个字符(除了换行符)
# res = re.match(r"...","hello world") # 三个点匹配任意三个字符
# print(res.group())
# 2. []: 匹配方括号中的任意一个字符
# res = re.match(r"[a-zA-Z0-9]","Hello world")# 匹配任意三个字母数字
# print(res.group())
# \d: 匹配任意数字(0-9)
# res = re.match(r"\d","123456")
# print(res.group())
# \D: 匹配任意非数字(非0-9)
# res = re.match(r"\D","__hello world")
# print(res.group())
# \w: 匹配任意字母数字下划线
# res = re.match(r"\w","hello world")
# print(res.group())
# \W: 匹配任意非字母数字下划线
# res = re.match(r"\W","]hello world")
# print(res.group())
# \s: 匹配任意空格(空格、制表符、换行符等) # 一个tab= 2个空格
# res = re.match(r"\s....","   hello world")
# print(res.group())
# \S: 匹配任意非空格(非空格、制表符、换行符等)
# res = re.match(r"\S","hello world")
# print(res.group())


# 3. 匹配多个字符
# 1. *: 匹配任意多个字符(0个或多个) --常用
# res = re.match(r"\d*","hello world")
# print(res.group())
# # 2. +: 匹配任意多个字符(1个或多个)  -- 常用
# res = re.match(r"\d+","123hello world")
# print(res.group())
# # 3. ?: 匹配任意多个字符(0个或1个) 要么有一次要么没有--常用
# # res = re.match(r"hello?","hello world")
# # print(res.group())
# # 4. {m} 匹配前一个字符出现m次
# res = re.match(r"\w{2}","hellohello world")
# print(res.group())
# # 5. {m,n} 匹配前一个字符出现m到n次
# # 注意必须符合m<=n,否则会报错
# res = re.match(r"\w{2,4}","hellohello world")
# print(res.group())


# 4.匹配开头和结尾
# ^: 匹配字符串开头 ： 表示对...取反
res = re.match(r"^hello","hello world")
print(res.group())
# 注意在[]中表示不匹配，不能匹配到hello
res = re.match(r"[^hello]","11111hello world")
print(res.group())

# $: 匹配字符串结尾
res = re.match(r".{7}\w$","bingbing")
print(res.group())
