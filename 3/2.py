import re

REGEX = r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)'

def run(lines):
    specs = parse(lines)
    invalid_ids = set()
    seen = {}

    for spec in specs:
        coords = spec_to_coords(spec)
        for coord in coords:
            if coord in seen:
                invalid_ids.add(spec[0])

                #If its the first time we saw a dupe
                if(seen[coord] != 'x'):
                    invalid_ids.add(seen[coord])
                    seen[coord] = 'x'
            else:
                seen[coord] = spec[0]

    ids = set([spec[0] for spec in specs])

    #set symmetric difference (disjoint)
    return ids ^ invalid_ids

def parse(lines):
    specs = [re.findall(REGEX, line)[0] for line in lines]
    return [(id, int(x), int(y), int(w), int(h)) for (id, x, y, w, h) in specs]

def spec_to_coords(spec):
    (_, x, y, w, h) = spec

    return [f"{i},{j}" for j in range(y, y + h) for i in range(x, x + w)]
