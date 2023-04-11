# 여러방법이 있음
outStr = ""
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for k in range(0, count):
    outStr += inStr[count - (k + 1)]

print("내용을 거꾸로 출력 --> %s" % outStr)

# 다른 방법
outStr = ""
inStr = input("문자열을 입력하세요: ")
count = len(inStr)

for k in range(count-1, -1, -1):
    outStr += inStr[k]

print("내용을 거꾸로 출력 --> %s" % outStr)