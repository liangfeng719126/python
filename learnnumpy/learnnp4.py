import numpy as np
from numpy import linalg as la

# 矩阵和矩阵的乘法
A = np.array([[1, 2], [0, 3]])
b = np.array([[4, 5, 6], [7, 8, 9]])
print(A.dot(b))

# 矩阵和向量的乘法
B = np.array([[1, 2],
              [0, 3]])  # 行表示一个特征的所有样本值（向量个数） 列表示一个样本所有特征值（向量）
c = np.array([[2],
              [3]])
print(B.dot(c))

# 计算矩阵特征值和特征向量
A1 = np.array([[3, 1],
               [0, 2]])
u, v = la.eig(A1)
print(u)
print(v)

# 计算矩阵的奇异值
u1, v1, w1 = la.svd(A1, full_matrices=True)
print(u1)
print(v1)
print(w1)