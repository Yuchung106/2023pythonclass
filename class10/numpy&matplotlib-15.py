import matplotlib.pyplot as plt

ratio=[34,32,16,18]
labels=['Apple','Banana','Melon','Grapes']
plt.pie(ratio, labels=labels,autopct='%.lf%%') #파이차트 출력
plt.show()
