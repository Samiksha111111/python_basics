num_list=[1,2,3,4,5,6,7,8,9]
def sum(*args):
    result=0
    for num in args:
        result+=num
    return result
print(sum(1,2,3,4,5))
    
num_list=[1,2,3,4,5,6,7,8,9]

def mul(*args):
    result=1
    for num in args:
        result*=num
    return result
print(mul(1,2,3,4,5))
    
def exponential():
    pass

def print_name(name="Samiksha"):
    print(f"Hello {name}")

print_name()
print_name(name="Sam")

# def print_full_name(**kwargs):
#     print(f"My name is {kwargs['fname']} {kwargs['lname']}")


# print_full_name(fname='Samiksha', lname='Magar', mname='none')

def print_result(*args, **kwargs):
    result=0
    for num in args:
        result+=num
    print(f"My name is {kwargs['fname']} {kwargs['lname']}")

print_result(10,20,30,40,50,fname='Samiksha', lname='Magar', mname='none')
