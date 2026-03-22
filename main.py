from itertools import product

import utl

utl.separator()
print("Kaitlyn Spelling Bingo Card Plotter")
print("(C) 2026 Izvestiya, CC-ND-BY-SA 4.0")
utl.separator(nl = True)

# Define letter-swapping arrays

name = "[0][1]t[2]l[3][4]"
clusters = [
    {
        "chars": ['k', 'c']
    },
    {
        "chars": ['a', 'ai', 'ae', 'ei', 'ay']
    },
    {
        "chars": ['e', '']
    },
    {
        "chars": ['i', 'y']
    },
    {
        "chars": ['n', 'nn']
    }
]

# Generate all combinations of the letter-swapping arrays
combos = product(*[c["chars"] for c in clusters])

# Generate the names based on the combinations
names = []
for combo in combos:
    result = name
    for i, part in enumerate(combo):
        result = result.replace(f"[{i}]", part)
    names.append(result)

utl.separator()
print("Generated names:")
print(", ".join(names))