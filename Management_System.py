import re
import json

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}
        
    def user_interface (self):
        print("\nWelcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")
        
    def add_contact(self):
        unique_id = input("Enter a unique id (phone number or email): ")
        if unique_id in self.contacts:
            print("Sorry a contact with this id already exists.")
            return
        
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        additional_info = input("Additional information (address, notes): ")
        
        if self.validate_contact(unique_id, phone, email):
            self.contacts[unique_id] = {
                "Name": name,
                "Phone": phone,
                "Email": email,
                "Additional Info": additional_info
            }
            print("Contact added successfully.")
        else:
            print("Sorry invalid contact details. Please try again.")

    def edit_contact(self):
        unique_id = input("Enter the unique id of the contact to edit: ")
        
        if unique_id not in self.contacts:
            print("Contact not found.")
            return
        
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        additional_info = input("New additional information (address, notes): ")
        
        if self.validate_contact(unique_id, phone, email):
            self.contacts[unique_id] = {
                "Name": name,
                "Phone": phone,
                "Email": email,
                "Additional Info": additional_info
            }
            print("Contact updated successfully.")
        else:
            print("Sorry invalid contact details. Please try again.")

    def delete_contact(self):
        unique_id = input("Enter the unique id of the contact to delete: ")
       
        if unique_id in self.contacts:
            del self.contacts[unique_id]
            print("You contact deleted successfully.")
        else:
            print("Sorry contact was not found. Please try again")

    def search_contact(self):
        unique_id = input("Enter the unique id of the contact to search for: ")
        contact = self.contacts.get(unique_id)
        if contact:
            print("Contact details:")
            for key, value in contact.items():
                print(f"{key}: {value}")
        else:
            print("Contact not found.")

    def display_all_contacts(self):
        if not self.contacts:
            print("There are currently no contacts available.")
            return
        for unique_id, contact in self.contacts.items():
            print(f"\nUnique ID: {unique_id}")
            for key, value in contact.items():
                print(f"{key}: {value}")

    def export_contacts(self):
        filename = input("Enter the filename to export contacts to: ")
        
        try:
            with open(filename, 'w') as file:
                json.dump(self.contacts, file, indent=4)
            print("Your contacts  were exported successfully.")
        except Exception as e:
            print(f"Sorry an error occurred while exporting contacts: {e}. \nPlease try again.")

    def import_contacts(self):
        filename = input("Enter the filename to import contacts from: ")
       
        try:
            with open(filename, 'r') as file:
                imported_contacts = json.load(file)
                self.contacts.update(imported_contacts)
            print("Contacts imported successfully.")
        except Exception as e:
            print(f"Sorrry an error occurred while importing contacts: {e}. \nPlease try agian.")

    def validate_contact(self, unique_id, phone, email):
        phone_regex = re.compile(r"^\+?[1-9]\d{1,14}$")
        email_regex = re.compile(r"[^@]+@[..^@]+\.[^@]+")
        return phone_regex.match(phone) and email_regex.match(email)

    def run_code(self):
        while True:
            self.user_interface()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.edit_contact()
            elif choice == '3':
                self.delete_contact()
            elif choice == '4':
                self.search_contact()
            elif choice == '5':
                self.display_all_contacts()
            elif choice == '6':
                self.export_contacts()
            elif choice == '7':
                self.import_contacts()
            elif choice == '8':
                print("Quitting the Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cms = ContactManagementSystem()
    cms.run_code()
