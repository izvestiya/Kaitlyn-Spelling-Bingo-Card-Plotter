# Kaitlyn Spelling Bingo Card Plotter
# (C) 2026 Izvestiya, CC-ND-BY-SA 4.0

import utl
import clusters as cl
import argparse

# Command-line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('cluster', help='cluster file to load')
args = parser.parse_args()

# Main execution
if __name__ == "__main__":
    cluster_name = args.cluster
    cluster = cl.get_cluster(cluster_name)

    utl.separator(nl = False)
    print("Kaitlyn Spelling Bingo Card Plotter")
    print("(C) 2026 Izvestiya, CC-ND-BY-SA 4.0")
    utl.separator()

    print("Loaded cluster: ", cluster_name)
    utl.separator()

    names, itr, count = cl.get_combos(cluster)

    print("Generated names:")
    print(", ".join(names))
    utl.separator()
    print(f"Total names generated: {count}")
