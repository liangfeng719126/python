import numpy as np

# 花式索引

# 用数组索引
arr1 = np.arange(12) * 2
print(arr1)
i = np.array([1, 1, 2, 4, 8, 5])
print(arr1[i])
i = np.array([[2, 3],
			  [4, 5]])
# [[ 4  6]
#  [10 12]]
print(arr1[i])  # 结果和索引数组的形状是一一样的
# 当被索引的数组是多维时候
# [[[ 4  5]
#   [ 6  7]]
#
#  [[ 8  9]
#   [10 11]]]
arr2 = np.arange(12).reshape(6, 2)
print(arr2)
print(arr2[i])  # 其实还索引的第一个轴的元素

# 我们想对多维数组的其他轴也进行索引
j = np.array([[1, 1],
			  [1, 0]])  # j的形状和i的形状必须相同 三个维度也一样

print(arr2[i, j])  # i表示第一个轴索取的元素，j表示第二个轴所取的元素 两个形状相同才有意义 因为j是在i取到元素之后在取的第二个轴的元素
# 求最大值的索引 用索引求出最大值
data = np.sin(np.arange(20)).reshape(5, 4)
print(data)
print(data.argmax(0))  # 第一个轴的最大值的索引
print(data[data.argmax(0), [0, 1, 2, 3]])
print(data.max(0))  # 和上面一样直接求最大值不用索引求

# 数组作为索引进行对其他数组的元素值进行修改
data1 = np.arange(10)
print(data1)
data1[[1, 4, 6]] = 100
print(data1)

data1[[1, 4, 6]] = [300, 200, 20]  # 根据索引赋值 值也可以是对于索引的数组
print(data1)

# 有重复元素时候会多次分配
data2 = np.arange(10)
print(data2)
data2[[3, 3, 7]] = [300, 500, 600]
print(data2)  # 3索引的元素值最终是500

# 对于 +=操作 重复元素的时候要注意
data3 = np.arange(5)
data4 = data3.copy()
print(data3)
data3[[1, 1, 3]] += 1  # 相当于把元素先取出来生成一个值列表 data3[[1, 1, 3]] = data3[[1, 1, 3]]+1[2,2,4] 然后赋值
print(data3)
data4[[1, 1, 3]] = [2, 2, 4]
print(data4)

# 使用bool进行索引 明确的指出哪些元素需要哪些不需要
data5 = np.arange(12).reshape(3, 4)
print(data5)
b = data5 > 5
print(b)  # b的形状和data5必须一样
print(data5[b])  # 把b当作索引 相当于根据条件进行索引和赋值
data5[b] = 100
print(data5)
# ix 其实就是取数组的笛卡尔积组合的索引
print(np.ix_([1, 5, 7, 2], [0, 3, 1, 2]))
# 1,0 1,3 1,1 1,2
# 5,0 5,3 5,1 5,2
# 7,0 7,3 7,1 7,2
# 2,0 2,3 2,1 2,2


