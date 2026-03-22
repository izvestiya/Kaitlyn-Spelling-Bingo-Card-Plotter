import utl
import clusters as cl

cluster_name = "kaitlyn"
cluster = cl.get_cluster(cluster_name)

utl.separator(nl = False)
print("Kaitlyn Spelling Bingo Card Plotter")
print("(C) 2026 Izvestiya, CC-ND-BY-SA 4.0")
utl.separator()

print("Loaded cluster: ", cluster_name)
utl.separator()

names, itr = cl.get_combos(cluster)

print("Generated names:")
print(", ".join(names))
utl.separator()
print(f"Total names generated: {itr}")
