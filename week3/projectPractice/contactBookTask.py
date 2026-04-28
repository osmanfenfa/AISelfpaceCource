def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"{name} added successfully.\n")

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"\nName: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}\n")
    else:
        print("Contact not found.\n")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully.\n")
    else:
        print("Contact not found.\n")

def display_contacts(contacts):
    if not contacts:
        print("No contacts available.\n")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"{name} | Phone: {info['phone']} | Email: {info['email']}")
    print()


def main():
    contacts = {}
    while True:
        print("==== Contact Book ====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            display_contacts(contacts)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()