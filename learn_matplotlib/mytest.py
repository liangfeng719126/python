import numpy as np
import matplotlib.pyplot as plt
import myplot  # 无法导入记得选择自己的工作空间，右键点击“Mark Directory as”选项，选择此选项下的Sources Root。就可以解决无法识别模块问题了

# 矩阵奇异值的视图化

fig, ax = plt.subplots(1, 1)
A = np.array([[3, 1],
              [0, 2]])
myplot.plot_matrix_multiplication(A, ax)
myplot.plot_matrix_eig(A, ax)

# 一维数组的情况
# x = [1, 2, 3]
# y = [2, 3, 4]
# plt.plot(x, y, color='red', marker='.', markersize=10, linestyle='-.')  # 画出（1，2）（2，3）（3，4）四个点并且连线
# 二维时候 会把列上的点连起来
# x = [[0, 1, 2],
#      [0, 1, 2]]
# y = [[1, 2, 3],
#      [2, 3, 4]]
# plt.plot(x, y, marker='.', markersize=10, linestyle='-.')
# 画网格点
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])
# X, Y = np.meshgrid(x, y)  # 全部组合的情况分开来
# print(X)
# print(Y)
# plt.plot(X, Y, marker='.', markersize=10, linestyle='')
# 画向量
# x = np.array([1, 2])
# y = np.array([3, 4])
# plt.plot(x, y, marker='.', markersize=10, linestyle='-.')


plt.grid()
plt.show()
