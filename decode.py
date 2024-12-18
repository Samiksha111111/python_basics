alien_msg=" ?uoy era woH !namuH iH"
print(f"""Alian msg: {alien_msg}
Now, Human msg:{alien_msg[::-1]}""")

#resource allocation
available_foods=["apple", "banana", "chocolates",
                  "watermelon", "chatpate"
                  "cupcakes", "pizza", "burger", "pestries"
                  ]
available_crews=3
each_crew_food=len(available_foods)//available_crews
remaining_food_count=len(available_foods)%available_crews
print(f"Each crew get {each_crew_food} food and remaining food count={remaining_food_count}")

