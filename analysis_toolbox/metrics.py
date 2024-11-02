
def calculate_diversity_metrics(interactions):
    # Count the frequency of interactions with each contact node
    interaction_counts = defaultdict(int)
    for node in interactions:
        interaction_counts[node] += 1

    total_interactions = sum(interaction_counts.values())

    # Shannon Entropy
    shannon_entropy = 0
    for count in interaction_counts.values():
        p = count / total_interactions
        shannon_entropy -= p * math.log2(p) if p > 0 else 0

    # Simpson's Diversity Index
    simpson_index = 1
    for count in interaction_counts.values():
        p = count / total_interactions
        simpson_index -= p**2

    # General Diversity: Average of the two metrics
    general_diversity = (shannon_entropy + simpson_index) / 2

    return {
        'shannon_entropy': shannon_entropy,
        'simpson_index': simpson_index,
        'general_diversity': general_diversity
    }


