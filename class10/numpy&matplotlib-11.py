import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(10)
y=np.random.rand(10)
colors=np.random.randint(0,100,10)
sizes=np.pi*1000*np.random.rand(10) #0 이상 1 미만의 난수 10개를 생성한 후, 각각에 1000을 곱하고 np.pi를 곱한 값을 sizes 변수에 저장
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7)#산점도
plt.show()
