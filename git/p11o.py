def store_contact(name, number, contacts={}):
    contacts[name.lower()]=number
    return contacts

def phone_book():
    contacts={}
    while True:
        name=input("Enter name: ")
        number=input("Enter number: ")
        contacts=store_contact(name, number, contacts)
        user_choice=input('''
        Do you want to exit?
        1.Yes
        2.No
        ''')
        if user_choice=='1':
            return contacts
            
my_contact_book=phone_book()
# print(f"My contact book: {my_contact_book}")

def get_ph_no(name,contacts):
    return contacts.get(name.lower())

user_name=input("Enter a name to find a number: ")
print(get_ph_no(user_name,my_contact_book))
