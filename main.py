# Kaitlyn Spelling Bingo Card Plotter
# (C) 2026 Izvestiya, CC-BY-SA 4.0

import utl
import clusters as cl
import formatter as fmt
import argparse
import sys

# Command-line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('cluster', help='cluster file to load')
parser.add_argument('--format', default='github', help='output format')
parser.add_argument('--no-pretty', help='Disable decorated output and statistics, and just print the formatted table. Use this if you want to pipe the output to another program or file.', action='store_true', default=False)
parser.add_argument('--str-separator', default=', ', help='separator to use when format is set to "string"')
args = parser.parse_args()

# Main execution
if __name__ == "__main__":
    cluster_name = args.cluster.lower()
    cluster = cl.get_cluster(cluster_name)

    if not args.no_pretty:
        utl.separator(nl = False)
        print("Loaded cluster: ", cluster["pretty"] if "pretty" in cluster else cluster_name.capitalize() + " (no pretty name provided)")
        utl.separator()

    names, itr, count = cl.get_combos(cluster)
    formatted_table = fmt.format(names, cluster, format = args.format, string_separator = args.str_separator)

    if not args.no_pretty:
        print("Generated names:")
        print()

    print(formatted_table)

    if not args.no_pretty:
        utl.separator()
        print(f"Total names generated: {count}")
        utl.separator()