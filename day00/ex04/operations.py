import sys

usage = "python operations.py <number1> <number2>"
example = "Example:\n\tpython operations.py 10 3"

print(sys.argv[1])
print(type(sys.argv[1]))
print(type(sys.argv[2]))
print(sys.argv[2])
# print('"123"'.isdigit())

if len(sys.argv) > 3:
    print("InputError: too many arguments\n")
    print(usage)
    print(example)
elif len(sys.argv) < 2:
    print("InputError: few arguments\n")
    print(usage)
    print(example)
elif sys.argv[1].isdigit == False or sys.argv[2].isdigit() == False:
    print("InputError: only numbers\n")
    print(usage + "\n" + example)
else:
    print("Sum:\t" + str(sys.argv[1] + sys.argv[2]))