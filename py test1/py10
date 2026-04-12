# def funa (a,b):
#     return a + b
# print(funa(1,2))  #3
# print(funa("hello ", "world"))  #hello world    

# 3.2 默认参数
def funb(a, b=10):#默认参数b的值为10，
    #如果调用函数时没有传入b的值，
    # 则使用默认值10,有默认参数的函数在定义时，
    # 默认参数必须放在非默认参数的后面，
    # 否则会报错
    print(a,b)
funb(5,20)  #5 20
funb(5)  #5 10 使用默认参数b的值10

# 3.3 可变参数
def func(*args):#args是一个可变参数，
    #参数名这样是为了命名规范，
    # 也可以使用其他名字，但必须在参数名前加*号，
    # 以表示这是一个可变参数，*args可以接受任意数量的位置参数，
    #可变参数可以接受任意数量的位置参数，
    # 以元组的形式传递给函数
    print(args)
func(1,2,3)  #(1, 2, 3)
func("a","b","c")  #('a', 'b', 'c')
func('你好世界')  #('你好世界',) 
# 字符串被当成一个整体传递给函数

#3.4关键字参数
def func2(**kwargs):#kwargs是一个关键字参数，
    #参数名这样是为了命名规范，
    # 也可以使用其他名字，但必须在参数名前加**号，
    # 以表示这是一个关键字参数，**kwargs可以接受任意数量的关键字参数，
    # 以字典的形式传递给函数
    print(kwargs)
    print(type(kwargs))   
func2(a=1, b=2, c=3)  #{'a': 1, 'b': 2, 'c': 3} 
func2(name="bingbing", age=18, gender="female")  
#{'name': 'bingbing', 'age': 18
# 'gender': 'female'}
func2()     
 #{} 没有传入任何关键字参数，kwargs是一个空字典
# 作用：可以扩展函数的功能，增加函数的灵活性和适应性，
# 可以接受任意数量的参数，适用于参数数量不确定的情况



# 3.5 函数嵌套
def outer():
    print("这是外层函数") 
    def inner(a):
        print("这是内层函数")
        # 内层函数不可以调用外层函数中的变量
        # ，但可以访问外层函数中的变量
       
        print(a)
    inner(20)  #在外层函数中调用内层函数
outer()  #调用外层函数，输出：这是外层函数 这是内层函数
