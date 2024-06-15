import json
import os

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @staticmethod
    def from_dict(contact_dict):
        return Contact(
            contact_dict["name"],
            contact_dict["phone"],
            contact_dict["email"],
            contact_dict["address"]
        )

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                contacts_data = json.load(file)
                return [Contact.from_dict(contact) for contact in contacts_data]
        return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        self.save_contacts()
        return True  # Signal success

    def get_contacts(self):
        return self.contacts

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        return results

    def update_contact(self, name, new_name=None, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                self.save_contacts()
                return True  # Signal success
        return False  # Signal failure

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                return True  # Signal success
        return False  # Signal failure

### Main Function (Handling Printing)

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            if contact_book.add_contact(name, phone, email, address):
                print(f"Contact {name} added successfully!")
            else:
                print("Failed to add contact. Please try again.")
        elif choice == "2":
            contacts = contact_book.get_contacts()
            if not contacts:
                print("No contacts found.")
            else:
                for contact in contacts:
                    print(contact)
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(search_term)
            if not results:
                print("No contacts found.")
            else:
                for contact in results:
                    print(contact)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            if contact_book.update_contact(name, new_name, new_phone, new_email, new_address):
                print(f"Contact {name} updated successfully!")
            else:
                print("Contact not found.")
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            if contact_book.delete_contact(name):
                print(f"Contact {name} deleted successfully!")
            else:
                print("Contact not found.")
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
