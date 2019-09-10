import re

REGEX = r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)'

def run(lines):
    specs = parse(lines)
    seen = set()
    dupes = set()

    for spec in specs:
        coords = spec_to_coords(spec)
        for coord in coords:
            if coord in seen:
                dupes.add(coord)
            else:
                seen.add(coord)

    return len(dupes)

def parse(lines):
    specs = [re.findall(REGEX, line)[0] for line in lines]
    return [(id, int(x), int(y), int(w), int(h)) for (id, x, y, w, h) in specs]

def spec_to_coords(spec):
    (_, x, y, w, h) = spec

    return [f"{i},{j}" for j in range(y, y + h) for i in range(x, x + w)]
