from functools import cmp_to_key

def run(board):
    pretty_print(board)
    units = parse_units(board)
    print(f"units: {units}")

    for unit in ordered_units(units):
        targets = find_targets(unit, units)
        adjacent_target = find_adjacent_target(unit, targets)

        #Attack
        if(adjacent_target):
            pass
        #Move
        else:
            tiles = find_candidate_tiles(targets, board)
            print(f"tiles: {tiles}")

def find_candidate_tiles(targets, board):
    s = set()

    for target in targets:
        tiles = [tile for tile in adjacent_positions(target.pos) if tile_is_empty(tile, board)]
        s.update(tiles)

    return s

def tile_is_empty(pos, board):
    x, y = pos
    return (
        x >= 0 and
        x < len(board[0]) and
        y >= 0 and
        y < len(board) and
        board[y][x] == '.'
    )

def adjacent_positions(pos):
    return [
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
    ]

def find_adjacent_target(hero, targets):
    all_adjacent = [unit for unit in targets if adjacent(hero.pos, unit.pos)]
    #Since sort is stable in Python, we do the tie breaker correctly
    return by_health(ordered_units(all_adjacent))[0] if len(all_adjacent) > 0 else None

def adjacent(a, b):
    return (a[0] == b[0] and (a[1] == b[1] - 1 or a[1] == b[1] + 1)) or (a[1] == b[1] and (a[0] == b[0] - 1 or a[0] == b[0] + 1))

def find_targets(hero, units):
    return [unit for unit in units if unit.elf != hero.elf]

def unit_order(a, b):
    return reading_order(a.pos, b.pos)

def reading_order(a, b):
    #If they are both on the same row, then use column as tie breaker
    if(a[1] == b[1]):
        return a[0] - b[0]
    else:
        return a[1] - b[1]

def by_health(units):
    return sorted(units, key=lambda u: u.hp)

def ordered_units(units):
    return sorted(units, key=cmp_to_key(unit_order))

def parse_units(board):
    units = []

    for y, row in enumerate(board):
        for x, char in enumerate(row):
            if(char == 'E' or char =='G'):
                units.append(Unit(char, (x, y)))

    return units

def pretty_print(board):
    for row in board:
        print(row)

class Unit:
    def __init__(self, symbol, pos):
        self.elf = symbol == 'E'
        self.pos = pos
        self.hp = 200

    def __repr__(self):
        return f"Elf?{self.elf}:{self.pos} HP: {self.hp}"
