import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QListWidget, QListWidgetItem
from main import ContactBook

class ContactBookGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.contact_book = ContactBook()  # Initialize your ContactBook instance

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Contact Book')
        self.setGeometry(100, 100, 600, 400)

        # Widgets
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()

        self.add_button = QPushButton('Add Contact')
        self.view_button = QPushButton('View Contacts')
        self.search_input = QLineEdit()
        self.search_button = QPushButton('Search')
        self.update_button = QPushButton('Update Contact')
        self.delete_button = QPushButton('Delete Contact')

        self.contact_list = QListWidget()

        # Layout
        main_layout = QVBoxLayout()

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel('Name:'))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel('Phone:'))
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(QLabel('Email:'))
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(QLabel('Address:'))
        form_layout.addWidget(self.address_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.view_button)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        action_layout = QHBoxLayout()
        action_layout.addWidget(self.update_button)
        action_layout.addWidget(self.delete_button)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.contact_list)
        main_layout.addLayout(action_layout)

        self.setLayout(main_layout)

        # Connect signals and slots
        self.add_button.clicked.connect(self.add_contact)
        self.view_button.clicked.connect(self.view_contacts)
        self.search_button.clicked.connect(self.search_contact)
        self.update_button.clicked.connect(self.update_contact)
        self.delete_button.clicked.connect(self.delete_contact)
        self.contact_list.itemClicked.connect(self.load_selected_contact)

    def add_contact(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()
        address = self.address_input.text().strip()

        if name and phone:  # Ensure name and phone are provided
            self.contact_book.add_contact(name, phone, email, address)
            self.clear_fields()
            self.view_contacts()
        else:
            self.show_message_box('Error', 'Name and Phone are required fields.')

    def view_contacts(self):
        self.contact_list.clear()
        contacts = self.contact_book.contacts
        for contact in contacts:
            item = QListWidgetItem(f'{contact.name} - {contact.phone}')
            self.contact_list.addItem(item)

    def search_contact(self):
        search_term = self.search_input.text().strip()
        if search_term:
            self.contact_list.clear()
            results = self.contact_book.search_contact(search_term)
            if not results:
                self.show_message_box('Search', 'No contacts found.')
            else:
                for contact in results:
                    item = QListWidgetItem(f'{contact.name} - {contact.phone}')
                    self.contact_list.addItem(item)
        else:
            self.show_message_box('Search', 'Please enter a search term.')

    def update_contact(self):
        current_item = self.contact_list.currentItem()
        if current_item:
            selected_text = current_item.text()
            name, phone = selected_text.split(' - ')[0], selected_text.split(' - ')[1]
            new_name = self.name_input.text().strip()
            new_phone = self.phone_input.text().strip()
            new_email = self.email_input.text().strip()
            new_address = self.address_input.text().strip()

            self.contact_book.update_contact(name, new_name, new_phone, new_email, new_address)
            self.clear_fields()
            self.view_contacts()
        else:
            self.show_message_box('Update', 'Please select a contact to update.')

    def delete_contact(self):
        current_item = self.contact_list.currentItem()
        if current_item:
            selected_text = current_item.text()
            name = selected_text.split(' - ')[0]
            self.contact_book.delete_contact(name)
            self.clear_fields()
            self.view_contacts()
        else:
            self.show_message_box('Delete', 'Please select a contact to delete.')

    def load_selected_contact(self, item):
        selected_text = item.text()
        name, phone = selected_text.split(' - ')[0], selected_text.split(' - ')[1]

        contacts = self.contact_book.contacts
        for contact in contacts:
            if contact.name == name and contact.phone == phone:
                self.name_input.setText(contact.name)
                self.phone_input.setText(contact.phone)
                self.email_input.setText(contact.email)
                self.address_input.setText(contact.address)
                break

    def clear_fields(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.address_input.clear()

    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactBookGUI()
    window.show()
    sys.exit(app.exec_())
