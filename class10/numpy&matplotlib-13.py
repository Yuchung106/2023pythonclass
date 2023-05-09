import matplotlib.pyplot as plt

fig, ax=plt.subplots()

#plt.subplots()를 사용하여 새로운 figure와 axes를 생성해서 이를 각각 fig와 ax 변수에 저장
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']

#과일별 막대의 색깔 레이블을 리스트로 선언
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

#막대 그래프를 생성. fruits를 x축, counts를 y축으로 하여 막대 그래프를 생성하고, 막대의 색상과 레이블을 지정
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color') # ax 객체의 legend 메소드를 사용하여 범례를 추가 하고 title 인자를 사용하여 범례의 제목 지정
plt.show()