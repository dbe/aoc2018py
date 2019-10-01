import re

REGEX = r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>'

def run(lines):
    # lines = '''
    #     position=< 9,  1> velocity=< 0,  2>
    #     position=< 7,  0> velocity=<-1,  0>
    #     position=< 3, -2> velocity=<-1,  1>
    #     position=< 6, 10> velocity=<-2, -1>
    #     position=< 2, -4> velocity=< 2,  2>
    #     position=<-6, 10> velocity=< 2, -2>
    #     position=< 1,  8> velocity=< 1, -1>
    #     position=< 1,  7> velocity=< 1,  0>
    #     position=<-3, 11> velocity=< 1, -2>
    #     position=< 7,  6> velocity=<-1, -1>
    #     position=<-2,  3> velocity=< 1,  0>
    #     position=<-4,  3> velocity=< 2,  0>
    #     position=<10, -3> velocity=<-1,  1>
    #     position=< 5, 11> velocity=< 1, -2>
    #     position=< 4,  7> velocity=< 0, -1>
    #     position=< 8, -2> velocity=< 0,  1>
    #     position=<15,  0> velocity=<-2,  0>
    #     position=< 1,  6> velocity=< 1,  0>
    #     position=< 8,  9> velocity=< 0, -1>
    #     position=< 3,  3> velocity=<-1,  1>
    #     position=< 0,  5> velocity=< 0, -1>
    #     position=<-2,  2> velocity=< 2,  0>
    #     position=< 5, -2> velocity=< 1,  2>
    #     position=< 1,  4> velocity=< 2,  1>
    #     position=<-2,  7> velocity=< 2, -2>
    #     position=< 3,  6> velocity=<-1, -1>
    #     position=< 5,  0> velocity=< 1,  0>
    #     position=<-6,  0> velocity=< 2,  0>
    #     position=< 5,  9> velocity=< 1, -2>
    #     position=<14,  7> velocity=<-2,  0>
    #     position=<-3,  6> velocity=< 2, -1>
    # '''
    # lines = list(map(lambda str: str.strip(), lines.strip().split("\n")))

    lights = [list(map(int, parse(line))) for line in lines]
    for i in range(20000):
        print_lights(lights, i)


def bounding_box(positions):
    minx, miny, maxx, maxy = find_max(positions)

    return (maxx + 1, maxy + 1)

def transpose(positions):
    minx, miny, maxx, maxy = find_max(positions)

    return [(x - minx, y - miny) for (x, y) in positions]

def find_max(positions):
    minx = min([pos[0] for pos in positions])
    miny = min([pos[1] for pos in positions])
    maxx = max([pos[0] for pos in positions])
    maxy = max([pos[1] for pos in positions])

    return minx, miny, maxx, maxy

def print_lights(lights, time):
    positions = [(light[0] + light[2] * time, light[1] + light[3] * time) for light in lights]
    positions = transpose(positions)
    width, height = bounding_box(positions)

    if(width > 100 or height > 100):
        return

    data = [['.' for i in range(height)] for j in range(width)]

    for pos in positions:
        x, y = pos
        data[x][y] = 'X'

    for y in range(height):
        for x in range(width):
            print(data[x][y], end='')

        print()


def parse(line):
    return re.findall(REGEX, line)[0]
