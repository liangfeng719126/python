import numpy as np
import matplotlib.pyplot as plt

fig, ax_list = plt.subplots(2, 2)  # 划分四个Axis

x = np.linspace(0, 10, 100)

ax_list[0, 0].plot(x, x)  # 对其中每个Axis画图
ax_list[0, 1].plot(x, x)
plt.show()
