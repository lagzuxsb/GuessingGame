import random

randomNumber = random.randint(1, 100)
GU = int(input("Take a guess: "))
tries = 1

while GU != randomNumber:
    if GU > randomNumber:
        print("Lower..")
    else:
        print("Higher...")


    GU = int(input("Take a guess: "))
tries += 1
if tries == 5:
    print("You failed to guess the number!")

if GU == randomNumber:
    print("You guessed it! The number was", randomNumber)
    print("And it only took you", tries, "tries!\n")
try:
    input("Press the enter key to exit.")
except:
    pass
