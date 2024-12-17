import random
random_number=random.randint(1,11)
while True:
    user_guess=int(input("Guess a number: "))
    if user_guess==random_number:
        print("is correct")
        print("you win")
    elif user_guess<random_number:
        print("is too small")
    else:
        print("is too big.")

   