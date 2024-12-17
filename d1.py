num1=float(input("Enter a first number:"))
num2=float(input("Enter a second number:"))
operation=(input("Enter operators like +,-,/,*:"))
if operation == '+':
    result=num1+num2
elif operation == '-':
    result=num1+num2
elif operation == '*':
    result=num1+num2
elif operation == '/':
    if num2 == 0:
        result="Error division by 0"
    else:
        result=num1/num2
else:
    result="Invalid operation"

print("The result is",result)

    



