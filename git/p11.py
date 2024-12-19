def phone_book():
    phone_book = {} 

    while True:
        name = input("Enter name or type 'exit' to stop: ")
        if name == "exit":
            break 

        phone_no = int(input("Enter phone number: "))  #
        phone_book[name] = phone_no  

        print(phone_book)  
    return phone_book
complete_ph_book=phone_book()
# print(f"Complete ph book: {complete_ph_book}")



