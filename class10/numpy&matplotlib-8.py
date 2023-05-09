import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(10,100,200)#10 이상 100 미만의 정수 중에서 200개를 무작위로 추출하여 1차원 배열로 반환한 것을 x에 저장
y=np.random.randint(10,100,200)#y에 저장
size=np.random.rand(200)*100
plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.3) #투명도
plt.colorbar()
plt.show()
