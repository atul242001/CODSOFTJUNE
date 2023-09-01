contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("-------------------------")

def search_contact():
    search_term = input("Enter name or phone number to search for a contact: ")
    found = False
    for name, info in contacts.items():
        if search_term in (name, info['phone']):
            print(f"Contact found - Name: {name}, Phone: {info['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email: ")
        address = input("Enter the new address: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\nContact Manager Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
