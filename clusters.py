# Kaitlyn Spelling Bingo Card Plotter
# (C) 2026 Izvestiya, CC-BY-SA 4.0

import json
import os
from itertools import product

# Load cluster data from the "clusters" directory
def get_cluster(cluster_name):
    cluster_path = os.path.join("clusters", f"{cluster_name}.cluster")

    if not os.path.isfile(cluster_path):
        raise FileNotFoundError(f"Cluster file '{cluster_path}' not found.")

    with open(cluster_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_combos(cluster, dedub = False):
    # Generate all combinations of the letter-swapping arrays
    combos = product(*cluster["clusters"])

    # Generate the names based on the combinations
    capitalize = cluster.get("capitalize", "first").lower()
    itr = 0
    names = []
    for combo in combos:
        result = cluster["name"]
        for i, part in enumerate(combo):
            result = result.replace(f"[{i}]", part)
        if capitalize == "first":
            result = result[0].upper() + result[1:] 
        elif capitalize == "strict":
            result = result.capitalize()
        names.append(result)
        itr += 1
    if dedub == True:
        names = set(names)  # Remove duplicates
    count = len(names)
    return names, itr, count