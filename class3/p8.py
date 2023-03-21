dan = 0
num = 0

for dan in range(2, 10) :
    print('\n%d단: \n' % dan, end = '')
    for num in range(1, 10):
        print('%d x %d = %d\n' % (dan, num, dan * num), end = '')
