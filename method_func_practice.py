def display_menu():
    print("Contact Manager")
    print("1. View contacts")
    print("2. Add a new contact")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    if name in contacts:
        print("This contact already exists.")
    else:
        contacts[name] = phone
        print("Contact added successfully.")

def search_contact(contacts):
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("Press Enter to continue...")  # Pause for user to press Enter before continuing
        print()  # Add a new line for better readability in the loop

if __name__ == "__main__":
    main()
