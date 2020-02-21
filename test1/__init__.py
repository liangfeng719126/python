import numpy


# 列表推导式 [1,2,3] [3,1,4] 两个序列元素不同的组合
# 列表推导式的结构是由一对方括号所包含的以下内容：一个表达式，
# 后面跟一个 for 子句，然后是零个或多个 for 或 if 子句。
# 其结果将是一个新列表，由对表达式依据后面的 for 和 if 子句的内容进行求值计算而得出。
def fun1():
    comb = []
    for i in [1, 2, 3]:
        for j in [3, 1, 4]:
            if i != j:
                comb.append((i, j))
    print("复杂写法：", comb)
    # 可以把 comb.append((i, j)) 操作不会对循环有任何影响 可以简化导前面去如下写法
    comb1 = [(i, j) for i in [1, 2, 3] for j in [3, 1, 4] if i != j]
    print("简单写法：", comb1)
    arr = [x ** 2 for x in range(10)]
    print(arr)


# 嵌套列表推导式 3x4的矩阵转置
def fun2():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    matrix_T = [[row[i] for row in matrix] for i in range(4)]
    print(matrix_T)

    matrix_T1 = []
    for i in range(4):
        rows = []
        for row in matrix:
            rows.append(row[i])
        matrix_T1.append(rows)
    print(matrix_T1)


# 元组打包解包 函数的多重赋值也是打包和解包的过程
def fun3():
    t = "a", "b", "c"
    print("打包：", t)
    t1, t2, t3 = t
    print("解包：", t1, " ", t2, " ", t3)


# 异常
#
#     如果在执行 try 子句期间发生了异常，该异常可由一个 except 子句进行处理。 如果异常没有被某个 except 子句所处理，则该异常会在 finally 子句执行之后被重新引发。
#
#     异常也可能在 except 或 else 子句执行期间发生。 同样地，该异常会在 finally 子句执行之后被重新引发。
#
#     如果在执行 try 语句时遇到一个 break, continue 或 return 语句，则 finally 子句将在执行 break, continue 或 return 语句之前被执行。
#
#     如果 finally 子句中包含一个 return 语句，则返回值将来自 finally 子句的某个 return 语句的返回值，而非来自 try 子句的 return 语句的返回值。#
def fun4(x, y):
    try:
        a = x / y
    except ZeroDivisionError:  # 捕获异常
        print("division by zero!")
    else:  # 没有异常时执行
        print(a)
    finally:  # 始终执行 如果还有异常则在执行后发生异常
        print("finally!")


# global nonlocal
# 闭包是扩大了作用域的函数 自由变量是未在局部作用域绑定的变量（外层的变量）可以直接访问其值但是不能修改
# 当然引用变量可以通过调用方法修改，和变量传递类似 但是变量就不行 想修改必须显示添加nonlocal声明是外层的变量 进行修改访问
# global 就是模块类的全局变量 在哪声明都行。
def fun5():
    fvalue = 1

    def fun6():
        nonlocal fvalue  #
        fvalue = 2  # 不加nonlocal赋值的 会从自由变量变为局部变量 外层fvalue值不变 加了之后显示声明为自由变量 使其可以修改
        print(fvalue)
        print(locals())

    fun6()
    print(fvalue)
    global fvalue1  # 声明为模块类全局变量
    fvalue1 = 3


fun5()
print(fvalue1)


# fun3()
# print(ts.test)

# 方法对象和类对象
class MyClass1:
    count = 1  # 类变量 所有实例共享
    tags = []

    def __init__(self, name):
        self.name = name  # self后面的变量是实例变量
        print("初始化方法")  # 创建对象时候调用 可以传递参数

    def myPrint(self):
        print("hello word!")

    def printName(self):
        # print(count) 报错 函数类不能使用类变量 搜索顺序是 legb
        # 局部作用域(local) -> 闭包函数外的函数(enclosing) -> 全局作用域(global) -> 内建作用域(build-in)
        # 搜索过程没有类的作用域
        # 当然模块作用域 类作用域 函数作用域 才会引入新的作用域 if else 语句块是在同一个作用域类的 如
        # >>> if True:
        # ...  msg = 'I am from Runoob'
        # ...
        # >>> msg
        # 'I am from Runoob'
        # >>>
        # 类是一个可以访问其外层作用域的局部作用域，
        # 但其本身却不能作为一个外层作用域被访问。
        # 因为方法函数中对名称的搜索跳过了外层的类，
        # 所以类属性必须作为对象属性并使用继承来访问#
        print(self.name)


my_class = MyClass1("dog")  # 类对象
my_method = my_class.myPrint  # 方法对象
my_method()  # 方法对象的调用 没有第一个参数self 方法对象相当于把对象和类函数绑定的对象 和下面等价
MyClass1.myPrint(my_class)

my_class1 = MyClass1("cat")
MyClass1.count += 1  # 类变量赋值+1
MyClass1.count += 1
print(my_class1.count, MyClass1.count)  # 实例打印类变量
my_class1.count = my_class1.count + 1  # 相当于给实例新增啦一个变量
print(my_class1.count, MyClass1.count, my_class.count)  # 实例不能修改只能访问类变量和签名自由变量类似
my_class1.count1 = 10  # 实例变量不需要声明 在第一次被赋值时候产生
print(my_class1.count1)

my_class.tags.append("dog")
my_class1.tags.append("cat")
print(MyClass1.tags)
my_class.tags = ["dog1", "cat1"]  # 实例变量可以访问类变量 但是不能修改 赋值操作相当于新增了一个变量 还是作用于的问题
print(my_class.tags, my_class1.tags, MyClass1.tags)

my_class.name = "dog1"
my_class.printName()

import test3

my_class2 = test3.Myclass2("liangfeng")
my_class2.printName1()


# 注意数据属性会覆盖掉具有相同名称的方法属性


class BClass:
    def __init__(self, name):
        self.name = name
        print("init_base")
        self.__printName()  # 调用_BClass__printName 方法 _BClass__printName 没被重写所以打印baseName
        self.printName()  # 调用被重写的方法 被重写 打印subName

    def printName(self):
        print("baseName", self.name)

    __printName = printName  # 私有变量 就是给变量起了别名 _BClass__printName

    print(locals())  # 在类掉方法 __init__ 之前执行 查看局部变量表里面的符号


class SubClass(BClass):
    def __init__(self, name, age):  # 该方法会覆盖父类的方法 没有该方法会调用父类的__init__方法
        super(SubClass, self).__init__(name)  # 要是父类也初始化需要调用父类的 __init__ 方法
        print("initSubClass")
        self.age = age

    def printName(self):
        print("subClassName", self.name)


# python 是动态类型的语言所以有多态特性
# subObj 赋值什么对象就是什么对象 没有明确的类型 这和java的多态一样
subObj = SubClass("dog", 12)
subObj.printName()


def f(a, L=[]):
    L.append(a)
    return L

# words = ['a', 'b', 'c']
# for w in words:
#     time.sleep(5)
#     print(w)
#     if w == 'c':
#         words.insert(-1,'c')
#     print(words)
