# Created by Doğukan DOĞU
# Wednesday, January 30th, 2019

import random

secretNumber = random.randint(0, 20)
guessChance = 6
print("Hey! I am thinking of a number between 0 and 20. Can you guess it? You have 6 chances.")

for guessesTaken in range(6):
    guess = int(input("Guess it :"))

    if guess < secretNumber:
        print("Your guess is too low.")
        guessChance -= 1
        print("Your guess chance is {}".format(guessChance))

    elif guess > secretNumber:
        print("Your guess is too high.")
        guessChance -= 1
        print("Your guess chance is {}".format(guessChance))

    else:
        break

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
    print("My number was {}".format(secretNumber))
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
