from math import inf
from string import ascii_lowercase

import re

def run(lines):
    # points = [parse(line) for line in lines]
    # points = [(int(a),int(b)) for (a,b) in points]
    points = [
        (1,1),
        (1,6),
        (8,3),
        (3,4),
        (5,5),
        (8,9)
    ]
    points = transpose(points)
    (_, maxx, _, maxy) = min_max(points)
    map = [[None] * (maxy + 1)] * (maxx + 1)

    for y in range(maxy + 1):
        for x in range(maxx + 1):
            closest = inf

            for point in points:
                dist = manhattan(point, (x, y))
                print(f"Dist from {x}, {y} to point is {dist}")
                if(dist < closest):
                    map[x][y] = points.index(point)
                    closest = dist
                elif(dist == closest):
                    map[x][y] = '.'

    pretty_print(map)
    return "Oreo"

def pretty_print(map):
    print(map)
    for y in range(0, len(map[0])):
        for x in range(0, len(map)):
            print(map[x][y], end='')

        print()


def parse(line):
    regex = r'(\d+), (\d+)'

    return re.findall(regex, line)[0]

def min_max(points):
    x = list(map(lambda point: point[0], points))
    y = list(map(lambda point: point[1], points))

    return (min(x), max(x), min(y), max(y))

def transpose(points):
    (minx, _, miny, _) = min_max(points)
    return [(x - minx, y - miny) for (x, y) in points]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
