from databases.contact_database import ContactDatabase

def add_contact(contact_db, contact_node, **details):
    contact_db.add_contact(contact_node, **details)

def edit_contact(contact_db, contact_index, **updated_details):
    contact_db.edit_contact(contact_index, **updated_details)

def delete_contact(contact_db, contact_index):
    contact_db.delete_contact(contact_index)
