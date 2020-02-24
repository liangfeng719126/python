import numpy as np

# 赋值，拷贝和视图

# 数组赋值 属于引用的赋值不会有新的数组产生
arr1 = np.array([1, 2, 3])
arr2 = arr1
print(arr2 is arr1)  # is比较的是数组对象的id 相当于java的对象地址 他们指向统一个对象所以是ture
arr2[1] = 100
print(arr1)  # [  1 100   3] 改变arr2也改变arr1 arr2是arr1的一个引用

# 视图或浅拷贝 numpy的切片操作会放回视图
arr3 = np.array([1, 2, 3, 4])
arr4 = arr3.view()
print(arr4 is arr3)  # 3 和4 不同
print(arr4.base is arr3)  # 4的base是3
print(arr4.flags.owndata)  # 4不拥有数据

arr4[2:] = 10
print(arr3)  # 修改4的数据会修改三的数据和前面的赋值类似但是id不同

# 深拷贝 就是一个完整的副本不影响原理的数据 id也不同
arr5 = np.array([1, 2, 3, 4, 5])
arr6 = arr5.view()
arr7 = arr6[2:].copy()  # 切片后拷贝视图数据减少数据量
print(arr7, arr6)  # 拷贝后的数据和原理数据独立存在
arr7[2] = 100
print(arr7, arr6)

