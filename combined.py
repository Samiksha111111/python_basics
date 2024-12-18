def setup_mission():
    available_foods = [
        "apple", "banana", "chocolates",
        "watermelon", "chatpate",  
        "cupcakes", "pizza", "burger", "pastries"  
    ]
    available_crews = int(input("Enter available crews: "))
    return available_crews,available_foods
    
    


def alien_attack_game():
    print("Welcome to the alien attack game")
    print("Starting mission...... ")
    crew_no, foods=setup_mission() 
    print(f"You have {crew_no} astronuts and food available= {foods}") 
    print("Welcome to the mars!!!!")
    print("Your battery is dead, Please charge the battery")
    print("Mission completed")


alien_attack_game()
