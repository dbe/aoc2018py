from math import inf

import re

def run(lines):
    points = [parse(line) for line in lines]
    points = [(int(a),int(b)) for (a,b) in points]
    points = transpose(points)

    (_, maxx, _, maxy) = min_max(points)
    map = [[None] * (maxy + 1)] * (maxx + 1)

    for y in range(maxy + 1):
        for x in range(maxx + 1):

            for point in points:


    return "Oreo"


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
