# 导入re模块
import re
# 1. 匹配分组
# 1.1 | 匹配左右任意一个表达式  --常用
# res = re.match(r"hello|world","world")
# # 先左后右，匹配不到就报错
# print(res.group())

# 2. （ab）将括号中字符作为一个分组  -- 常用
# res = re.match(r"\w+@(163|qq|126).\w+","123@163.com")
# print(res.group())

# 3. \num 引用第num个分组的内容 --经常在匹配标签时使用
# res = re.match("<(\w+)>\w+</\1>","<html>login</html>")
# res = re.match(r"<(\w*)><(\w*)>.*</\2></\1>","<html><body>login</body></html>")
# print(res.group())
# 注意：从外到内排序，\num 从1开始


# 4. （?P<name>）  分组起别名
# 5. (?P=name)    引用别名为name分组匹配到的字符串
# res = re.match(r"<(?P<l1>\w*)><(?P<l2>\w*)>.*</(?P=l2)></(?P=l1)>","<html><body>login</body></html>")
# print(res.group())

# 匹配网址  前缀一般是www，后缀： .com、.net、.org等
li = ["www.baidu.com","www.python.org","http.jd.cn","www.py.en"]
# res = re.match(r"www.\w*.com|net|org","www.baidu.com")
# print(res.group())

# for i in li:
#     res = re.match(r"www.\w*(.(com|net|org|cn|en))",i)
#     if res:
#         print(res.group())
#     else:
#         print(f"{i}不是网址")
#         continue


# 2. 高级用法
# 1. search() 扫描整个字符串并返回第一个成功匹配的对象，如果匹配失败，就返回None
# res = re.search(r"th","python")
# print(res.group())

# # 2. findall() 扫描整个字符串并返回所有成功匹配的子字符串
# res = re.findall(r"th","python python python")

# print(res)
# 注意：不需要group()方法，直接返回所有匹配的子字符串并以列表的形式返回

# 总结：match（）从开始位置匹配，匹配成功返回match对象，通过group()方法提取数据，匹配失败就返回None，只匹配一次

# search（）从字符串中任意位置匹配，匹配成功返回第一个成功匹配的对象，通过group()方法提取数据，匹配失败就返回None，只匹配一次

# findall（）从字符串中任意位置匹配，匹配成功返回一个列表，列表中包含所有匹配成功的子字符串，而且不需要通过group()方法提取数据
 

# 3. sub(pattern, repl, string, count=0, flags=0)
#  替换字符串中所有匹配的子字符串
# pattern: 正则表达式(代表需要被替换的，也就是字符串的旧内容)
# repl: 替换的字符串 （新内容）
# string: 要匹配的字符串 
# count: 替换次数，默认替换所有匹配的子字符串
# flags: 匹配标志位,可以设置为0,或多个标志位的或操作
# res = re.sub(r"th","TH","python python python",1)
# print(res)
# res = re.sub(r"\d","2","这是这个月的第30天",1)
# print(res)

# 4. split(pattern, string, maxsplit=0, flags=0)
#  根据匹配的子字符串将字符串分割成一个列表
# pattern: 正则表达式
# string: 字符串 
# maxsplit: 指定最大分割次数，默认分割所有匹配的子字符串


# res = re.split(r",","hello,Python,123,hahha",maxsplit=1)
# print(res)

# 三、 贪婪与非贪婪匹配
# 1. 贪婪匹配（默认）：在满足匹配时，匹配尽可能长得字符串
# res = re.match("em*","emmmmmm...")
# print(res.group())

# # 2. 非贪婪匹配：在满足匹配时，匹配尽可能短的字符串
# res = re.match("em+?","emmmmmm...")
# print(res.group())


# 四、原生字符串
# print("sixs\\tar")
# print(r"sixs\ttar")
# res = re.match(r"\\",r"\game")
# print(res.group())
# 正则表达式中，匹配字符串中的字符\，需要\\\\.

