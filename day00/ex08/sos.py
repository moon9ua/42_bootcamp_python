# print("hello".isalpha())
# print("hello.".isalpha())

import sys

if len(sys.argv) != 2:
    exit("ERROR")

str = sys.argv[1]

if str.isalnum() == False:
    exit("ERROR")

