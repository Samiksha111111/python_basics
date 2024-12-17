#*red-contains all the remaining items i.e being unpacked
# x=("apple")
# y=list(x)
# y[1]="kiwi"
# x=tuple(y)
# print(x)

#Tuples:ordered, immutable, allows duplicate elements
fruits = ["apple", "banana", "cherry","grapes"]
print(fruits[1])
(green,blue, *red)=fruits
print(green)
print(blue)
print(red)

