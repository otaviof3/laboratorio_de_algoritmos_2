def create_contact(phonebook,name,phone):
    if name in phonebook:
        phonebook[name].append(phone)
    else:
        phonebook[name] = [phone]
    return phonebook
def include_phone(phonebook,name,phone):
    if name not in phonebook:
        option_include = input("Do you want to add the requested name in the phonebook? (Type Yes if you do): ").capitalize()
        if option_include == "Yes":
            phonebook = create_contact(phonebook,name,phone)
        else:
            return phonebook
    else:
        phonebook[name].append(phone)
    return phonebook
def delete_phone(phonebook):
    delete_persons_phone = input("Person to delete a phone from: ").capitalize()
    if len(phonebook[delete_persons_phone]) == 1:
        print("Deleted person from phonebook")
        phonebook.pop(delete_persons_phone)
    else:
        delete_phone = int(input("Phone to delete: "))
        phonebook[delete_persons_phone].remove(delete_phone)
    return phonebook
def delete_contact(phonebook):
    delete_person = input("Person to delete from phonebook: ").capitalize()
    phonebook.pop(delete_person)
    return phonebook
def get_phones(phonebook):
    get_person = input("Which person's phone numbers to get: ").capitalize()
    print(phonebook.get(get_person))
def main(phonebook):
    try:
        while True:
            print("1. Create contact")
            print("2. Include phone")
            print("3. Delete phone")
            print("4. Delete contact")
            print("5. Get phones")
            print("Press any other number to leave")
            option = int(input("Type option (only numbers): "))
            if option == 1:
                name = input("Person name: ").capitalize()
                how_many = int(input("How many phones to register: "))
                for n in range(0,how_many):
                    phone = int(input("Phone number (only numbers): "))
                    phonebook = create_contact(phonebook,name,phone)
            elif option == 2:
                name = input("Person name: ").capitalize()
                phone = int(input("Phone to include: "))
                phonebook = include_phone(phonebook,name,phone)
            elif option == 3:
                phonebook = delete_phone(phonebook)
            elif option == 4:
                phonebook = delete_contact(phonebook)
            elif option == 5:
                get_phones(phonebook)
            else:
                break 
    except:
        print("Error, returning to start menu")
        main(phonebook)
phonebook = {}
main(phonebook)