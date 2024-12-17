import random
num_to_guess=random.randint(1,10)
while True:
    guess=int(input("Enter a random number: "))
    if guess==num_to_guess:
        print("number being guessed is correct! ")
    elif guess<num_to_guess:
        print("is too small")
    else:
        print("is too big")
