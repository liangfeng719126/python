print("初始化模块", __name__)
test = 1


#   方法定义在类的外面
def fun7(self):
    print("实例变量", self.name)


#  全局变量 在模块导入时候会初始化 属于模块的局域变量
out_name = "out_liangfeng"


def printOutName():
    print(out_name)


class Myclass2:


    def __init__(self, name):
        self.name = name

    # 用外部定义的函数赋值 和自由变量类似 类是自己的局部作用域 用全局的变量
    printName = fun7

    def printName1(self):
        fun7(self)  # 引用全局函数
        print(out_name)  # 引用全局变量

print(locals())