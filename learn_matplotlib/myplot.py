import numpy as np
from numpy import linalg as la


# 矩阵乘法对圆形进行变换
def plot_matrix_multiplication(matrix, ax):
    theta = np.linspace(0, np.pi * 2, 100)
    x = np.sin(theta)
    y = np.cos(theta)
    data = np.array([x, y])
    data_m = matrix.dot(data)
    ax.plot(data_m[0], data_m[1])


def plot_matrix_eig(matrix, ax):
    u, v = la.eig(matrix)
    v1 = v.copy()
    v[:, 1] = 0
    v1[:, 0] = 0
    print(v)
    print(v1)
    ax.plot(v[0], v[1], marker='.', markersize=10, linestyle='-.')
    ax.plot(v1[0], v1[1], marker='.', markersize=10, linestyle='-.')
