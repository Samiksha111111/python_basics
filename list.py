#List:ordered,  mutable, allows duplicate elements
empty_list=[]
empty_list.append("apple")
empty_list.append("banana")
empty_list.append("cherry")
empty_list.append("grapes")

print(empty_list)
# for fruit in empty_list:
#     print(fruit)
for index, fruit in enumerate(empty_list):
    print(f"index {index} and value: {fruit}")