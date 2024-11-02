class EdgeDatabase:
    def __init__(self, file_path="edges.csv"):
        self.edges = []
        self.graph = nx.Graph()
        self.file_path = file_path
        self.load_edges()  # Load edges from CSV if file exists

    def add_edge(self, node1, node2, **attributes):
        if (node1, node2) not in self.edges and (node2, node1) not in self.edges:
            self.edges.append((node1, node2, attributes))
            self.graph.add_edge(node1, node2, **attributes)
            self.save_edges()
            print(f"Edge between {node1} and {node2} added.")
        else:
            print(f"Edge between {node1} and {node2} already exists.")

    def edit_edge(self, node1, node2, **attributes):
        for i, (n1, n2, attr) in enumerate(self.edges):
            if (n1 == node1 and n2 == node2) or (n1 == node2 and n2 == node1):
                self.edges[i] = (node1, node2, attributes)
                self.graph[node1][node2].update(attributes)
                self.save_edges()
                print(f"Edge between {node1} and {node2} updated.")
                return
        print(f"Edge between {node1} and {node2} does not exist.")

    def delete_edge(self, node1, node2):
        for i, (n1, n2, attr) in enumerate(self.edges):
            if (n1 == node1 and n2 == node2) or (n1 == node2 and n2 == node1):
                self.edges.pop(i)
                self.graph.remove_edge(node1, node2)
                self.save_edges()
                print(f"Edge between {node1} and {node2} deleted.")
                return
        print(f"Edge between {node1} and {node2} does not exist.")

    def save_edges(self):
        with open(self.file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["node1", "node2", "attributes"])
            for node1, node2, attributes in self.edges:
                writer.writerow([node1, node2, attributes])

    def load_edges(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    node1, node2 = row[0], row[1]
                    attributes = eval(row[2])  # Convert string back to dictionary
                    self.edges.append((node1, node2, attributes))
                    self.graph.add_edge(node1, node2, **attributes)

    def visualize_network(self, node_db):
        G = nx.Graph()
        
        # Adding nodes with attributes
        for node_id, attributes in node_db.nodes.items():
            G.add_node(node_id, **attributes)

        # Adding edges with attributes
        for node1, node2, attributes in self.edges:
            G.add_edge(node1, node2, **attributes)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
        
        # Displaying node and edge attributes
        node_labels = {node: f"{node}\n{attrs}" for node, attrs in node_db.nodes.items()}
        edge_labels = {(n1, n2): attrs for n1, n2, attrs in self.edges}
        
        nx.draw_networkx_labels(G, pos, labels=node_labels)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.show()
