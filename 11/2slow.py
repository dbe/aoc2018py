#Note: This is very unoptimized and takes a long time to run.
#I can use memoization while calculating each size square from a given point to reduce runtime by a factor of ~500
def run(lines):
    serial = int(lines[0])
    grid = [[power(x + 1, y + 1, serial) for y in range(300)] for x in range(300)]

    max_power = float('-inf')
    max_coords = (-1, -1)
    max_size = 0

    for y in range(300):
        for x in range(300):
            for size in range(1, 300):
                if(x + size > 300 or y + size > 300):
                    break

                p = grid_power(x, y, size, grid)

                if(p > max_power):
                    max_power = p
                    max_coords = (x, y)
                    max_size = size

    return (max_coords[0] + 1, max_coords[1] + 1, max_size)


def grid_power(x, y, size, grid):
    power = 0

    for j in range(y, y + size):
        for i in range(x, x + size):
            power += grid[i][j]

    return power

#Verbose to keep each line equivalent to a step in the problem description
#Using 1 indexed x and y
def power(x, y, serial):
    id = x + 10
    level = id * y
    level = level + serial
    level = level * id
    level = int(str(level)[-3])
    return level - 5

def test_power():
    assert(power(3,5,8) == 4)
    assert(power(122,79,57) == -5)
    assert(power(217,196,39) == 0)
    assert(power(101,153,71) == 4)

def test_run():
    assert(run(['18']) == (33, 45))
    assert(run(['42']) == (21, 61))
