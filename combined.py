def setup_mission():
    available_foods = [
        "apple", "banana", "chocolates",
        "watermelon", "chatpate",  
        "cupcakes", "pizza", "burger", "pastries"  
    ]
    available_crews = int(input("Enter available crews: "))
    return available_crews,available_foods
    
#check batteries over hundred
def get_charged_batteries():
    batteries=[50,30,4,15,12,18,130]
    minimum_battery_power=20
    usable_battery_power=0
    usable_battery_count=0
    for battery in batteries:
        if battery>minimum_battery_power:
            usable_battery_power+=battery
            usable_battery_count+=1
            if usable_battery_power>=100:
                return usable_battery_power, usable_battery_count
            
def decrypt_alien_msg(alien_msg):
    human_msg=alien_msg[::-1]
    return human_msg

def food_divide_equally(foods, crew_members):
    equal_foods=len(foods)//crew_members
    remaining_food=len(foods)% crew_members
    return equal_foods, remaining_food

def alien_attack_game():
    print("Welcome to the alien attack game")
    print("Starting mission...... ")
    crew_no, foods=setup_mission() 
    print(f"You have {crew_no} astronuts and food available= {foods}") 
    print("Welcome to the mars!!!!")
    print("Your battery is dead, Please charge the battery")
    battery_power, battery_count=get_charged_batteries()
    print("Yay! Battery is charged..")
    print("Oops.. alien has arrived saying... ")
    print("rednerrus")
    decrypt_text=decrypt_alien_msg("rednerrus")
    print(f"Alien is saying: {decrypt_text}")
    print("Alien has captured all astronauts")
    print("If astronaut wants to escape they have to divide each food and give remaining foods")
    equal_foods, remaining_food=food_divide_equally(foods, crew_no)
    print(f"Each crew get {equal_foods} food and remaining food count={remaining_food}")                                # type: ignore
    print("Mission completed")


alien_attack_game()
