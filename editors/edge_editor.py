from databases.edge_database import EdgeDatabase

def add_edge(edge_db, node1, node2, **attributes):
    edge_db.add_edge(node1, node2, **attributes)

def edit_edge(edge_db, node1, node2, **attributes):
    edge_db.edit_edge(node1, node2, **attributes)

def delete_edge(edge_db, node1, node2):
    edge_db.delete_edge(node1, node2)
