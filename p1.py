num=int(input("Enter a number: "))
while True:
    output=num*2
    output+=10
    a=(output/2)
    b=a-num
    result=b
    print(result)

    user_choice=input("do you want to continue?: ")

    if user_choice.lower()=="no":
        break
    
    
