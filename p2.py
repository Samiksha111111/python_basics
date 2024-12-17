# tempr=float(input("Enter temperature in celcius: "))
# celcius=tempr
# fahrenheit =(celcius * 9/5) + 32
# print(f"temr in celcius {celcius} is equals to tmpr in fahrenheit {fahrenheit}")

#miter to kilometer
# mitre=float(input("Enter a length in meters: "))
# kilometer=mitre/1000
# print(f"Length in metres {mitre} is length in kilometer {kilometer}")

# feet=float(input("Enter in feets: "))
# inches=feet*12
# print(f"feet {feet} in inches {inches}")

#currency using hardcoded exchange rates
# dollor_to_rs=130
# dollor=float(input("Enter usd dollor: "))
# totol_rate=dollor*dollor_to_rs
# print(f"total rate {totol_rate} ")

# Simple Interest
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the annual interest rate (in %): "))
# time = float(input("Enter the time in years: "))
# simple_interest = (principal * rate * time) / 100
# print(f"Simple Interest is: {simple_interest:.2f}")

# # Compound Interest
# compound_interest = principal * ((1 + rate / 100) ** time - 1)
# print(f"Compound Interest is: {compound_interest:.2f}")

# # Area and Perimeter of a Rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area_rectangle = length * width
# perimeter_rectangle = 2 * (length + width)
# print(f"Area of the rectangle: {area_rectangle:.2f}")
# print(f"Perimeter of the rectangle: {perimeter_rectangle:.2f}")

# # Area and Circumference of a Circle
# radius = float(input("Enter the radius of the circle: "))
# area_circle = 3.14* radius ** 2 
# circumference_circle = 2 * 3.14* radius  
# print(f"Area of the circle: {area_circle:.2f}")
# print(f"Circumference of the circle: {circumference_circle:.2f}")

# Check if a number is Even or Odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is Even.")
# else:
#     print(f"{num} is Odd.")

# Check if a number is a Multiple of another number
# num = int(input("Enter the first number: "))
# divisor = int(input("Enter the second number: "))
# if num % divisor == 0:
#     print(f"{num} is a multiple of {divisor}.")
# else:
#     print(f"{num} is not a multiple of {divisor}.")
#square=i*i=num(is square)
# Check if a number is Prime 

# num = int(input("Enter a number to check if it's prime: "))

# if num <= 1:
#     print(f"{num} is not a Prime number.")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f"{num} is not a Prime number.")
#             break
#     else:
#         print(f"{num} is a Prime number.")

# num=int(input("Enter a number: "))
# if (num**0.5)%1==0:
#     print(f"{num} is a perfect square root.")
# else:
#      print(f"{num} is not a perfect square root.")

# num=int(input("Enter a number: "))
# if (num**(1/3))%1==0:
#     print(f"{num} is a perfect cube.")
# else:
#     print(f"{num} is not a perfect cube.")

user_choices=int(input('''
 Enter your choices:
1.Km to miles
2.Miles to Km
3.Centimeter to inch
4.Inch to centimeter
'''))
if user_choices==1:
    user_input=float(input("Enter km "))
    result=user_input*0.62137
    print(f"{user_input} Km= {result} in miles")
elif user_choices==2:
    user_input=float(input("Enter Km"))
    result=user_input*1.609344 
    print(f"{user_input} miles= {result} in km")
elif user_choices==3:
     user_input=float(input("Enter in centimeter"))
     result=user_input*0.393700787
     print(f"{user_input} centimeters = {result} in inches")
else:
    print("Invalid input")