import random as r
import time as t

slot = [0]*3
n = int(input('슬롯머신을 몇 번 돌릴까요?'))

for s in range(n):
    for k in range(3):
        slot[k] = r.randrange(7, 10)    # 무작위 수 7, 8, 9 생성
        print('%d ' % slot[k], end = '')
        t.sleep(1)
    if slot[0] + slot[1] + slot[2] == 21: # 모두 7인지 검사 slot[0] == 7 and slot[1] == 7 and slot[2] == 7
        print('\n잭팟이 터졌네요')
        break
    else:
        print('\n아까워라~~\n')