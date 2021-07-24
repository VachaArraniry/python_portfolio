import sqlite3

connection = sqlite3.connect('contactdb.db')
insert_contact = "INSERT INTO contacts (name, phone, address) VALUES ('{0}',{1},'{2}')"

contact_data_name = (input("Name : "))
contact_data_phone = (input("Phone : "))
contact_data_address = (input("Address : "))

cursor = connection.cursor()
cursor.execute(insert_contact.format(contact_data_name, contact_data_phone, contact_data_address))

connection.commit()

print(cursor.lastrowid)
