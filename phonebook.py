import json

phonebook = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phonebook.append({'name': name, 'phone': phone})
    print("Contact added.")

def view_contacts():
    if not phonebook:
        print("Phonebook is empty.")
        return
    for i, contact in enumerate(phonebook):
        print(f"{i + 1}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("Search by name or number: ").lower()
    found = False
    for contact in phonebook:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"{contact['name']} - {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    for contact in phonebook:
        if contact['name'].lower() == name.lower():
            new_name = input("Enter new name (press Enter to keep the same): ") or contact['name']
            new_phone = input("Enter new phone number (press Enter to keep the same): ") or contact['phone']
            contact['name'] = new_name
            contact['phone'] = new_phone
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(phonebook):
        if contact['name'].lower() == name.lower():
            del phonebook[i]
            print("Contact deleted.")
            return
    print("Contact not found.")

def sort_contacts():
    phonebook.sort(key=lambda contact: contact['name'].lower())
    print("Contacts sorted alphabetically by name.")

def save_to_file():
    filename = input("Enter filename to save (e.g., phonebook.json): ")
    with open(filename, 'w') as f:
        json.dump(phonebook, f)
    print("Phonebook saved.")

def load_from_file():
    global phonebook
    filename = input("Enter filename to load (e.g., phonebook.json): ")
    try:
        with open(filename, 'r') as f:
            phonebook = json.load(f)
        print("Phonebook loaded.")
    except FileNotFoundError:
        print("File not found.")

def menu():
    while True:
        print("\n📞 Phonebook Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Sort Contacts")
        print("7. Save to File")
        print("8. Load from File")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            sort_contacts()
        elif choice == '7':
            save_to_file()
        elif choice == '8':
            load_from_file()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    menu()
