from databases.node_database import NodeDatabase

def add_node(node_db, node_id, **attributes):
    node_db.add_node(node_id, **attributes)

def edit_node(node_db, node_id, **attributes):
    node_db.edit_node(node_id, **attributes)

def delete_node(node_db, node_id):
    node_db.delete_node(node_id)
