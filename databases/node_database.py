class NodeDatabase:
    def __init__(self, file_path="nodes.csv"):
        self.nodes = {}
        self.file_path = file_path
        self.load_nodes()  # Load nodes from CSV if file exists

    def add_node(self, node_id, **attributes):
        if node_id not in self.nodes:
            self.nodes[node_id] = attributes
            self.save_nodes()
            print(f"Node {node_id} added.")
        else:
            print(f"Node {node_id} already exists.")

    def edit_node(self, node_id, **attributes):
        if node_id in self.nodes:
            self.nodes[node_id].update(attributes)
            self.save_nodes()
            print(f"Node {node_id} updated.")
        else:
            print(f"Node {node_id} does not exist.")

    def delete_node(self, node_id):
        if node_id in self.nodes:
            del self.nodes[node_id]
            self.save_nodes()
            print(f"Node {node_id} deleted.")
        else:
            print(f"Node {node_id} does not exist.")

    def save_nodes(self):
        with open(self.file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["node_id", "attributes"])
            for node_id, attributes in self.nodes.items():
                writer.writerow([node_id, attributes])

    def load_nodes(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    node_id = row[0]
                    attributes = eval(row[1])  # Convert string back to dictionary
                    self.nodes[node_id] = attributes
