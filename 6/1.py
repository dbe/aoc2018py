from math import inf
from string import ascii_lowercase

import re

def run(lines):
    points = [parse(line) for line in lines]
    points = [(int(a),int(b)) for (a,b) in points]
    # points = [
    #     (1,1),
    #     (1,6),
    #     (8,3),
    #     (3,4),
    #     (5,5),
    #     (8,9)
    # ]
    points = transpose(points)
    (_, maxx, _, maxy) = min_max(points)

    #Build up map of points listing their closest Main Point
    #The purpose is to find which points are on the outer edge in order to disqualify them
    #Because they have infinite area
    map = [ [None for y in range(maxy + 1)] for x in range(maxx + 1)]
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            closest = inf

            for point in points:
                dist = manhattan(point, (x, y))
                if(dist < closest):
                    map[x][y] = points.index(point)
                    closest = dist
                elif(dist == closest):
                    map[x][y] = '.'

    edge_indices = get_edge_indices(map)
    valid_indices = set()
    for i in range(len(points)):
        if(i not in edge_indices):
            valid_indices.add(i)

    max_area = 0
    for index in valid_indices:
        area = count_area(map, index)
        if(area > max_area):
            max_area = area



    return max_area

def count_area(map, index):
    count = 0

    for col in map:
        for e in col:
            if(e == index):
                count += 1

    return count

def get_edge_indices(map):
    point_indices = set()

    for y in range(0, len(map[0])):
        for x in range(0, len(map)):
            #Top or bottom row
            if(y == 0 or y == len(map[0]) - 1):
                if(map[x][y] != '.'):
                    point_indices.add(map[x][y])
            #First or last column
            elif(x == 0 or x == len(map) - 1):
                if(map[x][y] != '.'):
                    point_indices.add(map[x][y])

    return point_indices

def pretty_print(map):
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
