# Kaitlyn Spelling Bingo Card Plotter
# (C) 2026 Izvestiya, CC-BY-SA 4.0

from tabulate import tabulate
import json

def extract_rows(pattern, names):
    rows = []
    col_len = len(names) // pattern
    for i in range(col_len):
        row = []
        for j in range(pattern):
            row.append(names[j * col_len + i])
        rows.append(row)
    return rows


def format(names, cluster, format = "github"):
    index_pattern = len(cluster["clusters"][0])
    rows = extract_rows(index_pattern, names)
    

    if format.lower() == "json":
        data = {"rows": rows, "cluster": cluster, "pretty": cluster["pretty"] if "pretty" in cluster else None}
        return json.dumps(data, indent=2)
    elif format.lower() == "csv":
        csv_data = ""
        for row in rows:
            csv_data += ",".join(row) + "\n"
        return csv_data

    headers = rows[0]
    del rows[0]
    return tabulate(rows, headers=headers, tablefmt=format)
    