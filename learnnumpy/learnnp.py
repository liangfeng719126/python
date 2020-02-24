import numpy as np
import sys

# 创建ndarray
arr = np.array([1, 2, 3])
print(arr)
print("数组中数据类型：", arr.dtype)

arr1 = np.array([(1, 2, 3), (4, 5, 6)])
print("二维数组，rank为2：", arr1)
# 创建初始值是0的数组3*4 其中4是第2个轴的数据个数(最里层的数组数据个数)，
# 3是第1个轴的数据个数(倒数第二层的数组的数据个数)
arr2 = np.zeros((3, 4))
print(arr2)

# 创建数字组成的数组类似range函数
# 2起始数字，10结束数字，3 步长
arr3 = np.arange(2, 10, 3)
print(arr3)

# linspace生成浮点数
# 10是数字数量
arr4 = np.linspace(0, 2, 10)
print(arr4)

# 打印大量数据[   0    1    2 ... 9997 9998 9999] 中间有省略号
arr5 = np.arange(10000)
print(arr5)
# 去掉打印省略
np.set_printoptions(threshold=sys.maxsize)
arr5 = np.arange(10000)
# print(arr5)


# 数组的算术运算会应用的单个元素上
# 加法把单个元素相加 乘法类似
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a + b
print("a+b:", c)
c1 = b * 2
print(c1)
# 比较运算也一样
c2 = b > 2
print(c2)

# 和矩阵乘法不同两个数组的乘法还是对应的元素相乘
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 1], [4, 3]])
print(A * B)
# 要用矩阵乘法可以用dot方法
C = A.dot(B)
print(C)

# 一元操作如求数组的最值求和
arr6 = np.arange(4)
print(arr6.sum())

# 对于多维数组可以用轴的方式进行一元操作来求部分一元值
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

arr7 = np.arange(12).reshape(3, 4)
print(arr7)
print(arr7.sum(axis=0))  # 对第一个轴的元素相加得到的是一维4个数的数组# [12 15 18 21]#
print(arr7.sum(axis=1))  # [ 6 22 38]

# 通函数 一些常用的数学函数
arr8 = np.arange(3)
print(np.exp(arr8))

# 一维数组的切片操作
arr9 = np.arange(10)
print(arr9)
print(arr9[::2])  # 取值
arr9[::2] = 100  # 赋值
print(arr9)
print(arr9[::-1])  # 注意 切片操作是新生成一个数组
print(arr9)

# 一维数组的遍历
arr10 = np.arange(10)
for i in arr10:
    print(i)

# 多维数组的切片操作和遍历
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
tarr = np.arange(12).reshape(3, 4)
print(tarr)
print(tarr[1, 2])  # 1代表第一个轴的元素索引，2代表第二个轴的元素索引
print(tarr[:, 1])  # :其实表示的是对于第一个轴的元素切片[:] 这里取全部元素 1表示对第一个轴的元素取1索引元素
print(tarr[0:2, 3])
print(tarr[0:2, 0:2])  # 第一个0:2表示对第一个轴取0到2的元素，第二个0:2表示在第一个轴取值的情况下在取第二个轴的0到2的值
print(tarr[0:2])  # 没有表明的轴表示取全部值
print(tarr[0:2, :])  # 推荐都加上：可阅读性更好
# 三维的情况
tarr2 = np.arange(12).reshape(2, 2, 3)
print(tarr2)
print(tarr2[:, 1, :])  # 索引加切片操作

# 对tarr遍历
for item in tarr:
    print(item)
# flat 用于遍历所有元素
for item in tarr.flat:
    print(item)

