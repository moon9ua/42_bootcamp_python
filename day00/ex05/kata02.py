x = (3, 30, 2019, 9, 25)

if len(x) != 5:
    print("ERROR")
    exit()

hour = str(x[0])
min = str(x[1])
year = str(x[2])
month = str(x[3])
day = str(x[4])

list = []
for arg in [month, day, year, hour, min]:
    if len(arg) == 1 and arg != year:
        list.append("0" + arg)
    else:
        list.append(arg)
print("{}/{}/{} {}:{}".format(list[0], list[1], list[2], list[3], list[4]))
