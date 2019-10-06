import pytest
import os

def run(lines):
    cave = parse_lines(lines)
    #Also removes carts from the cave map
    carts = find_carts(cave)

    for i in range(100):
        pretty_print(cave, carts)
        tick(cave, carts)
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

def tick(cave, carts):
    #TODO: Make this use carts in the correct order
    for cart in carts:
        move_cart(cave, cart)

CORNER_MAPPING = {
    '\\': {
        '>': 'v',
        'v': '>',
        '<': '^',
        '^': '<'
    },
    '/': {
        '>': '^',
        'v': '<',
        '<': 'v',
        '^': '>'
    }
}

INTERSECTION_MAPPING = {
    'left': 'straight',
    'straight': 'right',
    'right': 'left'
}

TURN_MAPPING = {
    'left': {
        '>': '^',
        'v': '>',
        '<': 'v',
        '^': '<'
    },
    'straight': {
        '>': '>',
        'v': 'v',
        '<': '<',
        '^': '^'
    },
    'right': {
        '>': 'v',
        'v': '<',
        '<': '^',
        '^': '>'
    },
}

def move_cart(cave, cart):
    next_pos = get_next_pos(cart)
    tile = cave[next_pos[1]][next_pos[0]]

    #No need to change direction
    if(tile == '-' or tile == '|'):
        next_dir = cart['dir']
    #Corners
    elif(tile == '\\' or tile == '/'):
        next_dir = CORNER_MAPPING[tile][cart['dir']]
    #Intersections
    else:
        turn = cart['next_intersection']
        cart['next_intersection'] = INTERSECTION_MAPPING[turn]
        next_dir = TURN_MAPPING[turn][cart['dir']]

    cart['pos'] = next_pos
    cart['dir'] = next_dir

def get_next_pos(cart):
    if(cart['dir'] == '>'):
        return (cart['pos'][0] + 1, cart['pos'][1])
    elif(cart['dir'] == '<'):
        return (cart['pos'][0] - 1, cart['pos'][1])
    elif(cart['dir'] == 'v'):
        return (cart['pos'][0], cart['pos'][1] + 1)
    else:
        return (cart['pos'][0], cart['pos'][1] - 1)


def pretty_print(cave, carts):
    for y, line in enumerate(cave):
        for x, col in enumerate(line):
            carts_here = carts_at_pos((x, y), carts)
            if(len(carts_here) > 1):
                print('X', end='')
            elif(len(carts_here) == 1):
                print(carts_here[0]['dir'], end='')
            else:
                print(col, end='')

        print()

#Returns None if there are no carts, otherwise returns the carts
def carts_at_pos(pos, carts):
    return [cart for cart in carts if cart['pos'] == pos]

#Finds carts and replaces them with the underlying terrain
def find_carts(cave):
    carts = []

    for y, line in enumerate(cave):
        for x, tile in enumerate(line):
            if(is_cart(tile)):
                carts.append({'pos': (x, y), 'dir': tile, 'next_intersection': 'left'})
                cave[y][x] = '|' if (tile == 'v' or tile == '^') else '-'

    return carts

def is_cart(tile):
    return (
        tile == '>' or
        tile == '<' or
        tile == 'v' or
        tile == '^'
    )

def parse_lines(lines):
    return [list(line) for line in lines]

### TESTS ###
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
### TESTS ###

@pytest.fixture
def cave():
    with open('13/in.txt') as f:
        return parse_lines(f.read().strip().split('\n'))

# def test_tick(cave):
#     carts = find_carts(cave)

def test_get_next_pos():
    cart = {'pos': (1, 5), 'dir': '>'}
    assert(get_next_pos(cart) == (2, 5))

    cart = {'pos': (1, 5), 'dir': '<'}
    assert(get_next_pos(cart) == (0, 5))

    cart = {'pos': (1, 5), 'dir': '^'}
    assert(get_next_pos(cart) == (1, 4))

    cart = {'pos': (1, 5), 'dir': 'v'}
    assert(get_next_pos(cart) == (1, 6))



def test_carts_at_pos():
    carts = [
        {'pos': (2, 0), 'dir': '>'},
        {'pos': (9, 3), 'dir': 'v'},
        {'pos': (9, 3), 'dir': '^'}
    ]

    assert(carts_at_pos((2,0), carts) == [carts[0]])
    assert(carts_at_pos((9,3), carts) == [carts[1], carts[2]])

    assert(carts_at_pos((0,2), carts) == [] )
    assert(carts_at_pos((3,9), carts) == [] )
    assert(carts_at_pos((0,0), carts) == [] )

def test_find_carts(cave):
    carts = find_carts(cave)

    assert(len(carts) == 2)
    assert(carts[0] == {'pos': (2, 0), 'dir': '>', 'next_intersection': 'left'})
    assert(carts[1] == {'pos': (9, 3), 'dir': 'v', 'next_intersection': 'left'})

    #Indexing cave is with y, x.
    #Make sure we took out the carts from the cave diagram
    assert(cave[0][2] == '-')
    assert(cave[3][9] == '|')

def test_is_cart():
    assert( is_cart("<-") == False )
    assert( is_cart("-") == False )
    assert( is_cart("+") == False )
    assert( is_cart("\\") == False )
    assert( is_cart("/") == False )
    assert( is_cart("|") == False )

    assert( is_cart(">") == True )
    assert( is_cart("<") == True )
    assert( is_cart("v") == True )
    assert( is_cart("^") == True )
