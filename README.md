# Kaitlyn Spelling Bingo Card Plotter

There are **9,600 ways** to spell Kaitlyn. We know because we generated all of them.

This tool takes a name, breaks it down into its phonetic components, and produces every conceivable spelling variation via Cartesian product. Some of them are real names. Some of them are prescription medications. All of them are someone's legal name in Utah. Probably.

## Why

Because my friend's name is Katelyn. Or Kaitlyn. Or Caitlinn... Or some other variation. I still have no idea how it's spelled. And then it became a Python project at 01:00. On gin. As these things tend to do.

## Installation
```bash
git clone https://github.com/izvestiya/Kaitlyn-Spelling-Bingo-Card-Plotter.git
cd Kaitlyn-Spelling-Bingo-Card-Plotter
pip install tabulate
```

That's it. No virtual environment needed (Probably). It's a shitpost, not a microservice.

## Usage
```
py main.py <cluster> [--format <format>]
```

`<cluster>` is the name of a `.cluster` file in the `clusters/` directory, without the extension. `--format` is optional and defaults to `github` (GitHub-flavored markdown table).
```bash
py main.py kaitlyn                    # 9,600 variations, github markdown
py main.py mackenzie --format grid    # 240 variations, ASCII box table
py main.py natasha --format csv       # 144 variations, comma separated
py main.py rebecca --format json      # 144 variations, JSON dump
```

### Flags

| Flag | Default | Description |
|------|---------|-------------|
| `--format` | `github` | Output format. Supports all tabulate formats, plus `csv`, `json`, and `str`. |
| `--no-pretty` | `false` | Disables decorative output (separators, stats, cluster info). Useful when piping to a file or another command. |
| `--str-separator` | `, ` | Separator used when `--format str` is set. Default is comma-space. |

## How It Works

### The Template

Every name has a pattern. Kaitlyn breaks down like this:
```
K - AIT - L - Y - N
^   ^^^       ^   ^
```
these parts can be spelled differently

The tool represents this as a template string where swappable positions are numbered indices and fixed letters are literal:
```
[0][1]t[2]l[3][4]
 ^  ^   ^   ^  ^
 K  AI  E   Y  N
```

`[0]` means "insert whatever is in cluster 0 here." The `t` and `l` are fixed — they're always the same regardless of spelling.

### The Clusters

Each numbered position has an array of possible substitutions:

| Position | Options | What it represents |
|----------|---------|-------------------|
| `[0]` | `k`, `c` | The opening consonant |
| `[1]` | `a`, `ai`, `ae`, `ei`, `ay` | The first vowel sound |
| `[2]` | `e`, ` ` (nothing) | Optional middle vowel |
| `[3]` | `i`, `y` | The second vowel sound |
| `[4]` | `n`, `nn` | The ending consonant |

### The Math

The generator takes the Cartesian product of all clusters. Meaning every possible combination of one option from each cluster: `3 × 5 × 2 × 2 × 2 × 2 × 2 × 5 × 2 × 2 = 9,600` unique spellings


That's it. No machine learning. No AI. Just `itertools.product` and questionable life choices.

### The Output

Results are grouped into columns by the first cluster, so all K-spellings and C-spellings appear side by side:
```
| Kaitlyn   | Caitlyn   |
|-----------|-----------|
| Kaitlynn  | Caitlynn  |
| Kaitlin   | Caitlin   |
| ...       | ...       |
```

## Cluster File Format

Cluster files are JSON and live in the `clusters/` directory with a `.cluster` extension.
```json
{
    "pretty": "Kaitlyn",
    "name": "[0][1][2][3][4][5][6][7][8][9]",
    "capitalize": "first",
    "clusters": [
        ["k", "c", "q"],
        ["a", "ai", "ae", "ei", "ay"],
        ["", "gh"],
        ["t", "tt"],
        ["e", ""],
        ["", "-"],
        ["l", "ll"],
        ["y", "e", "i", "í", "a"],
        ["n", "nn"],
        ["", "e"]
    ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `pretty` | string | The canonical display name. Used in headers and output metadata. |
| `name` | string | The template string. Numbered indices `[0]`, `[1]`, etc. are replaced by cluster values. Literal characters are kept as-is. |
| `capitalize` | string | Capitalization mode. `"first"` uppercases the first letter only (default). `"strict"` uppercases the first letter and lowercases everything else. `"none"` disables capitalization entirely. |
| `clusters` | array of arrays | Each inner array corresponds to a numbered index in the template. The generator produces every combination across all arrays. |

### Template Rules

- `[0]`, `[1]`, `[2]`... are replaced by values from the corresponding cluster array
- Indices can be reused: `n[0]t[0]sha` uses cluster `0` in two positions (both resolve to the same value per combination)
- Literal characters outside brackets are fixed
- There is no limit on the number of clusters

### Writing Your Own Cluster

1. Pick a name
2. Break it into its fixed and variable parts
3. Figure out every plausible substitution for each variable part
4. Write the JSON
5. Drop it in `clusters/`
6. Question your life choices

Example: if you wanted to add "Sean":
```json
{
    "pretty": "Sean",
    "name": "[0][1][2]",
    "clusters": [
        ["s", "sh"],
        ["ea", "au", "aw"],
        ["n", "nn"]
    ]
}
```

This produces: Sean, Seann, Shaun, Shaunn, Shawn, Shawnn, Saun, Saunn, Sawn, Sawnn, Shaun, Shaunn... you get the idea.

## Included Clusters

| Cluster | Variations | Highlight |
|---------|-----------|-----------|
| Kaitlyn | 9,600 | The original sin |
| Jaiden | 80 | `jadynn` is a prescription medication |
| Ashley | 96 | `aeschleigh` is an elf |
| Megan | 480 | `maeghinn` is a Tolkien character |
| Natasha | 144 | `nahtahschiah` is an incantation |
| Rebecca | 144 | `ribbicckh` is a keyboard smash |
| Madison | 360 | `maeddyssynn` is it a Greek musician or a diagnosis? Do I call an ambulance?? |
| Brittany | 240 | `bryttynni` is a Norse rune |
| Mackenzie | 13,824 | `MiecXeanzzeie` is an elder god that bills $500/hr |
| Hailey | 35 | The only name with some restraint |
| Beth | 192 | `bbheethhe` 9 letters to spell a 4-letter name. Hyperinflation: 125% |
| KVIIIlyn | 960 | `CVIIIllynne` is it a name or a CPU register? |

## Output Formats

### Via tabulate

All `tabulate` formats are supported. Some useful ones:

| Format | Flag | Description |
|--------|------|-------------|
| GitHub Markdown | `--format github` | Default. Renders in GitHub READMEs. |
| ASCII Grid | `--format grid` | Box-drawing table for terminals. |
| Pipe | `--format pipe` | Markdown pipe tables. |
| Pretty | `--format pretty` | PrettyTable-style ASCII. |
| HTML | `--format html` | Raw HTML table. |
| LaTeX | `--format latex` | For the academically unhinged. |
| Simple | `--format simple` | Minimal, no borders. |

For the full list of ~36 supported tabulate formats, see the [tabulate documentation](https://github.com/astanin/python-tabulate#table-format).

### Custom formats

| Format | Flag | Description |
|--------|------|-------------|
| CSV | `--format csv` | Comma-separated. No headers. |
| JSON | `--format json` | Full dump including cluster metadata. |

## Adding Names

Drop a `.cluster` file in `clusters/`. If you can break a name into substitutable phonetic chunks, you can generate every spelling of it. We accept pull requests for names that have personally wronged you.

## License

CC-BY-SA 4.0

## Author

[Izvestiya](https://github.com/izvestiya)
