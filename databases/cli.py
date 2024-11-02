import argparse
import ast
from databases.node_database import NodeDatabase
from databases.edge_database import EdgeDatabase
from databases.contact_database import ContactDatabase
from editors.node_editor import add_node, edit_node, delete_node
from editors.edge_editor import add_edge, edit_edge, delete_edge
from editors.contact_editor import add_contact, edit_contact, delete_contact

# Initialize databases
node_db = NodeDatabase()
edge_db = EdgeDatabase()
contact_db = ContactDatabase()

def parse_csv(data):
    """Parse a CSV string into a list of values."""
    return [value.strip() for value in data.split(',')]

def main():
    parser = argparse.ArgumentParser(description="Social Network Analysis CLI")
    parser.add_argument("action", choices=["add", "update", "remove"], help="Action to perform")
    parser.add_argument("data_type", choices=["node", "edge", "contact"], help="Type of data to manipulate")
    parser.add_argument("data", help="CSV formatted data for the action")
    args = parser.parse_args()

    if args.data_type == "node":
        handle_node(args.action, args.data)
    elif args.data_type == "edge":
        handle_edge(args.action, args.data)
    elif args.data_type == "contact":
        handle_contact(args.action, args.data)

def handle_node(action, data):
    data = parse_csv(data)
    if action == "add":
        node_id, interests, occupation, study, institution, gender, age, nationality, comments = data
        add_node(
            node_db,
            node_id,
            interests=interests,
            occupation=occupation,
            study=study,
            institution=institution,
            gender=gender,
            age=age,
            nationality=nationality,
            comments=comments
        )
        print(f"Added node: {node_id}")
    elif action == "update":
        node_id, interests, occupation, study, institution, gender, age, nationality, comments = data
        edit_node(
            node_db,
            node_id,
            interests=interests,
            occupation=occupation,
            study=study,
            institution=institution,
            gender=gender,
            age=age,
            nationality=nationality,
            comments=comments
        )
        print(f"Updated node: {node_id}")
    elif action == "remove":
        node_id = data[0]
        delete_node(node_db, node_id)
        print(f"Removed node: {node_id}")

def handle_edge(action, data):
    data = parse_csv(data)
    if action == "add":
        node1, node2, attributes = data
        attributes = ast.literal_eval(attributes)  # Convert string to dict
        add_edge(edge_db, node1, node2, **attributes)
        print(f"Added edge between: {node1} and {node2}")
    elif action == "update":
        node1, node2, attributes = data
        attributes = ast.literal_eval(attributes)
        edit_edge(edge_db, node1, node2, **attributes)
        print(f"Updated edge between: {node1} and {node2}")
    elif action == "remove":
        node1, node2 = data[:2]
        delete_edge(edge_db, node1, node2)
        print(f"Removed edge between: {node1} and {node2}")

def handle_contact(action, data):
    data = parse_csv(data)
    if action == "add":
        contact_node, details = data
        details = ast.literal_eval(details)
        add_contact(contact_db, contact_node, **details)
        print(f"Added contact with: {contact_node}")
    elif action == "update":
        contact_node, details = data
        details = ast.literal_eval(details)
        edit_contact(contact_db, contact_node, **details)
        print(f"Updated contact with: {contact_node}")
    elif action == "remove":
        contact_node = data[0]
        delete_contact(contact_db, contact_node)
        print(f"Removed contact with: {contact_node}")

if __name__ == "__main__":
    main()
