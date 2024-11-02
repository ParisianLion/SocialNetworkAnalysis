
class ContactDatabase:
    def __init__(self, user_node="User", file_path="contacts.csv"):
        self.user_node = user_node
        self.contacts = []
        self.file_path = file_path
        self.load_contacts()  # Load contacts from CSV if file exists

    def add_contact(self, contact_node, timestamp=None, **details):
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        contact_event = {
            "user_node": self.user_node,
            "contact_node": contact_node,
            "timestamp": timestamp,
            **details
        }
        self.contacts.append(contact_event)
        self.save_contacts()
        print(f"Contact event with {contact_node} added at {timestamp}.")

    def edit_contact(self, contact_index, **updated_details):
        if 0 <= contact_index < len(self.contacts):
            self.contacts[contact_index].update(updated_details)
            self.save_contacts()
            print(f"Contact event at index {contact_index} updated.")
        else:
            print(f"Contact event at index {contact_index} does not exist.")

    def delete_contact(self, contact_index):
        if 0 <= contact_index < len(self.contacts):
            deleted_contact = self.contacts.pop(contact_index)
            self.save_contacts()
            print(f"Contact event with {deleted_contact['contact_node']} on {deleted_contact['timestamp']} deleted.")
        else:
            print(f"Contact event at index {contact_index} does not exist.")

    def save_contacts(self):
        with open(self.file_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["user_node", "contact_node", "timestamp", "details"])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({
                    "user_node": contact["user_node"],
                    "contact_node": contact["contact_node"],
                    "timestamp": contact["timestamp"],
                    "details": contact.get("details", "")
                })

    def load_contacts(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contact_event = {
                        "user_node": row["user_node"],
                        "contact_node": row["contact_node"],
                        "timestamp": row["timestamp"],
                        "details": eval(row["details"]) if row["details"] else {}
                    }
                    self.contacts.append(contact_event)

    def visualize_contacts(self):
        # Display each contact event in the log
        print("Contact Log:")
        for i, contact in enumerate(self.contacts):
            print(f"{i}: Contact with {contact['contact_node']} at {contact['timestamp']}, Details: {contact.get('details', {})}")
