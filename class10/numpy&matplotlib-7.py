import matplotlib.pyplot as plt
import numpy as np

# 1. 기본 스타일 설정
plt.style.use('default') #matplotlib의 기본 스타일을 사용
plt.rcParams['figure.figsize']=(4 ,3 )
plt.rcParams['font.size']=12 #폰트사이즈

# 2. 데이터 준비
x = np.arange(2020 ,2027 )
y1 = np.array([1 ,3 ,7 ,5 ,9 ,7 ,14 ])
y2 = np.array([1 ,3 ,5 ,7 ,9 ,11 ,13 ])

# 3. 그래프 그리기
fig,ax1 = plt .subplots ()
ax1.plot(x, y1, '-s', color ='green', markersize =7, linewidth =5, alpha =0.7 ,label ='Price')
ax1.set_ylim(0, 18)
ax1.set_xlabel('Year') #x축 라벨
ax1.set_ylabel('Price ($)') #y축 라벨
ax1.tick_params(axis ='both',direction ='in')
ax2 =ax1.twinx()#ax1과 동일한 X축을 공유하지만 독립적인 y축을 가지는 두 번째 y축 생성
ax2.bar(x, y2, color ='deeppink', label ='Demand',alpha =0.7 ,width =0.7)
ax2.set_ylim (0 ,18 )#y축 범위 설정
ax2.set_ylabel(r'Demand ($\times10^6$)')
ax2.tick_params(axis ='y',direction ='in')
plt.show ()
