import json


class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact_id, name, phone_numbers, email):
        self.contacts[contact_id] = {
            'name': name,
            'phone number': phone_numbers,
            'email id': email
        }
        # self.display_contacts()
        self.add_data_to_file()

    def display_contacts(self):
        print(self.contacts)
        self.add_data_to_file()

    def add_data_to_file(self):
        with open('/content/sample_data/newDataFile.txt', 'w') as f:
            f.write(str(self.contacts))
            f.close()


c1 = ContactManager()
c1.add_contact(101, 'Abhishek', 12345, 'abhi@gmail.com')
c1.add_contact(102, 'JAyesh', 54311, 'jay@gmail.com')
c1.add_contact(103, 'Sammak', 696969, 'sammak@gmail.com')
c1.add_contact(104, 'Dhanooo', 65433, 'dhanu@gmail.com')
c1.add_contact(105, 'Bapat', 65456, 'bapat@gmail.com')
print(c1.contacts)
