import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Management System")
        
        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.master, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.master, text="Phone:")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5)
        self.entry_phone = tk.Entry(self.master)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.label_email = tk.Label(self.master, text="Email:")
        self.label_email.grid(row=2, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(self.master)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        self.label_address = tk.Label(self.master, text="Address:")
        self.label_address.grid(row=3, column=0, padx=5, pady=5)
        self.entry_address = tk.Entry(self.master)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.view_button = tk.Button(self.master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.search_button = tk.Button(self.master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.update_button = tk.Button(self.master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone_number = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if not phone_number.isdigit():
            messagebox.showerror("Error", "Phone number must contain only digits.")
            return
        elif len(phone_number) > 15:
            messagebox.showerror("Error", "Phone number must be 15 digits or fewer.")
            return

        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        messagebox.showinfo("Success", "Contact added successfully!")

        # Clear entry fields after adding contact
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Information", "Contact list is empty.")
            return

        contact_list = "Contact List:\n"
        for contact in self.contacts:
            contact_list += f"Name: {contact.name}, Phone: {contact.phone_number}\n"

        messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        search_query = self.entry_name.get().lower()
        if not search_query:
            messagebox.showinfo("Information", "Please enter a search query.")
            return

        found_contacts = [contact for contact in self.contacts if search_query in contact.name.lower() or search_query in contact.phone_number]
        if not found_contacts:
            messagebox.showinfo("Information", "No matching contacts found.")
            return

        search_results = "Search Results:\n"
        for contact in found_contacts:
            search_results += f"Name: {contact.name}, Phone: {contact.phone_number}\n"

        messagebox.showinfo("Search Results", search_results)

    def update_contact(self):
        search_query = self.entry_name.get().lower()
        if not search_query:
            messagebox.showinfo("Information", "Please enter the name of the contact to update.")
            return

        found_contacts = [contact for contact in self.contacts if search_query in contact.name.lower() or search_query in contact.phone_number]
        if not found_contacts:
            messagebox.showinfo("Information", "No matching contacts found.")
            return

        # For simplicity, assume only the first matching contact will be updated
        contact_to_update = found_contacts[0]

        # Prompt user for new details
        new_phone = self.entry_phone.get()
        new_email = self.entry_email.get()
        new_address = self.entry_address.get()

        if not new_phone.isdigit():
            messagebox.showerror("Error", "Phone number must contain only digits.")
            return
        elif len(new_phone) > 15:
            messagebox.showerror("Error", "Phone number must be 15 digits or fewer.")
            return

        # Update contact details
        contact_to_update.phone_number = new_phone
        contact_to_update.email = new_email
        contact_to_update.address = new_address

        messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self):
        search_query = self.entry_name.get().lower()
        if not search_query:
            messagebox.showinfo("Information", "Please enter the name of the contact to delete.")
            return

        found_contacts = [contact for contact in self.contacts if search_query in contact.name.lower() or search_query in contact.phone_number]
        if not found_contacts:
            messagebox.showinfo("Information", "No matching contacts found.")
            return

        # For simplicity, assume only the first matching contact will be deleted
        contact_to_delete = found_contacts[0]
        self.contacts.remove(contact_to_delete)
        messagebox.showinfo("Success", "Contact deleted successfully!")

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
