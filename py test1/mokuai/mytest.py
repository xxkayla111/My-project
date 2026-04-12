def test():
    print("哈哈哈")
if __name__ == "__main__":
    print("这是pytest")
    #如果当前模块是被直接运行的，输出：这是pytest
else:
    print("这是被导入的pytest")  #如果当前模块是被导入的，输出：这是被导入的pytest