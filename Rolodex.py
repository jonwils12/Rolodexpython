class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Rolodex:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print()

# Create a Rolodex instance
rolodex = Rolodex()

while True:
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Display Contacts")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contact = Contact(name, phone, email)
        rolodex.add_contact(contact)
        print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter name: ")
        contact = rolodex.search_contact(name)
        if contact:
            rolodex.remove_contact(contact)
            print("Contact removed successfully.")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name: ")
        contact = rolodex.search_contact(name)
        if contact:
            print("Contact found:")
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
        else:
            print("Contact not found.")

    elif choice == "4":
        rolodex.display_contacts()

    elif choice == "5":
        print("Exiting Rolodex. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
