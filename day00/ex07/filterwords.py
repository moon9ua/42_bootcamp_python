import sys

if sys.argv[1].isdigit() is True or sys.argv[2].isdigit() is False:
    print("ERROR")
    exit()
old_str = sys.argv[1]
n = int(sys.argv[2])

punc = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
str = ""
for i in range(len(old_str)):
    if not old_str[i] in punc:
        str = str + old_str[i]

words = [""]
j = 0
for i in range(len(str)):
    if str[i] == ' ':
        j += 1
        words.append("")
    else:
        words[j] = words[j] + str[i]

ret = []
for word in words:
    if len(word) > n:
        ret.append(word)

print(ret)
