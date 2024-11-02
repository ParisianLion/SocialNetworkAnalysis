import networkx as nx
import matplotlib.pyplot as plt
from databases.node_database import NodeDatabase
from databases.edge_database import EdgeDatabase

def visualize_network(node_db, edge_db):
    G = nx.Graph()
    for node_id, attributes in node_db.nodes.items():
        G.add_node(node_id, **attributes)
    for node1, node2, attributes in edge_db.edges:
        G.add_edge(node1, node2, **attributes)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    plt.show()
