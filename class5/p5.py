mdict_list = {'기본햄버거': 4000, '치즈햄버거': 4500, '불고기버거': 5000, '와퍼킹버거': 7000}
print(mdict_list)

# 새우버거, 5500원 추가
mdict_list['새우버거'] = 5500
print(mdict_list)

#불고기버거의 가격을 500원 인상
mdict_list['불고기버거'] = mdict_list['불고기버거'] + 500
print(mdict_list)

#기본햄버거 삭제하고 나이스버거 2000원 추가
del[mdict_list['기본햄버거']]
mdict_list['나이스버거'] = 2000
print(mdict_list)

#for ~ in ~~을 이용하여 출력

for k in mdict_list.keys():
    print(k, ':', mdict_list[k])