def run(lines):
    c1 = 0
    c2 = 0

    for line in lines:
        a, b = get_counts(line)
        c1 += 1 if a else 0
        c2 += 1 if b else 0

    return c1 * c2

def get_counts(line):
    counts = {}

    for c in line:
        counts[c] = counts.get(c, 0) + 1

    v = counts.values()

    return (2 in v, 3 in v)
