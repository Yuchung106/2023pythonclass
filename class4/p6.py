oddlist = list(range(1, 101, 2))
print(oddlist)

sum = 0

for k in oddlist:
    sum += k
print('합 : %d' % sum)