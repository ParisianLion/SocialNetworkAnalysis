import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from databases.node_database import NodeDatabase

def track_in_out_flow(node_db):
    # Initialize data structure to store weekly in/out changes
    weekly_in_out = {}

    # Assume `node_db.nodes` contains each node's "added_date" and "removed_date"
    for node_id, attributes in node_db.nodes.items():
        added_date = datetime.fromisoformat(attributes.get("added_date"))
        removed_date = attributes.get("removed_date")
        removed_date = datetime.fromisoformat(removed_date) if removed_date else None

        # Calculate weeks for added and removed dates
        added_week = added_date - timedelta(days=added_date.weekday())
        weekly_in_out.setdefault(added_week, {"in": 0, "out": 0})
        weekly_in_out[added_week]["in"] += 1

        if removed_date:
            removed_week = removed_date - timedelta(days=removed_date.weekday())
            weekly_in_out.setdefault(removed_week, {"in": 0, "out": 0})
            weekly_in_out[removed_week]["out"] += 1

    # Prepare data for plotting
    sorted_weeks = sorted(weekly_in_out.keys())
    weeks = [week.strftime("%Y-%m-%d") for week in sorted_weeks]
    in_counts = [weekly_in_out[week]["in"] for week in sorted_weeks]
    out_counts = [weekly_in_out[week]["out"] for week in sorted_weeks]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(weeks, in_counts, label="Added", marker="o", linestyle="-")
    plt.plot(weeks, out_counts, label="Lost", marker="x", linestyle="--")
    plt.xlabel("Week")
    plt.ylabel("Number of People")
    plt.title("Weekly In/Out Network Flow")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict
import math

def track_interaction_diversity(contact_db):
    # Step 1: Collate interactions weekly
    weekly_interactions = defaultdict(list)
    for contact in contact_db.contacts:
        timestamp = datetime.fromisoformat(contact['timestamp'])
        week_start = timestamp - timedelta(days=timestamp.weekday())
        week_start_str = week_start.strftime("%Y-%m-%d")
        weekly_interactions[week_start_str].append(contact['contact_node'])
    
    # Initialize lists to store diversity metrics
    weeks = sorted(weekly_interactions.keys())
    shannon_entropies = []
    simpson_indices = []
    general_diversity = []

    # Step 2: Calculate diversity metrics for each week
    for week in weeks:
        interactions = weekly_interactions[week]
        diversity_metrics = calculate_diversity_metrics(interactions)
        shannon_entropies.append(diversity_metrics['shannon_entropy'])
        simpson_indices.append(diversity_metrics['simpson_index'])
        general_diversity.append(diversity_metrics['general_diversity'])

    # Step 3: Plot general diversity over time
    plt.figure(figsize=(10, 6))
    plt.plot(weeks, general_diversity, label='General Diversity', marker='o')
    plt.xlabel('Week')
    plt.ylabel('Diversity Metric')
    plt.title('Interaction Diversity Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Plot individual diversity metrics
    plt.figure(figsize=(10, 6))
    plt.plot(weeks, shannon_entropies, label='Shannon Entropy', marker='o')
    plt.plot(weeks, simpson_indices, label='Simpson\'s Index', marker='x')
    plt.xlabel('Week')
    plt.ylabel('Diversity Metric')
    plt.title('Individual Diversity Metrics Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

