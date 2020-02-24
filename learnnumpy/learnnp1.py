import numpy as np

# 数组形状
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(arr1)
print(arr1.shape)  # 数组的形状由轴的元素的数量决定

# 可以把二维数组的形状变成一维数组
arr2 = arr1.ravel()
print(arr2)

# 也可以用reshape改变数组的形状
print(arr1.reshape(3, 2))  # 注意改变后是新生成的数组
print(arr1.T)

tarr1 = np.arange(12).reshape(2, 2, 3)
tarr2 = np.arange(12, 24, 1).reshape(2, 2, 3)
# [[[ 0  1  2]
#   [ 3  4  5]]
#
#  [[ 6  7  8]
#   [ 9 10 11]]]
# ------
# [[[12 13 14]
#   [15 16 17]]
#
#  [[18 19 20]
#   [21 22 23]]]
# ------
print(tarr1)
print("------")
print(tarr2)
print("------")
# [[[ 0  1  2]
#   [ 3  4  5]
#   [12 13 14]
#   [15 16 17]]
#
#  [[ 6  7  8]
#   [ 9 10 11]
#   [18 19 20]
#   [21 22 23]]]
print(np.hstack((tarr1, tarr2)))  # hstack沿第二轴进行合并
# [[[ 0  1  2]
#   [ 3  4  5]]
#
#  [[ 6  7  8]
#   [ 9 10 11]]
#
#  [[12 13 14]
#   [15 16 17]]
#
#  [[18 19 20]
#   [21 22 23]]]
print(np.vstack((tarr1, tarr2)))  # vstack沿第一轴进行合并
# [[[ 0  1  2 12 13 14]
#   [ 3  4  5 15 16 17]]
#
#  [[ 6  7  8 18 19 20]
#   [ 9 10 11 21 22 23]]]
print(np.concatenate((tarr1, tarr2), 2))  # 指定第三轴合并

#
arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])
arr5 = np.array([7, 8, 9])

print(np.column_stack((arr3, arr4, arr5)))  # 把一维数组堆叠到二维数组上 按照列堆叠

# 切分数组
# [array([[[0, 1, 2],
#         [3, 4, 5]]]),
#  array([[[ 6,  7,  8],
#         [ 9, 10, 11]]])]
print(np.vsplit(tarr1, 2))  # 把第一个轴上的元素切分维两份
# [array([[[0, 1, 2]],
#        [[6, 7, 8]]]),
# array([[[ 3,  4,  5]],
#        [[ 9, 10, 11]]])]
print(np.hsplit(tarr1, 2))  # 把第二个轴上的元素切分两份
print(np.array_split(tarr1, 3, 2)) # 指定第三个维度切分三份
