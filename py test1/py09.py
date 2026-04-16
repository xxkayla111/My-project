 # 1.类型转换
# 1.int() 转换为整数类型，只能转换数字字符串，不能转换非数字字符串，否则会报错
# print(int("123"))  #123
# print(int("abc"))  #会报错，不能转换非数字字符串  
# b = 3.14
# print(int(b))  #3 转换为整数类型会丢失小数部分
# # 2.float() 转换为浮点数类型，可以转换数字字符串和整数，不能转换非数字字符串，否则会报错
# print(float("3.14"))  #3.14
# print(float("123"))  #123.0
# print(float("abc"))  #会报错，不能转换非数字字符串
# print(float(3))  #3.0
# 3.str() 转换为字符串类型，可以转换任何类型的对象
# age = input("请输入年龄:")  #报错
 #输入的年龄是一个字符串类型

# age =int(input("请输入年龄:"))  
# print("输入的年龄是:", age)  #输入的年龄是: 18
# print("输入的年龄的类型是:", type(age))  #输入的年龄的类型
# if age > 18:
#     print("你已经成年了")
# else:
#     print("你还未成年")

# 1.2 float() 转换为浮点数类型，可以转换数字字符串和整数，不能转换非数字字符串，否则会报错
# print(float("31"))  #31.0
# print(float("abc"))  #会报错，不能转换非数字字符串
# 如果字符串中有正负号，数字，和小数点以外的字符，则不支持转换

# str() 转换为字符串类型，可以转换任何类型的对象
# n = 123
# print(type(n))  #<class 'int'>
# n = str(n)
# print(type(n))  #<class 'str'>
# print(n)  #123

# st = str(-1.0001000)
# print(st,type(st))  #-1.8

# li = [1, 2, 3]
# st = str(li)
# print(st,type(st))  #[1, 2, 3] <class 'str'>

# # eval() 将字符串当成表达式来计算，并返回计算结果
# st = "1 + 2 + 20"
# print(st)  #1 + 2 + 20
# print(eval(st))  #23
# a ="20 / 4"
# print(eval(a))  #5.0


# str -> list
# stl = "[[1,2],[3,4],[5,6]]"
# print(type(stl))
# li = eval(stl)
# print(li,type(li))
# # 不安全 容易被恶意攻击


#list（）将可迭代对象转换成列表
 #tuple -> list
t = (1, 2, 3)
print(list(t))  #<class 'tuple'>

#dict -> list
d = {"name": "bingbing", "age": 18, "gender": "female"}
print(list(d))  #['name', 'age', 'gender'] 结果是字典的键组成的列表 
#字典转换成列表时，默认是把字典的键转换成列表元素，如果想要把字典的值转换成列表元素，可以使用dict.values()方法
print(list(d.values()))  

# set -> list
s = {1, 2, 3, 4, 5,5,5,6,6,7,8,9}  #去掉重复元素
print(list(s))  #[1, 2, 3, 4, 5] 集合转换成列表时，结果是集合中元素组成的列表，集合是无序的，所以列表中的元素顺序也是不确定的
