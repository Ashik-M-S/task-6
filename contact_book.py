import sqlite3
bookdb = sqlite3.connect('contacts.db')
cursor = bookdb.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,phone TEXT NOT NULL,email TEXT
)''')
bookdb.commit()
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    bookdb.commit()
    print("Contact added successfully.")
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    if contacts:
        for contact in contacts:
            print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]} | Email: {contact[3]}")
    else:
        print("No contacts found.")
def update_contact():
    contact_id = input("Enter contact ID to update: ")
    name = input("Enter new name: ")
    phone = input("Enter new phone: ")
    email = input("Enter new email: ")
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
    bookdb.commit()
    print("Contact updated successfully.")
def delete_contact():
    contact_id = input("Enter contact ID to delete: ")
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    bookdb.commit()
    print("Contact deleted successfully.")
def menu():
    while True:
        print("\n--- Personal Contact Book ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
menu()
bookdb.close()
