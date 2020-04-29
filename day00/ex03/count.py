def text_analyzer(*args):
    if len(args) > 1:
        print("ERROR")
        return
    elif len(args) == 0:
        string = input("What is the text to analyse?\n")
    else:
        string = args[0]
    upper = 0
    lower = 0
    punc = 0
    space = 0
    for i in range(len(string)):
        if string[i].isupper():
            upper += 1
        elif string[i].islower():
            lower += 1
        elif string[i] in ",.:!?@\'\"/_[]":
            punc += 1
        elif string[i] == ' ':
            space += 1
    print("The text contains " + str(len(string)) + " characters:\n")
    print("- " + str(upper) + " upper letters\n")
    print("- " + str(lower) + " lower letters\n")
    print("- " + str(punc) + " punctuation marks\n")
    print("- " + str(space) + " spaces")

# text_analyzer("Python 2.0, released 2000, introduced features \
# like List comprehensions and a garbage collection system capable \
# of collecting reference cycles.")
# text_analyzer()
