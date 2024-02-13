import random
import time

from word import a

name = input("please enter your name :")
print(f"wellcame {name},"
      f"time to play Hangman")
time.sleep(1)

print("start guessing....")
time.sleep(0.5)

guesses = ""
turns = 10
b = random.choice(a)
print(b)
while True:
    guess = input("guess a character: ")
    guesses += guess
    if guess not in b:
        turns -= 1
        print("wrong")
        print(f"you have {turns} more guess")

    if turns == 0:
        print("you lose")
        break

    fail = 0
    for i in b:
        if i in guesses:
            print(i, end=" ")
        else:
            print("_", end="  ")
            fail += 1
    if fail == 0:
        print("you win")
        break
