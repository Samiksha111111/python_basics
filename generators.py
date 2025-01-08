# def natural_number():
#     n=1
#     while True:
#         yield n
#         n+=1
# gen=natural_number()
# for _ in range(10):
#     print(next(gen))

treasures=["Gole", "silver", "Gem"]
upper_treasure=[]
for treasure in treasures:
    upper_treasure.append(treasure.upper())
    #comprehension
capitalized_treasure=[treasure.upper() for treasure in treasures]
print(capitalized_treasure)
