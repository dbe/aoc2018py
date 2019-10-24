from collections import namedtuple
from datastructures import PriorityQueue
from functools import cmp_to_key

def run(board):
    board = parse_board(board)
    pretty_print(board)
    units = parse_units(board)

    while(True):
        for unit in ordered_units(units):
            targets = find_targets(unit, units)
            adjacent_target = find_adjacent_target(unit, targets)

            #Attack
            if(adjacent_target):
                pass
            #Move
            else:
                #All tiles which are adjacent to targets. Some may be unreachable
                tiles = find_candidate_tiles(targets, board)

                #All shortest paths to target tiles
                paths = reachable(unit, tiles, board)

                #If we don't have any reachable tiles, we can't do anything
                if(len(paths) == 0):
                    continue

                #The specific goal tile we want to head towards (tie broken by reading order)
                destination = determine_destination(paths)

                #The tile we will move to based on taking optimal path (tie broken by reading order first step)
                step = determine_step(unit.pos, destination, board)

                #Actually do the move
                move(unit, step, board)

                
                pretty_print(board)
                input()

def move(unit, step, board):
    x, y = unit.pos
    board[y][x] = '.'
    board[step[1]][step[0]] = unit.symbol

    unit.pos = step

def parse_board(board):
    return [list(row) for row in board]

#If there are multiple shortest paths from a to b, pick the one first in reading order
def determine_step(a, b, board):
    paths = []
    min_path = float('inf')
    tiles = [tile for tile in adjacent_positions(a) if tile_is_empty(tile, board)]

    for tile in tiles:
        path = find_path(tile, b, board)
        if(path):
            min_path = min(min_path, len(path))
            paths.append(path)

    tied = [path for path in paths if len(path) == min_path]

    steps = [path[0] for path in tied]

    return sorted(steps, key=cmp_to_key(reading_order))[0]

#Determines destination tile based on a list of shortest paths
def determine_destination(paths):
    dests = [path[-1] for path in paths]
    return sorted(dests, key=cmp_to_key(reading_order))[0]

#Returns the tile at pos. Takes into account y,x indexign into board
def tile_at_pos(pos, board):
    return board[pos[1]][pos[0]]

#Filter based on whether or not there exists a path between unit and goal tile
#Return all shortest paths
def reachable(unit, tiles, board):
    min_path = float('inf')
    paths_by_len = {}

    for tile in tiles:
        path = find_path(unit.pos, tile, board)
        if(path):
            min_path = min(min_path, len(path))
            paths = paths_by_len.get(len(path), [])
            paths.append(path)
            paths_by_len[len(path)] = paths

    return paths_by_len[min_path] if min_path in paths_by_len else []

#start, end are positions
def find_path(start, end, board):
    # return dfs([start], end, board, set())
    return dijkstra(start, end, board)

def dijkstra(start, end, board):
    Node = namedtuple("Node", ["pos", "d", "p"])
    seen = {}
    q = PriorityQueue()

    q.add(Node(start, 0, None), 0)
    while(len(q) > 0):
        cur = q.pop()
        if(cur.pos in seen):
            continue

        seen[cur.pos] = {'d': cur.d, 'p': cur.p}

        #Terminate early if we find the end
        if(cur.pos == end):
            break

        neighbors = [tile for tile in adjacent_positions(cur.pos) if (tile == end or tile_is_empty(tile, board))]
        for tile in neighbors:
            q.add(Node(tile, cur.d + 1, cur.pos), cur.d + 1)

    if(end not in seen):
        return None

    path = []
    current = end
    while(current is not None):
        path.insert(0, current)
        current = seen[current]['p']

    return path

#Not guarenteed to return optimal path
#Implemented as an excercise
def dfs(path, goal, board, seen):
    if(path[-1] == goal):
        return path
    elif(len(path) > 1 and tile_at_pos(path[-1], board) != '.'):
        return None
    elif(path[-1] in seen):
        return None
    else:
        seen.add(path[-1])
        for next in adjacent_positions(path[-1]):
            success = dfs([*path, next], goal, board, seen)
            if(success):
                return success

        return None

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
        print(''.join(row))

class Unit:
    def __init__(self, symbol, pos):
        self.symbol = symbol
        self.elf = symbol == 'E'
        self.pos = pos
        self.hp = 200

    def __repr__(self):
        return f"Elf?{self.elf}:{self.pos} HP: {self.hp}"
