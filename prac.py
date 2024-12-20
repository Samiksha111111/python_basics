def store_contacts(name, number, contacts={}):
    contacts[name.lower()]=number
    return contacts
def ph_book():
    contacts={}
    while True:
        name=input("Enter your name: ")
        number=input("Enter your number: ")
        contacts=store_contacts(name,number, contacts)
        user_choice=input('''
        Do you want to exit?
        1.Yes
        2.No
        ''')
        if user_choice=='1':
            return contacts
my_contacts=ph_book()

def get_ph_no(name,contacts):
    return contacts.get(name.lower())

user_name=input("Enter the name to find the number: ")
print(get_ph_no(user_name, my_contacts))


        