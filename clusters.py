import json
import os
from itertools import product

# Load cluster data from the "clusters" directory
def get_cluster(cluster_name):
    with open(os.path.join("clusters", f"{cluster_name}.cluster"), "r") as f:
        return json.load(f)

def get_combos(cluster):
    # Generate all combinations of the letter-swapping arrays
    combos = product(*cluster["clusters"])

    # Generate the names based on the combinations
    itr = 0
    names = []
    for combo in combos:
        result = cluster["name"]
        for i, part in enumerate(combo):
            result = result.replace(f"[{i}]", part)
        names.append(result)
        itr += 1
    return names, itr