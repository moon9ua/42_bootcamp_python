x = (3,30,2019,9,25)

if len(x) != 5:
    print ("ERROR")
    exit() # 인자로 뭐가 들어가는거지?

## 형식 바꾸기 전엔 이런 식으로.
## c에서는 int인지 등에 따라 d, s 등을 적어주어야 했는데, 파이썬엔 없는듯?
# print("{}/{}/{} {}:{}".format(x[3], x[4], x[2], x[0], x[1]))

hour = str(x[0])
min = str(x[1])
year = str(x[2])
month = str(x[3])
day = str(x[4])

## for arg in {hour, min, month, day}: # 왜 이렇게 하면 순서가 랜덤하게 바뀔까?
# for arg in [hour, min, month, day]:
#     # print(arg, len(arg))
#     if len(arg) == 1:
#         arg = '0' + arg
#     print (arg)
# print(hour) # 이렇게 하면 for문 안에서는 바뀌는데, 실제로는 값이 바뀌지가 않음. 왜?
# print ("{}/{}/{} {}:{}".format(month, day, year, hour, min))

list = []
for arg in [month, day, year, hour, min]:
    if len(arg) == 1 and arg != year:
        list.append("0" + arg)
    else:
        list.append(arg)
print ("{}/{}/{} {}:{}".format(list[0], list[1], list[2], list[3], list[4]))
# 리스트 요소 하나씩 넣지 않고 다 출력해주는거 없나?