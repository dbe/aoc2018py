def run(lines):
    serial = int(lines[0])
    grid = [[power(x + 1, y + 1, serial) for y in range(300)] for x in range(300)]
    sums = sum_grid(grid)
    # pretty_print(grid, 5, 5)
    # print()
    # pretty_print(sums, 6, 6)
    answer = get_max(sums)
    return answer

def pretty_print(grid, width, height):
    for y in range(height):
        for x in range(width):
            print(grid[x][y], end=' ')

        print()


def get_max(sums):
    max_pow = float('-inf')
    max_x = -1
    max_y = -1
    max_size = -1

    for y in range(1, 301):
        for x in range(1, 301):
            for size in range(1, min(302-y, 302-x)):
                pow = sums_power(x, y, size, sums)

                if(pow > max_pow):
                    max_pow = pow
                    max_x = x
                    max_y = y
                    max_size = size

    return (max_x, max_y, max_size)

def sums_power(x, y, size, sums):
    return sums[x+size-1][y+size-1] - sums[x-1][y+size-1] - sums[x+size-1][y-1] + sums[x-1][y-1]

def sum_grid(grid):
    sums = [[0 for y in range(301)] for x in range(301)]
    for y in range(1, 301):
        for x in range(1, 301):
            sums[x][y] = grid[x-1][y-1] + sums[x-1][y] + sums[x][y-1] - sums[x-1][y-1]

    return sums


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
