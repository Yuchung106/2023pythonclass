import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
x = np.arange(0.0, 50.0, 2.0)#0부터 50까지 2씩 증가하는 값을 가지는 NumPy array 생성
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0 #x의 값에 1.3 제곱을 한 값에 임의의 난수를 더한 후 30을 곱해 y 배열에 저장
sizes = np.random.rand(*x.shape) * 800 + 500 # x와 동일한 shape을 가지는 랜덤한 값들로 이루어진 NumPy array를 생성하고, 이를 800을 곱하고 500을 더한 값을 sizes변수에 저장
fig, ax = plt.subplots()
ax.scatter(x, y, sizes, c="green", alpha=0.5, marker=r'$\clubsuit$', label="Luck")
ax.set_xlabel("Leprechauns")
ax.set_ylabel("Gold")
ax.legend()#그래프에 범례(legend) 추가
plt.show()
