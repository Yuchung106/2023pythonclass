import matplotlib.pyplot as plt 
import numpy as np 

np.random.seed(0) #랜덤 시드를 0으로 설정
n = 50 
x = np.random.rand(n) 
y = np.random.rand(n) 
area = (30 * np.random.rand(n))**2 
colors = np.random.rand(n) 
plt.scatter(x, y, s=area, c=colors) 
plt.show()
