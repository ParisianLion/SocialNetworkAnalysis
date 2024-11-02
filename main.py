from databases.node_database import NodeDatabase
from databases.edge_database import EdgeDatabase
from databases.contact_database import ContactDatabase
from visualizations.network_visualizer import visualize_network
from visualizations.contact_log_visualizer import visualize_contact_log
from analysis_toolbox.analysis import track_in_out_flow, track_interaction_diversity, keyword_match_over_time

def main():
    # Initialize databases
    node_db = NodeDatabase()
    edge_db = EdgeDatabase()
    contact_db = ContactDatabase()

    # Run analysis functions
    print("Running in/out flow analysis...")
    track_in_out_flow(node_db)
    
    print("Running interaction diversity analysis...")
    track_interaction_diversity(contact_db)
    
    # Specify some keywords for keyword match analysis
    keywords = ["engineer", "hiking", "music", "teacher"]
    print(f"Running keyword match analysis with keywords: {keywords}")
    keyword_match_over_time(contact_db, node_db, keywords)

    # Run visualization functions
    print("Visualizing network...")
    visualize_network(node_db, edge_db)

    print("Visualizing contact log...")
    visualize_contact_log(contact_db)

if __name__ == "__main__":
    main()
