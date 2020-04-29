t = (19, 42, 21)

print("The {} numbers are:".format(str(len(t))), end="")
for i in range(len(t)):
    print(" " + str(t[i]), end="")
    if not i == len(t) - 1:
        print(",", end="")
    else:
        print()
