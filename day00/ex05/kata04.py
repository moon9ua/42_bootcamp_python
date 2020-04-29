x = (0, 4, 132.42222, 10000, 12345.67)

if len(x) != 5:
    print("ERROR")
    exit()

## 지금까지는 서식지정자와 format을 잘 몰라서 이렇게 했었음.
# list = []
# if len(str(x[0])) == 1:
#     tmp = "day_0" + str(x[0])
# else:
#     tmp = "day_" + str(x[0])

# list.append(tmp)

# if len(str(x[1])) == 1:
#     tmp = "ex_0" + str(x[1])
# else:
#     tmp = "ex_" + str(x[1])
# list.append(tmp)

# list.append(str(round(x[2], 2)))

# list.append(str(x[3]))
# list.append(str(x[4]))

# print("{}, {} : {}, {}, {}".format(list[0], list[1], list[2], list[3], list[4]))


## 서식 지정자 사용
# print("day_%02d, ex_%02d : %.2f, %2f, %2f" %(x[0], x[1], x[2], x[3], x[4]))

## 와 이게 되네. 내가 찾던 방법!
# print("day_%02d, ex_%02d : %.2f, %2f, %2f" %x)

## 서식지정자로 하는 방법을 못찾아서 이렇게 했었음.
# print(
#     "day_%02d, ex_%02d : %.2f, {}, {}"
#     .format(format(x[3], ".2e"), format(x[4], ".2e"))
#     %(x[0:3])
#     )


## 최종 답안
print("day_%02d, ex_%02d : %.2f, %.2e, %.2e" %x)