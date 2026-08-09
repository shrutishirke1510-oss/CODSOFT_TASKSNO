contacts = []


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")

    for contact in contacts:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])
        print("--------------------")


def search_contact():
    search = input("Enter name or phone number to search: ").lower()

    found = False

    for contact in contacts:
        if search in contact["name"].lower() or search in contact["phone"]:
            print("\nContact found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    name = input("Enter the name of the contact to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contact["name"] = input("Enter new name: ")
            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")
            contact["address"] = input("Enter new address:")

            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        
