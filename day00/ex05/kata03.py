phrase = "The right format"

if len(phrase) > 42:
    print(phrase[0:41])
    exit()
while len(phrase) != 42:
    phrase = "-" + phrase

print(phrase, end="")
