# 처음에 한 방법
# import sys

# text = ""

# for i in range(1, len(sys.argv)):
# 	if text == "":
# 		text = sys.argv[i]
# 	else:
# 		text = text + " " + sys.argv[i]
# 	i = i + 1

# new_text = ""

# for i in range(len(text) - 1, -1, -1):
# 	if text[i].isupper() == True:
# 		new_text = new_text + text[i].lower()
# 	else:
# 		new_text = new_text + text[i].upper()
# 	i = i - 1

# print(new_text)


# 다시 해본 방법
import sys

str = ' '.join(sys.argv[1:])
str = str[::-1]

for i in range(len(str)):
    if str[i].islower():
        print(str[i].upper(), end='')
    elif str[i].isupper():
        print(str[i].lower(), end='')
    else:
        print(str[i], end='')
