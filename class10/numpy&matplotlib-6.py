import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9,10) #-9부터 9까지의 값을 가진 1차원 numpy 배열 생성
y = x ** 2
plt.plot(x, y, linestyle=":", marker="*")
plt.show()
