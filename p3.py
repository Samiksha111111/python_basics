user_choices=int(input('''
 Enter your choices:
1.Simple interest
2.Compound interest
'''))
while True:
    if user_choices==1:
        principle=float(input("Enter the principle amount: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        time = float(input("Enter the time in years: "))
        simple_interest=(principle*rate*time)/100
        print(f"simple interest: {simple_interest}")
    elif user_choices==2:
        principle=float(input("Enter the principle amount: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        time = float(input("Enter the time in years: "))
        compound_interest = principle * ((1 + rate / 100) ** time - 1)
        print(f"simple interest: {compound_interest}")
    else:
        print("Invalid input")

