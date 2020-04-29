import sys

if len(sys.argv) == 1:
    exit()

list = sys.argv[1:]
str = ' '.join(list)

test = str.replace(" ", "")
if test.isalnum() is False:
    exit("ERROR")

dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

str = str.upper()
ret = ""
for i in range(len(str)):
    if str[i] == ' ':
        ret += '/'
    else:
        ret += dict[str[i]]
    if not i == len(str) - 1:
        ret += ' '

print(ret)
