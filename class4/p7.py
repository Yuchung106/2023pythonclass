n = int(input("몇개의 데이터 처리 : "))
listex = []
sum = 0

print('%d개의 데이터 입력 : ' % n)
for k in range(n):
    listex.append(int(input())) 
    sum += listex[k]
      
print('리스트 데이터의 합과 평균  : %d %.2f\n' % (sum, sum/n))

max, min = listex[0], listex[0]

for k in range(1, n):
    if listex[k] < min :
        min = listex[k]
    elif listex[k] > max :
        min = listex[k]

print('리스트 데이터의 최대값과 최소값 : %d, %d' % (max, min))