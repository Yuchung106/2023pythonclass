import random

gnum = 0
userw = 0
comw = 0
while True :
    com= random.randrange(3)
    user= int(input('가위0 바위1 보2 선택: '))
    if not(user in [0, 1, 2]):
        print('user= %d, com= %d' % (user, com))
        if user == com :
            print('비겼습니다!')
        elif (user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1) :
            print("User Win!")
            userw += 1
        else :
            print("Com Win!")
            comw += 1
    else:
        print('%d회로 가위바위보 ==End of game===' % gnum)
        print('user %d win, com %d win' % (userw, comw))
        break
    gnum += 1

