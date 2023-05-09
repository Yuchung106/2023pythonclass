import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11) #1부터 10까지의 정수를 배열로 만들어서 x에 저장
y = x * x

plt.title("Line graph")#그래프 제목
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y, color ="red")
plt.show()
