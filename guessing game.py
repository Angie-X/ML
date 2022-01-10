import random

def guess(x):
    ran_number = random.randint(1, x)
    print(f"random number is: {ran_number}")
    guess = 0
    while guess != ran_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < ran_number:
            print("too low")
        elif guess > ran_number:
            print("too high")
    print("you got")

guess(9)
