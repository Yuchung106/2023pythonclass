import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
plt.rcdefaults()# Matplotlib의 기본 설정 값으로 초기화 
fig, ax = plt.subplots()
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))

# people 튜플의 길이를 기반으로 인덱스 배열 y_pos를 생성
performance = 3 + 10 * np.random.rand(len(people))

#people의 길이의 개수만큼 3에서 13까지의 난수를 생성하고, 이를 performance 변수에 할당
error = np.random.rand(len(people))
ax.barh(y_pos, performance, xerr=error, align='center')# 수평 막대 그래프를 생성
ax.set_yticks(y_pos, labels=people)
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
plt.show()
