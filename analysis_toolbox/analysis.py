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

