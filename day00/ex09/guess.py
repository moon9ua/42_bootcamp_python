print (
'''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
'''
)

import random
x = str(random.randint(1, 99))

n = ""
count = 0
while n != x:
    n = input("What's your guess between 1 and 99?\n>> ")
    if n == "exit":
        exit("Goodbye!")
    if n.isdigit() == False:
        print("That's not a number.")
    elif n > x:
        print("Too high!")
    elif n < x:
        print("Too low!")
    count += 1

if x == "42":
    print("The answer to the ultimate question of life, the universe and everything is 42.")
if count == 1:
    print("Congratulations! You got it on your first try!")
else:
    print (
'''Congratulations, you've got it!
You won in %d attempts!''' % count
    )

### 여러줄 print 할때 어떻게 깔끔하게 하지?