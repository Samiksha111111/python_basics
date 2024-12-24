
# def is_palindrome(string):
#     return string==string[::-1]

# print(is_palindrome("aca"))
# print(is_palindrome("aabbaa"))
# print(is_palindrome("abbb"))
# print(is_palindrome("baabbb"))

# radius=float(input("Enter radius: "))
# area_of_circle=3.14* radius**2
# print(f"circle of area: {area_of_circle}")

# def area_of_circle(radius):
#     return 3.14*radius**2
# print(area_of_circle(5))

# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True
# number=int(input("Enter a number: "))
# print(is_prime(number))

# def fibonacci_sequence(max_number):
#     sequence=[]
#     a=0
#     b=1
#     while a<=max_number:
#         sequence.append(a)
#         a=b
#         b=a+b
#     return sequence
# max_number=int(input("Enter max number: "))
# sequence=fibonacci_sequence(max_number)
# print(f"Fibonacci sequnce: {sequence}")
# print(f"The sum is: {sum(sequence)}")

# def multiplication_table(num):
#     for i in range(1,11):
#         print(f"{num} *{i} = {num*i}")
# num=int(input("Enter a number :"))
# print(multiplication_table(num))

# def leap_year(year):
#     return year % 4 ==0 and (year%100!=0 or year %400==0)
# year=int(input("Enter year: "))
# print(leap_year(year))

# def count_vowel(string):
#     vowels="aeiouAEIOU"
#     return sum(1 for char in string if char in vowels)
# text=input("Enter text: ")
# print("no of vowels:", count_vowel(text))

   
def lcm(a,b):
    greater=max(a,b)
    while True:
        if greater%a==0 and greater % b == 0:
            return greater
        greater += 1


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM:", lcm(num1, num2))