from databases.contact_database import ContactDatabase
import matplotlib.pyplot as plt

def visualize_contact_log(contact_db):
    timestamps = [contact['timestamp'] for contact in contact_db.contacts]
    nodes = [contact['contact_node'] for contact in contact_db.contacts]
    
    plt.plot(timestamps, nodes, marker='o')
    plt.xlabel("Timestamp")
    plt.ylabel("Contact Node")
    plt.title("Contact Log")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
